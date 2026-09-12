"""
3. Unıte — Surec Akis Posteri PDF üretici (A3 dikey)
Çalistir: python pdf_uretim/uret_unite3_surec_posteri.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white

from pdf_style import (
    register_fonts, COLOR_PRIMARY, COLOR_SECONDARY,
    COLOR_MUTED, COLOR_LIGHT_GREY, COLOR_ACCENT
)

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(ROOT, 'units', 'unit3', 'Unite3_Surec_Posteri.pdf')

PAGE_W, PAGE_H = A3   # 841.89 x 1190.55 pt  (dikey/portrait)
MARGIN = 1.5 * cm     # 42.52 pt
TW     = PAGE_W - 2 * MARGIN  # 756.85 pt  (~26.7 cm)

# ── Renk Paleti ─────────────────────────────────────────────────────────────
STEP_COLORS = [
    HexColor('#DC2626'),  # 1  Problem
    HexColor('#D97706'),  # 2  Analiz
    HexColor('#15803D'),  # 3  Fikir
    HexColor('#1D4ED8'),  # 4  Eskiz
    HexColor('#1E40AF'),  # 5  Uygulama
    HexColor('#7E22CE'),  # 6  Test
    HexColor('#166534'),  # 7  Revize
]

STEP_BG = [
    HexColor('#FEF2F2'),
    HexColor('#FFFBEB'),
    HexColor('#F0FDF4'),
    HexColor('#EFF6FF'),
    HexColor('#EFF6FF'),
    HexColor('#FAF5FF'),
    HexColor('#F0FDF4'),
]

# ── Adim Verileri ────────────────────────────────────────────────────────────
STEPS = [
    {
        'no': '1', 'ad': 'PROBLEM TESPİTİ',
        'soru': 'Kim ne yaşıyor?',
        'aciklama': 'Günlük hayatta insanların yaşadığı gerçek bir güçlüğü gözlemle ve tanımla.',
        'arac': 'Araç: Problem Tespiti Formu (ÇK1)',
    },
    {
        'no': '2', 'ad': 'ANALİZ / EMPATİ',
        'soru': 'Kullanıcım ne hissediyor?',
        'aciklama': 'Problemi yaşayan kişinin yerine geç. Gözlem yap, sorular sor, hislerini anla.',
        'arac': 'Araç: Empati Haritası (ÇK2)  |  Kullanıcı Analiz Tablosu (ÇK3)',
    },
    {
        'no': '3', 'ad': 'FİKİR ÜRETİMİ',
        'soru': 'Nasıl çözebiliriz?',
        'aciklama': 'Eleştiri yok, sınır yok. Ne kadar çok fikir o kadar iyi. Sonra en iyisini seç.',
        'arac': 'Araç: Crazy 8 (ÇK4)  |  Fikir Seçim Matrisi (ÇK5)',
    },
    {
        'no': '4', 'ad': 'ESKİZ / TASLAK',
        'soru': 'Nasıl görünür ve ne gerekir?',
        'aciklama': 'Fikri kâğıda dökuyoruz. Mükemmel çizim şart değil — fikri aktarması yeterli.',
        'arac': 'Araç: Tasarım Eskizi Sayfası (ÇK6)  |  Malzeme Planlama Tablosu (ÇK7)',
    },
    {
        'no': '5', 'ad': 'UYGULAMA (PROTOTİP)',
        'soru': 'Gerçekten yapabilir miyim?',
        'aciklama': 'Eskizi üç boyutlu bir modele dönüştür. Bu mükemmel son ürün değil, bir denemedir.',
        'arac': 'Araç: Prototip Süreç Günlüğü (ÇK8)',
    },
    {
        'no': '6', 'ad': 'TEST / GERİ BİLDİRİM',
        'soru': 'Kullanıcım ne düşünüyor?',
        'aciklama': 'Prototipini gerçek bir kullanıcıya dene. Eleştiriyi dinle, not al.',
        'arac': 'Araç: Ürün Test ve Geri Bildirim Formu (ÇK9)',
    },
    {
        'no': '7', 'ad': 'REVİZE',
        'soru': 'Nasıl daha iyi olur?',
        'aciklama': 'Geri bildirimlere göre iyileştir. Ergonomiyi ve sürdürülebilirliği de kontrol et.',
        'arac': 'Araç: Revize Planı + Sürdürülebilirlik Kontrolü (ÇK10)',
    },
]

KAVRAMLAR = [
    ('Prototip',           'Test için yapılan deneme modeli'),
    ('Ergonomi',           'İnsan vücuduna uygun tasarım'),
    ('Sürdürülebilirlik',  'Geleceği gözeten tasarım'),
    ('Empati',             'Kullanıcının yerine geçmek'),
    ('İnovasyon',          'Özgün çözüm üretmek'),
    ('Geri Bildirim',      'Kullanıcı değerlendirmesi'),
    ('Özgünlük',           'Kendine özgü tasarım'),
]


# ── Yardimci Fonksiyonlar ────────────────────────────────────────────────────

def wrap_text(c, text, font, size, max_width):
    """Metni satirlara sar, liste dondur."""
    words = text.split()
    lines, cur = [], ''
    for word in words:
        test = (cur + ' ' + word).strip()
        if c.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_step_box(c, x, y, w, h, step, color, bg_color):
    """
    x, y  : alt-sol kose (ReportLab koordinatlari)
    w, h  : genislik / yukseklik
    """
    # Arka plan + cerceve
    c.setFillColor(bg_color)
    c.setStrokeColor(color)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 8, stroke=1, fill=1)

    # Sol vurgu bandi
    BAR_W = 1.1 * cm
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.setLineWidth(0)
    c.roundRect(x, y, BAR_W, h, 8, stroke=0, fill=1)
    c.rect(x + BAR_W - 10, y, 10, h, stroke=0, fill=1)   # sag kenari duzlestir

    # Adim numarasi (beyaz, bant merkezinde)
    c.setFillColor(white)
    c.setFont('TR-Bold', 22)
    num_w = c.stringWidth(step['no'], 'TR-Bold', 22)
    c.drawString(x + BAR_W / 2 - num_w / 2, y + h / 2 - 8, step['no'])

    # Icerik alani
    cx  = x + BAR_W + 0.4 * cm
    cw  = w - BAR_W - 0.6 * cm

    # Adim adi (kalin, adim rengi)
    c.setFillColor(color)
    c.setFont('TR-Bold', 13)
    c.drawString(cx, y + h - 0.75 * cm, step['ad'])

    # Anahtar soru (italik, koyu gri)
    c.setFillColor(HexColor('#374151'))
    c.setFont('TR-Italic', 10)
    c.drawString(cx, y + h - 1.35 * cm, '"' + step['soru'] + '"')

    # Aciklama (sarili metin)
    c.setFont('TR-Regular', 9)
    c.setFillColor(HexColor('#1F2937'))
    desc_lines = wrap_text(c, step['aciklama'], 'TR-Regular', 9, cw)
    dy = y + h - 2.05 * cm
    for dl in desc_lines[:2]:
        c.drawString(cx, dy, dl)
        dy -= 0.42 * cm

    # Arac referansi (alt, kucuk italik gri)
    c.setFont('TR-Italic', 8)
    c.setFillColor(HexColor('#6B7280'))
    c.drawString(cx, y + 0.38 * cm, step['arac'])


def draw_down_arrow(c, cx, y_top, y_bot, color):
    """Asagi ok (y_top > y_bot, gorsel olarak asagi)."""
    shaft_end = y_bot + 7
    c.setStrokeColor(color)
    c.setLineWidth(1.8)
    c.line(cx, y_top, cx, shaft_end)
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(cx, y_bot)
    p.lineTo(cx - 5, shaft_end)
    p.lineTo(cx + 5, shaft_end)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


# ── PDF Olustur ──────────────────────────────────────────────────────────────

c = pdfcanvas.Canvas(PDF_PATH, pagesize=A3)

BOX_H = 4.2 * cm   # Adim kutusu yuksekligi
GAP   = 0.5 * cm   # Kutular arasi bosluk

# Baslik bolumu
y = PAGE_H - MARGIN

c.setFillColor(COLOR_PRIMARY)
c.setFont('TR-Bold', 30)
c.drawString(MARGIN, y - 30, 'TASARIM ODAKLI DÜŞÜNME')
y -= 42

c.setFillColor(HexColor('#6B7280'))
c.setFont('TR-Regular', 13)
c.drawString(MARGIN, y - 14, 'Bir Fikri Gerçeğe Dönüştürmenin 7 Adımı   '
             + chr(8226) + '   7. Sınıf Teknoloji ve Tasarım')
y -= 26

c.setStrokeColor(COLOR_PRIMARY)
c.setLineWidth(2)
c.line(MARGIN, y - 6, PAGE_W - MARGIN, y - 6)
y -= 18

# Adim kutulari
current_y = y
for i, step in enumerate(STEPS):
    box_y = current_y - BOX_H
    draw_step_box(c, MARGIN, box_y, TW, BOX_H, step, STEP_COLORS[i], STEP_BG[i])
    current_y = box_y
    if i < len(STEPS) - 1:
        draw_down_arrow(
            c,
            MARGIN + TW / 2,
            current_y - 2,
            current_y - GAP + 5,
            STEP_COLORS[i + 1],
        )
        current_y -= GAP

# Dongu notu
note_y = current_y - 0.6 * cm
c.setFillColor(COLOR_PRIMARY)
c.setFont('TR-Bold', 9.5)
note = ('Tasarım asla bitmez. '
        'Revize edilen ürün, yeni bir döngünün başlangıcıdır.   (7 → 1 → 2 → ...)')
c.drawCentredString(PAGE_W / 2, note_y, note)

# Ayirici
sep_y = note_y - 0.45 * cm
c.setStrokeColor(COLOR_LIGHT_GREY)
c.setLineWidth(0.5)
c.line(MARGIN, sep_y, PAGE_W - MARGIN, sep_y)

# Anahtar kavramlar
kav_hdr_y = sep_y - 0.5 * cm
c.setFillColor(COLOR_PRIMARY)
c.setFont('TR-Bold', 10)
c.drawString(MARGIN, kav_hdr_y, 'ANAHTAR KAVRAMLAR')  # noqa: all-caps, no Türkçe issue

kav_y     = kav_hdr_y - 0.45 * cm
kav_col_w = TW / len(KAVRAMLAR)

for i, (kavram, tanim) in enumerate(KAVRAMLAR):
    kx = MARGIN + i * kav_col_w
    if i > 0:
        c.setStrokeColor(COLOR_LIGHT_GREY)
        c.setLineWidth(0.3)
        c.line(kx - 3, kav_y + 4, kx - 3, kav_y - 1.2 * cm)
    c.setFillColor(COLOR_SECONDARY)
    c.setFont('TR-Bold', 8.5)
    c.drawString(kx + 3, kav_y, kavram)
    c.setFillColor(HexColor('#374151'))
    c.setFont('TR-Regular', 7.5)
    for j, tl in enumerate(wrap_text(c, tanim, 'TR-Regular', 7.5, kav_col_w - 8)[:2]):
        c.drawString(kx + 3, kav_y - 0.38 * cm - j * 0.30 * cm, tl)

# Alt marka
c.setFillColor(HexColor('#9CA3AF'))
c.setFont('TR-Italic', 8)
c.drawString(MARGIN, MARGIN - 5, 'Türkiye Yüzyılı Maarif Modeli')
c.drawRightString(PAGE_W - MARGIN, MARGIN - 5,
                  '7. Sınıf Teknoloji ve Tasarım  '
                  + chr(8226) + '  3. Ünite: Tasarım Odaklı Süreç')

c.save()

try:
    from pypdf import PdfReader
    r = PdfReader(PDF_PATH)
    print(f'Poster PDF uretildi: {PDF_PATH}')
    print(f'Toplam sayfa: {len(r.pages)}')
except ImportError:
    print(f'Poster PDF uretildi: {PDF_PATH}')
