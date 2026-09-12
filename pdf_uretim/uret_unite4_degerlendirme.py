"""
4. Unite -- Degerlendirme Araclari PDF ureticisi
Tek PDF: Rubrik (2 sayfa) + Gozlem Formu (1 sayfa) + Oz Degerlendirme (1 sayfa) = 4 sayfa
Calistir: python pdf_uretim/uret_unite4_degerlendirme.py
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
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)
from reportlab.pdfgen import canvas as pdf_canvas

register_fonts()

PAGE_W, PAGE_H = A4
ML = 2.0 * cm
MR = 2.0 * cm
MT = 1.8 * cm
MB = 1.8 * cm
UW = PAGE_W - ML - MR        # 481.89 pt

CONTENT_TOP = PAGE_H - MT    # 790.87
CONTENT_BOT = MB             # 51.02

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT      = os.path.join(ROOT, 'units', 'unit4')
PDF_PATH = os.path.join(OUT, 'U4_PDF_04_Degerlendirme.pdf')

TEMP_RUBRIK = os.path.join(OUT, '_temp_rubrik.pdf')
TEMP_CG     = os.path.join(OUT, '_temp_cg.pdf')

COLOR_GREY_DARK = HexColor('#9CA3AF')
COLOR_SCORE_BG  = HexColor('#FFF7ED')

# ── Ortak: header / footer ─────────────────────────────────────────────────────

def hf_canvas(c, right_title, page_info=None):
    """Üst ve alt bant (canvas'a çizer)."""
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
    if page_info:
        c.setFont('TR-Regular', 6.5)
        c.drawRightString(PAGE_W - MR, 0.65 * cm, page_info)
    c.restoreState()


# ══════════════════════════════════════════════════════════════════════════════
# 1. ÜRÜN DEĞERLENDİRME RUBRİĞİ (Platypus)
# ══════════════════════════════════════════════════════════════════════════════

# Sütun genişlikleri (toplam = UW)
RUB_CW = [UW * p for p in [0.22, 0.20, 0.20, 0.18, 0.13, 0.07]]

s_sec_hdr = ParagraphStyle('s_sh', fontName='TR-Bold', fontSize=8.5,
    textColor=white, leading=11)
s_col_hdr = ParagraphStyle('s_ch', fontName='TR-Bold', fontSize=7,
    textColor=COLOR_SECONDARY, alignment=TA_CENTER, leading=9)
s_kriter = ParagraphStyle('s_k', fontName='TR-Bold', fontSize=7.5,
    textColor=COLOR_TEXT, leading=10)
s_desc = ParagraphStyle('s_d', fontName='TR-Regular', fontSize=6.5,
    textColor=COLOR_TEXT, leading=9)
s_yetersiz = ParagraphStyle('s_y', fontName='TR-Regular', fontSize=6.5,
    textColor=HexColor('#DC2626'), leading=9)
s_total_lbl = ParagraphStyle('s_tl', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_PRIMARY, alignment=TA_RIGHT, leading=10)
s_total_val = ParagraphStyle('s_tv', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_PRIMARY, alignment=TA_CENTER, leading=10)

s_body8 = ParagraphStyle('s_b8', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11)
s_bold8 = ParagraphStyle('s_B8', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_TEXT, leading=11)
s_note = ParagraphStyle('s_nt', fontName='TR-Italic', fontSize=7.5,
    textColor=COLOR_MUTED, leading=10)

RUBRIK_SECTIONS = [
    {
        'title': 'BÖLÜM 1 — ÇK1: Görünüş Çıkarma Kâğıdı',
        'weight': '%10', 'max': 12,
        'rows': [
            ('Görünüş\nsayısı',
             'Üç görünüş eksiksiz ve doğru adlandırılmış',
             'Üç görünüş var, adlandırma eksik',
             'İki görünüş çizilmiş',
             'Bir veya sıfır görünüş'),
            ('Ölçü\nbelirtme',
             '2+ ölçü (cm) doğru konumda yazılmış',
             '2 ölçü var, konumlandırma hatalı',
             '1 ölçü belirtilmiş',
             'Ölçü yok'),
            ('Çizim\nkalitesi',
             'Cetvel kullanılmış; görünüşler hizalı ve tanınabilir',
             'Görünüşler tanınabilir, kısmen hizalı',
             'Anlaşılır ama hizasız',
             'Nesne tanınmıyor'),
        ],
    },
    {
        'title': 'BÖLÜM 2 — 2B Paint Dosyası + Tasarım Kartı',
        'weight': '%25', 'max': 16,
        'rows': [
            ('Paint\ngörünüş',
             'Üst+ön görünüş şekil araçlarıyla çizilmiş, ölçüler yazılmış',
             'İki görünüş var, ölçü eksik',
             'Bir görünüş veya araçlar kısmen kullanılmış',
             'Çizim yok veya tanınamıyor'),
            ('Renk ve\ndüzen',
             'Farklı parçalar farklı renkle; görsel düzen özenli',
             'Renk kullanılmış ama tutarsız',
             'Tek renk, minimal düzen',
             'Renk veya düzen yok'),
            ('Tasarım\nKartı',
             '4 alan eksiksiz: nesne adı, üst/ön görünüş, gerekçe',
             '3 alan dolu',
             '2 alan dolu',
             '1 alan veya kart yok'),
            ('Dosya\nyönetimi',
             'Ad_Soyad_2B.png olarak doğru kaydedilmiş',
             'Kaydedilmiş, adlandırma kuralına uymuyor',
             'Kaydedilmiş, format farklı',
             'Dosya bulunamıyor'),
        ],
    },
    {
        'title': 'BÖLÜM 3 — ÇK3: Tinkercad Planlama Formu',
        'weight': '%10', 'max': 12,
        'rows': [
            ('Şekil\nanalizi',
             'Tüm parçalar temel şekillerle etiketlenmiş ve çizilmiş',
             "Parçaların büyük çoğunluğu tanımlanmış",
             'Yarısı tanımlanmış',
             'Minimal analiz'),
            ('Ölçü\nkaydı',
             'Tüm parçalar için en×boy×yük. (cm) yazılmış',
             "Çoğunun ölçüsü yazılmış",
             'Bazılarının ölçüsü yazılmış',
             'Ölçü yok veya tek parça'),
            ('Plan–Model\ntutarlılığı',
             'Tinkercad modeli planı büyük ölçüde yansıtıyor',
             'Modelde küçük sapmalar var',
             "Model plandan farklı, neden açıklanmamış",
             'Bağlantı kurulamıyor'),
        ],
    },
    {
        'title': 'BÖLÜM 4 — Tinkercad Modeli',
        'weight': '%30', 'max': 16,
        'rows': [
            ('Modelin\ntanınabilirliği',
             'Nesne açıkça tanınabilir; oran ve form uygun',
             'Tanınabilir, oran kısmen tutarsız',
             'Nesneye az benziyor',
             'Nesne tanınamıyor'),
            ('Şekil\nkullanımı',
             'Birden fazla şekil; birleştirme/delik operasyonu kullanılmış',
             'Birden fazla şekil, birleştirme basit',
             'Tek şekil veya çok basit',
             'Model yok veya başlangıç'),
            ('Ölçü\nduyarlılığı',
             'Ölçüler ÇK3 planıyla uyumlu (±20%)',
             'Kabul edilebilir sapma',
             'Belirsiz veya çok farklı',
             'Ölçü dikkate alınmamış'),
            ('Dosya ve\nekran görüntüsü',
             'Ad_Soyad_3B; 2 ekran görüntüsü doğru isimle kaydedilmiş',
             'İsimlendirilmiş veya ekran görüntüsü (biri eksik)',
             'Dosya var, adlandırma veya görüntü eksik',
             'Dosya bulunamıyor'),
        ],
    },
    {
        'title': 'BÖLÜM 5 — Tasarım Tanıtım Kartı + Sunum',
        'weight': '%15', 'max': 16,
        'rows': [
            ('Tanıtım\nKartı alanları',
             '5 alan eksiksiz: bilgi, eskiz, 3B görüntü, ölçüler, gerekçe',
             '4 alan dolu',
             '3 alan dolu',
             '2 veya daha az alan'),
            ('Görsel\nbelgeleme',
             'Eskiz→2B→3B süreç adımları görsellenmiş',
             "Sürecin büyük bölümü görsellenmiş",
             'Yalnızca son ürün görseli',
             'Görsel belgeleme yok'),
            ('Sunum\nanlaşılırlığı',
             'Tasarım kararları net; soru sormadan anlaşılıyor',
             'Açıklamalar anlaşılır, kısmen eksik',
             'Sunum kısa/belirsiz, yönlendirme gerekiyor',
             'Sunum yapılmamış'),
            ('Kullanıcı odaklı\ndüşünme',
             '"Kimin için / neden" açık ve gerekçeli',
             'Kullanıcı belirtilmiş, gerekçe kısa',
             'Yüzeysel açıklama',
             'Kullanıcı odaklı düşünme yok'),
        ],
    },
]


def build_rubrik_section(sec):
    """Bir bölüm için KeepTogether ile sarılmış tablo döndür."""
    num_rows = len(sec['rows'])
    # header + col labels + data rows + subtotal = num_rows+3
    span_end = num_rows + 1   # son satır = subtotal

    data = [
        # 0: bölüm başlığı
        [Paragraph(
            f"{sec['title']}  —  Ağırlık: {sec['weight']}  ·  "
            f"Maks: {sec['max']} puan",
            s_sec_hdr
        ), '', '', '', '', ''],
        # 1: sütun başlıkları
        [Paragraph('Kriter', s_col_hdr),
         Paragraph('Çok İyi — 4', s_col_hdr),
         Paragraph('İyi — 3', s_col_hdr),
         Paragraph('Geliştirilmeli — 2', s_col_hdr),
         Paragraph('Yetersiz — 1', s_col_hdr),
         Paragraph('Puan', s_col_hdr)],
    ]

    for i, (kriter, c4, c3, c2, c1) in enumerate(sec['rows']):
        data.append([
            Paragraph(kriter, s_kriter),
            Paragraph(c4, s_desc),
            Paragraph(c3, s_desc),
            Paragraph(c2, s_desc),
            Paragraph(c1, s_yetersiz),
            '',
        ])

    # Subtotal row
    data.append([
        '', '', '', '',
        Paragraph('Bölüm Toplamı:', s_total_lbl),
        Paragraph(f'___ / {sec["max"]}', s_total_val),
    ])

    style_cmds = [
        # Section header span + bg
        ('SPAN', (0, 0), (5, 0)),
        ('BACKGROUND', (0, 0), (5, 0), COLOR_PRIMARY),
        ('TOPPADDING', (0, 0), (5, 0), 5),
        ('BOTTOMPADDING', (0, 0), (5, 0), 5),
        ('LEFTPADDING', (0, 0), (5, 0), 6),
        # Col header row
        ('BACKGROUND', (0, 1), (5, 1), COLOR_LIGHT),
        ('TOPPADDING', (0, 1), (5, 1), 3),
        ('BOTTOMPADDING', (0, 1), (5, 1), 3),
        # Data rows padding
        ('TOPPADDING', (0, 2), (5, -2), 2.5),
        ('BOTTOMPADDING', (0, 2), (5, -2), 2.5),
        ('LEFTPADDING', (0, 0), (5, -1), 4),
        ('RIGHTPADDING', (0, 0), (5, -1), 4),
        # Alternating row bg
        ('ROWBACKGROUNDS', (0, 2), (5, num_rows + 1),
         [white, COLOR_VERY_LIGHT_GREY]),
        # Grid for data + col header
        ('GRID', (0, 1), (5, num_rows + 1), 0.4, COLOR_LIGHT_GREY),
        # Puan column: light bg
        ('BACKGROUND', (5, 2), (5, num_rows + 1), COLOR_SCORE_BG),
        # Valign
        ('VALIGN', (0, 0), (5, -1), 'MIDDLE'),
        # Subtotal row
        ('BACKGROUND', (0, -1), (5, -1), COLOR_VERY_LIGHT_GREY),
        ('TOPPADDING', (0, -1), (5, -1), 4),
        ('BOTTOMPADDING', (0, -1), (5, -1), 4),
        # Bold line below col headers
        ('LINEBELOW', (0, 1), (5, 1), 1.0, COLOR_SECONDARY),
    ]

    tbl = Table(data, colWidths=RUB_CW,
                style=TableStyle(style_cmds),
                repeatRows=2,
                hAlign='LEFT')

    return KeepTogether([tbl, Spacer(1, 8)])


def produce_rubrik():
    path = TEMP_RUBRIK

    def _hf(c, doc):
        hf_canvas(c, 'Ürün Değerlendirme Rubriği',
                  f'Sayfa {doc.page}')

    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        topMargin=1.6 * cm,
        bottomMargin=1.4 * cm,
        leftMargin=ML, rightMargin=MR,
        title='Urun Degerlendirme Rubrik',
    )

    elems = []

    # ── Başlık + öğrenci bilgisi ──
    elems.append(Spacer(1, 0.2 * cm))
    elems.append(Paragraph(
        'Ürün Değerlendirme Rubriği — 4. Ünite: Bilgisayar Destekli Tasarım',
        ParagraphStyle('rub_title', fontName='TR-Bold', fontSize=13,
                       textColor=COLOR_PRIMARY, leading=16)
    ))
    elems.append(Spacer(1, 0.15 * cm))

    # Öğrenci bilgisi satırı (tablo)
    info_data = [[
        Paragraph('Ad Soyad:', s_bold8),
        Paragraph('_' * 35, s_body8),
        Paragraph('Sınıf / No:', s_bold8),
        Paragraph('_' * 12, s_body8),
    ]]
    info_tbl = Table(info_data,
                     colWidths=[65, 260, 70, 90],
                     style=TableStyle([
                         ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
                         ('TOPPADDING', (0, 0), (-1, -1), 0),
                         ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                         ('LEFTPADDING', (0, 0), (-1, -1), 0),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                         ('LINEBELOW', (1, 0), (1, 0), 0.5, COLOR_WRITING_LINE),
                         ('LINEBELOW', (3, 0), (3, 0), 0.5, COLOR_WRITING_LINE),
                     ]))
    elems.append(info_tbl)
    elems.append(Spacer(1, 0.1 * cm))

    # Ölçek notu
    scale_data = [[
        Paragraph(
            '<b>Puanlama Ölçeği:</b>  '
            '4 — Çok İyi (kriter eksiksiz karşılandı)  ·  '
            '3 — İyi (kriter karşılandı)  ·  '
            '2 — Geliştirilmeli (kısmen)  ·  '
            '1 — Yetersiz (karşılanmadı)',
            ParagraphStyle('scale', fontName='TR-Regular', fontSize=7.5,
                           textColor=COLOR_TEXT, leading=10)
        )
    ]]
    scale_tbl = Table(scale_data, colWidths=[UW],
                      style=TableStyle([
                          ('BACKGROUND', (0, 0), (0, 0), COLOR_VERY_LIGHT),
                          ('TOPPADDING', (0, 0), (0, 0), 4),
                          ('BOTTOMPADDING', (0, 0), (0, 0), 4),
                          ('LEFTPADDING', (0, 0), (0, 0), 6),
                          ('BOX', (0, 0), (0, 0), 0.5, COLOR_LIGHT),
                      ]))
    elems.append(scale_tbl)
    elems.append(Spacer(1, 0.2 * cm))

    # ── Rubrik bölümleri ──
    for sec in RUBRIK_SECTIONS:
        elems.append(build_rubrik_section(sec))

    # ── Puan hesaplama tablosu ──
    elems.append(Spacer(1, 0.1 * cm))
    ph_header_style = ParagraphStyle('ph', fontName='TR-Bold', fontSize=8.5,
        textColor=white, leading=11)
    ph_lbl = ParagraphStyle('phlbl', fontName='TR-Regular', fontSize=8,
        textColor=COLOR_TEXT, leading=10)
    ph_bold = ParagraphStyle('phbld', fontName='TR-Bold', fontSize=8,
        textColor=COLOR_PRIMARY, alignment=TA_CENTER, leading=10)
    ph_cw = [UW * p for p in [0.36, 0.10, 0.22, 0.22, 0.10]]

    ph_data = [
        [Paragraph('PUAN HESAPLAMA', ph_header_style),
         '', '', '', ''],
        [Paragraph('Bölüm', s_col_hdr),
         Paragraph('Ağırlık', s_col_hdr),
         Paragraph('Ham Puan / Maks', s_col_hdr),
         Paragraph('Ağırlıklı Puan', s_col_hdr),
         Paragraph('Not', s_col_hdr)],
        [Paragraph('ÇK1 — Görünüş Çıkarma', ph_lbl),
         Paragraph('%10', ph_bold), Paragraph('___ / 12', ph_bold),
         Paragraph('___', ph_bold), ''],
        [Paragraph('2B Paint Dosyası + Tasarım Kartı', ph_lbl),
         Paragraph('%25', ph_bold), Paragraph('___ / 16', ph_bold),
         Paragraph('___', ph_bold), ''],
        [Paragraph('ÇK3 — Tinkercad Planlama', ph_lbl),
         Paragraph('%10', ph_bold), Paragraph('___ / 12', ph_bold),
         Paragraph('___', ph_bold), ''],
        [Paragraph('Tinkercad Modeli', ph_lbl),
         Paragraph('%30', ph_bold), Paragraph('___ / 16', ph_bold),
         Paragraph('___', ph_bold), ''],
        [Paragraph('Tasarım Tanıtım Kartı + Sunum', ph_lbl),
         Paragraph('%15', ph_bold), Paragraph('___ / 16', ph_bold),
         Paragraph('___', ph_bold), ''],
        [Paragraph('Süreç Gözlem Formu', ph_lbl),
         Paragraph('%10', ph_bold), Paragraph('Ayrı formdan', ph_bold),
         Paragraph('___', ph_bold), ''],
        [Paragraph('TOPLAM', ParagraphStyle('tot', fontName='TR-Bold',
            fontSize=9, textColor=COLOR_PRIMARY, alignment=TA_LEFT)),
         Paragraph('%100', ph_bold), '',
         Paragraph('___', ParagraphStyle('totv', fontName='TR-Bold',
            fontSize=11, textColor=COLOR_PRIMARY, alignment=TA_CENTER)),
         ''],
    ]

    ph_style = TableStyle([
        ('SPAN', (0, 0), (4, 0)),
        ('BACKGROUND', (0, 0), (4, 0), COLOR_PRIMARY),
        ('TOPPADDING', (0, 0), (4, 0), 5),
        ('BOTTOMPADDING', (0, 0), (4, 0), 5),
        ('LEFTPADDING', (0, 0), (4, 0), 6),
        ('BACKGROUND', (0, 1), (4, 1), COLOR_LIGHT),
        ('LINEBELOW', (0, 1), (4, 1), 1.0, COLOR_SECONDARY),
        ('ROWBACKGROUNDS', (0, 2), (4, 7), [white, COLOR_VERY_LIGHT_GREY]),
        ('BACKGROUND', (0, 8), (4, 8), COLOR_LIGHT),
        ('GRID', (0, 1), (4, 8), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0, 0), (4, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 2), (4, -1), 3),
        ('BOTTOMPADDING', (0, 2), (4, -1), 3),
        ('LEFTPADDING', (0, 0), (4, -1), 4),
        ('RIGHTPADDING', (0, 0), (4, -1), 4),
        ('ALIGN', (1, 2), (3, -1), 'CENTER'),
    ])

    ph_tbl = Table(ph_data, colWidths=ph_cw,
                   style=ph_style, hAlign='LEFT')
    elems.append(KeepTogether([ph_tbl]))
    elems.append(Spacer(1, 0.1 * cm))

    # Öğretmen notu
    note_data = [[
        Paragraph('<b>Öğretmen Notu:</b>', s_bold8),
        Paragraph('_' * 70, s_body8),
    ]]
    note_tbl = Table(note_data, colWidths=[85, UW - 85],
                     style=TableStyle([
                         ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
                         ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                         ('LEFTPADDING', (0, 0), (-1, -1), 0),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                         ('LINEBELOW', (1, 0), (1, 0), 0.5, COLOR_WRITING_LINE),
                     ]))
    elems.append(note_tbl)

    doc.build(elems, onFirstPage=_hf, onLaterPages=_hf)
    print('Rubrik olusturuldu:', path)


