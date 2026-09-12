"""
Unite4 -- Unite Sonu Sinavi + Cevap Anahtari (Bilgisayar Destekli Tasarim)
Sayfa 1: Ogrenci sinavi  --  8 MCQ (80p) + 2 kisa cevapli (20p) = 100p
Sayfa 2: Ogretmen cevap anahtari

Kullanim:
    python pdf_uretim/uret_unite4_degerlendirme_yeni.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_MUTED, COLOR_VERY_LIGHT_GREY, COLOR_TEXT,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, 'units', 'unit4', 'U4_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 4. Ünite'
DOC_TITLE  = '4. Ünite Sonu Sınavı'
PAGE_W     = A4[0] - 4 * cm


# ── Stil sabitleri ────────────────────────────────────────────────

S_BAS = ParagraphStyle(
    'U4D_Baslik', fontName='TR-Bold', fontSize=13,
    textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
)
S_META = ParagraphStyle(
    'U4D_Meta', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=4,
)
S_YON = ParagraphStyle(
    'U4D_Yonerge', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=4,
    backColor=COLOR_VERY_LIGHT, borderPadding=5,
)
S_BOLUM = ParagraphStyle(
    'U4D_Bolum', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=6,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)
S_SORU = ParagraphStyle(
    'U4D_Soru', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)
S_OPT = ParagraphStyle(
    'U4D_Opt', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10.5, spaceAfter=0, leftIndent=8,
)
S_KISA = ParagraphStyle(
    'U4D_Kisa', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3, spaceBefore=4,
)

# Cevap anahtarı stilleri
S_CA_HDR  = ParagraphStyle(
    'U4D_CA_HDR',  fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11,
)
S_CA_CELL = ParagraphStyle(
    'U4D_CA_CELL', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11,
)
S_CA_NO   = ParagraphStyle(
    'U4D_CA_NO',   fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11, alignment=1,
)
S_CA_ANS  = ParagraphStyle(
    'U4D_CA_ANS',  fontName='TR-Bold',    fontSize=9,
    textColor=COLOR_SECONDARY, leading=11, alignment=1,
)
S_CA_NOT  = ParagraphStyle(
    'U4D_CA_NOT',  fontName='TR-Italic',  fontSize=8,
    textColor=COLOR_MUTED,     leading=11,
)
S_CA_BAS  = ParagraphStyle(
    'U4D_CA_BAS',  fontName='TR-Bold',    fontSize=12,
    textColor=COLOR_PRIMARY,   leading=16, spaceAfter=6,
)
S_CA_ALT  = ParagraphStyle(
    'U4D_CA_ALT',  fontName='TR-Bold',    fontSize=9.5,
    textColor=COLOR_PRIMARY,   leading=13, spaceAfter=4, spaceBefore=8,
)
S_CA_ACIK = ParagraphStyle(
    'U4D_CA_ACIK', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT,      leading=12, leftIndent=8,
)


# ── Soru ve cevap verileri ────────────────────────────────────────

SORULAR = [
    (
        'Bilgisayar Destekli Tasarım (CAD) programlarının temel amacı nedir?',
        ['A) Yazı yazmak ve belge hazırlamak',
         'B) Tasarım fikirlerini dijital ortamda çizmek, modellemek ve görselleştirmek',
         'C) Fotoğraf ve video düzenlemek',
         'D) İnternet üzerinde arama yapmak'],
    ),
    (
        'Görünüş çıkarma yönteminde bir nesnenin kaç temel görünüşü çizilir?',
        ['A) 1  (yalnızca ön görünüş)',
         'B) 2  (ön ve arka)',
         'C) 3  (ön, üst ve yan)',
         'D) 6  (tüm yüzeyler)'],
    ),
    (
        'Tinkercad\'de "Delik" (Hole) işlevi ne işe yarar?',
        ['A) İki şekli birbirine yapıştırmak için',
         'B) Şeklin rengini değiştirmek için',
         'C) Şeklin içinden boşluk veya oyuk oluşturmak için',
         'D) Şekli döndürmek için'],
    ),
    (
        'Bir nesnenin "ön görünüşü" neyi gösterir?',
        ['A) Nesnenin yukarıdan bakıldığındaki şeklini',
         'B) Nesnenin iç yapısını ve kesitini',
         'C) Nesnenin arka yüzeyini',
         'D) Nesnenin önden bakıldığındaki düz yansımasını'],
    ),
    (
        '2B (iki boyutlu) ve 3B (üç boyutlu) tasarım arasındaki temel fark nedir?',
        ['A) 2B renk kullanır, 3B kullanmaz',
         'B) 2B yalnızca genişlik ve yüksekliği; 3B genişlik, yükseklik ve derinliği gösterir',
         'C) 2B bilgisayarda yapılır, 3B elle yapılır',
         'D) 3B yalnızca mimarlıkta kullanılır'],
    ),
    (
        'Tinkercad\'de 3B nesne oluştururken kullanılan temel yöntem hangisidir?',
        ['A) Fotoğraf çekerek nesneyi taramak',
         'B) Serbest elle çizim yapmak',
         'C) Kod yazmak',
         'D) Temel geometrik şekilleri birleştirerek ve keserek şekillendirmek'],
    ),
    (
        'Tasarım sürecinde "eskiz → 2B çizim → 3B model" sıralamasının temel amacı nedir?',
        ['A) Her adım ayrı bir not için gereklidir',
         'B) 3B model olmadan sunum yapılamaz',
         'C) Fikri adım adım geliştirmek ve somutlaştırmak için',
         'D) Yazılım böyle zorunlu kılıyor'],
    ),
    (
        'Tinkercad\'de tasarladığın nesnenin ölçülerine dikkat etmek neden önemlidir?',
        ['A) Ölçüler yalnızca baskıda önemlidir, dijital tasarımda önemsizdir',
         'B) Nesnenin gerçek dünya boyutlarına yakın ölçüler kullanılması gerekir',
         'C) Tüm şekillerin aynı boyutta olması zorunludur',
         'D) Ölçü yerine yalnızca görsel orantı yeterlidir'],
    ),
]

CEVAP_ANAHTARI = [
    (1,  'B', 'CAD — tasarım fikirlerini dijital ortamda çizmek, modellemek, görselleştirmek'),
    (2,  'C', 'Görünüş çıkarma — ön, üst ve yan olmak üzere 3 temel görünüş'),
    (3,  'C', 'Delik (Hole) — şeklin içinden boşluk veya oyuk oluşturur'),
    (4,  'D', 'Ön görünüş — nesnenin önden bakıldığındaki düz yansıması'),
    (5,  'B', '2B: genişlik+yükseklik; 3B: genişlik+yükseklik+derinlik'),
    (6,  'D', 'Tinkercad temel yöntemi — geometrik şekilleri birleştirme ve kesme'),
    (7,  'C', 'Eskiz→2B→3B sırası — fikri adım adım geliştirmek ve somutlaştırmak için'),
    (8,  'B', 'Ölçü önemi — gerçek dünya boyutlarına yakın ölçüler kullanılmalıdır'),
]

KISA_CEVAP_CA = [
    (
        '9. 2B ve 3B tasarım araçlarının farkları ve kullanım aşamaları',
        [
            '2B (Paint gibi): genişlik ve yükseklik boyutlarını gösterir; ön/üst/yan '
            'görünüşleri çizmek için kullanılır. Fikri 2D olarak belgeleme aşamasında uygundur.',
            '3B (Tinkercad gibi): genişlik, yükseklik ve derinliği gösterir; nesneyi tüm '
            'açılardan modellemek için kullanılır. Prototip oluşturma aşamasında uygundur.',
            'Tam puan için: 2B ve 3B fark doğru açıklanmış (5 p) + hangi aşamada '
            'kullanıldığı belirtilmiş (5 p).',
        ],
    ),
    (
        '10. Görünüş çıkarmanın önemi',
        [
            'Ön görünüş: genişlik + yükseklik. Üst görünüş: genişlik + derinlik. '
            'Yan görünüş: yükseklik + derinlik bilgisini verir.',
            'Bu üç görünüş birleşince nesnenin tüm boyutları tam olarak anlaşılır; '
            'üretimde veya 3B modelleme sırasında hata riski azalır.',
            'Tam puan için: görünüş türleri açıklanmış (5 p) + önemini gerekçelendirmiş (5 p).',
        ],
    ),
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
         _mcq_cell(i + 5, SORULAR[i + 4][0], SORULAR[i + 4][1])]
        for i in range(4)
    ]
    t = Table(rows, colWidths=[col_w, col_w], spaceBefore=2, spaceAfter=2)
    t.setStyle(TableStyle([
        ('VALIGN',         (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',     (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING',  (0, 0), (-1, -1), 4),
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

    E.append(Paragraph('4. Ünite Sonu Sınavı — Bilgisayar Destekli Tasarım', S_BAS))
    E.append(Paragraph(
        '<b>Adı-Soyadı:</b> _________________________  '
        '<b>Sınıf:</b> _______  <b>No:</b> _____  <b>Tarih:</b> _____________  '
        '<b>Süre:</b> 35 dk  <b>Puan:</b> 100',
        S_META,
    ))
    E.append(Paragraph(
        'Bu sınav 2 bölümden oluşur: Çoktan Seçmeli (8 soru × 10 puan = 80 puan) ve '
        'Kısa Cevaplı (2 soru × 10 puan = 20 puan). <b>Toplam: 100 puan.</b> '
        'Her soruda yalnızca bir doğru cevap vardır; doğru seçeneği daire içine alın.',
        S_YON,
    ))
    E.append(vsp(0.2))

    E.append(Paragraph('BÖLÜM 1: ÇOKTAN SEÇMELİ  (8 soru × 10 puan = 80 puan)', S_BOLUM))
    E.append(vsp(0.15))
    E.append(mcq_tablo())
    E.append(vsp(0.25))

    E.append(Paragraph('BÖLÜM 2: KISA CEVAPLI  (2 soru × 10 puan = 20 puan)', S_BOLUM))
    E.append(vsp(0.15))

    E.append(KeepTogether([
        Paragraph(
            '9. 2B ve 3B tasarım araçlarının farklarını açıklayın. '
            'Her birinin tasarım sürecinin hangi aşamasında kullanıldığını belirtin. '
            '<i>(10 puan)</i>',
            S_KISA,
        ),
        WritingLines(num_lines=3, line_spacing=15),
        vsp(0.2),
    ]))

    E.append(KeepTogether([
        Paragraph(
            '10. Bir nesnenin farklı açılardan çizilmesi (görünüş çıkarma) neden önemlidir? '
            'Ön, üst ve yan görünüşlerin her birinin hangi bilgiyi verdiğini açıklayın. '
            '<i>(10 puan)</i>',
            S_KISA,
        ),
        WritingLines(num_lines=3, line_spacing=15),
        vsp(0.1),
    ]))


# ── Sayfa 2: Cevap Anahtarı ───────────────────────────────────────

def ca_sayfa(E):
    E.append(Paragraph('Öğretmen İçin — Cevap Anahtarı', S_CA_BAS))
    E.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.0))
    E.append(vsp(0.3))

    E.append(Paragraph('Bölüm 1: Çoktan Seçmeli (her soru 10 puan)', S_CA_ALT))
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
    E.append(vsp(0.5))

    E.append(Paragraph('Bölüm 2: Kısa Cevaplı — Değerlendirme Rehberi', S_CA_ALT))
    for baslik, maddeler in KISA_CEVAP_CA:
        E.append(Paragraph(f'<b>{baslik}</b>', S_CA_HDR))
        E.append(vsp(0.1))
        for m in maddeler:
            E.append(Paragraph(f'• {m}', S_CA_ACIK))
        E.append(vsp(0.25))

    E.append(vsp(0.2))
    E.append(Paragraph(
        '<b>Not:</b> Yalnızca yanlış cevabı cezalandırmayın. '
        'Mantıklı gerekçe sunan öğrencilere kısmi puan verilebilir. '
        'Özgün ve doğru örnekleri tam puanla kabul edin.',
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
