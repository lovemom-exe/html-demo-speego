---
name: speego-frontend-standards
description: Quy chuẩn kiến trúc component, typography, bảng màu, form tư vấn, bố cục thẻ bài viết dọc và quy trình mở rộng trang cho website SpeeGo Logistics.
---

# SpeeGo Logistics — Design System & Frontend Development Skill

Tài liệu này là quy chuẩn kỹ thuật toàn diện (Technical Standards & Guidelines) dành cho việc phát triển, bảo trì và mở rộng hệ thống website **SpeeGo Logistics** (dòng trang Kiến thức / Knowledge, Tuyến thương mại, Sourcing, Fulfillment).

---

## 1. Kiến Trúc Dự Án & Nguyên Tắc Cốt Lõi

### 1.1. Triết Lý Kỹ Thuật
- **100% Vanilla Web:** Sử dụng HTML5, CSS3 hiện đại và JavaScript thuần (ES6+), **không sử dụng** framework cồng kềnh (React, Vue, Tailwind) hay thư viện phụ thuộc từ bên ngoài.
- **Component-Based Architecture:** Các thành phần dùng chung (Header, Footer, Form tư vấn) được tách thành các tệp partials độc lập trong thư mục `partials/` và nạp động qua `fetch()` API.
- **SPA Hash Router:** Điều hướng trang mượt mà không tải lại trình duyệt qua URL hash (ví dụ: `#/knowledge`, `#/en/shipping-guides`), hỗ trợ lịch sử duyệt web (`history`) và đánh dấu menu tự động.
- **Chạy Local Web Server:** Bắt buộc chạy ứng dụng qua một local web server (như `npx serve .` hoặc `python -m http.server 8080`) để tránh lỗi bảo mật CORS / `file:///` khi trình duyệt gọi `fetch()`.

---

## 2. Cấu Trúc Thư Mục & Vai Trò

```
html speego/
├── assets/                           # Hình ảnh thực tế, logo SpeeGo, banner kho bãi, cảng biển
│   ├── card_hand_device.jpg          # Ảnh thẻ tín dụng & smartphone (1376x768)
│   ├── port_sunset_hero.jpg          # Ảnh cảng biển hoàng hôn & máy bay (1592x736)
│   ├── speego-logo-dark.png          # Logo SpeeGo nền sáng
│   ├── speego-logo-white.png         # Logo SpeeGo nền tối (footer)
│   ├── warehouse_hero.jpg            # Ảnh sàn xưởng thiết bị công nghiệp (1592x736)
│   └── warehouse_racks_hero.jpg      # Ảnh hệ thống kệ pallet xanh-cam (1592x736)
├── Preview Knowledge/                # Thư mục chứa 20 ảnh mockup chuẩn (10 VI + 10 EN)
│   ├── VI/                           # Mockup Tiếng Việt (vi-01 đến vi-10)
│   └── EN/                           # Mockup Tiếng Anh (en-01 đến en-10)
├── css/
│   └── style.css                     # Stylesheet duy nhất, chứa toàn bộ design system
├── partials/                         # Các thành phần tái sử dụng
│   ├── header.html                   # Top bar + Main Nav + Breadcrumb động + Mobile Drawer
│   ├── cta-form.html                 # Mẫu form tư vấn động (Band 2 cột & Sidebar 1 cột)
│   └── footer.html                   # Footer chân trang 3 cột + Copyright + Toast thông báo
├── pages/                            # Nội dung riêng của từng trang (không chứa Header/Footer)
│   ├── sourcing.html                 # Trang Sourcing
│   ├── VI/                           # 10 trang Tiếng Việt
│   │   ├── vi-01-chuyenmuc-tat-ca-chuyen-muc.html
│   │   ├── vi-02-chuyenmuc-shipping-guides.html
│   │   ├── vi-03-chuyenmuc-industry-guides.html
│   │   ├── vi-04-chuyenmuc-trade-route.html
│   │   ├── vi-05-chuyenmuc-sourcing-qc.html
│   │   ├── vi-06-chuyenmuc-fulfillment-warehouse.html
│   │   ├── vi-07-chuyenmuc-import-export-news.html
│   │   ├── vi-08-post-chuan-bi-lo-hang.html
│   │   ├── vi-09-post-quy-trinh-nhap-kho.html
│   │   └── vi-10-post-kiem-soat-chat-luong.html
│   └── EN/                           # 10 trang Tiếng Anh (song ngữ đối ứng 1-1)
│       ├── en-01-chuyenmuc-tat-ca-chuyen-muc.html
│       └── ... (en-02 đến en-10)
├── scratch/                          # Scripts kiểm thử tự động, công cụ inspect
├── index.html                        # Vỏ ứng dụng chính (Shell), App Router & i18n
├── README.md                         # Hướng dẫn chạy và sử dụng dự án
└── SKILL.md                          # Tài liệu quy chuẩn này
```

