"""
9. Unite -- On Degerlendirme PDF ureticisi (birlesik)
Form 1 (Arac 1: Zihin Haritasi + Arac 2: Tanilama Testi) +
Form 2 (Arac 3: Acik Uclu + Arac 4: Eslestirme + Arac 5: Bosluk Doldurma)
Cikti: units/7_sinif/unit9/U9_PDF_02_On_Degerlendirme.pdf
Calistir: python pdf_uretim/uret_unite9_on_degerlendirme.py
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

ROOT     = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit9')
PDF_PATH = os.path.join(ROOT, 'U9_PDF_02_On_Degerlendirme.pdf')
UI = '9. Unite: Yapay Zeka ve Akilli Urunler  -  Teknoloji ve Tasarim  -  7. Sinif'

S_BAS  = ParagraphStyle('u9od_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u9od_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u9od_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u9od_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u9od_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u9od_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u9od_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u9od_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u9od_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)
S_KELL = ParagraphStyle('u9od_KELL', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=5, borderWidth=0.5,
                         borderColor=COLOR_LIGHT_GREY, leftIndent=4, rightIndent=4,
                         spaceBefore=3, spaceAfter=3)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


SORULAR = [
    (
        'Yapay zeka (YZ) kavramini en iyi aciklayan ifade hangisidir?',
        ['A) Insanlara benzeyen fiziksel robotlarin genel adi',
         'B) Bilgisayar programlarinin ogrenme, anlama ve karar verme gibi insan ozelliklerini '
         'taklit etmesini saglayan teknoloji',
         'C) Internet baglantisi gerektiren her tur mobil uygulama',
         'D) Sosyal medya platformlarinin yonetim sistemi'],
    ),
    (
        'Makine ogrenmesi ne anlama gelir?',
        ['A) Fabrika makinelerinin birbirini otomatik olarak tamir etmesi',
         'B) Bilgisayarin buyuk miktarda veriden oruntular cikararak belirli gorevlerde '
         'kendi kendine gelismesi',
         'C) Insanlarin bilgisayara geleneksel ders anlatimi yontemiyle bilgi aktarmasi',
         'D) Makinelerin calisma hizlarini optimize etmesi'],
    ),
    (
        'Derin ogrenme (deep learning) ile ilgili hangisi dogrudir?',
        ['A) Derin ogrenme, kitap okuyarak gerceklesen bir ogrenme surecidir',
         'B) Derin ogrenme, katmanli yapay sinir aglarini kullanarak buyuk verilerden '
         'anlam cikaran bir makine ogrenmesi yaklasimdir',
         'C) Derin ogrenme yalnizca matematik problemleri icin kullanilir',
         'D) Derin ogrenme, robotlarin hareket etmesini saglayan mekanik bir sistemdir'],
    ),
    (
        'Asagidakilerden hangisi yapay zeka kullanan bir uygulama ornEgidir?',
        ['A) Toplama, cikarma islemi yapan basit bir hesap makinesi uygulamasi',
         'B) Belge olusturmak icin kullanilan bir metin duzenleyici program',
         'C) Muzik uygulamasinin dinleme gecmisine gore "Sana Ozel" calma listesi olusturmasi',
         'D) Saati gosteren dijital bir alarmli saat uygulamasi'],
    ),
    (
        '"Istem muhendisligi" (prompt engineering) ne anlama gelir?',
        ['A) Bir yapay zeka modelini sifirdan yazilim kodlariyla programlama',
         'B) Yapay zekadan dogru ve ise yarar sonuclar elde etmek icin etkili talimatlar '
         '(istemler) yazma becerisi',
         'C) Bir bilgisayarin donanim bilesEnlerini tasarlama ve uretme sureci',
         'D) Yapay zeka araclarini yalnizca Ingilizce dilinde kullanma zorunlulugu'],
    ),
    (
        'Yapay zekanin "hAluSinasyon" yapmasi ne demektir?',
        ['A) Yapay zekanin ekran goruntusU alamamasi ve goruntu isleme hatasi vermesi',
         'B) Yapay zekanin cok fazla veri islemediginde asiri yavaslamasi',
         'C) Yapay zekanin var olmayan, yanlis veya uydurulmus bilgileri gercEkmis gibi '
         'guvenle sunmasi',
         'D) Yapay zekanin internet baglantisi kesildiginde calismayi durdurmasi'],
    ),
    (
        'Yapay zekanin insanlara gore en belirgin avantaji nedir?',
        ['A) Her konuda insan gibi ozgun ve yaratici dusunebilmesi',
         'B) Buyuk veri kumelerini cok hizla isleyerek belirli oruntuleri insandan daha '
         'hizli bulabilmesi',
         'C) Duygusal zekasinin insandan ustun olmasi',
         'D) Her kosulda her zaman dogru ve guvenilir sonuc uretmesi'],
    ),
    (
        '"Akilli urun" kavramini en iyi tanimlayan ifade hangisidir?',
        ['A) Pahali ve modern bir gorunume sahip olan her teknolojik urun',
         'B) Yalnizca internete baglanabilen her elektronik cihaz',
         'C) Algilayicilar (sensorler) araciligIyla cevresini algilayan, bu veriyi isleyen '
         've duruma gore tepki veren urun',
         'D) Siyah renkte tasarlanmis ve minimum malzeme kullanilan urunler'],
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
        '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>YAPAY ZEKA</b> ve <b>AKILLI URUN</b>. '
        'Bu kelimeleri duyduğunda aklina hangi kelimeler, kavramlar, nesneler, ornekler geliyor? '
        'Aklina gelen her seyi oklarla baglayarak yaz. Ne kadar cok, o kadar iyi!  '
        '<b>Sure: 5 dakika</b>',
        S_YON))
    E.append(vsp(0.15))
    E.append(MindMapCanvas('YAPAY ZEKA  AKILLI URUN', width=17 * cm, height=9.5 * cm, num_branches=8))
    E.append(vsp(0.2))
    E.append(Paragraph(
        '<b>Son soru:</b> Sence yapay zeka ile akilli urun birbiriyle nasil iliskilidir?',
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
        'sonra neden o secenegi sectiginizi aciklayin. Bilmedigin soruya "Tahminim su:" diye basla.  '
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
    E.append(Paragraph(
        '<b>Sure: 7 dakika</b>  — Tum sorulari yanitlamak zorunda degilsin; '
        'en rahat hissettigin sorudan basla.',
        S_YON))
    E.append(vsp(0.15))

    acik = [
        ('Yapay zekay kendi cumlelerinle tanimla. Sence yapay zeka nedir?', None),
        ('Gunluk hayatinda yapay zeka kullanan bir uygulama ya da urun var mi? '
         'Varsa hangisi? Nasil calistigini tahmin et.', None),
        ('Sence yapay zekanin bir zarari veya tehlikesi olabilir mi? Neden?', None),
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
        ['1', 'Yapay Zeka',        '.....', 'A', 'Bir problemi cozmek icin adim adim izlenen kural dizisi'],
        ['2', 'Makine Ogrenmesi',  '.....', 'B', "YZ'nin var olmayan veya yanlis bilgileri gercEkmis gibi sunmasi"],
        ['3', 'Halu Sinasyon',     '.....', 'C', 'Bilgisayarlarin ogrenme, anlama ve karar verme gibi insana ozgu gorevleri yapabilmesini saglayan teknoloji'],
        ['4', 'Istem (Prompt)',    '.....', 'D', "YZ'ye verilen yazili talimat veya soru"],
        ['5', 'Algoritma',         '.....', 'E', 'Verilerden oruntUler cikararak kendi kendine belirli gorevlerde gelisen YZ yaklasimi'],
    ]
    t_a = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_a],
        colWidths=[0.7*cm, 3.5*cm, 1.2*cm, 1.0*cm, 10.6*cm],
    )
    t_a.setStyle(TABLO_STILI)
    E.append(t_a)
    E.append(vsp(0.15))

    E.append(Paragraph('<b>Bolum B — YZ Uygulamasi ve Aciklama</b>', S_BLM))
    bolum_b = [
        ['No', 'YZ Uygulamasi',    'Cevap', 'Harf', 'Aciklama'],
        ['1', 'Oneri Sistemi',      '.....', 'A', 'Surucusuz araclar veya teslimat robotlari gibi cevreyi algilayarak bagimsiz hareket eden sistemler'],
        ['2', 'Ses Tanima',         '.....', 'B', 'Siri veya Alexa gibi sesli asistanlarin konusmay anlayip yanit vermesi'],
        ['3', 'Goruntu Tanima',     '.....', 'C', 'Otomatik yazim duzeltme ve ceviri uygulamalari'],
        ['4', 'Dogal Dil Isleme',   '.....', 'D', "Netflix veya Spotify'in izleme/dinleme gecmisine gore yeni icerik onermesi"],
        ['5', 'Otonon Sistem',      '.....', 'E', 'Yuz kilidi veya fotograf uygulamalarinin nesneleri ve yuzleri tanimas'],
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
        '<i>Kelime Havuzu: yapay zeka · makine ogrenmesi · derin ogrenme · istem · '
        'algoritma · akilli urun · halu sinasyon · veri</i>',
        S_KELL))
    E.append(vsp(0.1))

    bosluklar = [
        'Bilgisayar programlarinin ogrenme, anlama ve karar verme gibi insan ozelliklerini taklit etmesini saglayan teknolojiye <b>_________________</b> denir.',
        'Buyuk miktarda veriden oruntUler cikararak kendi kendine gelisen YZ yaklasimina <b>_________________</b> adi verilir.',
        'Katmanli yapay sinir aglarini kullanan, goruntu ve ses tanima gibi karmasik gorevlerde basarili olan yaklasim <b>_________________</b> olarak bilinir.',
        'Yapay zekaya verilen yazili talimat veya soruya <b>_________________</b> denir.',
        "YZ'nin bir sorunu adim adim nasil cozecEgini belirleyen kural dizisi <b>_________________</b> olarak adlandirilir.",
        'Algilayicilarla cevresini algilayan, bu veriyi isleyen ve duruma gore tepki veren urunE <b>_________________</b> denir.',
        'Yapay zekanin var olmayan veya yanlis bilgileri gercEkmis gibi sunmasina <b>_________________</b> adi verilir.',
        "YZ modellerinin ogrenmesi icin kullanilan, ornekler ve bilgilerden olusan hammaddeye <b>_________________</b> denir.",
    ]
    for i, metin in enumerate(bosluklar, 1):
        blok = [Paragraph(f'<b>{i}.</b>  {metin}', S_LBL), vsp(0.05)]
        E.append(KeepTogether(blok))

    E.append(vsp(0.2))
    E.append(sep())
    E.append(vsp(0.1))
    E.append(Paragraph('<b>Sana Gore</b> (istersen cevapla, istersen bos birak):', S_SMBD))
    E.append(vsp(0.05))
    E.append(Paragraph(
        'Daha once hic bir yapay zeka araci (sohbet botu, goruntu olusturucu, sesli asistan vb.) kullandin mi?',
        S_SML))
    E.append(WritingLines(num_lines=2))
    E.append(Paragraph('Bu unitede en cok merak ettigin konu nedir?', S_SML))
    E.append(WritingLines(num_lines=1))

    return E


if __name__ == '__main__':
    doc = create_doc(PDF_PATH, title='On Degerlendirme', unite_info=UI)
    elemanlar = form1_elemanlar() + form2_elemanlar()
    doc.build(elemanlar, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF uretildi: {PDF_PATH}')
