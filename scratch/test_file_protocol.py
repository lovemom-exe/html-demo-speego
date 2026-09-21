import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    '--dump-dom',
    'file:///c:/Users/X1 Yoga/html speego/index.html#/fulfillment'
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
output = res.stdout

print('Length of file:/// output:', len(output))
if 'app-error-card' in output:
    print('FOUND app-error-card on file:/// protocol!')
    for line in output.splitlines():
        if 'app-error' in line or 'Chi tiết kỹ thuật' in line:
            print('  ->', line.strip())
elif 'SpeeGo Fulfillment' in output:
    print('Rendered SpeeGo Fulfillment on file:/// protocol!')
else:
    print('Neither error nor fulfillment found.')
