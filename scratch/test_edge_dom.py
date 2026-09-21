import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--enable-logging=stderr',
    '--v=1',
    '--dump-dom',
    'file:///c:/Users/X1 Yoga/html speego/en-fulfillment.html'
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
dom = res.stdout
stderr = res.stderr

print('DOM length:', len(dom))
print('Stderr snippet:')
for line in stderr.splitlines()[-20:]:
    print('  ', line)

if '<main id="app-main">' in dom:
    part = dom.split('<main id="app-main">')[1].split('</main>')[0]
    print('Inside app-main length:', len(part))
    print('Checking fulfillment sections:')
    print('  Hero Dark Section:', 'ff-hero-dark-section' in part)
    print('  SpeeGo Fulfillment Title:', 'ff-hero-brand-title' in part)
    print('  4 Stats Columns:', 'ff-stats-bars-row' in part)
    print('  Dark Hub Card:', 'ff-dark-hub-card' in part)
    print('  Vibrant Orange Ticker:', 'ff-ticker-orange' in part)
    print('  Pricing Accordion:', 'ff-pricing-accordion' in part)
    print('  Calculator Widget:', 'ff-calc-card' in part)
    print('  Inside Houston Warehouse Slider:', 'warehouseGallery' in part)
    print('  FAQ Accordion:', 'ff-faq-section' in part)
    print('  Testimonials:', 'ff-testimonial-section' in part)
    print('  CTA Form (Band):', 'cta-form-band-section' in part)
    print('  App Error Card Present?:', 'app-error-card' in part)

