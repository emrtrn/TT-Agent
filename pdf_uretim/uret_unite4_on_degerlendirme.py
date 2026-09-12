"""
4. Unite -- On Degerlendirme PDF ureticisi
Tek PDF: Ogrenci Kagidi 1 (Zihin Haritasi + Tanilama Testi) + Kagit 2 (Acik Uclu + Eslestirme + Bosluk)
Calistir: python pdf_uretim/uret_unite4_on_degerlendirme.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable,
)

from pdf_style import (
    register_fonts, add_page_number, create_doc,
    make_student_info_header, section_title, yonerge_box,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, MindMapCanvas, HorizontalLine,
)

register_fonts()

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit4')
PDF_PATH = os.path.join(ROOT, 'U4_PDF_02_On_Degerlendirme.pdf')
UI = '4. Unite: Bilgisayar Destekli Tasarim  -  Teknoloji ve Tasarim  -  7. Sinif'

S_BAS  = ParagraphStyle('u4od_BAS',  fontName='TR-Bold',    fontSize=12, textColor=COLOR_PRIMARY,   leading=15, spaceBefore=8, spaceAfter=3)
S_BLM  = ParagraphStyle('u4od_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=6, spaceAfter=2)
S_LBL  = ParagraphStyle('u4od_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u4od_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u4od_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u4od_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=5, spaceAfter=2)
S_OPT  = ParagraphStyle('u4od_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u4od_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12, backColor=COLOR_VERY_LIGHT,
                         borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u4od_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)
S_KELL = ParagraphStyle('u4od_KELL', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=5, borderWidth=0.5,
                         borderColor=COLOR_LIGHT_GREY, leftIndent=4, rightIndent=4,
                         spaceBefore=3, spaceAfter=3)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


# =============================================================================
# KAGIT 1: Zihin Haritasi + Tanilama Testi
# =============================================================================

def kagit_1_elemanlar():
    E = []

    # --- SAYFA 1: Zihin Haritasi ---
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu calisma not icin degildir. Bildigini duerustce yaz — yanlis cevap olmaz!',
        S_NOT,
    ))
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.2))

    E.append(Paragraph('ARAC 1: ZIHIN HARITASI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>2B TASARIM</b> ve <b>3B TASARIM</b>. '
        'Bu kelimeleri duyduğunda aklına hangi kelimeler, kavramlar, nesneler, ornekler geliyor? '
        'Aklina gelen her seyi oklarla baglayarak yaz. Ne kadar cok, o kadar iyi!  '
        '<b>Sure: 5 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.2))

    mm_table = Table(
        [[
            MindMapCanvas('2B TASARIM', width=8.2 * cm, height=8.0 * cm, num_branches=8),
            MindMapCanvas('3B TASARIM', width=8.2 * cm, height=8.0 * cm, num_branches=8),
        ]],
        colWidths=[8.5 * cm, 8.5 * cm],
    )
    E.append(mm_table)
    E.append(vsp(0.3))

    E.append(Paragraph(
        '<b>Son soru:</b> Sence 2B tasarim ile 3B tasarim arasindaki en onemli fark nedir?',
        S_SMBD,
    ))
    E.append(WritingLines(num_lines=2))
    E.append(vsp(0.15))
    E.append(sep())

    E.append(PageBreak())

    # --- SAYFA 2+: Tanilama Testi ---
    E.append(make_student_info_header())
    E.append(vsp(0.2))
    E.append(Paragraph('ARAC 2: IKI ASAMALI TANILAMA TESTI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Her sorunun iki kismi var. Once dogru secenegi daire icine al, '
        'sonra neden o secenegi sectigini acikla. Bilmiyorsan "Tahminem su:" diye basla.  '
        '<b>Sure: 10-12 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    sorular = [
        ('Iki boyutlu (2B) tasarim programlarinda nesneler nasil cizilir?',
         ['A) X, Y ve Z eksenleri kullanilarak derinlikli bicimde',
          'B) Yalnizca X ve Y eksenleri kullanilarak duzlemsel bicimde',
          'C) Yalnizca renk ve doku ile',
          'D) Fotograf duzenleyerek']),
        ('Bir nesneyi tam yukaridan baktiginizda gordugunuz cizim hangisidir?',
         ['A) On gorunus', 'B) Yan gorunus', 'C) Ust gorunus (kusbakisi)', 'D) Perspektif gorunus']),
        ('Bir nesnenin uc boyutlu gosterimi icin X ve Y eksenlerine hangi eksen eklenir?',
         ['A) W ekseni', 'B) Z ekseni', 'C) T ekseni', 'D) V ekseni']),
        ('Tinkercad hangi amacla kullanilan bir programdir?',
         ['A) Fotograf duzenleme ve renklendirme',
          'B) Internet tarayicisinda muzik bestelemek',
          'C) Tarayici uzerinden uc boyutlu nesne modelleme',
          'D) Video kesme ve montaj']),
        ('Izometrik cizimde nesneler nasil gosterilir?',
         ['A) Sadece on yuzu gosterilerek',
          'B) Fotograf gibi gercekci bicimde',
          'C) Belirli acilar (genellikle 30 derece) kullanilarak kagit uzerinde derinlik hissi verecek sekilde',
          'D) Nesneler yukaridan kusbakisi olarak']),
        ('Bir tasarimci bilgisayarda bitirdigi 3B modelini nasil paylasabilir?',
         ['A) Yalnizca kagida cezerek',
          'B) Ekran goruntusu alarak veya dosya disa aktararak',
          'C) Modeli yuksek sesle anlatarak',
          'D) Tasarimlar paylasilamaz']),
        ('"Dijital prototip" ne anlama gelir?',
         ['A) Gercek malzemeden el ile uretilmis model',
          'B) Tasarimin kagit uzerindeki eskizi',
          'C) Tasarimin bilgisayar ortaminda olusturulmus deneme modeli',
          'D) Tasarimin renkli fotografu']),
        ('Coklu ortam sunusu hazirlamak icin hangisi dogru bir yaklasimdir?',
         ['A) Yalnizca yazili metin kullanmak',
          'B) Gorsel, metin ve ekran goruntusu bir arada kullanmak',
          'C) Sadece resim kullanmak',
          'D) Sadece sesli anlatim yapmak']),
    ]

    for i, (soru, secenekler) in enumerate(sorular, 1):
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


# =============================================================================
# KAGIT 2: Acik Uclu + Eslestirme + Bosluk Doldurma
# =============================================================================

def kagit_2_elemanlar():
    E = []

    E.append(PageBreak())
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu calisma not icin degildir. Bildigini duerustce yaz — yanlis cevap olmaz!',
        S_NOT,
    ))
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.2))

    # --- ARAÇ 3: Açık Uçlu ---
    E.append(Paragraph('ARAC 3: ACIK UCLU SORULAR', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagidaki sorulari kendi cumlelenle yanitla. Dogru/yanlis yok — kendi dusunceni yaz.  '
        '<b>Sure: 5-7 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    acik_sorular = [
        'Bir tasarimi bilgisayarda yapmanin, kagit uzerinde yapmaya gore avantajlari neler olabilir?',
        'Sence "iki boyutlu tasarim" ile "uc boyutlu tasarim" arasindaki en temel fark nedir? Ornekle acikla.',
        'Gunluk hayatta hangi urunlerin bilgisayar destekli tasarim programlariyla tasarlandigini dusunuyorsun?',
    ]

    for i, soru in enumerate(acik_sorular, 1):
        blok = []
        blok.append(Paragraph(f'<b>Soru {i}.</b> {soru}', S_SORU))
        blok.append(WritingLines(num_lines=3))
        blok.append(sep())
        blok.append(vsp(0.05))
        E.append(KeepTogether(blok))

    E.append(vsp(0.1))

    # --- ARAÇ 4: Eşleştirme ---
    E.append(Paragraph('ARAC 4: ESLESTIRME TESTI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Sol sutundaki kavramlari sag sutundaki tanimlarla eslestir. '
        'Cevabi noktalarin uzerine yaz.  <b>Sure: 4-5 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    tablo_stili = TableStyle([
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
        ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ])

    E.append(Paragraph('<b>Bolum A — Kavram ve Tanim</b>', S_BLM))
    bolum_a = [
        ['#', 'Kavram', 'Cevap', 'Harf', 'Tanim'],
        ['1', 'Iki Boyutlu (2B) Tasarim', '.....', 'A', 'Tasarimin bilgisayar ortaminda olusturulmus deneme modeli'],
        ['2', 'Uc Boyutlu (3B) Tasarim', '.....', 'B', 'Nesnenin X-Y-Z eksenleri kullanilarak derinlik, genislik ve yuksekligiyle olusturulan dijital formu'],
        ['3', 'Gorunus Cikarma', '.....', 'C', 'Nesnenin yalnizca X ve Y eksenleri uzerinde duzlemsel olarak cizilmesi'],
        ['4', 'Dijital Prototip', '.....', 'D', 'Nesnenin ust, on ve yan gibi farkli bakis acilarindan cizilmesi'],
        ['5', 'Izometrik Cizim', '.....', 'E', 'Belirli acilar (30 derece) kullanilarak kagit uzerinde derinlik hissi veren cizim teknigi'],
    ]
    t_a = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_a],
        colWidths=[0.6*cm, 4.0*cm, 1.2*cm, 1.0*cm, 10.2*cm],
    )
    t_a.setStyle(tablo_stili)
    E.append(t_a)
    E.append(vsp(0.2))

    E.append(Paragraph('<b>Bolum B — Program/Arac ve Aciklamasi</b>', S_BLM))
    bolum_b = [
        ['#', 'Program/Arac', 'Cevap', 'Harf', 'Aciklama'],
        ['1', 'MS Paint', '.....', 'A', '3B modeli 3B yaziciya gondermek icin kullanilan disa aktarma formati'],
        ['2', 'Tinkercad', '.....', 'B', 'Bilgisayar ekranini goruntu olarak kaydetme yontemi'],
        ['3', 'Coklu Ortam Sunusu', '.....', 'C', "Windows'ta varsayilan iki boyutlu dijital cizim programi"],
        ['4', 'Ekran Goruntusu', '.....', 'D', 'Gorsel, metin ve dijital icerigin bir arada kullanildigi sunum'],
        ['5', 'STL Dosyasi', '.....', 'E', 'Tarayici uzerinden kullanilan ucretsiz uc boyutlu modelleme programi'],
    ]
    t_b = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_b],
        colWidths=[0.6*cm, 4.0*cm, 1.2*cm, 1.0*cm, 10.2*cm],
    )
    t_b.setStyle(tablo_stili)
    E.append(t_b)
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.1))

    # --- ARAÇ 5: Boşluk Doldurma ---
    E.append(Paragraph('ARAC 5: BOSLUK DOLDURMA', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagidaki cumlelerde bos birakilan yerleri kutu icindeki kelimelerden uygun olaniyla doldur. '
        'Her kelime yalnizca bir kez kullanilir.  <b>Sure: 3-4 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.1))
    E.append(Paragraph(
        '<i>Kelime kutusu: iki boyutlu / uc boyutlu / ust gorunus / Z ekseni / izometrik / '
        'Tinkercad / dijital prototip / coklu ortam</i>',
        S_KELL,
    ))
    E.append(vsp(0.1))

    bosluklar = [
        'X ve Y eksenlerinde duzlemsel cizim yapan programlar ___________________ tasarim araclaridir.',
        'Derinlik, genislik ve yukseklik birlikte kullanildiginda tasarim ___________________ hale gelir.',
        'Bir nesneye tamamen yukaridan bakidiginda elde edilen cizim ___________________ olarak adlandirilir.',
        '2B tasarimda X ve Y eksenleri kullanilirken 3B tasarima ___________________ eklenir.',
        'Belirli acilar kullanarak kagit uzerinde derinlik hissi veren cizim tekniğine ___________________ cizim denir.',
        'Tarayici uzerinden ucretsiz olarak kullanabilecegimiz 3B modelleme programinin adi ___________________.',
        'Bilgisayar ortaminda olusturulan deneme modeline ___________________ denir.',
        'Tasarim surecini gorsel, metin ve ekran goruntusuyule birlikte sunan calismaya ___________________ sunusu denir.',
    ]

    for i, metin in enumerate(bosluklar, 1):
        blok = [Paragraph(f'<b>{i}.</b>  {metin}', S_SML), vsp(0.05)]
        E.append(KeepTogether(blok))

    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.1))

    # --- SANA GÖRE ---
    E.append(Paragraph('SANA GORE... (istersen cevapla, istersen bos birak)', S_BAS))
    E.append(vsp(0.05))
    E.append(Paragraph(
        'Daha once hic bilgisayarda bir sey cizdin ya da tasarladin mi? (Oyun, uygulama, program vb.)',
        S_LBL,
    ))
    E.append(WritingLines(num_lines=2))
    E.append(vsp(0.1))
    E.append(Paragraph('Bu unitede en cok merak ettigin konu nedir?', S_LBL))
    E.append(WritingLines(num_lines=2))

    return E


# =============================================================================
# ANA CALISTIRICI
# =============================================================================

if __name__ == '__main__':
    doc = create_doc(PDF_PATH, title='On Degerlendirme', unite_info=UI)
    elemanlar = kagit_1_elemanlar() + kagit_2_elemanlar()
    doc.build(elemanlar, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF uretildi: {PDF_PATH}')
