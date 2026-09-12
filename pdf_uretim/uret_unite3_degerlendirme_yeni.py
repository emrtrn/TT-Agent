"""
Unite3 -- Unite Sonu Sinavi + Cevap Anahtari (Tasarim Odakli Surec)
Sayfa 1: Ogrenci sinavi  --  8 MCQ (80p) + 2 kisa cevapli (20p) = 100p
Sayfa 2: Ogretmen cevap anahtari

Kullanim:
    python pdf_uretim/uret_unite3_degerlendirme_yeni.py
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
OUTPUT = os.path.join(ROOT, 'units', 'unit3', 'U3_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 3. Ünite'
DOC_TITLE  = '3. Ünite Sonu Sınavı'
PAGE_W     = A4[0] - 4 * cm


# ── Stil sabitleri ────────────────────────────────────────────────

S_BAS = ParagraphStyle(
    'U3D_Baslik', fontName='TR-Bold', fontSize=13,
    textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
)
S_META = ParagraphStyle(
    'U3D_Meta', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=4,
)
S_YON = ParagraphStyle(
    'U3D_Yonerge', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=3,
    backColor=COLOR_VERY_LIGHT, borderPadding=4,
)
S_BOLUM = ParagraphStyle(
    'U3D_Bolum', fontName='TR-Bold', fontSize=9,
    textColor=white, leading=13, spaceAfter=3, spaceBefore=4,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)
S_SORU = ParagraphStyle(
    'U3D_Soru', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_TEXT, leading=10, spaceAfter=1,
)
S_OPT = ParagraphStyle(
    'U3D_Opt', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_TEXT, leading=10, spaceAfter=0, leftIndent=8,
)
S_KISA = ParagraphStyle(
    'U3D_Kisa', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11, spaceAfter=2, spaceBefore=3,
)

# Cevap anahtarı stilleri
S_CA_HDR  = ParagraphStyle(
    'U3D_CA_HDR',  fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11,
)
S_CA_CELL = ParagraphStyle(
    'U3D_CA_CELL', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11,
)
S_CA_NO   = ParagraphStyle(
    'U3D_CA_NO',   fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11, alignment=1,
)
S_CA_ANS  = ParagraphStyle(
    'U3D_CA_ANS',  fontName='TR-Bold',    fontSize=9,
    textColor=COLOR_SECONDARY, leading=11, alignment=1,
)
S_CA_NOT  = ParagraphStyle(
    'U3D_CA_NOT',  fontName='TR-Italic',  fontSize=8,
    textColor=COLOR_MUTED,     leading=11,
)
S_CA_BAS  = ParagraphStyle(
    'U3D_CA_BAS',  fontName='TR-Bold',    fontSize=12,
    textColor=COLOR_PRIMARY,   leading=16, spaceAfter=6,
)
S_CA_ALT  = ParagraphStyle(
    'U3D_CA_ALT',  fontName='TR-Bold',    fontSize=9.5,
    textColor=COLOR_PRIMARY,   leading=13, spaceAfter=4, spaceBefore=8,
)
S_CA_ACIK = ParagraphStyle(
    'U3D_CA_ACIK', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT,      leading=12, leftIndent=8,
)


# ── Soru ve cevap verileri ────────────────────────────────────────

SORULAR = [
    (
        'Tasarım Odaklı Düşünme sürecinde "empati" adımının temel amacı nedir?',
        ['A) Fikir üretmek için beyin fırtınası yapmak',
         'B) Problemi yaşayan kişinin yerine geçerek ihtiyaçlarını ve duygularını anlamak',
         'C) Tasarımı test etmek ve geri bildirim almak',
         'D) Prototip üretmek için malzeme seçmek'],
    ),
    (
        'Aşağıdakilerden hangisi "prototip"i en doğru tanımlar?',
        ['A) Satışa hazır son ürün',
         'B) Tasarımın bilgisayarda çizilmiş görseli',
         'C) Tasarım fikrinin test edilmesi için yapılan deneme modeli',
         'D) Bir ürünün fabrikada üretilen ilk kopyası'],
    ),
    (
        'Design Thinking döngüsünde "Nasıl çözebiliriz?" sorusu hangi adımda sorulur?',
        ['A) Problem Tespiti', 'B) Empati',
         'C) Fikir Üretimi', 'D) Test / Geri Bildirim'],
    ),
    (
        'Ergonomi kavramı tasarımda neyi ifade eder?',
        ['A) Ürünün görsel açıdan güzel olması',
         'B) Ürünün ucuz malzemeyle üretilmesi',
         'C) Ürünün insan vücuduna, hareketlerine ve kullanım alışkanlıklarına uygun tasarlanması',
         'D) Ürünün çevre dostu olması'],
    ),
    (
        'Aşağıdakilerden hangisi "sürdürülebilir tasarım"ı en doğru tanımlar?',
        ['A) Her yıl güncellenen, moda olan ürünler tasarlamak',
         'B) Geleceği düşünerek az kaynak harcayan, geri dönüştürülebilir, uzun ömürlü ürünler tasarlamak',
         'C) Yalnızca doğal malzeme kullanan ürünler tasarlamak',
         'D) Tasarım sürecini mümkün olduğunca kısa tutmak'],
    ),
    (
        '"Crazy 8" etkinliği Design Thinking\'in hangi adımında kullanılır ve amacı nedir?',
        ['A) Problem Tespiti — problemi 8 farklı açıdan incelemek',
         'B) Fikir Üretimi — 8 dakikada 8 farklı fikir çizmek',
         'C) Test Aşaması — 8 kullanıcıyla ürünü denemek',
         'D) Revize — tasarımda 8 değişiklik yapmak'],
    ),
    (
        'Bir tasarım prototipinin test edilmesi sırasında kullanıcıdan gelen eleştiri nasıl değerlendirilmelidir?',
        ['A) Tasarımın başarısız olduğu anlamına gelir; sıfırdan başlanmalıdır',
         'B) Görmezden gelinmeli; tasarımcı kendi kararında ısrar etmelidir',
         'C) Tasarımı geliştirme fırsatı olarak görülmeli ve revize aşamasına taşınmalıdır',
         'D) Yalnızca çok sayıda kişi aynı eleştiriyi yapıyorsa dikkate alınmalıdır'],
    ),
    (
        'Tasarım Odaklı Düşünme döngüsü "revize" adımıyla neden bitmez?',
        ['A) Çünkü revize yapmak çok zaman alır',
         'B) Çünkü tasarım mükemmele ulaştığında döngü otomatik olarak durur',
         'C) Çünkü revize edilen ürün yeni bir döngünün başlangıcıdır; tasarım sürekli gelişir',
         'D) Çünkü revize adımından sonra sunum zorunludur'],
    ),
]

CEVAP_ANAHTARI = [
    (1,  'B', 'Empati — kişinin yerine geçerek ihtiyaçlarını ve duygularını anlamak'),
    (2,  'C', 'Prototip — tasarım fikrinin test edilmesi için yapılan deneme modeli'),
    (3,  'C', 'Fikir Üretimi — "Nasıl çözebiliriz?" sorusu bu adımda sorulur'),
    (4,  'C', 'Ergonomi — insan vücuduna, hareketlerine ve kullanım alışkanlıklarına uygunluk'),
    (5,  'B', 'Sürdürülebilir tasarım — az kaynak, geri dönüştürülebilir, uzun ömürlü'),
    (6,  'B', 'Crazy 8 — fikir üretimi adımında 8 dakikada 8 farklı fikir çizilir'),
    (7,  'C', 'Eleştiri → geliştirme fırsatı; revize aşamasına taşınmalıdır'),
    (8,  'C', 'Döngü bitmez — revize edilen ürün yeni bir döngünün başlangıcıdır'),
]

KISA_CEVAP_CA = [
    (
        '9. "Empati" ile "sempati" arasındaki fark',
        [
            'Empati: Kişinin yerine geçmek, onun bakış açısından hissetmek ve düşünmek.',
            'Sempati: Karşıdakine dışarıdan acımak; kendi perspektifinden yaklaşmak.',
            'Tasarımda empati tercih edilir çünkü kullanıcının gerçek ihtiyacını ancak '
            'onun yerine geçerek anlayabiliriz; sempati yüzeysel kalır.',
            'Tam puan için: fark doğru tanımlanmış (4 p) + tasarımda neden empati gerektiği (3 p) '
            '+ kendi sürecinden örnek (3 p).',
        ],
    ),
    (
        '10. Prototip neden mükemmel olmak zorunda değildir?',
        [
            'Prototip, fikri hızlı test etmek ve hataları erken yakalamak için yapılan deneme modelidir.',
            'Mükemmellik değil, işe yararlık denenir; hızlı yapılır, revize için açık kalır.',
            'Tam puan için: prototip amacı doğru açıklanmış (4 p) + "mükemmel olmak zorunda değil" '
            'gerekçesi verilmiş (3 p) + kişisel güçlük ve çözüm örneği (3 p).',
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

    E.append(Paragraph('3. Ünite Sonu Sınavı — Tasarım Odaklı Süreç', S_BAS))
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
    E.append(vsp(0.1))
    E.append(mcq_tablo())
    E.append(vsp(0.15))

    E.append(Paragraph('BÖLÜM 2: KISA CEVAPLI  (2 soru × 10 puan = 20 puan)', S_BOLUM))
    E.append(vsp(0.1))

    E.append(KeepTogether([
        Paragraph(
            '9. "Empati" ile "sempati" arasındaki farkı açıklayın. '
            'Tasarım sürecinde empati neden sempati yerine tercih edilir? <i>(10 puan)</i>',
            S_KISA,
        ),
        WritingLines(num_lines=3, line_spacing=14),
        vsp(0.15),
    ]))

    E.append(KeepTogether([
        Paragraph(
            '10. Bir prototip neden mükemmel olmak zorunda değildir? '
            'Prototip yapmanın asıl amacını açıklayın. <i>(10 puan)</i>',
            S_KISA,
        ),
        WritingLines(num_lines=3, line_spacing=14),
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
