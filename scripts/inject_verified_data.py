import json
import re

def inject_data(json_path, html_path):
    with open(json_path, 'r') as f:
        verified_items = json.load(f)
    
    with open(html_path, 'r') as f:
        html_content = f.read()

    update_count = 0
    for item in verified_items:
        common = item['common_name']
        sci = item['scientific_name']
        beh = item['behavior']
        care = item['care']
        val = item['value']
        
        # Exact match pattern for the specific card based on its common name
        # We target the species-entry block containing the common name
        pattern = rf'(<div class="species-common">[^<]*{re.escape(common)}[^<]*</div>\s*<div class="species-scientific">)[^<]*(</div>.*?<div class="species-detail">)[^<]*(</div>)'
        
        # New detail block with clean data
        new_detail = f"**Compatibility:** {beh}<br>**Care:** {care}<br>**Value:** {val}"
        
        replacement = rf'\1{sci}\2{new_detail}\3'
        
        new_content, count = re.subn(pattern, replacement, html_content, flags=re.DOTALL | re.IGNORECASE)
        if count > 0:
            html_content = new_content
            update_count += 1
            
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    print(f"Successfully updated {update_count} cards in the HTML.")

if __name__ == "__main__":
    inject_data('verified_inventory.json', 'fish-sale-repo/fish-room-sale.html')
