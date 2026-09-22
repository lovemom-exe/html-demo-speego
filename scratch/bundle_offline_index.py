import re
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(r"c:\Users\X1 Yoga\html speego")
index_path = BASE / "index.html"
index_content = index_path.read_text(encoding="utf-8")

# Extract all routes from pages/
route_files = set(re.findall(r"file:\s*'(pages/[^']+)'", index_content))

# Collect all files into bundle
bundle = {}
for p in ["partials/header.html", "partials/footer.html", "partials/cta-form.html"]:
    bundle[p] = (BASE / p).read_text(encoding="utf-8")

for f in sorted(route_files):
    file_p = BASE / f
    if file_p.exists():
        bundle[f] = file_p.read_text(encoding="utf-8")
    else:
        print(f"Warning: route file {f} does not exist!")

print(f"Total files in offline bundle: {len(bundle)}")

# Generate JS code for OFFLINE_BUNDLE with HTML script-tag-safe escaping
bundle_json = json.dumps(bundle, ensure_ascii=False).replace("<", "\\u003c")
offline_bundle_js = f"      // 1c. OFFLINE BUNDLE FOR FILE:/// PROTOCOL & ZERO-LATENCY BROWSING\n      const OFFLINE_BUNDLE = {bundle_json};\n"

# Replace fetchText in index_content
new_fetch_text = """      // 2. HELPER: FETCH WITH OFFLINE BUNDLE FALLBACK (file:/// & network offline)
      async function fetchText(url) {
        // Return from memory cache if available
        if (cache.pages && cache.pages[url]) {
          return cache.pages[url];
        }

        // Under local file:/// protocol, use offline bundle directly to prevent browser CORS block
        if (window.location.protocol === 'file:' && typeof OFFLINE_BUNDLE !== 'undefined' && OFFLINE_BUNDLE[url]) {
          return OFFLINE_BUNDLE[url];
        }

        try {
          const response = await fetch(url);
          if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
          }
          return await response.text();
        } catch (err) {
          if (typeof OFFLINE_BUNDLE !== 'undefined' && OFFLINE_BUNDLE[url]) {
            console.warn(`Fetch blocked or offline for [${url}], using embedded bundle fallback.`);
            return OFFLINE_BUNDLE[url];
          }
          console.error(`Error loading resource [${url}]:`, err);
          throw err;
        }
      }"""

# Find target location in index.html: right before `// In-memory cache for loaded partials and pages`
target_marker = "      // In-memory cache for loaded partials and pages"
if target_marker not in index_content:
    print("Error: Target marker not found in index.html!")
    sys.exit(1)

# Check if OFFLINE_BUNDLE already exists
start_marker = "      // 1c. OFFLINE BUNDLE FOR FILE:/// PROTOCOL & ZERO-LATENCY BROWSING"
if start_marker in index_content:
    prefix = index_content.split(start_marker)[0]
    suffix = index_content.split(target_marker)[1]
    index_content = prefix + offline_bundle_js + "\n" + target_marker + suffix
else:
    index_content = index_content.replace(target_marker, offline_bundle_js + "\n" + target_marker)

# Replace fetchText function
old_fetch_pattern = r"// 2\. HELPER: FETCH WITH TRY/CATCH\s*async function fetchText\(url\) \{.*?throw err;\s*\}\s*\}"
if re.search(old_fetch_pattern, index_content, flags=re.DOTALL):
    index_content = re.sub(old_fetch_pattern, new_fetch_text, index_content, flags=re.DOTALL)
    print("✓ Replaced fetchText successfully")
elif "HELPER: FETCH WITH OFFLINE BUNDLE FALLBACK" in index_content:
    print("✓ fetchText already using offline fallback")
else:
    print("Warning: old fetchText pattern did not match exactly, checking manual replacement")

index_path.write_text(index_content, encoding="utf-8")
print(f"✓ Updated index.html ({len(index_content):,} chars)")
