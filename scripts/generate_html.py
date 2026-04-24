import json
import re

def format_text(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    return text

def get_badges(text, details):
    combined = text.lower() + " " + " ".join(d.lower() for d in details)
    badges = []
    
    # Fish
    if any(w in combined for w in ['fish', 'tetra', 'guppi', 'pleco', 'cichlid', 'killifish', 'cory', 'puffer', 'loach', 'endler', 'platy']):
        badges.append(('fish', 'Fish'))
    # Herps
    if any(w in combined for w in ['gecko', 'frog', 'newt', 'reptile', 'herp', 'paludarium']):
        badges.append(('herps', 'Herps'))
    # Inverts
    if any(w in combined for w in ['shrimp', 'crayfish', 'scud', 'isopod', 'springtail', 'marmorkrebs']):
        badges.append(('inverts', 'Inverts'))
    # Plants
    if any(w in combined for w in ['plant', 'moss', 'monstera', 'epipremnum', 'philodendron', 'scindapsus', 'syngonium', 'hornwort', 'süsswassertang', 'riccia']):
        badges.append(('plants', 'Plants'))
        
    status = []
    if 'empty' in combined or 'drained' in combined:
        status.append(('empty', 'Empty'))
    elif 'under construction' in combined or 'half set up' in combined:
        status.append(('construction', 'Under Construction'))
    elif 'unconfirmed' in combined or 'tentative' in combined or 'tbd' in combined or 'unknown' in combined:
        status.append(('pending', 'Pending ID'))
    else:
        if not badges and any(w in combined for w in ['storage', 'tools', 'cables', 'empty', 'unused', 'bins']):
            pass
        else:
            status.append(('active', 'Active'))
            
    return badges, status

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def main():
    with open('parsed.json', 'r') as f:
        data = json.load(f)
        
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fish Room Tank Inventory</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b1326;
            --bg-glow: #0f2040;
            --teal: #00F0FF;
            --teal-dim: rgba(0, 240, 255, 0.15);
            --amber: #FFB000;
            --blue: #3b82f6;
            --purple: #a855f7;
            --green: #22c55e;
            --gray: #6b7280;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --glass-bg: rgba(11, 19, 38, 0.7);
            --glass-border: rgba(0, 240, 255, 0.2);
            --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        }
        
        * { box-sizing: border-box; }
        
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Space Grotesk', sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        /* Deep Water Background Gradient */
        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(circle at 50% 0%, var(--bg-glow) 0%, var(--bg-color) 70%, #050a14 100%);
            z-index: -2;
            pointer-events: none;
        }

        /* Bioluminescent Bubbles Animation */
        .bubbles {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            z-index: -1;
            pointer-events: none;
            overflow: hidden;
        }
        .bubble {
            position: absolute;
            bottom: -20px;
            background: radial-gradient(circle at 30% 30%, rgba(0, 240, 255, 0.4), rgba(0, 240, 255, 0.05));
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(0, 240, 255, 0.2), inset 0 0 10px rgba(0, 240, 255, 0.2);
            animation: rise infinite ease-in;
            opacity: 0;
        }
        @keyframes rise {
            0% { transform: translateY(0) translateX(0) scale(1); opacity: 0; }
            10% { opacity: 0.8; }
            50% { transform: translateY(-50vh) translateX(20px) scale(1.1); }
            90% { opacity: 0.5; }
            100% { transform: translateY(-100vh) translateX(-20px) scale(1.3); opacity: 0; }
        }

        /* Header / Stats Bar */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(11, 19, 38, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--glass-border);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        }

        h1 {
            margin: 0;
            font-size: 1.5rem;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 0 0 15px rgba(0, 240, 255, 0.6);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        h1::before {
            content: '';
            display: inline-block;
            width: 12px;
            height: 12px;
            background: var(--teal);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--teal);
        }

        .stats {
            display: flex;
            gap: 2rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .stat {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            color: var(--text-muted);
            font-size: 0.75rem;
        }
        .stat span {
            color: var(--teal);
            font-size: 1.2rem;
            font-weight: bold;
            text-shadow: 0 0 8px rgba(0, 240, 255, 0.4);
        }

        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        /* CSS Grid Room Map */
        .map-section {
            margin-bottom: 4rem;
        }
        
        .map-title {
            text-align: center;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }

        .room-map {
            display: grid;
            grid-template-columns: 1fr 2fr 1fr;
            grid-template-rows: 100px 200px 100px;
            gap: 1.5rem;
            padding: 2rem;
            background: rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px;
            position: relative;
        }

        .map-rack {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            color: var(--text-main);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(4px);
            padding: 1rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .map-rack::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, rgba(0,240,255,0.1) 0%, transparent 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .map-rack:hover {
            transform: translateY(-4px) scale(1.02);
            border-color: var(--teal);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.2), inset 0 0 15px rgba(0, 240, 255, 0.1);
            z-index: 10;
        }
        .map-rack:hover::before {
            opacity: 1;
        }
        
        .map-rack h3 {
            margin: 0;
            font-size: 1.1rem;
            color: #fff;
            font-family: 'Space Grotesk', sans-serif;
            text-shadow: 0 0 5px rgba(255,255,255,0.3);
            z-index: 1;
        }
        .map-rack p {
            margin: 0.5rem 0 0;
            font-size: 0.75rem;
            color: var(--teal);
            font-family: 'JetBrains Mono', monospace;
            text-transform: uppercase;
            z-index: 1;
        }

        /* Map Positioning */
        .wall-west { grid-column: 1 / 4; grid-row: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; background: transparent; border: none; padding: 0; }
        .wall-west .map-rack { width: 100%; height: 100%; }
        
        .wall-north { grid-column: 3; grid-row: 2; display: grid; grid-template-rows: 1fr 1fr; gap: 1rem; }
        
        .wall-east { grid-column: 1 / 4; grid-row: 3; }
        
        .wall-south { grid-column: 1; grid-row: 2; display: grid; grid-template-rows: 1fr 1fr; gap: 1rem; }
        
        .freestanding { grid-column: 2; grid-row: 2; border-color: var(--amber); }
        .freestanding h3 { color: var(--amber); }
        .freestanding p { color: var(--amber); }
        .freestanding:hover { border-color: var(--amber); box-shadow: 0 0 20px rgba(255, 176, 0, 0.2), inset 0 0 15px rgba(255, 176, 0, 0.1); }
        
        .corner-sw { position: absolute; bottom: 85px; left: 10px; width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; text-align: center; border: 1px dashed var(--teal); background: rgba(0,0,0,0.5); }
        .corner-sw h3 { font-size: 0.8rem; }

        /* Inventory Cards */
        .inventory-list {
            display: flex;
            flex-direction: column;
            gap: 2.5rem;
        }

        .rack-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            box-shadow: var(--glass-shadow);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            overflow: hidden;
            transition: all 0.4s ease;
            position: relative;
        }
        
        .rack-card:hover {
            border-color: rgba(0, 240, 255, 0.4);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 240, 255, 0.05);
        }

        .rack-card::after {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, var(--teal), transparent);
            opacity: 0.3;
        }

        .rack-header {
            background: rgba(0, 0, 0, 0.3);
            padding: 1.5rem 2.5rem;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .rack-header h2 {
            margin: 0;
            color: #fff;
            font-size: 1.4rem;
            letter-spacing: 1px;
        }
        
        .rack-misc {
            padding: 1rem 2.5rem;
            color: var(--text-muted);
            font-size: 0.9rem;
            font-style: italic;
            background: rgba(255,255,255,0.02);
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .rack-misc p { margin: 0.2rem 0; }

        .shelf {
            padding: 1.5rem 2.5rem;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            transition: background 0.2s ease;
        }
        .shelf:hover {
            background: rgba(0, 240, 255, 0.02);
        }
        .shelf:last-child {
            border-bottom: none;
        }
        .shelf h3 {
            margin: 0 0 1.2rem 0;
            color: var(--teal);
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .shelf h3::before {
            content: '';
            display: inline-block;
            width: 8px;
            height: 8px;
            background: var(--amber);
            border-radius: 1px;
            transform: rotate(45deg);
        }

        .tank-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1rem;
        }

        .tank-item {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 8px;
            padding: 1.2rem;
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .tank-item:hover {
            transform: translateY(-2px);
            border-color: rgba(255, 255, 255, 0.15);
            background: rgba(0, 0, 0, 0.6);
        }
        
        .tank-title {
            font-size: 1rem;
            line-height: 1.4;
            color: var(--text-main);
        }
        .tank-title strong {
            color: #fff;
            font-weight: 700;
        }
        .tank-title em {
            color: var(--teal);
            font-style: italic;
            opacity: 0.9;
        }
        
        .tank-details {
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
            padding-left: 0.8rem;
            border-left: 2px solid rgba(255,255,255,0.1);
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            line-height: 1.4;
        }

        .badges {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-top: auto;
            padding-top: 0.5rem;
        }
        .badge {
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.7rem;
            font-family: 'JetBrains Mono', monospace;
            text-transform: uppercase;
            font-weight: bold;
            letter-spacing: 0.5px;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
        }
        .badge::before {
            content: '';
            display: inline-block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
        }
        
        /* Category Badges */
        .badge.fish { background: rgba(59, 130, 246, 0.1); color: var(--blue); border: 1px solid rgba(59, 130, 246, 0.3); }
        .badge.fish::before { background: var(--blue); box-shadow: 0 0 5px var(--blue); }
        
        .badge.herps { background: rgba(255, 176, 0, 0.1); color: var(--amber); border: 1px solid rgba(255, 176, 0, 0.3); }
        .badge.herps::before { background: var(--amber); box-shadow: 0 0 5px var(--amber); }
        
        .badge.inverts { background: rgba(168, 85, 247, 0.1); color: var(--purple); border: 1px solid rgba(168, 85, 247, 0.3); }
        .badge.inverts::before { background: var(--purple); box-shadow: 0 0 5px var(--purple); }
        
        .badge.plants { background: rgba(34, 197, 94, 0.1); color: var(--green); border: 1px solid rgba(34, 197, 94, 0.3); }
        .badge.plants::before { background: var(--green); box-shadow: 0 0 5px var(--green); }
        
        /* Status Chips */
        .badge.empty { background: rgba(107, 114, 128, 0.1); color: var(--gray); border: 1px solid rgba(107, 114, 128, 0.3); }
        .badge.empty::before { background: var(--gray); }
        
        .badge.active { background: transparent; color: var(--teal); border: 1px dashed rgba(0, 240, 255, 0.4); }
        .badge.active::before { background: var(--teal); box-shadow: 0 0 5px var(--teal); }
        
        .badge.construction { background: transparent; color: var(--amber); border: 1px dashed rgba(255, 176, 0, 0.4); }
        .badge.construction::before { background: var(--amber); }
        
        .badge.pending { background: transparent; color: var(--text-muted); border: 1px dashed rgba(255,255,255,0.2); }
        .badge.pending::before { background: var(--text-muted); }

        @media (max-width: 768px) {
            .room-map {
                display: flex;
                flex-direction: column;
                height: auto;
            }
            .wall-west, .wall-north, .wall-south { display: flex; flex-direction: column; }
            .corner-sw { position: relative; bottom: 0; left: 0; width: 100%; height: auto; border-radius: 8px; padding: 1rem; }
            .stats { flex-direction: column; gap: 0.5rem; align-items: flex-end; }
            .stat { flex-direction: row; gap: 0.5rem; align-items: baseline; }
        }
    </style>
</head>
<body>
    <div class="bubbles" id="bubbles"></div>

    <header>
        <h1>Tank Inventory</h1>
        <div class="stats">
            <div class="stat">Total Tanks <span>~45</span></div>
            <div class="stat">Living Inhabitants <span>100+</span></div>
            <div class="stat">Species tracked <span>35+</span></div>
        </div>
    </header>

    <main>
        <section class="map-section">
            <h2 class="map-title">Room Layout (Top-Down)</h2>
            <div class="room-map">
                <!-- West Wall (Top) -->
                <div class="wall-west">
                    <a href="#west-wall-rack-6" class="map-rack">
                        <h3>Rack 6</h3>
                        <p>Paludarium / Jewel</p>
                    </a>
                    <a href="#west-wall-rack-7" class="map-rack">
                        <h3>Rack 7</h3>
                        <p>Crested Gecko</p>
                    </a>
                </div>
                
                <!-- North Wall (Right) -->
                <div class="wall-north">
                    <a href="#north-wall-rack-2-gray-rack" class="map-rack">
                        <h3>Rack 2</h3>
                        <p>Killifish / Puffers</p>
                    </a>
                    <a href="#north-wall-rack-3" class="map-rack">
                        <h3>Rack 3</h3>
                        <p>Dragon Puffer</p>
                    </a>
                </div>
                
                <!-- Entrance Wall (Bottom) -->
                <a href="#house-entrance-wall-rack-1-black-rack" class="map-rack wall-east">
                    <h3>Rack 1</h3>
                    <p>Entrance / Black Rack</p>
                </a>
                
                <!-- South Wall (Left) -->
                <div class="wall-south">
                    <a href="#south-wall-rack-5" class="map-rack">
                        <h3>Rack 5</h3>
                        <p>Killifish / UNS</p>
                    </a>
                    <a href="#south-wall-stand-1" class="map-rack">
                        <h3>Stand 1</h3>
                        <p>Flagfish</p>
                    </a>
                </div>
                
                <!-- Center -->
                <a href="#center-freestanding-rack-4" class="map-rack freestanding">
                    <h3>Rack 4</h3>
                    <p>High Plant Density</p>
                </a>
                
                <!-- SW Corner -->
                <a href="#south-west-corner-corner-stand" class="map-rack corner-sw">
                    <h3>Corner</h3>
                </a>
            </div>
        </section>

        <section class="inventory-list">
"""
    
    for rack in data:
        rack_id = slugify(rack['name'])
        html += f'''
            <article class="rack-card" id="{rack_id}">
                <div class="rack-header">
                    <h2>{format_text(rack['name'])}</h2>
                </div>'''
        
        if rack['misc']:
            html += '<div class="rack-misc">'
            for m in rack['misc']:
                html += f'<p>{format_text(m["text"])}</p>'
            html += '</div>'
            
        for shelf in rack['shelves']:
            html += f'''
                <div class="shelf">
                    <h3>{format_text(shelf['name'])}</h3>
                    <div class="tank-grid">'''
            
            for tank in shelf['tanks']:
                badges, status = get_badges(tank['text'], tank['details'])
                html += f'''
                        <div class="tank-item">
                            <div class="tank-title">{format_text(tank['text'])}</div>'''
                
                if tank['details']:
                    html += '<div class="tank-details">'
                    for detail in tank['details']:
                        html += f'<div>{format_text(detail)}</div>'
                    html += '</div>'
                
                if badges or status:
                    html += '<div class="badges">'
                    for b_type, b_label in badges:
                        html += f'<span class="badge {b_type}">{b_label}</span>'
                    for s_type, s_label in status:
                        html += f'<span class="badge {s_type}">{s_label}</span>'
                    html += '</div>'
                    
                html += '</div>'
            
            html += '''
                    </div>
                </div>'''
                
        html += '''
            </article>'''

    html += """
        </section>
    </main>

    <script>
        // Generate dynamic animated bubbles
        const bubblesContainer = document.getElementById('bubbles');
        const bubbleCount = Math.floor(window.innerWidth / 30); // scale with screen width
        
        for (let i = 0; i < bubbleCount; i++) {
            const bubble = document.createElement('div');
            bubble.classList.add('bubble');
            
            // Randomize properties for organic feel
            const size = Math.random() * 15 + 3; // 3px to 18px
            const left = Math.random() * 100; // 0vw to 100vw
            const duration = Math.random() * 12 + 6; // 6s to 18s rise
            const delay = Math.random() * 15; // 0s to 15s delay
            
            bubble.style.width = `${size}px`;
            bubble.style.height = `${size}px`;
            bubble.style.left = `${left}vw`;
            bubble.style.animationDuration = `${duration}s`;
            bubble.style.animationDelay = `${delay}s`;
            
            bubblesContainer.appendChild(bubble);
        }
    </script>
</body>
</html>
"""

    with open('tank-inventory.html', 'w') as f:
        f.write(html)
    print("Successfully generated tank-inventory.html")

if __name__ == '__main__':
    main()
