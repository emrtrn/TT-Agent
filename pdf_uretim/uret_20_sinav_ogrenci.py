"""
20 — Ünite Sonu Sınavı (Öğrenci Formu)
2 sayfaya sığdırılmış, başlık satırı tek satır.
MCQ bölümü 2 sütunlu layout ile sayfa 1'de bitirilir.

Kullanım:
    python pdf_uretim/uret_20_sinav_ogrenci.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, get_styles, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED, COLOR_WRITING_LINE,
    A4, cm,
)
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import white

OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'units', 'unit1', '20_Unite_Sonu_Sinavi_Ogrenci.pdf'
)

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 1. Ünite'
DOC_TITLE  = 'Ünite Sonu Sınavı — Öğrenci Formu'

# Kullanılabilir genişlik (A4 - 4 cm marjin)
PAGE_W = A4[0] - 4 * cm


def s(name, **kwargs):
    """get_styles() için kısayol, ek overrideler ile."""
    base = get_styles()[name]
    if not kwargs:
        return base
    import copy
    p = copy.copy(base)
    for k, v in kwargs.items():
        setattr(p, k, v)
    return p


def sınav_basligi():
    """Sınav bilgi satırı: Süre + Puan + Yönerge tek kutuda."""
    style = ParagraphStyle(
        'SinavYonerge', fontName='TR-Regular', fontSize=8.5,
        textColor=COLOR_TEXT, leading=12,
        backColor=COLOR_VERY_LIGHT, borderPadding=6,
        leftIndent=6, rightIndent=6, spaceAfter=4,
    )
    return Paragraph(
        'Bu sınav 2 bölümden oluşur: Çoktan Seçmeli (16p), Kısa Cevaplı (4p). '
        '<b>Toplam: 20 puan.</b>',
        style
    )


def bolum_baslik(metin):
    """Bölüm başlığı (turuncu, kompakt)."""
    st = ParagraphStyle(
        'BolumBaslik', fontName='TR-Bold', fontSize=10,
        textColor=white, leading=14, spaceAfter=4, spaceBefore=6,
        backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
        borderPadding=(3, 6, 3, 6),
    )
    return Paragraph(metin, st)


def soru_metni(fs=8.5):
    return ParagraphStyle(
        'Soru', fontName='TR-Bold', fontSize=fs,
        textColor=COLOR_TEXT, leading=12, spaceAfter=2,
    )


def secenek_stili(fs=8.5):
    return ParagraphStyle(
        'Secenek', fontName='TR-Regular', fontSize=fs,
        textColor=COLOR_TEXT, leading=11, spaceAfter=1, leftIndent=8,
    )


def mcq_cell(soru_no, soru_text, secenekler):
    """Tek bir MCQ sorusunu ReportLab paragrafları listesi olarak döndür."""
    sm = soru_metni()
    ss = secenek_stili()
    items = [Paragraph(f'{soru_no}. {soru_text}', sm)]
    for sey in secenekler:
        items.append(Paragraph(f'&nbsp;&nbsp;{sey}', ss))
    return items


SORULAR = [
    (
        "Aşağıdakilerden hangisi icad'a bir örnektir?",
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
        "\"Bir yemek tarifinin adım adım uygulanması\" hangi kavrama en yakındır?",
        ["A) Teknoloji", "B) Teknik", "C) Bilim", "D) Tasarım"],
    ),
    (
        "Aşağıdakilerden hangisi grafik tasarım örneği değildir?",
        ["A) Bir kitabın kapağı", "B) Bir şehir parkı",
         "C) Bir YouTube kanalının logosu", "D) Bir afiş"],
    ),
    (
        "STEAM kısaltmasındaki \"A\" harfi neyi ifade eder?",
        ["A) Architecture (Mimari)", "B) Automation (Otomasyon)",
         "C) Arts (Sanat)", "D) Algorithm (Algoritma)"],
    ),
    (
        "Endüstri 5.0'ın en önemli farklarından biri nedir?",
        ["A) Fabrikalardan insanların tamamen çıkarılması",
         "B) Üretimin tamamen yapay zekâya devredilmesi",
         "C) İnsan-makine iş birliği ve sürdürülebilirlik odağı",
         "D) Sadece elektrik kullanımının azaltılması"],
    ),
    (
        "Bir teknoloji haberinin güvenilirliğini değerlendirirken ilk sorulacak soru hangisi?",
        ["A) Haberi kaç kişi paylaşmış?",
         "B) Kaynak belli mi, yazar kim?",
         "C) Haber ne kadar uzun?",
         "D) Başlığı dikkat çekici mi?"],
    ),
    (
        "Bir ürünün \"iyi tasarlanmış\" olduğunu söyleyebilmek için ne gerekir?",
        ["A) Sadece estetiğine bakmak",
         "B) Sadece fiyatına bakmak",
         "C) Birden fazla ölçüte (işlevsellik, ergonomi, estetik, sürdürülebilirlik…)",
         "D) Sadece kim yaptığına bakmak"],
    ),
]


def mcq_bolum():
    """8 soruyu 2 sütunlu tablo olarak döndür (sol 4, sağ 4)."""
    from reportlab.platypus import ListFlowable

    col_w = (PAGE_W - 0.4 * cm) / 2

    rows = []
    for i in range(4):
        sol_items = mcq_cell(i + 1, SORULAR[i][0], SORULAR[i][1])
        sag_items = mcq_cell(i + 5, SORULAR[i + 4][0], SORULAR[i + 4][1])

        # Her hücreye bir iç tablo koy (sadece paragraflar listesi)
        def cell_table(items):
            inner_rows = [[p] for p in items]
            t = Table(inner_rows, colWidths=[col_w - 0.2 * cm])
            t.setStyle(TableStyle([
                ('TOPPADDING', (0, 0), (-1, -1), 1),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
                ('LEFTPADDING', (0, 0), (-1, -1), 2),
                ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            return t

        rows.append([cell_table(sol_items), cell_table(sag_items)])

    outer = Table(rows, colWidths=[col_w, col_w], spaceBefore=2, spaceAfter=2)
    outer.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('LINEAFTER', (0, 0), (0, -1), 0.5, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, COLOR_VERY_LIGHT]),
        ('BOX', (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
    ]))
    return outer


def kisa_cevap_sorular():
    """Bölüm 2 soruları: 9, 10 yazı çizgili; 11 tablo."""
    ss = s('BodyCompact', fontName='TR-Bold', fontSize=9, spaceAfter=3)
    items = []

    # Soru 9
    items.append(KeepTogether([
        Paragraph(
            '9. "İcat" ve "keşif" arasındaki farkı birer örnek vererek açıklayın.',
            ss
        ),
        WritingLines(num_lines=2, line_spacing=16),
        Spacer(1, 4),
    ]))

    # Soru 10
    items.append(KeepTogether([
        Paragraph(
            '10. Teknoloji ile tasarım arasındaki ilişkiyi bir günlük yaşam örneğiyle '
            '(telefon, araba, mobilya vb.) açıklayın.',
            ss
        ),
        WritingLines(num_lines=2, line_spacing=16),
        Spacer(1, 4),
    ]))

    return items


def build():
    doc = create_doc(OUTPUT_PATH, title=DOC_TITLE, unite_info=UNITE_INFO)
    styles = get_styles()
    elements = []

    # ── Öğrenci bilgi satırı (tek satır) ──
    elements.append(make_student_info_header())
    elements.append(Spacer(1, 3))
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 4))

    # ── Sınav başlığı + yönerge ──
    title_st = ParagraphStyle(
        'SinavTitle', fontName='TR-Bold', fontSize=14,
        textColor=COLOR_PRIMARY, leading=18, spaceAfter=4,
    )
    elements.append(Paragraph('Ünite Sonu Sınavı', title_st))
    elements.append(sınav_basligi())
    elements.append(Spacer(1, 4))

    # ── BÖLÜM 1: ÇOKTAN SEÇMELİ ──
    elements.append(bolum_baslik('BÖLÜM 1: ÇOKTAN SEÇMELİ  (8 soru × 2 puan = 16 puan)'))
    elements.append(Spacer(1, 3))
    elements.append(mcq_bolum())
    elements.append(Spacer(1, 6))

    # ── BÖLÜM 2: KISA CEVAPLI ──
    elements.append(bolum_baslik('BÖLÜM 2: KISA CEVAPLI  (2 soru × 2 puan = 4 puan)'))
    elements.append(Spacer(1, 4))
    for el in kisa_cevap_sorular():
        elements.append(el)
    elements.append(Spacer(1, 6))

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF olusturuldu: {OUTPUT_PATH}')


if __name__ == '__main__':
    build()
