"""
4. Unite -- Calisma Kagitlari PDF ureticisi
Tek PDF: CK1 (2 sayfa) + CK2 (1 sayfa) + CK3 (1 sayfa) = 4 sayfa
Calistir: python pdf_uretim/uret_unite4_calisma_kagitlari.py
"""

import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    register_fonts,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT,
    COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_WRITING_LINE,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as pdf_canvas

register_fonts()

# ── Sayfa yapisi ──────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4   # 595.28 x 841.89 pt
ML   = 2.0 * cm       # sol kenar bosluğu
MR   = 2.0 * cm       # sag kenar bosluğu
MT   = 1.8 * cm       # ust kenar bosluğu
MB   = 1.8 * cm       # alt kenar bosluğu
UW   = PAGE_W - ML - MR       # kullanilabilir genislik: 481.89 pt

CONTENT_TOP = PAGE_H - MT     # 790.87 pt
CONTENT_BOT = MB              # 51.02 pt

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT      = os.path.join(ROOT, 'units', 'unit4')
PDF_PATH = os.path.join(OUT, 'U4_PDF_03_Calisma_Kagitlari.pdf')

COLOR_GREY_DARK   = HexColor('#9CA3AF')
COLOR_VERY_LIGHT_GREY = HexColor('#F9FAFB')

# ── Ortak cizim yardimcilari ──────────────────────────────────────────────────

def hf(c, right_title, page_num=None):
    """Üst ve alt bant (header/footer)."""
    c.saveState()
    c.setStrokeColor(COLOR_ACCENT)
    c.setLineWidth(0.5)
    c.line(ML, PAGE_H - 0.9 * cm, PAGE_W - MR, PAGE_H - 0.9 * cm)
    c.setFont('TR-Italic', 7)
    c.setFillColor(COLOR_MUTED)
    c.drawString(ML, PAGE_H - 0.72 * cm,
                 '4. Ünite: Bilgisayar Destekli Tasarım')
    c.setFont('TR-Bold', 7)
    c.drawRightString(PAGE_W - MR, PAGE_H - 0.72 * cm, right_title)

    c.setStrokeColor(COLOR_LIGHT_GREY)
    c.setLineWidth(0.3)
    c.line(ML, 0.9 * cm, PAGE_W - MR, 0.9 * cm)
    c.setFont('TR-Italic', 6.5)
    c.setFillColor(COLOR_MUTED)
    c.drawString(ML, 0.65 * cm,
                 'Türkiye Yüzyılı Maarif Modeli · '
                 '7. Sınıf Teknoloji ve Tasarım')
    if page_num:
        c.setFont('TR-Regular', 6.5)
        c.drawRightString(PAGE_W - MR, 0.65 * cm, f'Sayfa {page_num}')
    c.restoreState()


def underline_field(c, label_font, label_size, label, x, y, line_w):
    """Etiket + alt çizgi (ad soyad, sınıf no gibi)."""
    c.setFont(label_font, label_size)
    c.setFillColor(COLOR_TEXT)
    c.drawString(x, y, label)
    lw = c.stringWidth(label, label_font, label_size)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.5)
    c.line(x + lw + 2, y - 3, x + lw + 2 + line_w, y - 3)
    return lw + 2 + line_w


def inst_box(c, x, y, w, h, lines):
    """Açık turunculu yönerge kutusu."""
    c.setFillColor(COLOR_VERY_LIGHT)
    c.setStrokeColor(COLOR_LIGHT)
    c.setLineWidth(0.8)
    c.rect(x, y, w, h, fill=1)
    ty = y + h - 11
    for line in lines:
        c.setFont('TR-Regular', 8)
        c.setFillColor(COLOR_TEXT)
        c.drawString(x + 7, ty, line)
        ty -= 12


