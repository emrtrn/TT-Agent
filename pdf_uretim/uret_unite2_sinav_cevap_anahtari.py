"""
Unite2 — Ünite Sonu Sınavı (Cevap Anahtarı)
YALNIZCA ÖĞRETMEN KULLANIMI — öğrencilere dağıtılmaz.

20 puan sistemine göre düzenlenmiştir:
  Bölüm 1: 8 soru × 1 puan = 8 puan
  Bölüm 2: 5 madde × 2 puan + 1 soru × 2 puan = 12 puan

Kullanım:
    python pdf_uretim/uret_unite2_sinav_cevap_anahtari.py
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
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import white, HexColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_OUTPUT = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Sinav_Cevap_Anahtari.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite'
DOC_TITLE  = '2. Ünite Sonu Sınavı — Cevap Anahtarı'
PAGE_W     = A4[0] - 4 * cm

COLOR_TEACHER = HexColor('#7C2D12')   # Koyu kırmızı-kahve (öğretmen belgeleri için)

# ── Stil sabitleri ───────────────────────────────────────────────

BOLUM_ST = ParagraphStyle(
    'CA_BolumBaslik', fontName='TR-Bold', fontSize=9.5,
    textColor=white, leading=14, spaceAfter=4, spaceBefore=8,
    backColor=COLOR_SECONDARY, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)

SORU_BASLIK_ST = ParagraphStyle(
    'CA_SoruBaslik', fontName='TR-Bold', fontSize=9.5,
    textColor=COLOR_SECONDARY, leading=13, spaceAfter=4, spaceBefore=6,
)

BODY_ST = ParagraphStyle(
    'CA_Body', fontName='TR-Regular', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3,
)

NOTE_ST = ParagraphStyle(
    'CA_Not', fontName='TR-Italic', fontSize=8.5,
    textColor=COLOR_MUTED, leading=11, spaceAfter=3,
    leftIndent=8, rightIndent=8,
    backColor=COLOR_VERY_LIGHT, borderPadding=5,
)

TH_ST = ParagraphStyle(
    'CA_TH', fontName='TR-Bold', fontSize=8.5,
    textColor=white, leading=11,
)

TD_ST = ParagraphStyle(
    'CA_TD', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11,
)

TD_BOLD_ST = ParagraphStyle(
    'CA_TDBold', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11,
)

CEVAP_ST = ParagraphStyle(
    'CA_Cevap', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_SECONDARY, leading=11,
)


# ── Bölüm 1: Cevap tablosu (2 sütun, 4 satır) ────────────────────

def bolum1_cevaplar():
    """8 MCQ cevabını 2 sütunlu kompakt tabloda göster."""

    CEVAPLAR = [
        ('1', 'C', 'Mekân (Uzam)',             'TT.7.2.1.a'),
        ('2', 'D', 'Zıtlık',                   'TT.7.2.1.b'),
        ('3', 'B', 'Bağlamı koruyarak aktarma', 'TT.7.2.2'),
        ('4', 'C', 'Ritim',                    'TT.7.2.1.b'),
        ('5', 'B', 'Konuyu/kavramı belirleme', 'TT.7.2.3'),
        ('6', 'B', 'Rengin açık-koyu değeri',  'TT.7.2.1.a'),
        ('7', 'C', 'Fikri görselleştirmek',    'TT.7.2.4.a'),
        ('8', 'B', 'Simetrik denge',           'TT.7.2.1.b'),
    ]

    half = PAGE_W / 2 - 0.15 * cm

    def side_table(rows_data):
        col_w = [0.7*cm, 0.9*cm, half - 0.7*cm - 0.9*cm - 1.7*cm, 1.7*cm]
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

def soru9_kilavuz():
    items = []

    items.append(Paragraph(
        'Soru 9 — Görsel Analiz  (5 madde × 2 puan = 10 puan)', SORU_BASLIK_ST))

    items.append(Paragraph(
        'Öğretmen notu: Akıllı tahtada ilgili görsel gösterilir. '
        'Önerilen görseller: <b>İznik çinisi</b> veya <b>Bauhaus afişi.</b> '
        'Farklı bir görsel de kullanılabilir; puanlama aşağıdaki kritere göredir.',
        NOTE_ST,
    ))

    # Puanlama kriteri satırları
    kriter_data = [
        [Paragraph('Her madde için puan kriteri', TH_ST),
         Paragraph('Puan', TH_ST)],
        [Paragraph('Eleman/ilke adı doğru ve açıklaması makul', TD_ST),
         Paragraph('2', TD_BOLD_ST)],
        [Paragraph('Eleman/ilke adı doğru, açıklama yok veya yüzeysel', TD_ST),
         Paragraph('1', TD_BOLD_ST)],
        [Paragraph('Yanlış veya boş', TD_ST),
         Paragraph('0', TD_BOLD_ST)],
    ]
    kriter_t = Table(kriter_data, colWidths=[PAGE_W - 1.8*cm, 1.8*cm])
    kriter_t.setStyle(TableStyle([
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
    items.append(kriter_t)
    items.append(Spacer(1, 4))

    # Örnek kabul edilebilir cevaplar
    ornek_data = [
        [Paragraph('', TH_ST),
         Paragraph('Örnek Elemanlar', TH_ST),
         Paragraph('Örnek İlkeler', TH_ST)],
        [Paragraph('<b>İznik çinisi</b>', TD_ST),
         Paragraph('Çizgi, Renk, Şekil', TD_ST),
         Paragraph('Ritim, Denge', TD_ST)],
        [Paragraph('<b>Bauhaus afişi</b>', TD_ST),
         Paragraph('Şekil, Renk, Çizgi', TD_ST),
         Paragraph('Denge, Vurgu', TD_ST)],
    ]
    col3 = [2.5*cm, (PAGE_W - 2.5*cm) / 2, (PAGE_W - 2.5*cm) / 2]
    ornek_t = Table(ornek_data, colWidths=col3)
    ornek_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    items.append(Paragraph(
        'Kabul edilebilir cevap örnekleri (makul her gözlem puanlanabilir):',
        ParagraphStyle('CA_AltBaslik', fontName='TR-Bold', fontSize=8,
                       textColor=COLOR_TEXT, leading=11, spaceAfter=2),
    ))
    items.append(ornek_t)

    return items


def soru10_kilavuz():
    items = []

    items.append(Paragraph(
        'Soru 10 — Yorumlamak / Kopyalamak  (2 puan)', SORU_BASLIK_ST))

    puan_data = [
        [Paragraph('Puan', TH_ST),
         Paragraph('Değerlendirme kriteri', TH_ST)],
        [Paragraph('2', CEVAP_ST),
         Paragraph(
             'Fark kavramsal olarak açıklanmış <b>ve</b> somut bir tasarım örneği verilmiş. '
             'Beklenen özet: Yorumlamak = orijinalin içeriğini/üslubunu koruyarak kendi '
             'ifadesiyle yeniden aktarmak; Kopyalamak = birebir aynısını üretmek.',
             TD_ST)],
        [Paragraph('1', TD_ST),
         Paragraph(
             'Fark belirtilmiş ancak somut örnek yok; ya da örnek var, fark açıklanmamış.',
             TD_ST)],
        [Paragraph('0', TD_ST),
         Paragraph(
             'Yalnızca "aynı değiller" gibi yüzeysel cevap, yanlış veya boş.',
             TD_ST)],
    ]
    col_p = [1.4*cm, PAGE_W - 1.4*cm]
    puan_t = Table(puan_data, colWidths=col_p)
    puan_t.setStyle(TableStyle([
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
    items.append(puan_t)

    return items


# ── Performans düzeyi + Kazanım dağılımı ─────────────────────────

def alt_tablolar():
    items = []

    perf_col = (PAGE_W - 0.3*cm) / 2

    # Sol: Performans düzeyi
    perf_data = [
        [Paragraph('Sınıf Performans Düzeyi', TH_ST),
         Paragraph('Toplam Puan', TH_ST)],
        [Paragraph('Üstün',            TD_ST), Paragraph('18 – 20', TD_ST)],
        [Paragraph('Yeterli',          TD_ST), Paragraph('14 – 17', TD_ST)],
        [Paragraph('Gelişiyor',        TD_ST), Paragraph('10 – 13', TD_ST)],
        [Paragraph('Destek Gerekli',   TD_ST), Paragraph('0 – 9',   TD_ST)],
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

    # Sağ: Kazanım dağılımı
    kaz_data = [
        [Paragraph('Kazanım',  TH_ST),
         Paragraph('Sorular',  TH_ST),
         Paragraph('Max (p)',  TH_ST)],
        [Paragraph('TT.7.2.1', TD_ST),
         Paragraph('1, 2, 4, 6, 8, 9', TD_ST),
         Paragraph('15', TD_ST)],
        [Paragraph('TT.7.2.2', TD_ST),
         Paragraph('3, 10',    TD_ST),
         Paragraph('3',  TD_ST)],
        [Paragraph('TT.7.2.3', TD_ST),
         Paragraph('5',        TD_ST),
         Paragraph('1',  TD_ST)],
        [Paragraph('TT.7.2.4', TD_ST),
         Paragraph('7',        TD_ST),
         Paragraph('1',  TD_ST)],
    ]
    kaz_t = Table(kaz_data, colWidths=[2.0*cm, perf_col - 2.0*cm - 1.5*cm, 1.5*cm])
    kaz_t.setStyle(TableStyle([
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

    outer = Table(
        [[perf_t, kaz_t]],
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
    return items


# ── Ana üretim fonksiyonu ────────────────────────────────────────

def build(output_path=None):
    out = output_path or _DEFAULT_OUTPUT
    doc = create_doc(out, title=DOC_TITLE, unite_info=UNITE_INFO)
    elems = []

    # ── Başlık bandı (öğretmen uyarısı) ──
    uyari_st = ParagraphStyle(
        'CA_Uyari', fontName='TR-Bold', fontSize=10,
        textColor=white, leading=14, alignment=TA_CENTER,
        backColor=COLOR_TEACHER, leftIndent=-6, rightIndent=-6,
        borderPadding=(4, 6, 4, 6), spaceAfter=6,
    )
    elems.append(Paragraph(
        'YALNIZCA ÖĞRETMEN KULLANIMI — Öğrencilere Dağıtılmaz', uyari_st))

    title_st = ParagraphStyle(
        'CA_Title', fontName='TR-Bold', fontSize=14,
        textColor=COLOR_PRIMARY, leading=18, spaceAfter=2,
    )
    sub_st = ParagraphStyle(
        'CA_Sub', fontName='TR-Regular', fontSize=9,
        textColor=COLOR_MUTED, leading=12, spaceAfter=6,
    )
    elems.append(Paragraph('2. Ünite Sonu Sınavı — Cevap Anahtarı', title_st))
    elems.append(Paragraph(
        'Temel Tasarım  •  Toplam: 20 puan  '
        '(Bölüm 1: 8p  |  Bölüm 2: 12p)', sub_st))
    elems.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elems.append(Spacer(1, 6))

    # ── BÖLÜM 1 ──
    elems.append(Paragraph(
        'BÖLÜM 1: ÇOKTAN SEÇMELİ  (8 soru × 1 puan = 8 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))
    elems.append(bolum1_cevaplar())
    elems.append(Spacer(1, 8))

    # ── BÖLÜM 2 ──
    elems.append(Paragraph(
        'BÖLÜM 2: KISA CEVAPLI  (12 puan)', BOLUM_ST))
    elems.append(Spacer(1, 4))

    for el in soru9_kilavuz():
        elems.append(el)
    elems.append(Spacer(1, 6))

    for el in soru10_kilavuz():
        elems.append(el)
    elems.append(Spacer(1, 8))

    # ── Alt tablolar ──
    elems.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elems.append(Spacer(1, 5))
    for el in alt_tablolar():
        elems.append(el)

    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
