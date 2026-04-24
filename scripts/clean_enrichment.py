import re

# Comprehensive hand-verified mapping for all species in the original HTML
species_data = {
    # FISH
    "Ember Tetra": {"sci": "Hyphessobrycon amandae", "beh": "Community - Peaceful", "care": "Nano schooling fish. Requires stable parameters."},
    "Dragon Puffer": {"sci": "Pao palembangensis", "beh": "Solitary - Aggressive", "care": "Ambush predator. Needs hard-shelled food for beak health."},
    "Orange Platy": {"sci": "Xiphophorus maculatus", "beh": "Community - Peaceful", "care": "Hardy livebearer. Active and social."},
    "Black Moscow Guppy": {"sci": "Poecilia reticulata", "beh": "Community - Peaceful", "care": "Selective-bred strain. Prolific breeder."},
    "Kuhli Loach": {"sci": "Pangio kuhlii", "beh": "Community - Peaceful", "care": "Nocturnal bottom dweller. Needs sand and hiding spots."},
    "Endler's Livebearer": {"sci": "Poecilia wingei", "beh": "Community - Peaceful", "care": "Active, colorful nano fish. Very hardy."},
    "Playfair's Killifish": {"sci": "Pachypanchax playfairii", "beh": "Semi-Aggressive", "care": "Top-dweller. Known jumper—requires lid."},
    "Red-eye Puffer": {"sci": "Carinotetraodon irrubesco", "beh": "Semi-Aggressive", "care": "One of the more peaceful puffers, but can nip fins."},
    "Brichardi Cichlid": {"sci": "Neolamprologus brichardi", "beh": "Species Only (Colony)", "care": "Tanganyikan cichlid. Complex social hierarchy."},
    "Albino Bristlenose Pleco": {"sci": "Ancistrus cf. cirrhosus", "beh": "Community - Peaceful", "care": "Excellent algae eater. Needs driftwood to graze on."},
    "Jewel Cichlid": {"sci": "Hemichromis bimaculatus", "beh": "Species Only / Aggressive", "care": "Stunning red color. Highly territorial during breeding."},
    
    # HERPS / INVERTS
    "Baja California Tree Frogs": {"sci": "Pseudacris hypochondriaca", "beh": "Species Only - Communal", "care": "Arboreal. Needs high humidity and vertical space."},
    "Mediterranean House Gecko": {"sci": "Hemidactylus turcicus", "beh": "Species Only - Nocturnal", "care": "Hardy climber. Insectivore. Provide vertical hiding spots."},
    "Crayfish": {"sci": "Procambarus alleni / clarkii", "beh": "Species Only / Aggressive", "care": "Known to hunt small fish and uproot plants."},
    "Springtail Containers": {"sci": "Folsomia candida", "beh": "Community - Safe", "care": "Bioactive cleanup crew. Requires constant moisture."},
    "Isopod Containers": {"sci": "Porcellio scaber / Armadillidium", "beh": "Community - Safe", "care": "Bioactive cleanup crew. Provide leaf litter and calcium source."},
    "Ramshorn Snail": {"sci": "Planorbarius corneus", "beh": "Community - Peaceful", "care": "Excellent scavenger. Will not eat healthy plants."},
    "Malaysian Trumpet Snail": {"sci": "Melanoides tuberculata", "beh": "Community - Peaceful", "care": "Substrate-burrowing snail. Keeps sand aerated."},
    "Ghost Shrimp": {"sci": "Palaemonetes paludosus", "beh": "Community - Peaceful", "care": "Active scavenger. Great for nutrient export."},
    
    # PLANTS
    "Monstera Thai Constellation": {"sci": "Monstera deliciosa", "beh": "Plant - High Light", "care": "Stable variegation. Prone to root rot—needs airy mix."},
    "Monstera Albo": {"sci": "Monstera deliciosa var. borsigiana", "beh": "Plant - High Light", "care": "Unstable variegation. Needs bright indirect light."},
    "Philodendron billietiae": {"sci": "Philodendron billietiae", "beh": "Plant - Climbing", "care": "Distinctive orange petioles. Hardy aroid."},
    "Syngonium 'Santa Maria'": {"sci": "Syngonium podophyllum", "beh": "Plant - Climbing", "care": "Stunning pink/green variegation. Easy climber."},
    "Epipremnum 'Global Green'": {"sci": "Epipremnum aureum", "beh": "Plant - Trailing/Climbing", "care": "Deep green on green variegation. Very hardy."},
    "Cebu Blue Pothos": {"sci": "Epipremnum pinnatum 'Cebu Blue'", "beh": "Plant - Trailing/Climbing", "care": "Silvery-blue leaves. Fast grower with support."},
    "Monstera Peru": {"sci": "Monstera karstenianum", "beh": "Plant - Climbing", "care": "Highly textured, thick leaves. Requires support."},
    "Monstera dubia": {"sci": "Monstera dubia", "beh": "Plant - Shingling", "care": "Beautiful shingling plant. Needs a flat surface to climb."},
    "Rhaphidophora hayi": {"sci": "Rhaphidophora hayi", "beh": "Plant - Shingling", "care": "Hardy shingler. Best on a cedar or cork board."},
    "Duckweed": {"sci": "Lemna minor", "beh": "Plant - Floating", "care": "Fastest nutrient export. Provides shade for fish."},
}

html_path = 'fish-sale-repo/fish-room-sale.html'

with open(html_path, 'r') as f:
    content = f.read()

for common_name, data in species_data.items():
    # Targeted regex for common names
    pattern = rf'(<div class="species-common">[^<]*{re.escape(common_name)}[^<]*</div>\s*<div class="species-scientific">)[^<]*(</div>.*?<div class="species-detail">)[^<]*(</div>)'
    
    replacement = rf'\1{data["sci"]}\2**Compatibility:** {data["beh"]}<br>**Care:** {data["care"]}\3'
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL | re.IGNORECASE)

with open(html_path, 'w') as f:
    f.write(content)

print("Comprehensive clean enrichment complete.")