def view_box(c, x, y, w, h, label, tip=''):
    """Görünüş çizim kutusu."""
    # Arka plan
    c.setFillColor(white)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.8)
    c.rect(x, y, w, h, fill=1)
    # Etiket bandı
    lh = 15
    c.setFillColor(COLOR_LIGHT)
    c.setStrokeColor(COLOR_LIGHT)
    c.rect(x, y + h - lh, w, lh, fill=1, stroke=0)
    c.setFont('TR-Bold', 8)
    c.setFillColor(COLOR_SECONDARY)
    c.drawCentredString(x + w / 2, y + h - lh + 4, label)
    # Alt not
    if tip:
        c.setFont('TR-Italic', 7)
        c.setFillColor(COLOR_GREY_DARK)
        c.drawCentredString(x + w / 2, y + 5, tip)


def hint_box(c, x, y, w, h, lines):
    """Hatırlatma kutusu (ÇK1 sağ üst)."""
    c.setFillColor(COLOR_VERY_LIGHT)
    c.setStrokeColor(COLOR_LIGHT)
    c.setLineWidth(0.5)
    c.rect(x, y, w, h, fill=1)
    ty = y + h - 13
    for i, line in enumerate(lines):
        if i == 0:
            c.setFont('TR-Bold', 8)
            c.setFillColor(COLOR_SECONDARY)
        elif line == '':
            ty -= 4
            continue
        else:
            c.setFont('TR-Regular', 7.5)
            c.setFillColor(COLOR_TEXT)
        c.drawCentredString(x + w / 2, ty, line)
        ty -= 11


# ── ÇK1 ──────────────────────────────────────────────────────────────────────

