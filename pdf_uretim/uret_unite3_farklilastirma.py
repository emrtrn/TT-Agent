"""
3. Unite -- Farklilastirma (Adim 6) PDF Ureticisi
11 ayri PDF uretir: 5 Zenginlestirme + 6 Destekleme (units/7_sinif/unit3/ klasorune kaydeder).

Calistir: python pdf_uretim/uret_unite3_farklilastirma.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white, HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether,
)

from pdf_style import (
    register_fonts, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, DrawingBox, HorizontalLine,
)

register_fonts()

OUT        = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit3')
UNITE_INFO = '3. Ünite: Tasarım Odaklı Süreç  •  Teknoloji ve Tasarım  •  7. Sınıf'
TW         = 17 * cm

# ── Stiller ─────────────────────────────────────────────────────────────────

S_BAS  = ParagraphStyle('u3f_BAS',  fontName='TR-Bold',    fontSize=13, textColor=COLOR_PRIMARY,   leading=16)
S_ALT  = ParagraphStyle('u3f_ALT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     alignment=TA_RIGHT, leading=10)
S_BLM  = ParagraphStyle('u3f_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=6, spaceAfter=2)
S_LBL  = ParagraphStyle('u3f_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11, spaceAfter=1)
S_SML  = ParagraphStyle('u3f_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SML7 = ParagraphStyle('u3f_SML7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      leading=9.5)
S_SMBD = ParagraphStyle('u3f_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMIT = ParagraphStyle('u3f_SMIT', fontName='TR-Italic',  fontSize=7.5,textColor=COLOR_MUTED,     leading=10)
S_TH   = ParagraphStyle('u3f_TH',   fontName='TR-Bold',    fontSize=7.5,textColor=white,           alignment=TA_CENTER, leading=10)
S_TH7  = ParagraphStyle('u3f_TH7',  fontName='TR-Bold',    fontSize=7,  textColor=white,           alignment=TA_CENTER, leading=9.5)
S_TD   = ParagraphStyle('u3f_TD',   fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_TD7  = ParagraphStyle('u3f_TD7',  fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=9.5)
S_TDC  = ParagraphStyle('u3f_TDC',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=10.5)
S_TDC7 = ParagraphStyle('u3f_TDC7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=9.5)
S_TDBD = ParagraphStyle('u3f_TDBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_YON  = ParagraphStyle('u3f_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12)
S_KAZ  = ParagraphStyle('u3f_KAZ',  fontName='TR-Bold',    fontSize=8,  textColor=COLOR_PRIMARY,   leading=11, spaceBefore=4)

COLOR_DASHED = HexColor('#AAAAAA')

TABLE_BASE = [
    ('BACKGROUND',     (0, 0), (-1, 0),  COLOR_PRIMARY),
    ('LINEBELOW',      (0, 0), (-1, 0),  1, COLOR_SECONDARY),
    ('GRID',           (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('TOPPADDING',     (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING',  (0, 0), (-1, 0),  3),
    ('BOTTOMPADDING',  (0, 1), (-1, -1), 5),
    ('LEFTPADDING',    (0, 0), (-1, -1), 4),
    ('RIGHTPADDING',   (0, 0), (-1, -1), 4),
    ('VALIGN',         (0, 0), (-1, -1), 'TOP'),
]

# ── Yardımcı Fonksiyonlar ────────────────────────────────────────────────────

def make_doc(fname, title):
    doc = SimpleDocTemplate(
        os.path.join(OUT, fname),
        pagesize=A4,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        leftMargin=2*cm,  rightMargin=2*cm,
        title=title,
    )
    doc.doc_title  = title
    doc.unite_info = UNITE_INFO
    return doc

def sp(n=4):
    return Spacer(1, n)

def blm(text):
    return Paragraph(text, S_BLM)

def etiket_baslik(tur, ad, alt=''):
    t = Table([[
        Paragraph(f'<b>{tur} — {ad}</b>', S_BAS),
        Paragraph(alt, S_ALT),
    ]], colWidths=[11*cm, 6*cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (0,0),(-1,0),  1.5, COLOR_PRIMARY),
        ('TOPPADDING',    (0,0),(-1,-1), 0),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(0,0),   0),
        ('RIGHTPADDING',  (-1,0),(-1,0), 0),
    ]))
    return t

def ogrenci_satiri():
    t = Table([[
        Paragraph('<b>Adı Soyadı:</b>', S_LBL), '',
        Paragraph('<b>Tarih:</b>',       S_LBL), '',
    ]], colWidths=[2.7*cm, 9.8*cm, 1.5*cm, 3*cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(-1,-1), 2),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
    ]))
    return t

def gorev_kutu(metin):
    t = Table([[Paragraph(metin, S_YON)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT),
        ('BOX',           (0,0),(-1,-1), 0.5, COLOR_ACCENT),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('RIGHTPADDING',  (0,0),(-1,-1), 8),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
    ]))
    return t

def ipucu_kutu(metin):
    t = Table([[Paragraph(metin, S_SML)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT_GREY),
        ('BOX',           (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('RIGHTPADDING',  (0,0),(-1,-1), 8),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
    ]))
    return t

def yon_adim(no, metin):
    t = Table([[
        Paragraph(f'<b>{no}.</b>', S_SMBD),
        Paragraph(metin, S_SML),
    ]], colWidths=[0.6*cm, 16.4*cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(0,0),   0),
        ('LEFTPADDING',   (1,0),(1,0),   4),
        ('RIGHTPADDING',  (0,0),(-1,-1), 0),
    ]))
    return t

def degerlendirme_tablo(satirlar, toplam=100):
    hdr  = [Paragraph('Ölçüt', S_TH), Paragraph('Puan', S_TH)]
    data = [hdr]
    for olcut, puan in satirlar:
        data.append([Paragraph(olcut, S_TD), Paragraph(str(puan), S_TDC)])
    data.append([Paragraph('<b>TOPLAM</b>', S_TDBD), Paragraph(f'<b>{toplam}</b>', S_TDC)])
    t = Table(data, colWidths=[14.5*cm, 2.5*cm])
    st = list(TABLE_BASE)
    st += [
        ('BACKGROUND', (0,-1),(-1,-1), COLOR_VERY_LIGHT),
        ('LINEABOVE',  (0,-1),(-1,-1), 1, COLOR_PRIMARY),
        ('FONT',       (0,-1),(-1,-1), 'TR-Bold', 8),
    ]
    t.setStyle(TableStyle(st))
    return t

def bicim_tablo(sure, teslim, format_str=''):
    rows = []
    if format_str:
        rows.append([Paragraph('<b>Format</b>', S_SMBD), Paragraph(format_str, S_SML)])
    rows.append([Paragraph('<b>Süre</b>',   S_SMBD), Paragraph(sure,   S_SML)])
    rows.append([Paragraph('<b>Teslim</b>', S_SMBD), Paragraph(teslim, S_SML)])
    t = Table(rows, colWidths=[2*cm, 15*cm])
    t.setStyle(TableStyle([
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('BACKGROUND',    (0,0),(0,-1),  COLOR_VERY_LIGHT),
        ('TOPPADDING',    (0,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 3),
        ('LEFTPADDING',   (0,0),(-1,-1), 4),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
    ]))
    return t

def kontrol_satiri(madde):
    t = Table([[
        Paragraph(madde, S_TD7),
        Paragraph('( )', S_TDC7),
        Paragraph('( )', S_TDC7),
        Paragraph('( )', S_TDC7),
    ]], colWidths=[13.7*cm, 1.1*cm, 1.1*cm, 1.1*cm])
    t.setStyle(TableStyle([
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0,0),(-1,-1), [white]),
        ('TOPPADDING',    (0,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(-1,-1), 4),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
    ]))
    return t

def kontrol_tablo(baslik, maddeler):
    hdr = [
        Paragraph(f'<b>{baslik}</b>', S_TH7),
        Paragraph('V', S_TH7),
        Paragraph('/\\', S_TH7),
        Paragraph('X', S_TH7),
    ]
    data = [hdr]
    for m in maddeler:
        data.append([Paragraph(m, S_TD7),
                     Paragraph('( )', S_TDC7),
                     Paragraph('( )', S_TDC7),
                     Paragraph('( )', S_TDC7)])
    t = Table(data, colWidths=[13.7*cm, 1.1*cm, 1.1*cm, 1.1*cm])
    t.setStyle(TableStyle(TABLE_BASE))
    return t

def yazma_alani(etiket, n=2):
    return [Paragraph(f'<b>{etiket}:</b>', S_LBL), WritingLines(n, 15), sp(3)]

# ── ZENGİNLEŞTİRME ETKİNLİKLERİ ─────────────────────────────────────────────

def zen1():
    """Etkinlik 1: Gerçek Sosyal Probleme Tam Design Thinking"""
    doc   = make_doc('Zen1_Gercek_DT_Projesi.pdf', 'Zenginleştirme Etkinlik 1 — Gerçek Sosyal Probleme Tam Design Thinking')
    story = []

    story += [
        etiket_baslik('Zenginleştirme Etkinlik 1', 'Gerçek Sosyal Probleme Tam Design Thinking',
                      'ZENGİNLEŞTİRME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(8),
        blm('Görev Tanımı'),
        sp(3),
        gorev_kutu(
            'Ders boyunca Design Thinking döngüsünü bir öğrenme konusu olarak gördün. '
            'Şimdi bu döngüyü gerçek bir toplumsal sorun için baştan sona kendin uygulayacaksın. '
            'Seçeceğin problem sınıfta çözülecek kadar küçük olmamalı — '
            'ama tek başına çözülemeyecek kadar büyük de olmamalı. '
            'Amaç: gerçek bir empati kurarak, gerçek bir çözüm önerisi üretmek.'
        ),
        sp(8),
        blm('Yönerge'),
        sp(3),
        yon_adim(1, 'Okulun, mahallenin ya da ailen içinden gerçek, gözlemlediğin bir problemi seç.'),
        sp(2),
        yon_adim(2, 'Problemi yaşayan en az 2 farklı kişiyle kısa görüşme veya gözlem yap. Empati haritalarını doldur.'),
        sp(2),
        yon_adim(3, '"Kullanıcı ... ihtiyaç duyar, çünkü ..." formatında net bir problem tanımı yaz.'),
        sp(2),
        yon_adim(4, 'En az 8 fikir üret (Crazy 8). Fikir seçim matrisiyle en güçlü fikri belirle.'),
        sp(2),
        yon_adim(5, 'Düşük maliyetli bir prototip ya da hizmet taslağı hazırla.'),
        sp(2),
        yon_adim(6, 'Prototipi en az 1 gerçek kullanıcıyla test et, geri bildirim al.'),
        sp(2),
        yon_adim(7, 'Geri bildirime göre en az 1 iyileştirme yap.'),
        sp(2),
        yon_adim(8, '5 dakikalık sunum yap: "Problemi nasıl seçtim, ne öğrendim, ne değiştirdim?"'),
        sp(8),
        KeepTogether([
            blm('Zorunlu Öğeler'),
            sp(3),
            Table([
                [Paragraph('Zorunlu Öğe', S_TH), Paragraph('Açıklama', S_TH)],
                [Paragraph('Problem tespiti formu', S_TD),
                 Paragraph('Gerçek gözlem veya görüşme notları içermelidir', S_SML)],
                [Paragraph('2 empati haritası', S_TD),
                 Paragraph('Farklı kullanıcılar için doldurulmuş', S_SML)],
                [Paragraph('Problem tanımı', S_TD),
                 Paragraph('"Kullanıcı / İhtiyaç / Çünkü" formatında yazılmış', S_SML)],
                [Paragraph('Crazy 8 + fikir matrisi', S_TD),
                 Paragraph('En az 8 fikir ve seçim gerekçesi', S_SML)],
                [Paragraph('Prototip', S_TD),
                 Paragraph('Fotoğraf veya detaylı eskiz', S_SML)],
                [Paragraph('Test notu', S_TD),
                 Paragraph('Kim test etti, ne söyledi, ne değiştirdim', S_SML)],
                [Paragraph('5 dk sözlü sunum', S_TD),
                 Paragraph('Süreç ve yansıtma anlatımı', S_SML)],
            ], colWidths=[5*cm, 12*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Biçim ve Teslim'),
            sp(3),
            bicim_tablo('2–3 hafta', 'Sınıfa sunum + öğretmene süreç dosyası',
                        'Süreç dosyası (tüm aşamalar) + sözlü sunum'),
        ]),
        sp(8),
        KeepTogether([
            blm('Değerlendirme'),
            sp(3),
            degerlendirme_tablo([
                ('Problemin gerçekliği ve empatinin derinliği', 25),
                ('Design Thinking aşamalarına eksiksiz uyum', 30),
                ('Çözümün özgünlüğü ve uygulanabilirliği', 25),
                ('Sunum akıcılığı ve yansıtmanın gücü', 20),
            ]),
        ]),
        sp(8),
        ipucu_kutu(
            'İpuçları: Mükemmel bir ürün değil, doğru soruya cevap aramak bu etkinliğin özüdür. '
            'Prototip kâğıt, karton ya da dijital bir taslak da olabilir — pahalı malzeme şart değil. '
            'Test ederken "Ne kadar beğendin?" değil "Neyi değiştirirdin?" sorusunu sor.'
        ),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def zen2():
    """Etkinlik 2: Tasarım Portföyü"""
    doc   = make_doc('Zen2_Tasarim_Portfoyu.pdf', 'Zenginleştirme Etkinlik 2 — Tasarım Portföyü')
    story = []

    story += [
        etiket_baslik('Zenginleştirme Etkinlik 2', 'Tasarım Portföyü',
                      'ZENGİNLEŞTİRME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(8),
        blm('Görev Tanımı'),
        sp(3),
        gorev_kutu(
            'Bir tasarımcı; daha önce ne ürettiğini, nasıl düşündüğünü ve nasıl geliştiğini gösteren '
            'bir portföy tutar. Bu ünite boyunca ürettiğin tüm çalışmalar senin tasarım portföyünün '
            'ilk sayfalarıdır. Portföyünü oluşturarak sadece çalışmalarını derlemeyeceksin — '
            'her adımın arkasındaki düşünceyi görünür kılacaksın.'
        ),
        sp(8),
        blm('Yönerge'),
        sp(3),
        yon_adim(1, 'Ünite boyunca doldurduğun tüm çalışma kâğıtlarını (ÇK1–ÇK11) bir dosyaya topla.'),
        sp(2),
        yon_adim(2, 'Her çalışma kâğıdı için 1 yansıtma notu ekle: "Bu adımda ne öğrendim? Ne değiştirirdim şimdi?"'),
        sp(2),
        yon_adim(3, 'Süreç boyunca en anlamlı bulduğun 3 anı/dönüm noktasını seç. Her biri için yarım sayfa yaz: "Neden önemliydi?"'),
        sp(2),
        yon_adim(4, 'Prototipinin fotoğrafını veya detaylı eskizini portföye ekle.'),
        sp(2),
        yon_adim(5, 'Kapak sayfası tasarla: Adın, bir tasarım sloganın ve portföyünü yansıtan bir görsel.'),
        sp(2),
        yon_adim(6, 'Sonuç sayfasına şunu yaz: "Design Thinking bana ne öğretti?" (en az 200 kelime)'),
        sp(8),
        KeepTogether([
            blm('Zorunlu Öğeler'),
            sp(3),
            Table([
                [Paragraph('Öğe', S_TH), Paragraph('Detay', S_TH)],
                [Paragraph('Çalışma kâğıtları', S_TD),
                 Paragraph('ÇK1–ÇK11 (en az 7\'si) + her biri için yansıtma notu', S_SML)],
                [Paragraph('3 dönüm noktası', S_TD),
                 Paragraph('Toplam ~1,5 sayfa yazılı', S_SML)],
                [Paragraph('Prototip belgesi', S_TD),
                 Paragraph('Fotoğraf veya detaylı eskiz', S_SML)],
                [Paragraph('Kapak tasarımı', S_TD),
                 Paragraph('Özgün, ad + slogan + görsel içermeli', S_SML)],
                [Paragraph('Sonuç yazısı', S_TD),
                 Paragraph('En az 200 kelime', S_SML)],
            ], colWidths=[4*cm, 13*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Biçim ve Teslim'),
            sp(3),
            bicim_tablo('Ünite boyunca sürekli; final teslim 10. derste',
                        'Öğretmene veya sınıf sergisine',
                        'Fiziksel dosya (klasör/defter) veya dijital PDF'),
        ]),
        sp(8),
        KeepTogether([
            blm('Değerlendirme'),
            sp(3),
            degerlendirme_tablo([
                ('Çalışmaların eksiksiz toplanması', 20),
                ('Yansıtma notlarının derinliği ve dürüstlüğü', 30),
                ('Dönüm noktası yazılarının anlamı', 25),
                ('Kapak ve genel düzenin özgünlüğü', 10),
                ('Sonuç yazısının kavramsal gücü', 15),
            ]),
        ]),
        sp(8),
        ipucu_kutu(
            'İpuçları: Portföy "güzel görünen" değil, "gerçeği gösteren" belgedir. Hataları da ekle — büyüme orada görünür. '
            'Yansıtma notları "güzel oldu" yerine "şunu fark ettim" ile başlamalı.'
        ),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def zen3():
    """Etkinlik 3: IDEO ve Frog Design Araştırması"""
    doc   = make_doc('Zen3_IDEO_Frog_Arastirma.pdf', 'Zenginleştirme Etkinlik 3 — IDEO ve Frog Design')
    story = []

    story += [
        etiket_baslik('Zenginleştirme Etkinlik 3', 'IDEO ve Frog Design — Profesyoneller Nasıl Düşünür?',
                      'ZENGİNLEŞTİRME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(8),
        blm('Görev Tanımı'),
        sp(3),
        gorev_kutu(
            'Dünyanın önde gelen tasarım şirketleri — IDEO ve Frog Design — Design Thinking\'i hayata geçiren firmalardır. '
            'IDEO sağlıktan eğitime, Frog Design ise teknolojiden sürdürülebilirliğe kadar pek çok alanda '
            '"insan merkezli tasarım" anlayışıyla ürünler ve sistemler geliştirmiştir. '
            'Bu etkinlikte bu iki firmanın yaklaşımını araştırarak kendi tasarım felsefeni geliştirmen için ilham alacaksın.'
        ),
        sp(8),
        blm('Yönerge'),
        sp(3),
        yon_adim(1, 'IDEO ve Frog Design hakkında araştırma yap: Her firmanın tasarım felsefesini ve çalışma yöntemini öğren.'),
        sp(2),
        yon_adim(2, 'Her firmadan 1 gerçek proje incele: "Hangi problemi çözdüler? Nasıl?" sorusunu yanıtla.'),
        sp(2),
        yon_adim(3, 'İki firmanın yaklaşımını karşılaştır: Benzerlikler ve farklılıklar (en az 5 madde).'),
        sp(2),
        yon_adim(4, '"Hangi firmanın yaklaşımı sana daha yakın geliyor? Neden?" sorusunu cevapla.'),
        sp(2),
        yon_adim(5, 'Kendi 3 maddelik "Tasarım Manifestom"u yaz: "Tasarlarken şunlara inanıyorum: ..."'),
        sp(2),
        yon_adim(6, 'Sunumunu hazırla: Sınıfa 5 dakika.'),
        sp(8),
        KeepTogether([
            blm('Araştırma Şablonu'),
            sp(3),
            Table([
                [Paragraph('', S_TH7),
                 Paragraph('IDEO', S_TH),
                 Paragraph('Frog Design', S_TH)],
                [Paragraph('Kuruluş yılı / ülke', S_TD),
                 Paragraph('', S_SML),
                 Paragraph('', S_SML)],
                [Paragraph('Tasarım felsefesi', S_TD),
                 Paragraph('', S_SML),
                 Paragraph('', S_SML)],
                [Paragraph('İncelediğim proje', S_TD),
                 Paragraph('', S_SML),
                 Paragraph('', S_SML)],
                [Paragraph('Çözdükleri problem', S_TD),
                 Paragraph('', S_SML),
                 Paragraph('', S_SML)],
                [Paragraph('Nasıl çözdüler?', S_TD),
                 Paragraph('', S_SML),
                 Paragraph('', S_SML)],
                [Paragraph('Bence en güçlü yanı', S_TD),
                 Paragraph('', S_SML),
                 Paragraph('', S_SML)],
            ], colWidths=[4*cm, 6.5*cm, 6.5*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWBACKGROUNDS', (0,1),(-1,-1), [white, COLOR_VERY_LIGHT_GREY]),
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 1.2*cm),
            ])),
        ]),
        sp(8),
        KeepTogether([
            blm('Tasarım Manifestom'),
            sp(3),
            Paragraph('Araştırma sonunda kendi 3 maddelik manifestonu yaz:', S_SML),
            sp(4),
            Paragraph('<b>Tasarlarken şunlara inanıyorum:</b>', S_SMBD),
            sp(4),
        ] + yazma_alani('1. Madde', 1)
          + yazma_alani('2. Madde', 1)
          + yazma_alani('3. Madde', 1)),
        sp(6),
        KeepTogether([
            blm('Biçim ve Teslim'),
            sp(3),
            bicim_tablo('1–2 hafta', 'Sınıf sunumu veya öğretmene',
                        'Araştırma notu (A4) + sözlü sunum veya poster'),
        ]),
        sp(6),
        KeepTogether([
            blm('Değerlendirme'),
            sp(3),
            degerlendirme_tablo([
                ('Araştırmanın kapsamı ve doğruluğu', 30),
                ('Karşılaştırmanın analitik derinliği', 25),
                ('Tasarım Manifestosunun özgünlüğü', 25),
                ('Sunum ya da posterin iletişim gücü', 20),
            ]),
        ]),
        sp(6),
        ipucu_kutu(
            'Önerilen kaynaklar: IDEO.org — hizmetler ve açık kaynak araçlar  |  '
            'TED.com — "David Kelley: How to build your creative confidence" (IDEO kurucusu)  |  '
            'Frog Design şirket web sitesi ve "Design Mind" blogu'
        ),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def zen4():
    """Etkinlik 4: Sürdürülebilir Malzeme Karşılaştırma Raporu"""
    doc   = make_doc('Zen4_Surdurulebilir_Malzeme.pdf', 'Zenginleştirme Etkinlik 4 — Sürdürülebilir Malzeme')
    story = []

    story += [
        etiket_baslik('Zenginleştirme Etkinlik 4', 'Sürdürülebilir Malzeme Karşılaştırma Raporu',
                      'ZENGİNLEŞTİRME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(8),
        blm('Görev Tanımı'),
        sp(3),
        gorev_kutu(
            'Bir prototip yaparken seçtiğimiz malzeme yalnızca "ne kadar işe yarıyor" sorusuna değil, '
            '"dünyaya ne maliyeti var" sorusuna da yanıt vermek zorundadır. '
            'Sürdürülebilirlik — doğayı tüketmeden, geri dönüştürülebilir ve uzun ömürlü çözümler üretmek — '
            'modern tasarımın merkezindedir. Bu etkinlikte en az 3 farklı malzemeyi karşılaştıracak '
            've bir "Malzeme Tavsiye Raporu" hazırlayacaksın.'
        ),
        sp(8),
        blm('Yönerge'),
        sp(3),
        yon_adim(1, 'Şu kategorilerden en az 3 malzeme seç: Plastik — Ahşap — Alüminyum — Geri dönüştürülmüş kâğıt — Doğal elyaf (jüt, pamuk) — Biyobozunur plastik.'),
        sp(2),
        yon_adim(2, 'Her malzeme için şu kriterleri araştır: üretim kaynağı, yaşam döngüsü, geri dönüşüm oranı, karbon izi, maliyet.'),
        sp(2),
        yon_adim(3, 'Karşılaştırma matrisini doldur (aşağıdaki tablo).'),
        sp(2),
        yon_adim(4, '"Bir okul atölyesi için en sürdürülebilir 2 malzeme hangisi?" sorusunu gerekçeyle cevapla.'),
        sp(2),
        yon_adim(5, 'Raporunu bir A4 sayfasında özetle — öğretmenin veliler toplantısında kullanabileceği biçimde.'),
        sp(8),
        KeepTogether([
            blm('Karşılaştırma Matrisi'),
            sp(3),
            Table([
                [Paragraph('Malzeme', S_TH7),
                 Paragraph('Üretim Kaynağı', S_TH7),
                 Paragraph('Yaşam Döngüsü', S_TH7),
                 Paragraph('Geri Dönüşüm', S_TH7),
                 Paragraph('Karbon İzi', S_TH7),
                 Paragraph('Maliyet', S_TH7)],
                [Paragraph('1.', S_TD7), Paragraph('', S_SML7), Paragraph('', S_SML7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7), Paragraph('', S_SML7)],
                [Paragraph('2.', S_TD7), Paragraph('', S_SML7), Paragraph('', S_SML7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7), Paragraph('', S_SML7)],
                [Paragraph('3.', S_TD7), Paragraph('', S_SML7), Paragraph('', S_SML7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7), Paragraph('', S_SML7)],
            ], colWidths=[2.5*cm, 3*cm, 3*cm, 2.5*cm, 3*cm, 3*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 1.4*cm),
            ])),
        ]),
        sp(8),
    ] + yazma_alani('Sonuç ve Tavsiyem: En sürdürülebilir 2 malzeme ve gerekçem', n=4) + [
        sp(6),
        KeepTogether([
            blm('Biçim ve Teslim'),
            sp(3),
            bicim_tablo('1 hafta', 'Öğretmene',
                        'Araştırma raporu (A4, 2–3 sayfa) + 1 sayfa özet'),
        ]),
        sp(6),
        KeepTogether([
            blm('Değerlendirme'),
            sp(3),
            degerlendirme_tablo([
                ('Araştırmanın kapsamı ve kaynak güvenilirliği', 30),
                ('Karşılaştırma matrisinin tamlığı', 25),
                ('Sonuç ve tavsiyenin gerekçeli olması', 30),
                ('Özet raporun iletişim kalitesi', 15),
            ]),
        ]),
        sp(6),
        ipucu_kutu(
            'Hatırla: "Sürdürülebilir" ile "geri dönüştürülebilir" aynı anlama gelmiyor — farkını araştır. '
            'Maliyet yalnızca para değildir: zaman ve çevre maliyeti de var.'
        ),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def zen5():
    """Etkinlik 5: Çeliştirici Tasarım Senaryosu"""
    doc   = make_doc('Zen5_Celisme_Analizi.pdf', 'Zenginleştirme Etkinlik 5 — Çeliştirici Tasarım Senaryosu')
    story = []

    story += [
        etiket_baslik('Zenginleştirme Etkinlik 5', 'Çeliştirici Tasarım Senaryosu — Hangisi Daha İyi?',
                      'ZENGİNLEŞTİRME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(8),
        blm('Görev Tanımı'),
        sp(3),
        gorev_kutu(
            'Tasarım sürecinde bazen iki farklı tasarımcı aynı probleme tamamen farklı çözümler üretir. '
            'İkisi de empati kurmuş, test etmiş, revize etmiştir. Yine de sonuçlar birbirinden çok farklıdır. '
            'Bu durumda "kim haklı?" Sana verilen iki farklı tasarım senaryosunu Design Thinking açısından analiz et. '
            'Her ikisini savun. Sonra kendi değerlendirmeni yaz.'
        ),
        sp(6),
        blm('Senaryo: Okul Bahçesindeki Bekleme Sorunu'),
        sp(3),
        Paragraph(
            '<b>Problem:</b> 40 dakika teneffüs boyunca öğrenciler okul bahçesinde oturacak yer bulamıyor, '
            'özellikle kış aylarında.',
            S_SML
        ),
        sp(6),
        Table([
            [Paragraph('Çözüm A — Ahmet\'in Tasarımı', S_TH),
             Paragraph('Çözüm B — Elif\'in Tasarımı', S_TH)],
            [Paragraph(
                'Ahşaptan, rüzgâr kesen cam panelli, 6 kişilik kapalı bekleme kabini. '
                'Malzeme maliyeti yüksek ama az yer kaplıyor. Test sonucu: "sıcak ama karanlık." '
                'İyileştirme: cam panel yüzeyini artırmış. Ergonomi: iyi. Sürdürülebilirlik: orta.',
                S_SML),
             Paragraph(
                'Eski ahşap paletlerden, sınıfların boyadığı modüler oturma köşeleri. '
                'Her köşe farklı sınıfın sorumluluğunda. Malzeme: düşük maliyetli, geri dönüşümlü. '
                'Test sonucu: "oturmak güzel ama soğuktan korunmuyor." İyileştirme: bez tenteler eklemiş. '
                'Ergonomi: orta. Sürdürülebilirlik: yüksek.',
                S_SML)],
        ], colWidths=[8.5*cm, 8.5*cm],
        style=TableStyle([
            ('BACKGROUND',    (0,0),(-1,0), COLOR_PRIMARY),
            ('GRID',          (0,0),(-1,-1), 0.5, COLOR_LIGHT_GREY),
            ('TOPPADDING',    (0,0),(-1,-1), 4),
            ('BOTTOMPADDING', (0,0),(-1,-1), 6),
            ('LEFTPADDING',   (0,0),(-1,-1), 6),
            ('RIGHTPADDING',  (0,0),(-1,-1), 6),
            ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ])),
        sp(8),
        KeepTogether([
            blm('Analiz Tablosu — Her İki Tasarımı Karşılaştır'),
            sp(3),
            Table([
                [Paragraph('Kriter', S_TH7),
                 Paragraph('Çözüm A — Ahmet', S_TH7),
                 Paragraph('Çözüm B — Elif', S_TH7)],
                [Paragraph('Empati gücü', S_TD7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7)],
                [Paragraph('Çözümün özgünlüğü', S_TD7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7)],
                [Paragraph('Test ve revize kalitesi', S_TD7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7)],
                [Paragraph('Ergonomi', S_TD7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7)],
                [Paragraph('Sürdürülebilirlik', S_TD7),
                 Paragraph('', S_SML7), Paragraph('', S_SML7)],
            ], colWidths=[3.5*cm, 6.75*cm, 6.75*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 1.2*cm),
            ])),
        ]),
        sp(8),
    ] + yazma_alani('Çözüm A için savunmam ("Bu tasarım şu açılardan güçlü...")', n=3) + [
        sp(4),
    ] + yazma_alani('Çözüm B için savunmam', n=3) + [
        sp(4),
    ] + yazma_alani('Kendi değerlendirmem — hangisini seçerdim ve neden?', n=5) + [
        sp(6),
        KeepTogether([
            blm('Biçim ve Teslim'),
            sp(3),
            bicim_tablo('1–2 ders (ev ödevi olarak da tamamlanabilir)', 'Öğretmene',
                        'A4 yazılı çalışma'),
        ]),
        sp(6),
        KeepTogether([
            blm('Değerlendirme'),
            sp(3),
            degerlendirme_tablo([
                ('Her iki analizin Design Thinking kriterlerine uygunluğu', 30),
                ('Savunma ve eleştirilerin gerekçeli olması', 30),
                ('Kişisel değerlendirmenin analitik derinliği', 30),
                ('Yazılı anlatımın netliği', 10),
            ]),
        ]),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


# ── DESTEKLEME MATERYALLERİ ───────────────────────────────────────────────────

def des1():
    """Materyal 1: Görsel Design Thinking Döngüsü Kartı"""
    doc   = make_doc('Des1_DT_Dongusu_Karti.pdf', 'Destekleme Materyal 1 — Design Thinking Döngüsü Kartı')
    story = []

    adimlar = [
        ('1', 'Problem Tespiti',
         'Çevremde gerçekten var olan bir sorunu fark ediyorum.',
         '"Kimin hayatını kolaylaştırabilir ya da güzelleştirebilirim?"'),
        ('2', 'Empati',
         'Problemi yaşayan kişinin yerine geçerek duygularını, ihtiyaçlarını ve zorluklarını anlıyorum.',
         '"Bu kişi ne hissediyor? Ne istiyor? Neyi zor buluyor?"'),
        ('3', 'Fikir Üretimi',
         'Sorun için olabildiğince çok ve farklı fikir üretiyorum. Hiçbir fikri baştan elemiyorum.',
         '"En saçma fikrim bile bu listeye giriyor mu?"'),
        ('4', 'Eskiz / Taslak',
         'En iyi fikrimi çiziyorum. Malzemeleri ve nasıl yapılacağını planlıyorum.',
         '"Bunu gerçekten yapabilir miyim? Neye ihtiyacım var?"'),
        ('5', 'Uygulama / Prototip',
         'Fikri somut bir nesneye, makete ya da modele dönüştürüyorum.',
         '"Bu prototip problemi çözüyor mu? Kullanıcı bunu kullanabilir mi?"'),
        ('6', 'Test / Geri Bildirim',
         'Prototipi gerçek bir kişiye gösteriyor ya da denettiriyorum. Geri bildirimini not alıyorum.',
         '"Neyin işe yaradığını öğrendim? Neyin değişmesi gerekiyor?"'),
        ('7', 'Revize',
         'Geri bildirimlere göre tasarımımı düzeltiyorum. Süreç burada bitmez — tekrar test edilebilir.',
         '"Bu değişiklik kullanıcı için gerçekten daha iyi mi?"'),
    ]

    data = [[
        Paragraph('Adım', S_TH7),
        Paragraph('Ne Yapıyorum?', S_TH),
        Paragraph('Anahtar Sorum', S_TH),
    ]]
    for no, ad, yapiyorum, sorum in adimlar:
        data.append([
            Paragraph(f'<b>{no}\n{ad}</b>', S_TDC7),
            Paragraph(yapiyorum, S_TD7),
            Paragraph(f'<i>{sorum}</i>', S_SMIT),
        ])

    story += [
        etiket_baslik('Destekleme Materyal 1', 'Design Thinking Döngüsü — 7 Adım Kartı',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        gorev_kutu(
            'Bu kart ünite boyunca masanda durabilir. Her adımda hangi soruyu sormak gerektiğini hatırlatır. '
            'A5 boyutunda baskı alarak lamineleyebilirsin.'
        ),
        sp(8),
        Table(data, colWidths=[3.2*cm, 7.9*cm, 5.9*cm],
              style=TableStyle(TABLE_BASE + [
                  ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 1.2*cm),
              ])),
        sp(8),
        blm('Döngü İpuçları'),
        sp(3),
        Table([
            [Paragraph('Dikkat!', S_TH), Paragraph('Neden?', S_TH)],
            [Paragraph('Adımlar sırayla ilerler ama geri dönmek mümkündür', S_TD),
             Paragraph('Tasarım doğrusal değil, döngüseldir', S_SML)],
            [Paragraph('Empati atlanırsa çözüm kullanıcıyı değil, seni tatmin eder', S_TD),
             Paragraph('Asıl kullanıcı senin dışındadır', S_SML)],
            [Paragraph('Test aşamasında "beğendin mi?" değil "ne değiştirirdin?" sor', S_TD),
             Paragraph('Eleştiri iyileştirmenin yakıtıdır', S_SML)],
        ], colWidths=[8.5*cm, 8.5*cm],
        style=TableStyle(TABLE_BASE)),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def des2():
    """Materyal 2: Adım Adım Prototip Yapım Rehberi"""
    doc   = make_doc('Des2_Prototip_Rehberi.pdf', 'Destekleme Materyal 2 — Adım Adım Prototip Yapım Rehberi')
    story = []

    story += [
        etiket_baslik('Destekleme Materyal 2', 'Adım Adım Prototip Yapım Rehberi',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(6),
        gorev_kutu(
            'Prototip yapmak zor görünebilir. Ama bunu adım adım yaparsak kolaylaşır. '
            'Her adımı tamamladığında kutuyu işaretle.'
        ),
        sp(8),
        blm('Başlamadan Önce: Eskizini Kontrol Et'),
        sp(3),
        Table([
            [Paragraph('Soru', S_TH), Paragraph('Cevabım', S_TH)],
            [Paragraph('Neyi yapmaya çalışıyorum? (1 cümle)', S_TD),
             Paragraph('', S_SML)],
            [Paragraph('Hangi malzemeleri kullanacağım?', S_TD),
             Paragraph('', S_SML)],
            [Paragraph('Ne kadar zamana ihtiyacım var?', S_TD),
             Paragraph('', S_SML)],
            [Paragraph('Yardıma ihtiyacım olacak mı?', S_TD),
             Paragraph('', S_SML)],
        ], colWidths=[7*cm, 10*cm],
        style=TableStyle(TABLE_BASE + [
            ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 0.9*cm),
        ])),
        sp(8),
        KeepTogether([
            blm('Adım 1 — Malzeme Hazırla'),
            sp(3),
            Paragraph('Eskizinde yazan malzemeleri masana koy. Eksik malzeme için alternatif düşün.', S_SML),
            sp(4),
        ] + yazma_alani('Eksik malzeme', 1)
          + yazma_alani('Alternatifim', 1)
          + [
            Table([[
                Paragraph('[ ]', S_SMBD),
                Paragraph('<b>Malzemelerim hazır.</b>', S_SML),
            ]], colWidths=[0.6*cm, 16.4*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(0,0), 0),  ('LEFTPADDING', (1,0),(1,0), 4),
                ('RIGHTPADDING', (0,0),(-1,-1), 0), ('VALIGN', (0,0),(-1,-1), 'TOP'),
            ])),
        ]),
        sp(8),
        KeepTogether([
            blm('Adım 2 — Kaba Yapıyı Kur'),
            sp(3),
            Paragraph(
                'Önce ölçü, renk veya detay düşünme. Sadece nesnenin dış iskeletini oluştur. '
                '<i>Mükemmel değil, işlevsel olsun. Bu bir prototip.</i>',
                S_SML),
            sp(4),
        ] + yazma_alani('Yaptığımda en çok zorlandığım şey', 1)
          + [
            Table([[
                Paragraph('[ ]', S_SMBD),
                Paragraph('<b>Kaba yapı tamam.</b>', S_SML),
            ]], colWidths=[0.6*cm, 16.4*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(0,0), 0),  ('LEFTPADDING', (1,0),(1,0), 4),
                ('RIGHTPADDING', (0,0),(-1,-1), 0), ('VALIGN', (0,0),(-1,-1), 'TOP'),
            ])),
        ]),
        sp(8),
        KeepTogether([
            blm('Adım 3 — Detayları Ekle'),
            sp(3),
            Paragraph(
                'Bağlantı noktaları (tutkal, bant, vida vb.), boyut düzeltmeleri ve gerekiyorsa renk ekle.',
                S_SML),
            sp(4),
            Table([[
                Paragraph('[ ]', S_SMBD),
                Paragraph('<b>Detaylar eklendi.</b>', S_SML),
            ]], colWidths=[0.6*cm, 16.4*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(0,0), 0),  ('LEFTPADDING', (1,0),(1,0), 4),
                ('RIGHTPADDING', (0,0),(-1,-1), 0), ('VALIGN', (0,0),(-1,-1), 'TOP'),
            ])),
        ]),
        sp(8),
        KeepTogether([
            blm('Adım 4 — Prototipi Tanıt'),
            sp(3),
            Paragraph(
                'Bir arkadaşına ya da öğretmenine göster ve şunu sor: "Bunu kullanmak ister miydin? Neden?"',
                S_SML),
            sp(4),
        ] + yazma_alani('Aldığım geri bildirim', 2)
          + [
            Table([[
                Paragraph('[ ]', S_SMBD),
                Paragraph('<b>Geri bildirim alındı.</b>', S_SML),
            ]], colWidths=[0.6*cm, 16.4*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(0,0), 0),  ('LEFTPADDING', (1,0),(1,0), 4),
                ('RIGHTPADDING', (0,0),(-1,-1), 0), ('VALIGN', (0,0),(-1,-1), 'TOP'),
            ])),
        ]),
        sp(8),
        KeepTogether([
            blm('Adım 5 — Notlarını Al'),
            sp(3),
            Paragraph('Prototip süreç günlüğüne (ÇK8) şu soruların yanıtını yaz:', S_SML),
            sp(4),
        ] + yazma_alani('En çok hangi adımda zorlandım?', 1)
          + yazma_alani('Tekrar yapsaydım ne değiştirirdim?', 1)
          + yazma_alani('Prototipin en iyi çalışan kısmı', 1)
          + [
            Table([[
                Paragraph('[ ]', S_SMBD),
                Paragraph('<b>Günlük dolduruldu.</b>', S_SML),
            ]], colWidths=[0.6*cm, 16.4*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(0,0), 0),  ('LEFTPADDING', (1,0),(1,0), 4),
                ('RIGHTPADDING', (0,0),(-1,-1), 0), ('VALIGN', (0,0),(-1,-1), 'TOP'),
            ])),
        ]),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def des3():
    """Materyal 3: Yapılandırılmış Problem Tespiti Soruları"""
    doc   = make_doc('Des3_Problem_Tespiti_Sorulari.pdf', 'Destekleme Materyal 3 — Problem Tespiti Soruları')
    story = []

    story += [
        etiket_baslik('Destekleme Materyal 3', 'Yapılandırılmış Problem Tespiti Soruları',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(6),
        gorev_kutu(
            'Bu sayfa, ÇK1 (Problem Tespiti Formu) doldurmanda sana yardımcı olur. '
            'Her soruyu sırayla yanıtla. "Bilmiyorum" yazabilirsin — sonra birlikte buluruz!'
        ),
        sp(8),
        blm('1. Başlangıç: Çevrene Bak'),
        sp(3),
    ] + yazma_alani('Bugün okulda ya da evde seni rahatsız eden / "daha iyi olabilirdi" dediğin bir durum', 2) + [
        sp(4),
    ] + yazma_alani('Bu durumu 1 cümleyle yaz', 1) + [
        sp(8),
        blm('2. Kimin Sorunu?'),
        sp(3),
        Table([
            [Paragraph('Bu problemi kim yaşıyor?', S_TD),
             Paragraph('( ) Ben yaşıyorum', S_SML),
             Paragraph('( ) Başkası yaşıyor', S_SML),
             Paragraph('( ) İkimiz de', S_SML)],
        ], colWidths=[4*cm, 4*cm, 5*cm, 4*cm],
        style=TableStyle([
            ('BOX',           (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
            ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
            ('TOPPADDING',    (0,0),(-1,-1), 4),
            ('BOTTOMPADDING', (0,0),(-1,-1), 4),
            ('LEFTPADDING',   (0,0),(-1,-1), 4),
            ('RIGHTPADDING',  (0,0),(-1,-1), 4),
            ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ])),
        sp(4),
    ] + yazma_alani('Başkası yaşıyorsa kim?', 1) + [
        sp(8),
        blm('3. Problemi Somutlaştır'),
        sp(3),
    ] + yazma_alani('"Ne zaman" — Bu problem ne zaman ortaya çıkıyor?', 1) + [
        sp(3),
    ] + yazma_alani('"Nerede" — Bu problem nerede oluyor?', 1) + [
        sp(3),
    ] + yazma_alani('"Neden" — Sence bu problem neden oluyor?', 2) + [
        sp(8),
        blm('4. Büyüklüğünü Ölç'),
        sp(3),
        Table([
            [Paragraph('Kaç kişi yaşıyor?', S_TD),
             Paragraph('( ) 1–2 kişi', S_SML),
             Paragraph('( ) 5–10 kişi', S_SML),
             Paragraph('( ) 10+ kişi', S_SML)],
            [Paragraph('Ne sıklıkla oluyor?', S_TD),
             Paragraph('( ) Her gün', S_SML),
             Paragraph('( ) Haftada birkaç kez', S_SML),
             Paragraph('( ) Ara sıra', S_SML)],
        ], colWidths=[4*cm, 3.5*cm, 5*cm, 4.5*cm],
        style=TableStyle([
            ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
            ('TOPPADDING',    (0,0),(-1,-1), 4),
            ('BOTTOMPADDING', (0,0),(-1,-1), 4),
            ('LEFTPADDING',   (0,0),(-1,-1), 4),
            ('RIGHTPADDING',  (0,0),(-1,-1), 4),
            ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ])),
        sp(8),
        blm('5. Daha Önce Çözülmüş mü?'),
        sp(3),
    ] + yazma_alani('Biri bu problemi çözmeye çalışmış mı? Sonuç ne olmuş?', 2) + [
        sp(8),
        KeepTogether([
            blm('6. Problemini Tek Cümleyle Yaz'),
            sp(3),
            gorev_kutu(
                '"_______________ problemi var çünkü _______________, bu durum _______________ yaratıyor."'
            ),
            sp(4),
        ] + yazma_alani('Cümlem (Bu cümle ÇK1\'in "Problem Tanımı" kutusuna gidecek)', 2)),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def des4():
    """Materyal 4: Örnek Cevaplı Empati Haritası"""
    doc   = make_doc('Des4_Empati_Haritasi_Ornek.pdf', 'Destekleme Materyal 4 — Örnek Cevaplı Empati Haritası')
    story = []

    HARITA_STYLE = [
        ('GRID',          (0,0),(-1,-1), 0.5, COLOR_LIGHT_GREY),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
        ('LEFTPADDING',   (0,0),(-1,-1), 6),
        ('RIGHTPADDING',  (0,0),(-1,-1), 6),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ('ROWMINIMUMHEIGHT', (0,0), (-1,-1), 2.2*cm),
    ]

    story += [
        etiket_baslik('Destekleme Materyal 4', 'Örnek Cevaplı Empati Haritası',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        gorev_kutu(
            'Önce Ayşe\'nin doldurduğu empati haritasını oku. '
            'Sonra 2. sayfadaki boş forma kendi kullanıcın için aynısını doldur.'
        ),
        sp(8),
        blm('Örnek Çalışma — Ayşe\'nin Empati Haritası'),
        sp(3),
        Paragraph(
            '<b>Kullanıcı:</b> Mehmet Amca, 68 yaşında — bir hafta boyunca markete gidemedi çünkü kaldırımlar karlıydı.',
            S_SML),
        sp(6),
        Table([
            [Paragraph('<b>Ne Düşünüyor?</b>\nAklından geçenler, endişeleri...', S_TH),
             Paragraph('<b>Ne Hissediyor?</b>\nİçindeki duygular...', S_TH)],
            [Paragraph(
                '"Keşke birisi beni markete götürebilse. Torunlarım çok meşgul. '
                'Yaşlılık insanı başkasına muhtaç ediyor, bu beni üzüyor."',
                S_SML),
             Paragraph(
                'Yalnızlık, bağımsızlığını kaybetme korkusu, biraz utanma '
                '("yük olmak istemiyorum"), ama aynı zamanda umut.',
                S_SML)],
        ], colWidths=[8.5*cm, 8.5*cm], style=TableStyle(HARITA_STYLE + [
            ('BACKGROUND', (0,0),(-1,0), COLOR_PRIMARY),
        ])),
        Table([
            [Paragraph('<b>Ne Söylüyor?</b>\nBaşkalarına ne diyor...', S_TH),
             Paragraph('<b>Ne Yapıyor?</b>\nGerçekte hangi davranışı gösteriyor...', S_TH)],
            [Paragraph(
                '"Bugün hava biraz daha iyi olursa çıkarım." '
                '"Kaldırımlara tuz serpilse iyi olurdu."',
                S_SML),
             Paragraph(
                'Dışarı çıkmaktan vazgeçiyor, telefonla komşuları arıyor, '
                'elindeki kısıtlı besinlerle idare etmeye çalışıyor.',
                S_SML)],
        ], colWidths=[8.5*cm, 8.5*cm], style=TableStyle(HARITA_STYLE + [
            ('BACKGROUND', (0,0),(-1,0), COLOR_PRIMARY),
        ])),
        sp(4),
        Table([
            [Paragraph('En Büyük Zorluk:', S_SMBD),
             Paragraph('Karlı kaldırımlarda düşme korkusu + ihtiyaçlarını karşılayamamak', S_SML),
             Paragraph('Temel İhtiyaç:', S_SMBD),
             Paragraph('Güvenli ve bağımsız hareket edebilmek', S_SML)],
        ], colWidths=[3.5*cm, 5*cm, 3*cm, 5.5*cm],
        style=TableStyle([
            ('BOX',           (0,0),(-1,-1), 0.5, COLOR_ACCENT),
            ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT),
            ('TOPPADDING',    (0,0),(-1,-1), 4),
            ('BOTTOMPADDING', (0,0),(-1,-1), 4),
            ('LEFTPADDING',   (0,0),(-1,-1), 4),
            ('RIGHTPADDING',  (0,0),(-1,-1), 4),
            ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ])),
        PageBreak(),
        etiket_baslik('Destekleme Materyal 4', 'Empati Haritası — Benim Kullanıcım',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        ogrenci_satiri(),
        sp(6),
    ] + yazma_alani('Kullanıcım (adı, yaşı veya tanımı)', 1) + [
        sp(6),
        Table([
            [Paragraph('<b>Ne Düşünüyor?</b>\nAklından geçenler, endişeleri, dilekleri...', S_TH),
             Paragraph('<b>Ne Hissediyor?</b>\nİçindeki duygular...', S_TH)],
            [Paragraph('', S_SML), Paragraph('', S_SML)],
        ], colWidths=[8.5*cm, 8.5*cm], style=TableStyle(HARITA_STYLE + [
            ('BACKGROUND', (0,0),(-1,0), COLOR_PRIMARY),
            ('ROWMINIMUMHEIGHT', (1,0), (-1,-1), 3*cm),
        ])),
        Table([
            [Paragraph('<b>Ne Söylüyor?</b>\nBaşkalarına ne diyor, ne anlatıyor...', S_TH),
             Paragraph('<b>Ne Yapıyor?</b>\nGerçekte hangi davranışı gösteriyor...', S_TH)],
            [Paragraph('', S_SML), Paragraph('', S_SML)],
        ], colWidths=[8.5*cm, 8.5*cm], style=TableStyle(HARITA_STYLE + [
            ('BACKGROUND', (0,0),(-1,0), COLOR_PRIMARY),
            ('ROWMINIMUMHEIGHT', (1,0), (-1,-1), 3*cm),
        ])),
        sp(6),
        Table([
            [Paragraph('<b>En Büyük Zorluk:</b>', S_SMBD),
             Paragraph('', S_SML),
             Paragraph('<b>Temel İhtiyaç:</b>', S_SMBD),
             Paragraph('', S_SML)],
        ], colWidths=[3.5*cm, 5*cm, 3*cm, 5.5*cm],
        style=TableStyle([
            ('BOX',           (0,0),(-1,-1), 0.5, COLOR_ACCENT),
            ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT),
            ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
            ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
            ('TOPPADDING',    (0,0),(-1,-1), 6),
            ('BOTTOMPADDING', (0,0),(-1,-1), 6),
            ('LEFTPADDING',   (0,0),(-1,-1), 4),
            ('RIGHTPADDING',  (0,0),(-1,-1), 4),
            ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
        ])),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def des5():
    """Materyal 5: Malzeme-Özellik Eşleştirme Kartları"""
    doc   = make_doc('Des5_Malzeme_Eslestirme.pdf', 'Destekleme Materyal 5 — Malzeme Eşleştirme Kartları')
    story = []

    KART_STYLE = [
        ('BOX',           (0,0),(-1,-1), 1, COLOR_DASHED),
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('TOPPADDING',    (0,0),(-1,-1), 8),
        ('BOTTOMPADDING', (0,0),(-1,-1), 8),
        ('LEFTPADDING',   (0,0),(-1,-1), 6),
        ('RIGHTPADDING',  (0,0),(-1,-1), 6),
        ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
        ('ROWMINIMUMHEIGHT', (0,0), (-1,-1), 1.5*cm),
    ]

    malzemeler = [
        'KARTON / MUKAVVA', 'KÖPÜK (STRAFOR)',
        'PLASTİK ŞİŞE (GERİ DÖNÜŞÜM)', 'TAHTA / KONTRAPLAK',
        'ALÇI', 'DEMİR TEL',
        'KUMAŞ / KEÇE', 'TOPRAK / KİL',
    ]

    ozellikler = [
        'Hafif ve şekillendirmesi kolay', 'Dayanıklı ve uzun ömürlü',
        'Geri dönüştürülebilir', 'Su geçirmez',
        'Isıya dayanıklı', 'Esnek ve bükülebilir',
        'Doğal malzeme', 'Düşük maliyetli',
        'Kolay kesilebilir', 'Yapıştırıcıya iyi tutunur',
    ]

    mal_rows = []
    for i in range(0, len(malzemeler), 2):
        mal_rows.append([
            Paragraph(f'<b>{malzemeler[i]}</b>', S_TDC),
            Paragraph(f'<b>{malzemeler[i+1]}</b>', S_TDC),
        ])

    ozel_rows = []
    for i in range(0, len(ozellikler), 2):
        ozel_rows.append([
            Paragraph(ozellikler[i], S_TDC7),
            Paragraph(ozellikler[i+1], S_TDC7),
        ])

    story += [
        etiket_baslik('Destekleme Materyal 5', 'Malzeme-Özellik Eşleştirme Kartları',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        gorev_kutu(
            'Bu kartları kes ve iki set yap: Malzeme kartları + Özellik kartları. '
            'Hangi malzeme hangi özelliklere sahip? Eşleştir! '
            'Not: Bazı malzemelerin birden fazla özelliği olabilir.'
        ),
        sp(8),
        blm('Malzeme Kartları'),
        sp(3),
        Table(mal_rows, colWidths=[8.5*cm, 8.5*cm],
              style=TableStyle(KART_STYLE + [
                  ('BACKGROUND', (0,0),(-1,-1), COLOR_VERY_LIGHT),
              ])),
        sp(8),
        blm('Özellik Kartları'),
        sp(3),
        Table(ozel_rows, colWidths=[8.5*cm, 8.5*cm],
              style=TableStyle(KART_STYLE)),
        sp(8),
        KeepTogether([
            blm('Cevap Tablosu — Öğretmen İçin'),
            sp(3),
            Table([
                [Paragraph('Malzeme', S_TH), Paragraph('Başlıca Özellikler', S_TH)],
                [Paragraph('Karton / Mukavva', S_TD),
                 Paragraph('Hafif, düşük maliyetli, kolay kesilebilir, yapıştırıcıya tutunur', S_SML)],
                [Paragraph('Köpük (Strafor)', S_TD),
                 Paragraph('Hafif, şekillendirmesi kolay, ısı yalıtımı yapar', S_SML)],
                [Paragraph('Plastik şişe (geri dönüşüm)', S_TD),
                 Paragraph('Geri dönüştürülebilir, su geçirmez, düşük maliyetli', S_SML)],
                [Paragraph('Tahta / Kontraplak', S_TD),
                 Paragraph('Dayanıklı, uzun ömürlü, yapıştırıcıya tutunur', S_SML)],
                [Paragraph('Alçı', S_TD),
                 Paragraph('Şekillendirmesi kolay (sıvı halde), ısıya dayanıklı, kırılgan', S_SML)],
                [Paragraph('Demir tel', S_TD),
                 Paragraph('Esnek ve bükülebilir, dayanıklı, düşük maliyetli', S_SML)],
                [Paragraph('Kumaş / Keçe', S_TD),
                 Paragraph('Hafif, esnek, doğal malzeme (keçe), düşük maliyetli', S_SML)],
                [Paragraph('Toprak / Kil', S_TD),
                 Paragraph('Doğal malzeme, şekillendirmesi kolay, geri dönüştürülebilir', S_SML)],
            ], colWidths=[4.5*cm, 12.5*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        blm('Oyun Modları'),
        sp(3),
        Table([
            [Paragraph('Mod', S_TH7), Paragraph('Nasıl Oynanır?', S_TH)],
            [Paragraph('Mod 1 — Eşleştirme', S_SMBD),
             Paragraph('Malzeme kartını al, özellik kartlarından hangisini ona yapıştıracaksın?', S_SML)],
            [Paragraph('Mod 2 — En Uygun Kim?', S_SMBD),
             Paragraph('Öğretmen bir kullanım amacı söyler. Öğrenciler en uygun malzemeyi seçer ve neden sorusunu cevaplar.', S_SML)],
            [Paragraph('Mod 3 — Sürdürülebilirlik Turu', S_SMBD),
             Paragraph('Her malzeme için "çevreye ne kadar dost?" sorusunu sor. Malzemeleri 1–5 arasında sırala.', S_SML)],
        ], colWidths=[4*cm, 13*cm],
        style=TableStyle(TABLE_BASE)),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


def des6():
    """Materyal 6: Nerede Kaldım? Kontrol Kartları"""
    doc   = make_doc('Des6_Nerede_Kaldim.pdf', 'Destekleme Materyal 6 — Nerede Kaldım? Kontrol Kartları')
    story = []

    def kontrol_karti(baslik, maddeler, ek_alan1='', ek_alan2=''):
        items = [
            KeepTogether([
                blm(baslik),
                sp(2),
                Table([[
                    Paragraph('<b>Ad:</b>', S_LBL), '',
                    Paragraph('<b>Tarih:</b>', S_LBL), '',
                ]], colWidths=[1.3*cm, 7*cm, 1.7*cm, 7*cm],
                style=TableStyle([
                    ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
                    ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
                    ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
                    ('TOPPADDING',    (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                    ('LEFTPADDING',   (0,0),(-1,-1), 2), ('RIGHTPADDING',  (0,0),(-1,-1), 4),
                ])),
                sp(4),
                kontrol_tablo('Bu derste...', maddeler),
                sp(3),
            ]),
        ]
        if ek_alan1:
            items += yazma_alani(ek_alan1, 1)
        if ek_alan2:
            items += yazma_alani(ek_alan2, 1)
        items.append(HorizontalLine(TW, COLOR_LIGHT_GREY, 0.3))
        items.append(sp(6))
        return items

    story += [
        etiket_baslik('Destekleme Materyal 6', '"Nerede Kaldım?" Kontrol Kartları',
                      'DESTEKLEME MATERYALİ'),
        sp(6),
        gorev_kutu(
            'Her ders sonunda ilgili kartı doldur. Hiç not verilmez — bu sadece senin için! '
            'V = Evet  /\\ = Biraz  X = Henüz hayır'
        ),
        sp(8),
    ]

    story += kontrol_karti(
        '1. Ders Sonu — "Tasarım Nedir?"',
        ['Design Thinking\'in ne olduğunu anlattım',
         '7 adımın adlarını biliyorum',
         'Günlük hayattan bir tasarım örneği verebildim'],
        'Bugün en çok ilgimi çeken',
        'Bir sonraki derste sormak istediğim',
    )
    story += kontrol_karti(
        '2. Ders Sonu — "Problem Tespiti"',
        ['Gerçek bir problem tespit ettim',
         'Problem tespiti formumu (ÇK1) doldurdum',
         'Problemimi 1 cümleyle ifade edebildim'],
        'Bugün en çok ilgimi çeken',
        'Bir sonraki derste sormak istediğim',
    )
    story += kontrol_karti(
        '3. Ders Sonu — "Empati"',
        ['Empati ile sempati arasındaki farkı biliyorum',
         'Kullanıcımı gözlemledim ya da düşündüm',
         'Empati haritamı (ÇK2) doldurdum'],
        'Bugün en çok ilgimi çeken',
        'Bir sonraki derste sormak istediğim',
    )
    story += kontrol_karti(
        '4. Ders Sonu — "Fikir Üretimi"',
        ['Crazy 8 kâğıdıma en az 4 fikir yazdım',
         'Fikirlerimi matrise göre değerlendirdim',
         'En güçlü fikrimi seçtim ve gerekçe yazdım'],
        'Bugün en çok ilgimi çeken',
        'Bir sonraki derste sormak istediğim',
    )
    story.append(PageBreak())
    story += kontrol_karti(
        '5. Ders Sonu — "Eskiz ve Planlama"',
        ['Tasarımımın eskizini çizdim (ÇK6)',
         'Hangi malzemeleri kullanacağımı belirledim',
         'Malzeme planlama tabloma (ÇK7) yazdım'],
        'Bugün en çok ilgimi çeken',
        'Bir sonraki derste sormak istediğim',
    )
    story += kontrol_karti(
        '6–7. Ders Sonu — "Prototip Yapımı"',
        ['Prototipin kaba yapısını tamamladım',
         'Süreç günlüğüme (ÇK8) bugünü yazdım',
         'Bir zorlukla karşılaştım ve çözüm aradım'],
        'Bugün en zorlandığım',
        'Yarın devam etmem gereken',
    )
    story += kontrol_karti(
        '8. Ders Sonu — "Test ve Geri Bildirim"',
        ['Prototipi en az 1 kişiye gösterdim',
         'Geri bildirim formumu (ÇK9) doldurdum',
         'Neyin değişmesi gerektiğini not aldım'],
        'Aldığım en değerli geri bildirim',
        'Bir sonraki derste sormak istediğim',
    )
    story += kontrol_karti(
        '9. Ders Sonu — "Revize"',
        ['Geri bildirime göre en az 1 şeyi değiştirdim',
         'Revize planımı (ÇK10) doldurdum',
         'Sürdürülebilirlik kontrolü yaptım'],
        'Değiştirdiğimde en çok fark yaratan şey',
        '',
    )
    story += kontrol_karti(
        '10. Ders Sonu — "Sunum ve Ünite Sonu"',
        ['Sunum şablonumu (ÇK11) doldurdum',
         'Tasarım sürecimi sınıfa anlattım',
         'Arkadaşımın sunumunu dinledim ve not aldım'],
        'Bu üniteden aklımda kalacak en önemli şey',
        'Design Thinking\'i başka bir yerde kullanabilir miyim? Nerede?',
    )

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.page if hasattr(doc, 'page') else 1


# ── Ana Üretim Döngüsü ───────────────────────────────────────────────────────

PDFS = [
    ('Zen1_Gercek_DT_Projesi.pdf',       'Zenginlestirme 1 - Gercek DT Projesi',   zen1),
    ('Zen2_Tasarim_Portfoyu.pdf',         'Zenginlestirme 2 - Tasarim Portfoyu',    zen2),
    ('Zen3_IDEO_Frog_Arastirma.pdf',      'Zenginlestirme 3 - IDEO/Frog Arastirma', zen3),
    ('Zen4_Surdurulebilir_Malzeme.pdf',   'Zenginlestirme 4 - Malzeme Raporu',      zen4),
    ('Zen5_Celisme_Analizi.pdf',          'Zenginlestirme 5 - Celisme Analizi',      zen5),
    ('Des1_DT_Dongusu_Karti.pdf',         'Destekleme 1 - DT Dongusu Karti',        des1),
    ('Des2_Prototip_Rehberi.pdf',         'Destekleme 2 - Prototip Rehberi',         des2),
    ('Des3_Problem_Tespiti_Sorulari.pdf', 'Destekleme 3 - Problem Tespiti Sorulari', des3),
    ('Des4_Empati_Haritasi_Ornek.pdf',    'Destekleme 4 - Empati Haritasi Ornek',   des4),
    ('Des5_Malzeme_Eslestirme.pdf',       'Destekleme 5 - Malzeme Eslestirme',      des5),
    ('Des6_Nerede_Kaldim.pdf',            'Destekleme 6 - Nerede Kaldim',           des6),
]

if __name__ == '__main__':
    print('\n3. Unite - Farklilastirma PDF Uretimi\n' + '-' * 46)
    toplam = 0
    for fname, aciklama, builder in PDFS:
        try:
            builder()
            toplam += 1
            print(f'  {aciklama:<46} -> OK')
        except Exception as e:
            print(f'  HATA [{aciklama}]: {e}')
    print('-' * 46)
    print(f'Tamamlanan: {toplam}/{len(PDFS)}')
    print(f'Konum: {OUT}')
