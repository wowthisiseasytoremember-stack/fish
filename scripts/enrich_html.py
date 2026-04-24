import json
import bs4
import re
import os

# Load task data
with open('task_data.json', 'r') as f:
    task_data = json.load(f)

# Scientific Name Dictionary (fallback)
scientific_dict = {
    "Ember Tetra": "Hyphessobrycon amandae",
    "Dragon Puffer": "Pao palembangensis",
    "Orange Platy": "Xiphophorus maculatus",
    "Black Moscow Guppy": "Poecilia reticulata 'Black Moscow'",
    "Kuhli Loach": "Pangio kuhlii",
    "Endler's Livebearer": "Poecilia wingei",
    "Playfair's Killifish": "Pachypanchax playfairii",
    "Red-eye Puffer": "Carinotetraodon irrubesco",
    "Brichardi Cichlid": "Neolamprologus brichardi",
    "Golden Killifish": "Fundulus chrysotus",
    "Dwarf Cory": "Corydoras pygmaeus",
    "Shell Dweller Colony": "Neolamprologus multifasciatus",
    "Gardner's Killifish": "Fundulopanchax gardneri",
    "Albino Pleco": "Pterygoplichthys sp.",
    "American Flagfish": "Jordanella floridae",
    "Jewel Cichlid": "Hemichromis sp.",
    "Common Pleco": "Pterygoplichthys sp.",
    "Killifish": "Cyprinodontiformes sp.",
    "Baja California Tree Frog": "Pseudacris hypochondriaca",
    "California Tree Frog": "Pseudacris sierra",
    "Mediterranean House Gecko": "Hemidactylus turcicus",
    "Taricha Newt": "Taricha sp.",
    "Spanish Ribbed Newt": "Pleurodeles waltl",
    "Day Gecko": "Phelsuma sp.",
    "Crested Dalmatian Gecko": "Correlophus ciliatus",
    "Baby Brine Shrimp": "Artemia salina",
    "Red Swamp Crayfish": "Procambarus clarkii",
    "Marmorkrebs": "Procambarus virginalis",
    "Cajun Dwarf Crayfish": "Cambarellus shufeldtii",
    "Australian Red Claw Crayfish": "Cherax quadricarinatus",
    "Brazos Dwarf Crayfish": "Cambarellus texanus",
    "Isopods": "Armadillidium / Porcellio spp.",
    "Springtails": "Folsomia candida",
    "Electric Blue Crayfish": "Procambarus alleni",
    "Albino / Ghost Crayfish": "Procambarus sp. var. albino",
    "Louisiana Grass Shrimp": "Palaemonetes paludosus",
    "Java Moss": "Vesicularia dubyana",
    "Spiky Moss": "Taxiphyllum sp. 'Spiky'",
    "Riccia": "Riccia fluitans",
    "Hornwort": "Ceratophyllum demersum",
    "Susswassertang": "Lomariopsis lineata",
    "Epipremnum 'Lemon Lime'": "Epipremnum aureum 'Lemon Lime'",
    "Epipremnum pinnatum": "Epipremnum pinnatum",
    "Philodendron billietiae": "Philodendron billietiae",
    "Monstera Albo": "Monstera deliciosa 'Albo Variegata'",
    "E. pinnatum Albo Variegata": "Epipremnum pinnatum albo variegata",
    "Scindapsus pictus": "Scindapsus pictus",
    "Silver Sword Philodendron": "Philodendron hastatum 'Silver Sword'",
    "Syngonium 'Santa Maria'": "Syngonium podophyllum 'Santa Maria'",
    "Epipremnum 'Global Green'": "Epipremnum aureum 'Global Green'",
    "Cebu Blue Pothos": "Epipremnum pinnatum 'Cebu Blue'",
    "Monstera Peru": "Monstera karstenianum 'Peru'",
    "Monstera dubia": "Monstera dubia",
    "Rhaphidophora hayi": "Rhaphidophora hayi",
    "Monstera Thai Constellation": "Monstera deliciosa 'Thai Constellation'",
    "Scindapsus 'Thai Jade'": "Scindapsus sp. 'Thai Jade'",
    "Duckweed": "Lemna minor",
    "Lion's Mane Mushroom": "Hericium erinaceus"
}

# Helper to find matching task
def find_task(common_name):
    # Normalize common name
    clean_name = re.sub(r'\(.*?\)', '', common_name).strip().lower()
    
    best_match = None
    max_score = 0
    
    for filename, data in task_data.items():
        inv = data['inventory'].lower()
        score = 0
        # Check for keywords
        words = clean_name.split()
        for word in words:
            if word in inv:
                score += 1
        
        if score > max_score:
            max_score = score
            best_match = data
            
    return best_match

# Load HTML
with open('fish-sale-repo/fish-room-sale.html', 'r') as f:
    soup = bs4.BeautifulSoup(f, 'lxml')

species_cards = soup.find_all('div', class_='species-entry')

for card in species_cards:
    common_el = card.find('div', class_='species-common')
    if not common_el: continue
    
    common_name = common_el.get_text().strip()
    # Clean up name for matching (e.g. remove count)
    match_name = re.sub(r'\(.*?\)', '', common_name).strip()
    
    task = find_task(match_name)
    
    # Update Scientific Name
    sci_el = card.find('div', class_='species-scientific')
    if sci_el:
        sci_name = scientific_dict.get(match_name, "")
        if task and task['scientific_name'] and not sci_name:
            sci_name = task['scientific_name']
        
        if sci_name:
            # Check if it's already italicized by the class, or if we need <em>
            # User said: "italicized. Use Google if needed to confirm"
            # CSS already has font-style: italic.
            sci_el.string = sci_name

    # Update Details
    detail_el = card.find('div', class_='species-detail')
    if detail_el:
        if task:
            care = task['care_notes']
            comp = task['comp_notes']
            # Synthesize 3-4 sentences
            sentences = []
            if care: sentences.append(care)
            if comp: sentences.append(comp)
            
            # Combine and truncate/refine
            full_text = " ".join(sentences)
            # Basic cleanup: remove markdown bolding
            full_text = full_text.replace('**', '').replace('*', '')
            
            # Ensure it's roughly 3-4 sentences
            parts = re.split(r'\. ', full_text)
            final_text = ". ".join(parts[:4])
            if not final_text.endswith('.'): final_text += '.'
            
            detail_el.string = final_text

    # Update Pricing
    inquire_el = card.find('span', class_='badge-inquire')
    if inquire_el and task:
        pricing = task['pricing']
        # Clean up pricing string
        pricing = re.sub(r'- \*\*.*?\*\*:\s*', '', pricing)
        pricing = pricing.replace('**', '').replace('*', '')
        
        # Format as "Value: [Pricing] / Inquire"
        if pricing != "Inquire":
            inquire_el.string = f"Value: {pricing} / Inquire"
        else:
            inquire_el.string = "Inquire"

# Write back
# Use formatter to preserve layout as much as possible
with open('fish-sale-repo/fish-room-sale.html', 'w') as f:
    f.write(str(soup))