---

## 3. Quy Chuẩn Typography & Tỷ Lệ Chữ (Đồng Bộ Homepage)

Dự án được đồng bộ 100% font chữ và tỷ lệ từ website chính thức: `https://speegoweb.vercel.app/`.

### 3.1. Font Chữ (Typography)
- **Primary Font Family:** `'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;`
- **Tải từ Google Fonts:**
  `<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700;1,800&display=swap" rel="stylesheet">`
- Biến CSS:
  ```css
  --font-base: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-heading: 'Inter', ui-sans-serif, system-ui, sans-serif;
  ```

### 3.2. Thang Tỷ Lệ Font (Type Scale)

| Thành phần | Kích thước | Trọng lượng (Weight) | Khoảng cách dòng (Line Height) | Màu sắc & Ghi chú |
|:---|:---|:---|:---|:---|
| **Hero Title H1** | `clamp(32px, 4.5vw, 46px)` | `800` (Extrabold) | `1.15` | `--text-navy` (`#04243D`), letter-spacing: `-0.025em` |
| **Section Title H2** | `clamp(24px, 3vw, 32px)` | `800` (Extrabold) | `1.25` | `--text-navy` (`#04243D`), letter-spacing: `-0.02em` |
| **Topic / Section Subtitle** | `14.5px - 17px` | `400` (Regular) | `1.5 - 1.6` | `#64748B` (Slate Muted) |
| **Card Heading H3** | `16.5px - 18px` | `700` (Bold) | `1.35 - 1.4` | `--text-navy` (`#04243D`), letter-spacing: `-0.01em` |
| **Card Excerpt / Body** | `13.5px - 14px` | `400` (Regular) | `1.55` | `#64748B` (Secondary body copy) |
| **Post Detail Content H2**| `1.38rem` (~22px) | `700` (Bold) | `1.35` | `--text-navy` |
| **Post Detail Paragraph** | `0.94rem` (~15px) | `400` (Regular) | `1.72` | `--text-body` (`#5B6472`) |
| **Section Tag / Eyebrow** | `11.5px` | `700` (Bold) | `1.0` | In hoa (`uppercase`), letter-spacing: `0.08em` |
| **Form Label** | `11.5px` | `700` (Bold) | `1.2` | In hoa (`uppercase`), letter-spacing: `0.03em`, `--speego-primary` |
| **Input Text** | `13.5px` | `400` (Regular) | `1.4` | `#1E293B` |
| **Form Button Text** | `14.5px` | `800` (Extrabold) | `1.2` | `#FFFFFF` |
| **Security Note / Meta** | `11.5px - 12px` | `400 - 500` | `1.45` | `#94A3B8` |

---

## 4. Hệ Thống Màu Sắc Chuẩn Thương Hiệu (Color Palette)

```css
:root {
  /* Brand Primary Colors */
  --speego-primary: #04243D;         /* Navy đậm chủ đạo (Header, Title, Form Labels) */
  --speego-primary-light: #0D3B66;   /* Navy sáng nhẹ */
  --speego-accent: #F26419;          /* Cam SpeeGo (Nút CTA, Highlight, Hover) */
  --speego-accent-hover: #D8520E;    /* Cam sậm khi hover */
  --orange-light: #FFF4ED;          /* Nền cam nhạt cho icon/badge con */

  /* Dark Sections & Sidebar */
  --navy-main: #04243D;             /* Nền dải Band CTA, Thanh Top bar */
  --navy-sidebar: #0B1D33;          /* Nền card Sidebar Form tư vấn */
  --navy-deep: #041A2D;             /* Nền chính của Footer */
  --navy-darker: #020F1A;           /* Nền thanh bản quyền dưới cùng (Copyright bar) */

  /* Neutrals & Surfaces */
  --bg-white: #FFFFFF;              /* Trắng tiêu chuẩn */
  --bg-light-gray: #F8FAFC;         /* Nền dải bài viết mới nhất, nền input */
  --bg-subtle-gray: #F1F5F9;        /* Nền card chủ đề con (subcat cards) */
  --border-light: #E2E8F0;          /* Đường viền hairline thẻ card */
  --border-input: #CBD5E1;          /* Viền input 1.5px chuẩn Homepage */
  --border-dark: rgba(255, 255, 255, 0.12); /* Viền mờ trên nền tối */

  /* Text Colors */
  --text-navy: #04243D;
  --text-body: #5B6472;
  --text-muted: #94A3B8;
  --text-white: #FFFFFF;
}
```

