import os
import glob
import re

def process_files():
    files = glob.glob('/home/ichabod/fish-sale-repo/tank_tasks/*.md')
    listings = []
    
    for file_path in files:
        with open(file_path, 'r') as f:
            content = f.read()
            
        inventory = ""
        # Find everything under ## Inventory Entry until the next header or section
        inventory_match = re.search(r'## Inventory Entry\n(.*?)(?=\n##|\n---|#|$)', content, re.DOTALL)
        if inventory_match:
            inventory = inventory_match.group(1).strip()
            # Clean up leading dashes/bullets if present
            inventory = re.sub(r'^-\s*', '', inventory, flags=re.MULTILINE).strip()
        
        pricing = ""
        # Match - **Liquidation Pricing:** or - Liquidation Pricing:
        pricing_match = re.search(r'-\s*\**Liquidation Pricing:\**\s*(.*?)(?=\n-\s*\*|\n---|#|$)', content, re.DOTALL)
        if pricing_match:
            pricing = pricing_match.group(1).strip()
            
        care_notes = ""
        # Match - **Care Notes:** or - **Notes:** or similar
        care_notes_match = re.search(r'-\s*\**(Care Notes|Notes):\**\s*(.*?)(?=\n-\s*\*|\n---|#|$)', content, re.DOTALL)
        if care_notes_match:
            care_notes = care_notes_match.group(2).strip()
            
        # Skip if pricing is N/A or $0 and no care notes or inventory is just a location/misc
        if (not pricing or pricing.lower() == "n/a" or pricing == "$0") and (not care_notes or care_notes.lower() == "n/a"):
            continue
            
        # Categorization
        category = "Misc"
        lower_inventory = inventory.lower()
        title = os.path.basename(file_path).lower()
        
        # Amphibians keywords
        if any(x in lower_inventory or x in title for x in ["frog", "toad", "newt", "salamander", "axolotl"]):
            category = "Amphibians"
        # Inverts keywords
        elif any(x in lower_inventory or x in title for x in ["shrimp", "isopod", "springtail", "snail", "invert", "cherry", "blue dream", "crayfish", "crab", "clarkii", "quadricarinatus"]):
            category = "Inverts"
        # Fish keywords
        elif any(x in lower_inventory or x in title for x in ["fish", "tetra", "cory", "guppy", "killifish", "puffer", "platy", "betta", "rasbora", "shiner", "pao", "danio", "loach", "pleco", "cichlid", "endler", "medaka"]):
            category = "Fish"
        # Plants keywords
        elif any(x in lower_inventory or x in title for x in ["plant", "monstera", "philo", "epipremnum", "scindapsus", "syngonium", "rhaphidophora", "moss", "fern", "albo", "aureum", "pinnatum", "pictus", "karstenianum", "dubia", "hayi", "taxiphyllum", "buce", "anubias", "cryptocoryne"]):
            category = "Plants"
        # Equipment keywords
        elif any(x in lower_inventory or x in title for x in ["tank", "enclosure", "shelf", "tub", "jar", "bucket", "filter", "equipment", "light", "rack", "terrarium", "breeder", "cube", "rimless", "rimmed", "aio", "pump", "heater"]):
            category = "Equipment"
            
        listings.append({
            "category": category,
            "inventory": inventory,
            "pricing": pricing,
            "care_notes": care_notes,
            "source": os.path.basename(file_path)
        })
    
    return listings

def format_output(listings):
    categories = ["Fish", "Amphibians", "Inverts", "Plants", "Equipment", "Misc"]
    output = "# Sales Listings\n\n"
    output += "These are estimated prices for downsizing the current collection. All items are sold as-is. Prices are based on current market value for used equipment and livestock.\n\n"
    
    for cat in categories:
        cat_listings = [l for l in listings if l['category'] == cat]
        if not cat_listings:
            continue
            
        output += f"## {cat}\n\n"
        # Sort by inventory name
        cat_listings.sort(key=lambda x: x['inventory'])
        
        for item in cat_listings:
            output += f"### {item['inventory']}\n\n"
            output += f"**Pricing:**\n{item['pricing']}\n\n"
            if item['care_notes'] and item['care_notes'].lower() != "n/a":
                output += f"**Care Notes:**\n{item['care_notes']}\n\n"
            output += "---\n\n"
            
    return output

if __name__ == "__main__":
    listings = process_files()
    final_md = format_output(listings)
    with open('/home/ichabod/fish-sale-repo/sales-listings.md', 'w') as f:
        f.write(final_md)
    print(f"Processed {len(listings)} listings.")
