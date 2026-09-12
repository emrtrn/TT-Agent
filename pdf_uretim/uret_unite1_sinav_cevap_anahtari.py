"""
Unite1 -- Unite Sonu Sinavi (Cevap Anahtari)
YALNIZCA OGRETMEN KULLANIMI -- ogrencilere dagitilmaz.

100 puan:
  Bolum 1: 8 soru x 5 puan = 40 puan
  Bolum 2: 3 soru x 10 puan = 30 puan
  Bolum 3: Performans gorevi = 30 puan

Kullanim:
    python pdf_uretim/uret_unite1_sinav_cevap_anahtari.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, add_page_number,
    HorizontalLine,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import white, HexColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_OUTPUT = os.path.join(ROOT, 'units', 'unit1', 'U1_PDF_04_Degerlendirme_CA.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 1. Ünite'
DOC_TITLE  = '1. Ünite Sonu Sınavı — Cevap Anahtarı'
PAGE_W     = A4[0] - 4 * cm

COLOR_TEACHER = HexColor('#7C2D12')


# ── Stil sabitleri ───────────────────────────────────────────────

BOLUM_ST = ParagraphStyle(
    'CA1_BolumBaslik', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=8,
    backColor=COLOR_SECONDARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)

SORU_BASLIK_ST = ParagraphStyle(
    'CA1_SoruBaslik', fontName='TR-Bold', fontSize=9.5,
    textColor=COLOR_SECONDARY, leading=13, spaceAfter=4, spaceBefore=6,
)

BODY_ST = ParagraphStyle(
    'CA1_Body', fontName='TR-Regular', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3,
)

NOTE_ST = ParagraphStyle(
    'CA1_Not', fontName='TR-Italic', fontSize=8.5,
    textColor=COLOR_MUTED, leading=11, spaceAfter=3,
    leftIndent=8, rightIndent=8,
    backColor=COLOR_VERY_LIGHT, borderPadding=5,
)

TH_ST = ParagraphStyle(
    'CA1_TH', fontName='TR-Bold', fontSize=8.5,
    textColor=white, leading=11,
)

TD_ST = ParagraphStyle(
    'CA1_TD', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11,
)

TD_BOLD_ST = ParagraphStyle(
    'CA1_TDBold', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11,
)

CEVAP_ST = ParagraphStyle(
    'CA1_Cevap', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_SECONDARY, leading=11,
)

ALT_BASLIK_ST = ParagraphStyle(
    'CA1_AltBaslik', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11, spaceAfter=3, spaceBefore=4,
)


# ── Bölüm 1: MCQ cevap tablosu ───────────────────────────────────

CEVAPLAR = [
    ('1', 'B', "Graham Bell'in telefonu yapması",  'İcat / keşif ayrımı'),
    ('2', 'C', 'Akıllı fab., IoT, yapay zekâ',    'Endüstri 4.0'),
    ('3', 'B', 'Teknik (yol/yöntem)',              'Teknik kavramı'),
    ('4', 'B', 'Bir şehir parkı',                  'Mimari / çevre tasarımı'),
    ('5', 'C', 'Arts (Sanat)',                     'STEAM açılımı'),
    ('6', 'C', 'İnsan-makine iş birliği',          'Endüstri 5.0'),
    ('7', 'B', 'Kaynak belli mi, yazar kim?',      'Medya okuryazarlığı'),
    ('8', 'C', 'Birden fazla ölçüte bakmak',       'Değerlendirme ölçütleri'),
]


def bolum1_cevaplar():
    half = PAGE_W / 2 - 0.15 * cm

    def side_table(rows_data):
        col_w = [0.6*cm, 0.9*cm, half - 0.6*cm - 0.9*cm - 2.0*cm, 2.0*cm]
        hdr = [
            Paragraph('No', TH_ST), Paragraph('Cevap', TH_ST),
            Paragraph('Konu', TH_ST), Paragraph('Kazanım', TH_ST),
        ]
        tbl_data = [hdr]
        for no, cevap, konu, kazanim in rows_data:
            tbl_data.append([
                Paragraph(no, TD_ST),
                Paragraph(f'<b>{cevap})</b>', CEVAP_ST),
                Paragraph(konu, TD_ST),
                Paragraph(kazanim, TD_ST),
            ])
        t = Table(tbl_data, colWidths=col_w, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND',    (0, 0), (-1, 0), COLOR_SECONDARY),
            ('TOPPADDING',    (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING',   (0, 0), (-1, -1), 5),
            ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
            ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN',         (0, 0), (1, -1),  'CENTER'),
            ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
            ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
        ]))
        return t

    left  = side_table(CEVAPLAR[:4])
    right = side_table(CEVAPLAR[4:])

    outer = Table([[left, right]], colWidths=[half + 0.15*cm, half + 0.15*cm])
    outer.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
    ]))
    return outer


# ── Bölüm 2: Puanlama kılavuzu ────────────────────────────────────

def _puan_tablosu(kriterler):
    """Genel amaçlı puan kriteri tablosu: [(puan, açıklama), ...]"""
    data = [[Paragraph('Puan', TH_ST), Paragraph('Değerlendirme kriteri', TH_ST)]]
    for puan, aciklama in kriterler:
        data.append([Paragraph(str(puan), CEVAP_ST), Paragraph(aciklama, TD_ST)])
    t = Table(data, colWidths=[1.4*cm, PAGE_W - 1.4*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('ALIGN',         (0, 0), (0, -1),  'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    return t


def soru9_kilavuz():
    items = []
    items.append(Paragraph('Soru 9 — İcat ve Keşif Farkı  (10 puan)', SORU_BASLIK_ST))
    items.append(Paragraph(
        'Beklenen: İcat = daha önce olmayan bir ürün/cihaz yapmak (örn: Bell – telefon). '
        'Keşif = zaten var olan bir şeyi ilk kez fark etmek (örn: Kolomb – Amerika).',
        NOTE_ST,
    ))
    items.append(_puan_tablosu([
        (10, 'Fark kavramsal olarak doğru açıklanmış <b>ve</b> her iki kavram için '
             'somut, doğru örnek verilmiş.'),
        (7,  'Fark açıklanmış, örneklerden biri doğru veya yüzeysel.'),
        (4,  'Fark belirtilmiş ancak örneksiz; ya da örnekler var ama fark açıklanmamış.'),
        (0,  'Yanlış, ilgisiz veya boş.'),
    ]))
    return items


def soru10_kilavuz():
    items = []
    items.append(Paragraph(
        'Soru 10 — Teknoloji ile Tasarım İlişkisi  (10 puan)', SORU_BASLIK_ST))
    items.append(Paragraph(
        'Beklenen: Teknoloji ve tasarım birbirini tamamlar. Teknoloji "nasıl çalışır"ı '
        '(işlevsellik), tasarım "nasıl görünür ve kullanılır"ı (estetik, ergonomi) çözer. '
        'Örnek: Akıllı telefon — işlemcisi teknoloji, ekran yerleşimi ve rengi tasarım.',
        NOTE_ST,
    ))
    items.append(_puan_tablosu([
        (10, 'Teknoloji-tasarım bağlantısı net biçimde açıklanmış <b>ve</b> '
             'somut, uygun bir günlük yaşam örneği verilmiş.'),
        (6,  'Bağlantı açıklanmış ancak örnek eksik veya yüzeysel; ya da '
             'örnek var bağlantı açıklanmamış.'),
        (3,  'Konuya değinilmiş ama kavramsal bütünlük yok.'),
        (0,  'Yanlış, ilgisiz veya boş.'),
    ]))
    return items


def soru11_kilavuz():
    items = []
    items.append(Paragraph(
        'Soru 11 — Yapay Zekâ Uygulamaları  (10 puan)', SORU_BASLIK_ST))
    items.append(Paragraph(
        'Her doğru uygulama + açıklama çifti: <b>3-4 puan</b>. '
        'Toplam 3 çift = 10 puan (serbest dağılım, 10\'u geçmez).',
        NOTE_ST,
    ))

    ornek_data = [
        [Paragraph('Kabul edilebilir örnekler', TH_ST)],
        [Paragraph(
            'Siri / Bixby / Google Asistan (sesli asistanlar) — '
            'Netflix / YouTube / Spotify önerileri — '
            'ChatGPT, Gemini vb. (sohbet botları) — '
            'Google Translate (otomatik çeviri) — '
            'Yüz tanıma ile telefon açma — '
            'Spam filtreleri — Otonom araçlar',
            TD_ST,
        )],
    ]
    t = Table(ornek_data, colWidths=[PAGE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ]))
    items.append(t)
    return items


# ── Bölüm 3: Performans görevi kılavuzu ──────────────────────────

def soru12_kilavuz():
    items = []
    items.append(Paragraph(
        'Soru 12 — Akıllı Saat / Geleneksel Kol Saati Karşılaştırması  (30 puan)',
        SORU_BASLIK_ST,
    ))

    # Alt bölüm: Tablo puanı
    items.append(Paragraph('Tablo doldurma  (8 hücre × 2 puan = 16 puan)', ALT_BASLIK_ST))

    tablo_data = [
        [Paragraph('Özellik', TH_ST),
         Paragraph('Akıllı Saat — beklenen cevap', TH_ST),
         Paragraph('Geleneksel Kol Saati — beklenen cevap', TH_ST)],
        [Paragraph('Hangi tasarım türü?', TD_ST),
         Paragraph('Endüstriyel tasarım + yazılım tasarımı', TD_ST),
         Paragraph('Endüstriyel tasarım', TD_ST)],
        [Paragraph('Hangi teknoloji kullanıyor?', TD_ST),
         Paragraph('Sensörler, batarya, yazılım, bluetooth/wifi', TD_ST),
         Paragraph('Mekanik / pil, saat motoru', TD_ST)],
        [Paragraph('Kullanıcıya faydası?', TD_ST),
         Paragraph('Sağlık takibi, bildirimler, navigasyon, çoklu işlev', TD_ST),
         Paragraph('Saat okuma, estetik değer, uzun pil ömrü', TD_ST)],
        [Paragraph('Olumsuz yanı (varsa)?', TD_ST),
         Paragraph('Kısa pil ömrü, bağımlılık, gizlilik, yüksek maliyet', TD_ST),
         Paragraph('Çoklu işlev yok, teknoloji uyumsuzluğu', TD_ST)],
    ]
    col_oz = PAGE_W * 0.28
    col_ak = PAGE_W * 0.36
    col_gn = PAGE_W * 0.36
    tbl = Table(tablo_data, colWidths=[col_oz, col_ak, col_gn])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    items.append(tbl)
    items.append(Spacer(1, 6))

    # Alt bölüm: Yorum + özgünlük puanı
    items.append(Paragraph('Yorum ve gerekçe + özgünlük  (14 puan)', ALT_BASLIK_ST))
    items.append(Paragraph(
        'Öğrenci bir görüş oluşturmalı ve gerekçelendirmeli. '
        '"Daha iyi" ifadesi kullanıma bağlıdır — bu farkındalığı göstermesi puanı artırır.',
        NOTE_ST,
    ))
    items.append(_puan_tablosu([
        (14, 'Net bir tercih belirtilmiş, <b>kullanım bağlamına uygun</b> gerekçe yazılmış '
             've eleştirel/özgün bir bakış açısı sergilenmiş.'),
        (10, 'Tercih net, gerekçe var ama yüzeysel; özgünlük sınırlı.'),
        (6,  'Tercih var, gerekçe yetersiz veya yalnızca tabloyu tekrar ediyor.'),
        (2,  'Çok kısa, gerekçesiz ya da sadece "daha güzel" düzeyinde.'),
        (0,  'Boş veya tamamen ilgisiz.'),
    ]))

    return items


# ── Genel puanlama + notlar ───────────────────────────────────────

def genel_puanlama():
    items = []

    items.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    items.append(Spacer(1, 5))

    perf_col = (PAGE_W - 0.3*cm) / 2

    # Sol: Sınıf performans düzeyi
    perf_data = [
        [Paragraph('Sınıf Performans Düzeyi', TH_ST),
         Paragraph('Toplam Puan', TH_ST)],
        [Paragraph('Üstün',          TD_ST), Paragraph('90 – 100', TD_ST)],
        [Paragraph('Yeterli',        TD_ST), Paragraph('70 – 89',  TD_ST)],
        [Paragraph('Gelişiyor',      TD_ST), Paragraph('50 – 69',  TD_ST)],
        [Paragraph('Destek Gerekli', TD_ST), Paragraph('0 – 49',   TD_ST)],
    ]
    perf_t = Table(perf_data, colWidths=[perf_col - 2.2*cm, 2.2*cm])
    perf_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN',         (-1, 0), (-1, -1), 'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))

    # Sağ: Bölüm dağılımı
    bolum_data = [
        [Paragraph('Bölüm', TH_ST),
         Paragraph('İçerik', TH_ST),
         Paragraph('Maks', TH_ST)],
        [Paragraph('1', TD_ST), Paragraph('Çoktan Seçmeli (8 soru)', TD_ST), Paragraph('40', TD_BOLD_ST)],
        [Paragraph('2', TD_ST), Paragraph('Kısa Cevaplı (9–11)',      TD_ST), Paragraph('30', TD_BOLD_ST)],
        [Paragraph('3', TD_ST), Paragraph('Performans Görevi (12)',   TD_ST), Paragraph('30', TD_BOLD_ST)],
        [Paragraph('',  TD_ST), Paragraph('<b>TOPLAM</b>',           TD_BOLD_ST), Paragraph('<b>100</b>', TD_BOLD_ST)],
    ]
    bolum_t = Table(bolum_data, colWidths=[1.2*cm, perf_col - 1.2*cm - 1.8*cm, 1.8*cm])
    bolum_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN',         (-1, 0), (-1, -1), 'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
        ('LINEABOVE',     (0, -1), (-1, -1), 0.8, COLOR_SECONDARY),
    ]))

    outer = Table(
        [[perf_t, bolum_t]],
        colWidths=[perf_col + 0.15*cm, perf_col + 0.15*cm],
    )
    outer.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
    ]))
    items.append(outer)
    items.append(Spacer(1, 8))

    # Değerlendirme notları
    items.append(Paragraph('Değerlendirme Notları', ALT_BASLIK_ST))
    notlar = [
        'Yanlış cevabı değil, <b>zayıf düşünmeyi</b> cezalandırın. Mantıksal çıkarım yapabilen öğrenciye kısmi puan verilebilir.',
        '<b>Özgün örneklere</b> prim verin. Anahtardaki örnekler dışında da makul cevaplar tam puan alabilir.',
        'Soru 12\'de <b>"Daha güzel"</b> ya da <b>"Daha kullanışlı"</b> gibi basit cevaplar değil; gerekçelendirilmiş görüş puan alır.',
    ]
    for not_metin in notlar:
        items.append(Paragraph(f'• {not_metin}', BODY_ST))

    return items


# ── Ana üretim fonksiyonu ────────────────────────────────────────

def build(output_path=None):
    out = output_path or _DEFAULT_OUTPUT
    doc = create_doc(out, title=DOC_TITLE, unite_info=UNITE_INFO)
    elems = []

    # Öğretmen uyarı bandı
    uyari_st = ParagraphStyle(
        'CA1_Uyari', fontName='TR-Bold', fontSize=10,
        textColor=white, leading=14, alignment=TA_CENTER,
        backColor=COLOR_TEACHER, leftIndent=-6, rightIndent=-6,
        borderPadding=(4, 6, 4, 6), spaceAfter=6,
    )
    elems.append(Paragraph(
        'YALNIZCA ÖĞRETMEN KULLANIMI — Öğrencilere Dağıtılmaz', uyari_st))

    title_st = ParagraphStyle(
        'CA1_Title', fontName='TR-Bold', fontSize=14,
        textColor=COLOR_PRIMARY, leading=18, spaceAfter=2,
    )
    sub_st = ParagraphStyle(
        'CA1_Sub', fontName='TR-Regular', fontSize=9,
        textColor=COLOR_MUTED, leading=12, spaceAfter=6,
    )
    elems.append(Paragraph(
        '1. Ünite Sonu Sınavı — Cevap Anahtarı', title_st))
    elems.append(Paragraph(
        'Teknoloji ve Tasarım Öğreniyorum  •  Toplam: 100 puan  '
        '(Bölüm 1: 40p  |  Bölüm 2: 30p  |  Bölüm 3: 30p)', sub_st))
    elems.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elems.append(Spacer(1, 6))

    # BÖLÜM 1
    elems.append(Paragraph(
        'BÖLÜM 1: ÇOKTAN SEÇMELİ  (8 soru × 5 puan = 40 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))
    elems.append(bolum1_cevaplar())
    elems.append(Spacer(1, 8))

    # BÖLÜM 2
    elems.append(Paragraph(
        'BÖLÜM 2: KISA CEVAPLI  (3 soru × 10 puan = 30 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))

    for el in soru9_kilavuz():
        elems.append(el)
    elems.append(Spacer(1, 5))

    for el in soru10_kilavuz():
        elems.append(el)
    elems.append(Spacer(1, 5))

    for el in soru11_kilavuz():
        elems.append(el)
    elems.append(Spacer(1, 8))

    # BÖLÜM 3
    elems.append(Paragraph(
        'BÖLÜM 3: PERFORMANS GÖREVİ  (30 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))

    for el in soru12_kilavuz():
        elems.append(el)
    elems.append(Spacer(1, 8))

    # Genel puanlama + notlar
    for el in genel_puanlama():
        elems.append(el)

    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
