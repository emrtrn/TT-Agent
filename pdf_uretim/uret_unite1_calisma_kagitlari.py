# -*- coding: utf-8 -*-
"""
1. Unite - Calisma Kagitlari (Kombine)
Calistirir: python pdf_uretim/uret_unite1_calisma_kagitlari.py
Uretilen PDF: units/7_sinif/unit1/U1_Calisma_Kagitlari_Kombine.pdf
- Kapak sayfasi YOK
- 8 calisma kagidi, her biri bir sayfada
- Tutarli baslik formati: "Calisma Kagidi N - Baslik"
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, Flowable,
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

CIKTI = os.path.join(PDF_DIR, 'U1_Calisma_Kagitlari_Kombine.pdf')
UI    = 'Teknoloji ve Tasarım - 7. Sınıf - 1. Ünite: Çalışma Kâğıtları'

# ============================================================
# STİLLER
# ============================================================

S_CK    = ParagraphStyle('ck_CK',   fontName='TR-Bold',    fontSize=10.5, textColor=white,
                          leading=13, alignment=TA_LEFT,
                          backColor=COLOR_PRIMARY, borderPad=5,
                          spaceBefore=0, spaceAfter=3)
S_META  = ParagraphStyle('ck_META', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=3)
S_BSL   = ParagraphStyle('ck_BSL',  fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceBefore=4, spaceAfter=2)
S_GOV   = ParagraphStyle('ck_GOV',  fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=3, alignment=TA_JUSTIFY,
                          backColor=COLOR_VERY_LIGHT, leftIndent=5, rightIndent=5,
                          borderPad=4)
S_BODY  = ParagraphStyle('ck_BODY', fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=2)
S_NOTE  = ParagraphStyle('ck_NOTE', fontName='TR-Italic',  fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=2)
S_LABEL = ParagraphStyle('ck_LBL',  fontName='TR-Bold',    fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1)
S_STEP  = ParagraphStyle('ck_STEP', fontName='TR-Bold',    fontSize=8, textColor=white,
                          leading=11, backColor=COLOR_SECONDARY, borderPad=3,
                          spaceBefore=4, spaceAfter=2)
S_QUES  = ParagraphStyle('ck_QST',  fontName='TR-Bold',    fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1, spaceBefore=3)
S_CELL  = ParagraphStyle('ck_CEL',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          leading=10)
S_CELLB = ParagraphStyle('ck_CLB',  fontName='TR-Bold',    fontSize=7.5, textColor=COLOR_TEXT,
                          leading=10)


def vsp(h=0.15):
    return Spacer(1, h * cm)


def hr():
    return HRFlowable(width='100%', thickness=0.4, color=COLOR_LIGHT_GREY,
                      spaceAfter=3, spaceBefore=3)


def ck_baslik(no, baslik, tur=None, sure=None):
    blok = []
    blok.append(Paragraph(f'Çalışma Kâğıdı {no} — {baslik}', S_CK))
    parts = []
    if tur:
        parts.append(f'Tür: {tur}')
    if sure:
        parts.append(f'Süre: {sure}')
    if parts:
        blok.append(Paragraph('  |  '.join(parts), S_META))
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


def grup_satiri():
    cols = [
        Paragraph('Grup No: _______', S_LABEL),
        Paragraph('Tarih: ______________', S_LABEL),
        Paragraph('Ders Saati: _________', S_LABEL),
    ]
    t = Table([cols], colWidths=[5 * cm, 6 * cm, 6 * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
    ]))
    return t


def grup_uyeler():
    return Paragraph(
        'Grup Üyeleri: ______________________  ______________________  ______________________',
        S_LABEL)


def cp(txt, bold=False):
    return Paragraph(txt, S_CELLB if bold else S_CELL)


def tablo_stili(header_color=None):
    hc = header_color or COLOR_PRIMARY
    return TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), hc),
        ('TEXTCOLOR',     (0, 0), (-1, 0), white),
        ('FONTNAME',      (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTSIZE',      (0, 0), (-1, -1), 7.5),
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 0.8, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ])


# ============================================================
# ÖZEL FLOWABLE'LAR
# ============================================================

class DrawingBox(Flowable):
    """Ortasında kavram etiketi olan çerçeveli zihin haritası kutusu"""
    def __init__(self, width, height, label):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.label = label

    def draw(self):
        c = self.canv
        c.setStrokeColor(COLOR_PRIMARY)
        c.setFillColor(COLOR_VERY_LIGHT)
        c.setLineWidth(1.2)
        c.roundRect(0, 0, self.width, self.height, 6, stroke=1, fill=1)
        c.setFillColor(COLOR_PRIMARY)
        c.setFont('TR-Bold', 13)
        c.drawCentredString(self.width / 2, self.height / 2 - 5, self.label)

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)


class VennDiyagrami(Flowable):
    """İki kesişen daireden oluşan Venn diyagramı"""
    def __init__(self, width, height):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        r = h * 0.41
        cx1 = w * 0.34
        cx2 = w * 0.66
        cy = h * 0.5

        c.setLineWidth(1.2)
        c.setStrokeColor(COLOR_PRIMARY)
        c.circle(cx1, cy, r, stroke=1, fill=0)
        c.setStrokeColor(COLOR_SECONDARY)
        c.circle(cx2, cy, r, stroke=1, fill=0)

        c.setFont('TR-Italic', 7.5)
        c.setFillColor(COLOR_MUTED)
        c.drawCentredString(cx1 - r * 0.52, cy + 5, 'Ürün 1')
        c.drawCentredString(cx1 - r * 0.52, cy - 8, 'yalnızca')
        c.drawCentredString((cx1 + cx2) / 2, cy + 5, 'Ortak')
        c.drawCentredString((cx1 + cx2) / 2, cy - 8, 'özellikler')
        c.drawCentredString(cx2 + r * 0.52, cy + 5, 'Ürün 2')
        c.drawCentredString(cx2 + r * 0.52, cy - 8, 'yalnızca')

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)


# ============================================================
# SAYFA 1: ZİHİN HARİTAM
# ============================================================

def ck1():
    e = []
    e += ck_baslik(1, 'ZİHİN HARİTAM', tur='Bireysel', sure='5 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(Paragraph(
        'Yönerge: Aşağıdaki iki merkez kelimeyi görüyorsun: <b>TEKNOLOJİ</b> ve <b>TASARIM</b>. '
        'Bu kelimeleri duyunca aklına hangi kelimeler, kavramlar, nesneler, örnekler geliyor? '
        'Aklına gelen her şeyi oklarla bağlayarak yaz. Doğru/yanlış cevap yok!',
        S_GOV))
    e.append(vsp(0.1))

    box1 = DrawingBox(8.1 * cm, 9 * cm, 'TEKNOLOJİ')
    box2 = DrawingBox(8.1 * cm, 9 * cm, 'TASARIM')
    kutu_t = Table([[box1, box2]], colWidths=[8.5 * cm, 8.5 * cm])
    kutu_t.setStyle(TableStyle([
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
    ]))
    e.append(kutu_t)
    e.append(vsp(0.15))

    e.append(Paragraph(
        'Son Soru: Sence teknoloji ile tasarım birbiriyle ilişkili mi? Neden?',
        S_QUES))
    e.append(WritingLines(2, line_spacing=18))
    e.append(vsp(0.1))
    e.append(Paragraph(
        'Not: Bu kâğıdı öğretmenin saklayacak ve ünite sonunda sana geri verecek. '
        'Ünite sonunda aynı kâğıda farklı renkle ekleme yapacaksın — aradaki fark öğrendiklerini gösterecek!',
        S_NOTE))
    return e


# ============================================================
# SAYFA 2: 5N1K KAVRAM SORGULAMASI
# ============================================================

def ck2():
    e = []
    e += ck_baslik(2, '5N1K KAVRAM SORGULAMASI', tur='Grup', sure='10 dk')
    e.append(grup_satiri())
    e.append(grup_uyeler())
    e.append(vsp(0.08))
    e.append(Paragraph(
        'Yönerge: Grubunuz 3 kavram kartı aldı. Her kavram için aşağıdaki 6 soruyu cevaplayın. '
        'Bilmediğiniz noktalar için "Bunu araştırmamız gerekiyor" diye not düşün.',
        S_GOV))
    e.append(vsp(0.08))

    sorular = ['NE?', 'NE ZAMAN?', 'NEREDE?', 'NASIL?', 'NEDEN?', 'KİM?']
    cw = 17 * cm / 3

    def kavram_tablo(baslik):
        data = [[cp(baslik, True), '']]
        for s in sorular:
            data.append([cp(s, True), ''])
        t = Table(data, colWidths=[cw * 0.38, cw * 0.62])
        t.setStyle(TableStyle([
            ('SPAN',          (0, 0), (1, 0)),
            ('BACKGROUND',    (0, 0), (-1, 0), COLOR_SECONDARY),
            ('TEXTCOLOR',     (0, 0), (-1, 0), white),
            ('ALIGN',         (0, 0), (-1, 0), 'CENTER'),
            ('FONTSIZE',      (0, 0), (-1, -1), 7.5),
            ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
            ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
            ('LINEBELOW',     (0, 0), (-1, 0), 0.8, COLOR_PRIMARY),
            ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING',    (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING',   (0, 0), (-1, -1), 4),
            ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ]))
        return t

    k1 = kavram_tablo('KAVRAM 1: _______________')
    k2 = kavram_tablo('KAVRAM 2: _______________')
    k3 = kavram_tablo('KAVRAM 3: _______________')
    ust = Table([[k1, k2, k3]], colWidths=[cw, cw, cw])
    ust.setStyle(TableStyle([
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 2),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    e.append(ust)
    e.append(vsp(0.12))
    e.append(hr())
    e.append(Paragraph('Sınıfa Sunacağımız Özet', S_BSL))
    e.append(Paragraph(
        'Bu 3 kavramı 2 cümle ile sınıfa nasıl anlatacaksınız?', S_BODY))
    e.append(WritingLines(2, line_spacing=18))
    e.append(vsp(0.1))
    e.append(Paragraph('Araştırılması Gereken Sorularımız', S_BSL))
    for i in range(1, 4):
        e.append(Paragraph(
            f'{i}. ___________________________________________________________________________',
            S_BODY))
    return e


# ============================================================
# SAYFA 3: KAYNAK KARŞILAŞTIRMA
# ============================================================

def ck3():
    e = []
    e += ck_baslik(3, 'KAYNAK KARŞILAŞTIRMA', tur='Bireysel', sure='15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.08))
    e.append(Paragraph(
        'Yönerge: Öğretmenin sınıfa 3 farklı kaynaktan aynı teknoloji haberini getirdi. '
        'Her kaynağı aşağıdaki tablo üzerinde incele. Amaç "daha doğru" olanı bulmak değil, '
        'her kaynağın nasıl yazıldığını görmek.',
        S_GOV))
    e.append(vsp(0.06))
    e.append(Paragraph(
        'Haberin Konusu: _______________________________________________________________',
        S_LABEL))
    e.append(vsp(0.06))

    kriteler = [
        'Yazar kim? (isim/unvan)',
        'Yayın tarihi belli mi?',
        'Hangi bilgiler veriliyor?',
        'Referans/kaynak gösteriliyor mu?',
        'Dil nasıl? (nesnel/duygusal)',
        'Başlık ne kadar iddialı?',
        'Görsel var mı? Nasıl?',
    ]
    data = [[cp('Değerlendirme Kriteri', True),
             cp('Kaynak A\n(Bilimsel Dergi)', True),
             cp('Kaynak B\n(Haber Sitesi)', True),
             cp('Kaynak C\n(Sosyal Medya)', True)]]
    for k in kriteler:
        data.append([cp(k), '', '', ''])
    t = Table(data, colWidths=[6.5 * cm, 3.5 * cm, 3.5 * cm, 3.5 * cm])
    t.setStyle(tablo_stili())
    e.append(t)
    e.append(vsp(0.1))

    e.append(Paragraph('Analiz Soruları', S_BSL))
    for s in [
        '1. Üç kaynak da aynı bilgiyi mi veriyor? Farklılıklar neler?',
        '2. Hangisi sana en güvenilir göründü? Neden?',
        '3. Bu haberde eksik/kayıp olduğunu düşündüğün bilgi var mı?',
        '4. Bir arkadaşına bu haberi anlatmak isteseydin hangi kaynağı kullanırdın? Neden?',
    ]:
        e.append(Paragraph(s, S_QUES))
        e.append(WritingLines(1, line_spacing=18))
    e.append(vsp(0.08))

    e.append(Paragraph(
        'Güvenilir Kaynağın 5 Özelliği — Her kaynağı işaretle: Var / Yok / Kısmen',
        S_BSL))
    data2 = [
        [cp('Özellik', True), cp('Kaynak A', True), cp('Kaynak B', True), cp('Kaynak C', True)],
        [cp('1. Yazar belli'), '', '', ''],
        [cp('2. Kaynağın kendisi güvenilir'), '', '', ''],
        [cp('3. Tarih güncel'), '', '', ''],
        [cp('4. Referans veriyor'), '', '', ''],
        [cp('5. Dengeli / olgusal dil'), '', '', ''],
    ]
    t2 = Table(data2, colWidths=[7.5 * cm, 3 * cm, 3 * cm, 3.5 * cm])
    t2.setStyle(tablo_stili())
    e.append(t2)
    return e


# ============================================================
# SAYFA 4: TEKNOLOJİ-TASARIM GÖZLÜĞÜYLE
# ============================================================

def ck4():
    e = []
    e += ck_baslik(4, 'TEKNOLOJİ-TASARIM GÖZLÜĞÜYLE', tur='Bireysel', sure='15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.08))
    e.append(Paragraph(
        'Yönerge: Bu derste öğrendiğin kavramları kullanarak 8-10 cümlelik bir metin yaz. '
        '<b>Şartlar:</b> Kendi cümlelerini kullan • En az 3 kavram geçsin '
        '(buluş, icat, keşif, bilim, teknik, tasarım, teknoloji, endüstri, STEAM, Endüstri 4.0/5.0, yapay zekâ, '
        'mimari/grafik/endüstriyel tasarım) • Kendi hayatından en az 2 örnek ver • Kendi görüşünü paylaş.',
        S_GOV))
    e.append(vsp(0.06))
    e.append(Paragraph(
        'Başlık: _________________________________  '
        '(Öneri: "Gözlüğümü Taktım", "Çevreme Yeni Bir Bakış", "Günlük Hayatımdaki Teknoloji ve Tasarım")',
        S_LABEL))
    e.append(vsp(0.05))
    e.append(WritingLines(11, line_spacing=19))
    e.append(vsp(0.1))

    e.append(Paragraph('Yazımı Kontrol Et — Metninde var mı? (Onay için işaretle)', S_BSL))
    items = [
        'En az 3 kavram geçiyor',
        'Kendi görüşümü belirttim',
        'Kendi hayatımdan en az 2 örnek var',
        '8-10 cümle arasında',
        'İmla kurallarına dikkat ettim',
        'Başlık koydum',
    ]
    rows = [[Paragraph(f'[ ]  {items[i]}', S_BODY),
             Paragraph(f'[ ]  {items[i+1]}', S_BODY)] for i in range(0, 6, 2)]
    kt = Table(rows, colWidths=[8.5 * cm, 8.5 * cm])
    kt.setStyle(TableStyle([
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ]))
    e.append(kt)
    e.append(vsp(0.08))
    e.append(Paragraph(
        'Kullandığım Kavramlar:  '
        '1. ________________  2. ________________  3. ________________',
        S_LABEL))
    return e


# ============================================================
# SAYFA 5: ÇÖZÜMLEME ŞABLONU
# ============================================================

def ck5():
    e = []
    e += ck_baslik(5, 'ÇÖZÜMLEME ŞABLONU', tur='Grup', sure='15 dk')
    e.append(grup_satiri())
    e.append(grup_uyeler())
    e.append(vsp(0.06))
    e.append(Paragraph(
        'Yönerge: Grubunuz bir tasarım ürünü seçecek. Bu ürünü detaylı şekilde inceleyerek '
        'aşağıdaki şablonu dolduracaksınız. Amaç: Bu üründe teknoloji nerede, tasarım nerede — ortaya çıkarmak.',
        S_GOV))
    e.append(vsp(0.06))

    satir = Table([[
        Paragraph('Ürün Adı: _______________________________', S_LABEL),
        Paragraph('Kategori:  [ ] Mimari/Çevre  [ ] Grafik Tasarım  [ ] Endüstriyel Tasarım', S_LABEL),
    ]], colWidths=[6 * cm, 11 * cm])
    satir.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    e.append(satir)
    e.append(Paragraph(
        'Kısa Tanım: _______________________________________________________________________________',
        S_LABEL))
    e.append(vsp(0.06))

    def ozellik_tablosu(baslik, satirlar):
        data = [[cp(baslik, True), '']]
        for s in satirlar:
            data.append([cp(s), ''])
        t = Table(data, colWidths=[7.5 * cm, 9.5 * cm])
        t.setStyle(TableStyle([
            ('SPAN',          (0, 0), (1, 0)),
            ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
            ('TEXTCOLOR',     (0, 0), (-1, 0), white),
            ('FONTSIZE',      (0, 0), (-1, -1), 7.5),
            ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
            ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
            ('LINEBELOW',     (0, 0), (-1, 0), 0.8, COLOR_PRIMARY),
            ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING',    (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING',   (0, 0), (-1, -1), 4),
            ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ]))
        return t

    e.append(ozellik_tablosu(
        'TASARIM UNSURLARI — Üründeki tasarım unsurlarını tespit et',
        ['Biçim / Form', 'Renk(ler)', 'Malzeme', 'Estetik Etkisi', 'Boyut / Ölçek', 'Kullanıcı Deneyimi']))
    e.append(vsp(0.06))
    e.append(ozellik_tablosu(
        'TEKNOLOJİ UNSURLARI — Üründeki teknoloji unsurlarını tespit et',
        ['Nasıl Çalışıyor?', 'Üretim Yöntemi', 'Kullanılan Teknikler', 'Hangi Bilimsel Bilgiye Dayanıyor?']))
    e.append(vsp(0.08))

    e.append(Paragraph(
        'Teknoloji ve Tasarım Nasıl Birleşmiş? — Bu üründe iki alan nerede kesişiyor?',
        S_QUES))
    e.append(WritingLines(2, line_spacing=18))

    e.append(Paragraph('Günlük Hayata Etkisi', S_BSL))
    for s in ['1. Bu ürün günlük hayatımızı nasıl kolaylaştırıyor?',
              '2. Bu ürün olmasaydı ne yapardık?',
              '3. Bu ürün sence geliştirilmeye açık mı? Nasıl?']:
        e.append(Paragraph(s, S_QUES))
        e.append(WritingLines(1, line_spacing=18))

    e.append(Paragraph('Sunum İçin Hazırlık — Sınıfa 3 dakikada neyi anlatacaksınız?', S_BSL))
    for i in range(1, 4):
        e.append(Paragraph(
            f'{i}. ___________________________________________________________________________',
            S_BODY))
    return e


# ============================================================
# SAYFA 6: VENN DİYAGRAMI KARŞILAŞTIRMA
# ============================================================

def ck6():
    e = []
    e += ck_baslik(6, 'VENN DİYAGRAMI KARŞILAŞTIRMA', tur='Bireysel', sure='10 dk')
    e.append(ad_satiri())
    e.append(vsp(0.08))
    e.append(Paragraph(
        'Yönerge: Bu derste incelenen üç tasarım alanından iki ürün seç. '
        'Venn diyagramı üzerinde bu iki ürünü karşılaştır. '
        'Yalnızca o ürüne ait özellikleri ilgili dairenin kendi alanına, '
        'her ikisinde de bulunanları orta alana yaz.',
        S_GOV))
    e.append(vsp(0.06))

    urun_t = Table([[
        Paragraph('Ürün 1: _______________________  Kategorisi: ________________', S_LABEL),
        Paragraph('Ürün 2: _______________________  Kategorisi: ________________', S_LABEL),
    ]], colWidths=[8.5 * cm, 8.5 * cm])
    urun_t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    e.append(urun_t)
    e.append(vsp(0.06))
    e.append(VennDiyagrami(17 * cm, 8 * cm))
    e.append(Paragraph(
        'İpucu: Ortak alana yazacağın özellikler iki tasarım türünün ortak ilkelerini gösterir '
        '(örn. estetik, işlevsellik, denge).',
        S_NOTE))
    e.append(vsp(0.1))

    e.append(Paragraph('Yorumlama Soruları', S_BSL))
    for s in [
        '1. İki üründe ne gibi beklenmedik ortaklıklar buldun?',
        '2. Ortak alandaki özellikler sana hangi tasarım ilkelerini hatırlatıyor?',
        '3. Farklılık alanındaki özellikler neden farklı? (İşlevleri mi, kullanıcıları mı farklı?)',
    ]:
        e.append(Paragraph(s, S_QUES))
        e.append(WritingLines(2, line_spacing=18))
    return e


# ============================================================
# SAYFA 7: ÇEVREMİ DEĞERLENDİRİYORUM
# ============================================================

def ck7():
    e = []
    e += ck_baslik(7, 'ÇEVREMİ DEĞERLENDİRİYORUM', tur='Bireysel', sure='15 dk')
    e.append(ad_satiri())
    e.append(vsp(0.06))
    e.append(Paragraph(
        'Yönerge: Çevrenizden bir ürün veya problem seçeceksiniz ve onu kendi '
        'belirlediğiniz ölçütlere göre değerlendireceksiniz.',
        S_GOV))
    e.append(vsp(0.05))

    e.append(Paragraph('ADIM 1: Alanını Seç', S_STEP))
    alanlar = [
        'Günlük tüketim malzemeleri (çanta, kalem, su şişesi vb.)',
        'Ulaşım (otobüs, bisiklet, servis, metro vb.)',
        'Mimari (okul binası, park, ev, AVM vb.)',
        'Yazılım/Uygulama (mobil uygulama, web sitesi)',
        'Lojistik (kargo, market taşıma, teslimat)',
        'Diğer: ______________________________',
    ]
    alan_rows = [[Paragraph(f'[ ]  {alanlar[i]}', S_BODY),
                  Paragraph(f'[ ]  {alanlar[i+1]}', S_BODY)] for i in range(0, 6, 2)]
    at = Table(alan_rows, colWidths=[8.5 * cm, 8.5 * cm])
    at.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    e.append(at)

    e.append(Paragraph('ADIM 2: Ürününü/Problemini Belirt', S_STEP))
    e.append(Paragraph(
        'Ürün / Problem: _________________________________  '
        'Neden bu ürünü seçtin? _________________________________',
        S_LABEL))

    e.append(Paragraph('ADIM 3: Ölçütleri Belirle (En az 4 ölçüt seç)', S_STEP))
    olcutler = [
        'İşlevsellik (Amacına uygun mu?)',   'Ergonomi (Kullanımı rahat mı?)',
        'Estetik (Göze hoş mu?)',             'Sürdürülebilirlik (Çevreye zarar var mı?)',
        'Ekonomiklik (Maliyeti makul mü?)',   'Erişilebilirlik (Herkes kullanabilir mi?)',
        'Güvenlik (Zarar verir mi?)',         'Dayanıklılık (Uzun ömürlü mü?)',
    ]
    olcut_rows = [[Paragraph(f'[ ]  {olcutler[i]}', S_BODY),
                   Paragraph(f'[ ]  {olcutler[i+1]}', S_BODY)] for i in range(0, 8, 2)]
    ot = Table(olcut_rows, colWidths=[8.5 * cm, 8.5 * cm])
    ot.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    e.append(ot)

    e.append(Paragraph('ADIM 4: Ölçme ve Puanlama (1 = Çok Zayıf, 5 = Çok İyi)', S_STEP))
    puan_data = [
        [cp('Ölçüt', True), cp('Puan (1-5)', True), cp('Gerekçe', True)],
    ] + [[cp('___________________________'), '', ''] for _ in range(5)] + [
        [cp('TOPLAM', True), cp('___ / ___', True), cp('Ortalama: ___', True)],
    ]
    pt = Table(puan_data, colWidths=[7 * cm, 3 * cm, 7 * cm])
    pt.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR',     (0, 0), (-1, 0), white),
        ('BACKGROUND',    (0, -1), (-1, -1), COLOR_LIGHT),
        ('FONTSIZE',      (0, 0), (-1, -1), 7.5),
        ('ALIGN',         (1, 0), (1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 0.8, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ]))
    e.append(pt)

    e.append(Paragraph('ADIM 5: Yargıda Bulun', S_STEP))
    e.append(Paragraph('Ürün Genel Değerlendirmesi + Önerin:', S_LABEL))
    e.append(WritingLines(3, line_spacing=18))
    e.append(vsp(0.06))
    e.append(Paragraph(
        'Sınıfa Sunum: Hangi ürünü seçtim  •  Hangi ölçütleri belirledim  •  '
        'Ne sonuç çıktı  •  Neyi önerdim',
        S_NOTE))
    return e


# ============================================================
# SAYFA 8: ÖZ DEĞERLENDİRME
# ============================================================

def ck8():
    e = []
    e += ck_baslik(8, 'ÖZ DEĞERLENDİRME', tur='Bireysel')
    e.append(ad_satiri())
    e.append(vsp(0.06))
    e.append(Paragraph(
        'Yönerge: Bu ünite boyunca kendini nasıl gördüğünü dürüstçe yaz. '
        'Bu form notla ölçülmez — amaç öğrenme yolculuğunu fark etmek.',
        S_GOV))
    e.append(vsp(0.06))

    e.append(Paragraph(
        'Ünite Boyunca Kendimi Nasıl Değerlendiriyorum? (1 = Hiç, 5 = Çok iyi)',
        S_BSL))
    puan_bas = [cp(str(i), True) for i in range(1, 6)]
    rt_data = [[cp('Öğrenme Alanı', True)] + puan_bas]
    for oz in ['Kavramları anladım', 'Grup çalışmalarına katıldım', 'Sorular sordum',
               'Araştırma yaptım', 'Kaynakları değerlendirdim', 'Kendi fikrimi oluşturdum',
               'Arkadaşlarımı dinledim', 'Görevlerimi zamanında tamamladım']:
        rt_data.append([cp(oz), '', '', '', '', ''])
    rt = Table(rt_data, colWidths=[9.5 * cm, 1.5 * cm, 1.5 * cm, 1.5 * cm, 1.5 * cm, 1.5 * cm])
    rt.setStyle(tablo_stili())
    e.append(rt)
    e.append(vsp(0.08))

    e.append(Paragraph('Kendime Sorular', S_BSL))
    for s in [
        '1. Bu ünitede en çok ne öğrendim?',
        '2. En zor gelen konu / etkinlik hangisiydi? Neden?',
        '3. En çok hangi etkinlikten keyif aldım?',
        '4. Arkadaşlarımın çalışmalarından ne öğrendim?',
        '5. Bir sonraki ünitede kendim için ne yapacağım?',
    ]:
        e.append(Paragraph(s, S_QUES))
        e.append(WritingLines(1, line_spacing=18))
    e.append(vsp(0.08))

    e.append(Paragraph(
        'Kendime Verdiğim Not: Bu ünitedeki çalışmalarımı genel olarak  ____  / 10  '
        'olarak değerlendiriyorum.',
        S_LABEL))
    e.append(vsp(0.06))
    e.append(Paragraph('Öğretmenime Mesajım (isteğe bağlı):', S_LABEL))
    e.append(WritingLines(2, line_spacing=18))
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
        title='1. Ünite - Çalışma Kâğıtları',
    )
    doc.unite_info = UI

    story = []
    sayfalar = [ck1, ck2, ck3, ck4, ck5, ck6, ck7, ck8]
    for i, ck in enumerate(sayfalar):
        story += ck()
        if i < len(sayfalar) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print('OK  U1_Calisma_Kagitlari_Kombine.pdf  (8 sayfa)')


if __name__ == '__main__':
    main()
