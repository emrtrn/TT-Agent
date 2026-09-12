"""
8. Unite -- On Degerlendirme PDF ureticisi (birlesik)
Form 1 (Arac 1: Zihin Haritasi + Arac 2: Tanilama Testi) +
Form 2 (Arac 3: Acik Uclu + Arac 4: Eslestirme + Arac 5: Bosluk Doldurma)
Cikti: units/7_sinif/unit8/U8_PDF_02_On_Degerlendirme.pdf
Calistir: python pdf_uretim/uret_unite8_on_degerlendirme.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)

from pdf_style import (
    register_fonts, add_page_number, create_doc,
    make_student_info_header,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_ACCENT,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY,
    WritingLines, MindMapCanvas, HorizontalLine,
)

register_fonts()

ROOT     = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit8')
PDF_PATH = os.path.join(ROOT, 'U8_PDF_02_On_Degerlendirme.pdf')
UI = '8. Unite: Butunlesik Ogrenme: STEAM  -  Teknoloji ve Tasarim  -  7. Sinif'

S_BAS  = ParagraphStyle('u8od_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u8od_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u8od_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u8od_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u8od_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u8od_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u8od_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u8od_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u8od_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)
S_KELL = ParagraphStyle('u8od_KELL', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=5, borderWidth=0.5,
                         borderColor=COLOR_LIGHT_GREY, leftIndent=4, rightIndent=4,
                         spaceBefore=3, spaceAfter=3)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


SORULAR = [
    (
        'STEAM kisaltmasindaki <b>"E"</b> harfi hangi disiplini temsil eder?',
        ['A) Ekoloji', 'B) Ekonomi', 'C) Muhendislik', 'D) Elektronik'],
    ),
    (
        'Bir grup ogrenci okullarindaki su israfini onlemek icin bir sistem tasarliyor. '
        'Bu proje STEAM\'in hangi ozelligini en iyi gostermektedir?',
        ['A) Tek bir disiplin yeterlidir',
         'B) Sanat bileseni gereksizdir',
         'C) Birden fazla disiplin birlikte calisir',
         'D) Matematik bileseni yoktur'],
    ),
    (
        'Muhendislik tasarim surecinin <b>ilk adimi</b> hangisidir?',
        ['A) Malzeme secmek', 'B) Problem belirlemek',
         'C) Prototip uretmek', 'D) Sunum yapmak'],
    ),
    (
        'Bir projede <b>"paydas"</b> kimdir?',
        ['A) Projeyi degerlendiren ogretmen',
         'B) Problemden etkilenen veya cozumunden yararlanan kisi/grup',
         'C) Proje ekibinin lideri',
         'D) Yalnizca problemi yaratan kisi'],
    ),
    (
        '<b>"Prototip"</b> kavrami icin en dogru aciklama hangisidir?',
        ['A) Satisa hazir final urun',
         'B) Yalnizca bilgisayarda yapilan cizim',
         'C) Bir tasarimin test edilmek uzere yapilan ilk deneme modeli',
         'D) Yalnizca profesyonellerin yapabilecegi model'],
    ),
    (
        'STEAM yaklasiminda <b>Sanat (Arts)</b> bilesEninin temel katkisi nedir?',
        ['A) Sarki soylemek ve dans etmek',
         'B) Yalnizca resim cizmek',
         'C) Sanat tarihi arastirmak',
         'D) Estetik, tasarim ve yaraticilik'],
    ),
    (
        'Grup calismasinda <b>gorev dagilimi</b> yapmanin temel amaci nedir?',
        ['A) Bazi ogrencilerin daha az calismasini saglamak',
         'B) Her uyenin sorumlulugunu netlestirerek verimliligi artirmak',
         'C) Ogretmenin isini kolaylastirmak',
         'D) Projeyi bireysel calismaya donusturmek'],
    ),
    (
        'Asagidakilerden hangisi gercek bir STEAM projesine <b>en iyi ornek</b> olabilir?',
        ['A) Matematik testi cozmek',
         'B) Siir ezberlemek',
         'C) Tek basina bir resim cizmek',
         'D) Gunes enerjisiyle calisan bir bahce sulama sistemi tasarlamak'],
    ),
]

TABLO_STILI = TableStyle([
    ('FONTNAME', (0, 0), (-1, 0), 'TR-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'TR-Regular'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('LEADING', (0, 0), (-1, -1), 11),
    ('BACKGROUND', (0, 0), (-1, 0), COLOR_LIGHT),
    ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_PRIMARY),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_VERY_LIGHT, None]),
    ('GRID', (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('ALIGN', (2, 0), (2, -1), 'CENTER'),
])


def form1_elemanlar():
    E = []
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu calisma not icin degildir. Dogru ya da yanlis cevap yoktur. Aklina geleni ictenlikle yaz!',
        S_NOT))
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.2))
    E.append(Paragraph('ARAC 1: ZIHIN HARITASI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagida bir anahtar kelime var: <b>STEAM</b>. '
        'Bu kelimeyi duyduğunda aklina hangi sozcukler, kavramlar, ornekler, dersler geliyor? '
        'Her birini oklarla merkeze baglayarak yaz. Istedigin kadar dal ekleyebilirsin.  '
        '<b>Sure: 5 dakika</b>',
        S_YON))
    E.append(vsp(0.15))
    E.append(MindMapCanvas('STEAM', width=17 * cm, height=9.5 * cm, num_branches=8))
    E.append(vsp(0.2))
    E.append(Paragraph(
        '<b>Son soru:</b> Sence STEAM\'deki bes disiplin birbiriyle iliskili midir? Neden?',
        S_SMBD))
    E.append(WritingLines(num_lines=2))
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Ogretmenin bu kagidi toplayacak ve unite sonunda sana geri verecek.',
        S_NOT))
    E.append(sep())
    E.append(PageBreak())

    E.append(make_student_info_header())
    E.append(vsp(0.2))
    E.append(Paragraph('ARAC 2: IKI ASAMALI TANILAMA TESTI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Her sorunun iki kismi var. Once dogru secenegi isaretleyin (A/B/C/D), '
        'sonra neden o secenegi sectiginizi aciklayin. Bilmedigin soruya "Emin degilim ama..." diye basla.  '
        '<b>Sure: 12 dakika</b>',
        S_YON))
    E.append(vsp(0.15))

    for i, (soru, secenekler) in enumerate(SORULAR, 1):
        blok = []
        blok.append(Paragraph(f'<b>Soru {i}.</b> {soru}', S_SORU))
        for s in secenekler:
            blok.append(Paragraph(s, S_OPT))
        blok.append(vsp(0.1))
        blok.append(Paragraph('<b>Neden bu secenegi sectin?</b>', S_SMBD))
        blok.append(WritingLines(num_lines=1))
        blok.append(sep())
        blok.append(vsp(0.05))
        E.append(KeepTogether(blok))
    return E


def form2_elemanlar():
    E = []
    E.append(PageBreak())
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu calisma not icin degildir. Bildiklerini durustce yaz — yanlis cevap yok!',
        S_NOT))
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.2))

    # ARAC 3
    E.append(Paragraph('ARAC 3: ACIK UCLU SORULAR', S_BAS))
    E.append(Paragraph('<b>Sure: 7 dakika</b>  — Tum sorulari yanitlamak zorunda degilsin; en rahat hissettigin sorudan basla.', S_YON))
    E.append(vsp(0.15))

    acik = [
        ('STEAM nedir? Kendi cumlelenle acikla.', None),
        ('Gunluk hayatinda karsilastigin ve STEAM kullanilarak cozulebilecek bir problemi dusun. '
         'Bu problemi tarif et ve hangi STEAM disiplinlerini kullanabileceğini yaz.', None),
        ('Daha once bir grupla proje yaptiysan: En cok hangi konuda zorlandin? '
         'Bu zorluğu nasil astin?', None),
        ('Bir muhendis, bir sanatci ve bir matematikci ayni projede nasil is birligi yapabilir? '
         'Kisa bir ornek ver.', None),
    ]
    for i, (soru, ornek) in enumerate(acik, 1):
        blok = []
        blok.append(Paragraph(f'<b>Soru {i}.</b> {soru}', S_SORU))
        if ornek:
            blok.append(Paragraph(f'<i>{ornek}</i>', S_NOT))
        blok.append(WritingLines(num_lines=3))
        blok.append(sep())
        blok.append(vsp(0.05))
        E.append(KeepTogether(blok))

    E.append(vsp(0.1))

    # ARAC 4
    E.append(Paragraph('ARAC 4: ESLESTIRME TESTI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Sol sutundaki kavramlari sag sutundaki tanimlarla eslestir. '
        'Her tanim yalnizca bir kez kullanilir.  <b>Sure: 5 dakika</b>',
        S_YON))
    E.append(vsp(0.1))

    E.append(Paragraph('<b>Bolum A — Kavram ve Tanim</b>', S_BLM))
    bolum_a = [
        ['No', 'Kavram', 'Cevap', 'Harf', 'Tanim'],
        ['1', 'STEAM',                         '.....', 'A', 'Bir tasarim problemini adim adim cozmek icin izlenen yapilandirilmis surec'],
        ['2', 'Prototip',                       '.....', 'B', 'Elestiri yapilmadan mumkun oldugunda fazla fikir uretme yontemi'],
        ['3', 'Paydas',                         '.....', 'C', 'Bir tasarimin test edilmek uzere yapilan ilk deneme modeli'],
        ['4', 'Muhendislik tasarim sureci',     '.....', 'D', 'Bilim, Teknoloji, Muhendislik, Sanat ve Matematikten olusan butunlesik ogrenme'],
        ['5', 'Beyin firtinasi',                '.....', 'E', 'Bir problemden etkilenen veya cozumunden yararlanan kisi ya da grup'],
    ]
    t_a = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_a],
        colWidths=[0.7*cm, 3.8*cm, 1.2*cm, 1.0*cm, 10.3*cm],
    )
    t_a.setStyle(TABLO_STILI)
    E.append(t_a)
    E.append(vsp(0.15))

    E.append(Paragraph('<b>Bolum B — STEAM Rolu ve Gorev</b>', S_BLM))
    bolum_b = [
        ['No', 'Rol',              'Cevap', 'Harf', 'Gorev'],
        ['1', 'Bilim (S)',          '.....', 'A', 'Projenin gorsel tasarimini, renklerini ve estetik duzenini belirlemek'],
        ['2', 'Teknoloji (T)',      '.....', 'B', 'Olcumleri yapmak, malzeme maliyetini hesaplamak, veri analizi yapmak'],
        ['3', 'Muhendislik (E)',    '.....', 'C', 'Dijital araclari kullanmak, belgeleme yapmak, yazilim/uygulama secmek'],
        ['4', 'Sanat (A)',          '.....', 'D', 'Yapimi planlamak, malzemeleri birlestirmek, sistemin calismasini saglamak'],
        ['5', 'Matematik (M)',      '.....', 'E', 'Projenin bilimsel temelini arastirmak, deneyleri planlamak, neden isE yaradigini aciklamak'],
    ]
    t_b = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_b],
        colWidths=[0.7*cm, 3.5*cm, 1.2*cm, 1.0*cm, 10.6*cm],
    )
    t_b.setStyle(TABLO_STILI)
    E.append(t_b)
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.1))

    # ARAC 5
    E.append(Paragraph('ARAC 5: BOSLUK DOLDURMA', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Kutucuktaki kelimelerden uygun olanlari secererek cumleleri tamamla. '
        'Her kelime yalnizca bir kez kullanilir.  <b>Sure: 4 dakika</b>',
        S_YON))
    E.append(vsp(0.1))
    E.append(Paragraph(
        '<i>Kelime Havuzu: Bilim · Muhendislik · Sanat · prototip · paydas · '
        'beyin firtinasi · disiplinler arasi · problem</i>',
        S_KELL))
    E.append(vsp(0.1))

    bosluklar = [
        'STEAM; <b>_________________</b> , Teknoloji, <b>_________________</b> , <b>_________________</b> ve Matematigi butunlestiren bir ogrenme yaklasimdir.',
        'Bir tasarimin test edilmek uzere yapilan ilk deneme modeline <b>_________________</b> denir.',
        'Elestiri yapilmadan mumkun olduğunca cok fikir uretme yontemine <b>_________________</b> denir.',
        'Bir problemden etkilenen ya da cozumunden yararlanan kisiye <b>_________________</b> adi verilir.',
        'STEAM projelerinde farkli derslerden gelen bilgiler bir arada kullanildiği icin bu yaklasim <b>_________________</b> olarak nitelendirilir.',
        'Tasarim odakli surecte ilk adim, cozulecek bir <b>_________________</b> belirlemektir.',
    ]
    for i, metin in enumerate(bosluklar, 1):
        blok = [Paragraph(f'<b>{i}.</b>  {metin}', S_LBL), vsp(0.05)]
        E.append(KeepTogether(blok))

    E.append(vsp(0.2))
    E.append(sep())
    E.append(vsp(0.1))
    E.append(Paragraph('<b>Yansitma:</b> Bu unite hakkinda merak ettigin bir sey var mi? Varsa yaz:', S_SMBD))
    E.append(WritingLines(num_lines=2))

    return E


if __name__ == '__main__':
    doc = create_doc(PDF_PATH, title='On Degerlendirme', unite_info=UI)
    elemanlar = form1_elemanlar() + form2_elemanlar()
    doc.build(elemanlar, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF uretildi: {PDF_PATH}')
