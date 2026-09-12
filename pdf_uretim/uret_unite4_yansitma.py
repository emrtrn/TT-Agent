"""
4. Unite -- Ogretmen Yansitma ve Kapanis PDF Ureticisi
5 ayri PDF uretir (units/7_sinif/unit4/ klasorune kaydeder).

Calistir: python pdf_uretim/uret_unite4_yansitma.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
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
    WritingLines, HorizontalLine,
)

register_fonts()

OUT        = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit4')
UNITE_INFO = '4. Unite: Bilgisayar Destekli Tasarim  -  Teknoloji ve Tasarim  -  7. Sinif'
TW         = 17 * cm

# Stiller

S_BAS  = ParagraphStyle('u4y_BAS',  fontName='TR-Bold',    fontSize=13, textColor=COLOR_PRIMARY,   leading=16)
S_ALT  = ParagraphStyle('u4y_ALT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     alignment=TA_RIGHT, leading=10)
S_BLM  = ParagraphStyle('u4y_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=6, spaceAfter=2)
S_LBL  = ParagraphStyle('u4y_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11, spaceAfter=1)
S_SML  = ParagraphStyle('u4y_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SML7 = ParagraphStyle('u4y_SML7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      leading=9.5)
S_SMBD = ParagraphStyle('u4y_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMIT = ParagraphStyle('u4y_SMIT', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11)
S_TH   = ParagraphStyle('u4y_TH',   fontName='TR-Bold',    fontSize=7.5,textColor=white,           alignment=TA_CENTER, leading=10)
S_TH7  = ParagraphStyle('u4y_TH7',  fontName='TR-Bold',    fontSize=7,  textColor=white,           alignment=TA_CENTER, leading=9.5)
S_TD   = ParagraphStyle('u4y_TD',   fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_TD7  = ParagraphStyle('u4y_TD7',  fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=9.5)
S_TDC  = ParagraphStyle('u4y_TDC',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=10.5)
S_TDBD = ParagraphStyle('u4y_TDBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_YON  = ParagraphStyle('u4y_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12)
S_KAP  = ParagraphStyle('u4y_KAP',  fontName='TR-Italic',  fontSize=8.5,textColor=COLOR_TEXT,      leading=13, spaceAfter=2)

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

# Yardimci fonksiyonlar

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

def arac_baslik(no_str, ad, alt=''):
    t = Table([[
        Paragraph(f'<b>{no_str} — {ad}</b>', S_BAS),
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

def ogretmen_satiri():
    t = Table([[
        Paragraph('<b>Ogretmen:</b>', S_LBL), '',
        Paragraph('<b>Okul:</b>',     S_LBL), '',
    ]], colWidths=[2.5*cm, 6.5*cm, 1.8*cm, 6.2*cm])
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

def ogrenci_satiri():
    t = Table([[
        Paragraph('<b>Ad-Soyad (Istege bagli):</b>', S_LBL), '',
        Paragraph('<b>Tarih:</b>',                    S_LBL), '',
    ]], colWidths=[5*cm, 7.5*cm, 1.5*cm, 3*cm])
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

def yazma_alani(etiket, n=2):
    return [Paragraph(f'<b>{etiket}</b>', S_LBL), WritingLines(n, 15), sp(4)]

def secim(secenek):
    return Paragraph(f'( ) {secenek}', S_SML)

def ders_blogu(no_str, baslik, sorular=None, secimler=None, notlar=None):
    items = [
        KeepTogether([
            blm(f'{no_str}. Ders — "{baslik}"'),
            sp(3),
            Table([[
                Paragraph('<b>Planlanan sureye uygun gecti mi?</b>', S_LBL),
                Paragraph('( ) Evet  ( ) Hayir', S_SML),
            ]], colWidths=[8*cm, 9*cm],
            style=TableStyle([
                ('TOPPADDING',    (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING',   (0,0),(-1,-1), 0), ('RIGHTPADDING',  (0,0),(-1,-1), 0),
                ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
            ])),
            sp(3),
            Table([[
                Paragraph('<b>Planlanan:</b>', S_LBL), Paragraph('_____ dk', S_SML),
                Paragraph('<b>Gerceklesen:</b>', S_LBL), Paragraph('_____ dk', S_SML),
            ]], colWidths=[2.5*cm, 5*cm, 3.5*cm, 6*cm],
            style=TableStyle([
                ('TOPPADDING',    (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING',   (0,0),(-1,-1), 0), ('RIGHTPADDING',  (0,0),(-1,-1), 0),
                ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
            ])),
            sp(5),
        ]),
    ]
    if sorular:
        for soru_tuple in sorular:
            if isinstance(soru_tuple, tuple):
                etiket, secler = soru_tuple
                items.append(Paragraph(f'<b>{etiket}</b>', S_LBL))
                items.append(sp(2))
                for s in secler:
                    items.append(secim(s))
                items.append(sp(6))
            else:
                items += yazma_alani(soru_tuple, 2)
    if notlar:
        items += [Paragraph('<b>Bir sonraki sefere icin not:</b>', S_LBL), sp(2)]
        for not_str in notlar:
            items.append(secim(not_str))
        items.append(sp(4))
    items.append(HorizontalLine(TW, COLOR_LIGHT_GREY, 0.3))
    items.append(sp(6))
    return items

# ARAC 1: OGRETMEN YANSITMA GUNLUGU

def arac1():
    doc   = make_doc('Kapanis1_Ogretmen_Yansitma.pdf', 'Arac 1 - Ogretmen Yansitma Gunlugu')
    story = []

    story += [
        arac_baslik('Arac 1', 'Ogretmen Yansitma Gunlugu', 'OGRETMEN REHBERI'),
        sp(6),
        ogretmen_satiri(),
        sp(4),
        Table([[
            Paragraph('<b>Sinif:</b>', S_LBL), '',
            Paragraph('<b>Uygulama Donemi:</b>', S_LBL), '',
        ]], colWidths=[1.8*cm, 5*cm, 4*cm, 6.2*cm],
        style=TableStyle([
            ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
            ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
            ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
            ('TOPPADDING',    (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
            ('LEFTPADDING',   (0,0),(-1,-1), 2), ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ])),
        sp(8),
        blm('Genel Yansitma'),
        sp(4),
    ] + yazma_alani('Bu uniteyi tek bir cumleyle nasil ozetlersiniz?', 1) + [
        sp(2),
    ] + yazma_alani('Hangi beklentiniz karsilandi?', 2) + [
        sp(2),
    ] + yazma_alani("Hangi beklentiniz karsilanmadi? Olasi nedeni neydi?", 2) + [
        sp(2),
        Paragraph("<b>Ogrencilerin 2B'den 3B'ye gecis surecini kavrama duzeyi genel olarak nasil oldu?</b>", S_LBL),
        sp(2),
        secim("Buyuk cogunluk goruntus mantigini ve Tinkercad'i akici kullandi"),
        secim("Cogunluk 2B tarafini kavradı; 3B modelleme zorlu geldi"),
        secim("Tinkercad arayuzu ogrenme suresini beklenmeden uzatti"),
        secim("2B ve 3B arasindaki kavramsal bag yeterince kurulamadi"),
        sp(8),
        blm('Ders Saati Bazinda Yansitma'),
        sp(4),
    ]

    # 1-2. Ders
    story += ders_blogu('1-2', 'Goruntus Cikarma + El Cizimi (Sinif)',
        sorular=[
            "'Ust, on, yan goruntus' kavrami ogrencilerde somutlasti mi?",
            ('CK1 (Goruntus Cikarma Kagidi) nasil ise yaradi? En cok hangi kutuda zorlandilar?', [
                'Ust Goruntus', 'On Goruntus', 'Yan Goruntus', 'Olcu belirtme',
            ]),
            "Nesne secimi serbest birakilmasi nasil sonuclandi? (Cok basit mi, cok karmasik mi?)",
        ],
        notlar=[
            'Goruntus orneklerini daha somut nesnelerle arttiracagim',
            'CK1 yonergesini daha ayrintili aciklayacagim',
            'Destekleme Materyal 2 (Adim Adim Rehber) daha erken sunacagim',
            'Diger: ___________________________',
        ]
    )

    # 3-4. Ders
    story += ders_blogu('3-4', "Paint Dijital Cizim + Tasarim Karti (Atolye)",
        sorular=[
            ("Paint'i ilk kez kullanan ogrenci orani yaklasik neydi?", [
                'Buyuk cogunluk daha once kullanmis',
                'Yaklasik yarisi ilk kez kullandi',
                'Buyuk cogunluk ilk kez kullandi',
            ]),
            ("En cok hangi araçta zorlandilar?", [
                'Sekil araclari (dikdortgen, elips)',
                'Renk doldurma',
                "Dosyayi PNG olarak kaydetme",
                'Metin/olcu yazma',
            ]),
            ("Tasarim Karti 4 alani zamaninda tamamlanabildi mi?", [
                'Buyuk cogunluk tamamladi',
                'Yarisi tamamladi, yarisi yarim kaldi',
                'Cogu tamamlayamadi -> sure yetersizdi',
            ]),
        ],
        notlar=[
            "Paint arac tanitimini ayri bir blokta yapacagim",
            "Tasarim Karti icin ek sure ayiracagim",
            "Arac Referans Kart'ni masalara onceden dagitacagim",
            'Diger: ___________________________',
        ]
    )

    # 5-6. Ders
    story += ders_blogu('5-6', 'Izometrik Cizim + Tinkercad Planlama (Sinif)',
        sorular=[
            ('Izometrik kagita kup cizimi nasil gitti?', [
                'Buyuk cogunluk bagimsiz cizdi',
                'Rehber gosterimle cizdiler',
                'Onemli bir kisim anlasilamadan birakti',
            ]),
            "CK3 (Tinkercad Planlama Formu) nasil ise yaradi?",
            ("'Parcalari temel sekillerle ifade et' talimatini ogrenciler kavrayabildi mi?", [
                'Evet, hemen anladilar',
                'Birkaç ornek sonrasi kavradilar',
                'Soyut kaldi, somutlastirmak guc oldu',
            ]),
        ],
        notlar=[
            'Izometrik cizimi daha basit bir nesneyle baslatacagim',
            "CK3'te parca ornekleri listesini genisletecegim",
            'Tinkercad tanitim videosunu sinifta izleteceğim',
            'Diger: ___________________________',
        ]
    )

    # 7-8. Ders
    story += ders_blogu('7-8', 'Tinkercad Modelleme + Tasarim Tanitim Karti + Kapanis (Atolye)',
        sorular=[
            "Teknik aksakliklar yasandi mi? (Hesap girisi, internet, yazilim yavasligi vb.)",
            ("Ogrenciler CK3 planiyla tutarli model olusturabildi mi?", [
                'Buyuk cogunluk planini modele yansitti',
                'Kismen yansitti; bazi degisiklikler yapti (gereksiz)',
                'Plan ile model arasinda belirgin kopukluk vardi',
            ]),
            ("Tasarim Tanitim Karti yetisebildi mi?", [
                'Evet, cogunluk 5 alani da doldurdu',
                'Zamanin buyuk bolumu modele harcandi; kart yarim kaldi',
                'Kart bir sonraki derse ya da eve odev olarak verildi',
            ]),
            ("Sunum (Tasarim Tanitim) kalitesi nasil oldu?", [
                'Cogunluk hem sureci hem karari net anlatti',
                "Nesneyi anlatilar ama karari (neden/kimin icin) aciklayamadi",
                'Sunum kaygisi icerigi golgeledi',
            ]),
            "Unite kapanis atmosferi nasil oldu?",
        ],
        notlar=[
            'Modelleme suresini bir ders daha uzatmayi talep edecegim',
            "Tasarim Tanitim Karti'ni modellemeden once dolduracagim",
            "Sunum oncesi kisa yansitma etkinligi ekleyecegim",
            'Diger: ___________________________',
        ]
    )

    story += [
        blm('Ogrenci Performanslari'),
        sp(4),
        Paragraph('<b>En Buyuk Gelisimi Gosteren Ogrenciler</b>', S_SMBD),
        sp(3),
    ]
    # Performans tablosu
    for baslik, sutunlar in [
        ('En Buyuk Gelisimi Gosteren Ogrenciler',
         ['Ogrenci', 'Gozlenen Gelisim', 'Ne Destekledi?']),
        ('Ek Destek Gereksinimi Olan Ogrenciler',
         ['Ogrenci', 'Gozlenen Zorluk', 'Sonraki Unitede Denenecek']),
        ('Zenginlestirmeye Yonlendirilebilecek Ogrenciler',
         ['Ogrenci', 'Ilgi / Yetenek Alani', 'Onerilen Etkinlik (Adim 6)']),
    ]:
        rows = [[Paragraph(s, S_TH) for s in sutunlar]]
        for _ in range(3):
            rows.append([Paragraph('', S_TD)] * len(sutunlar))
        cw = TW / len(sutunlar)
        t = Table(rows, colWidths=[cw]*len(sutunlar), rowHeights=[None] + [14]*3)
        ts = TableStyle(list(TABLE_BASE) + [
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, COLOR_VERY_LIGHT_GREY]),
        ])
        t.setStyle(ts)
        story += [Paragraph(f'<b>{baslik}</b>', S_SMBD), sp(3), t, sp(6)]

    story += [
        blm('Materyal Degerlendirmesi'),
        sp(4),
    ]
    materyaller = [
        'On Degerlendirme Paketi',
        'Arac Referans Karti (A5)',
        'CK1 Goruntus Cikarma Kagidi',
        'CK2 Izometrik Cizim Kagidi',
        'CK3 Tinkercad Planlama Formu',
        'Urun Degerlendirme Rubriği',
        'Surec Gozlem Formu',
        'Ogrenci Oz Degerlendirme Formu',
        'Zenginlestirme Paketi',
        'Destekleme Paketi',
    ]
    mat_rows = [[Paragraph(m, S_TH7) for m in ['Materyal', 'Degerlendirme (1-5)', 'Not']]]
    for m in materyaller:
        mat_rows.append([Paragraph(m, S_TD7), Paragraph('____', S_TDC), Paragraph('', S_TD7)])
    mat_t = Table(mat_rows, colWidths=[9.5*cm, 3.5*cm, 4*cm], repeatRows=1)
    mat_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [mat_t, sp(6)]

    story += [
        sp(2),
    ] + yazma_alani('Degisiklik dusundugum materyal ve gerekcesi:', 2) + [
        blm('Kazanim Duzeyleri (Sinif Geneli)'),
        sp(4),
    ]
    kaz_rows = [
        [Paragraph(s, S_TH7) for s in
         ['Kazanim', 'Ustun (%)', 'Yeterli (%)', 'Gelisiyor (%)', 'Destek Gerekli (%)']],
        [Paragraph('TT.7.4.1 - 2B/3B arac kullanimi', S_TD7),
         Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC)],
        [Paragraph('TT.7.4.2 - Dijital araçla tasarim', S_TD7),
         Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC)],
        [Paragraph('TT.7.4.3 - Coklu ortam sunusu', S_TD7),
         Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC)],
    ]
    kaz_cw = [7*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.5*cm]
    kaz_t = Table(kaz_rows, colWidths=kaz_cw, rowHeights=[None, 14, 14, 14])
    kaz_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [kaz_t, sp(4)]

    story += (
        yazma_alani('En basarili olunan kazanim:', 1) +
        yazma_alani('En cok zorlanilan kazanim:', 1) + [
            blm('Ders Disi Gozlemler'),
            sp(3),
            Paragraph('<b>Sinif atmosferi (uygun olanlari isaretle):</b>', S_LBL),
            sp(2),
            secim("Tinkercad beklenmedik duzey motivasyon yaratti"),
            secim("2B/3B gecis kavramsalbir 'aha!' ani olusturdu"),
            secim("Teknik aksakliklar sinif enerjisini dusurdu"),
            secim("Zaman baskisi ogrenci kaygisini artirdi"),
            secim("Bazi ogrenciler Tinkercad'i cok hizli kavrayip digerlerine destek oldu"),
            sp(6),
        ] + yazma_alani('Velilerden gelen yansimalar (varsa):', 2) +
        yazma_alani('Disiplinlerarasi gozlemler (Matematik-Gorsel Sanatlar-Bilisim baglantilari):', 2) + [
            blm('Kendime Not: Bir Sonraki Unite Icin'),
            sp(3),
            Paragraph("<b>5. Unite baslamadan once yapmam gerekenler:</b>", S_LBL),
            sp(2),
            Paragraph('( ) _______________________________________________', S_SML),
            Paragraph('( ) _______________________________________________', S_SML),
            Paragraph('( ) _______________________________________________', S_SML),
            sp(6),
            Paragraph('<b>Bu uniteden 5. Uniteye (Mimari Tasarim) tasinacak baglantilar:</b>', S_LBL),
            sp(2),
            Paragraph('<b>Kopru kavram:</b>  Goruntus cikarma -> kat plani-kesit-cephe', S_SML),
            Paragraph('<b>Hatirlatilacak:</b>  Olcek kavrami, 3 goruntus kurali', S_SML),
            Paragraph('<b>Kullanilacak ogrenci calismasi:</b>  ___________________________', S_SML),
            sp(8),
            blm('Profesyonel Gelisim Notu'),
            sp(4),
        ] + yazma_alani('Bu unitede ben ne ogrendim?', 3) +
        yazma_alani('Tinkercad konusunda daha fazla gelistirmek istedigim beceri:', 2) +
        yazma_alani('Hangi konuda egitim/okuma yapmam gerekiyor?', 2)
    )

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.filename

# ARAC 2: OGRENCI DONUT ANKETI

def arac2():
    doc   = make_doc('Kapanis2_Ogrenci_Donut_Anketi.pdf', 'Arac 2 - Ogrenci Donut Anketi')
    story = []

    story += [
        arac_baslik('Arac 2', 'Ogrenci Donut Anketi', 'OGRENCI FORMU'),
        sp(6),
        Paragraph(
            'Sevgili Ogrenci, Bu ankete samimi cevaplar vermen, bir sonraki donem icin cok degerli. '
            '<b>Adini yazman zorunlu degil. Cevaplarin not olarak kullanilmaz.</b>',
            S_SMIT),
        sp(4),
        ogrenci_satiri(),
        sp(8),
        blm('BOLUM 1: Kavramlar Hakkinda'),
        sp(4),
    ] + yazma_alani('Bu unitede en kolay ogrendigim konu:', 1) + [
        sp(2),
    ] + yazma_alani('Bu unitede en zor gelen konu:', 1) + [
        sp(2),
    ] + yazma_alani("Bu unitede 'Bunu hayatimda kullanabilirim!' diye dusundugum konu:", 1) + [
        sp(6),
        blm('BOLUM 2: Etkinlikler Hakkinda'),
        sp(3),
        Paragraph('Her etkinlik icin 1-5 arasi puan ver (1 = hic sevmedim, 5 = cok sevdim):', S_SML),
        sp(4),
    ]
    etkinlikler = [
        "Nesne secip goruntuslerini el ile cizme",
        "Paint'te nesne goruntuslerini dijital cizme",
        "Izometrik kagida cizim",
        "Tinkercad'de 3B model olusturma",
        "Tasarim Tanitim Karti hazirlayip sinifa sunma",
    ]
    etk_rows = [[Paragraph(e, S_TH7) for e in ['Etkinlik', 'Puanim (1-5)']]]
    for e in etkinlikler:
        etk_rows.append([Paragraph(e, S_TD), Paragraph('', S_TDC)])
    etk_t = Table(etk_rows, colWidths=[13.5*cm, 3.5*cm], rowHeights=[None]+[16]*len(etkinlikler))
    etk_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [
        etk_t,
        sp(4),
    ] + yazma_alani('En cok sevdigim etkinlik ve neden:', 1) + [
        sp(2),
    ] + yazma_alani('En az sevdigim etkinlik ve neden:', 1) + [
        sp(6),
        blm('BOLUM 3: Ogrenme Deneyimim'),
        sp(4),
        Paragraph("<b>Tinkercad'de calismak nasil hissettirdi?</b>", S_LBL),
        sp(2),
        secim('Kolay ve eglenceli, daha fazla yapmak istedim'),
        secim('Zor ama anladikca keyif aldim'),
        secim('Zor geldi, eksiklikler kaldi'),
        secim('Teknik sorunlar cok zorladi'),
        sp(5),
        Paragraph('<b>Kagit ciziminden bilgisayar cizimine gecis nasil oldu?</b>', S_LBL),
        sp(2),
        secim('Bilgisayar daha kolaydi'),
        secim('Ikisi farkli ama ikisini de begendim'),
        secim('Kagit benim icin daha kolaydi'),
        secim('Fark etmedi'),
        sp(5),
        Paragraph("<b>Ogretmenin aciklamalari anlasilir miydi?</b>", S_LBL),
        sp(2),
        secim('Cok net, her seyi anladim'),
        secim('Cogunlukla netti'),
        secim('Zaman zaman kayboldum'),
        secim('Cogu zaman karisikti'),
        sp(5),
        Paragraph("<b>Sinif ortami nasil oldu?</b>", S_LBL),
        sp(2),
        secim('Rahatca soru sorabildim'),
        secim('Soru sormaktan cekindim'),
        secim('Arkadaslarimla iyi calistik'),
        secim('Bilgisayar basinda tek basima calismak yorucu geldi'),
        sp(8),
        blm('BOLUM 4: Oneriler'),
        sp(4),
    ] + yazma_alani('Bir sonraki unitede olmasi istedigim bir sey:', 2) + [
        sp(2),
    ] + yazma_alani('Bir sonraki unitede olmamasi istedigim bir sey:', 2) + [
        sp(2),
    ] + yazma_alani('Ogretmenime soylemek istedigim bir sey:', 2) + [
        sp(6),
        blm('BOLUM 5: Kendine Bir Not'),
        sp(4),
    ] + yazma_alani('Bu uniteden 10 yil sonra hatirlaycagim bir sey:', 2) + [
        sp(4),
        Table([[
            Paragraph('<b>Kendimi bu unitede nasil degerlendiriyorum?</b>', S_LBL), '',
            Paragraph('____ / 10', S_SML),
        ]], colWidths=[10*cm, 4*cm, 3*cm],
        style=TableStyle([
            ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0),(-1,-1), 2),
            ('BOTTOMPADDING', (0,0),(-1,-1), 2),
            ('LEFTPADDING', (0,0),(-1,-1), 0),
            ('RIGHTPADDING', (0,0),(-1,-1), 0),
        ])),
        sp(3),
    ] + yazma_alani('Neden bu puani verdim:', 1)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.filename

# ARAC 3: ZUMRE PAYLASIM SABLONU

def arac3():
    doc   = make_doc('Kapanis3_Zumre_Paylasim.pdf', 'Arac 3 - Zumre Paylasim Sablonu')
    story = []

    story += [
        arac_baslik('Arac 3', 'Zumre Paylasim Sablonu', 'OGRETMEN REHBERİ'),
        sp(6),
        ogretmen_satiri(),
        sp(4),
        Table([[
            Paragraph('<b>Sinif Sayisi:</b>', S_LBL), '',
            Paragraph('<b>Ogrenci Sayisi:</b>', S_LBL), '',
        ]], colWidths=[3*cm, 5.5*cm, 3.5*cm, 5*cm],
        style=TableStyle([
            ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
            ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
            ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
            ('TOPPADDING',    (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
            ('LEFTPADDING',   (0,0),(-1,-1), 2), ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ])),
        sp(4),
    ] + yazma_alani('Uygulama Donemi:', 1) + [
        sp(4),
        blm('1. Ana Deneyim'),
        sp(3),
    ] + yazma_alani('Bu uniteyi nasil uyguladiniz? Kisa bir paragrafla ozetleyin:', 4) + [
        sp(4),
        blm('2. Ise Yarayan 3 Uygulama'),
        sp(3),
    ] + yazma_alani('Uygulama 1 ve neden ise yaradi:', 2) + [
        sp(2),
    ] + yazma_alani('Uygulama 2 ve neden ise yaradi:', 2) + [
        sp(2),
    ] + yazma_alani('Uygulama 3 ve neden ise yaradi:', 2) + [
        sp(4),
        blm('3. Zorluklar ve Cozumler'),
        sp(3),
    ] + yazma_alani('Zorluk 1 / Denenen cozum / Sonuc:', 3) + [
        sp(2),
    ] + yazma_alani('Zorluk 2 / Denenen cozum / Sonuc:', 3) + [
        sp(4),
        blm('4. Tinkercad Kullanimi Hakkinda Paylasim'),
        sp(3),
        Paragraph("<b>Okulunuzda Tinkercad'e erisim nasil?</b>", S_LBL),
        sp(2),
        secim('Okul bilgisayarlarinda sorunsuz'),
        secim('Yavas/kesintili internet sorun yaratti'),
        secim('Hesap acma/giris surecinde zorluk yasandi'),
        secim('Alternatif arac kullandik: ___________________________'),
        sp(5),
    ] + yazma_alani("Tinkercad disinda denediginiz 3B arac var mi?", 2) + [
        sp(4),
        blm('5. Olcme ve Degerlendirme'),
        sp(3),
        Paragraph('<b>Kullanilan araclar (uygun olanlari isaretle):</b>', S_LBL),
        sp(2),
        secim('Surec gozlem formu'),
        secim('Urun degerlendirme rubriği'),
        secim('Ogrenci oz degerlendirme formu'),
        secim('Akran degerlendirme'),
        secim('Diger: _______________________'),
        sp(5),
    ]
    duzeyleri_rows = [
        [Paragraph(s, S_TH7) for s in ['Duzey', 'Yaklasik Yuzde']],
        [Paragraph('Ustun', S_TD),   Paragraph('% ___', S_TDC)],
        [Paragraph('Yeterli', S_TD), Paragraph('% ___', S_TDC)],
        [Paragraph('Gelisiyor', S_TD), Paragraph('% ___', S_TDC)],
        [Paragraph('Destek Gerekli', S_TD), Paragraph('% ___', S_TDC)],
    ]
    d_t = Table(duzeyleri_rows, colWidths=[9*cm, 8*cm], rowHeights=[None]+[14]*4)
    d_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [d_t, sp(6)] + yazma_alani('Diger ogretmenler icin pratik oneriler:', 3) + [
        sp(4),
    ] + yazma_alani('Ortak gundem onerileri:', 2)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.filename

# ARAC 4: UNITE OZET TABLOSU

def arac4():
    doc   = make_doc('Kapanis4_Unite_Ozet_Tablosu.pdf', 'Arac 4 - Unite Ozet Tablosu')
    story = []

    story += [
        arac_baslik('Arac 4', 'Unite Ozet Tablosu', 'OGRETMEN REHBERI'),
        sp(6),
        blm('Tum Materyaller Listesi'),
        sp(4),
    ]

    materyaller_data = [
        [Paragraph(s, S_TH7) for s in ['#', 'Materyal', 'Kullanim Yeri', 'Sure', 'Baskı']],
        ['1', 'Ders Plani',                          'Ogretmen hazırligi',         'Tum unite',    'Ogretmende'],
        ['2', 'On Degerlendirme Ogretmen Rehberi',   'Unite basi',                 '5 dk',         'Ogretmende'],
        ['3', 'On Degerlendirme Ogrenci-1',          '1. ders',                    '15 dk',        'Ogrenciye 1 sayfa'],
        ['4', 'On Degerlendirme Ogrenci-2',          '1. ders',                    '15 dk',        'Ogrenciye 1 sayfa'],
        ['5', 'Arac Referans Karti (A5)',             '3-8. dersler',               '-',            'Ogrenciye lamine'],
        ['6', 'CK1 Goruntus Cikarma (A4, 2 sayfa)',  '1-2. dersler',               '2 ders',       'Ogrenciye'],
        ['7', 'CK2 Izometrik Cizim (A4)',             '5-6. dersler',               '2 ders',       'Ogrenciye'],
        ['8', 'CK3 Tinkercad Planlama (A4)',          '5-6. dersler',               '2 ders',       'Ogrenciye'],
        ['9', 'Urun Degerlendirme Rubriği (A4, 2s)', 'Ogretmen degerlendirme',     '-',            'Ogretmende'],
        ['10', 'Surec Gozlem Formu (A4)',             'Tum unite',                  '-',            'Ogretmende'],
        ['11', 'Ogrenci Oz Degerlendirme (A4)',       '8. ders kapanis',            '10 dk',        'Ogrenciye'],
        ['12', 'Zenginlestirme Paketi',               'Ileri ogrenciler',           'Unite boyunca', 'Istege gore'],
        ['13', 'Destekleme Paketi',                   'Destek gerektiren',          'Unite boyunca', 'Istege gore'],
    ]
    rows = [materyaller_data[0]]
    for row in materyaller_data[1:]:
        rows.append([Paragraph(str(c), S_TD7) for c in row])
    mat_cws = [0.6*cm, 5.5*cm, 3.5*cm, 2.5*cm, 4.9*cm]
    mat_t = Table(rows, colWidths=mat_cws, repeatRows=1)
    mat_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [mat_t, sp(8)]

    story += [blm('Kazanim-Materyal Eslesmesi'), sp(4)]
    kaz_mat_rows = [
        [Paragraph(s, S_TH7) for s in ['Kazanim', 'Ilgili Materyaller']],
        [Paragraph('TT.7.4.1 - 2B/3B arac kullanimi', S_TD7),
         Paragraph('CK1, CK2, CK3, Arac Referans Karti', S_TD7)],
        [Paragraph('TT.7.4.2 - Dijital aracla tasarim', S_TD7),
         Paragraph('CK1 (arka yuz), CK3, Tinkercad modeli', S_TD7)],
        [Paragraph('TT.7.4.3 - Coklu ortam sunusu', S_TD7),
         Paragraph('Tasarim Karti (Ders 4), Tasarim Tanitim Karti (Ders 8)', S_TD7)],
    ]
    km_t = Table(kaz_mat_rows, colWidths=[6*cm, 11*cm], rowHeights=[None, 18, 18, 18], repeatRows=1)
    km_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [km_t, sp(8)]

    story += [blm('Hazirlik Kontrol Listesi'), sp(4)]
    for baslik, maddeler in [
        ('1 Hafta Oncesi', [
            "Sunum slayitlari gozden gecirildi ve ozellesti",
            "Calisma kagitlari (CK1, CK2, CK3) fotokopi edildi",
            "Arac Referans Karti yazdirildi (tercihen lamine)",
            "On Degerlendirme kagitlari fotokopi edildi",
            "Tinkercad hesabi / okul erisimi test edildi",
            "Atolye bilgisayarlarinda Paint acilabildigı dogrulandi",
        ]),
        ('1 Gun Oncesi', [
            "Akilli tahta test edildi",
            "Atolye bilgisayarlari calisir durumda",
            "Izometrik noktali kagit (CK2) hazir",
            "Ogrenci calısmalari icin klasor/dosya yeri belirlendi",
        ]),
        ('Ders Gunu', [
            "Materyaller masalarda/sıralarda hazir",
            "Surec Gozlem Formu elde (tum unite boyunca doldurulacak)",
            "Zaman yonetimi plani gozden gecirildi",
        ]),
    ]:
        story.append(Paragraph(f'<b>{baslik}</b>', S_SMBD))
        story.append(sp(2))
        for m in maddeler:
            story.append(Paragraph(f'( ) {m}', S_SML))
        story.append(sp(6))

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.filename

# ARAC 5: SONRAKI UNITEYE GECIS NOTLARI

def arac5():
    doc   = make_doc('Kapanis5_Gecis_Notlari.pdf', 'Arac 5 - 5. Uniteye Gecis Notlari')
    story = []

    story += [
        arac_baslik('Arac 5', '5. Uniteye Gecis Notlari', 'OGRETMEN REHBERI'),
        sp(6),
        Paragraph('<b>5. Unite: Mimari Tasarim</b>', S_SMBD),
        Paragraph('Sure: 8 ders saati (4 hafta)  -  Kazanim Sayisi: 3', S_SML),
        sp(8),
        blm('4. Unite < - > 5. Unite Kopruler'),
        sp(4),
    ]

    kopru_rows = [
        [Paragraph(s, S_TH7) for s in ['4. Uniteden Gelen', '5. Unitede Derinlesecek']],
        [Paragraph('Ust-on-yan goruntus cikarma', S_TD7),
         Paragraph('Kat plani, kesit, cephe cizimi', S_TD7)],
        [Paragraph('Olcek kullanimi (cm bazinda)', S_TD7),
         Paragraph('Mimari olcek (1/50, 1/100)', S_TD7)],
        [Paragraph('Izometrik cizim', S_TD7),
         Paragraph('3B maket/perspektif', S_TD7)],
        [Paragraph('2B nesneden 3B modele gecis', S_TD7),
         Paragraph('Mimari plan -> yapi maketi', S_TD7)],
        [Paragraph('Kullanici odakli tasarim gerekcesi', S_TD7),
         Paragraph('Mekanin islevi ve kullanicisi', S_TD7)],
    ]
    kopru_t = Table(kopru_rows, colWidths=[8.5*cm, 8.5*cm], repeatRows=1)
    kopru_t.setStyle(TableStyle(list(TABLE_BASE)))
    story += [kopru_t, sp(8)]

    story += [
        blm('Gecis Kopru Sorusu'),
        sp(4),
        Paragraph(
            'Son derste veya 5. unilenin ilk dersinde su soruyu sor:',
            S_SML),
        sp(3),
        Paragraph(
            '"Bu unitede nesnelerin goruntuslerini cikardiniz. Peki bir evin planini (ustten goruntusunu) '
            'cizmis olsaydınız, bu bize ne soylerdı? Iceride kac oda var, kapilar nerede, hangi oda daha buyuk?"',
            S_KAP),
        sp(8),
        blm('Hatirlatilacak Kavramlar (5. Unite Baslamadan)'),
        sp(4),
        Paragraph('<b>5 dakikalik hatirlama turu:</b>', S_LBL),
        sp(2),
        Paragraph('- "Ust goruntus bize ne gosterir?"  -->  Mimari karsiligi: kat plani', S_SML),
        Paragraph('- "On goruntus bize ne gosterir?"  -->  Mimari karsiligi: cephe cizimi', S_SML),
        Paragraph('- "Olcek neydi? 1 cm kagita = gercekte kac cm?"', S_SML),
        sp(8),
        blm('Hazirlik Odevi (5. Unite Oncesi)'),
        sp(4),
        Paragraph(
            '2. dersin sonunda verilebilir (1. derste odev verme):',
            S_SML),
        sp(3),
        Paragraph(
            '"Evinizin ya da okulunuzun herhangi bir odasini tepe noktasindan fotograflarsaniz nasil gorunurdu? '
            'Gozunuzde canlandirin. Cizmeye calisin — cetvel ve olcu sart degil."',
            S_KAP),
        sp(8),
        blm('5. Unite Zumre Ipucu'),
        sp(4),
        Paragraph(
            'Matematik ile ortak calisma firsati yuksek: olcek, oran, alan hesabi. '
            'Matematik ogretmeniyle "olcek" konusunu koordineli islemek mumkun.',
            S_SML),
        sp(8),
        blm('Ogrenci Profilinin 5. Uniteye Yansimasi'),
        sp(4),
        Paragraph('<b>Bu unitede Tinkercad\'de zorlanan ogrenciler icin:</b>', S_SMBD),
        sp(2),
        Paragraph('- 5. unitede mekani fiziksel maket ile somutlastirmaya oncelik verin.', S_SML),
        Paragraph('- Goruntus cikarma rehber materyalini yeniden sunabilirsiniz.', S_SML),
        sp(5),
        Paragraph('<b>Bu unitede ustun performans gosteren ogrenciler icin:</b>', S_SMBD),
        sp(2),
        Paragraph('- Mimari Tasarim zenginlestirme paketini erken onerin.', S_SML),
        Paragraph('- Tinkercad becerilerini daha gelismis araclara kopru olarak sunun.', S_SML),
        sp(10),
        HorizontalLine(TW, COLOR_PRIMARY, 1.0),
        sp(6),
        blm('Kapanis Notu'),
        sp(4),
        Paragraph(
            'Bu paket, 4. Unite\'nin tum materyallerini kapsar. '
            'Toplam 15 dokuman, yaklasik 10 PDF ve 40+ sayfa baskı icerir.',
            S_SML),
        sp(3),
        Paragraph(
            'Unitede ogrenciler hem 2B hem 3B dusunme becerisinin temelini atti. '
            "Tinkercad'i ilk kez kullanan bir 7. sinif ogrencisi icin bu, somut bir teknoloji yetkinligi "
            "ve 'ben de yapabilirim' deneyimidir.",
            S_KAP),
        sp(4),
        Paragraph(
            'Bir sonraki unitede iyi dersler, anlamli tasarimlar ve guclu baglantilar dilerim.',
            S_SMIT),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return doc.filename

# ANA

if __name__ == '__main__':
    import pypdf

    PDF_PATH = os.path.join(OUT, 'U4_PDF_Yansitma_ve_Kapanis.pdf')

    parcalar = []
    for fn in [arac1, arac2, arac3, arac4, arac5]:
        path = fn()
        parcalar.append(path)

    writer = pypdf.PdfWriter()
    for src in parcalar:
        reader = pypdf.PdfReader(src)
        for page in reader.pages:
            writer.add_page(page)
    with open(PDF_PATH, 'wb') as f:
        writer.write(f)

    for tmp in parcalar:
        try:
            os.remove(tmp)
        except Exception:
            pass

    print(f'PDF uretildi: {PDF_PATH}')