def produce_ck1(c):

    # ── Sayfa 1: Ön Yüz ──────────────────────────────────────────────────────
    hf(c, 'ÇK1 — Görünüş Çıkarma Kâğıdı', '1 / 2')

    # Başlık
    y = CONTENT_TOP - 18
    c.setFont('TR-Bold', 13)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y,
                 'ÇK1 — Görünüş Çıkarma Kâğıdı')

    # Öğrenci bilgisi
    y -= 22
    underline_field(c, 'TR-Bold', 8.5, 'Ad Soyad:', ML, y, 180)
    underline_field(c, 'TR-Bold', 8.5, 'Sınıf / No:', ML + 236, y, 75)
    underline_field(c, 'TR-Bold', 8.5, 'Nesnenin Adı:', ML + 357, y, 120)

    # Yönerge kutusu
    y -= 10
    IH = 32
    inst_box(c, ML, y - IH, UW, IH, [
        'Cetvel kullanarak seçtiğin nesnenin üst, ön ve yan görünüşlerini'
        ' aşağıdaki kutulara çiz.',
        'Her görünüşte en az 2 ölçü (cm) belirt.'
        ' Görünüşlerin hizalı olmasına dikkat et.',
    ])
    y -= IH + 8

    # Çizim alanı: 2×2 ızgara
    NEDEN_H = 26
    draw_top = y
    draw_bot = CONTENT_BOT + NEDEN_H + 4
    draw_h   = draw_top - draw_bot
    GAP      = 8
    box_h    = (draw_h - GAP) / 2
    box_w    = (UW - GAP) / 2

    xl = ML
    xr = ML + box_w + GAP
    yb = draw_bot
    yt = draw_bot + box_h + GAP

    # Üst Görünüş (sol üst)
    view_box(c, xl, yt, box_w, box_h,
             'ÜST GÖRÜNÜŞ  (Yukarıdan Bakış)',
             'Nesneye tam yukarıdan bak')

    # Hatırlatma (sağ üst)
    hint_box(c, xr, yt, box_w, box_h, [
        'HATIRLATMA',
        '',
        'Görünüşler hizalı olmalı:',
        '• Üst & ön görünüş: aynı genislik',
        '• Ön & yan görünüş: aynı yükseklik',
        '',
        'Çizerken:',
        '• Önce hafif çiz, sonra kalınlaştır',
        '• Cetvel kullan',
        '• En az 2 ölçü yaz (cm)',
        '',
        'Görünüş = Nesneye',
        'tek yönden bakış!',
    ])

    # Ön Görünüş (sol alt)
    view_box(c, xl, yb, box_w, box_h,
             'ÖN GÖRÜNÜŞ  (Önden Bakış)',
             'Nesneye tam önden bak')

    # Yan Görünüş (sağ alt)
    view_box(c, xr, yb, box_w, box_h,
             'YAN GÖRÜNÜŞ  (Yandan Bakış)',
             'Nesneye tam yandan bak')

    # "Bu nesneyi neden seçtim"
    ny = CONTENT_BOT + 12
    c.setFont('TR-Bold', 8.5)
    c.setFillColor(COLOR_TEXT)
    label = 'Bu nesneyi neden seçtim:'
    c.drawString(ML, ny, label)
    lw = c.stringWidth(label, 'TR-Bold', 8.5)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.5)
    c.line(ML + lw + 4, ny - 3, PAGE_W - MR, ny - 3)

    # ── Sayfa 2: Ödev (Arka Yüz) ─────────────────────────────────────────────
    c.showPage()
    hf(c, 'ÇK1 — Ödev (Arka Yüz)', '2 / 2')

    y = CONTENT_TOP - 18
    c.setFont('TR-Bold', 12)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y,
                 'ÇK1 — Arka Yüz: 1. Hafta Ödevi')

    y -= 20
    OH = 40
    inst_box(c, ML, y - OH, UW, OH, [
        'Evden basit bir nesne seç (kutu, fincan, oyuncak, şişe, kalemlik vb.).',
        'Aşağıdaki kutulara üst ve ön görünüşünü çiz.'
        ' Tahmini ölçülerini (cm) belirt.',
        'Nesneyi haftaya atölyeye getir — ÇK1’i de yanında getir!',
    ])
    y -= OH + 10

    # Nesne adı
    c.setFont('TR-Bold', 8.5)
    c.setFillColor(COLOR_TEXT)
    c.drawString(ML, y, 'Nesnenin Adı:')
    nw = c.stringWidth('Nesnenin Adı:', 'TR-Bold', 8.5)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.5)
    c.line(ML + nw + 4, y - 3, ML + nw + 4 + 220, y - 3)
    y -= 16

    # 2 büyük çizim kutusu
    OLCU_H  = 48
    BOX_H2  = y - CONTENT_BOT - OLCU_H - 6
    BOX_W2  = (UW - GAP) / 2

    view_box(c, ML, CONTENT_BOT + OLCU_H + 4, BOX_W2, BOX_H2,
             'ÜST GÖRÜNÜŞ',
             'Yukarıdan çiz')
    view_box(c, ML + BOX_W2 + GAP, CONTENT_BOT + OLCU_H + 4, BOX_W2, BOX_H2,
             'ÖN GÖRÜNÜŞ',
             'Önden çiz')

    # Ölçüler
    oy = CONTENT_BOT + OLCU_H - 4
    c.setFont('TR-Bold', 8.5)
    c.setFillColor(COLOR_TEXT)
    c.drawString(ML, oy, 'Tahmini Ölçüler:')
    tw = c.stringWidth('Tahmini Ölçüler:', 'TR-Bold', 8.5)

    olcu_fields = [
        ('En (genişlik):', ML + tw + 8, 55),
        ('Boy (derinlik):', ML + tw + 8 + 55 + 95, 55),
        ('Yükseklik:', ML + tw + 8 + 55 + 95 + 55 + 95, 55),
    ]
    for lbl, fx, fw in olcu_fields:
        c.setFont('TR-Regular', 8.5)
        c.setFillColor(COLOR_TEXT)
        c.drawString(fx, oy, lbl)
        bw2 = c.stringWidth(lbl, 'TR-Regular', 8.5)
        c.setFont('TR-Regular', 8)
        c.drawString(fx + bw2 + fw + 2, oy, 'cm')
        c.setStrokeColor(COLOR_WRITING_LINE)
        c.setLineWidth(0.5)
        c.line(fx + bw2 + 2, oy - 3, fx + bw2 + 2 + fw, oy - 3)

    # Temel şekiller
    sy = CONTENT_BOT + 18
    c.setFont('TR-Bold', 8.5)
    c.setFillColor(COLOR_TEXT)
    c.drawString(ML, sy, 'Temel şekiller (küp, silindir, küre vb.):')
    sw = c.stringWidth('Temel şekiller (küp, silindir, küre vb.):', 'TR-Bold', 8.5)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.5)
    c.line(ML + sw + 4, sy - 3, PAGE_W - MR, sy - 3)

    c.showPage()


