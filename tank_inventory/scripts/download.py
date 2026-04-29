import re
import urllib.request
import os

url = "https://photos.app.goo.gl/4Lp7pFbvBaWEcyQ86"
save_dir = "/home/ichabod/photos/tank_inventory/"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching: {e}")
    exit(1)

# Look for the lh3.googleusercontent.com/pw/ links which are the high-res image sources
pattern = r'(https://lh3\.googleusercontent\.com/pw/[A-Za-z0-9_-]+)'
matches = re.findall(pattern, html)

# Deduplicate preserving order
unique_urls = []
for m in matches:
    if m not in unique_urls:
        unique_urls.append(m)

print(f"Found {len(unique_urls)} unique image base URLs.")

# Skip the first one as it is often a profile pic or album cover that's small
for i, base_url in enumerate(unique_urls):
    # Download at a reasonable resolution for analysis
    img_url = base_url + "=w1024"
    filename = f"{save_dir}photo{i+1:02d}.jpg"
    try:
        urllib.request.urlretrieve(img_url, filename)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
