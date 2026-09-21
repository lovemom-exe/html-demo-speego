import re
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(r"c:\Users\X1 Yoga\html speego")

def build_standalone_pages():
    header_raw = (BASE / "partials/header.html").read_text(encoding="utf-8")
    footer_raw = (BASE / "partials/footer.html").read_text(encoding="utf-8")
    cta_raw = (BASE / "partials/cta-form.html").read_text(encoding="utf-8")
    
    # Extract CTA Band template
    cta_band_match = re.search(r'<template id="tmpl-cta-band">(.*?)</template>', cta_raw, flags=re.DOTALL)
    cta_band_tmpl = cta_band_match.group(1) if cta_band_match else ""

    # Build Vietnamese CTA
    vi_cta = cta_band_tmpl.replace("{{TAG}}", "LET'S MOVE FORWARD") \
        .replace("{{HEADING}}", "Bắt đầu từ nhu cầu của bạn.") \
        .replace("{{SUBTEXT}}", "Chia sẻ về hàng hóa và kế hoạch của doanh nghiệp. SpeeGo sẽ tư vấn giải pháp phù hợp.") \
        .replace("{{PHONE}}", "(+84) 906 828 898 ↗") \
        .replace("{{LABEL_NAME}}", "Họ và tên") \
        .replace("{{PLACEHOLDER_NAME}}", "Nguyễn Văn An") \
        .replace("{{LABEL_EMAIL}}", "Email") \
        .replace("{{PLACEHOLDER_EMAIL}}", "ban@congty.com") \
        .replace("{{LABEL_PHONE}}", "Số điện thoại") \
        .replace("{{PLACEHOLDER_PHONE}}", "Số điện thoại liên hệ") \
        .replace("{{LABEL_MESSAGE}}", "Nhu cầu tư vấn") \
        .replace("{{PLACEHOLDER_MESSAGE}}", "Loại hàng, số lượng, điểm đi và điểm đến...") \
        .replace("{{BTN_SUBMIT}}", "Soạn email tư vấn ↗") \
        .replace("{{SECURITY_NOTE}}", "Mở ứng dụng email với nội dung đã điền. Thông tin chỉ được gửi đi khi bạn bấm Gửi trong email.")

    # Build English CTA
    en_cta = cta_band_tmpl.replace("{{TAG}}", "LET'S MOVE FORWARD") \
        .replace("{{HEADING}}", "Start with what<br>you need.") \
        .replace("{{SUBTEXT}}", "Tell us about your products and business plans. SpeeGo will help you find the right solution.") \
        .replace("{{PHONE}}", "(+84) 906 828 898 ↗") \
        .replace("{{LABEL_NAME}}", "Full name") \
        .replace("{{PLACEHOLDER_NAME}}", "Your full name") \
        .replace("{{LABEL_EMAIL}}", "Email") \
        .replace("{{PLACEHOLDER_EMAIL}}", "you@company.com") \
        .replace("{{LABEL_PHONE}}", "Phone number") \
        .replace("{{PLACEHOLDER_PHONE}}", "Your contact number") \
        .replace("{{LABEL_MESSAGE}}", "How can we help?") \
        .replace("{{PLACEHOLDER_MESSAGE}}", "Product type, quantity, origin, and destination...") \
        .replace("{{BTN_SUBMIT}}", "Draft an Inquiry ↗") \
        .replace("{{SECURITY_NOTE}}", "Opens your email app with a prepared message. Your information is only sent when you click Send in your email app.")

    # Build Scripts block common to fulfillment
    scripts_common = """
  <script>
    // 1. Mobile Menu Drawer
    const openBtn = document.getElementById('mobileMenuOpen');
    const closeBtn = document.getElementById('mobileMenuClose');
    const drawer = document.getElementById('mobileDrawer');
    const backdrop = document.getElementById('drawerBackdrop');

    function openDrawer() {
      if (drawer) drawer.classList.add('open');
      if (backdrop) backdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeDrawer() {
      if (drawer) drawer.classList.remove('open');
      if (backdrop) backdrop.classList.remove('open');
      document.body.style.overflow = '';
    }

    if (openBtn) openBtn.onclick = openDrawer;
    if (closeBtn) closeBtn.onclick = closeDrawer;
    if (backdrop) backdrop.onclick = closeDrawer;
    document.querySelectorAll('#mobileDrawerLinks a').forEach(a => a.addEventListener('click', closeDrawer));

    // 2. Pricing Accordion Toggle
    function togglePricingGroup(headerEl) {
      const group = headerEl.closest('.ff-pricing-group');
      if (!group) return;
      const isActive = group.classList.contains('active');
      document.querySelectorAll('.ff-pricing-group').forEach(g => {
        g.classList.remove('active');
        const icon = g.querySelector('.ff-pricing-toggle-icon');
        if (icon) icon.textContent = '+';
      });
      if (!isActive) {
        group.classList.add('active');
        const icon = group.querySelector('.ff-pricing-toggle-icon');
        if (icon) icon.textContent = '✕';
      }
    }
    window.togglePricingGroup = togglePricingGroup;

    // 3. FAQ Accordion Toggle
    document.querySelectorAll('.faq-item').forEach(item => {
      const btn = item.querySelector('.faq-question-btn');
      if (btn) {
        btn.onclick = () => {
          const isActive = item.classList.contains('active');
          document.querySelectorAll('.faq-item').forEach(other => {
            if (other !== item) other.classList.remove('active');
          });
          if (isActive) item.classList.remove('active');
          else item.classList.add('active');
        };
      }
    });

    // 4. Warehouse Gallery Slider (3s Auto-Play with Hover Pause)
    let currentGallerySlide = 0;
    let galleryAutoPlayTimer = null;

    function setSlide(idx) {
      const slides = document.querySelectorAll('.ff-warehouse-slide');
      const dots = document.querySelectorAll('.ff-slider-dots .ff-dot');
      if (!slides || slides.length === 0) return;

      currentGallerySlide = (idx + slides.length) % slides.length;
      slides.forEach((slide, i) => {
        if (i === currentGallerySlide) slide.classList.add('active');
        else slide.classList.remove('active');
      });
      dots.forEach((dot, i) => {
        if (i === currentGallerySlide) dot.classList.add('active');
        else dot.classList.remove('active');
      });
    }

    function slideGallery(dir) {
      setSlide(currentGallerySlide + dir);
      restartGalleryAutoPlay();
    }

    function startGalleryAutoPlay() {
      stopGalleryAutoPlay();
      const frame = document.querySelector('.ff-warehouse-slider-frame');
      if (!frame) return;
      galleryAutoPlayTimer = setInterval(() => {
        setSlide(currentGallerySlide + 1);
      }, 3000);
    }

    function stopGalleryAutoPlay() {
      if (galleryAutoPlayTimer) {
        clearInterval(galleryAutoPlayTimer);
        galleryAutoPlayTimer = null;
      }
    }

    function restartGalleryAutoPlay() {
      stopGalleryAutoPlay();
      startGalleryAutoPlay();
    }

    function initWarehouseGallery() {
      const frame = document.querySelector('.ff-warehouse-slider-frame');
      if (!frame) return;
      setSlide(0);
      startGalleryAutoPlay();
      frame.onmouseenter = () => stopGalleryAutoPlay();
      frame.onmouseleave = () => startGalleryAutoPlay();
    }

    window.setSlide = function(idx) {
      setSlide(idx);
      restartGalleryAutoPlay();
    };
    window.slideGallery = slideGallery;
    window.initWarehouseGallery = initWarehouseGallery;
    window.stopGalleryAutoPlay = stopGalleryAutoPlay;

    // 5. Cost Calculator
    function calculateFulfillmentCost() {
      const wEl = document.getElementById('calcWeight');
      const zEl = document.getElementById('calcZone');
      const lEl = document.getElementById('calcLength');
      const wiEl = document.getElementById('calcWidth');
      const hEl = document.getElementById('calcHeight');
      const pkgEl = document.getElementById('calcPkg');

      if (!wEl || !zEl) return;

      const weight = parseFloat(wEl.value) || 0;
      const zone = parseInt(zEl.value, 10) || 1;
      const l = parseFloat(lEl.value) || 0;
      const w = parseFloat(wiEl.value) || 0;
      const h = parseFloat(hEl.value) || 0;
      const pkg = pkgEl ? pkgEl.value : 'poly';

      const dimWeight = (l * w * h) / 166;
      const billableWeight = Math.max(weight, dimWeight);

      let extraPkgCost = 0;
      let pkgText = 'Đã bao gồm';
      if (document.documentElement.lang === 'en') pkgText = 'Included';

      if (pkg === 'bubble') { extraPkgCost = 0.50; pkgText = '+$0.50'; }
      else if (pkg === 'carton_s') { extraPkgCost = 1.00; pkgText = '+$1.00'; }
      else if (pkg === 'carton_m') { extraPkgCost = 1.50; pkgText = '+$1.50'; }
      else if (pkg === 'carton_l') { extraPkgCost = 1.70; pkgText = '+$1.70'; }

      const resWeight = document.getElementById('calcResultWeight');
      const resAio = document.getElementById('calcResultAio');
      const resPkg = document.getElementById('calcResultPkg');
      const resShip = document.getElementById('calcResultShip');
      const resTotal = document.getElementById('calcResultTotal');

      if (resWeight) resWeight.textContent = `${billableWeight.toFixed(2)} lbs`;

      let total = 0;
      let aioText = '$7.00';
      let shipText = document.documentElement.lang === 'en' ? 'Included' : 'Đã bao gồm';

      if (billableWeight <= 1.76) {
        total = 7.00 + extraPkgCost;
        aioText = '$7.00';
      } else if (billableWeight <= 5.5) {
        total = 10.00 + extraPkgCost;
        aioText = '$10.00';
      } else {
        let handlingFee = 2.50;
        if (billableWeight > 15 && billableWeight <= 30) handlingFee = 3.25;
        else if (billableWeight > 30 && billableWeight <= 50) handlingFee = 4.50;
        else if (billableWeight > 50 && billableWeight <= 70) handlingFee = 6.35;
        else if (billableWeight > 70 && billableWeight <= 100) handlingFee = 7.75;
        else if (billableWeight > 100) handlingFee = 10.00;

        const zoneFactor = 0.45 * zone;
        const weightFactor = (billableWeight - 1) * 0.85;
        const uspsRate = 5.20 + zoneFactor + weightFactor;
        total = handlingFee + uspsRate + extraPkgCost;
        aioText = `$${handlingFee.toFixed(2)}`;
        shipText = `$${uspsRate.toFixed(2)}`;
      }

      if (resAio) resAio.textContent = aioText;
      if (resPkg) resPkg.textContent = pkgText;
      if (resShip) resShip.textContent = shipText;
      if (resTotal) resTotal.textContent = `$${total.toFixed(2)}`;
    }
    window.calculateFulfillmentCost = calculateFulfillmentCost;

    // Run on DOM ready
    document.addEventListener('DOMContentLoaded', () => {
      initWarehouseGallery();
      calculateFulfillmentCost();
    });
  </script>
"""

    # 1. Generate Vietnamese fulfillment.html in root
    vi_content = (BASE / "pages/fulfillment/vi-fulfillment.html").read_text(encoding="utf-8")
    vi_body = re.sub(r'<script>.*?</script>\s*', '', vi_content, flags=re.DOTALL)
    vi_body_rendered = re.sub(r'<div data-component="cta-form".*?</div>', vi_cta, vi_body)

    # Prepare Header with active fulfillment
    vi_header = header_raw.replace('id="navLinkFulfillment"', 'id="navLinkFulfillment" class="nav-item active"') \
                          .replace('id="langToggle"', 'id="langToggle" onclick="window.location.href=\'en-fulfillment.html\'"') \
                          .replace('<span id="currentLangText">Tiếng Việt</span>', '<span id="currentLangText">English</span>')

    vi_standalone = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SpeeGo Fulfillment - Giải pháp kho vận tối ưu cho doanh nghiệp</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700;1,800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div id="header-container">{vi_header}</div>
  
  <div class="breadcrumb-container" id="appBreadcrumb">
    <div class="container">
      <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <div class="breadcrumb-list" id="breadcrumbList">
          <a href="index.html#/knowledge" class="breadcrumb-link">Trang chủ</a>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-current">Fulfillment</span>
        </div>
      </nav>
    </div>
  </div>

  <main id="app-main">
    {vi_body_rendered}
  </main>

  <div id="footer-container">{footer_raw}</div>

  {scripts_common}