---

## 5. Quy Cách Form Tư Vấn (Consultation Form Component)

Form tư vấn là thành phần chuyển đổi khách hàng trọng tâm, gồm 2 biến thể:

### 5.1. Biến thể Dải Ngang Full-Width (`variant="band"`)
- **Vị trí:** Đặt ở cuối các trang hub/tổng quan (ví dụ: `vi-01`, `sourcing.html`).
- **Bố cục:** Lưới 2 cột (`1fr 1.2fr` trên Desktop, `1fr` trên Mobile).
  - Cột trái: Tagline, Heading trắng lớn, mô tả ngắn, số hotline `(+84) 906 828 898 ↗`.
  - Cột phải: Card trắng nổi bật (`consult-card-white`):
    - Bo góc `14px`, viền `1px solid #E2E8F0`, bóng đổ `box-shadow: 0 16px 40px rgba(4, 36, 61, 0.08)`.
    - Hàng 1 chia 2 cột: Họ tên & Email.
    - Hàng 2: Số điện thoại.
    - Hàng 3: Nhu cầu tư vấn (`textarea`).
    - Nút Submit: Chiều cao `48px`, nền cam `#F26419`, chữ trắng in hoa đậm 14.5px weight 800, bo góc `10px`.

### 5.2. Biến thể Cột Bên (`variant="sidebar"`)
- **Vị trí:** Đặt tại cột phải (~40%) của section "Bài viết mới nhất" trong các trang chuyên mục (trang 02 đến 07).
- **Bố cục:** Card dọc nền Navy đậm (`consult-card-sidebar`):
  - Màu nền `--navy-sidebar` (`#0B1D33`), bo góc `14px`, viền `1px solid rgba(255, 255, 255, 0.12)`.
  - Toàn bộ trường input xếp chồng 1 cột theo chiều dọc.
  - Ô nhập liệu dùng kính mờ: nền `rgba(255, 255, 255, 0.06)`, viền `rgba(255, 255, 255, 0.18)`, chữ trắng, placeholder màu mờ `rgba(255, 255, 255, 0.5)`.

### 5.3. Thông Số Input & Controls (Chuẩn 100% Homepage)
- **Chiều cao input:** Cố định **`46px`** (trừ `textarea` có `min-height: 80px`).
- **Viền input:** `1.5px solid #CBD5E1`.
- **Bo góc:** **`9px`**.
- **Hiệu ứng Focus:** Viền chuyển sang cam `#F26419`, nền trắng `#FFFFFF`, bóng tỏa `box-shadow: 0 0 0 3px rgba(242, 100, 25, 0.15)`.
- **Nhãn (`label`):** Font size `11.5px`, font-weight `700`, in hoa toàn bộ (`text-transform: uppercase`), `letter-spacing: 0.03em`.
- **Ghi chú bảo mật:** `11.5px`, màu `#94A3B8`, căn giữa (`text-align: center`).

---

## 6. Quy Tắc Thẻ Bài Viết (Latest Resources - Post Cards)

> [!IMPORTANT]
> **QUY TẮC BẮT BUỘC: ĐỊNH DẠNG THẺ CHỮ NHẬT DỌC**
> Toàn bộ thẻ bài viết trong mục "Bài viết mới nhất / Latest Resources" trên tất cả các trang chuyên mục **BẮT BUỘC PHẢI Ở DẠNG THẺ CHỮ NHẬT DỌC** (khớp chính xác phong cách thiết kế của trang mẫu `Preview Knowledge/VI/vi-03-chuyenmuc-industry-guides.png`).
> **TUYỆT ĐỐI KHÔNG ĐƯỢC DÙNG THẺ DẠNG DẠT NGANG** (ảnh bên trái, chữ bên phải) vì gây tốn diện tích và phá vỡ cấu trúc lưới responsive.

