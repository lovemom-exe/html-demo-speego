import urllib.request
import re

url = "https://speegoweb.vercel.app/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    print("Page title:", re.findall(r'<title>(.*?)</title>', html, re.I))
    css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html, re.I)
    print("CSS links:", css_links)
    
    # Check font imports
    fonts = re.findall(r'fonts\.googleapis\.com[^\'"]+', html)
    print("Fonts:", fonts)
    
    # Save first 2000 chars of HTML
    print("\n--- Snippet of head ---")
    head_match = re.search(r'<head>(.*?)</head>', html, re.S | re.I)
    if head_match:
        print(head_match.group(1)[:1500])
except Exception as e:
    print("Error:", e)
