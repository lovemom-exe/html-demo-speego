import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(r"c:\Users\X1 Yoga\html speego")
index_html = (BASE / "index.html").read_text(encoding="utf-8")

scripts = re.findall(r"<script>(.*?)</script>", index_html, flags=re.DOTALL)
print(f"Found {len(scripts)} inline scripts in index.html")

for i, s in enumerate(scripts):
    test_js = BASE / f"scratch/test_script_{i}.js"
    test_js.write_text(s, encoding="utf-8")
    res = subprocess.run(["node", "--check", str(test_js)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print(f"Script {i} SYNTAX ERROR:")
        print(res.stderr)
    else:
        print(f"Script {i} syntax is valid!")
