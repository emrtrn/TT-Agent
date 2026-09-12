"""
6. Unite -- On Degerlendirme PDF ureticisi (birlesik)
Form 1 (Arac 1: Zihin Haritasi + Arac 2: Tanilama Testi) +
Form 2 (Arac 3: Acik Uclu + Arac 4: Eslestirme + Arac 5: Bosluk Doldurma)
Cikti: units/7_sinif/unit6/U6_PDF_02_On_Degerlendirme.pdf
Calistir: python pdf_uretim/uret_unite6_on_degerlendirme.py
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

ROOT     = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit6')
PDF_PATH = os.path.join(ROOT, 'U6_PDF_02_On_Degerlendirme.pdf')
UI = '6. Unite: Dogadan Tasarima  -  Teknoloji ve Tasarim  -  7. Sinif'

S_BAS  = ParagraphStyle('u6od_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u6od_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u6od_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u6od_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u6od_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u6od_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u6od_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u6od_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u6od_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)
S_KELL = ParagraphStyle('u6od_KELL', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=5, borderWidth=0.5,
                         borderColor=COLOR_LIGHT_GREY, leftIndent=4, rightIndent=4,
                         spaceBefore=3, spaceAfter=3)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


SORULAR = [
    (
        'Biyomimikri kavraminin en dogru tanimi hangisidir?',
        ['A) Hayvanlari taklit eden robot yapimi teknolojisi',
         'B) Dogadaki canlilarin ozelliklerini tasarima uyarlama yaklasimi',
         'C) Dogal malzemeleri kullanarak urun yapma yontemi',
         'D) Biyoloji ile mimariyi birlestiren bir sanat akimi'],
    ),
    (
        'Geko kertenkeleleri duvara kolayca yapişabilir cunku ayaklarinda milyonlarca ince nano tuy bulunur. '
        'Bu ozelligi taklit eden urun hangisidir?',
        ['A) Su gecirmez cizme',
         'B) Yuzucu gozlugu',
         'C) Yapiskanlı nano yuzey bandi',
         'D) Isi yalitim malzemesi'],
    ),
    (
        'Lotus ciceginin yapraklarindaki ozellik sayesinde su yüzeyde tutunmaz, damlalar yuvarlanip gider. '
        'Bu "lotus etkisi" hangi tasarima ilham kaynagi olmustur?',
        ['A) Gunes enerjisi toplayan panel yapimi',
         'B) Su gecirmez ve kendiliğinden temizlenen kumas uretimi',
         'C) Hafif ama dayanikli cati kirisi tasarimi',
         'D) Hizli yuzucu kiyafeti yapimi'],
    ),
    (
        'Biyomorfizm nedir?',
        ['A) Canlilarin islevsel ozelliklerini birebir taklit etme',
         'B) Dogal formlari estetik amacla tasarima yansitma',
         'C) Biyolojik malzemeleri dogrudan urunlerde kullanma',
         'D) Ekosistemi koruma odakli tasarim yapma'],
    ),
    (
        'Kopek baliğinin deri yapisindaki kucuk disimsi cikıntilar suyu verimli bicimde keser. '
        'Bu ozellik hangi alanda kullanilmak uzere arastirilmistir?',
        ['A) Hava araci govde tasarimi',
         'B) Tibbi implant kaplamalar',
         'C) Yuzucu kiyafeti tasarimi',
         'D) Gunes paneli yuzeyi'],
    ),
    (
        'Biyofili kavramini en iyi aciklayan ifade hangisidir?',
        ['A) Biyoçesitliligi koruma çabasi',
         'B) Insanin dogayla olan icgüdüsel bagi ve dogaya yönelik egilimi',
         'C) Bitkileri dekoratif tasarim ogesi olarak kullanma',
         'D) Dogal malzemeleri geri donusturme anlayisi'],
    ),
    (
        "Afrika'daki termit tepeleri icinde kendi sicakliklarini kontrol eden dogal bir havalandirma sistemi calisir. "
        'Bu sistem hangi yapiya ilham vermistir?',
        ['A) Gunes paneli ciftligi',
         'B) Yesil cati (teras bahce)',
         'C) Eastgate Centre ofis binasi',
         'D) Kopru kirisi tasarimi'],
    ),
    (
        'Bir tasarimci biyomimetik yaklasimi kullanirken en temel olarak hangi soruya odaklanir?',
        ['A) Bu urunun maliyeti nedir?',
         'B) Bu problemi doga nasil çözmüs?',
         'C) Bu formu kim daha once cizmis?',
         'D) Bu urunu kimler satin alir?'],
    ),
]


# =============================================================================
# FORM 1: Zihin Haritasi + Tanilama Testi
# =============================================================================

def form1_elemanlar():
    E = []

    # --- SAYFA 1: Zihin Haritasi ---
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu calisma not icin degildir. Dogru ya da yanlis cevap yoktur. '
        'Aklina geleni ictenlikle yaz!',
        S_NOT))
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.2))
    E.append(Paragraph('ARAC 1: ZIHIN HARITASI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>DOGA</b> ve <b>TASARIM</b>. '
        'Bu kelimeleri duyduğunda aklina gelen her seyi oklar ve kelimelerle bagla. '
        'Canli adlari, urunler, kavramlar, her sey olabilir!  <b>Sure: 5-7 dakika</b>',
        S_YON))
    E.append(vsp(0.15))
    E.append(MindMapCanvas('DOGA  TASARIM', width=17 * cm, height=9.5 * cm, num_branches=8))
    E.append(vsp(0.2))
    E.append(Paragraph(
        '<b>Son soru:</b> Sence DOGA ve TASARIM birbiriyle nasil iliskili? Kisaca acikla:',
        S_SMBD))
    E.append(WritingLines(num_lines=2))
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Ogretmenin bu kagidi toplayacak ve unite sonunda sana geri verecek.',
        S_NOT))
    E.append(sep())
    E.append(PageBreak())

    # --- SAYFA 2+: Tanilama Testi ---
    E.append(make_student_info_header())
    E.append(vsp(0.2))
    E.append(Paragraph('ARAC 2: IKI ASAMALI TANILAMA TESTI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Her sorunun iki kismi var. Once dogru secenegi isaretleyin (A/B/C/D), '
        'sonra neden o secenegi sectiginizi aciklayin. Bilmiyorsan "Emin degilim ama..." diye basla.  '
        '<b>Sure: 10-12 dakika</b>',
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


# =============================================================================
# FORM 2: Acik Uclu + Eslestirme + Bosluk Doldurma
# =============================================================================

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
    ('ALIGN', (3, 0), (3, -1), 'CENTER'),
])


def form2_elemanlar():
    E = []

    E.append(PageBreak())
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu calisma not icin degildir. Ne bildigini ogrenmek istiyoruz. '
        'Bos birakmak yerine tahminin yaz!',
        S_NOT))
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.2))

    # ARAC 3: Acik Uclu
    E.append(Paragraph('ARAC 3: ACIK UCLU SORULAR', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagidaki sorulari kendi cumlelenle yanitla. '
        'Dogru/yanlis yok — kendi dusunceni yaz.  <b>Sure: 5-7 dakika</b>',
        S_YON))
    E.append(vsp(0.15))

    acik_sorular = [
        'Dogadan esinlenerek yapildigini dusundugun bir urun var mi? Varsa, dogadaki hangi ozellikten ilham alindigini acikla.',
        'Bir hayvani ya da bitkinin hangi ozelligi seni en cok sasirtiyor? Bu ozellik bir tasarima nasil uygulanabilir?',
        'Teknoloji ve Tasarim dersinin "Dogadan Tasarima" unitesinde ne ogrenecegini tahmin ediyorsun?',
    ]
    for i, soru in enumerate(acik_sorular, 1):
        blok = []
        blok.append(Paragraph(f'<b>Soru {i}.</b> {soru}', S_SORU))
        blok.append(WritingLines(num_lines=3))
        blok.append(sep())
        blok.append(vsp(0.05))
        E.append(KeepTogether(blok))

    E.append(vsp(0.1))

    # ARAC 4: Eslestirme
    E.append(Paragraph('ARAC 4: ESLESTIRME TESTI', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Sol sutundaki kavramlari sag sutundaki tanimlarla eslestir. '
        'Her tanim yalnizca bir kez kullanilir.  <b>Sure: 4-5 dakika</b>',
        S_YON))
    E.append(vsp(0.15))

    E.append(Paragraph('<b>Bolum A — Kavram ve Tanim</b>', S_BLM))
    bolum_a = [
        ['#', 'Kavram', 'Cevap', 'Harf', 'Tanim'],
        ['1', 'Biyomimikri',  '.....', 'A', "Insanin dogayla olan icgudüsel bagi; insanlarin dogaya yakin olmaktan duydugu tatmin"],
        ['2', 'Biyofili',     '.....', 'B', "Dogal bir yapi ya da davranisi birebir taklit etme; ornegin bir kusun kanadini model alarak ucak tasarimi"],
        ['3', 'Biyomorfizm',  '.....', 'C', "Dogadaki canlilarin ozelliklerini inceleyerek yeni urunler, surecler veya cozumler gelistirme yaklasimi"],
        ['4', 'Biyotaklit',   '.....', 'D', "Bir tasarim fikrinin ilk deneme modeli; tam urun degil, test edilebilir ornek"],
        ['5', 'Prototip',     '.....', 'E', "Dogal form ve dokuları estetik amacla tasarima yansitma; balik pulu deseni gibi"],
    ]
    t_a = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_a],
        colWidths=[0.6*cm, 3.0*cm, 1.2*cm, 1.0*cm, 11.2*cm],
    )
    t_a.setStyle(TABLO_STILI)
    E.append(t_a)
    E.append(vsp(0.2))

    E.append(Paragraph('<b>Bolum B — Dogal Ozellik ve Tasarim Urunu</b>', S_BLM))
    bolum_b = [
        ['#', 'Dogal Ozellik', 'Cevap', 'Harf', 'Tasarim Urunu'],
        ['1', 'Geko kertenkelessinin ayagindaki nano tuyler',              '.....', 'A', 'Su gecirmez ve kendi kendini temizleyen kumas'],
        ['2', 'Lotus ciceginin su itici, kendiliğinden temizlenen yapragi','.....', 'B', 'Dogal iklim kullanan Eastgate Centre ofis binasi'],
        ['3', 'Bal arisinin altigen petek hucresi',                        '.....', 'C', 'Yapiskanlı nano yuzey bandi'],
        ['4', 'Termit tepesindeki dogal havalandirma kanallari',           '.....', 'D', 'Hafif ama dayanikli altigen panel ve ambalaj tasarimi'],
    ]
    t_b = Table(
        [[Paragraph(c, S_SML) for c in row] for row in bolum_b],
        colWidths=[0.6*cm, 5.0*cm, 1.2*cm, 1.0*cm, 9.2*cm],
    )
    t_b.setStyle(TABLO_STILI)
    E.append(t_b)
    E.append(vsp(0.15))
    E.append(sep())
    E.append(vsp(0.1))

    # ARAC 5: Bosluk Doldurma
    E.append(Paragraph('ARAC 5: BOSLUK DOLDURMA', S_BAS))
    E.append(Paragraph(
        '<b>Yonerge:</b> Asagidaki cumlelerde bos birakilan yerleri kutu icindeki sozcuklerden uygun olaniyla doldur. '
        'Her sozcuk yalnizca bir kez kullanilir.  <b>Sure: 3-4 dakika</b>',
        S_YON))
    E.append(vsp(0.1))
    E.append(Paragraph(
        '<i>Sozcuk kutusu: biyomimikri / lotus / geko / biyomorfizm / termit / disiplinler arasi</i>',
        S_KELL))
    E.append(vsp(0.1))

    bosluklar = [
        "Dogadaki canlilarin ozelliklerini taklit ederek yeni urunler ya da cozumler gelistirme yaklasimina <b>________________________</b> denir.",
        "Yapraklarindaki yapi sayesinde suyu kendiliğinden iten cicek <b>________________________</b>'tur; bu ozellik su gecirmez kumas tasarimina ilham vermistir.",
        "Milyonlarca nano tuy sayesinde duvara yapişabilen kertenkele turu <b>________________________</b>'dur; bu ozelligi taklit eden yapishkanlı yuzeyler gelistirilmistir.",
        "Dogal formlari estetik amacla tasarima yansitma yaklasimina <b>________________________</b> denir; mobilya veya mucevherde yaprak damari motifi buna bir ornektir.",
        "Tepeleri mukemmel dogal havalandirma sistemiyle donatilmis bu bocegin adi <b>________________________</b>'tir; yuvalari Afrika'daki bir ofis binasina ilham vermistir.",
        "Biyomimikri projeleri genellikle biyoloji, muhendislik, matematik ve sanati bir arada kullanan <b>________________________</b> bir yaklasim gerektirir.",
    ]
    for i, metin in enumerate(bosluklar, 1):
        blok = [Paragraph(f'<b>{i}.</b>  {metin}', S_LBL), vsp(0.05)]
        E.append(KeepTogether(blok))

    return E


# =============================================================================
# ANA CALISTIRICI
# =============================================================================

if __name__ == '__main__':
    doc = create_doc(PDF_PATH, title='On Degerlendirme', unite_info=UI)
    elemanlar = form1_elemanlar() + form2_elemanlar()
    doc.build(elemanlar, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF uretildi: {PDF_PATH}')
