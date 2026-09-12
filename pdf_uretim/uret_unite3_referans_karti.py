"""
3. Ünite — Öğrenci Referans Kartı PDF üretici (A5 çift yüzlü)
Ön yüz: 7 adım kontrol listesi + ÇK tablosu + tasarım cümlesi
Arka yüz: 8 anahtar kavram sözlüğü
Çalıştır: python pdf_uretim/uret_unite3_referans_karti.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)

from pdf_style import (
    register_fonts,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_VERY_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED, COLOR_LIGHT_GREY, COLOR_WRITING_LINE,
    HorizontalLine,
)

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(ROOT, 'units', 'unit3', 'Unite3_Referans_Karti.pdf')

PAGE_W, PAGE_H = A5   # 419.53 x 595.28 pt

# ── Dokuman ──────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A5,
    topMargin=1.2 * cm,
    bottomMargin=1.2 * cm,
    leftMargin=1.0 * cm,
    rightMargin=1.0 * cm,
    title='3. Ünite Öğrenci Referans Kartı',
    author='Teknoloji ve Tasarım',
)
doc.doc_title = 'Tasarım Odaklı Süreç — Referans Kartı'
doc.unite_info = 'Teknoloji ve Tasarım  •  7. Sınıf  •  3. Ünite'

# Kullanilabilir genislik: 419.53 - 2x28.35 = 362.83 pt (~12.8 cm)
TW = PAGE_W - 2 * 1.0 * cm   # 399.53... ama plateypus frame genisligi farklidir
# Tablo sutun genisliklerini gercek usable width'e gore ayarla
# usable = PAGE_W - leftMargin - rightMargin = 419.53 - 28.35 - 28.35 = 362.83 pt
USABLE = 362.83

# ── Stiller ──────────────────────────────────────────────────────────────────
s_title = ParagraphStyle('s_title', fontName='TR-Bold', fontSize=12,
    textColor=COLOR_PRIMARY, spaceAfter=3, leading=15)

s_subtitle = ParagraphStyle('s_subtitle', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_MUTED, spaceAfter=5, leading=10)

s_section = ParagraphStyle('s_section', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_SECONDARY, spaceAfter=3, spaceBefore=2, leading=12)

s_body = ParagraphStyle('s_body', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, spaceAfter=3, leading=11)

s_small = ParagraphStyle('s_small', fontName='TR-Regular', fontSize=7,
    textColor=COLOR_TEXT, leading=10)

s_small_bold = ParagraphStyle('s_small_bold', fontName='TR-Bold', fontSize=7,
    textColor=COLOR_TEXT, leading=10)

s_kavram = ParagraphStyle('s_kavram', fontName='TR-Bold', fontSize=9.5,
    textColor=COLOR_PRIMARY, spaceAfter=2, leading=12)

s_tanim = ParagraphStyle('s_tanim', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, spaceAfter=5, leading=11)

s_quote = ParagraphStyle('s_quote', fontName='TR-BoldItalic', fontSize=8.5,
    textColor=COLOR_PRIMARY, alignment=TA_CENTER, spaceAfter=4, leading=12)

s_note_center = ParagraphStyle('s_note_center', fontName='TR-Italic', fontSize=7,
    textColor=COLOR_MUTED, alignment=TA_CENTER, leading=10)


# ── Sayfa Numarasi (A5 icin ozel) ────────────────────────────────────────────
def add_page_number_a5(canvas_obj, doc_obj):
    canvas_obj.saveState()
    # Ust cizgi
    canvas_obj.setStrokeColor(COLOR_ACCENT)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(1.0 * cm, PAGE_H - 0.9 * cm,
                    PAGE_W - 1.0 * cm, PAGE_H - 0.9 * cm)
    # Ust sol
    canvas_obj.setFont('TR-Regular', 6.5)
    canvas_obj.setFillColor(COLOR_MUTED)
    canvas_obj.drawString(1.0 * cm, PAGE_H - 0.75 * cm,
                          'Teknoloji ve Tasarım  •  7. Sınıf  •  3. Ünite')
    # Ust sag
    canvas_obj.drawRightString(PAGE_W - 1.0 * cm, PAGE_H - 0.75 * cm,
                                'Tasarım Odaklı Süreç — Referans Kartı')
    # Alt cizgi
    canvas_obj.setStrokeColor(COLOR_LIGHT_GREY)
    canvas_obj.setLineWidth(0.3)
    canvas_obj.line(1.0 * cm, 0.9 * cm, PAGE_W - 1.0 * cm, 0.9 * cm)
    # Alt sag: sayfa no
    canvas_obj.setFont('TR-Regular', 6.5)
    canvas_obj.drawRightString(PAGE_W - 1.0 * cm, 0.65 * cm,
                                f'Sayfa {doc_obj.page}')
    # Alt sol
    canvas_obj.setFont('TR-Italic', 6.5)
    canvas_obj.drawString(1.0 * cm, 0.65 * cm, 'Türkiye Yüzyılı Maarif Modeli')
    canvas_obj.restoreState()


# ── Flowable Yardimcilari ────────────────────────────────────────────────────
def tablo_stili_kompakt():
    return TableStyle([
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
    ])


# ── ICERIK ───────────────────────────────────────────────────────────────────
elements = []


# ============================================================
#  ON YUZ
# ============================================================
elements.append(Paragraph('TASARIM ODAKLI DÜŞÜNME', s_title))
elements.append(Paragraph('3. Ünite — Öğrenci Referans Kartı', s_subtitle))
elements.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
elements.append(Spacer(1, 0.2 * cm))

# Ogrenci bilgisi
info_data = [[
    Paragraph('<b>Adı Soyadı:</b>', s_small),
    '',
    '',
    Paragraph('<b>Sınıf / No:</b>', s_small),
    '',
    '',
]]
info_tbl = Table(
    info_data,
    colWidths=[1.8 * cm, 4.8 * cm, 0.4 * cm, 2.0 * cm, 2.4 * cm, 0.4 * cm],
)
info_tbl.setStyle(TableStyle([
    ('LINEBELOW', (1, 0), (1, 0), 0.6, COLOR_WRITING_LINE),
    ('LINEBELOW', (4, 0), (4, 0), 0.6, COLOR_WRITING_LINE),
    ('VALIGN',      (0, 0), (-1, -1), 'BOTTOM'),
    ('TOPPADDING',    (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ('LEFTPADDING',   (0, 0), (-1, -1), 1),
    ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
]))
elements.append(info_tbl)
elements.append(Spacer(1, 0.25 * cm))

# ── 7 Adim Kontrol Listesi ──────────────────────────────────
elements.append(Paragraph('7 ADIM KONTROL LİSTESİ', s_section))

step_rows = [
    [
        Paragraph('<b>Adım</b>', s_small_bold),
        Paragraph('<b>Ad</b>', s_small_bold),
        Paragraph('<b>Anahtar Soru</b>', s_small_bold),
        Paragraph('<b>Hafta</b>', s_small_bold),
        Paragraph('<b>Kontrol</b>', s_small_bold),
    ],
    ['1', Paragraph('Problem Tespiti', s_small),
     Paragraph('Kim ne yaşıyor?', s_small), '1', ''],
    ['2', Paragraph('Analiz / Empati', s_small),
     Paragraph('Kullanıcım ne hissediyor?', s_small), '2', ''],
    ['3', Paragraph('Fikir Üretimi', s_small),
     Paragraph('Nasıl çözebiliriz?', s_small), '2', ''],
    ['4', Paragraph('Eskiz / Taslak', s_small),
     Paragraph('Nasıl görünür, ne gerekir?', s_small), '3', ''],
    ['5', Paragraph('Uygulama', s_small),
     Paragraph('Gerçekten yapabilir miyim?', s_small), '3-4', ''],
    ['6', Paragraph('Test', s_small),
     Paragraph('Kullanıcım ne düşünüyor?', s_small), '4', ''],
    ['7', Paragraph('Revize', s_small),
     Paragraph('Nasıl daha iyi olur?', s_small), '5', ''],
]
# Sutunlar: 0.6 + 3.0 + 6.0 + 1.2 + 1.5 = 12.3 cm => ~348 pt (biraz altinda, OK)
step_tbl = Table(
    step_rows,
    colWidths=[0.6 * cm, 3.0 * cm, 6.0 * cm, 1.2 * cm, 1.5 * cm],
)
step_tbl.setStyle(tablo_stili_kompakt())
step_tbl.setStyle(TableStyle([
    *tablo_stili_kompakt()._cmds,
    ('ALIGN', (0, 1), (0, -1), 'CENTER'),
    ('ALIGN', (3, 1), (3, -1), 'CENTER'),
    ('ALIGN', (4, 1), (4, -1), 'CENTER'),
    ('FONTNAME', (0, 1), (0, -1), 'TR-Bold'),
    ('TEXTCOLOR', (0, 1), (0, -1), COLOR_PRIMARY),
]))
elements.append(step_tbl)
elements.append(Spacer(1, 0.25 * cm))

# ── Calisma Kagitlarim ──────────────────────────────────────
elements.append(Paragraph('ÇALIŞMA KÂĞITLARIM', s_section))

ck_rows = [
    [Paragraph('<b>Ders</b>', s_small_bold),
     Paragraph('<b>Çalışma Kâğıdı</b>', s_small_bold),
     Paragraph('<b>Teslim</b>', s_small_bold)],
    ['2',   Paragraph('ÇK1 — Problem Tespiti Formu', s_small), ''],
    ['3',   Paragraph('ÇK2 — Empati Haritası', s_small), ''],
    ['3',   Paragraph('ÇK3 — Kullanıcı Analiz Tablosu', s_small), ''],
    ['4',   Paragraph('ÇK4 — Crazy 8 Beyin Fırtınası', s_small), ''],
    ['4',   Paragraph('ÇK5 — Fikir Seçim Matrisi', s_small), ''],
    ['5',   Paragraph('ÇK6 — Tasarım Eskizi Sayfası', s_small), ''],
    ['5',   Paragraph('ÇK7 — Malzeme Planlama Tablosu', s_small), ''],
    ['6-7', Paragraph('ÇK8 — Prototip Süreç Günlüğü', s_small), ''],
    ['8',   Paragraph('ÇK9 — Ürün Test ve Geri Bildirim Formu', s_small), ''],
    ['9',   Paragraph('ÇK10 — Revize Planı + Sürdürülebilirlik Kontrolü', s_small), ''],
    ['10',  Paragraph('ÇK11 — Tasarım Süreci Sunum Şablonu', s_small), ''],
]
# Sutunlar: 0.8 + 10.6 + 1.4 = 12.8 cm => ~362 pt (tam usable width)
ck_tbl = Table(
    ck_rows,
    colWidths=[0.8 * cm, 10.6 * cm, 1.4 * cm],
)
ck_tbl.setStyle(tablo_stili_kompakt())
ck_tbl.setStyle(TableStyle([
    *tablo_stili_kompakt()._cmds,
    ('ALIGN', (0, 1), (0, -1), 'CENTER'),
    ('ALIGN', (2, 1), (2, -1), 'CENTER'),
]))
elements.append(ck_tbl)
elements.append(Spacer(1, 0.25 * cm))

# ── Tasarim Cumlesi ─────────────────────────────────────────
elements.append(Paragraph('TASARIM CÜMLESİ', s_section))

sentence_style = ParagraphStyle('sentence', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=13, backColor=COLOR_VERY_LIGHT,
    borderPadding=6, spaceAfter=4)
elements.append(Paragraph(
    'Benim tasarımım <b>_______________________</b> için '
    '<b>_______________________</b> yapar, '
    'çünkü <b>_______________________</b>.',
    sentence_style,
))


# ============================================================
#  ARKA YUZ
# ============================================================
elements.append(PageBreak())

elements.append(Paragraph('ANAHTAR KAVRAMLAR', s_title))
elements.append(Paragraph('3. Ünite — Tasarım Odaklı Süreç', s_subtitle))
elements.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
elements.append(Spacer(1, 0.3 * cm))

VOCAB = [
    ('Tasarım Odaklı Düşünme',
     'İnsan ihtiyaçlarını merkeze alarak gerçek sorunlara yaratıcı çözümler geliştirme yaklaşımı.'),
    ('Empati',
     'Problemi yaşayan kişinin yerine geçmek. Ne hissettiği anlaşılmaya çalışılır.'),
    ('Prototip',
     'Tasarım fikrinin test edilmesi için yapılan deneme modeli. Mükemmel olmak zorunda değil.'),
    ('Ergonomi',
     'Ürünün insan vücuduna, hareketlerine ve kullanım alışkanlıklarına uygun tasarlanması.'),
    ('Sürdürülebilirlik',
     'Uzun ömürlü, geri dönüştürülebilir, üretimde az kaynak harcayan ürünler tasarlamak.'),
    ('İnovasyon',
     'Daha önce yapılmamış, özgün bir çözüm üretmek.'),
    ('Geri Bildirim',
     'Kullanıcının ürünü denedikten sonra paylaştığı değerlendirme ve öneriler.'),
    ('Revize',
     'Geri bildirimlere göre tasarımı iyileştirmek. Tasarım döngüsü asla bitmez.'),
]

for kavram, tanim in VOCAB:
    elements.append(Paragraph(kavram, s_kavram))
    elements.append(Paragraph(tanim, s_tanim))
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.4))

elements.append(Spacer(1, 0.4 * cm))
elements.append(Paragraph(
    '"Tasarımcılar asla \'bitti\' demez — \'daha iyi\' der."',
    s_quote,
))
elements.append(Paragraph(
    'Eleştiri, tasarımın düşmanı değil, en iyi arkadaşıdır.',
    s_note_center,
))

# ── Olustur ──────────────────────────────────────────────────────────────────
doc.build(
    elements,
    onFirstPage=add_page_number_a5,
    onLaterPages=add_page_number_a5,
)

try:
    from pypdf import PdfReader
    r = PdfReader(PDF_PATH)
    print(f'Referans karti PDF uretildi: {PDF_PATH}')
    print(f'Toplam sayfa: {len(r.pages)}')
except ImportError:
    print(f'Referans karti PDF uretildi: {PDF_PATH}')
