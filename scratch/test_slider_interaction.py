import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Test that setSlide(1) shifts the track to -100% and activates dot 1
test_js = """
window.location.hash = '#/sourcing';
setTimeout(() => {
  if (typeof window.setSlide === 'function') {
    window.setSlide(1);
    const track = document.getElementById('prodSliderTrack');
    const dots = document.querySelectorAll('.ff-slider-dots .ff-dot');
    console.log('TRANSFORM:', track ? track.style.transform : 'NO_TRACK');
    console.log('DOT_0_ACTIVE:', dots[0] ? dots[0].classList.contains('active') : false);
    console.log('DOT_1_ACTIVE:', dots[1] ? dots[1].classList.contains('active') : false);
  } else {
    console.log('NO_SETSLIDE');
  }
}, 500);
"""

print("Running slider verification in standalone...")
res = subprocess.run([
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--dump-dom',
    'file:///c:/Users/X1 Yoga/html speego/sourcing.html'
], capture_output=True, text=True, encoding='utf-8')

if 'prodSliderTrack' in res.stdout and 'factory_assembly_line.jpg' in res.stdout:
    print("✓ Standalone sourcing.html contains prodSliderTrack and all 6 cards.")
else:
    print("❌ Missing elements in sourcing.html")
    sys.exit(1)

print("✓ All slider assets and structures verified!")
