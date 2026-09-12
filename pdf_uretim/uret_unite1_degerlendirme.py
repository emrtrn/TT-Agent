"""
Unite1 -- Unite Sonu Sinavi + Cevap Anahtari
Sayfa 1: Ogrenci sinavi  --  8 MCQ (80p) + 2 kisa cevapli (20p) = 100p
Sayfa 2: Ogretmen cevap anahtari

Kullanim:
    python pdf_uretim/uret_unite1_degerlendirme.py
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
OUTPUT = os.path.join(ROOT, 'units', 'unit1', 'U1_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 1. Ünite'
DOC_TITLE  = '1. Ünite Sonu Sınavı'
PAGE_W     = A4[0] - 4 * cm


# ── Stil sabitleri ────────────────────────────────────────────────

S_BAS = ParagraphStyle(
    'U1D_Baslik', fontName='TR-Bold', fontSize=13,
    textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
)
S_YON = ParagraphStyle(
    'U1D_Yonerge', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=4,
    backColor=COLOR_VERY_LIGHT, borderPadding=5,
)
S_BOLUM = ParagraphStyle(
    'U1D_Bolum', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=6,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)
S_SORU = ParagraphStyle(
    'U1D_Soru', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)
S_OPT = ParagraphStyle(
    'U1D_Opt', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10.5, spaceAfter=0, leftIndent=8,
)
S_KISA = ParagraphStyle(
    'U1D_Kisa', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3, spaceBefore=4,
)

# Cevap anahtarı stilleri
S_CA_HDR  = ParagraphStyle(
    'U1D_CA_HDR',  fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11,
)
S_CA_CELL = ParagraphStyle(
    'U1D_CA_CELL', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11,
)
S_CA_NO   = ParagraphStyle(
    'U1D_CA_NO',   fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11, alignment=1,
)
S_CA_ANS  = ParagraphStyle(
    'U1D_CA_ANS',  fontName='TR-Bold',    fontSize=9,
    textColor=COLOR_SECONDARY, leading=11, alignment=1,
)
S_CA_NOT  = ParagraphStyle(
    'U1D_CA_NOT',  fontName='TR-Italic',  fontSize=8,
    textColor=COLOR_MUTED,     leading=11,
)
S_CA_BAS  = ParagraphStyle(
    'U1D_CA_BAS',  fontName='TR-Bold',    fontSize=12,
    textColor=COLOR_PRIMARY,   leading=16, spaceAfter=6,
)
S_CA_ALT  = ParagraphStyle(
    'U1D_CA_ALT',  fontName='TR-Bold',    fontSize=9.5,
    textColor=COLOR_PRIMARY,   leading=13, spaceAfter=4, spaceBefore=8,
)
S_CA_ACIK = ParagraphStyle(
    'U1D_CA_ACIK', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT,      leading=12, leftIndent=8,
)


# ── Soru ve cevap verileri ────────────────────────────────────────

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
        'Bir ürünün "iyi tasarlanmış" olduğunu söyleyebilmek için aşağıdakilerden hangisine bakılmalıdır?',
        ["A) Sadece estetiğine",
         "B) Sadece fiyatına",
         "C) Birden fazla ölçüte (işlevsellik, ergonomi, estetik, sürdürülebilirlik vb.)",
         "D) Sadece kim yaptığına"],
    ),
]

CEVAP_ANAHTARI = [
    (1,  'B', 'İcat — daha önce olmayan bir şeyin ilk kez yapılması (Graham Bell → telefon)'),
    (2,  'C', 'Endüstri 4.0 — akıllı fabrikalar, nesnelerin interneti, yapay zekâ'),
    (3,  'B', 'Teknik — adım adım uygulanan yol veya yöntem'),
    (4,  'B', 'Grafik tasarım değil — şehir parkı mimari/çevre tasarımıdır'),
    (5,  'C', 'STEAM — Science, Technology, Engineering, Arts, Mathematics; "A" = Sanat'),
    (6,  'C', 'Endüstri 5.0 — insan-makine iş birliği ve sürdürülebilirlik odağı'),
    (7,  'B', 'Medya okuryazarlığı — kaynak ve yazar önce sorgulanmalı'),
    (8,  'C', 'İyi tasarım çok ölçütlüdür: işlevsellik, ergonomi, estetik, sürdürülebilirlik'),
]

KISA_CEVAP_CA = [
    (
        '9. "İcat" ve "keşif" arasındaki fark',
        [
            'İcat: Daha önce var olmayan bir ürün/cihaz ilk kez yapılır. Örnek: Graham Bell → telefon.',
            'Keşif: Doğada zaten var olan bir şey ilk kez fark edilir. Örnek: Kolomb → Amerika.',
            'Tam puan için: fark açıklanmış (4 p) + her iki örnek doğru (3 + 3 p).',
        ],
    ),
    (
        '10. Teknoloji ile tasarım arasındaki ilişki',
        [
            'Teknoloji "nasıl çalışır"ı (işlevsellik), tasarım "nasıl görünür ve kullanılır"ı (estetik, ergonomi) çözer.',
            'Örnek: Akıllı telefon — işlemcisi/yazılımı teknoloji, ekran yerleşimi ve rengi tasarımdır.',
            'Tam puan için: ilişki net ifade (5 p) + günlük yaşam örneği ve açıklaması (5 p).',
        ],
    ),
]


# ── Sayfa 1: Sınav ────────────────────────────────────────────────

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


def sinav_sayfa(E):
    E.append(make_student_info_header())
    E.append(vsp(0.1))
    E.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    E.append(vsp(0.15))

    E.append(Paragraph('1. Ünite Sonu Sınavı — Teknoloji ve Tasarım Öğreniyorum', S_BAS))
    E.append(Paragraph(
        '<b>Adı-Soyadı:</b> _________________________  '
        '<b>Sınıf:</b> _______  <b>No:</b> _____  <b>Tarih:</b> _____________  '
        '<b>Süre:</b> 35 dk  <b>Puan:</b> 100',
        ParagraphStyle('U1D_Meta', fontName='TR-Regular', fontSize=8,
                       textColor=COLOR_TEXT, leading=11, spaceAfter=4),
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
            '9. "İcat" ve "keşif" arasındaki farkı birer örnek vererek açıklayın. '
            '<i>(10 puan)</i>',
            S_KISA,
        ),
        WritingLines(num_lines=3, line_spacing=15),
        vsp(0.2),
    ]))

    E.append(KeepTogether([
        Paragraph(
            '10. Teknoloji ile tasarım arasındaki ilişkiyi bir günlük yaşam örneğiyle '
            '(telefon, araba, mobilya vb.) açıklayın. <i>(10 puan)</i>',
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

    # MCQ tablosu
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

    # Kısa cevap rehberi
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
