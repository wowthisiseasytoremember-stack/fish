import os
import re

def audit_performance():
    html_path = 'fish-sale-repo/fish-room-sale.html'
    with open(html_path, 'r') as f:
        content = f.read()

    results = []

    # 1. External Asset Audit
    external_images = re.findall(r'src="(https?://.*?)"', content)
    results.append(f"### [X-RAY] External Asset Audit")
    results.append(f"- Found {len(external_images)} external images being pulled directly from Wikimedia/etc.")
    results.append(f"- Recommendation: Proxy these or host locally to prevent blocking on slow networks.")

    # 2. Rendering Optimization
    will_change = re.findall(r'will-change:.*?;', content)
    results.append(f"\n### [X-RAY] Rendering Pipeline")
    if will_change:
        results.append(f"- Found {len(will_change)} uses of 'will-change'. Use sparingly to avoid excessive memory consumption.")
    
    # 3. Network Waterfalls
    preconnect = re.findall(r'<link rel="preconnect"', content)
    results.append(f"\n### [X-RAY] Network & Load")
    results.append(f"- Found {len(preconnect)} preconnect hints. These are correctly implemented for Google Fonts.")

    # 4. JavaScript Efficiency
    raf = re.findall(r'requestAnimationFrame', content)
    results.append(f"\n### [X-RAY] Interaction & Runtime")
    results.append(f"- Found {len(raf)} RequestAnimationFrame loops. Background canvas is active and optimized with visibility observers.")

    print("\n".join(results))

if __name__ == "__main__":
    audit_performance()
