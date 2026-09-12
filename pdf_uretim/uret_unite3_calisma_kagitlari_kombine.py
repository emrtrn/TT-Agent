# -*- coding: utf-8 -*-
"""
3. Unite - Calisma Kagitlari (Kombine, tek PDF)
Calistirir: python pdf_uretim/uret_unite3_calisma_kagitlari_kombine.py
Uretilen PDF: units/7_sinif/unit3/U3_PDF_03_Calisma_Kagitlari.pdf
- Kapak sayfasi YOK
- 11 calisma kagidi (CK8 iki sayfa), her biri bir sayfada baslar
- Baslik formati: "Calisma Kagidi N - Baslik" (Unit 1/2 uyumlu, beyaz metin, turuncu arka plan)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak,
)
from pdf_style import (
    register_fonts, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, DrawingBox,
)

register_fonts()

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, 'units', 'unit3')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI     = os.path.join(PDF_DIR, 'U3_PDF_03_Calisma_Kagitlari.pdf')
UNITE_ADI = 'Teknoloji ve Tasarım — 7. Sınıf — 3. Ünite: Tasarım Odaklı Süreç'

# ============================================================
# STİLLER
# ============================================================

S_CK    = ParagraphStyle('ck3_CK',   fontName='TR-Bold',    fontSize=10.5, textColor=white,
                          leading=13, alignment=TA_LEFT,
                          backColor=COLOR_PRIMARY, borderPad=5,
                          spaceBefore=0, spaceAfter=3)
S_META  = ParagraphStyle('ck3_META', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=3)
S_ADIM  = ParagraphStyle('ck3_ADIM', fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceBefore=4, spaceAfter=2)
S_GOV   = ParagraphStyle('ck3_GOV',  fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,
                          leading=11, spaceAfter=3,
                          backColor=COLOR_VERY_LIGHT, leftIndent=5, rightIndent=5, borderPad=4)
S_BODY  = ParagraphStyle('ck3_BODY', fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,
                          leading=11, spaceAfter=2)
S_NOTE  = ParagraphStyle('ck3_NOTE', fontName='TR-Italic',  fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=2)
S_LABEL = ParagraphStyle('ck3_LBL',  fontName='TR-Bold',    fontSize=8,   textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1)
S_BOLUM = ParagraphStyle('ck3_BLM',  fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceAfter=2)
S_KUCUK = ParagraphStyle('ck3_KCK',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          leading=10, spaceAfter=1)
S_SML   = ParagraphStyle('ck3_SML',  fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,
                          leading=11)
S_SMBD  = ParagraphStyle('ck3_SMBD', fontName='TR-Bold',    fontSize=8,   textColor=COLOR_TEXT,
                          leading=11)
S_TMPL  = ParagraphStyle('ck3_TMPL', fontName='TR-Italic',  fontSize=8,   textColor=COLOR_MUTED,
                          leading=11)
S_CUMLE = ParagraphStyle('ck3_CUMLE',fontName='TR-Regular', fontSize=9,   textColor=COLOR_TEXT,
                          leading=14,
                          backColor=COLOR_VERY_LIGHT, borderPadding=6)
S_TH    = ParagraphStyle('ck3_TH',   fontName='TR-Bold',    fontSize=7.5, textColor=white,
                          alignment=TA_CENTER, leading=10)
S_TD    = ParagraphStyle('ck3_TD',   fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          alignment=TA_LEFT,   leading=10)
S_TD_C  = ParagraphStyle('ck3_TDC',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          alignment=TA_CENTER, leading=10)
S_NUM   = ParagraphStyle('ck3_NUM',  fontName='TR-Bold',    fontSize=10,  textColor=COLOR_PRIMARY,
                          alignment=TA_LEFT,   leading=13)

TABLE_STYLE_BASE = [
    ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
    ('LINEBELOW',     (0, 0), (-1, 0), 1,   COLOR_SECONDARY),
    ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('TOPPADDING',    (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, 0),  3),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 7),
    ('LEFTPADDING',   (0, 0), (-1, -1), 4),
    ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
]

TW = 17 * cm

# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def vsp(h=0.15):
    return Spacer(1, h * cm)


def sp(n=4):
    return Spacer(1, n)


def ck_baslik(no, baslik, kazanim):
    """Unit 1/2 uyumlu renkli başlık bandı + meta satır."""
    blok = []
    blok.append(Paragraph(f'Çalışma Kâğıdı {no} — {baslik}', S_CK))
    blok.append(Paragraph(f'Kazanım: {kazanim}', S_META))
    return blok


def ad_satiri():
    cols = [
        Paragraph('Ad Soyad: ______________________', S_LABEL),
        Paragraph('Sınıf/No: _________', S_LABEL),
        Paragraph('Tarih: ____________', S_LABEL),
    ]
    t = Table([cols], colWidths=[8.5 * cm, 4.25 * cm, 4.25 * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
    ]))
    return t


def yonerge_kutu(metin, sure):
    icerik = f'<b>Yönerge:</b> {metin}    <b>|    Süre:</b> {sure}'
    t = Table([[Paragraph(icerik, S_GOV)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, -1), COLOR_VERY_LIGHT),
        ('BOX',           (0, 0), (-1, -1), 0.5, COLOR_ACCENT),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def bolum(text):
    return Paragraph(text, S_BOLUM)


def alan(etiket, n=2):
    """Etiket + n satirlik yazi alani; list dondurur."""
    return [Paragraph(etiket, S_LABEL), WritingLines(n, 15)]


def bilgi_kutu(icerik):
    t = Table([[Paragraph(icerik, S_SML)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, -1), COLOR_VERY_LIGHT),
        ('BOX',           (0, 0), (-1, -1), 0.5, COLOR_PRIMARY),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('TOPPADDING',    (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def kontrol_tablo(maddeler):
    data = [[Paragraph(b, S_TH) for b in
             ['Kontrol Maddesi', 'Tamam', 'Geliştirilmeli', 'Uygulanamaz']]]
    for m in maddeler:
        data.append([
            Paragraph(m, S_TD),
            Paragraph('( )', S_TD_C),
            Paragraph('( )', S_TD_C),
            Paragraph('( )', S_TD_C),
        ])
    t = Table(data, colWidths=[9.5 * cm, 2.5 * cm, 2.5 * cm, 2.5 * cm])
    t.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
    ]))
    return t


def ogrenci_satiri():
    t = Table([[
        Paragraph('<b>Adı Soyadı:</b>', S_LABEL), '',
        Paragraph('<b>Sınıf/No:</b>', S_LABEL),   '',
        Paragraph('<b>Tarih:</b>', S_LABEL),       '',
    ]], colWidths=[2.7 * cm, 5.1 * cm, 2 * cm, 2.8 * cm, 1.5 * cm, 2.9 * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW',     (1, 0), (1, 0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3, 0), (3, 0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (5, 0), (5, 0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ]))
    return t


def header_blok(no, baslik, kazanim):
    """CK baslik bandi + ad satiri + yonerge."""
    return ck_baslik(no, baslik, kazanim)


# ============================================================
# SAYFA 1: PROBLEM TESPİTİ FORMU
# ============================================================

def ck1():
    e = []
    e += ck_baslik(1, 'Problem Tespiti Formu', 'TT.7.3.1  —  Ders 2  —  ~15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Günlük hayatında seni rahatsız eden ya da zorlandığını gördüğün gerçek bir sorunu '
        'gözlemle ve bu formu doldur.',
        '15 dakika'))
    e.append(vsp(0.1))

    e.append(bolum('Adım 1 — Problem Gözlemi'))
    e += alan('Problemi ne zaman / nerede fark ettin?', 2)
    e.append(vsp(0.1))
    e += alan('Bu problemi KİM yaşıyor? (kişiyi veya grubu tanımla)', 2)
    e.append(vsp(0.1))
    e += alan('Problem tam olarak NE? (ne oluyor, ne zorlanıyorlar?)', 3)

    e.append(vsp(0.1))
    e.append(bolum('Adım 2 — Problemi Bir Cümleyle Tanımla'))
    e.append(Paragraph('[Kişi/grup] , [durum/bağlam] içindeyken [sorun] yaşıyor çünkü [neden].', S_TMPL))
    e += alan('Cevabını yaz:', 3)

    e.append(vsp(0.1))
    e.append(bolum('Adım 3 — Problemi Değerlendir'))
    chk_data = [
        [Paragraph(b, S_TH) for b in ['Soru', 'Evet', 'Hayır', 'Emin Değilim']],
        [Paragraph('Bu problemi gerçek bir kişi yaşıyor mu?',      S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Problem gözlemlenebilir mi?',                   S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Bir ürün veya araç bu problemi çözebilir mi?',  S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Yaşım ve imkânlarımla çözüm üretebilir miyim?', S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
    ]
    chk_t = Table(chk_data, colWidths=[9.5 * cm, 2.5 * cm, 2.5 * cm, 2.5 * cm])
    chk_t.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 8)]))
    e.append(chk_t)

    e.append(vsp(0.1))
    e.append(bolum('Adım 4 — Önem Ölçeği'))
    e.append(Paragraph('Bu problem kaç kişiyi etkiliyor?', S_LABEL))
    olcek = Table([[
        Paragraph('Sadece bir kişi\n( ) 1', S_TD_C),
        Paragraph('Az kişi\n( ) 2', S_TD_C),
        Paragraph('Birçok kişi\n( ) 3', S_TD_C),
        Paragraph('Çok fazla kişi\n( ) 4', S_TD_C),
    ]], colWidths=[4.25 * cm] * 4)
    olcek.setStyle(TableStyle([
        ('GRID',           (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ALIGN',          (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',         (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',     (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',  (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [COLOR_VERY_LIGHT_GREY]),
    ]))
    e.append(olcek)

    e.append(vsp(0.1))
    e.append(bolum('Yansıtma'))
    e += alan('Bu problemle çalışmak istememin nedeni:', 2)
    return e


# ============================================================
# SAYFA 2: EMPATİ HARİTASI
# ============================================================

def ck2():
    e = []
    e += ck_baslik(2, 'Empati Haritası', 'TT.7.3.1  —  Ders 3  —  ~15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Problemini yaşayan kişiyi gözlemle ya da hayal et. Onun yerine geç; '
        'ne düşündüğünü, hissettiğini, söylediğini ve yaptığını yaz.',
        '15 dakika'))
    e.append(vsp(0.1))

    e.append(bolum('Kullanıcı Profili'))
    profil = Table([[
        Paragraph('<b>Adı / Takma Adı:</b>', S_SML), '',
        Paragraph('<b>Yaşı:</b>', S_SML), '',
        Paragraph('<b>Rolü / Mesleği:</b>', S_SML), '',
    ]], colWidths=[3.2 * cm, 3 * cm, 1.4 * cm, 1.8 * cm, 3 * cm, 4.6 * cm])
    profil.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW',     (1, 0), (1, 0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3, 0), (3, 0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (5, 0), (5, 0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
    ]))
    e.append(profil)
    e.append(sp(5))

    S_QUAD = ParagraphStyle('ck3_QUAD', fontName='TR-Bold', fontSize=8.5, textColor=white,
                             alignment=TA_CENTER, leading=11)
    S_SMMT = ParagraphStyle('ck3_SMMT', fontName='TR-Italic', fontSize=7.5, textColor=COLOR_MUTED,
                             leading=10)
    quad = Table([
        [Paragraph('DÜŞÜNÜYOR', S_QUAD),
         Paragraph('HİSSEDİYOR', S_QUAD)],
        [Paragraph('(Kafasında neler dönüyor? Endişeleri neler?)', S_SMMT),
         Paragraph('(Hangi duygu? Mutlu mu, hayal kırıklığı mı?)', S_SMMT)],
        [Paragraph('SÖYLÜYOR', S_QUAD),
         Paragraph('YAPIYOR', S_QUAD)],
        [Paragraph('(Başkalarına ne söylüyor? Şikâyetleri?)', S_SMMT),
         Paragraph('(Bu problem için günlük hayatta ne yapıyor?)', S_SMMT)],
    ], colWidths=[8.4 * cm, 8.4 * cm],
       rowHeights=[0.65 * cm, 5.0 * cm, 0.65 * cm, 5.0 * cm])
    quad.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('BACKGROUND',    (0, 2), (-1, 2),  COLOR_PRIMARY),
        ('TEXTCOLOR',     (0, 0), (-1, 0),  white),
        ('TEXTCOLOR',     (0, 2), (-1, 2),  white),
        ('BACKGROUND',    (0, 1), (-1, 1),  white),
        ('BACKGROUND',    (0, 3), (-1, 3),  white),
        ('BOX',           (0, 0), (-1, -1), 1, COLOR_PRIMARY),
        ('GRID',          (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('ALIGN',         (0, 0), (-1, 0),  'CENTER'),
        ('ALIGN',         (0, 2), (-1, 2),  'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
    ]))
    e.append(quad)
    e.append(vsp(0.15))

    e.append(bolum('Temel Bulgular'))
    e += alan('En büyük acı noktası (pain point):', 1)
    e.append(sp(2))
    e += alan('En çok ihtiyaç duyduğu şey:', 1)
    e.append(sp(2))
    e += alan('Tasarımımın ona sağlaması gereken fayda:', 1)
    return e


# ============================================================
# SAYFA 3: KULLANICI ANALİZ TABLOSU
# ============================================================

def ck3():
    e = []
    e += ck_baslik(3, 'Kullanıcı Analiz Tablosu', 'TT.7.3.1  —  Ders 3  —  ~10 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        "ÇK2'deki empati haritanı kullanarak kullanıcını daha derinlemesine analiz et.",
        '10 dakika'))
    e.append(vsp(0.1))

    e.append(bolum('Kullanıcı Özeti'))
    ozet = Table([
        [Paragraph('<b>Kategori</b>', S_TH), Paragraph('<b>Bilgi</b>', S_TH)],
        [Paragraph('Kullanıcı kim?', S_TD), ''],
        [Paragraph('Yaşı / Grubu', S_TD), ''],
        [Paragraph('Problemi nerede yaşıyor?', S_TD), ''],
        [Paragraph('Problemi ne zaman yaşıyor?', S_TD), ''],
        [Paragraph('Şu an nasıl çözüyor? (varsa)', S_TD), ''],
        [Paragraph('Mevcut çözümün eksikleri', S_TD), ''],
    ], colWidths=[5 * cm, 12 * cm])
    ozet.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 18)]))
    e.append(ozet)
    e.append(sp(4))

    e.append(bolum('İhtiyaç Analizi'))
    e += alan('Kullanıcının gerçek ihtiyacı (bunu yapmak istiyor, bunu başarmak istiyor...):', 2)
    e.append(sp(3))
    e += alan('Kısıtlar (para, zaman, fiziksel sınırlamalar...):', 2)
    e.append(sp(3))
    e += alan('İdeal çözüm nasıl olmalı? (kullanıcının gözünden):', 2)
    e.append(sp(4))

    e.append(bolum('Tasarım Kriterleri'))
    e.append(Paragraph('Tasarımımın sağlaması gereken en önemli 3 özellik:', S_LABEL))
    krit = Table([
        [Paragraph('<b>#</b>', S_TH), Paragraph('<b>Kriter</b>', S_TH)],
        [Paragraph('1', S_TD_C), ''],
        [Paragraph('2', S_TD_C), ''],
        [Paragraph('3', S_TD_C), ''],
    ], colWidths=[1 * cm, 16 * cm])
    krit.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('ALIGN',         (0, 0), (0, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 15),
    ]))
    e.append(krit)
    e.append(sp(4))

    e.append(bolum('Yansıtma'))
    e += alan('Kullanıcımı anlamak için daha ne yapabilirdim?', 2)
    return e


# ============================================================
# SAYFA 4: CRAZY 8 BEYİN FIRTINASI
# ============================================================

def ck4():
    e = []
    e += ck_baslik(4, 'Crazy 8 Beyin Fırtınası', 'TT.7.3.2  —  Ders 4  —  ~10 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Her kutuya farklı bir fikir çiz veya yaz. 8 dakikan var — her fikre sadece '
        '1 dakika! Eleştirme, mükemmel olmak zorunda değil.',
        '8 dk + 2 dk seçim'))
    e.append(vsp(0.1))

    crazy8 = Table([
        [Paragraph('<b>1</b>', S_NUM), Paragraph('<b>2</b>', S_NUM)],
        [Paragraph('<b>3</b>', S_NUM), Paragraph('<b>4</b>', S_NUM)],
        [Paragraph('<b>5</b>', S_NUM), Paragraph('<b>6</b>', S_NUM)],
        [Paragraph('<b>7</b>', S_NUM), Paragraph('<b>8</b>', S_NUM)],
    ], colWidths=[8.4 * cm, 8.4 * cm], rowHeights=[4.7 * cm] * 4)
    crazy8.setStyle(TableStyle([
        ('GRID',          (0, 0), (-1, -1), 1,   COLOR_LIGHT_GREY),
        ('BOX',           (0, 0), (-1, -1), 1.2, COLOR_PRIMARY),
        ('BACKGROUND',    (0, 0), (-1, -1), white),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('ALIGN',         (0, 0), (-1, -1), 'LEFT'),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
    ]))
    e.append(crazy8)
    e.append(sp(5))
    e.append(bilgi_kutu(
        'En beğendiğim 2 fikir:  No: ____  ve  No: ____'
        '     Neden bu ikisini seçtim: ______________________________'))
    return e


# ============================================================
# SAYFA 5: FİKİR SEÇİM MATRİSİ
# ============================================================

def ck5():
    e = []
    e += ck_baslik(5, 'Fikir Seçim Matrisi', 'TT.7.3.2  —  Ders 4  —  ~10 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        "Crazy 8'den seçtiğin en iyi fikirleri buraya yaz. "
        "Her fikri kriterlere göre 1–3 puan ver.",
        '10 dakika'))
    e.append(vsp(0.1))

    e.append(Paragraph('<b>Puanlama:</b>  1 = Zayıf    2 = Orta    3 = İyi', S_SML))
    e.append(sp(4))
    matris = Table([
        [Paragraph('<b>Kriter</b>', S_TH), Paragraph('<b>Ağır.</b>', S_TH),
         Paragraph('<b>Fikir A</b>', S_TH), Paragraph('<b>Fikir B</b>', S_TH),
         Paragraph('<b>Fikir C</b>', S_TH)],
        [Paragraph('Fikir / Tasarım Adı', S_TD), Paragraph('—', S_TD_C),
         Paragraph('__________', S_TD_C), Paragraph('__________', S_TD_C),
         Paragraph('__________', S_TD_C)],
        [Paragraph('Kullanıcı ihtiyacını karşılıyor mu?', S_TD),
         Paragraph('× 3', S_TD_C), '', '', ''],
        [Paragraph('Yapılabilir mi? (malzeme, süre)', S_TD),
         Paragraph('× 2', S_TD_C), '', '', ''],
        [Paragraph('Özgün / yaratıcı mı?', S_TD),
         Paragraph('× 2', S_TD_C), '', '', ''],
        [Paragraph('Ergonomik olabilir mi?', S_TD),
         Paragraph('× 1', S_TD_C), '', '', ''],
        [Paragraph('Sürdürülebilir malzeme kullanılabilir mi?', S_TD),
         Paragraph('× 1', S_TD_C), '', '', ''],
        [Paragraph('<b>TOPLAM (maks. 27)</b>', S_SMBD),
         Paragraph('—', S_TD_C),
         Paragraph('___', S_TD_C), Paragraph('___', S_TD_C), Paragraph('___', S_TD_C)],
    ], colWidths=[7 * cm, 1.5 * cm, 2.83 * cm, 2.83 * cm, 2.84 * cm])
    matris.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('BOTTOMPADDING', (0, 1), (-1, -1), 20),
        ('BACKGROUND',    (0, 7), (-1, 7),  COLOR_VERY_LIGHT_GREY),
        ('FONTNAME',      (0, 7), (-1, 7),  'TR-Bold'),
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
    ]))
    e.append(matris)
    e.append(sp(6))
    e.append(bilgi_kutu('Kazanan fikir: _______________________________________'))
    e.append(sp(4))

    e.append(bolum('Seçim Gerekçesi'))
    e += alan('Neden bu fikri seçtim:', 3)
    e.append(sp(3))
    e += alan('Bu fikri geliştirmek için düşündüğüm değişiklikler:', 2)
    return e


# ============================================================
# SAYFA 6: TASARIM ESKİZİ SAYFASI
# ============================================================

def ck6():
    e = []
    e += ck_baslik(6, 'Tasarım Eskizi Sayfası', 'TT.7.3.2  —  Ders 5  —  ~15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Seçtiğin fikri çiz. Mükemmel olmak zorunda değilsin — fikri aktarması yeterli. '
        'Boyutları ve malzeme notlarını da ekle.',
        '15 dakika'))
    e.append(vsp(0.1))

    isim = Table([[
        Paragraph('<b>Tasarım Adı:</b>', S_LABEL), '',
        Paragraph('<b>Versiyon:</b>', S_LABEL), '',
    ]], colWidths=[3 * cm, 10.5 * cm, 2 * cm, 1.5 * cm])
    isim.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW',     (1, 0), (1, 0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3, 0), (3, 0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
    ]))
    e.append(isim)
    e.append(sp(4))

    e.append(bolum('Ana Eskiz  (Ön Görünüş)'))
    e.append(DrawingBox(height=9 * cm, caption='Ön görünüşü buraya çiz'))
    e.append(sp(4))

    e.append(bolum('Detay Görünüşler'))
    detail = Table([[
        DrawingBox(width=8.2 * cm, height=5 * cm, caption='Yan görünüş'),
        DrawingBox(width=8.2 * cm, height=5 * cm, caption='Üst görünüş'),
    ]], colWidths=[8.5 * cm, 8.5 * cm])
    detail.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ]))
    e.append(detail)
    e.append(sp(4))

    e.append(bolum('Ölçüler ve Malzeme Notları'))
    e.append(Paragraph(
        '<b>Tahmini boyutlar:</b>  En: _____ cm   Boy: _____ cm   Yükseklik: _____ cm',
        S_SML))
    e += alan('Kullanmayı düşündüğüm malzemeler:', 1)
    e.append(sp(2))
    e += alan('Özel dikkat edilmesi gereken detay:', 1)
    return e


# ============================================================
# SAYFA 7: MALZEME PLANLAMA TABLOSU
# ============================================================

def ck7():
    e = []
    e += ck_baslik(7, 'Malzeme Planlama Tablosu', 'TT.7.3.2  —  Ders 5  —  ~10 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Prototipini yapmak için ihtiyaç duyduğun malzemeleri listele. '
        'Her malzemeyi gerçekçi şekilde değerlendir.',
        '10 dakika'))
    e.append(vsp(0.1))

    e.append(bolum('Malzeme Listesi'))
    m_data = [[
        Paragraph('<b>#</b>', S_TH),
        Paragraph('<b>Malzeme</b>', S_TH),
        Paragraph('<b>Miktar</b>', S_TH),
        Paragraph('<b>Boyut / Özellik</b>', S_TH),
        Paragraph('<b>Nereden Temin?</b>', S_TH),
        Paragraph('<b>Maliyet</b>', S_TH),
    ]]
    for i in range(1, 9):
        m_data.append([Paragraph(str(i), S_TD_C), '', '', '', '', ''])
    malzeme = Table(m_data, colWidths=[0.8 * cm, 4.8 * cm, 1.8 * cm, 3.5 * cm, 3.7 * cm, 2.4 * cm])
    malzeme.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('ALIGN',         (0, 0), (0, -1), 'CENTER'),
        ('ALIGN',         (2, 0), (2, -1), 'CENTER'),
        ('ALIGN',         (5, 0), (5, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
    ]))
    e.append(malzeme)
    e.append(bilgi_kutu('Tahmini toplam maliyet: _____________ TL'))
    e.append(sp(4))

    e.append(bolum('Araçlar ve Ekipmanlar'))
    e += alan('Kullanmam gereken araçlar:', 1)
    e.append(sp(3))

    e.append(bolum('Sürdürülebilirlik Notu'))
    surd = Table([
        [Paragraph('<b>Konu</b>', S_TH), Paragraph('<b>Yanıt</b>', S_TH)],
        [Paragraph('Geri dönüştürülmüş / atık malzeme kullandım mı?', S_TD),
         Paragraph('( ) Evet — ________________   ( ) Hayır', S_TD)],
        [Paragraph('Doğal / çevre dostu malzeme var mı?', S_TD),
         Paragraph('( ) Evet — ________________   ( ) Hayır', S_TD)],
        [Paragraph('Malzeme fazlası oluşursa ne yapacağım?', S_TD), ''],
    ], colWidths=[8 * cm, 9 * cm])
    surd.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 12)]))
    e.append(surd)
    e.append(sp(4))

    e.append(bolum('Yansıtma'))
    e += alan('Bu malzemelerle gerçekten yapabilir miyim? Aklımdaki en büyük zorluk:', 1)
    return e


# ============================================================
# SAYFA 8 (2 sayfa): PROTOTİP SÜREÇ GÜNLÜĞÜ
# ============================================================

def ck8():
    e = []
    e += ck_baslik(8, 'Prototip Süreç Günlüğü', 'TT.7.3.2  —  Ders 6–7  —  ~20 dk × 2')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Her ders saatinin sonunda bu günlüğü doldur. '
        'Yanlış giden şeyler de tasarım sürecinin parçasıdır — dürüst yaz!',
        '5–8 dakika / ders'))
    e.append(vsp(0.1))

    e.append(bilgi_kutu('DERS 6 — İlk Üretim Günü'))
    e.append(sp(4))
    e.append(Paragraph('<b>Tarih:</b> ___________', S_LABEL))
    e.append(sp(3))
    e += alan('Bugün ne yaptım?', 3)
    e.append(sp(3))
    e += alan('Hangi adımı tamamladım?', 1)
    e.append(sp(3))
    e += alan('Karşılaştığım zorluk:', 2)
    e.append(sp(3))
    e += alan('Bu zorluğu nasıl çözdüm / çözmeye çalıştım?', 2)
    e.append(sp(5))

    e.append(bolum('Bugünün Eskizi'))
    e.append(DrawingBox(height=5.5 * cm, caption='Bugün ne görünüyordu?'))
    e.append(sp(3))
    e += alan('Yarın devam edeceklerim:', 2)

    # Sayfa 2 (CK8 devam)
    e.append(PageBreak())
    e += ck_baslik(8, 'Prototip Süreç Günlüğü — Ders 7', 'TT.7.3.2  —  Ders 7  —  ~20 dk')
    e.append(ogrenci_satiri())
    e.append(vsp(0.1))
    e.append(bilgi_kutu('DERS 7 — Tamamlama Günü'))
    e.append(sp(4))
    e.append(Paragraph('<b>Tarih:</b> ___________', S_LABEL))
    e.append(sp(3))
    e += alan('Bugün ne yaptım?', 3)
    e.append(sp(3))
    e += alan('Planlamadığım ama yaptığım değişiklik:', 2)
    e.append(sp(3))
    e += alan('Prototipim şu an nasıl görünüyor? (kısaca tanımla):', 2)
    e.append(sp(4))

    e.append(bolum('Değerlendirme'))
    dg = Table([
        [Paragraph('<b>Konu</b>', S_TH), Paragraph('<b>Yanıt</b>', S_TH)],
        [Paragraph('Memnun olduğum kısım', S_TD), ''],
        [Paragraph('Hâlâ eksik olan kısım', S_TD), ''],
    ], colWidths=[5 * cm, 12 * cm])
    dg.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 18)]))
    e.append(dg)
    e.append(sp(5))
    e.append(bilgi_kutu(
        'Teste hazır mıyım?  ( ) Evet — tam hazır    '
        '( ) Evet — bazı eksiklerle    ( ) Hayır — neden: ___________________'))
    return e


# ============================================================
# SAYFA 9: ÜRÜN TEST VE GERİ BİLDİRİM FORMU
# ============================================================

def ck9():
    e = []
    e += ck_baslik(9, 'Ürün Test ve Geri Bildirim Formu', 'TT.7.3.2  —  Ders 8  —  ~15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Prototipini bir kullanıcıya dene. Test ederken gözlem yap; '
        'bittikten sonra geri bildirim al.',
        '15 dakika'))
    e.append(vsp(0.1))

    e.append(bolum('Test Bilgileri'))
    tb = Table([[
        Paragraph('<b>Test eden kişi:</b>', S_LABEL), '',
        Paragraph('<b>İlişkisi:</b>', S_LABEL), '',
    ]], colWidths=[3.5 * cm, 5 * cm, 2.5 * cm, 6 * cm])
    tb.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW',     (1, 0), (1, 0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3, 0), (3, 0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
    ]))
    e.append(tb)
    e.append(sp(3))

    e.append(bolum('Gözlem Notları  (test sırasında al)'))
    e += alan('Test ederken kullanıcı şunları yaptı:', 2)
    e.append(sp(3))
    e += alan('Kullanıcının zorlandığı nokta:', 2)
    e.append(sp(3))
    e += alan('Kullanıcının kolayca yaptığı şey:', 1)
    e.append(sp(4))

    e.append(bolum('Geri Bildirim Soruları  (test sonrası sor)'))
    r_data = [
        [Paragraph('<b>Soru</b>', S_TH),
         Paragraph('1\nZayıf', S_TH), Paragraph('2', S_TH), Paragraph('3', S_TH),
         Paragraph('4', S_TH), Paragraph('5\nMükemmel', S_TH)],
        [Paragraph('Ürünü kullanmak ne kadar kolaydı?', S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Ürün problemi ne kadar çözüyor?', S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Tasarım ne kadar güvenli hissettiriyor?', S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Ürün ne kadar dayanıklı görünüyor?', S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
        [Paragraph('Genel memnuniyet', S_TD),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
         Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C)],
    ]
    rating = Table(r_data, colWidths=[8.5 * cm, 1.7 * cm, 1.7 * cm, 1.7 * cm, 1.7 * cm, 1.7 * cm])
    rating.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    e.append(rating)
    e.append(sp(4))

    e.append(bolum('Açık Sorular'))
    e += alan('"Bu ürünü gerçekten kullanır mıydın? Neden?"', 2)
    e.append(sp(3))
    e += alan('"Değişmesini istediğin bir şey ne olurdu?"', 2)
    e.append(sp(3))

    e.append(bolum('Test Sonucu'))
    e += alan('En önemli iyileştirme önerisi:', 1)
    e.append(sp(2))
    e += alan('Benim kendi gözlemim — değiştirmem gereken şey:', 1)
    return e


# ============================================================
# SAYFA 10: REVİZE PLANI + SÜRDÜRÜLEBİLİRLİK KONTROLÜ
# ============================================================

def ck10():
    e = []
    e += ck_baslik(10, 'Revize Planı + Sürdürülebilirlik Kontrolü',
                   'TT.7.3.2  —  Ders 9  —  ~15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        "ÇK9'daki geri bildirimleri kullanarak ürününü iyileştir. "
        "Sürdürülebilirlik ve ergonomi kontrolünü de unutma.",
        '15 dakika'))
    e.append(vsp(0.1))

    e.append(bolum('Revize Listesi'))
    rv = Table([
        [Paragraph('<b>#</b>', S_TH),
         Paragraph('<b>Değiştirilecek Kısım</b>', S_TH),
         Paragraph('<b>Neden? (geri bildirim kaynağı)</b>', S_TH),
         Paragraph('<b>Yapıldı</b>', S_TH)],
        *[[Paragraph(str(i), S_TD_C), '', '', Paragraph('( )', S_TD_C)] for i in range(1, 6)],
    ], colWidths=[0.8 * cm, 6.5 * cm, 7.5 * cm, 2.2 * cm])
    rv.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('ALIGN',         (0, 0),  (0, -1),  'CENTER'),
        ('ALIGN',         (-1, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 1),  (-1, -1), 14),
    ]))
    e.append(rv)
    e.append(sp(4))

    e.append(bolum('Revize Karşılaştırması'))
    karsil = Table([
        [Paragraph('<b>Önceki hali nasıldı?</b>', S_SMBD),
         Paragraph('<b>Şimdi nasıl?</b>', S_SMBD)],
        [WritingLines(2, 14), WritingLines(2, 14)],
    ], colWidths=[8.4 * cm, 8.4 * cm])
    karsil.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_VERY_LIGHT_GREY),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    e.append(karsil)
    e.append(sp(5))

    e.append(bolum('Ergonomi Kontrol Listesi'))
    e.append(kontrol_tablo([
        'Ürün tutulması / kullanılması kolay',
        'Keskin / tehlikeli kenar yok',
        'Ağırlık ve boyut kullanıcıya uygun',
        'Hareketli parçalar güvenli',
        'Uzun süre kullanımda rahat',
    ]))
    e.append(sp(5))

    e.append(bolum('Sürdürülebilirlik Kontrol Listesi'))
    e.append(kontrol_tablo([
        'Gereksiz malzeme kullanımından kaçınıldı',
        'En az bir geri dönüştürülmüş / atık malzeme kullanıldı',
        'Ürün onarılabilir ya da parçalanabilir',
        'Uzun ömürlü olacak şekilde tasarlandı',
        'Doğaya zarar vermeyen malzeme seçildi',
    ]))
    e.append(sp(4))

    e.append(bolum('Yansıtma'))
    e += alan('Bu revizeden sonra ürünüm nasıl değişti?', 1)
    e.append(sp(2))
    e += alan('Tasarım döngüsü sona mı erdi? Bir sonraki adımda ne yapardın?', 1)
    return e


# ============================================================
# SAYFA 11: TASARIM SÜRECİ SUNUM ŞABLONU
# ============================================================

def ck11():
    e = []
    e += ck_baslik(11, 'Tasarım Süreci Sunum Şablonu', '—  Ders 10  —  ~15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Tasarım sürecini bu şablona özetle. Sunum sırasında bu kâğıdı rehber olarak kullan.',
        '15 dakika hazırlık'))
    e.append(vsp(0.1))

    e.append(Paragraph(
        'Benim tasarımım  <b>_________________________</b>  için   '
        '<b>_________________________</b>  yapar,   '
        'çünkü  <b>_________________________</b>.', S_CUMLE))
    e.append(sp(5))

    e.append(bolum('7 Adım Özeti'))
    ozet = Table([
        [Paragraph('<b>Adım</b>', S_TH),
         Paragraph('<b>Yaptığım</b>', S_TH),
         Paragraph('<b>En Önemli Bulgum</b>', S_TH)],
        *[[Paragraph(a, S_TD), '', ''] for a in [
            '1 — Problem Tespiti', '2 — Analiz / Empati', '3 — Fikir Üretimi',
            '4 — Eskiz / Taslak', '5 — Uygulama', '6 — Test', '7 — Revize',
        ]],
    ], colWidths=[4.5 * cm, 6.25 * cm, 6.25 * cm])
    ozet.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 10)]))
    e.append(ozet)
    e.append(sp(4))

    e.append(bolum('Ürünümü Tanıtıyorum'))
    urun = Table([
        [Paragraph('<b>Alan</b>', S_TH), Paragraph('<b>Bilgi</b>', S_TH)],
        *[[Paragraph(a, S_TD), ''] for a in [
            'Ürünümün adı', 'Hangi problemi çözüyor?', 'Kullanıcım kim?',
            'En özgün yanı', 'Sürdürülebilirlik özelliği',
        ]],
    ], colWidths=[5 * cm, 12 * cm])
    urun.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 10)]))
    e.append(urun)
    e.append(sp(4))

    e.append(bolum('Öz Değerlendirme'))
    oz = Table([
        [Paragraph('<b>Konu</b>', S_TH),
         Paragraph('<b>1</b>', S_TH), Paragraph('<b>2</b>', S_TH),
         Paragraph('<b>3</b>', S_TH), Paragraph('<b>4</b>', S_TH),
         Paragraph('<b>5</b>', S_TH)],
        *[[Paragraph(k, S_TD),
           Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
           Paragraph('( )', S_TD_C), Paragraph('( )', S_TD_C),
           Paragraph('( )', S_TD_C)] for k in [
            'Tasarımım problemi çözüyor',
            'Tüm adımları uyguladım',
            'Kullanıcı geri bildirimini dikkate aldım',
            'Özgün ve yaratıcı bir çözüm ürettim',
        ]],
    ], colWidths=[9.2 * cm, *[1.56 * cm] * 5])
    oz.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    e.append(oz)
    e.append(sp(4))
    e += alan('Bu ünitede en çok öğrendiğim şey:', 2)
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
        title='3. Unite -- Tasarim Odakli Surec: Calisma Kagitlari',
    )
    doc.unite_info = UNITE_ADI

    story = []
    sayfalar = [ck1, ck2, ck3, ck4, ck5, ck6, ck7, ck8, ck9, ck10, ck11]
    for i, ck in enumerate(sayfalar):
        story += ck()
        if i < len(sayfalar) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print('OK  U3_PDF_03_Calisma_Kagitlari.pdf  (12 sayfa)')


if __name__ == '__main__':
    main()
