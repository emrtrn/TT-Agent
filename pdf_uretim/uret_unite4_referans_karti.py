"""
4. Unite - Arac Referans Karti PDF ureticisi (A5 cift yuzlu)
On yuz: MS Paint araclari (2B)
Arka yuz: Tinkercad araclari (3B)
Calistir: python pdf_uretim/uret_unite4_referans_karti.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)

from pdf_style import (
    register_fonts,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_VERY_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED, COLOR_LIGHT_GREY, COLOR_WRITING_LINE,
    HorizontalLine,
)

register_fonts()

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(ROOT, 'units', 'unit4', 'U4_PDF_Arac_Referans_Karti.pdf')

PAGE_W, PAGE_H = A5   # 419.53 x 595.28 pt

# Usable width: PAGE_W - 2x leftMargin = 419.53 - 2*28.35 = 362.83 pt
USABLE = 362.83

# ── Dokuman ──────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A5,
    topMargin=1.2 * cm,
    bottomMargin=1.2 * cm,
    leftMargin=1.0 * cm,
    rightMargin=1.0 * cm,
    title='4. Unite Arac Referans Karti',
    author='Teknoloji ve Tasarim',
)

# ── Stiller ──────────────────────────────────────────────────────────────────
s_title = ParagraphStyle('s_title', fontName='TR-Bold', fontSize=12,
    textColor=COLOR_PRIMARY, spaceAfter=2, leading=15)

s_subtitle = ParagraphStyle('s_subtitle', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_MUTED, spaceAfter=4, leading=10)

s_section = ParagraphStyle('s_section', fontName='TR-Bold', fontSize=7.5,
    textColor=COLOR_SECONDARY, spaceAfter=1, spaceBefore=3, leading=10)

s_body = ParagraphStyle('s_body', fontName='TR-Regular', fontSize=7,
    textColor=COLOR_TEXT, spaceAfter=2, leading=9.5)

s_small = ParagraphStyle('s_small', fontName='TR-Regular', fontSize=6.5,
    textColor=COLOR_TEXT, leading=9)

s_small_bold = ParagraphStyle('s_small_bold', fontName='TR-Bold', fontSize=6.5,
    textColor=COLOR_TEXT, leading=9)

s_mono = ParagraphStyle('s_mono', fontName='TR-Mono', fontSize=7,
    textColor=COLOR_PRIMARY, leading=10,
    backColor=COLOR_VERY_LIGHT, borderPadding=3)

s_warn = ParagraphStyle('s_warn', fontName='TR-Bold', fontSize=7,
    textColor=COLOR_SECONDARY, leading=10, spaceAfter=2,
    backColor=COLOR_LIGHT, borderPadding=4)

s_note = ParagraphStyle('s_note', fontName='TR-Italic', fontSize=6.5,
    textColor=COLOR_MUTED, alignment=TA_CENTER, leading=9)


# ── Sayfa Numarasi (A5) ───────────────────────────────────────────────────────
def add_header_footer(canvas_obj, doc_obj):
    canvas_obj.saveState()
    # Ust cizgi
    canvas_obj.setStrokeColor(COLOR_ACCENT)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(1.0 * cm, PAGE_H - 0.9 * cm,
                    PAGE_W - 1.0 * cm, PAGE_H - 0.9 * cm)
    canvas_obj.setFont('TR-Regular', 6.5)
    canvas_obj.setFillColor(COLOR_MUTED)
    canvas_obj.drawString(1.0 * cm, PAGE_H - 0.75 * cm,
                          'Teknoloji ve Tasarim  -  7. Sinif  -  4. Unite')
    canvas_obj.drawRightString(PAGE_W - 1.0 * cm, PAGE_H - 0.75 * cm,
                               'Bilgisayar Destekli Tasarim - Arac Referans Karti')
    # Alt cizgi
    canvas_obj.setStrokeColor(COLOR_LIGHT_GREY)
    canvas_obj.setLineWidth(0.3)
    canvas_obj.line(1.0 * cm, 0.9 * cm, PAGE_W - 1.0 * cm, 0.9 * cm)
    canvas_obj.setFont('TR-Italic', 6.5)
    canvas_obj.setFillColor(COLOR_MUTED)
    canvas_obj.drawString(1.0 * cm, 0.65 * cm, 'Turkiye Yuzyili Maarif Modeli')
    canvas_obj.setFont('TR-Regular', 6.5)
    canvas_obj.drawRightString(PAGE_W - 1.0 * cm, 0.65 * cm,
                               f'Sayfa {doc_obj.page}')
    canvas_obj.restoreState()


# ── Tablo Stili Yardimcilari ─────────────────────────────────────────────────
def tbl_style(header_cols=None):
    """Kompakt tablo stili"""
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR',  (0, 0), (-1, 0), white),
        ('FONTNAME',   (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTSIZE',   (0, 0), (-1, 0), 6.5),
        ('ALIGN',      (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 3),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 3),
        ('FONTNAME',   (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',   (0, 1), (-1, -1), 6.5),
        ('TEXTCOLOR',  (0, 1), (-1, -1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',       (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',  (0, 0), (-1, 0), 1.2, COLOR_SECONDARY),
    ]
    return TableStyle(cmds)


def tbl_style_mono(bold_col=0):
    """Kisayol tablosu: ilk sutun mono font"""
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR',  (0, 0), (-1, 0), white),
        ('FONTNAME',   (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTSIZE',   (0, 0), (-1, 0), 6.5),
        ('ALIGN',      (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 3),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 3),
        ('FONTNAME',   (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',   (0, 1), (-1, -1), 6.5),
        ('TEXTCOLOR',  (0, 1), (-1, -1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',       (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',  (0, 0), (-1, 0), 1.2, COLOR_SECONDARY),
        ('FONTNAME',   (bold_col, 1), (bold_col, -1), 'TR-Bold'),
        ('TEXTCOLOR',  (bold_col, 1), (bold_col, -1), COLOR_PRIMARY),
        ('ALIGN',      (bold_col, 1), (bold_col, -1), 'CENTER'),
    ]
    return TableStyle(cmds)


def sp(h=0.15):
    return Spacer(1, h * cm)

def hl():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.4)


# ── ICERIK ───────────────────────────────────────────────────────────────────
elements = []


# ============================================================
#  ON YUZ — MS PAINT ARACLARI
# ============================================================

elements.append(Paragraph('MS PAINT ARAÇLARI — 2B TASARIM', s_title))
elements.append(Paragraph('4. Ünite — Araç Referans Kartı  |  Ön Yüz', s_subtitle))
elements.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
elements.append(sp(0.05))

# Ogrenci bilgisi
info_data = [[
    Paragraph('<b>Adı Soyadı:</b>', s_small), '',
    '', Paragraph('<b>Sınıf / No:</b>', s_small), '', '',
]]
info_tbl = Table(
    info_data,
    colWidths=[1.8*cm, 5.0*cm, 0.3*cm, 1.8*cm, 2.4*cm, 0.5*cm],
)
info_tbl.setStyle(TableStyle([
    ('LINEBELOW', (1, 0), (1, 0), 0.6, COLOR_WRITING_LINE),
    ('LINEBELOW', (4, 0), (4, 0), 0.6, COLOR_WRITING_LINE),
    ('VALIGN',      (0, 0), (-1, -1), 'BOTTOM'),
    ('TOPPADDING',    (0, 0), (-1, -1), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ('LEFTPADDING',   (0, 0), (-1, -1), 1),
    ('RIGHTPADDING',  (0, 0), (-1, -1), 1),
]))
elements.append(info_tbl)
elements.append(sp(0.2))

# ── Ana Araclar Tablosu ──────────────────────────────────────
elements.append(Paragraph('ANA ARAÇLAR', s_section))

paint_tools = [
    [Paragraph('<b>Araç</b>', s_small_bold),
     Paragraph('<b>Ne Yapar?</b>', s_small_bold),
     Paragraph('<b>Nasıl Kullanılır?</b>', s_small_bold)],
    [Paragraph('Dikdörtgen', s_small),
     Paragraph('Kare ve dikdörtgen çizer', s_small),
     Paragraph('Tıkla + sürükle', s_small)],
    [Paragraph('Elips', s_small),
     Paragraph('Daire ve oval çizer', s_small),
     Paragraph('Tıkla + sürükle', s_small)],
    [Paragraph('Çizgi', s_small),
     Paragraph('Düz çizgi çeker', s_small),
     Paragraph('Tıkla + sürükle', s_small)],
    [Paragraph('Dolgu (Kova)', s_small),
     Paragraph('Alanı renkle doldurur', s_small),
     Paragraph('Renk seç, sonra tıkla', s_small)],
    [Paragraph('Metin (A)', s_small),
     Paragraph('Yazı ekler', s_small),
     Paragraph('Alan çiz, yaz', s_small)],
    [Paragraph('Silgi', s_small),
     Paragraph('Çizimi siler', s_small),
     Paragraph('Üzerinden geç', s_small)],
    [Paragraph('Renk Seçici', s_small),
     Paragraph('Rengi kopyalar', s_small),
     Paragraph('Renk almak için tıkla', s_small)],
]
# Sutunlar: 2.6 + 4.6 + 5.6 = 12.8 cm => ~363 pt
paint_tbl = Table(paint_tools, colWidths=[2.6*cm, 4.8*cm, 5.4*cm])
paint_tbl.setStyle(tbl_style())
elements.append(paint_tbl)
elements.append(sp(0.1))

# ── Kisayollar ──────────────────────────────────────────────
elements.append(Paragraph('ÖNEMLİ KLAVYE KISAYOLLARI', s_section))

shortcuts = [
    [Paragraph('<b>Kısayol</b>', s_small_bold),
     Paragraph('<b>İşlem</b>', s_small_bold)],
    ['Ctrl + Z', Paragraph('Geri al — hata yaptıysam!', s_small)],
    ['Ctrl + S', Paragraph('Kaydet (sık kullan!)', s_small)],
    ['Ctrl + C / V', Paragraph('Kopyala / Yapıştır', s_small)],
    ['Ctrl + A', Paragraph('Tümünü seç', s_small)],
    ['Shift + çiz', Paragraph('Kare / tam daire (orantılı)', s_small)],
]
# Sutunlar: 3.0 + 9.8 = 12.8 cm
ks_tbl = Table(shortcuts, colWidths=[3.0*cm, 9.8*cm])
ks_tbl.setStyle(tbl_style_mono(bold_col=0))
elements.append(ks_tbl)
elements.append(sp(0.2))

# ── Dosya Kaydetme ──────────────────────────────────────────
elements.append(Paragraph('DOSYA KAYDETME', s_section))

kaydet_data = [
    [Paragraph('<b>Adım</b>', s_small_bold),
     Paragraph('<b>İşlem</b>', s_small_bold)],
    ['1', Paragraph('Dosya → Farklı Kaydet → PNG', s_small)],
    ['2', Paragraph('Ad_Soyad_2B.png  (boşluk ve Türkçe karakter kullanma)', s_small)],
    ['3', Paragraph('Kayıt yeri: Masaüstü veya öğretmenin gösterdiği klasör', s_small)],
]
kaydet_tbl = Table(kaydet_data, colWidths=[0.8*cm, 12.0*cm])
kaydet_tbl.setStyle(tbl_style_mono(bold_col=0))
elements.append(kaydet_tbl)
elements.append(sp(0.2))

# ── Kontrol Listesi ─────────────────────────────────────────
elements.append(Paragraph('TESLİM ÖNCESİ KONTROL', s_section))

kontrol_data = [
    [Paragraph('<b>?</b>', s_small_bold),
     Paragraph('<b>Kontrol</b>', s_small_bold)],
    ['', Paragraph('3 görünüş var: üst · ön · yan', s_small)],
    ['', Paragraph('Her görünüşün adı yazılmış', s_small)],
    ['', Paragraph('En az 2 ölçü (cm) belirtilmiş', s_small)],
    ['', Paragraph('Dosya kaydedildi (Ad_Soyad_2B.png)', s_small)],
]
kontrol_tbl = Table(kontrol_data, colWidths=[0.8*cm, 12.0*cm])
kontrol_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
    ('TEXTCOLOR',  (0, 0), (-1, 0), white),
    ('FONTNAME',   (0, 0), (-1, 0), 'TR-Bold'),
    ('FONTSIZE',   (0, 0), (-1, 0), 7),
    ('ALIGN',      (0, 0), (-1, 0), 'CENTER'),
    ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING',    (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ('LEFTPADDING',   (0, 0), (-1, -1), 3),
    ('RIGHTPADDING',  (0, 0), (-1, -1), 3),
    ('FONTNAME',   (0, 1), (-1, -1), 'TR-Regular'),
    ('FONTSIZE',   (0, 1), (-1, -1), 7),
    ('TEXTCOLOR',  (0, 1), (-1, -1), COLOR_TEXT),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('GRID',       (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
    ('LINEBELOW',  (0, 0), (-1, 0), 1.2, COLOR_SECONDARY),
    # Kontrol kutusu: bos alan gibi cerceveli
    ('BOX',        (0, 1), (0, -1), 0.6, COLOR_MUTED),
    ('ALIGN',      (0, 1), (0, -1), 'CENTER'),
]))
elements.append(kontrol_tbl)


# ============================================================
#  ARKA YUZ — TINKERCAD ARACLARI
# ============================================================
elements.append(PageBreak())

elements.append(Paragraph('TİNKERCAD ARAÇLARI — 3B TASARIM', s_title))
elements.append(Paragraph('4. Ünite — Araç Referans Kartı  |  Arka Yüz', s_subtitle))
elements.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
elements.append(sp(0.15))

# ── Temel Islemler Tablosu ──────────────────────────────────
elements.append(Paragraph('TEMEL ARAÇLAR VE İŞLEMLER', s_section))

tc_tools = [
    [Paragraph('<b>Araç / İşlem</b>', s_small_bold),
     Paragraph('<b>Nasıl Yapılır?</b>', s_small_bold)],
    [Paragraph('Şekil ekle', s_small),
     Paragraph('Sağ panelden şekli düzleme sürükle', s_small)],
    [Paragraph('Ölçü değiştir', s_small),
     Paragraph('Şekli seç → beyaz kutucuklara sayı gir (mm)', s_small)],
    [Paragraph('Hareket ettir', s_small),
     Paragraph('Şekli tıkla + sürükle', s_small)],
    [Paragraph('Yükseklik ayarla', s_small),
     Paragraph('Şekli seç → üstteki siyah kona tıkla + sürükle', s_small)],
    [Paragraph('Döndür', s_small),
     Paragraph('Şekli seç → kavisli oku tıkla + sürükle', s_small)],
    [Paragraph('Kopyala / Yapıştır', s_small),
     Paragraph('Ctrl+C → Ctrl+V', s_small)],
    [Paragraph('Sil', s_small),
     Paragraph('Şekli seç → Delete tuşu', s_small)],
    [Paragraph('<b>Gruplama</b>', s_small_bold),
     Paragraph('<b>İki şekli seç (Shift+tık) → Ctrl+G</b>', s_small_bold)],
    [Paragraph('Grubu Çöz', s_small),
     Paragraph('Grubu seç → Ctrl+Shift+G', s_small)],
    [Paragraph('<b>Delik (Hole)</b>', s_small_bold),
     Paragraph('<b>Şekli seç → sağ panelde "Hole" tıkla (gri olur)</b>', s_small_bold)],
    [Paragraph('Geri Al', s_small),
     Paragraph('Ctrl+Z', s_small)],
    [Paragraph('Hepsini Seç', s_small),
     Paragraph('Ctrl+A', s_small)],
]
# Sutunlar: 3.2 + 9.6 = 12.8 cm
tc_tbl = Table(tc_tools, colWidths=[3.2*cm, 9.6*cm])
tc_tbl.setStyle(tbl_style())
elements.append(tc_tbl)
elements.append(sp(0.2))

# ── Delik Kullanimi ─────────────────────────────────────────
elements.append(KeepTogether([
    Paragraph('DELİK (HOLE) KULLANIMI', s_section),
    Paragraph(
        '1. Silindir ekle  →  '
        '2. "Hole" tıkla (gri olur)  →  '
        '3. Diğer nesnenin üzerine yerleştir  →  '
        '4. İkisini seç (Shift+tık)  →  '
        '5. Ctrl+G ile grupla  →  Delik açıldı!',
        s_body,
    ),
    sp(0.1),
]))

# ── Goruntuye Kisayollar ────────────────────────────────────
elements.append(Paragraph('GÖRÜNTÜ KISIAYOLLARI', s_section))

goruntu = [
    [Paragraph('<b>Kısayol</b>', s_small_bold),
     Paragraph('<b>İşlem</b>', s_small_bold)],
    ['F', Paragraph('Tüm modeli ekrana sığdır', s_small)],
    ['Fare tekerleği', Paragraph('Yaklaştır / uzaklaştır', s_small)],
    ['Sağ tık + sürükle', Paragraph('Görüntüyü döndür', s_small)],
    ['Orta tık + sürükle', Paragraph('Görüntüyü kaydır', s_small)],
]
goruntu_tbl = Table(goruntu, colWidths=[3.8*cm, 9.0*cm])
goruntu_tbl.setStyle(tbl_style_mono(bold_col=0))
elements.append(goruntu_tbl)
elements.append(sp(0.2))

# ── Dosya Adlandirma ve Kayit ───────────────────────────────
elements.append(KeepTogether([
    Paragraph('DOSYA ADLANDIRMA', s_section),
    Table(
        [
            [Paragraph('<b>Dosya</b>', s_small_bold),
             Paragraph('<b>Ad</b>', s_small_bold)],
            [Paragraph('3B model (Tinkercad\'de)', s_small),
             Paragraph('Ad_Soyad_3B', s_small)],
            [Paragraph('Ekran görüntüsü 1', s_small),
             Paragraph('Ad_Soyad_3B_1.png', s_small)],
            [Paragraph('Ekran görüntüsü 2', s_small),
             Paragraph('Ad_Soyad_3B_2.png', s_small)],
        ],
        colWidths=[4.8*cm, 8.0*cm],
        style=tbl_style(),
    ),
    sp(0.15),
]))

# ── Ekran Goruntusu ─────────────────────────────────────────
elements.append(KeepTogether([
    Paragraph('EKRAN GÖRÜNTÜSÜ ALMA', s_section),
    Table(
        [
            [Paragraph('<b>Yöntem</b>', s_small_bold),
             Paragraph('<b>Adımlar</b>', s_small_bold)],
            [Paragraph('Snipping Tool', s_small),
             Paragraph('Başlat → Snipping Tool → Yeni → Alanı seç', s_small)],
            [Paragraph('Klavye kısayolu', s_small),
             Paragraph('Windows + Shift + S', s_small)],
        ],
        colWidths=[3.2*cm, 9.6*cm],
        style=tbl_style(),
    ),
    sp(0.15),
]))

# ── Kayit Uyarisi ───────────────────────────────────────────
elements.append(Paragraph(
    'Tinkercad buluta otomatik kaydeder — ama hesabınıza giriş yapmalısınız! '
    'Giriş yoksa → kayıt yok → çalışma kaybolur!',
    s_warn,
))

elements.append(sp(0.15))
elements.append(Paragraph(
    'Türkiye Yüzyılı Maarif Modeli · 7. Sınıf Teknoloji ve Tasarım · 4. Ünite: Bilgisayar Destekli Tasarım',
    s_note,
))


# ── Olustur ──────────────────────────────────────────────────────────────────
doc.build(
    elements,
    onFirstPage=add_header_footer,
    onLaterPages=add_header_footer,
)

try:
    from pypdf import PdfReader
    r = PdfReader(PDF_PATH)
    print(f'Referans karti PDF uretildi: {PDF_PATH}')
    print(f'Toplam sayfa: {len(r.pages)}')
except ImportError:
    print(f'Referans karti PDF uretildi: {PDF_PATH}')
