"""
Unite2 -- Unite Sonu Sinavi + Cevap Anahtari (Temel Tasarim)
Sayfa 1: Ogrenci sinavi  --  8 MCQ (80p) + 2 kisa cevapli (20p) = 100p
Sayfa 2: Ogretmen cevap anahtari

Kullanim:
    python pdf_uretim/uret_unite2_degerlendirme.py
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
OUTPUT = os.path.join(ROOT, 'units', 'unit2', 'U2_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite'
DOC_TITLE  = '2. Ünite Sonu Sınavı'
PAGE_W     = A4[0] - 4 * cm


# ── Stil sabitleri ────────────────────────────────────────────────

S_BAS = ParagraphStyle(
    'U2D_Baslik', fontName='TR-Bold', fontSize=13,
    textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
)
S_META = ParagraphStyle(
    'U2D_Meta', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=4,
)
S_YON = ParagraphStyle(
    'U2D_Yonerge', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=4,
    backColor=COLOR_VERY_LIGHT, borderPadding=5,
)
S_BOLUM = ParagraphStyle(
    'U2D_Bolum', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=6,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)
S_SORU = ParagraphStyle(
    'U2D_Soru', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)
S_OPT = ParagraphStyle(
    'U2D_Opt', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10.5, spaceAfter=0, leftIndent=8,
)
S_KISA = ParagraphStyle(
    'U2D_Kisa', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3, spaceBefore=4,
)

# Cevap anahtarı stilleri
S_CA_HDR  = ParagraphStyle(
    'U2D_CA_HDR',  fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11,
)
S_CA_CELL = ParagraphStyle(
    'U2D_CA_CELL', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11,
)
S_CA_NO   = ParagraphStyle(
    'U2D_CA_NO',   fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11, alignment=1,
)
S_CA_ANS  = ParagraphStyle(
    'U2D_CA_ANS',  fontName='TR-Bold',    fontSize=9,
    textColor=COLOR_SECONDARY, leading=11, alignment=1,
)
S_CA_NOT  = ParagraphStyle(
    'U2D_CA_NOT',  fontName='TR-Italic',  fontSize=8,
    textColor=COLOR_MUTED,     leading=11,
)
S_CA_BAS  = ParagraphStyle(
    'U2D_CA_BAS',  fontName='TR-Bold',    fontSize=12,
    textColor=COLOR_PRIMARY,   leading=16, spaceAfter=6,
)
S_CA_ALT  = ParagraphStyle(
    'U2D_CA_ALT',  fontName='TR-Bold',    fontSize=9.5,
    textColor=COLOR_PRIMARY,   leading=13, spaceAfter=4, spaceBefore=8,
)
S_CA_ACIK = ParagraphStyle(
    'U2D_CA_ACIK', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT,      leading=12, leftIndent=8,
)


# ── Soru ve cevap verileri ────────────────────────────────────────

SORULAR = [
    (
        'Tasarımda "derinlik" ya da "alan" hissi yaratan, öne-arkaya konumlandırma ve örtüşmeyle ilgili eleman hangisidir?',
        ['A) Doku', 'B) Çizgi', 'C) Mekân (Uzam)', 'D) Valör'],
    ),
    (
        'Bir afişte siyah arka plan üzerine sarı yazı kullanılması hangi tasarım ilkesine en iyi örnek oluşturur?',
        ['A) Denge', 'B) Birlik', 'C) Ritim', 'D) Zıtlık (Kontrast)'],
    ),
    (
        'Aşağıdakilerden hangisi "yeniden yorumlama"yı en doğru tanımlar?',
        ['A) Bir eseri birebir kopyalamak',
         'B) Bir eserin içeriğini inceleyip bağlamdan kopmadan kendi ifadesiyle aktarmak',
         'C) Eserden bütünüyle farklı, yeni bir şey üretmek',
         'D) Bir eserin renklerini değiştirmek'],
    ),
    (
        'Anadolu halılarında tekrar eden motif dizileri hangi tasarım ilkesini en çok yansıtır?',
        ['A) Vurgu', 'B) Oran-Orantı', 'C) Ritim', 'D) Hareket'],
    ),
    (
        'Analoji yapabilmek için aşağıdaki adımlardan hangisi önce gelir?',
        ['A) İki unsuru görsel olarak çizmek',
         'B) Konu ya da kavramı belirlemek',
         'C) Soyut renk ve doku seçmek',
         'D) Slogan yazmak'],
    ),
    (
        '"Valör", bir nesneye ya da yüzeye uygulandığında neyi ifade eder?',
        ['A) Rengin sıcak ya da soğuk olması',
         'B) Rengin açık-koyu değeri (ışık-gölge aralığı)',
         'C) Nesnenin üç boyutlu dış biçimi',
         'D) Birden fazla rengin bir arada kullanılması'],
    ),
    (
        'Tasarım sürecinde taslak çiziminin temel amacı nedir?',
        ['A) Ürünü bitmiş hâliyle göstermek',
         'B) Maliyeti hesaplamak',
         'C) Fikri görselleştirmek, alternatifler üretmek ve en iyisini seçmek',
         'D) Akrana sunmak için hazırlamak'],
    ),
    (
        'Bir bina cephesinin tam orta eksenine göre sağ ve sol tarafı birbirinin yansıması gibi tasarlanmıştır. Bu hangi denge türüdür?',
        ['A) Asimetrik denge', 'B) Simetrik denge',
         'C) Dinamik denge', 'D) Radyal denge'],
    ),
]

CEVAP_ANAHTARI = [
    (1,  'C', 'Mekân (Uzam) — derinlik ve alan hissi, örtüşme ve konumlandırma ile oluşur'),
    (2,  'D', 'Zıtlık (Kontrast) — siyah/sarı gibi keskin renk karşıtlığı'),
    (3,  'B', 'Yeniden yorumlama — bağlamdan kopmadan kendi ifadesiyle aktarma'),
    (4,  'C', 'Ritim — tekrar eden motif dizileri (halı, çini vb.)'),
    (5,  'B', 'Analoji — önce konu/kavramı belirle, sonra benzer unsuru bul'),
    (6,  'B', 'Valör — rengin açık-koyu değeri; ışık ve gölgeyi ifade eder'),
    (7,  'C', 'Taslak — fikri görselleştirmek ve alternatifleri karşılaştırmak için'),
    (8,  'B', 'Simetrik denge — eksenin her iki yanı birbirinin aynası'),
]

KISA_CEVAP_CA = [
    (
        '9. "Yorumlamak" ile "kopyalamak" arasındaki fark',
        [
            'Yorumlamak: Orijinal eserin içeriğini, bağlamını ya da mesajını koruyarak '
            'kendi üslubuyla yeniden ifade etmektir.',
            'Kopyalamak: Eserin birebir aynısını üretmektir; özgün katkı yoktur.',
            'Tam puan için: kavramsal fark açıklanmış (4 p) + somut tasarım örneği (4 p) + '
            'iki kavramı karıştırmıyor (2 p).',
        ],
    ),
    (
        '10. Analoji yapma adımları',
        [
            'Adım 1 — Konu/kavramı belirle (3 p).',
            'Adım 2 — Benzerlik kuracağın iki unsuru seç (3 p).',
            'Adım 3 — Benzerliği sözel (slogan), görsel (çizim), soyut (renk/doku) veya '
            'nesnel (somut örnek) olarak yansıt (4 p).',
            'Farklı sıralama veya ek adım kabul edilir; anlam tutarlıysa tam puan.',
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

    E.append(Paragraph('2. Ünite Sonu Sınavı — Temel Tasarım', S_BAS))
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
            '9. "Yorumlamak" ile "kopyalamak" arasındaki farkı bir tasarım örneği vererek '
            'açıklayın. <i>(10 puan)</i>',
            S_KISA,
        ),
        WritingLines(num_lines=3, line_spacing=15),
        vsp(0.2),
    ]))

    E.append(KeepTogether([
        Paragraph(
            '10. Analoji yapabilmek için hangi adımlar izlenmelidir? '
            'En az 3 adımı kısaca açıklayın. <i>(10 puan)</i>',
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