</body>
</html>"""

    (BASE / "fulfillment.html").write_text(vi_standalone, encoding="utf-8")
    print("✓ Created fulfillment.html in root")

    # 2. Generate English en-fulfillment.html in root
    en_content = (BASE / "pages/fulfillment/en-fulfillment.html").read_text(encoding="utf-8")
    en_body = re.sub(r'<script>.*?</script>\s*', '', en_content, flags=re.DOTALL)
    en_body_rendered = re.sub(r'<div data-component="cta-form".*?</div>', en_cta, en_body)

    en_header = header_raw.replace('id="navLinkFulfillment"', 'id="navLinkFulfillment" class="nav-item active"') \
                          .replace('id="langToggle"', 'id="langToggle" onclick="window.location.href=\'fulfillment.html\'"') \
                          .replace('<span id="currentLangText">Tiếng Việt</span>', '<span id="currentLangText">Tiếng Việt</span>') \
                          .replace('id="navLinkImportExport">Xuất nhập khẩu', 'id="navLinkImportExport">Import & Export') \
                          .replace('id="navLinkRoutes">Tuyến vận chuyển', 'id="navLinkRoutes">Shipping Routes') \
                          .replace('id="headerCtaBtn">Nhận tư vấn ↗', 'id="headerCtaBtn">Get in Touch ↗')

    en_footer = footer_raw.replace('Khám phá', 'Explore') \
                          .replace('Kết nối với SpeeGo', 'Connect with SpeeGo') \
                          .replace('Xuất nhập khẩu', 'Import & Export') \
                          .replace('Tuyến vận chuyển', 'Shipping Routes')

    en_standalone = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SpeeGo Fulfillment - Warehouse operations built for your business</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700;1,800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div id="header-container">{en_header}</div>
  
  <div class="breadcrumb-container" id="appBreadcrumb">
    <div class="container">
      <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <div class="breadcrumb-list" id="breadcrumbList">
          <a href="index.html#/en/knowledge" class="breadcrumb-link">Home</a>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-current">Fulfillment</span>
        </div>
      </nav>
    </div>
  </div>

  <main id="app-main">
    {en_body_rendered}
  </main>

  <div id="footer-container">{en_footer}</div>

  {scripts_common}
</body>
</html>"""

    (BASE / "en-fulfillment.html").write_text(en_standalone, encoding="utf-8")
    print("✓ Created en-fulfillment.html in root")

if __name__ == "__main__":
    build_standalone_pages()