# ══════════════════════════════════════════════════════════════════════════════
# 2. SÜREÇ GÖZLEM FORMU (Canvas)
# ══════════════════════════════════════════════════════════════════════════════

def produce_gozlem_formu(c):

    hf_canvas(c, 'Süreç Gözlem Formu')

    y = CONTENT_TOP - 18
    c.setFont('TR-Bold', 12)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y,
                 'Süreç Gözlem Formu — 4. Ünite: Bilgisayar Destekli Tasarım')

    # Sınıf / Öğretmen / Dönem
    y -= 20
    def inf(label, x, lw):
        c.setFont('TR-Bold', 8.5)
        c.setFillColor(COLOR_TEXT)
        c.drawString(x, y, label)
        lbl_w = c.stringWidth(label, 'TR-Bold', 8.5)
        c.setStrokeColor(COLOR_WRITING_LINE)
        c.setLineWidth(0.5)
        c.line(x + lbl_w + 2, y - 3, x + lbl_w + 2 + lw, y - 3)

    inf('Sınıf:', ML, 60)
    inf('Öğretmen:', ML + 115, 150)
    inf('Dönem:', ML + 330, 120)

    # Ölçek açıklaması
    y -= 14
    BH = 54
    c.setFillColor(COLOR_VERY_LIGHT)
    c.setStrokeColor(COLOR_LIGHT)
    c.setLineWidth(0.7)
    c.rect(ML, y - BH, UW, BH, fill=1)

    # İki sütun: Puanlama | Kriterler
    half = UW / 2 - 4
    # Sol: Puanlama ölçeği
    c.setFont('TR-Bold', 8)
    c.setFillColor(COLOR_SECONDARY)
    c.drawString(ML + 5, y - 10, 'Puanlama Ölçeği')
    pu_lines = [
        '3 — Yetkin: Bağımsız, sürekli olarak gösteriyor',
        '2 — Gelişiyor: Zaman zaman yönlendirme gerekiyor',
        '1 — Başlangıç: Sık yardım gerekiyor; nadiren gösteriyor',
    ]
    c.setFont('TR-Regular', 7.5)
    c.setFillColor(COLOR_TEXT)
    py = y - 22
    for ln in pu_lines:
        c.drawString(ML + 5, py, ln)
        py -= 10

    # Dikey ayırıcı
    c.setStrokeColor(COLOR_LIGHT_GREY)
    c.setLineWidth(0.4)
    c.line(ML + half + 4, y - 4, ML + half + 4, y - BH + 4)

    # Sağ: Kriter kısaltmaları
    c.setFont('TR-Bold', 8)
    c.setFillColor(COLOR_SECONDARY)
    c.drawString(ML + half + 12, y - 10, 'Gözlem Kriterleri')
    crit_lines = [
        'A — Araç Kullanımı: Paint/Tinkercad araçlarını etkili kullanıyor',
        'B — Plana Uyma: Çalışma kâğıtlarını dolduruyor, adımları izliyor',
        'C — Sorun Çözme: Sorunla karşılaşınca önce kendisi çözmeye çalışıyor',
        'D — Sorumluluk: İşleri zamanında bitiriyor, dosyaları doğru kaydediyor',
        'E — Katılım: Sınıf tartışmalarına ve sunuma katılıyor',
    ]
    c.setFont('TR-Regular', 7)
    c.setFillColor(COLOR_TEXT)
    cy = y - 20
    for ln in crit_lines:
        c.drawString(ML + half + 12, cy, ln)
        cy -= 9.2
    y -= BH + 6

    # Tablo
    COL_NO  = 18
    COL_AD  = 162
    COL_CR  = 42   # her kriter için
    COL_TOT = 42
    COL_NOT = UW - COL_NO - COL_AD - 5 * COL_CR - COL_TOT  # ~48.89

    # Sütun x pozisyonları
    xs = [ML]
    for w in [COL_NO, COL_AD, COL_CR, COL_CR, COL_CR, COL_CR, COL_CR, COL_TOT]:
        xs.append(xs[-1] + w)

    HDR_H   = 20
    N_ROWS  = 20
    FOOTER_H = 25
    avail_h  = y - CONTENT_BOT - FOOTER_H - HDR_H
    ROW_H    = avail_h / N_ROWS

    # Tablo başlık bandı
    c.setFillColor(COLOR_PRIMARY)
    c.setStrokeColor(COLOR_PRIMARY)
    c.rect(ML, y - HDR_H, UW, HDR_H, fill=1, stroke=0)

    headers = ['No', 'Ad Soyad', 'A', 'B', 'C', 'D', 'E',
               'Toplam\n(/15)', 'Not']
    col_centers = []
    for i in range(len(xs) - 1):
        col_centers.append(xs[i] + (xs[i + 1] - xs[i]) / 2)
    col_centers.append(xs[-1] + COL_NOT / 2)

    c.setFont('TR-Bold', 7.5)
    c.setFillColor(white)
    for i, hdr in enumerate(headers):
        if '\n' in hdr:
            lines = hdr.split('\n')
            c.setFont('TR-Bold', 7)
            c.drawCentredString(col_centers[i], y - 10, lines[0])
            c.setFont('TR-Regular', 6.5)
            c.drawCentredString(col_centers[i], y - 18, lines[1])
        else:
            c.setFont('TR-Bold', 7.5)
            c.drawCentredString(col_centers[i], y - HDR_H / 2 - 3, hdr)
    y -= HDR_H

    # Satırlar
    for row in range(N_ROWS):
        ry = y - row * ROW_H
        bg = white if row % 2 == 0 else COLOR_VERY_LIGHT_GREY
        c.setFillColor(bg)
        c.setStrokeColor(COLOR_LIGHT_GREY)
        c.setLineWidth(0.3)
        c.rect(ML, ry - ROW_H, UW, ROW_H, fill=1)

        # Numara
        c.setFont('TR-Bold', 8)
        c.setFillColor(COLOR_SECONDARY)
        c.drawCentredString(col_centers[0], ry - ROW_H / 2 - 3, str(row + 1))

        # Sütun dikey çizgileri
        c.setStrokeColor(COLOR_LIGHT_GREY)
        for xi in xs[1:]:
            c.line(xi, ry - ROW_H, xi, ry)
        # Not kolonu sağı
        c.line(xs[-1] + COL_NOT, ry - ROW_H, xs[-1] + COL_NOT, ry)

    # Dış çerçeve
    c.setStrokeColor(COLOR_LIGHT_GREY)
    c.setLineWidth(0.8)
    tbl_h = HDR_H + N_ROWS * ROW_H
    c.rect(ML, y - N_ROWS * ROW_H, UW, tbl_h, fill=0)

    # Özet satırı (alt)
    sy = CONTENT_BOT + FOOTER_H - 8
    c.setFont('TR-Bold', 8)
    c.setFillColor(COLOR_TEXT)
    parts = [
        ('Sınıf Ortalaması:', ML),
        ('En Yüksek:', ML + 175),
        ('En Düşük:', ML + 330),
    ]
    for lbl, px in parts:
        c.drawString(px, sy, lbl)
        lw = c.stringWidth(lbl, 'TR-Bold', 8)
        c.setStrokeColor(COLOR_WRITING_LINE)
        c.setLineWidth(0.5)
        c.line(px + lw + 3, sy - 3, px + lw + 3 + 80, sy - 3)

    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# 3. ÖĞRENCİ ÖZ DEĞERLENDİRME (Canvas)
