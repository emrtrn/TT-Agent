"""
Unite6 -- Unite Sonu Sinavi + Cevap Anahtari (Dogadan Tasarima)
Sayfa 1: Ogrenci sinavi  --  10 MCQ x 10 puan = 100p
Sayfa 2: Ogretmen cevap anahtari

Kullanim:
    python pdf_uretim/uret_unite6_degerlendirme.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, add_page_number,
    make_student_info_header, HorizontalLine,
    COLOR_PRIMARY, COLOR_SECONDARY,
    COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_MUTED, COLOR_VERY_LIGHT_GREY, COLOR_TEXT,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, 'units', 'unit6', 'U6_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 6. Ünite'
DOC_TITLE  = '6. Ünite Sonu Sınavı'
PAGE_W     = A4[0] - 4 * cm


# ── Stil sabitleri ────────────────────────────────────────────────

S_BAS = ParagraphStyle(
    'U6D_Baslik', fontName='TR-Bold', fontSize=13,
    textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
)
S_META = ParagraphStyle(
    'U6D_Meta', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=3,
)
S_YON = ParagraphStyle(
    'U6D_Yonerge', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=3,
    backColor=COLOR_VERY_LIGHT, borderPadding=4,
)
S_BOLUM = ParagraphStyle(
    'U6D_Bolum', fontName='TR-Bold', fontSize=9,
    textColor=white, leading=13, spaceAfter=3, spaceBefore=4,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)
S_SORU = ParagraphStyle(
    'U6D_Soru', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_TEXT, leading=10, spaceAfter=1,
)
S_OPT = ParagraphStyle(
    'U6D_Opt', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_TEXT, leading=10, spaceAfter=0, leftIndent=8,
)

# Cevap anahtarı stilleri
S_CA_HDR  = ParagraphStyle(
    'U6D_CA_HDR',  fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11,
)
S_CA_CELL = ParagraphStyle(
    'U6D_CA_CELL', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11,
)
S_CA_NO   = ParagraphStyle(
    'U6D_CA_NO',   fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11, alignment=1,
)
S_CA_ANS  = ParagraphStyle(
    'U6D_CA_ANS',  fontName='TR-Bold',    fontSize=9,
    textColor=COLOR_SECONDARY, leading=11, alignment=1,
)
S_CA_NOT  = ParagraphStyle(
    'U6D_CA_NOT',  fontName='TR-Italic',  fontSize=8,
    textColor=COLOR_MUTED,     leading=11,
)
S_CA_BAS  = ParagraphStyle(
    'U6D_CA_BAS',  fontName='TR-Bold',    fontSize=12,
    textColor=COLOR_PRIMARY,   leading=16, spaceAfter=6,
)
S_CA_ALT  = ParagraphStyle(
    'U6D_CA_ALT',  fontName='TR-Bold',    fontSize=9.5,
    textColor=COLOR_PRIMARY,   leading=13, spaceAfter=4, spaceBefore=8,
)


# ── Soru ve cevap verileri ────────────────────────────────────────

SORULAR = [
    (
        'Biyomimikri kavramının en doğru tanımı hangisidir?',
        ['A) Hayvanları taklit eden robot yapımı teknolojisi',
         'B) Doğadaki canlıların özelliklerini inceleyerek yeni ürünler ve çözümler geliştirme yaklaşımı',
         'C) Doğal malzemeleri kullanarak ürün yapma yöntemi',
         'D) Biyoloji ile mimariyi birleştiren bir sanat akımı'],
    ),
    (
        'Lotus çiçeğinin yaprağında su tutunmaz; damlalar yuvarlanarak gider. Bu "lotus etkisi" hangi ürüne ilham vermiştir?',
        ['A) Güneş enerjisi toplayan panel',
         'B) Su geçirmez ve kendiliğinden temizlenen kumaş',
         'C) Hafif ama dayanıklı çatı kirişi',
         'D) Hızlı yüzücü kıyafeti'],
    ),
    (
        'Geko kertenkeleleri duvara kolayca yapışabilir çünkü ayaklarında milyonlarca ince nano tüy bulunur. Bu özelliği taklit eden ürün hangisidir?',
        ['A) Su geçirmez çizme',
         'B) Yüzücü gözlüğü',
         'C) Yapışkanlı nano yüzey bandı',
         'D) Isı yalıtım malzemesi'],
    ),
    (
        'Termit tepeleri içinde mükemmel bir doğal havalandırma sistemi çalışır. Bu sistem hangi yapıya ilham vermiştir?',
        ['A) Güneş paneli çiftliği',
         'B) Yeşil çatı (teras bahçe)',
         'C) Eastgate Centre ofis binası',
         'D) Köprü kirişi tasarımı'],
    ),
    (
        'Biyomorfizm nedir?',
        ['A) Canlıların işlevsel özelliklerini birebir taklit etme',
         'B) Doğal formları estetik amaçla tasarıma yansıtma',
         'C) Biyolojik malzemeleri doğrudan ürünlerde kullanma',
         'D) Ekosistemi koruma odaklı tasarım yapma'],
    ),
    (
        'Biyofili kavramını en iyi açıklayan ifade hangisidir?',
        ['A) Biyoçeşitliliği koruma çabası',
         'B) İnsanın doğayla olan içgüdüsel bağı ve doğaya yönelik eğilimi',
         'C) Bitkileri dekoratif tasarım ögesi olarak kullanma',
         'D) Doğal malzemeleri geri dönüştürme anlayışı'],
    ),
    (
        'Biyomimetik tasarımcının ilk ve en temel sorusu hangisidir?',
        ['A) Bu ürünün maliyeti nedir?',
         'B) Bu problemi doğa nasıl çözmüş?',
         'C) Bu formu kim daha önce çizmiş?',
         'D) Bu ürünü kimler satın alır?'],
    ),
    (
        'Köpek balığının derisindeki dişimsi çıkıntılar sürtünmeyi azaltır. Bu özellik en çok hangi alanda kullanılmıştır?',
        ['A) Hava aracı gövde tasarımı',
         'B) Tıbbi implant kaplamaları',
         'C) Yüzücü kıyafeti tasarımı',
         'D) Güneş paneli yüzeyi'],
    ),
    (
        'Bal arısının altıgen petek yapısı, az malzemeyle yüksek dayanıklılık sağlar. Bu özellik hangi tasarım ürünlerine uygulanmıştır?',
        ['A) Su geçirmez bez ve kumaşlar',
         'B) Isı pompaları ve klimalar',
         'C) Kamera lensleri ve optik sistemler',
         'D) Hafif ama dayanıklı panel ve ambalaj tasarımları'],
    ),
    (
        'Biyomimikri projeleri neden "disiplinler arası" bir yaklaşım gerektirir?',
        ['A) Çünkü yalnızca biyoloji bilgisiyle çözülemez; mühendislik, matematik ve sanatı da kapsar',
         'B) Çünkü farklı okullardaki öğrencilerle birlikte yapılmalıdır',
         'C) Çünkü doğa tek bir alanda çalışmaz; her canlı ayrı bilim dalıyla çalışır',
         'D) Çünkü farklı ülkelerin araştırmaları birleştirilmelidir'],
    ),
]

CEVAP_ANAHTARI = [
    (1,  'B', 'Biyomimikri — doğadaki canlıların özelliklerini inceleyerek çözümler geliştirme'),
    (2,  'B', 'Lotus etkisi — su geçirmez ve kendiliğinden temizlenen kumaş'),
    (3,  'C', 'Geko nano tüyleri — yapışkanlı nano yüzey bandı'),
    (4,  'C', 'Termit tepesi havalandırması — Eastgate Centre ofis binası (Zimbabwe)'),
    (5,  'B', 'Biyomorfizm — doğal formu estetik amaçla tasarıma yansıtma (işlev taklidi yok)'),
    (6,  'B', 'Biyofili — insanın doğayla olan içgüdüsel bağı ve doğaya eğilimi'),
    (7,  'B', 'Biyomimetik tasarımın temel sorusu: "Bu problemi doğa nasıl çözmüş?"'),
    (8,  'C', 'Köpek balığı derisi (sharkskin) — Speedo yüzücü kıyafeti tasarımı'),
    (9,  'D', 'Bal arısı peteği (altıgen) — hafif ama dayanıklı panel ve ambalaj'),
    (10, 'A', 'Disiplinler arası: biyoloji + mühendislik + matematik + sanat birlikte gerekir'),
]


# ── Yardımcı fonksiyonlar ─────────────────────────────────────────

def vsp(cm_val):
    return Spacer(1, cm_val * cm)


def _mcq_cell(no, soru, opts):
    col_w = (PAGE_W - 0.4 * cm) / 2 - 0.2 * cm
    items = [Paragraph(f'{no}. {soru}', S_SORU)]
    for opt in opts:
        items.append(Paragraph(f'&nbsp;&nbsp;{opt}', S_OPT))
    inner = Table([[p] for p in items], colWidths=[col_w])
    inner.setStyle(TableStyle([
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    return inner


def mcq_tablo():
    col_w = (PAGE_W - 0.4 * cm) / 2
    rows = [
        [_mcq_cell(i + 1, SORULAR[i][0], SORULAR[i][1]),
         _mcq_cell(i + 6, SORULAR[i + 5][0], SORULAR[i + 5][1])]
        for i in range(5)
    ]
    t = Table(rows, colWidths=[col_w, col_w], spaceBefore=1, spaceAfter=1)
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


# ── Sayfa 1: Sınav ────────────────────────────────────────────────

def sinav_sayfa(E):
    E.append(make_student_info_header())
    E.append(vsp(0.1))
    E.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    E.append(vsp(0.15))

    E.append(Paragraph('6. Ünite Sonu Sınavı — Doğadan Tasarıma', S_BAS))
    E.append(Paragraph(
        '<b>Adı-Soyadı:</b> _________________________  '
        '<b>Sınıf:</b> _______  <b>No:</b> _____  <b>Tarih:</b> _____________  '
        '<b>Süre:</b> 35 dk  <b>Puan:</b> 100',
        S_META,
    ))
    E.append(Paragraph(
        'Her sorunun yalnızca bir doğru cevabı vardır. '
        'Doğru seçeneği daire içine alın. <b>(Her soru 10 puan)</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    E.append(Paragraph('ÇOKTAN SEÇMELİ  (10 soru × 10 puan = 100 puan)', S_BOLUM))
    E.append(vsp(0.1))
    E.append(mcq_tablo())


# ── Sayfa 2: Cevap Anahtarı ───────────────────────────────────────

def ca_sayfa(E):
    E.append(Paragraph('Öğretmen İçin — Cevap Anahtarı', S_CA_BAS))
    E.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.0))
    E.append(vsp(0.3))

    E.append(Paragraph('Çoktan Seçmeli (her soru 10 puan)', S_CA_ALT))
    col_w = [1.3 * cm, 3.2 * cm, 12.5 * cm]
    hdr = [
        Paragraph('<b>Soru</b>', S_CA_HDR),
        Paragraph('<b>Cevap</b>', S_CA_HDR),
        Paragraph('<b>Açıklama</b>', S_CA_HDR),
    ]
    rows = [hdr]
    for no, cevap, acik in CEVAP_ANAHTARI:
        rows.append([
            Paragraph(str(no), S_CA_NO),
            Paragraph(f'<b>{cevap}</b>', S_CA_ANS),
            Paragraph(acik, S_CA_CELL),
        ])
    tablo = Table(rows, colWidths=col_w, repeatRows=1)
    tablo.setStyle(TableStyle([
        ('BACKGROUND',     (0, 0), (-1, 0),  COLOR_VERY_LIGHT),
        ('LINEBELOW',      (0, 0), (-1, 0),  1.2, COLOR_PRIMARY),
        ('GRID',           (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, None]),
        ('VALIGN',         (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',     (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING',  (0, 0), (-1, -1), 4),
        ('LEFTPADDING',    (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',   (0, 0), (-1, -1), 6),
    ]))
    E.append(tablo)
    E.append(vsp(0.4))
    E.append(Paragraph(
        '<b>Not:</b> Yalnızca yanlış cevabı cezalandırmayın. '
        'Mantıklı gerekçe sunan öğrencilere kısmi puan verilebilir.',
        S_CA_NOT,
    ))


# ── Ana üretim fonksiyonu ─────────────────────────────────────────

def build(output_path=None):
    out = output_path or OUTPUT
    doc = create_doc(out, title=DOC_TITLE, unite_info=UNITE_INFO)
    E = []

    sinav_sayfa(E)
    E.append(PageBreak())
    ca_sayfa(E)

    doc.build(E, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
