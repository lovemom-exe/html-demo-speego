import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(r"c:\Users\X1 Yoga\html speego")
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

def test_url(url, expected_snippets):
    print(f"\n--- Testing: {url} ---")
    cmd = [
        edge_path,
        '--headless=new',
        '--disable-gpu',
        '--dump-dom',
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    dom = res.stdout

    if '<main id="app-main">' in dom:
        content = dom.split('<main id="app-main">')[1].split('</main>')[0]
        if 'app-error-card' in content:
            print("❌ FAILED: Found app-error-card inside app-main!")
            return False
    elif 'app-error-card' in dom and '<main id="app-main">' not in dom:
        print("❌ FAILED: Found app-error-card in DOM!")
        return False

    all_passed = True
    for snip in expected_snippets:
        if snip in dom:
            print(f"  ✓ Found: '{snip[:40]}...'")
        else:
            print(f"  ❌ MISSING: '{snip}'")
            all_passed = False

    return all_passed

# 1. Test VI SPA route
vi_expected = [
    "Tìm nguồn hàng &amp;",
    "kiểm soát chất lượng",
    "sourcing-subnav-grid",
    "Ngành hàng",
    "Mô hình sản xuất",
    "Vì sao SpeeGo",
    "Kiểm soát chất lượng",
    "Tư vấn nguồn hàng ↗",
    "Mỹ phẩm",
    "Nails",
    "Decor, nội thất",
    "Thủ công mỹ nghệ",
    "Thiết bị kỹ thuật",
    "OEM",
    "ODM",
    "Private Label",
    "Mạng lưới đối tác rộng lớn",
    "Kiểm tra trước sản xuất",
    "Nhìn tận nơi sản xuất",
    "prodSliderTrack",
    "Quy trình QC tại nhà máy",
    "Dây chuyền lắp ráp tự động",
    "Chiết rót &amp; đóng gói phòng sạch",
    "Biệt trữ &amp; quét mã xuất xưởng",
    "factory_assembly_line.jpg",
    "factory_packaging_qc.jpg",
    "factory_staging_dispatch.jpg",
    "SpeeGo có hỗ trợ đàm phán MOQ không?",
    "Kevin Le",
    "Sarah Mitchell",
    "Bắt đầu từ nhu cầu của bạn."
]

# 2. Test EN SPA route
en_expected = [
    "Comprehensive",
    "sourcing",
    "and quality control.",
    "sourcing-subnav-grid",
    "Industries",
    "Manufacturing models",
    "Why SpeeGo",
    "Quality control",
    "Discuss sourcing needs ↗",
    "Cosmetics",
    "Nails",
    "Decor &amp; furniture",
    "Handicrafts",
    "Technical equipment",
    "OEM",
    "ODM",
    "Private Label",
    "An extensive partner network",
    "Pre-production inspection",
    "See the production floor.",
    "prodSliderTrack",
    "QC on the factory floor",
    "Automated assembly line",
    "Cleanroom bottling &amp; packaging",
    "Staging &amp; barcode dispatch",
    "factory_assembly_line.jpg",
    "factory_packaging_qc.jpg",
    "factory_staging_dispatch.jpg",
    "Does SpeeGo help negotiate MOQs?",
    "Kevin Le",
    "Sarah Mitchell",
    "Start with what",
    "you need."
]

passed_vi = test_url("file:///c:/Users/X1 Yoga/html speego/index.html#/sourcing", vi_expected)
passed_en = test_url("file:///c:/Users/X1 Yoga/html speego/index.html#/en/sourcing", en_expected)
passed_vi_standalone = test_url("file:///c:/Users/X1 Yoga/html speego/sourcing.html", vi_expected)
passed_en_standalone = test_url("file:///c:/Users/X1 Yoga/html speego/en-sourcing.html", en_expected)

if passed_vi and passed_en and passed_vi_standalone and passed_en_standalone:
    print("\n🎉 ALL SOURCING VERIFICATION TESTS PASSED 100%!")
    sys.exit(0)
else:
    print("\n❌ SOME VERIFICATION TESTS FAILED!")
    sys.exit(1)
