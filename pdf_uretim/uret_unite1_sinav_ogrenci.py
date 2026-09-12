"""
Unite1 -- Unite Sonu Sinavi (Ogrenci Formu)
3 bolum: Coktan Secmeli (40p), Kisa Cevapli (30p), Performans Gorevi (30p) = 100 puan
Sayfa 1: MCQ + Kisa Cevapli; Sayfa 2: Performans Gorevi

Kullanim:
    python pdf_uretim/uret_unite1_sinav_ogrenci.py
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
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_OUTPUT = os.path.join(ROOT, 'units', 'unit1', 'U1_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 1. Ünite'
DOC_TITLE  = '1. Ünite Sonu Sınavı — Öğrenci Formu'
PAGE_W     = A4[0] - 4 * cm


# ── Stil sabitleri ───────────────────────────────────────────────

BOLUM_ST = ParagraphStyle(
    'U1_BolumBaslik', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=6,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)

SORU_ST = ParagraphStyle(
    'U1_SoruMetni', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)

OPT_ST = ParagraphStyle(
    'U1_SecenekMetni', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10.5, spaceAfter=0, leftIndent=8,
)

KISA_SORU_ST = ParagraphStyle(
    'U1_KisaSoru', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3,
)

HDR_ST = ParagraphStyle(
    'U1_TblHdr', fontName='TR-Bold', fontSize=8,
    textColor=white, leading=11,
)

CELL_ST = ParagraphStyle(
    'U1_TblCell', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11,
)


# ── MCQ soru verileri ────────────────────────────────────────────

SORULAR = [
    (
        "Aşağıdakilerden hangisi icat'a bir örnektir?",
        ["A) Newton'un yerçekimini fark etmesi",
         "B) Graham Bell'in telefonu ilk kez yapması",
         "C) Kolomb'un Amerika'ya ulaşması",
         "D) Arşimet'in kaldırma kuvvetini bulması"],
    ),
    (
        "Endüstri 4.0'ı en doğru tanımlayan ifade hangisidir?",
        ["A) Fabrikalarda elektrik kullanılmaya başlanması",
         "B) Sanayi üretiminde buhar gücü dönemi",
         "C) Akıllı fabrikalar, nesnelerin interneti ve yapay zekânın üretime girmesi",
         "D) Sadece üretimde robot kullanılması"],
    ),
    (
        '"Bir yemek tarifinin adım adım uygulanması" aşağıdaki kavramlardan hangisine en yakındır?',
        ["A) Teknoloji", "B) Teknik", "C) Bilim", "D) Tasarım"],
    ),
    (
        "Aşağıdakilerden hangisi grafik tasarım örneği değildir?",
        ["A) Bir kitabın kapağı", "B) Bir şehir parkı",
         "C) Bir YouTube kanalının logosu", "D) Bir afiş"],
    ),
    (
        'STEAM kısaltmasındaki "A" harfi neyi ifade eder?',
        ["A) Architecture (Mimari)", "B) Automation (Otomasyon)",
         "C) Arts (Sanat)", "D) Algorithm (Algoritma)"],
    ),
    (
        "Aşağıdakilerden hangisi Endüstri 5.0'ın en önemli farklarından biridir?",
        ["A) Fabrikalardan insanların tamamen çıkarılması",
         "B) Üretimin tamamen yapay zekâya devredilmesi",
         "C) İnsan-makine iş birliği ve sürdürülebilirlik odağı",
         "D) Sadece elektrik kullanımının azaltılması"],
    ),
    (
        "Bir teknoloji haberinin güvenilirliğini değerlendirmek için öncelikle sorulacak soru hangisidir?",
        ["A) Haberi kaç kişi paylaşmış?",
         "B) Kaynak belli mi, yazar kim?",
         "C) Haber ne kadar uzun?",
         "D) Başlığı dikkat çekici mi?"],
    ),
    (
        'Bir ürünün "iyi tasarlanmış" olduğunu söyleyebilmek için aşağıdakilerden en az kaçına bakmak gerekir?',
        ["A) Sadece estetiğine",
         "B) Sadece fiyatına",
         "C) Birden fazla ölçüte (işlevsellik, ergonomi, estetik, sürdürülebilirlik vb.)",
         "D) Sadece kim yaptığına"],
    ),
]


# ── MCQ bölümü (2 sütun) ─────────────────────────────────────────

def _mcq_cell(no, text, opts):
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
        ('VALIGN',         (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',     (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING',  (0, 0), (-1, -1), 3),
        ('LEFTPADDING',    (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',   (0, 0), (-1, -1), 2),
        ('LINEAFTER',      (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, COLOR_VERY_LIGHT]),
        ('BOX',            (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
    ]))
    return t


# ── Kısa cevaplı bölüm ───────────────────────────────────────────

def kisa_cevap_bolum():
    items = []

    # Soru 9
    items.append(KeepTogether([
        Paragraph(
            '9. "İcat" ve "keşif" arasındaki farkı birer örnek vererek açıklayın. '
            '<i>(10 puan)</i>',
            KISA_SORU_ST,
        ),
        WritingLines(num_lines=3, line_spacing=15),
        Spacer(1, 4),
    ]))

    # Soru 10
    items.append(KeepTogether([
        Paragraph(
            '10. Teknoloji ile tasarım arasındaki ilişkiyi bir günlük yaşam örneğiyle '
            '(telefon, araba, mobilya vb.) açıklayın. <i>(10 puan)</i>',
            KISA_SORU_ST,
        ),
        WritingLines(num_lines=3, line_spacing=15),
        Spacer(1, 4),
    ]))

    # Soru 11 — YZ uygulamaları tablosu
    items.append(Paragraph(
        '11. Günlük hayatınızda yapay zekâyı kullanan 3 uygulama/araç yazın ve '
        'her biri için kısa bir açıklama yapın. <i>(10 puan)</i>',
        KISA_SORU_ST,
    ))
    col_no   = 0.6 * cm
    col_urun = (PAGE_W - col_no) * 0.38
    col_acik = (PAGE_W - col_no) * 0.62
    tbl_data = [
        [Paragraph('No', HDR_ST),
         Paragraph('Uygulama / Araç', HDR_ST),
         Paragraph('Ne İş Yapıyor?', HDR_ST)],
        [Paragraph('1', CELL_ST), Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
        [Paragraph('2', CELL_ST), Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
        [Paragraph('3', CELL_ST), Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
    ]
    tbl = Table(tbl_data, colWidths=[col_no, col_urun, col_acik], rowHeights=[None, 1.1*cm, 1.1*cm, 1.1*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN',         (0, 0), (0, -1),  'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    items.append(tbl)

    return items


# ── Performans görevi bölümü (sayfa 2) ───────────────────────────

def performans_bolum():
    items = []

    # Soru 12 — karşılaştırma tablosu
    items.append(Paragraph(
        '12. Aşağıdaki tabloyu doldurun: Akıllı saat ile geleneksel kol saatini '
        'karşılaştırın. Her kutucuğa en az bir bilgi yazın. '
        '<i>(8 hücre × 2 puan = 16 puan)</i>',
        KISA_SORU_ST,
    ))
    items.append(Spacer(1, 4))

    col_oz  = PAGE_W * 0.32
    col_ak  = PAGE_W * 0.34
    col_gen = PAGE_W * 0.34
    krs_data = [
        [Paragraph('Özellik', HDR_ST),
         Paragraph('Akıllı Saat', HDR_ST),
         Paragraph('Geleneksel Kol Saati', HDR_ST)],
        [Paragraph('Hangi tasarım türü?', CELL_ST),   Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
        [Paragraph('Hangi teknoloji kullanıyor?', CELL_ST), Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
        [Paragraph('Kullanıcıya faydası?', CELL_ST),  Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
        [Paragraph('Olumsuz yanı (varsa)?', CELL_ST), Paragraph('', CELL_ST), Paragraph('', CELL_ST)],
    ]
    krs_t = Table(
        krs_data,
        colWidths=[col_oz, col_ak, col_gen],
        rowHeights=[None, 1.5*cm, 1.5*cm, 1.5*cm, 1.5*cm],
    )
    krs_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN',         (0, 0), (-1, 0),  'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    items.append(krs_t)
    items.append(Spacer(1, 10))

    # Yorum sorusu
    items.append(KeepTogether([
        Paragraph(
            'Tablodaki bilgileri değerlendirerek: <b>Sizce hangisi daha iyi tasarlanmış? '
            'Gerekçenizi açıklayın.</b> <i>(14 puan)</i>',
            KISA_SORU_ST,
        ),
        WritingLines(num_lines=5, line_spacing=16),
        Spacer(1, 8),
    ]))

    # Puan özeti
    puan_st = ParagraphStyle(
        'U1_PuanOzet', fontName='TR-Bold', fontSize=8.5,
        textColor=COLOR_TEXT, leading=12,
        backColor=COLOR_LIGHT, borderPadding=5,
    )
    items.append(Paragraph(
        'Bölüm 1: ____ / 40 &nbsp;&nbsp;|&nbsp;&nbsp; '
        'Bölüm 2: ____ / 30 &nbsp;&nbsp;|&nbsp;&nbsp; '
        'Bölüm 3: ____ / 30 &nbsp;&nbsp;|&nbsp;&nbsp; '
        '<b>TOPLAM: ____ / 100</b>',
        puan_st,
    ))

    return items


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
        'U1_SinavBaslik', fontName='TR-Bold', fontSize=13,
        textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
    )
    yonerge_st = ParagraphStyle(
        'U1_SinavYonerge', fontName='TR-Regular', fontSize=8.5,
        textColor=COLOR_TEXT, leading=12, spaceAfter=4,
        backColor=COLOR_VERY_LIGHT, borderPadding=5,
    )
    elems.append(Paragraph('1. Ünite Sonu Sınavı — Teknoloji ve Tasarım Öğreniyorum', title_st))
    elems.append(Paragraph(
        'Bu sınav 3 bölümden oluşur: Çoktan Seçmeli (40p), Kısa Cevaplı (30p), '
        'Performans Görevi (30p). <b>Toplam: 100 puan.</b>  Süre: 40 dakika.',
        yonerge_st,
    ))
    elems.append(Spacer(1, 4))

    # BÖLÜM 1: Çoktan Seçmeli
    elems.append(Paragraph('BÖLÜM 1: ÇOKTAN SEÇMELİ  (8 soru × 5 puan = 40 puan)', BOLUM_ST))
    elems.append(Spacer(1, 3))
    elems.append(mcq_bolum())
    elems.append(Spacer(1, 5))

    # BÖLÜM 2: Kısa Cevaplı
    elems.append(Paragraph('BÖLÜM 2: KISA CEVAPLI  (3 soru × 10 puan = 30 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))
    for el in kisa_cevap_bolum():
        elems.append(el)

    # Sayfa 2: Performans Görevi
    elems.append(PageBreak())
    elems.append(Paragraph('BÖLÜM 3: PERFORMANS GÖREVİ  (30 puan)', BOLUM_ST))
    elems.append(Spacer(1, 5))
    for el in performans_bolum():
        elems.append(el)

    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