# ── ÇK2 ──────────────────────────────────────────────────────────────────────

def produce_ck2(c):
    hf(c, 'ÇK2 — İzometrik Çizim Kâğıdı')

    # Başlık + öğrenci bilgisi (kompakt)
    y = CONTENT_TOP - 16
    c.setFont('TR-Bold', 11)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y,
                 'ÇK2 — İzometrik Çizim Kâğıdı')

    y -= 18
    underline_field(c, 'TR-Bold', 8, 'Ad Soyad:', ML, y, 200)
    underline_field(c, 'TR-Bold', 8, 'Sınıf / No:', ML + 265, y, 80)
    y -= 8

    # İzometrik nokta ızgarası
    dot_top    = y - 2
    dot_bottom = CONTENT_BOT + 2
    dot_left   = ML - 2
    dot_right  = PAGE_W - MR + 2

    dx = 14.17                         # ~0.5 cm
    dy = dx * math.sqrt(3) / 2         # ~12.27 pt

    dot_color = HexColor('#CACACA')
    c.setFillColor(dot_color)
    c.setStrokeColor(dot_color)

    row = 0
    yy = dot_top
    while yy >= dot_bottom - 1:
        x_off = (dx / 2) if (row % 2 == 1) else 0.0
        xx = dot_left + x_off
        while xx <= dot_right + 1:
            c.circle(xx, yy, 0.7, fill=1, stroke=0)
            xx += dx
        yy -= dy
        row += 1

    # Bölme çizgisi (üst %57, alt %43)
    grid_h = dot_top - dot_bottom
    div_y  = dot_bottom + grid_h * 0.43

    c.setStrokeColor(COLOR_LIGHT)
    c.setLineWidth(1.0)
    c.setDash(5, 5)
    c.line(ML, div_y, PAGE_W - MR, div_y)
    c.setDash()

    def section_label(text, sub, ly):
        bw = 285
        bh = 26
        c.setFillColor(COLOR_VERY_LIGHT)
        c.setStrokeColor(COLOR_LIGHT)
        c.setLineWidth(0.5)
        c.rect(ML, ly, bw, bh, fill=1)
        c.setFont('TR-Bold', 8)
        c.setFillColor(COLOR_SECONDARY)
        c.drawString(ML + 5, ly + bh - 11, text)
        c.setFont('TR-Regular', 7.5)
        c.setFillColor(COLOR_TEXT)
        c.drawString(ML + 5, ly + 3, sub)

    section_label(
        'ETKİNLİK 1 — Küp Çizimi  (Ders 5)',
        '3 farklı boyutta küp çiz. Sonra iki kübü üst üste koy.',
        dot_top - 28,
    )
    section_label(
        'ETKİNLİK 2 — Nesnenin İzometrik Görünüşü  (Ders 6)',
        'Tinkercad’de yapacağın nesnenin izometrik çizimini yap.',
        div_y + 4,
    )

    # İpucu bandı (en alt, içerik altı)
    tip_y = CONTENT_BOT + 2
    c.setFont('TR-Italic', 7)
    c.setFillColor(COLOR_GREY_DARK)
    c.drawString(ML, tip_y,
                 'İpucu: Dikey kenarlar → düz yukarı'
                 '  ·  Yatay kenarlar → 30° sağa veya 30° sola')

    c.showPage()


# ── ÇK3 ──────────────────────────────────────────────────────────────────────

