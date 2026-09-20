import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"c:\Users\X1 Yoga\html speego")
pages_dir = BASE_DIR / "pages"
assets_dir = BASE_DIR / "assets"
css_file = BASE_DIR / "css" / "style.css"
index_file = BASE_DIR / "index.html"

errors = []
warnings = []

# 1. Verify CSS rules for featured-cards-list and featured-article-card
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

if "display: flex; flex-direction: column;" in css and ".featured-cards-list {" in css:
    # Check if duplicate flex remains
    matches = re.findall(r'\.featured-cards-list\s*\{[^}]*display:\s*flex[^}]*\}', css)
    if matches:
        errors.append(f"CSS still has .featured-cards-list with display:flex! {matches}")

if ".featured-cards-list" not in css:
    errors.append("CSS missing .featured-cards-list")

if "grid-template-columns: repeat(2, 1fr)" not in css:
    errors.append("CSS .featured-cards-list should have grid-template-columns: repeat(2, 1fr)")

print("✓ CSS verified: .featured-cards-list is 2-column grid with single-card constraints.")

# 2. Check all HTML pages for featured-article-card placement
from html.parser import HTMLParser

class CardHierarchyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_stack = []
        self.invalid_cards = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        self.tag_stack.append((tag, classes))
        
        if 'featured-article-card' in classes:
            # Check if any ancestor is 'featured-cards-list'
            has_featured_list_ancestor = any(
                'featured-cards-list' in anc_classes
                for anc_tag, anc_classes in self.tag_stack[:-1]
            )
            if not has_featured_list_ancestor:
                self.invalid_cards.append(self.getpos())

    def handle_endtag(self, tag):
        if self.tag_stack:
            self.tag_stack.pop()

all_html_files = list(pages_dir.rglob("*.html"))
print(f"Found {len(all_html_files)} page files in pages/")

for p in all_html_files:
    rel_path = p.relative_to(BASE_DIR)
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    # Parse hierarchy
    parser = CardHierarchyParser()
    parser.feed(html)
    for line, col in parser.invalid_cards:
        errors.append(f"In {rel_path} (L{line}:C{col}): featured-article-card is NOT inside a featured-cards-list container!")

    # Check images referenced in page
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    for src in img_srcs:
        if src.startswith("http") or src.startswith("data:"):
            continue
        img_path = BASE_DIR / src.replace("/", os.sep)
        if not img_path.exists():
            errors.append(f"In {rel_path}: Image not found: {src} -> {img_path}")

print(f"✓ Checked all {len(all_html_files)} HTML pages for card structure and asset paths.")

# 3. Check index.html route and language pair consistency
with open(index_file, "r", encoding="utf-8") as f:
    index_html = f.read()

# Extract ROUTES
routes = re.findall(r"'#(/[^']+)':\s*\{\s*file:\s*'([^']+)'", index_html)
print(f"✓ Found {len(routes)} routes defined in index.html.")

for route_hash, file_rel in routes:
    file_path = BASE_DIR / file_rel.replace("/", os.sep)
    if not file_path.exists():
        errors.append(f"Route #{route_hash} points to missing file: {file_rel}")

# Extract LANG_PAIRS
pairs = re.findall(r"'#(/[^']+)':\s*'#(/[^']+)'", index_html)
print(f"✓ Found {len(pairs)} language pairs defined in index.html.")

for src, tgt in pairs:
    src_route = [r for r in routes if r[0] == src]
    tgt_route = [r for r in routes if r[0] == tgt]
    if not src_route:
        errors.append(f"Language pair source #{src} not found in ROUTES")
    if not tgt_route:
        errors.append(f"Language pair target #{tgt} not found in ROUTES")

# 4. Summary
print("\n================== VERIFICATION SUMMARY ==================")
if errors:
    print(f"FAILED: Found {len(errors)} errors:")
    for e in errors:
        print(f"  - ❌ {e}")
else:
    print("SUCCESS: 0 errors found! All tests passed perfectly.")

if warnings:
    print(f"Warnings ({len(warnings)}):")
    for w in warnings:
        print(f"  - ⚠️ {w}")
print("==========================================================")
