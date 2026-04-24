import os
import re
from bs4 import BeautifulSoup

html_path = '/Users/justin/fish-sale-repo/fish-room-sale.html'
tasks_dir = '/Users/justin/fish-sale-repo/tank_tasks/'

def parse_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'# (?:Tank/Inhabitant|Misc Inventory) Task: (.*)', content)
    title = title_match.group(1).strip() if title_match else ""
    title = re.sub(r'[\*_]{1,2}', '', title)
    
    scientific_name = ""
    sci_match = re.search(r'\*([A-Z][a-z]+ [a-z]+(?:\s[a-z\']+)?)\*', content)
    if sci_match:
        scientific_name = sci_match.group(1)
    
    findings_section = content.split('## Findings')[-1].split('### Findings')[-1]
    
    compat_match = re.search(r'- \*\*Compatibility Audit:\*\*\s*(.*)', findings_section)
    pricing_match = re.search(r'- \*\*Liquidation Pricing:\*\*\s*(.*?)(?=- \*\*Care Notes:|$)', findings_section, re.DOTALL)
    care_match = re.search(r'- \*\*Care Notes:\*\*\s*(.*)', findings_section)
    
    compatibility = compat_match.group(1).strip() if compat_match else ""
    pricing_raw = pricing_match.group(1).strip() if pricing_match else ""
    care = care_match.group(1).strip() if care_match else ""
    
    price_range = ""
    # Look for $XX–$YY
    price_search = re.search(r'\$(\d+(?:–\d+)?(?:–\$\d+)?)', pricing_raw)
    if price_search:
        price_range = price_search.group(0)
    else:
        total_search = re.search(r'\*\*Total Estimate:\*\*\s*(\$[\d–]+)', pricing_raw)
        if total_search:
            price_range = total_search.group(1)

    return {
        'title': title,
        'scientific_name': scientific_name,
        'compatibility': compatibility,
        'pricing': price_range,
        'care': care,
        'file': os.path.basename(file_path)
    }

def categorize(task):
    title = task['title'].lower()
    content = (task['compatibility'] + task['care']).lower()
    
    fish_keywords = ['tetra', 'puffer', 'platy', 'guppy', 'loach', 'killifish', 'cory', 'cichlid', 'livebearer', 'danio', 'rasbora', 'baras']
    herp_keywords = ['frog', 'gecko', 'newt', 'snake', 'turtle', 'amphibian', 'reptile', 'terrarium', 'enclosure']
    invert_keywords = ['shrimp', 'crayfish', 'isopod', 'springtail', 'snail', 'marmorkrebs', 'crustacean']
    plant_keywords = ['moss', 'philodendron', 'monstera', 'epipremnum', 'scindapsus', 'syngonium', 'rhaphidophora', 'pothos', 'fern', 'mushroom', 'fungi', 'duckweed', 'hornwort', 'riccia', 'susswassertang', 'aroid']
    
    if any(k in title for k in fish_keywords): return 'fish'
    if any(k in title for k in herp_keywords): return 'herp'
    if any(k in title for k in invert_keywords): return 'invert'
    if any(k in title for k in plant_keywords): return 'plant'
    
    if 'tank' in title or 'filter' in title or 'light' in title or 'equipment' in title:
        return 'equipment'
        
    return 'equipment'

def synthesize_details(task):
    compat = task['compatibility']
    # Filter out obvious template errors
    if "Tropical plant species" in compat and categorize(task) in ['fish', 'herp', 'invert']:
        compat = ""
        
    para = f"{compat} {task['care']}".strip()
    sentences = re.split(r'(?<=[.!?])\s+', para)
    cleaned = [s.strip() for s in sentences if s.strip()]
    return " ".join(cleaned[:4])

