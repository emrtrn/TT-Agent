"""
Unite7 -- Unite Sonu Sinavi + Cevap Anahtari (Enerjinin Donusumu ve Tasarim)
Sayfa 1: Ogrenci sinavi  --  8 MCQ x 10p + 2 kisa x 10p = 100p
Sayfa 2: Ogretmen cevap anahtari

Kullanim:
    python pdf_uretim/uret_unite7_degerlendirme.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_SECONDARY,
    COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_MUTED, COLOR_VERY_LIGHT_GREY, COLOR_TEXT,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, 'units', 'unit7', 'U7_PDF_04_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarim • 7. Sinif • 7. Unite'
DOC_TITLE  = '7. Unite Sonu Sinavi'
PAGE_W     = A4[0] - 4 * cm


# Stil sabitleri (kompakt)

S_BAS = ParagraphStyle(
    'U7D_Baslik', fontName='TR-Bold', fontSize=13,
    textColor=COLOR_PRIMARY, leading=17, spaceAfter=3,
)
S_META = ParagraphStyle(
    'U7D_Meta', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=3,
)
S_YON = ParagraphStyle(
    'U7D_Yonerge', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=3,
    backColor=COLOR_VERY_LIGHT, borderPadding=4,
)
S_BOLUM = ParagraphStyle(
    'U7D_Bolum', fontName='TR-Bold', fontSize=9,
    textColor=white, leading=13, spaceAfter=3, spaceBefore=4,
    backColor=COLOR_PRIMARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)
S_SORU = ParagraphStyle(
    'U7D_Soru', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_TEXT, leading=10, spaceAfter=1,
)
S_OPT = ParagraphStyle(
    'U7D_Opt', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_TEXT, leading=10, spaceAfter=0, leftIndent=8,
)
S_KISA = ParagraphStyle(
    'U7D_Kisa', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11, spaceAfter=2, spaceBefore=3,
)

# Cevap anahtari stilleri
S_CA_HDR  = ParagraphStyle(
    'U7D_CA_HDR',  fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11,
)
S_CA_CELL = ParagraphStyle(
    'U7D_CA_CELL', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11,
)
S_CA_NO   = ParagraphStyle(
    'U7D_CA_NO',   fontName='TR-Bold',    fontSize=8.5,
    textColor=COLOR_PRIMARY,   leading=11, alignment=1,
)
S_CA_ANS  = ParagraphStyle(
    'U7D_CA_ANS',  fontName='TR-Bold',    fontSize=9,
    textColor=COLOR_SECONDARY, leading=11, alignment=1,
)
S_CA_NOT  = ParagraphStyle(
    'U7D_CA_NOT',  fontName='TR-Italic',  fontSize=8,
    textColor=COLOR_MUTED,     leading=11,
)
S_CA_BAS  = ParagraphStyle(
    'U7D_CA_BAS',  fontName='TR-Bold',    fontSize=12,
    textColor=COLOR_PRIMARY,   leading=16, spaceAfter=6,
)
S_CA_ALT  = ParagraphStyle(
    'U7D_CA_ALT',  fontName='TR-Bold',    fontSize=9.5,
    textColor=COLOR_PRIMARY,   leading=13, spaceAfter=4, spaceBefore=8,
)
S_CA_KISA = ParagraphStyle(
    'U7D_CA_KISA', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT,      leading=11, spaceAfter=3,
)


# Soru ve cevap verileri

SORULAR = [
    (
        'Afagidakilerden hangisi "kinetik enerji"nin dogru tanimidir?',
        ['A) Birikimis, depolanmis enerji',
         'B) Hareket halindeki bir nesnenin sahip oldugu enerji',
         'C) Kimyasal baglarin kirilmasiyla aciga cikan enerji',
         'D) Gunes isinlarinin yeryuzune ulastirdigi enerji'],
    ),
    (
        'Bir komur santralinde gerceklesen dogru enerji donusum sirasi hangisidir?',
        ['A) Elektrik → Isi → Kimyasal',
         'B) Kinetik → Potansiyel → Elektrik',
         'C) Kimyasal → Isi → Mekanik → Elektrik',
         'D) Isik → Kimyasal → Elektrik'],
    ),
    (
        'Yenilenebilir enerji kaynaklari icin afagidakilerden hangisi kesinlikle dogrudir?',
        ['A) Tum yenilenebilir kaynaklar her cografyada esit verimlidir',
         'B) Yenilenebilir kaynaklarin kurulum maliyeti sifirdir',
         'C) Dogada kendiliGinden yenilendikleri icin tukenme riski tasimazlar',
         'D) Yenilenebilir kaynaklar hicbir zaman kesintiye ugramaz'],
    ),
    (
        "Turkiye'nin hangi bolgesinde gunes enerjisi potansiyeli en yuksektir?",
        ['A) Karadeniz kiyilari',
         'B) Ic Anadolu platolari',
         "C) Dogu Karadeniz daglari",
         'D) Guney Anadolu ve Akdeniz kiyilari'],
    ),
    (
        'Kuresel isinmanin temel mekanizmasi afagidakilerden hangisinde dogru aciklanmistir?',
        ['A) Gunesin daha fazla enerji uretmesiyle yeryuzu isinir',
         'B) Atmosferdeki sera gazlari yeryuzunden yansayan isiyi tutar, sicaklik yukselir',
         'C) Ozon tabakasindaki delik UV isinlari artirir ve isinmaya neden olur',
         'D) Orman yanginlari atmosferi isitarak kuresel sicakligi arttirir'],
    ),
    (
        'Fosil yakitlar hakkinda afagidakilerden hangisi <b>yanlistir</b>?',
        ['A) Milyonlarca yilda organik maddelerin donusumuyle olusmuslardir',
         'B) Komur, petrol ve dogalgaz fosil yakit ornekleridir',
         'C) Yandiklarinda CO2 ve diger sera gazlari salarlar',
         'D) Jeotermal enerji de bir fosil yakit turudur'],
    ),
    (
        'Enerji verimliligi yuksek bir cihaz icin afagidakilerden hangisi dogrudir?',
        ['A) Cok fazla enerji uretir',
         'B) Ayni isi daha az enerji tuketerek yapar',
         'C) Yalnizca yenilenebilir enerji kaynaklariyla calisir',
         'D) Her zaman daha pahali ve buyuktur'],
    ),
    (
        'Yenilenebilir enerjiyle calisan bir urun tasarlarken <b>once</b> ne yapilmalidir?',
        ['A) Hemen malzeme listesi hazirlamak',
         'B) Tasarim problemini ve hedef kullaniciy tanimlamak',
         'C) Urunun fiyatini hesaplamak',
         'D) Mevcut en populer urunu kopyalamak'],
    ),
]

CEVAP_ANAHTARI = [
    (1, 'B', 'Kinetik enerji = hareket halindeki nesnenin enerjisi'),
    (2, 'C', 'Komur santralinde: Kimyasal → Isi → Mekanik → Elektrik'),
    (3, 'C', 'Yenilenebilir kaynaklar dogada kendiliGinden yenilenir, tukenme riski yoktur'),
    (4, 'D', "Turkiye'nin en yuksek gunes potansiyeli: Guney Anadolu ve Akdeniz kiyilari"),
    (5, 'B', 'Sera gazlari yansayan isiyi tutarak kuresel sicakligi arttirir'),
    (6, 'D', 'Jeotermal enerji yenilenebilir bir kaynaktir; fosil yakit degildir'),
    (7, 'B', 'Enerji verimliligi: ayni isi daha az enerji harcayarak yapma'),
    (8, 'B', 'Tasarim surecinde oncelik: problemi ve hedef kullaniciy tanimlamak'),
]


# Yardimci fonksiyonlar

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


# Sayfa 1: Sinav

def sinav_sayfa(E):
    E.append(make_student_info_header())
    E.append(vsp(0.1))
    E.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    E.append(vsp(0.15))

    E.append(Paragraph('7. Unite Sonu Sinavi — Enerjinin Donusumu ve Tasarim', S_BAS))
    E.append(Paragraph(
        '<b>Adi-Soyadi:</b> _________________________  '
        '<b>Sinif:</b> _______  <b>No:</b> _____  <b>Tarih:</b> _____________  '
        '<b>Sure:</b> 35 dk  <b>Puan:</b> 100',
        S_META,
    ))
    E.append(Paragraph(
        'Her sorunun yalnizca bir dogru cevabi vardir. '
        'Dogru secenegi daire icine alin. <b>(Her soru 10 puan)</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    E.append(Paragraph('COKTAN SECMELI  (8 soru x 10 puan = 80 puan)', S_BOLUM))
    E.append(vsp(0.1))
    E.append(mcq_tablo())
    E.append(vsp(0.15))

    E.append(Paragraph('KISA CEVAPLI  (2 soru x 10 puan = 20 puan)', S_BOLUM))
    E.append(vsp(0.1))

    q9 = KeepTogether([
        Paragraph(
            '9. Elektrik enerejisiyle calisan bir ampul yandifinda hangi enerji donusumleri '
            'gercekleSir? Bu surecte "kayip enerji" nereye gider? Kisa acikla.',
            S_KISA,
        ),
        WritingLines(3, line_spacing=14),
        vsp(0.1),
    ])
    E.append(q9)

    q10 = KeepTogether([
        Paragraph(
            '10. Yenilenebilir ve yenilenemez enerji kaynaklarinin temel farkini acikla; '
            'her birinden birer ornek ver.',
            S_KISA,
        ),
        WritingLines(3, line_spacing=14),
    ])
    E.append(q10)


# Sayfa 2: Cevap Anahtari

def ca_sayfa(E):
    E.append(Paragraph('OGretmen Icin — Cevap Anahtari', S_CA_BAS))
    E.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.0))
    E.append(vsp(0.3))

    E.append(Paragraph('Coktan Secmeli (her soru 10 puan)', S_CA_ALT))
    col_w = [1.3 * cm, 3.0 * cm, 12.7 * cm]
    hdr = [
        Paragraph('<b>Soru</b>', S_CA_HDR),
        Paragraph('<b>Cevap</b>', S_CA_HDR),
        Paragraph('<b>Aciklama</b>', S_CA_HDR),
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

    E.append(Paragraph('Kisa Cevapli Sorular — Beklenen Yanitlar', S_CA_ALT))
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Soru 9:</b> Elektrik → isik + isi. Kayip enerji (isi) cevreye yayilir; '
        'enerji kaybolmaz, donusur (enerjinin korunumu). '
        'Ampul uretilen isi enerjisi atmosfere aktarilir.',
        S_CA_KISA,
    ))
    E.append(Paragraph(
        '<b>Soru 10:</b> Yenilenebilir: dogada kendiliGinden yenilenir, tukenme riski yok '
        '(ornek: gunes, ruzgar). Yenilenemez: milyonlarca yilda olusmus, sinirli miktar '
        '(ornek: komur, petrol). Temel fark: yenilenme suresi ve tukenme riskidir.',
        S_CA_KISA,
    ))
    E.append(vsp(0.4))
    E.append(Paragraph(
        '<b>Not:</b> Kisa cevaplarda fikrin dogru oldugu ve mantikli aciklandigi '
        'surece tam puan verilebilir.',
        S_CA_NOT,
    ))


# Ana uretim fonksiyonu

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
