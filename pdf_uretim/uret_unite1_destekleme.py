# -*- coding: utf-8 -*-
"""
1. Unite - Destekleme Paketi (Kombine)
Calistirir: python pdf_uretim/uret_unite1_destekleme.py

Uretilen PDF: units/7_sinif/unit1/U1_Destekleme_Paketi_Kombine.pdf
- Kapak sayfasi YOK
- 2 etkinlik, her biri bir sayfada
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable,
)
from pdf_style import (
    register_fonts, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines,
)

register_fonts()

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, 'units', 'unit1')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U1_Destekleme_Paketi_Kombine.pdf')
UI    = 'Teknoloji ve Tasarım - 7. Sınıf - 1. Ünite: Destekleme Paketi'

# ============================================================
# STİLLER — çok kompakt
# ============================================================

S_ETK   = ParagraphStyle('d_ETK',  fontName='TR-Bold',    fontSize=11, textColor=white,
                          leading=14, alignment=TA_LEFT,
                          backColor=COLOR_PRIMARY, borderPad=5,
                          spaceBefore=0, spaceAfter=4)
S_META  = ParagraphStyle('d_META', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=3)
S_BSL   = ParagraphStyle('d_BSL',  fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceBefore=4, spaceAfter=2)
S_GOV   = ParagraphStyle('d_GOV',  fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=3, alignment=TA_JUSTIFY,
                          backColor=COLOR_VERY_LIGHT, leftIndent=5, rightIndent=5,
                          borderPad=4)
S_BODY  = ParagraphStyle('d_BODY', fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=2, alignment=TA_JUSTIFY)
S_NOTE  = ParagraphStyle('d_NOTE', fontName='TR-Italic',  fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=2)
S_LABEL = ParagraphStyle('d_LBL',  fontName='TR-Bold',    fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1)
S_KAV   = ParagraphStyle('d_KAV',  fontName='TR-Bold',    fontSize=8, textColor=white,
                          leading=11, alignment=TA_LEFT,
                          backColor=COLOR_SECONDARY, borderPad=3,
                          spaceBefore=4, spaceAfter=2)


def vsp(h=0.15):
    return Spacer(1, h * cm)


def hr(color=COLOR_LIGHT_GREY, thickness=0.4):
    return HRFlowable(width='100%', thickness=thickness, color=color, spaceAfter=3, spaceBefore=3)


def etkinlik_baslik(no, baslik, tur=None, sure=None):
    blok = []
    blok.append(Paragraph(f'ETKİNLİK {no}: {baslik}', S_ETK))
    meta_parts = []
    if tur:
        meta_parts.append(f'Tür: {tur}')
    if sure:
        meta_parts.append(f'Süre: {sure}')
    if meta_parts:
        blok.append(Paragraph('  |  '.join(meta_parts), S_META))
    return blok


def ad_tarih():
    """Ad Soyad + Tarih tek satırda"""
    data = [[
        Paragraph('Ad Soyad: ____________________________', S_LABEL),
        Paragraph('Tarih: ________________', S_LABEL),
    ]]
    t = Table(data, colWidths=[11 * cm, 6 * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
    ]))
    return t


# ============================================================
# ETKİNLİK 1: ADIM ADIM TANIM ŞABLONU
# ============================================================

def etkinlik1():
    e = []
    e += etkinlik_baslik(1, 'ADIM ADIM TANIM ŞABLONU', tur='Yapılandırılmış Yazma', sure='20 dk')
    e.append(Paragraph(
        'Kavramları kendi cümlelerinle tanımlamak için aşağıdaki boşlukları doldur.',
        S_GOV))
    e.append(vsp(0.1))
    e.append(ad_tarih())
    e.append(vsp(0.1))

    # KAVRAM 1: BULUŞ
    e.append(Paragraph('KAVRAM 1: BULUŞ', S_KAV))
    e.append(Paragraph(
        'Buluş, <u>_________________</u> (yeni bir fikir / eski bir şey / bir cihaz) bulmaktır.',
        S_BODY))
    e.append(Paragraph(
        'Örnek: <u>_________________</u> buluş yapmıştır.  |  Ne buldu? <u>__________________________________</u>',
        S_BODY))

    # KAVRAM 2: İCAT
    e.append(Paragraph('KAVRAM 2: İCAT', S_KAV))
    e.append(Paragraph(
        'İcat, <u>_________________</u> (daha önce olmayan / doğada olan / ucuz olan) bir ürünü ilk kez yapmaktır.',
        S_BODY))
    e.append(Paragraph(
        'Graham Bell <u>_________________</u> icat etmiştir.  |  Bu icat olmadan hayatımız: <u>____________________</u>',
        S_BODY))

    # KAVRAM 3: KEŞİF
    e.append(Paragraph('KAVRAM 3: KEŞİF', S_KAV))
    e.append(Paragraph(
        'Keşif, <u>_________________</u> (zaten var olan / yeni yapılan / fabrika ürünü) bir şeyi ilk kez fark etmektir.',
        S_BODY))
    e.append(Paragraph(
        'Kolomb <u>_________________</u> keşfetmiştir.  |  Keşif ≠ İcat, çünkü: <u>_____________________________</u>',
        S_BODY))

    # KAVRAM 4: TEKNOLOJİ
    e.append(Paragraph('KAVRAM 4: TEKNOLOJİ', S_KAV))
    e.append(Paragraph(
        '1. Teknoloji, <u>_________________</u> (bilim + teknik / sadece bilgisayar / sadece internet).',
        S_BODY))
    e.append(Paragraph(
        '2. Teknoloji, insanın <u>_________________</u> (ihtiyacını / dileğini / korkusunu) karşılar.',
        S_BODY))
    e.append(Paragraph(
        '3. Bir kalem bile teknoloji ürünüdür.  →  Doğru  /  Yanlış  (doğru olanı daire içine al)',
        S_BODY))

    # KAVRAM 5: TASARIM
    e.append(Paragraph('KAVRAM 5: TASARIM', S_KAV))
    e.append(Paragraph(
        'Tasarım, bir ürünü <u>_______________________________________________________________</u> yapmaktır.',
        S_BODY))
    e.append(Paragraph('(İpucu: hem güzel, hem kullanışlı, hem de planlı)', S_NOTE))

    e.append(hr())
    e.append(Paragraph('Şimdi bu 3 kavramı kendi sözcüklerinle tanımla (1 cümle yeter):', S_BSL))
    e.append(Paragraph(
        'STEAM: <u>____________________________________________________________________________</u>',
        S_BODY))
    e.append(Paragraph(
        'Yapay Zekâ: <u>________________________________________________________________________</u>',
        S_BODY))
    e.append(Paragraph(
        'Endüstri 4.0: <u>______________________________________________________________________</u>',
        S_BODY))

    return e


# ============================================================
# ETKİNLİK 2: ÖRNEK CEVAPLI KÂĞITLAR
# ============================================================

def etkinlik2():
    e = []
    e += etkinlik_baslik(2, 'ÖRNEK CEVAPLI KÂĞITLAR', tur='Rehberli Yazma', sure='20 dk')
    e.append(Paragraph('Önce örnek yazıyı oku, sonra sen kendi yazını yaz.', S_GOV))
    e.append(vsp(0.06))

    e.append(Paragraph('ÖRNEK YAZI: "Gözlüğümü Taktım"', S_BSL))
    ornek = (
        'Geçen hafta okuldan eve dönerken çevreme daha dikkatli bakmaya başladım. '
        'Otobüste oturduğum koltuk bir <b>tasarım</b> ürünüydü — birisi planlamıştı. '
        'Telefonumu çıkardım, Google Maps açıktı; içindeki yapay zekâ ise <b>teknoloji</b>. '
        'Eve gelince buzdolabımı açtım — ilk buzdolabı bir <b>icattı</b>, artık evlere girmiş bir teknoloji. '
        'Akşam haberlerde TOGG fabrikasını gösterdiler: robotlar ve insanlar yan yana — bu <b>Endüstri 5.0</b>. '
        'Bu ünite sayesinde gördüm ki teknoloji ve tasarım hayatımızın her yerinde. '
        'Ben de büyüyünce belki bir gün bir şey tasarlayıp icat edeceğim.'
    )
    e.append(Paragraph(ornek, S_BODY))
    e.append(vsp(0.08))

    e.append(hr())
    e.append(Paragraph('ŞİMDİ SENİN YAZIN', S_BSL))
    e.append(Paragraph('Başlığını seç veya kendin yaz:', S_LABEL))

    baslik_data = [[
        Paragraph('"Gözlüğümü Taktım"', S_BODY),
        Paragraph('"Yeni Bir Gözle Evim"', S_BODY),
        Paragraph('"Çevremdeki Dünya"', S_BODY),
        Paragraph('Başka: ____________', S_BODY),
    ]]
    bt = Table(baslik_data, colWidths=[4.25 * cm, 4.25 * cm, 4.25 * cm, 4.25 * cm])
    bt.setStyle(TableStyle([
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('BACKGROUND',    (0, 0), (-1, -1), COLOR_VERY_LIGHT),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ]))
    e.append(bt)
    e.append(vsp(0.06))

    e.append(Paragraph(
        '<i>Kullanabileceğin kavramlar: buluş, icat, keşif, bilim, teknik, tasarım, teknoloji, '
        'endüstri, STEAM, Endüstri 4.0, Endüstri 5.0, yapay zekâ</i>',
        S_NOTE))
    e.append(Paragraph(
        '<i>Yardımcı cümleler: "Geçen hafta fark ettim ki…" — "Odamdaki ___ aslında bir ___ örneği." — '
        '"Ben de büyüyünce…"</i>',
        S_NOTE))
    e.append(vsp(0.05))

    e.append(Paragraph('Başlık: ___________________________________', S_LABEL))
    e.append(WritingLines(7, line_spacing=20))
    e.append(vsp(0.1))
    e.append(ad_tarih())

    return e


# ============================================================
# ANA BLOK
# ============================================================

def main():
    doc = SimpleDocTemplate(
        CIKTI,
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.8 * cm, bottomMargin=1.8 * cm,
        title='1. Ünite - Destekleme Paketi',
    )
    doc.unite_info = UI

    story = []
    story += etkinlik1()
    story.append(PageBreak())
    story += etkinlik2()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print('OK  U1_Destekleme_Paketi_Kombine.pdf  (2 sayfa)')


if __name__ == '__main__':
    main()