def produce_ck3(c):
    hf(c, 'ÇK3 — Tinkercad Planlama Formu')

    # Başlık
    y = CONTENT_TOP - 18
    c.setFont('TR-Bold', 12)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y,
                 'ÇK3 — Tinkercad Planlama Formu')

    # Öğrenci bilgisi satır 1
    y -= 22
    underline_field(c, 'TR-Bold', 8.5, 'Ad Soyad:', ML, y, 175)
    underline_field(c, 'TR-Bold', 8.5, 'Sınıf / No:', ML + 235, y, 75)
    underline_field(c, 'TR-Bold', 8.5, 'Tarih:', ML + 358, y, 105)

    # Nesne adı
    y -= 18
    c.setFont('TR-Bold', 8.5)
    c.setFillColor(COLOR_TEXT)
    c.drawString(ML, y, 'Modelleyeceğim Nesne:')
    nw = c.stringWidth('Modelleyeceğim Nesne:', 'TR-Bold', 8.5)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.5)
    c.line(ML + nw + 4, y - 3, PAGE_W - MR, y - 3)

    # Yönerge
    y -= 10
    IH = 28
    inst_box(c, ML, y - IH, UW, IH, [
        'Nesneyi temel şekillerden (küp, silindir, küre, koni...) oluşturacaksın.',
        'Her parçayı çiz ve numaralandır; şekil adını'
        ' ve ölçülerini (en × boy × yükseklik, cm) tabloya gir.',
    ])
    y -= IH + 8

    # Ana alan: çizim (sol) + tablo (sağ)
    REM_H   = 52
    content_bot = CONTENT_BOT + REM_H + 6
    content_h   = y - content_bot

    draw_w  = UW * 0.52
    GAP     = 8
    tbl_w   = UW - draw_w - GAP
    tbl_x   = ML + draw_w + GAP

    # Çizim alanı (sol)
    c.setFillColor(white)
    c.setStrokeColor(COLOR_WRITING_LINE)
    c.setLineWidth(0.8)
    c.rect(ML, content_bot, draw_w, content_h, fill=1)
    lh = 15
    c.setFillColor(COLOR_LIGHT)
    c.setStrokeColor(COLOR_LIGHT)
    c.rect(ML, content_bot + content_h - lh, draw_w, lh, fill=1, stroke=0)
    c.setFont('TR-Bold', 8)
    c.setFillColor(COLOR_SECONDARY)
    c.drawCentredString(ML + draw_w / 2, content_bot + content_h - lh + 4,
                        'Nesnenin Parçalarını Çiz ve Etiketle')
    c.setFont('TR-Italic', 7)
    c.setFillColor(COLOR_GREY_DARK)
    c.drawCentredString(ML + draw_w / 2, content_bot + 6,
                        'Her parçaya numara ver (1, 2, 3...)')

    # Tablo
    HDR_H   = 20
    COL_H   = 22
    NUM_ROWS = 9
    total_tbl_h = HDR_H + COL_H + NUM_ROWS * ((content_h - HDR_H - COL_H) / NUM_ROWS)
    row_h   = (content_h - HDR_H - COL_H) / NUM_ROWS

    # Tablo başlık bandı
    c.setFillColor(COLOR_PRIMARY)
    c.setStrokeColor(COLOR_PRIMARY)
    c.rect(tbl_x, content_bot + content_h - HDR_H, tbl_w, HDR_H, fill=1, stroke=0)
    c.setFont('TR-Bold', 8)
    c.setFillColor(white)
    c.drawCentredString(tbl_x + tbl_w / 2,
                        content_bot + content_h - HDR_H + 6,
                        'PARÇA TABLOSU')

    # Sütun başlıkları
    col_hdr_y = content_bot + content_h - HDR_H - COL_H
    # Sütun genişlikleri (No | Temel Şekil | Ölçüler | İşlem)
    cw = [tbl_w * p for p in [0.11, 0.28, 0.38, 0.23]]
    col_labels = [
        'No', 'Temel Şekil',
        'En×Boy×Yük. (cm)', 'İşlem'
    ]
    col_sub = ['', '', '(yaklaşık)', 'Ekle/Delik/İkisi']

    c.setFillColor(COLOR_LIGHT)
    c.setStrokeColor(COLOR_LIGHT_GREY)
    c.setLineWidth(0.4)
    c.rect(tbl_x, col_hdr_y, tbl_w, COL_H, fill=1)

    cx = tbl_x
    for i, (lbl, sub, cw_i) in enumerate(zip(col_labels, col_sub, cw)):
        if i > 0:
            c.setStrokeColor(COLOR_LIGHT_GREY)
            c.line(cx, col_hdr_y, cx, col_hdr_y + COL_H)
        c.setFont('TR-Bold', 7)
        c.setFillColor(COLOR_SECONDARY)
        c.drawCentredString(cx + cw_i / 2, col_hdr_y + COL_H - 10, lbl)
        if sub:
            c.setFont('TR-Italic', 6)
            c.setFillColor(COLOR_MUTED)
            c.drawCentredString(cx + cw_i / 2, col_hdr_y + 3, sub)
        cx += cw_i

    # Satırlar
    for row in range(NUM_ROWS):
        ry = col_hdr_y - (row + 1) * row_h
        bg = white if row % 2 == 0 else HexColor('#FFF7ED')
        c.setFillColor(bg)
        c.setStrokeColor(COLOR_LIGHT_GREY)
        c.setLineWidth(0.3)
        c.rect(tbl_x, ry, tbl_w, row_h, fill=1)
        # Numara
        c.setFont('TR-Bold', 8)
        c.setFillColor(COLOR_SECONDARY)
        c.drawCentredString(tbl_x + cw[0] / 2, ry + row_h / 2 - 4, str(row + 1))
        # Sütun çizgisi
        cx = tbl_x + cw[0]
        for cw_i in cw[1:]:
            c.setStrokeColor(COLOR_LIGHT_GREY)
            c.line(cx, ry, cx, ry + row_h)
            cx += cw_i

    # Tablo dış çerçevesi
    tbl_total_h = HDR_H + COL_H + NUM_ROWS * row_h
    c.setStrokeColor(COLOR_LIGHT_GREY)
    c.setLineWidth(0.8)
    c.rect(tbl_x, content_bot + content_h - tbl_total_h,
           tbl_w, tbl_total_h, fill=0)

    # Hatırlatma kutusu (alt)
    c.setFillColor(COLOR_VERY_LIGHT)
    c.setStrokeColor(COLOR_LIGHT)
    c.setLineWidth(0.8)
    c.rect(ML, CONTENT_BOT + 2, UW, REM_H, fill=1)
    c.setFont('TR-Bold', 8)
    c.setFillColor(COLOR_SECONDARY)
    c.drawString(ML + 6, CONTENT_BOT + REM_H - 11,
                 'TİNKERCAD HATIRLAT MALARI')
    rem_items = [
        'Şekil ekle: Sağ panelden çalışma düzlemine sürükle',
        'Ölçü gir: Şekli seç → beyaz kutucuklara sayı yaz  '
        '(mm cinsinden!  →  1 cm = 10 mm)',
        'Delik (Hole): Şekli seç → sağ panelde “Hole” tıkla '
        '(gri olur) → diğeriyle Ctrl+G ile grupla',
        'Gruplama: İki şekli seç (Shift+tıkla) → Ctrl+G',
    ]
    ry2 = CONTENT_BOT + REM_H - 23
    for item in rem_items:
        c.setFont('TR-Regular', 7)
        c.setFillColor(COLOR_TEXT)
        c.drawString(ML + 8, ry2, '• ' + item)
        ry2 -= 9.5

    c.showPage()


# ── Ana ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    c = pdf_canvas.Canvas(PDF_PATH, pagesize=A4)
    produce_ck1(c)
    produce_ck2(c)
    produce_ck3(c)
    c.save()
    print(f'PDF uretildi: {PDF_PATH}')