### 6.1. Bố Cục Thẻ Dọc Chuẩn (`.featured-article-card`)
- **Container lưới:** `.featured-cards-list` với `display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;`.
- **Thẻ:** Bo góc `14px`, nền trắng `#FFFFFF`, viền `1px solid #E2E8F0`, `box-shadow: 0 4px 18px rgba(15, 39, 66, 0.05)`.
- **Ảnh trên đầu (`.featured-img-wrap`):**
  - Chiều cao cố định: **`190px`**, chiều rộng 100%.
  - Bo góc trên theo thẻ cha (`overflow: hidden`).
  - Phủ badge nhãn danh mục nền Navy ở góc trên bên trái (`.featured-tag-pill`).
  - Ảnh bên trong có `object-fit: cover`, hiệu ứng hover zoom nhẹ: `transform: scale(1.06)`.
- **Nội dung bên dưới (`.featured-content`):**
  - Padding: `20px 22px 24px`.
  - Dòng meta: `12px`, ngày đăng · SpeeGo Team kèm badge `EN` nếu là bài tiếng Anh.
  - Tiêu đề: `16.5px`, bold 700, màu navy `#04243D`, giãn dòng `1.4`.
  - Mô tả tóm tắt: `13.5px`, màu xám `#64748B`, giãn dòng `1.55`.
  - Link đọc tiếp: `13.5px`, màu cam đậm `--orange-primary` kèm icon mũi tên `↗`.

### 6.2. Quy Tắc Xử Lý Khi Trang Chỉ Có 1 Thẻ (Trang 02 & Trang 06)
- **Vấn đề:** Trong lưới 2 cột (`1.55fr 1fr`), nếu trang chỉ có 1 bài viết mà để thẻ tự do chiếm trọn cột trái (~700px), thẻ sẽ bị kéo bè sang ngang gây mất cân đối.
- **Giải pháp:** Bọc thẻ duy nhất trong container:
  ```html
  <div class="featured-cards-list single-card">
    <div class="featured-article-card">
      ...
    </div>
  </div>
  ```
- **CSS áp dụng:**
  ```css
  .featured-cards-list.single-card,
  .featured-cards-list:has(> .featured-article-card:only-child) {
    display: grid;
    grid-template-columns: minmax(0, 360px);
  }
  ```
  Nhờ quy tắc này, thẻ luôn giữ đúng kích thước chữ nhật dọc chuẩn mực (~360px) giống hệt trang 03, 05, 07.

---

## 7. Cơ Chế Song Ngữ & Đồng Bộ Shell (Bilingual Engine)

Trang web hỗ trợ song ngữ hoàn chỉnh 1-1 giữa Tiếng Việt (VI) và Tiếng Anh (EN).

### 7.1. Bảng Ánh Xạ Đường Dẫn 1-1 (`LANG_PAIRS`)
Mỗi trang tiếng Việt có đúng một trang tiếng Anh đối ứng trong `index.html`:
```javascript
const LANG_PAIRS = {
  '#/knowledge': '#/en/knowledge',
  '#/knowledge/huong-dan-van-chuyen': '#/en/shipping-guides',
  '#/knowledge/kien-thuc-nganh-hang': '#/en/industry-guides',
  '#/knowledge/tuyen-thuong-mai': '#/en/trade-routes',
  '#/knowledge/sourcing-qc': '#/en/sourcing-qc',
  '#/knowledge/fulfillment-kho-van': '#/en/fulfillment-warehouse',
  '#/knowledge/tin-xuat-nhap-khau': '#/en/import-export-news',
  '#/knowledge/chuan-bi-lo-hang': '#/en/post/preparing-your-shipment',
  '#/knowledge/quy-trinh-nhap-kho': '#/en/post/fulfillment-receiving',
  '#/knowledge/kiem-soat-chat-luong': '#/en/post/quality-control',
  // Chiều ngược lại (EN -> VI)...
};
```

### 7.2. Tự Động Hóa Vỏ Ứng Dụng (Shell Localization)
Khi người dùng bấm nút chuyển ngôn ngữ trên Header (`#langToggle`), hàm `updateShellLanguage(currentLang)` và `renderCtaComponents(container)` sẽ tự động:
1. Đổi toàn bộ nhãn thanh menu Desktop & Mobile Drawer.
2. Đổi nút Header: `Nhận tư vấn ↗` ⟷ `Get in Touch ↗`.
3. Đổi nút Ngôn ngữ: `English` ⟷ `Tiếng Việt`.
4. Đổi toàn bộ Footer (Tagline, Cột Khám phá, Cột Kết nối, Quy trình 8 bước).
5. Thay thế toàn bộ nội dung trong Form tư vấn (từ điển `CTA_I18N`):
   - Nút gửi: `Soạn email tư vấn ↗` ⟷ `Draft an Inquiry ↗`.
   - Nhãn ô: `Họ và tên` ⟷ `Full name`, `Số điện thoại` ⟷ `Phone number`, v.v.
   - Ghi chú bảo mật: Song ngữ đầy đủ.
   - Thông báo Toast phản hồi sau khi gửi: Song ngữ kèm tên người gửi.

