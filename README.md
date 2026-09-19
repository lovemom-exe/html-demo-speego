# SpeeGo Logistics - Kiến trúc Component & Demo các trang Knowledge & Sourcing

Dự án mở rộng giao diện website SpeeGo Logistics theo kiến trúc **Component-based** dùng chung partials (Header, CTA Form, Footer) và **SPA Hash Router** bằng JavaScript thuần (fetch API), không phụ thuộc bất kỳ framework hay thư viện bên ngoài nào.

---

## 1. Lệnh Khởi Chạy Local Server (Bắt buộc)

Do trình duyệt bảo mật chặn các yêu cầu `fetch()` với giao thức cục bộ `file:///`, bạn cần chạy thư mục qua một local web server.

Mở terminal tại thư mục dự án (`html speego`) và chạy một trong các lệnh sau:

### Cách 1: Dùng Node.js / npx (Khuyên dùng)
```bash
npx serve .
# Hoặc:
npx http-server -p 8080
```
Sau đó truy cập: [http://localhost:3000](http://localhost:3000) (hoặc port hiển thị trên terminal).

### Cách 2: Dùng Python 3 (Có sẵn trên hầu hết các máy)
```bash
python -m http.server 8080
# Hoặc trên macOS/Linux:
python3 -m http.server 8080
```
Sau đó truy cập: [http://localhost:8080](http://localhost:8080)

### Cách 3: Dùng VS Code Extension
- Cài extension **Live Server**
- Click chuột phải vào file `index.html` → chọn **"Open with Live Server"**.

---

## 2. Các Đường Dẫn Demo (Hash URL)

Khi server đang chạy, bạn có thể chuyển đổi giữa các trang qua thanh điều hướng hoặc truy cập trực tiếp các URL sau:

| Tên Trang | URL Hash | File Nguồn |
| :--- | :--- | :--- |
| **Knowledge Hub (Tiếng Việt)** | `#/knowledge` | `pages/VI/vi-01-chuyenmuc-tat-ca-chuyen-muc.html` |
| **Hướng dẫn vận chuyển (Tiếng Việt)** | `#/knowledge/huong-dan-van-chuyen` | `pages/VI/vi-02-chuyenmuc-shipping-guides.html` |
| **Sourcing (Bản refactor dùng partials)** | `#/sourcing` | `pages/sourcing.html` |
| **Knowledge Hub (Tiếng Anh)** | `#/en/knowledge` | `pages/EN/en-01-chuyenmuc-tat-ca-chuyen-muc.html` |
| **Shipping Guides (Tiếng Anh)** | `#/en/shipping-guides` | `pages/EN/en-02-chuyenmuc-shipping-guides.html` |

> **Mẹo**: Nhấp vào nút **"English ▾" / "Tiếng Việt ▾"** trên header để chuyển đổi ngôn ngữ nhanh chóng giữa các trang tương ứng.

---

## 3. Cấu Trúc Thư Mục Dự Án

```
html speego/
├── assets/                           # Hình ảnh, logo SpeeGo và ảnh banner
│   ├── speego-logo-dark.png
│   ├── speego-logo-white.png
│   └── warehouse_hero.jpg
├── Preview Knowledge/                # Thư mục ảnh mockup thiết kế (VI & EN)
├── css/
│   └── style.css                     # Stylesheet tổng hợp dùng chung toàn bộ trang
├── partials/                         # Các component dùng chung
│   ├── header.html                   # Top bar + Main Nav + Breadcrumb động + Mobile Drawer
│   ├── cta-form.html                 # Form tư vấn (hỗ trợ 2 layout: "band" & "sidebar")
│   └── footer.html                   # Footer chuẩn 3 cột + Copyright bar + Toast popup
├── pages/                            # Các trang nội dung độc lập (không lặp header/footer)
│   ├── sourcing.html                 # Trang Sourcing refactored
│   ├── knowledge.html                # Alias trang Knowledge Hub
│   ├── knowledge-shipping-guide.html # Alias trang Hướng dẫn vận chuyển
│   ├── VI/                           # Thư mục các trang Tiếng Việt
│   │   ├── vi-01-chuyenmuc-tat-ca-chuyen-muc.html
│   │   └── vi-02-chuyenmuc-shipping-guides.html
│   └── EN/                           # Thư mục các trang Tiếng Anh
│       ├── en-01-chuyenmuc-tat-ca-chuyen-muc.html
│       └── en-02-chuyenmuc-shipping-guides.html
├── index.html                        # SPA Hash Router nạp partials & pages
└── README.md                         # Hướng dẫn này
```

---

## 4. Cách Sử Dụng Partials Cho 8 Trang Tiếp Theo

Để thêm một trang mới (ví dụ `pages/VI/vi-03-chuyenmuc-industry-guides.html`):

1. **Khai báo thẻ bao ngoài kèm Metadata**:
```html
<div class="page-container" 
     data-page="industry-guides" 
     data-nav="knowledge" 
     data-breadcrumb='[{"label":"Trang chủ","href":"#/sourcing"},{"label":"Knowledge","href":"#/knowledge"},{"label":"Kiến thức ngành hàng","href":"#/knowledge/kien-thuc-nganh-hang"}]'>
  <!-- Chỉ viết phần nội dung riêng của trang tại đây -->
</div>
```

2. **Chèn Form Tư vấn (CTA Form)**:
- Nếu muốn dùng dải ngang full-width (biến thể `band`):
```html
<div data-component="cta-form" data-variant="band" data-heading="Bắt đầu từ nhu cầu của bạn."></div>
```
- Nếu muốn dùng card hẹp 1 cột (biến thể `sidebar`):
```html
<div data-component="cta-form" data-variant="sidebar" data-heading="Bạn cần tư vấn?" data-phone="(+84) 906 828 898 ↗"></div>
```

3. **Đăng ký route vào `index.html`**:
Thêm 1 dòng vào đối tượng `ROUTES`:
```javascript
'#/knowledge/kien-thuc-nganh-hang': {
  file: 'pages/VI/vi-03-chuyenmuc-industry-guides.html',
  title: 'Kiến thức ngành hàng | SpeeGo Knowledge',
  nav: 'knowledge',
  lang: 'vi'
}
```
Mọi xử lý tải partials, active menu, breadcrumb động và hiển thị toast form sẽ tự động hoạt động!
