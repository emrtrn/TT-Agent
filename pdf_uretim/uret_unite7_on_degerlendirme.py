"""
7. Unite -- On Degerlendirme PDF ureticisi (birlesik)
Form 1 (Arac 1: Zihin Haritasi + Arac 2: Tanilama Testi) +
Form 2 (Arac 3: Acik Uclu + Arac 4: Eslestirme + Arac 5: Bosluk Doldurma)
Cikti: units/7_sinif/unit7/U7_PDF_02_On_Degerlendirme.pdf
Calistir: python pdf_uretim/uret_unite7_on_degerlendirme.py
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

ROOT     = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit7')
PDF_PATH = os.path.join(ROOT, 'U7_PDF_02_On_Degerlendirme.pdf')
UI = '7. Unite: Enerjinin Donusumu ve Tasarim  -  Teknoloji ve Tasarim  -  7. Sinif'

S_BAS  = ParagraphStyle('u7od_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u7od_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u7od_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u7od_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u7od_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u7od_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u7od_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u7od_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u7od_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)
S_KELL = ParagraphStyle('u7od_KELL', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=5, borderWidth=0.5,
                         borderColor=COLOR_LIGHT_GREY, leftIndent=4, rightIndent=4,
                         spaceBefore=3, spaceAfter=3)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


SORULAR = [
    (
        'Bir nehirde akan su elektrik uretmek icin kullaniliyor. Suyun akarken sahip oldugu enerji turu asagidakilerden hangisidir?',
        ['A) Kimyasal enerji', 'B) Kinetik enerji', 'C) Potansiyel enerji', 'D) Ses enerjisi'],
    ),
    (
        'Bir termik santralde komur yakildifinda asagidaki enerji donusum zinciri hangi secenekte dogru verilmistir?',
        ['A) Elektrik enerjisi → Isi enerjisi → Kimyasal enerji',
         'B) Kinetik enerji → Isi enerjisi → Elektrik enerjisi',
         'C) Kimyasal enerji → Isi enerjisi → Elektrik enerjisi',
         'D) Potansiyel enerji → Kimyasal enerji → Isi enerjisi'],
    ),
    (
        'Asagidaki tanimlardan hangisi "yenilenebilir enerji kaynagi"ni dogru aciklar?',
        ['A) Dogada kendiliğinden yenilenen, kullandikca tukenmeyen enerji kaynaklari',
         'B) Fabrikada uretilen ve satin alinan enerji turleri',
         'C) Yalnizca gunes ve rüzgardan elde edilen enerji',
         'D) Fosil yakitlardan daha pahali olan enerji kaynaklari'],
    ),
    (
        'Gunes enerjisi hakkinda asagidakilerden hangisi dogrudir?',
        ['A) Yalnizca sicak ulkelerde kullanilabilir',
         'B) Sadece elektrik uretmek icin kullanilir',
         'C) Uretimi sirasinda hic bakim gerektirmez',
         'D) Tukenme riski olmayan, temiz bir enerji kaynaktidir'],
    ),
    (
        'Kuresel isinmanin en onemli nedeni asagidakilerden hangisidir?',
        ['A) Gunesin giderek daha fazla enerji uretmesi',
         'B) Fosil yakitlarin yakilmasiyla atmosfere salinen sera gazlari',
         'C) Ozon tabakasindaki deliğin buyumesi',
         'D) Ormanların cok hizli buyumesi'],
    ),
    (
        'Asagidakilerden hangisi fosil yakit degildir?',
        ['A) Komur', 'B) Petrol', 'C) Jeotermal enerji', 'D) Dogalgaz'],
    ),
    (
        '"Enerji verimliligi yuksek" bir urun ne anlama gelir?',
        ['A) Ayni isi daha az enerji tuketerek yapan urun',
         'B) Cok fazla enerji ureten cihaz',
         'C) Yalnizca gunes enerjisiyle calisan urun',
         'D) Tasarimi karmasik, ama dayanikli urun'],
    ),
    (
        'Bir tasarimci yeni bir ev aydinlatma sistemi tasarliyor. Surdurulebilirlik acisindan en dogru enerji kaynagi tercihi hangisi olur?',
        ['A) Komurle calisan termik santralden beslenen sistem',
         'B) Dogalgaz jeneratoru',
         'C) Aku depolama sistemi olmayan gunes paneli',
         'D) Gunes paneli + aku depolama sistemli, sebeke bagimsiz cozum'],
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
        '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>ENERJI</b> ve <b>TASARIM</b>. '
        'Bu kelimeleri duyduğunda aklina ne geliyor? Kavramlar, nesneler, ornekler, sorular... '
        'Aklina gelen her seyi yaz ve oklarla bagla.  <b>Sure: 6 dakika</b>',
        S_YON))
    E.append(vsp(0.15))
    E.append(MindMapCanvas('ENERJI  TASARIM', width=17 * cm, height=9.5 * cm, num_branches=8))
    E.append(vsp(0.2))
    E.append(Paragraph(
        '<b>Son soru:</b> Sence enerji ile tasarim birbiriyle baglantili mi? Neden?',
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
    E.append(Paragraph('<b>Sure: 7 dakika</b>', S_YON))
    E.append(vsp(0.15))

    acik = [
        ('Sabahtan aksama kadar gunluk hayatinda en az 5 farkli enerji donusumu gerceklesiyor. '
         'Bunlardan ikisini yaz ve hangi enerji turlerinin birbiriyle donustuğunu acikla.',
         'Ornek: Telefonumu sarja takiyorum → elektrik enerjisi → kimyasal enerji (pil)'),
        ("Turkiye'nin en cok hangi yenilenebilir enerji kaynagini kullandigini dusunuyorsun? "
         'Neden bu kaynagin avantajli oldugunu acikla.', None),
        ('"Kuresel isinma" derken ne anliyorsun? Bunun nedenini ve insanliga etkisini kendi cumlelenle acikla.', None),
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
        '<b>Yonerge:</b> Sol sutundaki kavramlari sag sutundaki tanimlarla eslestir. Her tanim yalnizca bir kez kullanilir.  '
        '<b>Sure: 5 dakika</b>',
        S_YON))
    E.append(vsp(0.1))

    E.append(Paragraph('<b>Bolum A — Kavram ve Tanim</b>', S_BLM))
    bolum_a = [
        ['No', 'Kavram', 'Cevap', 'Harf', 'Tanim'],
        ['1', 'Kinetik enerji',     '.....', 'A', 'Bir kisinin veya kurulusun faaliyetleri sonucu atmosfere salinen toplam CO2 miktari'],
        ['2', 'Sera gazi',          '.....', 'B', 'Atmosferde birikerek isinin uzaya kacmasini engelleyen gaz (ornek: CO2, metan)'],
        ['3', 'Enerji donusumu',    '.....', 'C', 'Bitkisel ve hayvansal atiklarin yakilmasi veya fermantasyonuyla elde edilen enerji'],
        ['4', 'Karbon ayak izi',    '.....', 'D', 'Hareket halindeki bir nesnenin sahip oldugu enerji'],
        ['5', 'Biyokutle enerjisi', '.....', 'E', 'Bir enerji turunun baska bir enerji turune gecmesi'],
    ]
    t_a = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_a],
        colWidths=[0.7*cm, 3.5*cm, 1.2*cm, 1.0*cm, 10.6*cm],
    )
    t_a.setStyle(TABLO_STILI)
    E.append(t_a)
    E.append(vsp(0.15))

    E.append(Paragraph('<b>Bolum B — Enerji Kaynagi ve Tur</b>', S_BLM))
    bolum_b = [
        ['No', 'Enerji Kaynagi',      'Cevap', 'Harf', 'Tur'],
        ['1', 'Gunes paneli',          '.....', 'A', 'Yenilenemez — fosil yakit'],
        ['2', 'Komur santrali',        '.....', 'B', 'Yenilenebilir — yeralti isisi'],
        ['3', 'Ruzgar turbini',        '.....', 'C', 'Yenilenebilir — gunes isinimi'],
        ['4', 'Jeotermal santral',     '.....', 'D', 'Yenilenebilir — suyun kinetik/potansiyel enerjisi'],
        ['5', 'Baraj (hidroelektrik)', '.....', 'E', 'Yenilenebilir — hava hareketi'],
    ]
    t_b = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_b],
        colWidths=[0.7*cm, 4.0*cm, 1.2*cm, 1.0*cm, 10.1*cm],
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
        '<i>Kelime Havuzu: fosil yakit · kuresel isinma · enerji verimliligi · yenilenebilir · '
        'potansiyel · karbon ayak izi · sera gazi</i>',
        S_KELL))
    E.append(vsp(0.1))

    bosluklar = [
        'Bir kulenin tepesinde bekleyen kaya, asagi dusmeden once <b>_________________</b> enerjisine sahiptir.',
        'Komur, petrol ve dogalgaz gibi kaynaklar milyonlarca yilda olustugu icin <b>_________________</b> olarak adlandirilir.',
        'Gunes, ruzgar ve su gibi dogada kendiliğinden yenilenen kaynaklar <b>_________________</b> enerji olarak bilinir.',
        "Atmosferdeki CO2 ve metan gibi gazlar, Dunya'nin isisinin uzaya kacmasini engeller; bu gazlara <b>_________________</b> denir.",
        'Yeryuzu sicakliginin insan faaliyetleri nedeniyle yavas yavas artmasi olayina <b>_________________</b> adi verilir.',
        'Ayni isi daha az enerji kullanarak yapan urunler <b>_________________</b> acisindan ustundur.',
        'Bir bireyin veya toplumun faaliyetleri sonucu atmosfere salinen toplam CO2\'ye <b>_________________</b> denir.',
    ]
    for i, metin in enumerate(bosluklar, 1):
        blok = [Paragraph(f'<b>{i}.</b>  {metin}', S_LBL), vsp(0.05)]
        E.append(KeepTogether(blok))

    return E


S_SML  = ParagraphStyle('u7od_SML2', fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT, leading=11)
S_LBL  = ParagraphStyle('u7od_LBL2', fontName='TR-Regular', fontSize=8.5, textColor=COLOR_TEXT, leading=11)


if __name__ == '__main__':
    doc = create_doc(PDF_PATH, title='On Degerlendirme', unite_info=UI)
    elemanlar = form1_elemanlar() + form2_elemanlar()
    doc.build(elemanlar, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF uretildi: {PDF_PATH}')