def update_html():
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # We need to RESTORE the common names from data-search if they were lost
    # data-search often has "Common Name Scientific Name"
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    tasks = []
    for filename in sorted(os.listdir(tasks_dir)):
        if filename.endswith('.md'):
            tasks.append(parse_md_file(os.path.join(tasks_dir, filename)))
    
    # Mapping tasks to entries
    # Clean tasks list
    clean_tasks = []
    for t in tasks:
        # Extract name to match
        m = t['title'].replace('Inhabitants:', '').replace('Inhabitant:', '').replace('Equipment:', '').strip()
        m = re.sub(r'\s*\(.*?\)', '', m) # remove (x11) etc
        t['match_name'] = m.lower().rstrip('s')
        clean_tasks.append(t)
        
    ambiguous = []
    used_tasks = set()
    
    for entry in soup.find_all(class_='species-entry'):
        search_text = entry.get('data-search', '').lower()
        if not search_text: continue
        
        # Try to find a task that matches search_text
        best_task = None
        for t in clean_tasks:
            if t['match_name'] and t['match_name'] in search_text:
                best_task = t
                break
        
        if best_task:
            used_tasks.add(best_task['file'])
            # Update entry
            entry.find(class_='species-common').string = best_task['title']
            
            sci_el = entry.find(class_='species-scientific')
            if best_task['scientific_name']:
                sci_el.string = best_task['scientific_name']
            
            if not sci_el.get_text().strip():
                ambiguous.append(best_task['title'])
            
            detail_el = entry.find(class_='species-detail')
            if detail_el:
                detail_el.string = synthesize_details(best_task)
            
            badge_inquire = entry.find(class_='badge-inquire')
            if badge_inquire:
                if best_task['pricing']:
                    badge_inquire.string = f"Value: {best_task['pricing']} / Inquire"
                else:
                    badge_inquire.string = "Inquire"

    # Now handle unused tasks (new entries)
    for t in clean_tasks:
        if t['file'] in used_tasks: continue
        
        cat = categorize(t)
        if cat != 'equipment':
            list_id = f"{cat}-list"
            target_list = soup.find(id=list_id)
            if target_list:
                new_entry = soup.new_tag('div', attrs={'class': 'species-entry', 'data-search': f"{t['title']} {t['scientific_name']}"})
                info = soup.new_tag('div', attrs={'class': 'species-info'})
                
                common_div = soup.new_tag('div', attrs={'class': 'species-common'})
                common_div.string = t['title']
                info.append(common_div)
                
                sci_div = soup.new_tag('div', attrs={'class': 'species-scientific'})
                sci_div.string = t['scientific_name']
                if not sci_div.string:
                    ambiguous.append(t['title'])
                info.append(sci_div)
                
                badges = soup.new_tag('div', attrs={'class': 'species-badges'})
                care_badge = soup.new_tag('span', attrs={'class': 'badge-care badge-beginner'})
                care_badge.string = "Beginner"
                badges.append(care_badge)
                
                inquire_badge = soup.new_tag('span', attrs={'class': 'badge-inquire'})
                if t['pricing']:
                    inquire_badge.string = f"Value: {t['pricing']} / Inquire"
                else:
                    inquire_badge.string = "Inquire"
                badges.append(inquire_badge)
                info.append(badges)
                
                detail_div = soup.new_tag('div', attrs={'class': 'species-detail'})
                detail_div.string = synthesize_details(t)
                info.append(detail_div)
                
                new_entry.append(info)
                expand_icon = soup.new_tag('span', attrs={'class': 'species-expand-icon'})
                expand_icon.string = "▸"
                new_entry.append(expand_icon)
                target_list.append(new_entry)
        else:
            # Equipment
            found_eq = False
            for rack in soup.find_all(class_='rack-card'):
                rack_name = rack.find(class_='rack-name').get_text().lower()
                if ('tank' in t['title'].lower() and 'tank' in rack_name) or \
                   (('filter' in t['title'].lower() or 'light' in t['title'].lower()) and 'filtration' in rack_name):
                    
                    body = rack.find(class_='rack-body')
                    new_tank = soup.new_tag('div', attrs={'class': 'tank-entry'})
                    t_info = soup.new_tag('div', attrs={'class': 'tank-info'})
                    t_inhab = soup.new_tag('div', attrs={'class': 'tank-inhabitants'})
                    strong = soup.new_tag('strong')
                    strong.string = t['title']
                    t_inhab.append(strong)
                    if t['pricing']:
                        t_inhab.append(f" — Value: {t['pricing']}")
                    t_info.append(t_inhab)
                    t_eq = soup.new_tag('div', attrs={'class': 'tank-equipment'})
                    t_eq.string = t['care']
                    t_info.append(t_eq)
                    new_tank.append(t_info)
                    body.append(new_tank)
                    found_eq = True
                    break
            
            if not found_eq:
                misc_rack = None
                for rack in soup.find_all(class_='rack-card'):
                    if 'misc' in rack.find(class_='rack-name').get_text().lower():
                        misc_rack = rack
                        break
                if not misc_rack:
                    grid = soup.find(class_='racks-grid')
                    misc_rack = soup.new_tag('div', attrs={'class': 'rack-card', 'style': '--rack-color: var(--color-storage)'})
                    header = soup.new_tag('div', attrs={'class': 'rack-header'})
                    h_text = soup.new_tag('div', attrs={'class': 'rack-header-text'})
                    h_name = soup.new_tag('div', attrs={'class': 'rack-name'})
                    h_name.string = "Miscellaneous Equipment"
                    h_text.append(h_name)
                    header.append(h_text)
                    misc_rack.append(header)
                    body = soup.new_tag('div', attrs={'class': 'rack-body'})
                    misc_rack.append(body)
                    grid.append(misc_rack)
                
                body = misc_rack.find(class_='rack-body')
                new_tank = soup.new_tag('div', attrs={'class': 'tank-entry'})
                t_info = soup.new_tag('div', attrs={'class': 'tank-info'})
                t_inhab = soup.new_tag('div', attrs={'class': 'tank-inhabitants'})
                strong = soup.new_tag('strong')
                strong.string = t['title']
                t_inhab.append(strong)
                if t['pricing']:
                    t_inhab.append(f" — Value: {t['pricing']}")
                t_info.append(t_inhab)
                t_eq = soup.new_tag('div', attrs={'class': 'tank-equipment'})
                t_eq.string = t['care']
                t_info.append(t_eq)
                new_tank.append(t_info)
                body.append(new_tank)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
    if ambiguous:
        print("\nItems with ambiguous or missing scientific names:")
        for item in sorted(list(set(ambiguous))):
            print(f"- {item}")

if __name__ == "__main__":
    update_html()
