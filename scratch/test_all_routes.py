import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
routes_to_test = [
    '#/knowledge',
    '#/fulfillment',
    '#/sourcing',
    '#/tuyen-van-chuyen',
    '#/xuat-nhap-khau',
    '#/en/knowledge',
    '#/en/fulfillment',
    '#/en/sourcing',
    '#/en/shipping-routes',
    '#/en/import-export'
]

for r in routes_to_test:
    cmd = [
        edge_path,
        '--headless=new',
        '--disable-gpu',
        '--dump-dom',
        f'file:///c:/Users/X1 Yoga/html speego/index.html{r}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    dom = res.stdout
    if '<main id="app-main">' in dom:
        content = dom.split('<main id="app-main">')[1].split('</main>')[0]
        has_err = 'app-error-card' in content
        print(f"Route {r:22} -> Has Error: {str(has_err):5} | Length: {len(content):,} chars")
    else:
        print(f"Route {r:22} -> FAILED TO FIND APP-MAIN")
