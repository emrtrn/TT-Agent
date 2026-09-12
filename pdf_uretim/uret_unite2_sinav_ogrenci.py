"""
Unite2 — Ünite Sonu Sınavı (Öğrenci Formu)
8 soru × 1 puan (Bölüm 1) + 12 puan (Bölüm 2) = 20 puan
2 sütunlu MCQ layout; tek sayfaya sığdırılmış.

Kullanım:
    python pdf_uretim/uret_unite2_sinav_ogrenci.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, get_styles, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_TEXT,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_OUTPUT = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Sinav_Ogrenci.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite'
DOC_TITLE  = '2. Ünite Sonu Sınavı — Öğrenci Formu'
PAGE_W     = A4[0] - 4 * cm  # ~17 cm kullanılabilir genişlik


# ── Stil sabitleri ───────────────────────────────────────────────

BOLUM_ST = ParagraphStyle(
    'BolumBaslik2', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=6,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)

SORU_ST = ParagraphStyle(
    'SoruMetni2', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)

OPT_ST = ParagraphStyle(
    'SecenekMetni2', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10.5, spaceAfter=0, leftIndent=8,
)

KISA_SORU_ST = ParagraphStyle(
    'KisaSoru2', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3,
)

BLANK_ST = ParagraphStyle(
    'BlankSatir2', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11, leftIndent=4,
)

HDR_ST = ParagraphStyle(
    'TblHdr2', fontName='TR-Bold', fontSize=8,
    textColor=white, leading=11,
)


# ── MCQ soru verileri ────────────────────────────────────────────

SORULAR = [
    (
        'Tasarımda "derinlik/alan" hissi veren, örtüşme ve konumlandırmayla ilgili eleman hangisidir?',
        ['A) Doku', 'B) Çizgi', 'C) Mekân (Uzam)', 'D) Valör'],
    ),
    (
        'Siyah arka plan üzerine sarı yazı kullanımı hangi tasarım ilkesine örnektir?',
        ['A) Denge', 'B) Birlik', 'C) Ritim', 'D) Zıtlık'],
    ),
    (
        '"Yeniden yorumlama"yı en doğru tanımlayan hangisidir?',
        ['A) Eseri birebir kopyalamak',
         'B) Bağlamı koruyarak kendi ifadesiyle aktarmak',
         'C) Eserden bütünüyle farklı bir şey üretmek',
         'D) Eserin yalnızca renklerini değiştirmek'],
    ),
    (
        'Anadolu halılarındaki tekrar eden motifler hangi tasarım ilkesini yansıtır?',
        ['A) Vurgu', 'B) Oran-Orantı', 'C) Ritim', 'D) Hareket'],
    ),
    (
        'Analoji yaparken hangi adım önce gelir?',
        ['A) İki unsuru görsel olarak çizmek',
         'B) Konuyu ya da kavramı belirlemek',
         'C) Soyut renk ve doku seçmek',
         'D) Slogan yazmak'],
    ),
    (
        '"Valör" bir nesneye uygulandığında neyi ifade eder?',
        ['A) Rengin sıcak ya da soğuk olması',
         'B) Rengin açık-koyu değeri (ışık-gölge)',
         'C) Nesnenin üç boyutlu dış biçimi',
         'D) Birden fazla rengin kullanılması'],
    ),
    (
        'Tasarım sürecinde taslak çiziminin temel amacı nedir?',
        ['A) Ürünü bitmiş hâliyle göstermek',
         'B) Maliyeti hesaplamak',
         'C) Fikri görselleştirmek ve en iyisini seçmek',
         'D) Akrana sunmak için hazırlamak'],
    ),
    (
        'Binanın sağ-sol tarafı tam yansıma olarak tasarlanması hangi denge türüdür?',
        ['A) Asimetrik denge', 'B) Simetrik denge',
         'C) Dinamik denge', 'D) Radyal denge'],
    ),
]


# ── MCQ bölümü (2 sütun) ─────────────────────────────────────────

def _mcq_cell(no, text, opts):
    """Tek bir MCQ sorusunu iç tablo olarak döndür."""
    col_w = (PAGE_W - 0.4 * cm) / 2 - 0.2 * cm
    items = [Paragraph(f'{no}. {text}', SORU_ST)]
    for opt in opts:
        items.append(Paragraph(f'&nbsp;&nbsp;{opt}', OPT_ST))
    inner = Table([[p] for p in items], colWidths=[col_w])
    inner.setStyle(TableStyle([
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    return inner


def mcq_bolum():
    col_w = (PAGE_W - 0.4 * cm) / 2
    rows = [
        [_mcq_cell(i + 1, SORULAR[i][0], SORULAR[i][1]),
         _mcq_cell(i + 5, SORULAR[i + 4][0], SORULAR[i + 4][1])]
        for i in range(4)
    ]
    t = Table(rows, colWidths=[col_w, col_w], spaceBefore=2, spaceAfter=2)
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
        ('LINEAFTER',     (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, COLOR_VERY_LIGHT]),
        ('BOX',           (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
    ]))
    return t


# ── Kısa cevaplı bölüm ───────────────────────────────────────────

def kisa_cevap_bolum():
    items = []

    # Soru 9 — 5 madde × 2 puan = 10 puan
    items.append(Paragraph(
        '9. Akıllı tahtada verilen görselde yer aldığını düşündüğünüz <b>en az 3 tasarım '
        'elemanını</b> ve <b>2 tasarım ilkesini</b> yazınız. Her biri için bu eserde neden '
        'kullanıldığını kısaca açıklayınız. <i>(5 madde × 2 puan = 10 puan)</i>',
        KISA_SORU_ST,
    ))

    col_w2 = (PAGE_W - 0.2 * cm) / 2
    tbl_data = [
        [Paragraph('Tasarım Elemanları (her biri 2 puan)', HDR_ST),
         Paragraph('Tasarım İlkeleri (her biri 2 puan)', HDR_ST)],
        [Paragraph('1. _________________________________', BLANK_ST),
         Paragraph('1. _________________________________', BLANK_ST)],
        [Paragraph('2. _________________________________', BLANK_ST),
         Paragraph('2. _________________________________', BLANK_ST)],
        [Paragraph('3. _________________________________', BLANK_ST),
         Paragraph('', BLANK_ST)],
    ]
    tbl = Table(tbl_data, colWidths=[col_w2, col_w2])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ]))
    items.append(tbl)
    items.append(Spacer(1, 5))

    # Soru 10 — 2 puan
    items.append(KeepTogether([
        Paragraph(
            '10. "Yorumlamak" ile "kopyalamak" arasındaki farkı <b>bir tasarım örneğiyle</b> '
            'açıklayınız. <i>(2 puan)</i>',
            KISA_SORU_ST,
        ),
        WritingLines(num_lines=2, line_spacing=16),
    ]))

    return items


# ── Puan özeti satırı ────────────────────────────────────────────

def puan_satiri():
    st = ParagraphStyle(
        'PuanOzet2', fontName='TR-Bold', fontSize=8.5,
        textColor=COLOR_TEXT, leading=12,
        backColor=COLOR_LIGHT, borderPadding=4,
    )
    return Paragraph(
        'Bölüm 1: ____ / 8&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;'
        'Bölüm 2: ____ / 12&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;'
        '<b>TOPLAM: ____ / 20</b>',
        st,
    )


# ── Ana üretim fonksiyonu ────────────────────────────────────────

def build(output_path=None):
    out = output_path or _DEFAULT_OUTPUT
    doc = create_doc(out, title=DOC_TITLE, unite_info=UNITE_INFO)
    elems = []

    # Öğrenci bilgi satırı
    elems.append(make_student_info_header())
    elems.append(Spacer(1, 3))
    elems.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elems.append(Spacer(1, 4))

    # Sınav başlığı
    title_st = ParagraphStyle(
        'SinavBaslik2', fontName='TR-Bold', fontSize=13,
        textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
    )
    yonerge_st = ParagraphStyle(
        'SinavYonerge2', fontName='TR-Regular', fontSize=8.5,
        textColor=COLOR_TEXT, leading=12, spaceAfter=4,
        backColor=COLOR_VERY_LIGHT, borderPadding=5,
    )
    elems.append(Paragraph('2. Ünite Sonu Sınavı — Temel Tasarım', title_st))
    elems.append(Paragraph(
        'Bu sınav 2 bölümden oluşur: Çoktan Seçmeli (8p), Kısa Cevaplı (12p). '
        '<b>Toplam: 20 puan.</b> Kurşun kalem kullan.',
        yonerge_st,
    ))
    elems.append(Spacer(1, 4))

    # BÖLÜM 1: Çoktan Seçmeli
    elems.append(Paragraph('BÖLÜM 1: ÇOKTAN SEÇMELİ  (8 soru × 1 puan = 8 puan)', BOLUM_ST))
    elems.append(Spacer(1, 3))
    elems.append(mcq_bolum())
    elems.append(Spacer(1, 5))

    # BÖLÜM 2: Kısa Cevaplı
    elems.append(Paragraph('BÖLÜM 2: KISA CEVAPLI  (12 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))
    for el in kisa_cevap_bolum():
        elems.append(el)
    elems.append(Spacer(1, 5))

    # Puan özeti
    elems.append(puan_satiri())

    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
