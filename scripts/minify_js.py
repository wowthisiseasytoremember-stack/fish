import re
import os

def minify(html_path):
    with open(html_path, 'r') as f:
        content = f.read()

    def js_minifier(match):
        js = match.group(2)
        # Remove single-line comments
        js = re.sub(r'//.*?\n', '\n', js)
        # Remove multi-line comments
        js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
        # Collapse whitespace
        js = re.sub(r'\s+', ' ', js)
        # Remove whitespace around special characters
        js = re.sub(r'\s*([{};:,=\(\)])\s*', r'\1', js)
        return match.group(1) + js.strip() + match.group(3)

    new_content = re.sub(r'(<script>)(.*?)(</script>)', js_minifier, content, flags=re.DOTALL)
    
    with open(html_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    minify('fish-room-sale.html')
