"""
Adim 6: Farklilaştirma Paketleri PDF Uretici
Unite 4: Bilgisayar Destekli Tasarim
- Unite4_Zenginlestirme_Paketi.pdf
- Unite4_Destekleme_Paketi.pdf
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
pt = 1.0
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from pdf_style import register_fonts, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, \
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED, COLOR_LIGHT_GREY, \
    COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE

register_fonts()

# ============================================================
# SAYFA BOYUTLARI
# ============================================================

PAGE_W, PAGE_H = A4
ML = 2.0 * cm
MR = 2.0 * cm
MT = 1.8 * cm
MB = 1.8 * cm
UW = PAGE_W - ML - MR   # 481.89 pt

HEADER_Y = PAGE_H - MT
FOOTER_Y = MB

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit4')

# ============================================================
# YARDIMCI STILLER
# ============================================================

def _s(name, **kw):
    base = dict(fontName='TR-Regular', fontSize=9, leading=13,
                textColor=COLOR_TEXT, spaceAfter=0, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

s_cover_tag  = _s('ctag',  fontName='TR-Bold', fontSize=10, textColor=COLOR_PRIMARY, alignment=TA_CENTER)
s_cover_h1   = _s('ch1',   fontName='TR-Bold', fontSize=26, textColor=COLOR_PRIMARY, alignment=TA_CENTER, leading=32)
s_cover_h2   = _s('ch2',   fontName='TR-Bold', fontSize=14, textColor=COLOR_SECONDARY, alignment=TA_CENTER, leading=18)
s_cover_meta = _s('cmeta', fontName='TR-Regular', fontSize=10, textColor=COLOR_TEXT, alignment=TA_CENTER, leading=16)
s_cover_foot = _s('cfoot', fontName='TR-Italic', fontSize=8, textColor=COLOR_MUTED, alignment=TA_CENTER)

s_h1   = _s('h1',  fontName='TR-Bold', fontSize=14, textColor=COLOR_PRIMARY, leading=18, spaceBefore=10, spaceAfter=4)
s_h2   = _s('h2',  fontName='TR-Bold', fontSize=11, textColor=COLOR_SECONDARY, leading=14, spaceBefore=8, spaceAfter=3)
s_h3   = _s('h3',  fontName='TR-Bold', fontSize=9.5, textColor=COLOR_ACCENT, leading=13, spaceBefore=6, spaceAfter=2)
s_body = _s('body', fontSize=8.5, leading=12, spaceAfter=2)
s_bold = _s('bold', fontName='TR-Bold', fontSize=8.5, leading=12)
s_note = _s('note', fontName='TR-Italic', fontSize=8, textColor=COLOR_MUTED, leading=11, spaceAfter=3)
s_tbl  = _s('tbl',  fontSize=7.5, leading=11)
s_tbl_b = _s('tblb', fontName='TR-Bold', fontSize=7.5, leading=11)
s_tbl_c = _s('tblc', fontSize=7.5, leading=11, alignment=TA_CENTER)
s_tbl_bc = _s('tblbc', fontName='TR-Bold', fontSize=7.5, leading=11, alignment=TA_CENTER)
s_check = _s('check', fontSize=8.5, leading=13, leftIndent=6)
s_indent = _s('indent', fontSize=8.5, leading=12, leftIndent=12, spaceAfter=1)

def HR():
    return HRFlowable(width=UW, thickness=0.5, color=COLOR_LIGHT_GREY, spaceAfter=4, spaceBefore=4)

def SP(h=4):
    return Spacer(1, h)

def P(text, style=None):
    return Paragraph(text, style or s_body)

def B(text):
    return Paragraph(text, s_bold)

def H1(text):
    return Paragraph(text, s_h1)

def H2(text):
    return Paragraph(text, s_h2)

def H3(text):
    return Paragraph(text, s_h3)

# ============================================================
# HEADER / FOOTER (Platypus callback için)
# ============================================================

def _hf_canvas(canvas, doc, right_title):
    canvas.saveState()
    canvas.setFont('TR-Regular', 8)
    canvas.setFillColor(COLOR_MUTED)
    canvas.drawString(ML, FOOTER_Y - 6, "Turkiye Yuzyili Maarif Modeli  ·  7. Sinif Teknoloji ve Tasarim  ·  4. Unite: Bilgisayar Destekli Tasarim")
    page_num = canvas.getPageNumber()
    canvas.drawRightString(PAGE_W - MR, FOOTER_Y - 6, str(page_num))
    # ust bant
    canvas.setFont('TR-Italic', 7.5)
    canvas.drawRightString(PAGE_W - MR, HEADER_Y + 2, right_title)
    canvas.setStrokeColor(COLOR_LIGHT_GREY)
    canvas.setLineWidth(0.4)
    canvas.line(ML, HEADER_Y - 2, PAGE_W - MR, HEADER_Y - 2)
    canvas.line(ML, FOOTER_Y, PAGE_W - MR, FOOTER_Y)
    canvas.restoreState()

# ============================================================
# KAPAK SAYFASI
# ============================================================

def cover_page(story, tag, title, subtitle, meta_lines, bg_color=None):
    from reportlab.platypus import Flowable

    class CoverFlowable(Flowable):
        def __init__(self):
            Flowable.__init__(self)
            self.width = UW
            # frame height = PAGE_H - topMargin - bottomMargin - frame padding (12pt)
            self.height = PAGE_H - (MT + 10) - (MB + 10) - 12

        def draw(self):
            c = self.canv
            w, h = self.width, self.height
            bg = bg_color or COLOR_VERY_LIGHT
            c.setFillColor(bg)
            c.roundRect(0, 0, w, h, 12, stroke=0, fill=1)
            # etiket
            c.setFillColor(COLOR_PRIMARY)
            c.setFont('TR-Bold', 10)
            c.drawCentredString(w / 2, h - 40, tag)
            # dekoratif cizgi
            c.setStrokeColor(COLOR_LIGHT)
            c.setLineWidth(2)
            c.line(w * 0.2, h - 52, w * 0.8, h - 52)
            # baslik
            c.setFillColor(COLOR_PRIMARY)
            c.setFont('TR-Bold', 24)
            lines = title.split('\n')
            y = h - 90
            for line in lines:
                c.drawCentredString(w / 2, y, line)
                y -= 32
            # alt baslik
            c.setFillColor(COLOR_SECONDARY)
            c.setFont('TR-Bold', 13)
            c.drawCentredString(w / 2, y - 10, subtitle)
            # meta
            c.setFillColor(COLOR_TEXT)
            c.setFont('TR-Regular', 10)
            my = y - 50
            for line in meta_lines:
                c.drawCentredString(w / 2, my, line)
                my -= 18
            # alt dekor cizgi
            c.setStrokeColor(COLOR_LIGHT)
            c.setLineWidth(1.5)
            c.line(w * 0.3, 35, w * 0.7, 35)
            c.setFillColor(COLOR_MUTED)
            c.setFont('TR-Italic', 8)
            c.drawCentredString(w / 2, 20, "Turkiye Yuzyili Maarif Modeli  ·  7. Sinif Teknoloji ve Tasarim")

    story.append(CoverFlowable())
    story.append(PageBreak())

# ============================================================
# ZENGINLESTIRME PAKETI
# ============================================================

def produce_zenginlestirme():
    out_path = os.path.join(OUT_DIR, 'U4_PDF_06_Zenginlestirme.pdf')

    right_title = "4. Unite: Zenginlestirme Paketi"

    def on_page(canvas, doc):
        if doc.page > 1:
            _hf_canvas(canvas, doc, right_title)

    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=ML, rightMargin=MR,
        topMargin=MT + 10, bottomMargin=MB + 10,
    )

    story = []

    # Kapak
    cover_page(story,
        tag="ZENGINLESTIRME PAKETI",
        title="4. Unite:\nBilgisayar Destekli Tasarim",
        subtitle="Ileri Duzey Ogrenciler icin Derinlestirme Materyalleri",
        meta_lines=[
            "7. Sinif  ·  Teknoloji ve Tasarim",
            "8 Saat / 4 Hafta",
            "TT.7.4.1 · TT.7.4.2 · TT.7.4.3",
        ]
    )

    # Giris notu
    story.append(P(
        "Bu paket; hizli ogrenen, analitik dusunce ve gorsel-uzamsal becerileri guclu olan "
        "ogrenciler icin tasarlanmistir. Maarif Modeli'nin farklilaştirma boyutuyla uyumludur. "
        "Etkinlikler <b>zorunlu degildir</b>; ilgi ve istege gore secilir.",
        _s('info', fontName='TR-Italic', fontSize=8.5, textColor=COLOR_SECONDARY, leading=13,
           borderColor=COLOR_LIGHT, borderPadding=6, backColor=COLOR_VERY_LIGHT)
    ))
    story.append(SP(8))

    # Paket icerigi tablosu
    story.append(H1("PAKET ICERIGI"))
    tbl_data = [
        [P('#', s_tbl_bc), P('Etkinlik', s_tbl_b), P('Tur', s_tbl_b), P('Sure', s_tbl_bc)],
        [P('1', s_tbl_c), P("Tarihin CAD'i: Tasarim Araclari Nasil Degisti?", s_tbl),
         P('Arastirma + infografik', s_tbl), P('1-2 hafta', s_tbl_c)],
        [P('2', s_tbl_c), P("Tinkercad'den Gercege: 3B Baski Dunyasi", s_tbl),
         P('Arastirma + sunum', s_tbl), P('1 hafta', s_tbl_c)],
        [P('3', s_tbl_c), P("Ileri Tinkercad: Birlestirme ve Delik Meydan Okumasi", s_tbl),
         P('Uygulama projesi', s_tbl), P('2-3 ders', s_tbl_c)],
        [P('4', s_tbl_c), P("Kullanici icin Yeniden Tasarla", s_tbl),
         P('Elestirel tasarim', s_tbl), P('1-2 hafta', s_tbl_c)],
        [P('5', s_tbl_c), P("Urunun Otobiyografisi", s_tbl),
         P('Yaratici yazma', s_tbl), P('1 hafta', s_tbl_c)],
        [P('6', s_tbl_c), P("Turk Tasarim Dunyasi: Yerli Uretimden Dunyaya", s_tbl),
         P('Arastirma + sunum', s_tbl), P('1-2 hafta', s_tbl_c)],
        [P('7', s_tbl_c), P("Mesleki Kesif: Endustriyel Tasarimciyla Roportaj", s_tbl),
         P('Arastirma + yansitma', s_tbl), P('1 hafta', s_tbl_c)],
    ]
    cws = [UW * p for p in [0.05, 0.47, 0.28, 0.20]]
    tbl = Table(tbl_data, colWidths=cws, repeatRows=1)
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [COLOR_VERY_LIGHT, white]),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([tbl]))
    story.append(SP(8))

    # Secim kilavuzu
    story.append(H2("ETKINLIK SECIM KILAVUZU"))
    sec_data = [
        [P('Ogrenci Profili', s_tbl_b), P('Onerilen Etkinlik', s_tbl_b)],
        [P('Analitik, sistematik dusunen', s_tbl), P('Etkinlik 1, 3', s_tbl)],
        [P('Arastirma ve okuma seven', s_tbl), P('Etkinlik 2, 6', s_tbl)],
        [P('Elestirel ve sorgulayici', s_tbl), P('Etkinlik 4', s_tbl)],
        [P('Yaratici, sozsel anlatimi guclu', s_tbl), P('Etkinlik 5', s_tbl)],
        [P('Gorsel, uzamsal dusunen', s_tbl), P('Etkinlik 3, 7', s_tbl)],
        [P('Gelecege yonelik dusunen', s_tbl), P('Etkinlik 2, 6, 7', s_tbl)],
    ]
    sec_cws = [UW * 0.55, UW * 0.45]
    sec_tbl = Table(sec_data, colWidths=sec_cws, repeatRows=1)
    sec_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_SECONDARY),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [COLOR_VERY_LIGHT, white]),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([sec_tbl]))
    story.append(PageBreak())

    # -------------------------------------------------------
    # Etkinlikler
    # -------------------------------------------------------

    activities = [
        {
            'no': '1',
            'title': "ETKiNLiK 1: TARiHiN CAD'i - TASARIM ARACLARI NASIL DEGiSTi?",
            'intro': (
                "Insanlar binlerce yildir tasarim yapmaktadir. Misir piramitlerinden Osmanli camilerine, "
                "bugunku TOGG fabrikasina kadar uzanan bu surekte tasarim araclari kokten degisti. "
                "Sen bu donusumu arastiracak ve bir infografik hazirlayacaksin."
            ),
            'yonerge': [
                "Asagidaki uc donemi arastir:",
                "  - El cizimi donemi (1900 oncesi): Cetvel, pergel, cizim masasi",
                "  - Teknik cizim donemi (1900-1980): T-cetveli, izometrik cizim taktlari",
                "  - Dijital CAD donemi (1980-gunumuze): AutoCAD, SolidWorks, Tinkercad, Fusion 360",
                "Her donem icin sunlari bul: Kullanilan bascal araclar (1-2 arac), bir Turk ya da dunya "
                "mimari/muhendisi ornegi, donemin avantaji ve sinirlilik.",
                "Bilgilerini A4 boyutunda dikey infografik olarak duzenle.",
                "Tasariminda zaman cizelgesi formati kullan; her doneme ait bir gorsel ya da eskiz ekle.",
            ],
            'zorunlu': [
                "Uc donemi kapsayan zaman cizelgesi",
                "Her donem icin en az 1 Turkiye veya dunya ornegi",
                "El cizimi, teknik cizim ve dijital ekranin karsilastirmali avantaj tablosu",
                "Kendi degerlendirmen: 'Hangi donemde calismak isterdin? Neden?'",
            ],
            'format': "A4 el cizimi veya dijital infografik",
            'sure': "1-2 hafta",
            'teslim': "Ogretmene basilmis veya dijital + sinifa kisa tanitim (2 dk)",
            'rubrik': [
                ("Uc donemi eksiksiz kapsama", 30),
                ("Turkiye / dunya baglantisi", 20),
                ("Karsilastirmali analiz", 25),
                ("Gorsel duzen ve anlasilirlik", 15),
                ("Kisisel degerlendirme", 10),
            ],
            'ipuclari': [
                "Mimar Sinan'in cizimlerini ve Osmanli mimarlik belgelerini arastir.",
                "TOGG'un tasarim surecini incele - resmi web sitesinde bilgi bulabilirsin.",
                "Infografikini ilk once kagita taslak olarak planla, sonra temize cek.",
            ],
        },
        {
            'no': '2',
            'title': "ETKiNLiK 2: TINKERCAD'DEN GERCEGE - 3B BASKI DUNYASI",
            'intro': (
                "Tinkercad'de bir model olusturdun. Peki bu modeli gercek bir nesneye donusturmek mumkun mu? "
                "3B yazicilar tam da bunu yapiyor. Dunya genelinde hangi alanlarda kullanildigini, "
                "Turkiye'deki gelismeleri ve gelecegini arastirarak bir sunum hazirlayacaksin."
            ),
            'yonerge': [
                "3B baski nedir? Kisaca acikla (1 paragraf).",
                "Asagidaki 3 alandan birini sec ve derinlemesine arastir:",
                "  - Tip: Protez uzuvlar, kemik replasmanlar",
                "  - Uzay ve havacilik: Roket parcalari, uydu bilesenleri (Turksat, ROKETSAN)",
                "  - Mimarlik ve insaat: Yapi maketleri, baskili evler",
                "Sectigin alan icin: Dunyadan bir gercek uygulama ornegi, Turkiye'den bir ornek, avantajlar ve sinirlamalar.",
                "Tinkercad ile 3B yazici arasindaki baglantini acikla.",
            ],
            'zorunlu': [
                "3B baski tanimi ve calisma prensibi (kisaca)",
                "Secilen alandan dunya + Turkiye ornegi",
                "Avantaj / sinirlilik tablosu",
                "Tinkercad -> 3B baski surecinin adim adim aciklamasi",
                "Sonuc: 'Bu teknolojiyi sen nerede kullanmak isterdin?'",
            ],
            'format': "5-8 slayt sunum veya A4 arastirma raporu",
            'sure': "1 hafta",
            'teslim': "Sinifa 3-5 dakikalik sunum",
            'rubrik': [
                ("Teknik dogruluk", 25),
                ("Turkiye baglantisi", 20),
                ("Avantaj/sinirlilik analizi", 25),
                ("Tinkercad -> 3B baski baglantisi", 20),
                ("Sunum akisi ve gorsel duzen", 10),
            ],
            'ipuclari': [
                "TUBITAK ve ASELSAN'in 3B baski calismalarini arastir.",
                "Tinkercad'in .STL dosya formatinin 3B yazicilarla uyumlu oldugunu belirt.",
                "Arastirmanda bilimsel/resmi kaynaklara oncelik ver.",
            ],
        },
        {
            'no': '3',
            'title': "ETKiNLiK 3: iLERi TINKERCAD - BiRLESTiRME VE DELiK MEYDAN OKUMASI",
            'intro': (
                "Sinifta olusturdugun modelde temel sekilleri bir araya getirdin. Bu etkinlikte cok daha "
                "karmasik bir nesne tasarlayacaksin: birden fazla Group ve en az iki Hole iceren, "
                "gercek bir islevi olan bir nesne."
            ),
            'yonerge': [
                "Asagidaki nesnelerden birini sec (veya ogretmenle belirleyin):",
                "  Kucuk bir raf askisi / Kalem-cetvel tutucu / Telefon standi / Anahtar askisi",
                "Nesneyi once kagida ciz: ust, on ve yan gorunusler + olculer.",
                "Tinkercad'de en az: 5+ temel sekil, 2 Group islemi, 2 Hole islemi, gercekci olculer.",
                "Iki farkli acidan ekran goruntus al.",
                "Kagit planin ile Tinkercad modelini karsilastir: ne degisti, neden?",
            ],
            'zorunlu': [
                "El cizimi plan (3 goruntus + olculer)",
                "Tinkercad modeli (en az 5 sekil, 2 Group, 2 Hole)",
                "2 ekran goruntus (farkli acilar)",
                "Yansitma notu: 'Ne zorlandim? Nasil cozdum?'",
            ],
            'format': "Tinkercad baglantisi + ekran goruntuleri + el cizimi",
            'sure': "2-3 ders (sinif disinda da calisilabilir)",
            'teslim': "Ogretmene ekran goruntuleri + el cizimi",
            'rubrik': [
                ("El cizimi kalitesi ve olculeri", 20),
                ("Teknik yeterlilik (Group + Hole kullanimi)", 30),
                ("Nesnenin taninabilirligi ve gercekci olculer", 25),
                ("Plan-model tutarliligi", 15),
                ("Yansitma notu", 10),
            ],
            'ipuclari': [
                "Hole isleminde sekli tamamen nesnenin icine gom, sonra Group'la.",
                "Olculeri CK3 formundakiyle tutarli tut.",
                "Tinkercad'in Rotate ve Align araclarini dene.",
            ],
        },
        {
            'no': '4',
            'title': "ETKiNLiK 4: KULLANICI iCiN YENiDEN TASARLA",
            'intro': (
                "Iyi bir tasarim, yalnizca 'guzel' degil - kullanicinin gercek ihtiyacini karsilamalidir. "
                "Cevrenizde her gun kullandigin ama 'su kisim daha iyi olabilirdi' dedigin bir nesne sec. "
                "Onu kullanici odakli dusenerek yeniden tasarla."
            ),
            'yonerge': [
                "Mevcut nesneyi incele: Nedir? Kim kullaniyor? Hangi sorunu cozu?",
                "Sorunlari tespit et: Kullanicinin en cok zorlandigi 2-3 seyi listele.",
                "(Mumkunse 1 kisiyle kisa gorusme yap.)",
                "Yeniden tasarla: Kagida yeni tasarimini ciz (3 goruntus), degisiklikleri acikla.",
                "Orijinal vs. Yeni Tasarim tablosu hazirla.",
                "Sunum: 2-3 dk 'Neden bu tasarim daha iyi?' diye anlat.",
            ],
            'zorunlu': [
                "Mevcut nesne analizi (kullanici, sorun, bagam)",
                "En az 2-3 tespit edilen sorun",
                "Yeni tasarim cizimi (3 goruntus)",
                "Orijinal vs. Yeni Tasarim karsilastirma tablosu",
                "Gerekceli kisa sunum",
            ],
            'format': "A4 tasarim raporu + cizimler",
            'sure': "1-2 hafta",
            'teslim': "Ogretmene rapor + sinifa sunum",
            'rubrik': [
                ("Kullanici analizi ve sorun tespiti", 25),
                ("Cizim kalitesi ve yaraticilik", 25),
                ("Degisikliklerin gerkcesi", 25),
                ("Karsilastirma tablosu", 15),
                ("Sunum anlasilirlik", 10),
            ],
            'ipuclari': [
                "Okul cantasi, sandalye, kalemlik, su sisesi gibi her gun kullanilan nesneler iyi baslangiç.",
                "Kullanici gorusmesi kisa olabilir - 3 soru yeterli.",
                "Yeniden tasarim mutlaka daha karmasik olmak zorunda degil - daha pratik olmasi yeterli.",
            ],
        },
        {
            'no': '5',
            'title': "ETKiNLiK 5: URUNUN OTOBiYOGRAFiSi",
            'intro': (
                "Sen bu unitede bir nesne tasarladın. Simdi o nesne konusabilseydi ne soylerdı? "
                "Tasarladigin nesnenin bakis acisindan bir otobiyografi yaz. Tasarim surecini, "
                "varolis amacini ve gelecege dair hayallerini nesnenin agzindan anlat."
            ),
            'yonerge': [
                "Asagidaki sorulari rehber olarak kullanarak 3-4 paragraf (200-300 kelime) yaz:",
                "1. Dogusun: 'Ben nasil ortaya ciktim? Tasarimcim beni neden tasarladi?'",
                "2. Bicimim: 'Seklim nasil? Neden bu olculerdeyim? Hangi parcalardan olusuyorum?'",
                "3. Islevim: 'Kimin icin varim? Hangi problemi cozuyorum?'",
                "4. Gelecek: 'Zamanla nasil gelistirilebilirim? Benden 50 yil sonra ne olabilir?'",
            ],
            'zorunlu': [
                "Nesnenin agzindan yazilmis 3-4 paragraf",
                "Tasarim surecine (eskiz, Paint, Tinkercad) en az bir atif",
                "Kullanici ve islev aciklamasi",
                "Gelecege yonelik hayal",
            ],
            'format': "El yazisi veya dijital metin, A4",
            'sure': "1 hafta (ev odevi olarak yapilabilir)",
            'teslim': "Ogretmene yazili + isteye bagli sinifa okunabilir",
            'rubrik': [
                ("Nesnenin bakis acisindan yazilmis olmasi", 20),
                ("Tasarim surecine atif", 20),
                ("Kullanici ve islev aciklamasi", 25),
                ("Yaraticilik ve dil akiciligi", 25),
                ("Gelecek hayal bolumu", 10),
            ],
            'ipuclari': [
                "'Ben bir kalemligim ve...' diye baslayabilirsin.",
                "Tasarimini ve teknik ozelliklerini gercekten iyi bildigin icin bu yazi sana kolay gelecek.",
                "Eglenceli ve yaratici ol - kural yok, hayal gucunu kullan!",
            ],
        },
        {
            'no': '6',
            'title': "ETKiNLiK 6: TURK TASARIM DUNYASI - YERLi URETiMDEN DUNYAYA",
            'intro': (
                "Turkiye, son yillarda teknoloji ve tasarim alaninda onemli adimlar atti. TOGG, BAYKAR, "
                "ASELSAN ve pek cok tasarim sirketi yurt icinde ve dunyada adindan soz ettiriyor. "
                "Bu gelismeleri arastiracak ve Turk tasarimimn guclu yonlerini sunacaksin."
            ),
            'yonerge': [
                "Asagidaki alanlardan en az ikisini sec:",
                "  - Otomotiv: TOGG - Turkiye'nin yerli otomobili",
                "  - Savunma: BAYKAR TB2, Akinci insansiz hava araclari",
                "  - Uzay: Turksat uydulari, Turkiye Uzay Ajansi projeleri",
                "  - Endustriyel Tasarim: Vestel, Arcelik gibi Turk markalarin urun tasarimlari",
                "Her sectigin alan icin: urunun ne oldugunu acikla, hangi tasarim araclari kullanildi, "
                "Turkiye'ye ve dunyaya katkisi.",
                "'Bilgisayar Destekli Tasarim bu urunlerde nasil kullanilmis?' sorusunu yanitla.",
                "A3 poster veya 6-8 slaytlik sunum formatinda hazirla.",
            ],
            'zorunlu': [
                "En az 2 Turk urun/sirket incelemesi",
                "CAD baglantisi ('Bu urunler nasil tasarlandi?')",
                "Turkiye'nin tasarim alanindaki guclu yonleri",
                "Kisisel yorum: 'Bu alanlardan hangisinde calismak isterdim?'",
            ],
            'format': "A3 poster veya dijital sunum (6-8 slayt)",
            'sure': "1-2 hafta",
            'teslim': "Sinifa sunum veya sinif duvarina asma",
            'rubrik': [
                ("Incelenen urun/sirketlerin dogrulugu", 25),
                ("CAD baglantisinin kurulmasi", 25),
                ("Turkiye'nin katkisina dair analiz", 25),
                ("Gorsel duzen ve anlasilirlik", 15),
                ("Kisisel yorum", 10),
            ],
            'ipuclari': [
                "TOGG'un resmi web sitesinde tasarim sureci hakkinda bilgi var.",
                "BAYKAR'in yayimladigi teknik dokumanlari arastir.",
                "Vestel ve Arcelik'in urun tasarim odullerini incele.",
            ],
        },
        {
            'no': '7',
            'title': "ETKiNLiK 7: MESLEKi KESiF - ENDUSTRiYEL TASARIMCIYLA ROPORTAJ",
            'intro': (
                "Endustriyel tasarimcilar, muhendisler ve mimarlar her gun bilgisayar destekli tasarim "
                "araclarini kullaniyor. Bu meslegi kesfetmek icin sanal bir roportaj hazirlayacaksin: "
                "Gercek bir tasarimci hakkinda arastirma yaparak onun agzindan sorulara cevap vereceksin."
            ),
            'yonerge': [
                "Asagidaki meslek gruplarindan birini sec:",
                "  Endustriyel tasarimci / Urun tasarimcisi / Makine muhendisi (CAD kullanan) / Mimar",
                "Bu meslegi gercekten icra eden (Turk ya da yabanci) bir kisiyi arastir.",
                "Asagidaki 10 soruyu arastirma verilerine dayanarak o kisinin agzindan yanıtla:",
                "  Bu meslegi neden sectin? / Gunluk isin nasil geciyor? / Hangi programlari kullaniyorsun?",
                "  Tinkercad gibi araclarla buyuk yazilimlar arasindaki fark nedir?",
                "  En zor tasarim projen hangisiydi? / Bir ogrenciye ne ogutlersin?",
                "  Tasarim yaparken en cok neye dikkat edersin? / Yapay zeka kullaniyor musun?",
                "  Turkiye'de bu meslek nasil gelisiyor? / Gelecekte bu meslek nasil degisecek?",
                "Sona kendi yansitma notunu ekle.",
            ],
            'zorunlu': [
                "Arastirilan kisinin kisa biyografisi (gercek kisi)",
                "10 soruya arastirma verilerine dayali yanitlar",
                "Kaynak listesi (en az 2 kaynak)",
                "Kisisel yansitma notu",
            ],
            'format': "A4, soru-cevap formati",
            'sure': "1 hafta",
            'teslim': "Ogretmene yazili",
            'rubrik': [
                ("Arastirmanin gercek veriye dayanmasi", 30),
                ("Sorularin eksiksiz yanitlanmasi", 30),
                ("CAD/teknoloji baglantisi", 20),
                ("Kisisel yansitma", 10),
                ("Kaynak kullanimi", 10),
            ],
            'ipuclari': [
                "LinkedIn, TED konusmalari ve universite web siteleri iyi kaynaklardir.",
                "Turk tasarimcilar icin 'Tasarim Turkiye' platformunu arastir.",
                "Yanıtlari kendi cumlelerinle yaz - dogrusun kopyalamak degil.",
            ],
        },
    ]

    for act in activities:
        # Her etkinlik yeni sayfada
        blocks = []
        blocks.append(H2(act['title']))
        blocks.append(SP(4))
        blocks.append(P("<b>Gorev Tanimi</b>"))
        blocks.append(P(act['intro']))
        blocks.append(SP(4))
        blocks.append(P("<b>Yonerge</b>"))
        for line in act['yonerge']:
            prefix = "•  " if not line.startswith(' ') else "    –  "
            blocks.append(P(prefix + line.lstrip(), s_indent))

        blocks.append(SP(4))
        blocks.append(P("<b>Zorunlu Ogeler</b>"))
        for item in act['zorunlu']:
            blocks.append(P("•  " + item, s_indent))

        blocks.append(SP(4))
        # Format/sure/teslim kutusu
        ft_data = [
            [P('Format:', s_tbl_b), P(act['format'], s_tbl)],
            [P('Sure:', s_tbl_b), P(act['sure'], s_tbl)],
            [P('Teslim:', s_tbl_b), P(act['teslim'], s_tbl)],
        ]
        ft_tbl = Table(ft_data, colWidths=[UW * 0.15, UW * 0.85])
        ft_tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), COLOR_VERY_LIGHT),
            ('GRID', (0,0), (-1,-1), 0.3, COLOR_LIGHT_GREY),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        blocks.append(ft_tbl)
        blocks.append(SP(4))

        # Rubrik
        blocks.append(P("<b>Degerlendirme</b>"))
        rub_data = [[P('Olcut', s_tbl_b), P('Puan', s_tbl_bc)]]
        for olcut, puan in act['rubrik']:
            rub_data.append([P(olcut, s_tbl), P(str(puan), s_tbl_c)])
        rub_data.append([P('TOPLAM', s_tbl_b), P('100', s_tbl_bc)])
        rub_tbl = Table(rub_data, colWidths=[UW * 0.85, UW * 0.15], repeatRows=1)
        rub_tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), COLOR_SECONDARY),
            ('TEXTCOLOR',  (0,0), (-1,0), white),
            ('BACKGROUND', (0,-1), (-1,-1), COLOR_LIGHT),
            ('ROWBACKGROUNDS', (0,1), (-1,-2), [COLOR_VERY_LIGHT, white]),
            ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        blocks.append(rub_tbl)
        blocks.append(SP(4))

        # Ipuclari
        blocks.append(P("<b>Ipuclari</b>"))
        for ip in act['ipuclari']:
            blocks.append(P("•  " + ip, s_indent))

        story.append(KeepTogether(blocks[:8]))
        for b in blocks[8:]:
            story.append(b)
        story.append(PageBreak())

    # Ogretmen notlari
    story.append(H1("OGRETMEN NOTLARI"))
    notlar = [
        ("Zorluk degil, derinlik",
         "Bu etkinlikler 'daha fazla is' degil, konuya farkli kapilardan giristir."),
        ("Secim hakki",
         "Ogrenciye 2-3 etkinlikten secim sunun; tumunu yapmak zorunda degil."),
        ("Otonomi",
         "Yonlendirme az, ozgun yorum alani genis tutulmustur."),
        ("Paylasim firsati",
         "Ciktilari sinif duvarina, okul sergisine ya da portfolyoya ekleyin."),
        ("Not yuku degil",
         "Degerlendirme tablolar yonlendiricidir; standart nota cevirme zorunlu degildir."),
    ]
    for i, (baslik, aciklama) in enumerate(notlar, 1):
        story.append(P(f"<b>{i}. {baslik}</b> — {aciklama}"))
        story.append(SP(3))

    story.append(SP(8))
    story.append(P(
        "Bu etkinlikler standart musfredat tamamlandiktan sonra bireysel calisma, ev odevi "
        "(2. ders sonunda verilmeli), okul sonrasi kulup veya yil sonu sergisi icin de uygunudur.",
        s_note
    ))

    doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=lambda c, d: on_page(c, d))
    return out_path

# ============================================================
# DESTEKLEME PAKETI
# ============================================================

def produce_destekleme():
    out_path = os.path.join(OUT_DIR, 'U4_PDF_05_Destekleme.pdf')

    right_title = "4. Unite: Destekleme Paketi"

    def on_page(canvas, doc):
        if doc.page > 1:
            _hf_canvas(canvas, doc, right_title)

    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=ML, rightMargin=MR,
        topMargin=MT + 10, bottomMargin=MB + 10,
    )

    story = []

    # Kapak
    cover_page(story,
        tag="DESTEKLEME PAKETI",
        title="4. Unite:\nBilgisayar Destekli Tasarim",
        subtitle="Ek Destege Ihtiyac Duyan Ogrenciler icin Materyaller",
        meta_lines=[
            "7. Sinif  ·  Teknoloji ve Tasarim",
            "8 Saat / 4 Hafta",
            "TT.7.4.1 · TT.7.4.2 · TT.7.4.3",
        ],
        bg_color=HexColor('#EFF6FF')
    )

    # Giris
    story.append(P(
        "Bu paket; ogrenme surecinde ek zamana, gorsel destege veya yapilandirilmis rehbere ihtiyac "
        "duyan ogrenciler icin tasarlanmistir. "
        "Bu materyaller <b>tum ogrencilere acik bir kaynak havuzunun parca</b>sidir.",
        _s('info2', fontName='TR-Italic', fontSize=8.5, textColor=HexColor('#1E40AF'), leading=13,
           borderColor=HexColor('#BFDBFE'), borderPadding=6, backColor=HexColor('#EFF6FF'))
    ))
    story.append(SP(8))

    # Icindekiler
    story.append(H1("PAKET ICERIGI"))
    ic_data = [
        [P('#', s_tbl_bc), P('Materyal', s_tbl_b), P('Amac', s_tbl_b)],
        [P('1', s_tbl_c), P('Gorsel CAD Araclari Sozlugu', s_tbl),
         P('Temel kavramlari resim + tek cumle ozetiyle gosterir', s_tbl)],
        [P('2', s_tbl_c), P('Goruntus Cikarma Adim Adim Rehberi', s_tbl),
         P('Ust-on-yan goruntus cizimini 5 adimda yonlendirir', s_tbl)],
        [P('3', s_tbl_c), P('2B-3B Eslestirme Kartlari', s_tbl),
         P('Nesne goruntus ile 3B modelini oyunla bagdastirir', s_tbl)],
        [P('4', s_tbl_c), P('Tinkercad Kontrol Listesi', s_tbl),
         P('Her adimi tik kutucuklariyla izlemeye yarar', s_tbl)],
        [P('5', s_tbl_c), P('Ornek Cevapli Goruntus Cikarma Kagidi', s_tbl),
         P('Doldurulmus ornek ile birlikte ogrenmeyi destekler', s_tbl)],
        [P('6', s_tbl_c), P('"Nerede Kaldim?" Ders Kontrol Kartlari', s_tbl),
         P('Her ders sonunda kendi kendini kontrol eder', s_tbl)],
    ]
    ic_cws = [UW * 0.05, UW * 0.32, UW * 0.63]
    ic_tbl = Table(ic_data, colWidths=ic_cws, repeatRows=1)
    ic_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#EFF6FF'), white]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([ic_tbl]))
    story.append(PageBreak())

    # -------------------------------------------------------
    # MATERYAL 1: Gorsel CAD Sozlugu
    # -------------------------------------------------------
    story.append(H1("MATERYAL 1: GORSEL CAD ARACLARI SOZLUGU"))
    story.append(P(
        "A5 boyutunda baskı alin. Lamine edilirse unite boyunca masada tutulabilir. "
        "Her kavram: ad + ne ise yarar + nasil kullanilir.",
        s_note
    ))
    story.append(SP(6))

    story.append(H2("2B CiZiM KAVRAMLARI"))

    kavramlar_2b = [
        ("GORUNTUS",
         "Bir nesneyi farkli yonlerden gorundugumuzde ortaya cikan 2B (duz) cizimdir.",
         "Uc temel goruntus: Ust, On, Yan",
         "Nesneyi onune koy. Yukaridan bak -> Ust goruntus. Onden bak -> On goruntus. Sagdan bak -> Yan goruntus."),
        ("OLCEK",
         "Gercek nesneyi kuculterek ya da buyuterek kagida sigmaya yarar.",
         "Ornek: 1 cm kagida = gercekte 10 cm -> Olcek: 1/10",
         "Nesnenin gercek olcusunu bul, kuculterek ciz, olculeri gercek degerleriyle yaz."),
        ("iZOMETRiK CiZiM",
         "Nesneyi tek bir resimde hem onden hem yandan hem de ustden gosterir. 3B gibi gorunur ama duz kagida cizilir.",
         "Noktalı izometrik kagida ciz.",
         "Her cizgi yatay, 30 derece sag veya 30 derece sol olur."),
    ]

    for kavram, tanim, ek, nasil in kavramlar_2b:
        blk = []
        blk.append(P(f"<b>{kavram}</b>",
                    _s('kav', fontName='TR-Bold', fontSize=9, textColor=COLOR_PRIMARY, leading=13)))
        blk.append(P(f"<i>Ne ise yarar:</i> {tanim}"))
        blk.append(P(f"<i>Not:</i> {ek}"))
        blk.append(P(f"<i>Nasil kullanilir:</i> {nasil}"))
        blk.append(HR())
        story.append(KeepTogether(blk))

    # Paint araclari tablosu
    story.append(H3("PAINT ARACLARI"))
    paint_data = [
        [P('Arac', s_tbl_bc), P('Ne Yapar?', s_tbl_b), P('Ne Icin?', s_tbl_b)],
        [P('Dikdortgen', s_tbl_c), P('Kare/dikdortgen cizer', s_tbl), P('Duz kenarli sekiller icin', s_tbl)],
        [P('Elips', s_tbl_c), P('Oval/daire cizer', s_tbl), P('Yuvarlak sekiller icin', s_tbl)],
        [P('Cizgi', s_tbl_c), P('Duz cizgi cizer', s_tbl), P('Kenarlar ve cizgiler icin', s_tbl)],
        [P('Renk Doldur', s_tbl_c), P('Renk doldurur', s_tbl), P('Alanlari boyar', s_tbl)],
        [P('Metin', s_tbl_c), P('Yazi ekler', s_tbl), P('Olcu yazmak icin', s_tbl)],
    ]
    paint_cws = [UW * 0.20, UW * 0.40, UW * 0.40]
    paint_tbl = Table(paint_data, colWidths=paint_cws, repeatRows=1)
    paint_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#EFF6FF'), white]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([paint_tbl]))
    story.append(SP(8))

    story.append(H2("3B MODELLEME KAVRAMLARI"))

    # Tinkercad sekiller tablosu
    story.append(H3("TEMEL SEKILLER (Tinkercad)"))
    sekil_data = [
        [P('Sekil', s_tbl_bc), P('Turkce', s_tbl_b), P('Ne Zaman Kullanilir?', s_tbl_b)],
        [P('Box', s_tbl_c), P('Kutu / Dikdortgenler arasi', s_tbl), P('Duz yuzeylu her nesne', s_tbl)],
        [P('Cylinder', s_tbl_c), P('Silindir', s_tbl), P('Yuvarlak-uzun nesneler, kalemler', s_tbl)],
        [P('Sphere', s_tbl_c), P('Kure', s_tbl), P('Yuvarlak nesneler', s_tbl)],
        [P('Cone', s_tbl_c), P('Koni', s_tbl), P('Uclar, sivri sekiller', s_tbl)],
        [P('Torus', s_tbl_c), P('Halka / Simit', s_tbl), P('Halka, bilezik sekilleri', s_tbl)],
        [P('Wedge', s_tbl_c), P('Kama / Takoz', s_tbl), P('Ucgen kesitli sekiller', s_tbl)],
    ]
    sekil_cws = [UW * 0.20, UW * 0.33, UW * 0.47]
    sekil_tbl = Table(sekil_data, colWidths=sekil_cws, repeatRows=1)
    sekil_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#EFF6FF'), white]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([sekil_tbl]))
    story.append(SP(6))

    # Group ve Hole aciklamalari
    for kavram, tanim, adimlar in [
        ("GROUP (Birlestirme)",
         "Iki veya daha fazla sekli tek bir parca haline getirir.",
         ["Hepsini sec (tikla + Shift ile digerleri)",
          "Ust menuден 'Group' dugmesine bas",
          "Hepsi bir parca oldu"]),
        ("HOLE (Delik)",
         "Bir sekilden parca cikarmaya (delik acmaya) yarar.",
         ["Delik seklini olustur",
          "Ozellikler panelinden 'Hole' sec (renk gri olur)",
          "Delik seklini nesnenin icine tasi",
          "Ikisini sec -> Group"]),
    ]:
        blk = []
        blk.append(H3(kavram))
        blk.append(P(f"<i>Ne ise yarar:</i> {tanim}"))
        blk.append(P("<i>Nasil kullanilir:</i>"))
        for i, adim in enumerate(adimlar, 1):
            blk.append(P(f"  {i}. {adim}", s_indent))
        blk.append(HR())
        story.append(KeepTogether(blk))

    story.append(PageBreak())

    # -------------------------------------------------------
    # MATERYAL 2: Goruntus Cikarma Rehberi
    # -------------------------------------------------------
    story.append(H1("MATERYAL 2: GORUNTUS CIKARMA ADIM ADIM REHBERi"))
    story.append(P("Bu rehberi CK1 Goruntus Cikarma Kagidi ile birlikte kullan. "
                   "Her adimi sirayla takip et; bir adimi bitirmeden digerine gecme.", s_note))
    story.append(SP(4))

    story.append(P("<b>Nesnem:</b> _____________________________________"))
    story.append(HR())
    story.append(SP(4))

    adimlar_rehber = [
        ("ADIM 1: NESNEYI iNCELE",
         "Nesneyi eline al ve her yonluunden bak.",
         [
             "[ ]  Nesneyi onume koydum",
             "[ ]  Yukaridan baktim",
             "[ ]  Onden baktim",
             "[ ]  Sagdan baktim",
         ],
         "Nesnemin genel sekli: _______________ (dikdortgen / silindir / karisik)",
         ""),
        ("ADIM 2: UST GORUNTUSU CiZ",
         "Nesneye tam yukaridan bak. Gordugunu CK1'deki 'Ust Goruntus' kutusuna ciz.",
         [
             "[ ]  Cetvelimi kullandim",
             "[ ]  Dis kenarlari cizim",
             "[ ]  Nesneye ozgu detaylari (delik, cikinti) ekledim",
         ],
         "",
         "Ipucu: Yukaridan bakinca bir bardak daire, bir kutu dikdortgen gorunur."),
        ("ADIM 3: ON GORUNTUSU CiZ",
         "Nesneye tam onden bak. Gordugunu CK1'deki 'On Goruntus' kutusuna ciz.",
         [
             "[ ]  Cetvelimi kullandim",
             "[ ]  Yuksekligi ve genisligi gosterdim",
             "[ ]  Detaylari ekledim",
         ],
         "",
         "Ipucu: On goruntus genellikle nesnenin 'yuzu'dur - en tanidk aci."),
        ("ADIM 4: YAN GORUNTUSU CiZ",
         "Nesneye sagdan bak. Gordugunu CK1'deki 'Yan Goruntus' kutusuna ciz.",
         [
             "[ ]  Cetvelimi kullandim",
             "[ ]  Derinligi ve yuksekligi gosterdim",
             "[ ]  Detaylari ekledim",
         ],
         "",
         "Ipucu: Yan goruntus nesnenin 'profili'dir."),
        ("ADIM 5: OLCULERI YAZ",
         "Her goruntuse en onemli olculeri yaz (cm olarak).",
         [
             "[ ]  Genisligi yazdim (cm)",
             "[ ]  Yuksekligi yazdim (cm)",
             "[ ]  Derinligi yazdim (cm)",
         ],
         "",
         "Ipucu: Olculeri goruntus dismdan, kucuk oklu cizgilerle yaz."),
    ]

    for baslik, aciklama, maddeler, alan, ipucu in adimlar_rehber:
        blk = []
        blk.append(H3(baslik))
        blk.append(P(aciklama))
        for madde in maddeler:
            blk.append(P(madde, s_check))
        if alan:
            blk.append(P(alan))
        if ipucu:
            blk.append(P(f"<i>{ipucu}</i>", s_note))
        blk.append(HR())
        story.append(KeepTogether(blk))

    # Kontrol kutusu
    story.append(SP(4))
    story.append(H3("Bitti mi? Kontrol et:"))
    for madde in [
        "[ ]  Uc goruntus de var mi?",
        "[ ]  Tum goruntuler taninabilir mi?",
        "[ ]  En az 2 olcu var mi?",
        "[ ]  Adimi nereye koyduğumu bilen var mi?",
    ]:
        story.append(P(madde, s_check))

    story.append(PageBreak())

    # -------------------------------------------------------
    # MATERYAL 3: Eslestirme Kartlari
    # -------------------------------------------------------
    story.append(H1("MATERYAL 3: 2B-3B ESLESTIRME KARTLARI"))
    story.append(P("Asagidaki kartlari kes, kartona yapistir (ya da lamine et). "
                   "Asagidaki 3 oyun modundan birini uygula.", s_note))
    story.append(SP(6))

    story.append(H2("Oyun Modlari"))
    oyunlar = [
        ("1. Hizli Eslestirme",
         "Tum kartlari masaya duz koy. Kronometre tut. Tum 2B-3B ciftlerini en hizli bulan kazanir."),
        ("2. Tahmin Oyunu",
         "Bir kisi 3B kart gosterir, digeri hangi 2B goruntuslerin oldugunu soyl."),
        ("3. Aciklama Yarismasi",
         "Bir kisi karti gormeden tarif eder, digeri dogru karti bulmaya calisir."),
    ]
    for baslik, aciklama in oyunlar:
        story.append(P(f"<b>{baslik}:</b> {aciklama}", s_indent))

    story.append(SP(6))
    story.append(H2("Kart Seti"))
    kart_data = [
        [P('#', s_tbl_bc), P('3B NESNENiN ADI', s_tbl_bc),
         P('2B UST GORUNTUS', s_tbl_bc), P('2B ON GORUNTUS', s_tbl_bc)],
        [P('1', s_tbl_c), P('Kup', s_tbl), P('Kare', s_tbl_c), P('Kare', s_tbl_c)],
        [P('2', s_tbl_c), P('Silindir', s_tbl), P('Daire', s_tbl_c), P('Dikdortgen', s_tbl_c)],
        [P('3', s_tbl_c), P('Koni', s_tbl), P('Daire', s_tbl_c), P('Ucgen', s_tbl_c)],
        [P('4', s_tbl_c), P('Dikdortgenler arasi (kutu)', s_tbl), P('Dikdortgen', s_tbl_c), P('Dikdortgen', s_tbl_c)],
        [P('5', s_tbl_c), P('Kare prizma (ince)', s_tbl), P('Kare', s_tbl_c), P('Dikdortgen (yatik)', s_tbl_c)],
        [P('6', s_tbl_c), P('Kure', s_tbl), P('Daire', s_tbl_c), P('Daire', s_tbl_c)],
        [P('7', s_tbl_c), P('Halka (torus)', s_tbl), P('Ic ice daireler', s_tbl_c), P('Ince dikdortgen', s_tbl_c)],
        [P('8', s_tbl_c), P('Kama (wedge)', s_tbl), P('Dikdortgen', s_tbl_c), P('Dik ucgen', s_tbl_c)],
    ]
    kart_cws = [UW * 0.06, UW * 0.34, UW * 0.30, UW * 0.30]
    kart_tbl = Table(kart_data, colWidths=kart_cws, repeatRows=1)
    kart_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#EFF6FF'), white]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([kart_tbl]))
    story.append(P("Baski notu: Her satir bir cift kart olusturur. Kesip iki yigin halinde kullanin.",
                   s_note))
    story.append(PageBreak())

    # -------------------------------------------------------
    # MATERYAL 4: Tinkercad Kontrol Listesi
    # -------------------------------------------------------
    story.append(H1("MATERYAL 4: TINKERCAD KONTROL LiSTESi"))
    story.append(P("Bu kontrol listesini Tinkercad calismasi sirasinda yaninda tut. "
                   "Her adimi tamamladiginda kutucugu isarete.", s_note))
    story.append(SP(6))

    story.append(P("<b>Ad Soyad:</b> _________________________  <b>Nesnem:</b> _________________________"))
    story.append(HR())
    story.append(SP(4))

    asamalar = [
        ("ASAMA 1 - HAZIRLIK (Ders 5 oncesi)", [
            "[ ]  CK3 Tinkercad Planlama Formumu doldurdum",
            "[ ]  Nesnemin parcalarini temel sekillerle listeledim",
            "[ ]  Her parcanin olculerini (en x boy x yukseklik) yazdim",
            "[ ]  Tinkercad hesabima giris yaptim (veya ogretmenle actim)",
        ]),
        ("ASAMA 2 - iLK SEKiL (Tinkercad acikken)", [
            "[ ]  Yeni calisma alani actim",
            "[ ]  ilk temel seklimi surukle-birak ile ekledim",
            "[ ]  Olculerini plan kagidimdaki degerlerle ayarladim",
            "[ ]  Sekli dogru konuma tasidim",
        ]),
        ("ASAMA 3 - PARCALARI BiRLESTiRME", [
            "[ ]  ikinci seklimi ekledim ve olculendirdim",
            "[ ]  iki sekli hizaladim (Align aracini denedim)",
            "[ ]  Hepsini secip Group yaptim",
            "[ ]  Model planimdakine benziyor mu? Kontrol ettim",
        ]),
        ("ASAMA 4 - DETAY EKLEME (varsa)", [
            "[ ]  Gerekiyorsa Hole (delik) sekli ekledim",
            "[ ]  Hole seklini nesnenin icine yerlestirdim",
            "[ ]  Group ile deligi olusturdim",
            "[ ]  Modeli dondurerek her acidan kontrol ettim",
        ]),
        ("ASAMA 5 - KAYDETME VE BiTiRME", [
            "[ ]  Dosya adini 'Ad_Soyad_3B' olarak duzelttim",
            "[ ]  Farkli acidan ekran goruntus aldim (en az 2)",
            "[ ]  Ekran goruntulerini dogru isimle kaydettim",
            "[ ]  Modeli ogretmenim gosterdim veya paylastim",
        ]),
    ]

    for baslik, maddeler in asamalar:
        blk = []
        blk.append(H3(baslik))
        for madde in maddeler:
            blk.append(P(madde, s_check))
        blk.append(SP(3))
        story.append(KeepTogether(blk))

    story.append(HR())
    story.append(SP(4))
    story.append(H3("Sorunum var mi?"))
    sorun_data = [
        [P('Sorun', s_tbl_b), P('Ne Yapacagim', s_tbl_b)],
        [P('Sekli hareket ettiremiyorum', s_tbl), P('Sekle tikla, sonra surukle', s_tbl)],
        [P('Olcuyu degistiremiyorum', s_tbl), P('Sekle cift tikla -> kenar ok belirir', s_tbl)],
        [P('Group calısmiyor', s_tbl), P('Hepsini sectiginden emin ol', s_tbl)],
        [P('Hole gorunmuyor', s_tbl), P('Once Group yap, sonra kontrol et', s_tbl)],
        [P('Kaydedenemedim', s_tbl), P('Sag ustte otomatik kayit var - kontrol et', s_tbl)],
    ]
    sorun_cws = [UW * 0.40, UW * 0.60]
    sorun_tbl = Table(sorun_data, colWidths=sorun_cws, repeatRows=1)
    sorun_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#EFF6FF'), white]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([sorun_tbl]))
    story.append(PageBreak())

    # -------------------------------------------------------
    # MATERYAL 5: Ornek Cevapli Goruntus Cikarma
    # -------------------------------------------------------
    story.append(H1("MATERYAL 5: ORNEK CEVAPLI GORUNTUS CIKARMA KAGiDi"))
    story.append(P("Once bu ornegi incele. Sonra ayni yapıyı kendi nesnen icin uygula. "
                   "Ornek nesne: plastik bir silgi (dikdortgen prizma)", s_note))
    story.append(SP(6))

    story.append(H2("ORNEK: SiLGi iCiN GORUNTUS CIKARMA"))
    story.append(P("<b>Secilen Nesne:</b> Dikdortgen plastik silgi"))
    story.append(P("<b>Olculer:</b> 6 cm x 2 cm x 1 cm (uzunluk x genislik x yukseklik)"))
    story.append(SP(6))

    # Goruntus kutulari tablo olarak
    goruntus_data = [
        [P('UST GORUNTUS\n(Yukaridan bakis)', s_tbl_bc),
         P('ON GORUNTUS\n(Onden bakis)', s_tbl_bc),
         P('YAN GORUNTUS\n(Sagdan bakis)', s_tbl_bc)],
        [
            Paragraph(
                "<i>Duz dikdortgen</i><br/>Uzunluk: 6 cm<br/>Genislik: 2 cm",
                _s('gcell', fontSize=8, leading=12, alignment=TA_CENTER)
            ),
            Paragraph(
                "<i>Ince uzun dikdortgen</i><br/>Uzunluk: 6 cm<br/>Yukseklik: 1 cm",
                _s('gcell2', fontSize=8, leading=12, alignment=TA_CENTER)
            ),
            Paragraph(
                "<i>Kucuk dikdortgen</i><br/>Genislik: 2 cm<br/>Yukseklik: 1 cm",
                _s('gcell3', fontSize=8, leading=12, alignment=TA_CENTER)
            ),
        ],
    ]
    goruntus_cws = [UW / 3, UW / 3, UW / 3]
    g_tbl = Table(goruntus_data, colWidths=goruntus_cws, rowHeights=[None, 60])
    g_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('BACKGROUND', (0,1), (-1,1), HexColor('#EFF6FF')),
        ('GRID', (0,0), (-1,-1), 0.6, HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([g_tbl]))
    story.append(SP(4))
    story.append(P("<i>Bu nesneyi neden sectim:</i> Silgiyi sectim cunku sekli basit ve her yonden "
                   "farkli gorunuyor. Uc goruntus cizmek kolay olacakti.", s_note))
    story.append(HR())
    story.append(SP(6))

    story.append(H2("SiMDi KENDi NESNENi CiZ"))
    story.append(P("<b>Sectigim Nesne:</b> _________________________________"))
    story.append(SP(4))

    bos_data = [
        [P('UST GORUNTUS', s_tbl_bc), P('ON GORUNTUS', s_tbl_bc), P('YAN GORUNTUS', s_tbl_bc)],
        ['', '', ''],
    ]
    b_tbl = Table(bos_data, colWidths=goruntus_cws, rowHeights=[None, 90])
    b_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
        ('TEXTCOLOR',  (0,0), (-1,0), white),
        ('BACKGROUND', (0,1), (-1,1), white),
        ('GRID', (0,0), (-1,-1), 0.6, HexColor('#BFDBFE')),
        ('VALIGN', (0,1), (-1,1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([b_tbl]))
    story.append(SP(6))
    story.append(P("<b>Olculerim:</b>  Uzunluk: _____ cm  ·  Genislik: _____ cm  ·  Yukseklik: _____ cm"))
    story.append(PageBreak())

    # -------------------------------------------------------
    # MATERYAL 6: Ders Kontrol Kartlari
    # -------------------------------------------------------
    story.append(H1("MATERYAL 6: \"NEREDE KALDIM?\" DERS KONTROL KARTLARI"))
    story.append(P("Her ders sonunda (son 3-5 dakika) doldur.  v = evet  ·  ~ = biraz  ·  x = hayir",
                   s_note))
    story.append(SP(6))

    kontrol_kartlar = [
        ("DERS 1-2 KONTROL KARTI", "Goruntus Cikarma - El Cizimi + Paint", [
            "Ust, on ve yan goruntusun ne oldugunu bilirim",
            "Cetvel kullanarak goruntus cizebilirim",
            "Paint'i acip arac cubuğunu bulabilirim",
            "Paint'te dikdortgen/elips aracini kullanabilirim",
        ]),
        ("DERS 3-4 KONTROL KARTI", "Paint Goruntusleri + Tasarim Karti", [
            "Paint'te sekil araclariyla goruntus cizebildim",
            "Farkli parclara farkli renk verdim",
            "Dosyami dogru adla kaydettim (Ad_Soyad_2B.png)",
            "Tasarim Kartimin 4 alanini doldurdum",
        ]),
        ("DERS 5-6 KONTROL KARTI", "Izometrik Cizim + Tinkercad Planlama", [
            "Izometrik kagita kup cizebildim",
            "Nesnemin parcalarini temel sekillerle listeledim",
            "CK3'teki tablo sutunlarini doldurdum",
            "Tinkercad'de hesabima giris yapabildim",
        ]),
        ("DERS 7-8 KONTROL KARTI", "Tinkercad Modelleme + Tasarim Tanitim Karti", [
            "Tinkercad'de en az 2 sekil kullandim",
            "Modeli Group yaptim",
            "Dosyami dogru adla kaydedip ekran goruntus aldim",
            "Tasarim Tanitim Kartimin alanlarini doldurdum",
        ]),
    ]

    for baslik, konu, maddeler in kontrol_kartlar:
        blk = []
        blk.append(H3(f"{baslik}  —  {konu}"))
        blk.append(P("<b>Ad:</b> _________________  <b>Tarih:</b> ___________"))
        blk.append(SP(3))

        k_data = [[P('Yapabildigime emin miyim?', s_tbl_b),
                   P('v', s_tbl_bc), P('~', s_tbl_bc), P('x', s_tbl_bc)]]
        for madde in maddeler:
            k_data.append([P(madde, s_tbl), P('[ ]', s_tbl_c), P('[ ]', s_tbl_c), P('[ ]', s_tbl_c)])
        k_cws = [UW * 0.73, UW * 0.09, UW * 0.09, UW * 0.09]
        k_tbl = Table(k_data, colWidths=k_cws, repeatRows=1)
        k_tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), HexColor('#1D4ED8')),
            ('TEXTCOLOR',  (0,0), (-1,0), white),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#EFF6FF'), white]),
            ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BFDBFE')),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        blk.append(k_tbl)
        blk.append(SP(3))
        blk.append(P("<b>Bu derste en iyi yaptigim:</b> _______________________________________"))
        blk.append(P("<b>Sormak istedigim / Anlamadigim:</b> _______________________________________"))
        blk.append(HR())
        story.append(KeepTogether(blk))

    # Son kart icin farkli sorular
    story.append(SP(4))
    story.append(P("<b>Bu unite boyunca en cok gelistigim alan:</b> _______________________________"))
    story.append(SP(3))
    story.append(P("<b>Bir dahaki unitede daha cok dikkat edecegim:</b> _______________________________"))

    story.append(PageBreak())

    # -------------------------------------------------------
    # Akran Mentorlugu
    # -------------------------------------------------------
    story.append(H1("AKRAN MENTÖRLUGU REHBERi"))
    story.append(SP(4))

    mentor_col = [
        H2("Mentor Ogrenci icin"),
        P("1. <b>Once dinle.</b> Arkadasin ne soruyor?"),
        P("2. <b>Cevabi dogrudan soyleme</b> - sormaya yonlendir: 'Peki bir daha dener misin?'"),
        P("3. <b>Adim adim goster:</b> 'Once sunu yap, sonra sunu...'"),
        P("4. <b>Sabırlı ol</b> - ayni seyi birkaç kez anlatman gerekebilir."),
        P("5. <b>Kucuk basarilari kutla:</b> 'Bak, Group'u yaptin!'"),
    ]
    desteklenen_col = [
        H2("Desteklenen Ogrenci icin"),
        P("1. Sormaktan cekinme - sormak guctur."),
        P("2. Kontrol listeni kullan - nerede kaldigini aninda gorursun."),
        P("3. Ornek cevapli kagida bakabilirsin, ama kendi nesnen icin kendin ciz."),
        P("4. 'Bir daha gosterir misin?' demek tamamen normal."),
    ]

    mentor_flowable = []
    for item in mentor_col:
        mentor_flowable.append(item)

    dest_flowable = []
    for item in desteklenen_col:
        dest_flowable.append(item)

    akran_data = [[mentor_col, desteklenen_col]]
    akran_tbl = Table(akran_data, colWidths=[UW * 0.50 - 4, UW * 0.50 - 4])
    akran_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LINEAFTER', (0,0), (0,-1), 0.5, COLOR_LIGHT_GREY),
        ('RIGHTPADDING', (0,0), (0,-1), 8),
        ('LEFTPADDING', (1,0), (1,-1), 8),
    ]))
    story.append(KeepTogether([akran_tbl]))

    story.append(SP(12))
    story.append(HR())
    story.append(H2("OGRETMEN NOTLARI"))
    ilkeler = [
        ("Onur koruyucu sunum",
         "Bu materyaller 'tum ogrencilere acik kaynak havuzu' olarak tanitilmali."),
        ("Secim hakki",
         "'Bu materyali kullanmak ister misin?' sorulmali, dayatilmamali."),
        ("Basari deneyimi",
         "Her materyal, ogrencinin basarabileceği duzeyindedir."),
        ("Gecicilik",
         "Amac bagimlilik degil; ogrenci ilerledikce materyale ihtiyac azalmali."),
    ]
    for baslik, aciklama in ilkeler:
        story.append(P(f"<b>{baslik}</b> — {aciklama}"))
        story.append(SP(3))

    doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=lambda c, d: on_page(c, d))
    return out_path

# ============================================================
# ANA
# ============================================================

if __name__ == '__main__':
    # Hatalı değişken adını düzelt
    path1 = produce_zenginlestirme()
    print(f"Zenginlestirme paketi olusturuldu: {path1}")
    path2 = produce_destekleme()
    print(f"Destekleme paketi olusturuldu: {path2}")
    print("Adim 6 tamamlandi.")