# ══════════════════════════════════════════════════════════════════════════════

def produce_oz_degerlendirme(c):

    hf_canvas(c, 'Öğrenci Öz Değerlendirme')

    y = CONTENT_TOP - 18
    c.setFont('TR-Bold', 12)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y, 'Öğrenci Öz Değerlendirme Formu')

    y -= 20
    # Öğrenci bilgisi
    def inf2(label, x, lw):
        c.setFont('TR-Bold', 8.5)
        c.setFillColor(COLOR_TEXT)
        c.drawString(x, y, label)
        lw2 = c.stringWidth(label, 'TR-Bold', 8.5)
        c.setStrokeColor(COLOR_WRITING_LINE)
        c.setLineWidth(0.5)
        c.line(x + lw2 + 2, y - 3, x + lw2 + 2 + lw, y - 3)

    inf2('Ad Soyad:', ML, 180)
    inf2('Sınıf / No:', ML + 248, 75)
    inf2('Tarih:', ML + 370, 90)

    y -= 8
    c.setFont('TR-Italic', 8)
    c.setFillColor(COLOR_MUTED)
    c.drawString(ML, y,
                 'Bu form not için değildir. Dürüstçe yanıtla — yanlış cevap olmaz!')
    y -= 14

    # ── Bölüm 1: Likert ─────────────────────────────────────────────────────
    c.setFont('TR-Bold', 9.5)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y, 'Bölüm 1 — Kendimi Değerlendiriyorum')
    y -= 14

    c.setFont('TR-Regular', 8)
    c.setFillColor(COLOR_TEXT)
    c.drawString(ML, y,
                 'Her ifade için sana en uygun seçeneği işaretle  '
                 '(1 = Hiç katılmıyorum · 4 = Tamamen katılıyorum)')
    y -= 8

    # Likert tablo
    ITEM_TXT_W = 330
    CB_W = (UW - ITEM_TXT_W) / 4   # ~37.97 per checkbox col
    HDR_H_L = 16
    ITEM_H = 22

    likert_items = [
        'Paint ile nesnelerin görünüşlerini çizebiliyorum.',
        'Tinkercad\'de temel şekillerle 3B nesne oluşturabilirim.',
        'Kâğıtta plan yapmak bilgisayarda çalışmamı kolaylaştırdı.',
        'Tasarımımı başkalarına anlaşılır biçimde anlatabildim.',
        'Zorlandığımda yardım istemeden önce kendim çözmeye çalıştım.',
        'Bu ünitede zamanımı iyi kullandım ve işlerimi zamanında tamamladım.',
    ]
    n_items = len(likert_items)
    tbl_h = HDR_H_L + n_items * ITEM_H

    # Header bandı
    c.setFillColor(COLOR_PRIMARY)
    c.setStrokeColor(COLOR_PRIMARY)
    c.rect(ML, y - tbl_h, UW, HDR_H_L, fill=1, stroke=0)

    c.setFont('TR-Bold', 7.5)
    c.setFillColor(white)
    c.drawString(ML + 5, y - HDR_H_L + 5, 'İfade')
    for ci, lbl in enumerate(['1', '2', '3', '4']):
        cx = ML + ITEM_TXT_W + CB_W * ci + CB_W / 2
        c.drawCentredString(cx, y - HDR_H_L + 5, lbl)

    # İtem satırları
    for ri, item in enumerate(likert_items):
        iy = y - HDR_H_L - ri * ITEM_H
        bg = white if ri % 2 == 0 else COLOR_VERY_LIGHT_GREY
        c.setFillColor(bg)
        c.setStrokeColor(COLOR_LIGHT_GREY)
        c.setLineWidth(0.3)
        c.rect(ML, iy - ITEM_H, UW, ITEM_H, fill=1)
        # Item text
        c.setFont('TR-Regular', 8)
        c.setFillColor(COLOR_TEXT)
        c.drawString(ML + 5, iy - ITEM_H / 2 - 3, item)
        # Checkboxes
        for ci in range(4):
            cx = ML + ITEM_TXT_W + CB_W * ci + CB_W / 2 - 5
            cy2 = iy - ITEM_H / 2 - 5
            c.setFillColor(white)
            c.setStrokeColor(COLOR_LIGHT_GREY)
            c.setLineWidth(0.5)
            c.rect(cx, cy2, 10, 10, fill=1)
        # Col dividers
        for ci in range(1, 5):
            c.setStrokeColor(COLOR_LIGHT_GREY)
            c.line(ML + ITEM_TXT_W + CB_W * ci, iy - ITEM_H,
                   ML + ITEM_TXT_W + CB_W * ci, iy)
        c.line(ML + ITEM_TXT_W, iy - ITEM_H, ML + ITEM_TXT_W, iy)

    # Dış çerçeve
    c.setStrokeColor(COLOR_LIGHT_GREY)
    c.setLineWidth(0.8)
    c.rect(ML, y - tbl_h, UW, tbl_h, fill=0)

    y -= tbl_h + 14

    # ── Bölüm 2: Yansıtma soruları ──────────────────────────────────────────
    c.setFont('TR-Bold', 9.5)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y, 'Bölüm 2 — Yansıtma Soruları')
    y -= 12

    questions = [
        '1.  2B ve 3B tasarım araçlarından hangisi sana daha doğal geldi? Neden?',
        '2.  Tinkercad\'de en çok zorlandığın işlem hangisiydi? Nasıl aştın?',
        '3.  Tasarım Tanıtım Kartını hazırlarken neye dikkat ettin?',
        '4.  Bu ünitede en çok ne öğrendiğini düşünüyorsun? (1 cümle)',
        '5.  Bir sonraki ünitede (Mimari Tasarım) bu becerileri nerede kullanabilirsin?',
    ]
    Q_GAP = 8   # satır aralığı için çizgi
    Q_LINES = [2, 2, 2, 1, 2]   # her soru için kaç boş satır

    for qi, (q, n_lines) in enumerate(zip(questions, Q_LINES)):
        c.setFont('TR-Bold' if qi < 3 else 'TR-Regular', 8)
        c.setFillColor(COLOR_TEXT)
        c.drawString(ML, y, q)
        y -= 12
        for _ in range(n_lines):
            c.setStrokeColor(COLOR_WRITING_LINE)
            c.setLineWidth(0.4)
            c.line(ML, y, PAGE_W - MR, y)
            y -= 11
        y -= 4

    # ── Bölüm 3: Hızlı değerlendirme ────────────────────────────────────────
    y -= 4
    c.setFont('TR-Bold', 9.5)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(ML, y, 'Bölüm 3 — Hızlı Değerlendirme')
    y -= 12

    for lbl in [
        'Bu ünitede en iyi yaptığım şey:',
        'Bir dahaki sefere farklı yapmak istediğim şey:',
    ]:
        c.setFont('TR-Regular', 8)
        c.setFillColor(COLOR_TEXT)
        c.drawString(ML, y, lbl)
        y -= 11
        c.setStrokeColor(COLOR_WRITING_LINE)
        c.setLineWidth(0.4)
        c.line(ML, y, PAGE_W - MR, y)
        y -= 14

    c.showPage()


# ── Ana ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import pypdf

    produce_rubrik()

    c = pdf_canvas.Canvas(TEMP_CG, pagesize=A4)
    produce_gozlem_formu(c)
    produce_oz_degerlendirme(c)
    c.save()

    writer = pypdf.PdfWriter()
    for src in [TEMP_RUBRIK, TEMP_CG]:
        reader = pypdf.PdfReader(src)
        for page in reader.pages:
            writer.add_page(page)
    with open(PDF_PATH, 'wb') as f:
        writer.write(f)

    import os as _os
    for tmp in [TEMP_RUBRIK, TEMP_CG]:
        try:
            _os.remove(tmp)
        except Exception:
            pass

    print(f'PDF uretildi: {PDF_PATH}')
