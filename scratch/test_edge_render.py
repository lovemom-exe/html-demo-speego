import subprocess
import time
import http.server
import socketserver
import threading
import os

PORT = 8989

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=r'c:\Users\X1 Yoga\html speego', **kwargs)

httpd = socketserver.TCPServer(('', PORT), Handler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()
time.sleep(1)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    '--dump-dom',
    f'http://localhost:{PORT}/index.html#/fulfillment'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
output = res.stdout

if 'SpeeGo Fulfillment' in output:
    print('SUCCESS: SpeeGo Fulfillment rendered in DOM!')
elif 'app-error-card' in output:
    print('ERROR SCREEN RENDERED!')
    # Print error details
    for line in output.splitlines():
        if 'app-error' in line or 'Chi tiết kỹ thuật' in line:
            print('  ->', line.strip())
else:
    print('Neither fulfillment nor error found. Length:', len(output))
    if len(output) < 500:
        print('Output:', output)

httpd.shutdown()