---

## 8. Quy Trình Thêm Trang Mới (Step-by-Step Checklist)

Khi được yêu cầu tạo thêm một trang mới (ví dụ: `vi-11-...` hoặc `en-11-...`), hãy thực hiện nghiêm ngặt theo 5 bước sau:

### Bước 1: Tạo Tệp HTML Trang Trong `pages/`
- Tạo file tại `pages/VI/vi-xx-ten-trang.html` (hoặc `pages/EN/en-xx-ten-trang.html`).
- Bọc toàn bộ nội dung trong thẻ gốc chứa Metadata:
  ```html
  <div class="page-container" 
       data-page="ten-dinh-danh" 
       data-nav="knowledge" 
       data-breadcrumb='[{"label":"Trang chủ","href":"#/sourcing"},{"label":"Knowledge","href":"#/knowledge"},{"label":"Tên Trang","href":"#/duong-dan"}]'>
    <!-- Nội dung riêng của trang -->
  </div>
  ```

### Bước 2: Chèn Form Tư Vấn Nếu Trang Cần
- Dạng Band (cuối trang): `<div data-component="cta-form" data-variant="band"></div>`
- Dạng Sidebar (cột phải): `<div data-component="cta-form" data-variant="sidebar"></div>`

### Bước 3: Đăng Ký Tuyến Đường Trong `index.html`
- Thêm đối tượng route vào `ROUTES`:
  ```javascript
  '#/duong-dan': {
    file: 'pages/VI/vi-xx-ten-trang.html',
    title: 'Tiêu đề trang | SpeeGo Knowledge',
    nav: 'knowledge',
    lang: 'vi'
  }
  ```
- Đăng ký cặp chuyển ngữ đối ứng trong `LANG_PAIRS` (VI ⟷ EN).

### Bước 4: Kiểm Tra Hình Ảnh Tham Chiếu
- Đảm bảo tất cả thẻ `<img>` chỉ trỏ tới các tệp hiện có trong thư mục `assets/` (`assets/*.jpg` hoặc `assets/*.png`).
- Luôn thêm thuộc tính dự phòng `onerror="this.onerror=null; this.src='assets/warehouse_hero.jpg';"` cho các ảnh thẻ bài viết.

### Bước 5: Chạy Bộ Kiểm Thử Tự Động
- Chạy lệnh kiểm tra trong terminal:
  ```bash
  py -3.12 scratch/verify_suite.py
  ```
- Đảm bảo kết quả trả về `SUCCESS: 0 errors found! All tests passed perfectly.` trước khi bàn giao cho khách hàng.

---

## 9. Những Điều Cấm Kỵ (Strict Constraints / Don'ts)

1. **KHÔNG** sử dụng thẻ bài viết dạng ngang trong phần "Bài viết mới nhất / Latest Resources". Mọi thẻ bài viết phải là **thẻ chữ nhật dọc**.
2. **KHÔNG** lặp lại mã HTML của Header, Footer hoặc Form tư vấn trực tiếp trong từng file trang; bắt buộc dùng cơ chế component partials.
3. **KHÔNG** hardcode trực tiếp text tiếng Việt vào `partials/cta-form.html` mà phải sử dụng các token `{{LABEL_NAME}}`, `{{BTN_SUBMIT}}`, v.v., để hệ thống i18n tự động render theo ngữ cảnh.
4. **KHÔNG** sử dụng font chữ lạ hay thêm thư viện CSS ngoài (Bootstrap, Tailwind); mọi kiểu dáng phải kế thừa từ biến CSS trong `css/style.css`.
5. **KHÔNG** chạy lệnh `cd` trong môi trường dòng lệnh; luôn chỉ định đường dẫn làm việc qua cờ hoặc tham số trực tiếp.
6. **KHÔNG** tự ý thay đổi nội dung bài viết hay thông điệp đã được người dùng chốt trong các vòng trước.
