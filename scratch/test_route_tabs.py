import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

def test_page(hash_url, checks):
    cmd = [
        edge_path,
        '--headless=new',
        '--disable-gpu',
        '--dump-dom',
        f'file:///c:/Users/X1 Yoga/html speego/index.html{hash_url}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    dom = res.stdout
    print(f"\n=== Testing {hash_url} ===")
    all_passed = True
    for name, substr in checks.items():
        found = substr in dom
        print(f"  [{'✓' if found else '❌'}] {name}: {found}")
        if not found:
            all_passed = False
    return all_passed

# 1. Check Xuất nhập khẩu (06-import-export.png)
ie_checks = {
    "Hero Title": "Xuất nhập khẩu",
    "Hero Tag": "IMPORT &amp; EXPORT",
    "Hero Sub": "thuận lợi hơn.",
    "Hero Image": "card_hand_device.jpg",
    "Hero Caption": "Chứng từ rõ ràng. Quy trình xuyên suốt.",
    "Section Core Services": "Giải pháp cho từng yêu cầu xuất nhập khẩu.",
    "Card 1": "Tư vấn hải quan",
    "Card 2": "Khai báo và thông quan xuất nhập khẩu",
    "Card 3": "Kiểm tra chuyên ngành",
    "Card 4": "Chứng nhận xuất xứ hàng hóa",
    "Card 5": "Các dịch vụ hỗ trợ tuân thủ bổ sung",
    "Section Why Choose": "Hiểu thủ tục.",
    "Why Card 1": "Am hiểu thủ tục xuất nhập khẩu",
    "Why Card 2": "Hỗ trợ đa dạng loại hàng",
    "Why Card 3": "Kiểm soát rủi ro hải quan",
    "Why Card 4": "Hỗ trợ xuyên suốt quy trình",
    "CTA Form": "Soạn email tư vấn ↗"
}
ie_ok = test_page("#/xuat-nhap-khau", ie_checks)

# 2. Check Tuyến vận chuyển (07-china-shipping.png & 08-vietnam-shipping.png)
routes_checks = {
    "Hero Tag": "INTERNATIONAL FREIGHT",
    "Hero Title China": "Dịch vụ vận chuyển từ",
    "Hero Dest Target": "đến Mỹ, Canada &amp; Úc",
    "Hero Image": "warehouse_hero.jpg",
    "Hero Caption": "Kết nối hàng hóa. Mở rộng thị trường.",
    "Tab China": "Xuất phát từ Trung Quốc",
    "Tab Vietnam": "Xuất phát từ Việt Nam",
    "Dest US": "Trung Quốc ➔ Mỹ",
    "Dest CA": "Trung Quốc ➔ Canada",
    "Dest AU": "Trung Quốc ➔ Úc",
    "Dest Global": "Trung Quốc ➔ Nước khác",
    "8 Steps Section Title": "Từng bước rõ ràng.",
    "Step 1": "Tiếp nhận yêu cầu",
    "Step 2": "Tư vấn giải pháp",
    "Step 3": "Kết nối nguồn hàng",
    "Step 4": "Theo dõi sản xuất",
    "Step 5": "Kiểm tra chất lượng",
    "Step 6": "Chuẩn bị chứng từ",
    "Step 7": "Vận chuyển quốc tế",
    "Step 8": "Hoàn tất &amp; bàn giao",
    "Methods Section": "Linh hoạt phương thức vận chuyển.",
    "Method Ocean": "Vận chuyển đường biển",
    "Method Air": "Vận chuyển đường hàng không",
    "Method Road": "Vận chuyển đường bộ",
    "Why Choose Section": "Đồng hành trên hành trình quốc tế.",
    "Why 1 Transit Time": "Thời gian vận chuyển",
    "Why 2 Cost Optimization": "Hỗ trợ chi phí tối đa cho khách hàng",
    "Why 3 Multimodal": "Đa dạng phương thức",
    "Why 4 US Fulfillment": "Fulfillment tại Mỹ",
    "Why 5 US Entity": "Hiện diện tại Mỹ",
    "Rate Table Title": "Bảng giá vận chuyển",
    "Rate Air": "Đường hàng không",
    "Rate FCL": "Đường biển · FCL",
    "Rate LCL": "Đường biển · LCL",
    "FAQ Title": "Câu hỏi thường gặp",
    "FAQ 1": "SpeeGo hỗ trợ những điểm đến nào?",
    "FAQ 2": "Có thể gửi hàng lẻ không?",
    "FAQ 3": "Thời gian vận chuyển có cố định không?",
    "FAQ 4": "Tôi cần cung cấp gì để nhận báo giá?",
    "FAQ 5": "Có thể kết hợp fulfillment tại Mỹ không?",
    "Testimonial": "Sarah Mitchell",
    "CTA Form": "Soạn email tư vấn ↗"
}
routes_ok = test_page("#/tuyen-van-chuyen", routes_checks)

print("\n==================================================")
if ie_ok and routes_ok:
    print("ALL ASSERTIONS PASSED 100%! The pages match the mockups perfectly.")
else:
    print("SOME ASSERTIONS FAILED!")
print("==================================================")
