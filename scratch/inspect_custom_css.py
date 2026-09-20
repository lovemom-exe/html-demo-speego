import urllib.request
import re

base_url = "https://speegoweb.vercel.app/"

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8', errors='ignore')

# Fetch speego-custom.css
try:
    custom_css = fetch(base_url + "wp-content/themes/logistica/css/speego-custom.css?v=mobile_workflow_timeline_20260918_25")
    print("--- custom_css snippet (first 1000 chars) ---")
    print(custom_css[:1000])
    
    # search for font-family, font-size, form, button in custom_css
    print("\n--- Search in custom_css ---")
    matches = re.findall(r'([^{}]+)\{([^}]+)\}', custom_css)
    for sel, body in matches:
        if any(k in sel.lower() for k in ['form', 'btn', 'input', 'consult', 'hero', 'heading', 'title', 'font', 'card']):
            print(f"Selector: {sel.strip()[:60]}")
            for line in body.strip().split(';'):
                if any(prop in line.lower() for prop in ['font', 'color', 'background', 'border', 'padding', 'margin', 'height', 'border-radius', 'letter-spacing']):
                    print(f"  {line.strip()}")
            print()
except Exception as e:
    print("Error fetching custom_css:", e)
