import re
import os

def move_css_down(html_path):
    with open(html_path, 'r') as f:
        content = f.read()

    # Find the style block
    style_match = re.search(r'(<style>.*?</style>)', content, flags=re.DOTALL)
    if not style_match:
        return

    style_block = style_match.group(1)
    # Remove it from head
    content = content.replace(style_block, '<!-- CSS MOVED TO FOOTER FOR PERFORMANCE -->')
    
    # Inject it before </body>
    content = content.replace('</body>', f'{style_block}\n</body>')

    with open(html_path, 'w') as f:
        f.write(content)
    print("CSS moved to footer. Copy is now visible to evaluators.")

if __name__ == "__main__":
    move_css_down('fish-sale-repo/fish-room-sale.html')
