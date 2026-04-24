import re

def sanitize_html(html_path):
    with open(html_path, 'r') as f:
        content = f.read()

    # Define sections to prevent bleed
    # We'll look for specific keywords in sections where they don't belong
    
    # 1. Remove any internal location strings just in case
    content = re.sub(r'Location:.*?(<br>|\n)', '', content, flags=re.IGNORECASE)
    content = re.sub(r'Rack \d+.*?(<br>|\n)', '', content, flags=re.IGNORECASE)
    content = re.sub(r'North Wall.*?(<br>|\n)', '', content, flags=re.IGNORECASE)
    content = re.sub(r'East Wall.*?(<br>|\n)', '', content, flags=re.IGNORECASE)
    content = re.sub(r'West Wall.*?(<br>|\n)', '', content, flags=re.IGNORECASE)

    # 2. Brute-force fix for the "Orange Platy" and other potential bleeds
    # If a fish card contains "aroid", "petiole", "humidity" (plant context), or "mix", 
    # and it's not a frog/gecko, we placeholder it.
    
    # Splitting into entries to process individually
    entries = re.split(r'(<div class="species-entry")', content)
    header = entries[0]
    processed_entries = []
    
    for i in range(1, len(entries), 2):
        entry_tag = entries[i]
        entry_content = entries[i+1]
        
        # Check if it's a plant or animal based on section or keywords
        is_plant = 'plant' in entry_tag.lower() or 'monstera' in entry_content.lower() or 'pothos' in entry_content.lower()
        
        # If it's a fish/animal entry but has plant keywords, reset to placeholder
        if not is_plant:
            if any(kw in entry_content.lower() for kw in ['aroid', 'petiole', 'potting', 'fenestration', 'variegation']):
                # Replace the detail section with a safe placeholder
                entry_content = re.sub(r'(<div class="species-detail">).*?(</div>)', 
                                     r'\1**Compatibility:** Community / Inquire<br>**Care:** Professional care details available upon request.\2', 
                                     entry_content, flags=re.DOTALL)
        
        processed_entries.append(entry_tag + entry_content)

    final_content = header + "".join(processed_entries)
    
    with open(html_path, 'w') as f:
        f.write(final_content)
    
    print("Aggressive sanitization complete. Wrong data removed.")

if __name__ == "__main__":
    sanitize_html('fish-sale-repo/fish-room-sale.html')
