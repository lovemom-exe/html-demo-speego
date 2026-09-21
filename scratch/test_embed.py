import json
from pathlib import Path

BASE = Path(r'c:\Users\X1 Yoga\html speego')

partials = {
    'partials/header.html': (BASE / 'partials/header.html').read_text(encoding='utf-8'),
    'partials/footer.html': (BASE / 'partials/footer.html').read_text(encoding='utf-8'),
    'partials/cta-form.html': (BASE / 'partials/cta-form.html').read_text(encoding='utf-8')
}

pages = {
    'pages/fulfillment/vi-fulfillment.html': (BASE / 'pages/fulfillment/vi-fulfillment.html').read_text(encoding='utf-8'),
    'pages/fulfillment/en-fulfillment.html': (BASE / 'pages/fulfillment/en-fulfillment.html').read_text(encoding='utf-8'),
    'pages/sourcing/sourcing.html': (BASE / 'pages/sourcing/sourcing.html').read_text(encoding='utf-8'),
    'pages/xuat_nhap_khau/xuat-nhap-khau.html': (BASE / 'pages/xuat_nhap_khau/xuat-nhap-khau.html').read_text(encoding='utf-8'),
    'pages/xuat_nhap_khau/en-xuat-nhap-khau.html': (BASE / 'pages/xuat_nhap_khau/en-xuat-nhap-khau.html').read_text(encoding='utf-8'),
    'pages/tuyen_van_chuyen/tuyen-van-chuyen.html': (BASE / 'pages/tuyen_van_chuyen/tuyen-van-chuyen.html').read_text(encoding='utf-8'),
    'pages/tuyen_van_chuyen/en-tuyen-van-chuyen.html': (BASE / 'pages/tuyen_van_chuyen/en-tuyen-van-chuyen.html').read_text(encoding='utf-8'),
    'pages/Knowledge/VI/vi-01-chuyenmuc-tat-ca-chuyen-muc.html': (BASE / 'pages/Knowledge/VI/vi-01-chuyenmuc-tat-ca-chuyen-muc.html').read_text(encoding='utf-8'),
    'pages/Knowledge/EN/en-01-chuyenmuc-tat-ca-chuyen-muc.html': (BASE / 'pages/Knowledge/EN/en-01-chuyenmuc-tat-ca-chuyen-muc.html').read_text(encoding='utf-8')
}

print('Partials loaded:', len(partials))
print('Pages loaded:', len(pages))
