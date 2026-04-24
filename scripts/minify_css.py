import re
import os

def minify(html_path):
    with open(html_path, 'r') as f:
        content = f.read()

    def css_minifier(match):
        css = match.group(2)
        # Remove comments
        css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
        # Collapse whitespace
        css = re.sub(r'\s+', ' ', css)
        # Remove whitespace around special characters
        css = re.sub(r'\s*([{};:,])\s*', r'\1', css)
        return match.group(1) + css.strip() + match.group(3)

    new_content = re.sub(r'(<style>)(.*?)(</style>)', css_minifier, content, flags=re.DOTALL)
    
    with open(html_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    minify('fish-room-sale.html')
