# -*- coding: utf-8 -*-
"""
4. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit4/U4_PDF_Ogretmen_Hazirlik.pdf
Calistir: python pdf_uretim/uret_unite4_ogretmen_hazirlik.py
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
    PageBreak, KeepTogether, HRFlowable,
)
from pdf_style import (
    register_fonts, add_page_number, make_cover,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY,
    HorizontalLine,
)

register_fonts()

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, 'units', 'unit4')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U4_PDF_Ogretmen_Hazirlik.pdf')
UI    = '4. Unite - Bilgisayar Destekli Tasarim'
CW    = A4[0] - 4 * cm

# ============================================================
# STİLLER
# ============================================================

S_H1  = ParagraphStyle('h1',  fontName='TR-Bold',    fontSize=13, textColor=COLOR_PRIMARY,
                         leading=17, spaceBefore=16, spaceAfter=6)
S_H2  = ParagraphStyle('h2',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_SECONDARY,
                         leading=14, spaceBefore=10, spaceAfter=4)
S_H3  = ParagraphStyle('h3',  fontName='TR-Bold',    fontSize=10, textColor=COLOR_ACCENT,
                         leading=13, spaceBefore=7, spaceAfter=3)
S_BD  = ParagraphStyle('bd',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, spaceAfter=4, alignment=TA_JUSTIFY)
S_IND = ParagraphStyle('ind', fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, spaceAfter=3, alignment=TA_JUSTIFY, leftIndent=12)
S_BUL = ParagraphStyle('bul', fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=12, spaceAfter=2, leftIndent=16, bulletIndent=4)
S_NOT = ParagraphStyle('not', fontName='TR-Italic',  fontSize=8.5, textColor=COLOR_MUTED,
                         leading=12, spaceAfter=4, leftIndent=8)
# bilgi kutusu
S_BH  = ParagraphStyle('bh',  fontName='TR-Bold',    fontSize=9,  textColor=white, leading=12)
S_BB  = ParagraphStyle('bb',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, alignment=TA_JUSTIFY)
# hikaye kutusu
S_SH  = ParagraphStyle('sh',  fontName='TR-Bold',    fontSize=9,  textColor=white, leading=12)
S_SB  = ParagraphStyle('sb',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, alignment=TA_JUSTIFY)
S_SC  = ParagraphStyle('sc',  fontName='TR-Italic',  fontSize=8.5, textColor=COLOR_SECONDARY,
                         leading=12)
# soru-cevap
S_QQ  = ParagraphStyle('qq',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY,
                         leading=13, spaceBefore=6, spaceAfter=2)
S_QA  = ParagraphStyle('qa',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, spaceAfter=5, alignment=TA_JUSTIFY, leftIndent=10)
# yanlis anlama
S_YAN = ParagraphStyle('yan', fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                         leading=12, spaceAfter=1)
S_DUZ = ParagraphStyle('duz', fontName='TR-Regular', fontSize=8.5, textColor=COLOR_TEXT,
                         leading=12, spaceAfter=5, leftIndent=6)
# tablo içi
S_TH  = ParagraphStyle('th',  fontName='TR-Bold',    fontSize=8.5, textColor=white,
                         leading=12, alignment=TA_CENTER)
S_TC  = ParagraphStyle('tc',  fontName='TR-Regular', fontSize=8.5, textColor=COLOR_TEXT,
                         leading=12, alignment=TA_LEFT)
S_TCB = ParagraphStyle('tcb', fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_TEXT,
                         leading=12, alignment=TA_LEFT)


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def vsp(h=0.2):
    return Spacer(1, h * cm)

def hr(c=None, t=0.4):
    return HRFlowable(width='100%', thickness=t, color=c or COLOR_LIGHT_GREY,
                       spaceBefore=3, spaceAfter=3)

def bolum_baslik(no, baslik):
    return [
        HRFlowable(width='100%', thickness=1.5, color=COLOR_PRIMARY,
                    spaceBefore=8, spaceAfter=4),
        Paragraph(f'BÖLÜM {no} — {baslik}', S_H1),
    ]

def bilgi_kutusu(baslik, satirlar):
    rows = [[Paragraph(baslik, S_BH)]]
    for s in satirlar:
        rows.append([Paragraph(s, S_BB)])
    t = Table(rows, colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (0, 0),  COLOR_PRIMARY),
        ('BACKGROUND',    (0, 1), (0, -1), COLOR_VERY_LIGHT),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('LINEBELOW',     (0, 0), (0, 0),  1.5, COLOR_SECONDARY),
        ('BOX',           (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    return KeepTogether([t, vsp(0.2)])

def hikaye(baslik, satirlar, baglanti=None):
    rows = [[Paragraph(baslik, S_SH)]]
    for s in satirlar:
        rows.append([Paragraph(s, S_SB)])
    if baglanti:
        rows.append([Paragraph(baglanti, S_SC)])
    t = Table(rows, colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (0, 0),  COLOR_SECONDARY),
        ('BACKGROUND',    (0, 1), (0, -1), COLOR_VERY_LIGHT_GREY),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('LINEBELOW',     (0, 0), (0, 0),  1, COLOR_ACCENT),
        ('BOX',           (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    return KeepTogether([t, vsp(0.2)])


# ============================================================
# BÖLÜM 1 — KAVRAMLARIN ANATOMİSİ
# ============================================================

def bolum1():
    e = []
    e += bolum_baslik(1, 'KAVRAMLARIN ANATOMİSİ')

    e.append(Paragraph('1.1 İki Boyutlu ve Üç Boyutlu Tasarım: Neden Fark Önemlidir?', S_H2))
    e.append(Paragraph(
        '<b>2B (İki Boyutlu) Tasarım:</b> Bir nesnenin yalnızca iki eksen — genişlik (X) ve '
        'yükseklik (Y) — üzerinde gösterilmesidir. Düzlemseldir; derinlik bilgisi yoktur. '
        'Bir kâğıt üzerindeki çizim, bir logo, bir kat planı: hepsi 2B\'dir.', S_BD))
    e.append(Paragraph(
        'Öğrenciler çoğu zaman "2B = basit, 3B = zor" gibi bir hiyerarşi kurar. Oysa gerçek '
        'farklı: 2B ile 3B farklı sorulara yanıt verir. "Bu nesne önden nasıl görünür?" → 2B. '
        '"Bu nesne uzayda nasıl yer kaplar?" → 3B. İkisi birbirini tamamlar, biri diğerinden '
        'üstün değildir.', S_BD))
    e.append(Paragraph(
        'Meslek dünyasına bağlantı: Bir mimar hem 2B kat planı çizer hem de 3B maket veya '
        'render üretir. Bir endüstriyel tasarımcı hem teknik çizim hem de CAD modeli hazırlar. '
        'Bu ünite öğrencileri her iki dil için temel donanımla donatmaktadır.', S_BD))

    e.append(Paragraph('Üçüncü Eksen — Z\'nin Anlamı', S_H3))
    e.append(Paragraph(
        'X ekseni yatay (genişlik), Y ekseni dikey (yükseklik), Z ekseni derinlik '
        '(ileri-geri) anlamına gelir. Bu üç ekseni birlikte düşünmek 3B uzayı oluşturur.',
        S_BD))
    e.append(bilgi_kutusu(
        'Z Ekseni: Bilinen Bir Kargasa',
        ['Birçok öğrenci Z eksenini ilk duyduğunda "yukarı mı, aşağı mı gidiyor?" diye sorar.',
         'Yanıt bağlama bağlıdır: Tinkercad\'de Z ekseni yüksekliği temsil eder. Bazı '
         '3B yazılımlarda (oyun motorlarında) Y yükseklik, Z derinlik olabilir.',
         'Bu tutarsızlık endüstride bilinen bir karışıklık kaynağıdır. Öğrencilere söylemeye '
         'değer: "Hangi eksenin ne anlama geldiği, kullandığınız araca göre değişebilir. '
         'Önemli olan üç boyutun kavramını anlamaktır."']))

    e.append(Paragraph('1.2 Görünüş Çıkarma: Mimarlık ve Mühendisliğin Ortak Dili', S_H2))
    e.append(Paragraph(
        'Görünüş çıkarma, bir nesnenin farklı yönlerden görünümünü ayrı ayrı çizme '
        'işlemidir. Teknik çizimde standart görünüşler: üst (kuşbakışı/plan), ön (cephe), '
        'yan (profil).', S_BD))
    e.append(Paragraph(
        '<b>Neden bu kadar önemli?</b> Bir nesnenin fotoğrafı o nesnenin tam geometrisini '
        'iletmez. Açı, ışık ve perspektif gerçek ölçüleri gizler. Görünüş çizimleri ise net, '
        'ölçülebilir, yoruma kapalı bilgi verir. Bu yüzden mühendislik çizimleri ve teknik '
        'resim, sanayi devrimiyle birlikte standartlaştırıldı.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Türk Standartları Enstitüsü (TSE), teknik çizim '
        'standartlarını belirler. Bir fabrikada üretilecek parçanın çiziminin Türkiye\'nin '
        'her yerinde aynı şekilde okunması gerekir. Görünüş çıkarma bunun temelini oluşturur.',
        S_NOT))
    e.append(Paragraph(
        '<b>Sınıfta dikkat:</b> Öğrenciler üst görünüşte "nesneyi çok yukarıdan bakarak '
        'çiziyorum" yerine "nesnenin üstü böyle görünür" diye düşünebilir. Aradaki fark '
        'küçük ama kritiktir: Görünüş çıkarma perspektif çizimi değildir; nesnenin o yüzeyi '
        'dik olarak kâğıda düzlenir.', S_NOT))

    e.append(Paragraph('1.3 İzometrik Çizim: Kâğıtta Derinlik Yaratmanın Zekice Yolu', S_H2))
    e.append(Paragraph(
        'İzometrik kelimesi Yunancadan gelir: <i>isos</i> (eşit) + <i>metron</i> (ölçüm). '
        'İzometrik çizimde üç eksen birbirinden eşit açıyla (120°) ayrılır; kâğıtta bunu '
        'uygulamak için 30° açılar kullanılır.', S_BD))

    karsi_data = [
        [Paragraph('Özellik', S_TH), Paragraph('Perspektif Çizim', S_TH),
         Paragraph('İzometrik Çizim', S_TH)],
        [Paragraph('Uzaktaki nesneler', S_TC), Paragraph('Küçülür', S_TC),
         Paragraph('Aynı ölçekte kalır', S_TC)],
        [Paragraph('Ölçü bilgisi', S_TC), Paragraph('Bozulur', S_TC),
         Paragraph('Korunur', S_TC)],
        [Paragraph('Kullanım amacı', S_TC), Paragraph('Gerçekçi görünüm', S_TC),
         Paragraph('Teknik çizim, ölçüm', S_TC)],
        [Paragraph('Oyun/yazılım örneği', S_TC), Paragraph('3B oyunlar (FPS)', S_TC),
         Paragraph('Minecraft, SimCity', S_TC)],
    ]
    karsi_t = Table(karsi_data, colWidths=[CW*0.32, CW*0.34, CW*0.34])
    karsi_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, COLOR_VERY_LIGHT]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    e.append(KeepTogether([karsi_t, vsp(0.15)]))
    e.append(Paragraph(
        'Türkiye bağlantısı: İzometrik çizim genellikle Teknoloji ve Tasarım\'a özgüdür. '
        'Öğrencilerin büyük çoğunluğu izometrik çizimi ilk kez bu ünitede görecektir.',
        S_NOT))

    e.append(Paragraph('1.4 Dijital Prototip: "Yapmadan Önce Dene"nin Dijital Hali', S_H2))
    e.append(Paragraph(
        'Prototip kavramı 3. Ünitede işlendi. Dijital prototip, fiziksel malzeme kullanmadan '
        'bilgisayar ortamında oluşturulan deneme modelidir.', S_BD))
    e.append(bilgi_kutusu(
        'Dijital Prototip Neden Değerlidir?',
        ['Malzeme sıfır. Değiştirme anlık. Geri alma mümkün.',
         'Tinkercad\'de bir küpü kopyalayıp 20 farklı varyasyon denemek — gerçek dünyada '
         'bu işlem hem zaman hem maliyet gerektirir.',
         'Ölçek sorunu: Öğrenciler "büyük görünüyor" diye ölçüyü büyüttükten sonra '
         '"ama gerçekte ne kadar büyük?" sorusunu sormayabilirler. Milimetre-santimetre '
         'dönüşümünü pekiştirmek bu noktada değerlidir.']))

    e.append(Paragraph('1.5 Çoklu Ortam Sunusu: Tasarımı Anlatmanın Dili', S_H2))
    e.append(Paragraph(
        'Çoklu ortam (multimedia), birden fazla medya türünü — yazı, görsel, ses, video, '
        'animasyon — bir arada kullanan içeriktir. Bu ünitede öğrenciler yalnızca dijital '
        'bir model değil, o modeli belgeleyen ve tanıtan bir sunum da hazırlar.', S_BD))
    e.append(Paragraph(
        'Mesleki gerçeklik: Bir tasarımcı yalnızca ürün geliştirmez, onu müşteriye, '
        'yatırımcıya veya ekibine anlatmak zorundadır. "Tasarımını sunabilmek" ayrı bir '
        'beceridir. Apple\'ın ürün lansmanları, girişimcilerin "pitch" sunuları, mimarların '
        '"tasarım toplantıları" — bunların hepsinde çoklu ortam kullanılır.', S_BD))
    return e


# ============================================================
# BÖLÜM 2 — CAD'IN DOĞUŞU VE GELİŞİMİ
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'BİLGİSAYAR DESTEKLİ TASARIMIN DOĞUŞU VE GELİŞİMİ')

    e.append(Paragraph('2.1 Kâğıt ve Kalemden Ekrana: CAD\'ın Tarihi', S_H2))
    e.append(Paragraph(
        'CAD (Computer-Aided Design / Bilgisayar Destekli Tasarım), 20. yüzyılın ikinci '
        'yarısında doğdu.', S_BD))

    e.append(Paragraph('1963 — Sketchpad ve Her Şeyin Başlangıcı', S_H3))
    e.append(Paragraph(
        'Ivan Sutherland, MIT\'de doktora tezi olarak Sketchpad adlı sistemi geliştirdi. '
        'Bu program, kullanıcının ışık kalemi ile bilgisayar ekranında çizim yapmasına '
        'olanak sağlıyordu. Bugün "grafik kullanıcı arayüzü" dediğimiz kavramın öncülüdür.',
        S_BD))
    e.append(Paragraph(
        'Sutherland\'ın tezi 1988\'de Turing Ödülü\'ne layık görüldü — bilgisayar biliminin '
        'Nobel\'i. Doktora jürisindeki bir profesör programı gördüğünde "Bu tez olabilir mi? '
        'Bu bir bilim kurgu filmi!" demişti.', S_BD))

    e.append(Paragraph('1970\'ler — Otomobil ve Havacılık Endüstrisinin Yatırımı', S_H3))
    e.append(Paragraph(
        'Ford, Boeing ve Lockheed gibi şirketler CAD sistemlerine büyük yatırım yaptı. '
        'Sebep açıktı: Bir uçağın binlerce parçasını kâğıt üzerinde tasarlamak hem yavaş '
        'hem hataya açıktı. CAD bu süreci hem hızlandırdı hem de mühendisler arasındaki '
        'paylaşımı kolaylaştırdı.', S_BD))

    e.append(Paragraph('1982 — AutoCAD ve Kişisel Bilgisayar Devrimi', S_H3))
    e.append(Paragraph(
        'Autodesk şirketi AutoCAD\'i piyasaya sürdü. İlk kez CAD yazılımı kişisel '
        'bilgisayarlarda çalışabilir hale geldi. Artık sadece büyük şirketler değil, '
        'küçük ofisler de CAD kullanabiliyordu.', S_BD))
    e.append(Paragraph(
        'AutoCAD bugün hâlâ dünyanın en yaygın kullanılan mühendislik çizim yazılımlarından '
        'biridir. Türkiye\'de inşaat, makine ve tesisat projelerinde standart araçtır.',
        S_NOT))

    e.append(Paragraph('2.2 MS Paint: Basit Ama Dönüştürücü', S_H2))
    e.append(Paragraph(
        'MS Paint, Windows\'un 1985\'teki ilk sürümüyle birlikte geldi. Başlangıcı '
        'mütevazıydı: piksel piksel boyama yapan, kaydedilen görüntüyü baskıya '
        'gönderebilen bir yazılım.', S_BD))
    e.append(bilgi_kutusu(
        'Neden Hâlâ Paint?',
        ['Paint\'in gücü sadeliğindedir. Temel şekiller, renkler, metin — her şey '
         'birkaç tıklamayla ulaşılabilir.',
         '7. sınıf öğrencisinin "2B görünüş çizmek" gibi odaklı bir görev için '
         'Photoshop veya Illustrator öğrenmesi gerekmez. Araç, görevin önüne geçmemelidir.',
         '2017\'de Microsoft\'un Paint\'i kaldıracağı açıklanınca sosyal medyada büyük '
         'kamuoyu tepkisi oluştu. Microsoft geri adım attı — Paint, Windows 11\'de hâlâ '
         'kullanılabilir. Bu da bir ürün tasarımı dersi: kullanıcıların sevdiği şeyi '
         'karmaşıklaştırmak her zaman iyi bir fikir değildir.']))

    e.append(Paragraph('2.3 Tinkercad: Okulun Kucağında Doğan 3B Tasarım Aracı', S_H2))
    e.append(Paragraph(
        'Tinkercad, 2011\'de Kai Backman ve Mikko Mononen tarafından kuruldu. Hedefleri '
        'açıktı: 3B modellemeyi herkese erişilebilir kılmak. Autodesk 2013\'te Tinkercad\'i '
        'satın aldı ve ücretsiz bir eğitim aracı olarak geliştirmeye devam etti.', S_BD))
    e.append(Paragraph(
        '<b>Teknik temel — Constructive Solid Geometry (CSG):</b> Tinkercad\'ın çalışma '
        'mantığı "katı geometri inşaatı"na dayanır. Temel şekiller (küp, silindir, '
        'küre...) birleştirilir veya birbirinden çıkarılır. Bu, gerçek dünya mühendislik '
        'yazılımlarının (SolidWorks, Fusion 360) temel mantığıyla aynıdır.', S_BD))
    e.append(Paragraph(
        '<b>Delik (Hole) özelliği bu yüzden kritiktir:</b> Öğrenciler bir şeklin içinden '
        'başka bir şekli çıkarırken aslında temel Boole işlemi (Boolean operation) '
        'yapıyorlar. Bu kavram ileride daha ileri yazılımlarda karşılarına çıkacak.', S_BD))
    e.append(Paragraph(
        'Türkiye\'de: FabLab\'lar ve okullardaki 3B yazıcılar yaygınlaştıkça Tinkercad '
        'modellerini doğrudan baskıya göndermek mümkün hale geliyor. Bugün dünyada '
        '50 milyonun üzerinde kayıtlı kullanıcı var; bunların büyük çoğunluğu '
        'okul öğrencileri.', S_NOT))
    return e


# ============================================================
# BÖLÜM 3 — CAD'IN GERÇEK DÜNYASI
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'CAD\'IN GERÇEK DÜNYASI')

    e.append(Paragraph('3.1 Hangi Sektör, Hangi Araç?', S_H2))
    e.append(Paragraph(
        'Tinkercad bu tablonun en alt basamağındadır. Ama her mühendis, mimar veya '
        'tasarımcının ilk adımı da bir "fikri hızlıca görselleştirmek"tir — Tinkercad '
        'tam bunu yapar.', S_BD))

    sektor_data = [
        [Paragraph('Sektör', S_TH), Paragraph('Yaygın CAD Aracı', S_TH),
         Paragraph('Ne Üretiyor?', S_TH)],
        [Paragraph('İnşaat / Mimarlık', S_TC), Paragraph('AutoCAD, Revit', S_TC),
         Paragraph('Kat planları, cephe çizimleri, BIM modelleri', S_TC)],
        [Paragraph('Makine Mühendisliği', S_TC), Paragraph('SolidWorks, CATIA', S_TC),
         Paragraph('Parça ve montaj çizimleri, simülasyon', S_TC)],
        [Paragraph('Ürün Tasarımı', S_TC), Paragraph('Fusion 360, Rhino', S_TC),
         Paragraph('Tüketici ürünleri, mobilya, elektronik kutu', S_TC)],
        [Paragraph('Havacılık', S_TC), Paragraph('CATIA, NX', S_TC),
         Paragraph('Uçak gövdesi, kanat geometrisi', S_TC)],
        [Paragraph('Oyun / Film', S_TC), Paragraph('Maya, Blender', S_TC),
         Paragraph('Karakter modelleri, sahne varlıkları', S_TC)],
        [Paragraph('Eğitim / Prototipleme', S_TCB), Paragraph('Tinkercad', S_TCB),
         Paragraph('İlk model, fikir doğrulama', S_TCB)],
    ]
    sektor_t = Table(sektor_data, colWidths=[CW*0.30, CW*0.30, CW*0.40])
    sektor_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, COLOR_VERY_LIGHT]),
        ('BACKGROUND',    (0, -1), (-1, -1), COLOR_LIGHT),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    e.append(KeepTogether([sektor_t, vsp(0.2)]))

    e.append(Paragraph('3.2 3B Yazıcı ile Tinkercad Arasındaki Köprü', S_H2))
    e.append(Paragraph(
        'Tinkercad\'deki model, "Export → STL" komutuyla 3B yazıcıya gönderilebilecek bir '
        'dosyaya dönüştürülür. STL (Stereolithography), 3B modellerin yüzeyini üçgenlerle '
        'tanımlayan evrensel bir format standardıdır.', S_BD))
    e.append(Paragraph(
        'Bu bağlantı öğrenciler için motive edicidir: "Bugün çizdiğin modeli gerçek '
        'malzemeden üretmek mümkün." Okuldaki veya FabLab\'daki 3B yazıcı bu köprüyü '
        'görünür kılar.', S_BD))
    e.append(Paragraph(
        'Türkiye bağlantısı: Milli Eğitim Bakanlığı\'nın Maker Space ve EBA girişimleri '
        'kapsamında bazı okullara 3B yazıcı sağlandı. Bu araçları kullanan öğrencilerin '
        'ilk adımı çoğunlukla Tinkercad modelidir.', S_NOT))

    e.append(Paragraph('3.3 Ölçek ve Gerçeklik: Mühendisliğin En Kritik Alışkanlığı', S_H2))
    e.append(Paragraph(
        'Tinkercad\'de bir küp oluşturduğunuzda varsayılan boyut 20×20×20 mm\'dir. '
        'Öğrenciler çoğu zaman ekranda "büyük görünsün" diye ölçüyü rastgele büyütür — '
        'asıl nesnenin gerçek dünyada ne kadar büyük olduğunu düşünmeden.', S_BD))
    e.append(bilgi_kutusu(
        'Sinifta Güçlü Bir Soru',
        ['"Tasarladığın kupanın ağzının çapı kaç milimetre? Gerçekten ağzını sokabilir misin?"',
         'Bu soru öğrencileri ölçeklendirme alışkanlığına yönlendirir.',
         'Mesleki önemi: Makine mühendisliğinde "tolerans" kavramı, iki parçanın birbirine '
         'tam oturması için gerekli ölçü hassasiyetini ifade eder. 0,1 mm\'lik bir hata '
         'bir motoru kullanılamaz hale getirebilir. Tinkercad\'de ölçü alışkanlığı bu '
         'anlayışın tohumunu atar.']))
    return e


# ============================================================
# BÖLÜM 4 — DİSİPLİNLERARASI BAĞLANTILAR
# ============================================================

def bolum4():
    e = []
    e += bolum_baslik(4, 'DİSİPLİNLERARASI BAĞLANTILAR')

    e.append(Paragraph('4.1 Matematik: Geometri Hayata İndi', S_H2))
    matematik = [
        '2B görünüş çizimi → kesişim noktası, paralel kenarlar, simetri ekseni.',
        '3B modelleme → hacim, yüzey alanı, koordinat sistemi.',
        'İzometrik çizim → 30° açı, trigonometri (temel düzey).',
        'Ölçek → oran-orantı, birim dönüşümü.',
    ]
    for m in matematik:
        e.append(Paragraph(f'• {m}', S_BUL))
    e.append(Paragraph(
        'Koordinat sistemi bağlantısı derste doğal geçişler yaratır: "Matematikte x ve y '
        'eksenlerini öğrendiniz. 3B tasarımda buna z ekliyoruz." Bu bağlantı soyut '
        'gördükleri matematik kavramını somutlaştırır.', S_BD))

    e.append(Paragraph('4.2 Bilişim Teknolojileri: Araç Gerçek Olmaya Başlıyor', S_H2))
    e.append(Paragraph(
        'Paint ve Tinkercad bu ünite öncesinde öğrencilerin büyük çoğunluğuna yabancıdır. '
        'Dosya kaydetme, dışa aktarma, ekran görüntüsü alma — bunlar Bilişim dersinde '
        'öğrendikleri becerilerdir.', S_BD))
    e.append(Paragraph(
        '<b>Sınıfta yavaş ilerleme bekleyin:</b> 20 öğrencinin yarısı ilk Tinkercad '
        'oturumunda "hesap açamadım" veya "tarayıcı çöküyor" gibi teknik sorunlarla '
        'karşılaşabilir. Atölyeden bir ders önce hesap açılmasını istemek bu süreci '
        'önemli ölçüde hızlandırır.', S_NOT))

    e.append(Paragraph('4.3 Görsel Sanatlar: Teknik Çizim Bir Sanat Değil midir?', S_H2))
    e.append(Paragraph(
        'Teknik çizim ile serbest sanatsal çizim farklı amaçlara hizmet eder. Teknik '
        'çizim enformasyon iletir; belirsizlik istenmez. Sanatsal çizim duygu ve yorum '
        'içerebilir.', S_BD))
    e.append(Paragraph(
        'Öte yandan: İzometrik çizimde simetri ve denge estetik bir kaygıdır. Tasarım '
        'Kartı\'nı oluştururken renk seçimi, alan dengesi, font boyutu — bunlar grafik '
        'tasarım kararlarıdır. Öğrenciler fark etmeden hem teknik hem de sanatsal '
        'düşünüyor.', S_BD))

    e.append(Paragraph('4.4 Fen Bilgisi: Malzeme ve Yapı', S_H2))
    e.append(Paragraph(
        '3B yazıcıyla üretim bağlamında: Tinkercad\'de tasarlanan nesne hangi malzemeden '
        'üretilirse ne kadar dayanıklı olur? PLA filament kırılgan mı, esnek mi? Bu sorular '
        'Fen Bilgisi\'nin malzeme konusuna bağlanır.', S_BD))
    e.append(Paragraph(
        '<b>Bütünleşik etkinlik fikri:</b> Fen dersinde "malzeme özellikleri" işlenirken '
        'öğrencilerden Tinkercad\'de o malzemeden yapılmış bir nesne tasarlamaları '
        'istenebilir.', S_NOT))
    return e


# ============================================================
# BÖLÜM 5 — GÜNÜMÜZ CAD VE TÜRK ENDÜSTRİSİ
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'GÜNÜMÜZ CAD VE TÜRK ENDÜSTRİSİ')

    e.append(Paragraph('5.1 TOGG: Yerli Otomobilin Dijital Temeli', S_H2))
    e.append(Paragraph(
        'TOGG T10X\'in tasarım süreci tamamen dijital ortamda yürütüldü. Araç, üretim '
        'hattına gelmeden önce milyonlarca sanal testle geçirildi: Aerodinamik simülasyon, '
        'çarpışma testi, ısı yönetimi — bunların hepsi dijital ikiz (digital twin) '
        'üzerinde yapıldı.', S_BD))
    e.append(Paragraph(
        'Pininfarina, araca estetik forma katkı yaptı. Ancak Türk mühendisler tüm yapısal '
        've mekanik tasarımı Dassault Systèmes\'in 3DEXPERIENCE platformu üzerinde '
        'geliştirdi. Bu platform, SolidWorks ve CATIA gibi araçları tek çatı altında toplar.',
        S_BD))
    e.append(bilgi_kutusu(
        'Öğrencilere Mesaj',
        ['"Bu derste Tinkercad kullanıyorsunuz."',
         '"TOGG mühendisleri çok daha güçlü araçlar kullanıyor — ama temel mantık aynı: '
         'temel şekiller + birleştirme/çıkarma + ölçü hassasiyeti."']))

    e.append(Paragraph('5.2 Savunma Sanayii ve CAD', S_H2))
    e.append(Paragraph(
        'Türkiye\'nin Bayraktar TB2 insansız hava aracı, Akıncı ve Aksungur dahil tüm '
        'platformların tasarımı CAD ortamında yapılmaktadır. Roketsan\'ın füzeleri, '
        'Aselsan\'ın elektronik sistemleri, TUSAŞ\'ın uçak gövdeleri — bunların tamamı '
        '3B CAD modellemeden çıkar.', S_BD))
    e.append(Paragraph(
        'TUSAŞ (Türkiye\'nin milli havacılık şirketi), mühendis yetiştirme kapsamında '
        'bazı liselerde CAD eğitimleri düzenlemektedir. Bu ünitedeki beceriler potansiyel '
        'havacılık mühendisliği kariyer yolunun ilk adımıdır.', S_BD))
    return e


# ============================================================
# BÖLÜM 6 — YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI
# ============================================================

def bolum6():
    e = []
    e += bolum_baslik(6, 'YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI')
    e.append(Paragraph(
        'Aşağıdaki yanlış anlamalar öğrencilerin büyük çoğunluğunda görülür. '
        'Bunları ders başında "tuzak soru" olarak kullanabilir ya da akışta '
        'düzeltme fırsatı çıktığında hazırlıklı olabilirsiniz.', S_BD))

    yanlis = [
        ('"2B tasarım eskimiş, herkes 3B kullanıyor"',
         '2B teknik çizim hâlâ mühendislik ve mimarliğin standart dilidir. Kat planı, devre '
         'şeması, logo tasarımı — hepsi 2B\'dir. İkisi birbirini tamamlar.'),
        ('"Üst görünüş = nesnenin üst yüzeyinin resmi"',
         'Üst görünüş, nesnenin tam yukarıdan bakıldığında düzlemsel olarak çizilmesidir; '
         'perspektif değil, dik projeksiyon.'),
        ('"Tinkercad\'de ne çizersem o kadar büyük üretilir"',
         'Tinkercad\'de ölçüler milimetreyle ifade edilir. Gerçek boyutu belirleyen, ölçü '
         'kutusuna yazılan sayıdır; ekranda büyük görünmesi değil.'),
        ('"Delik (Hole) = silgi gibi bir şey"',
         'Hole, bir şekli silmez; onu maske olarak kullanır. Başka bir şekle Ctrl+G ile '
         'gruplandırılınca, Hole olan şeklin kapladığı alan çıkarılır.'),
        ('"İzometrik çizim = perspektif çizim"',
         'Perspektifte uzak nesneler küçülür, yakınlar büyür. İzometrikte tüm ölçüler eşit '
         'kalır. İzometrik ölçü bilgisini korur; perspektif gerçekçi görünüm verir.'),
        ('"Görünüş sayısı ne kadar fazla olursa o kadar iyi"',
         'Gerekli olmayan görünüş çizilmez. Basit bir nesne için 2 görünüş yeterlidir; '
         'karmaşık nesneler 3 veya daha fazla gerektirebilir.'),
        ('"Çoklu ortam sunusu sadece Tasarım Kartı demektir"',
         'Çoklu ortam sunusu yazı + görsel + dijital içeriği birleştiren genel bir iletişim '
         'biçimidir. Tasarım Kartı bu ünitede üretilen özel örneğidir.'),
        ('"Kâğıtta planlamak zaman kaybı, direkt bilgisayarda yaparım"',
         'Kâğıt planı hızlı deneme-yanılmaya olanak verir. Tinkercad\'de hata yapmak '
         'yavaştır; kâğıtta çizim 10 kat hızlı prototipleme sağlar.'),
    ]

    y_data = [[Paragraph('Yanlış Anlama', S_TH), Paragraph('Doğru Açıklama', S_TH)]]
    for yan, duz in yanlis:
        y_data.append([Paragraph(yan, S_TCB), Paragraph(duz, S_TC)])

    y_t = Table(y_data, colWidths=[CW*0.38, CW*0.62])
    y_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, COLOR_VERY_LIGHT]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    e.append(y_t)
    return e


# ============================================================
# BÖLÜM 7 — SINIFTA ANLATILABİLECEK HİKAYELER
# ============================================================

def bolum7():
    e = []
    e += bolum_baslik(7, 'SINIFTA ANLATILABİLECEK HİKAYELER')
    e.append(Paragraph(
        'Somut hikayeler soyut kavramları kalıcı hale getirir. Aşağıdaki anlatılar '
        'ilgili kavramlara bağlanarak ders akışına doğal biçimde yerleştirilebilir.',
        S_BD))

    e.append(hikaye(
        'Ivan Sutherland\'ın Çılgın Tezi (1963)',
        ['Ivan Sutherland, doktora tezini yazmak için bir yıl bilgisayar odasında geçirdi. '
         'Kullandığı bilgisayar — TX-2 — bir oda büyüklüğündeydi ve o dönem için devasa '
         'bir güce sahipti.',
         'Sutherland\'ın yarattığı Sketchpad programı, ilk kez bir bilgisayarın ekranına '
         'bakarak elle çizim yapılabilmesine olanak tanıyordu. Doktora jürisindeki bir '
         'profesör "Bu tez olabilir mi? Bu bir bilim kurgu filmi!" demişti.',
         'Sutherland\'ın tezi 1988\'de Turing Ödülü ile taçlandırıldı. Bugün kullandığınız '
         'her grafik arayüz, her tasarım yazılımı, her video oyunu doğrudan '
         'Sketchpad\'in torunudur.'],
        '"Bilgisayarda çizim yapmak bugün çok olağan geliyor. Ama 60 yıl önce birisi '
        'bunu ilk kez yaptığında insanlar inanamadı." — CAD tarihine giriş.'))

    e.append(hikaye(
        'Boeing 777: Kâğıt Olmadan Tasarlanan İlk Uçak (1994)',
        ['Boeing, 1990\'ların başında yeni nesil geniş gövdeli yolcu uçağı 777 projesine '
         'başladı. Kararı cesurdu: Bu uçak tamamen bilgisayar ortamında tasarlanacaktı. '
         'Kâğıt çizim kullanılmayacaktı.',
         'Daha önce 757 ve 767 projelerinde parçalar fabrikada bir araya getirildiğinde '
         'uyuşmazlıklar ortaya çıkıyordu — bazı parçalar birbirine giremiyordu. 777\'de '
         'CATIA yazılımıyla tüm tasarım tek bir 3B dijital ortamda yapıldı.',
         '777\'nin kuyruğu ile gövdesinin birleşme noktasındaki uyuşmazlık hata payı '
         '0,023 inç oldu. Bir önceki uçakta bu hata 2 inç üzerindeydi. 777 bugün hâlâ '
         'üretilmekte ve dünyanın en güvenli geniş gövdeli uçakları arasında.'],
        '"Tinkercad\'de ölçüleri doğru girmek neden önemli?" sorusuna cevap. Gerçek '
        'mühendislikte küçük hatalar büyük sonuçlar doğurabilir.'))

    e.append(hikaye(
        'Şirketi Kurtaran Prototip: Dyson Süpürgesi (1978–1993)',
        ['James Dyson 1978\'de bir kâğıt fabrikasını ziyaret ederken talaş toplayan '
         'siklon sistemini gördü. "Süpürge torbası olmadan bu sistemle çalışan bir '
         'elektrikli süpürge yapılabilir mi?" diye sordu kendine.',
         'Cevabı bulmak için 15 yıl ve 5.127 prototip gerekti. İlk 5.126 prototip '
         'çalışmadı — ya çok gürültülüydü, ya güç yeterliydi ama emme yoktu, ya da '
         'dayanıklı değildi. Dyson her başarısızlıktan ne öğrendiğini not etti.',
         '1993\'te G-Force modeli piyasaya çıktı. Bugün Dyson bir mühendislik ve '
         'tasarım ikonu.'],
        'Öğrencilere: 3B modelde ilk denemelerinin çalışmaması normaldir — "prototip '
        'başarısızlığı öğrenmenin kendisidir."'))

    e.append(hikaye(
        'Tinkercad\'in Doğuşu: İki Fin ve Büyük Hedef (2011)',
        ['Kai Backman ve Mikko Mononen, web tabanlı 3B modellemenin herkes için '
         'erişilebilir olması gerektiğine inanıyordu. O zamanlar 3B modelleme yazılımları '
         'hem pahalıydı hem de öğrenmesi aylar süren karmaşık araçlardı.',
         'İkilinin fikri basitti: Temel geometrik şekillerle sürükle-bırak mantığında '
         'çalışan, herhangi bir kurulum gerektirmeyen, ücretsiz bir web uygulaması. '
         'Kullanıcı 5 dakikada bir model oluşturabilmeliydi.',
         'Autodesk 2013\'te şirketi satın aldı ve Tinkercad\'i ücretsiz bir eğitim '
         'aracı olarak korumaya devam etti.'],
        '"Bugün siz Tinkercad kullanıyorsunuz. Bu araç iki kişinin \'bu daha kolay '
        'olabilir\' demesiyle başladı."'))

    e.append(hikaye(
        'Çocuğun Düşüncesinden Çıkan Sanayi Standardı: LEGO ve 3B Modelleme',
        ['LEGO, 2010\'ların başında Digital Designer adlı bir yazılım geliştirdi. '
         'Çocuklar sanal LEGO parçalarıyla dijital ortamda inşaat yapabiliyordu. Yazılım, '
         'günümüz Tinkercad\'inin çalışma mantığına çok benziyordu: hazır birimler + '
         'birleştirme.',
         'Sonra LEGO bir adım daha attı: Dijital tasarımlı setleri gerçek parçalara '
         'dönüştürerek siparişe hazır hale getirdi.',
         'Bu bir döngüydü: Fiziksel → Dijital → Fiziksel. Tam olarak bu ünitedeki süreç: '
         'Kâğıt eskiz → Tinkercad modeli → (ileride) 3B baskı.'],
        '"LEGO\'nun fiziksel parçaları nasıl birleştiğini düşünün. '
        'Tinkercad\'de de tam aynı mantığı kullanıyorsunuz."'))

    return e


# ============================================================
# BÖLÜM 8 — ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR')
    e.append(Paragraph(
        'Bazı sorular anında yanıt gerektirmez. "Harika soru — düşünmem lazım" ya da '
        '"Bu konuyu ileride daha ayrıntılı işleyeceğiz" demek tamamen uygundur.',
        S_BD))

    qas = [
        ('"Neden görünüş çizmeyi öğreniyoruz? Zaten fotoğraf çekebiliriz."',
         'Fotoğraf bir bakış açısından çekilir ve perspektif nedeniyle gerçek ölçüleri '
         'bozar. Görünüş çizimi nesnenin tam geometrik bilgisini verir; hiçbir yorum veya '
         'perspektif bozulması yoktur. Makine parçası üretmek için fabrikaya fotoğraf '
         'değil, teknik çizim gönderilir. Ölçüler ve açılar net olmalıdır.'),
        ('"Tinkercad çok yavaş. Profesyoneller bunu kullanıyor mu?"',
         'Hayır, profesyoneller genellikle Tinkercad kullanmaz — SolidWorks, CATIA, '
         'Fusion 360 gibi daha güçlü araçlar kullanır. Ama Tinkercad\'in mantığı aynıdır: '
         'temel geometri + Boole işlemleri. Tinkercad\'i öğrenmek bu araçlara geçişi '
         'kolaylaştırır. Kalem yazmayı öğrenmek için kullanılan araç büyüyünce değişir, '
         'ama yazma eylemi aynı kalır.'),
        ('"Yapay zekâ zaten 3B modelleri otomatik üretiyor. Neden kendimiz çizelim?"',
         'YZ ile 3B model üretimi henüz çok erken aşamadadır ve üretilen modeller çoğunlukla '
         'görsel içerik için; üretilebilir teknik parçalar için değil. Daha da önemlisi: '
         'Modeli otomatik ürettirseniz de ne istediğinizi tarif etmek, üretilen modeli '
         'değerlendirmek ve düzeltmek için teknik bir anlayış gereklidir. Alet kullanan '
         'kişinin aklı hâlâ belirleyicidir.'),
        ('"3B yazıcı olmayan okullarda bu ünitenin ne anlamı var?"',
         'Dijital prototip, fiziksel üretimden bağımsız olarak değerlidir. Tinkercad modeli '
         'yapılabilirlik ve ölçülendirme düşüncesini geliştirir. Bu ünitenin asıl hedefi '
         '3B yazıcı kullanmak değil, mekânsal düşünme ve dijital tasarım becerisini '
         'kazandırmaktır. Kâğıt eskiz → 2B → 3B süreci ürün geliştirme mantığını öğretir.'),
        ('"Paint çok eski bir program, neden onu kullanıyoruz?"',
         'Paint\'in eski olması bir sorun değil, avantajdır: Arayüzü sade, kurulumu '
         'gereksiz, her Windows bilgisayarında hazır. Bu dersin amacı en gelişmiş grafik '
         'yazılımını öğretmek değil; 2B görünüş çizimini dijital ortama taşımaktır. '
         'Araç amaca hizmet ettiği sürece değerlidir.'),
        ('"İzometrik çizimde bütün kenarlar eşit mi? Gerçekçi değil ki."',
         'Gerçek değil, ama bu bilinçli bir tercih. İzometrik çizim gerçekçilik değil, '
         'ölçü bilgisi için kullanılır. Eğer uzaktaki kenar küçülseydi, o kenarın gerçek '
         'uzunluğunu ölçemezdik. Mühendisler izometrik çizim seçer çünkü çizimden doğrudan '
         'ölçü alabilmek ister. Mimari maket fotoğraflarının çoğu da izometrik perspektiften '
         'çekilir — aynı sebepten.'),
    ]

    for soru, cevap in qas:
        e.append(KeepTogether([
            Paragraph(soru, S_QQ),
            Paragraph(cevap, S_QA),
        ]))

    e.append(vsp(0.5))
    e.append(hr(c=COLOR_LIGHT_GREY))
    e.append(Paragraph(
        '<i>Bu doküman 4. Ünite öğretim sürecinin arka planını oluşturmak amacıyla '
        'hazırlanmıştır. Ders planı, sunum içeriği ve değerlendirme araçları ayrı '
        'dosyalarda yer almaktadır.</i>', S_NOT))
    return e


# ============================================================
# ANA FONKSİYON
# ============================================================

def main():
    doc = SimpleDocTemplate(
        CIKTI,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        title='4. Unite - Ogretmen Hazirlik Rehberi',
        author='Teknoloji ve Tasarim Ogretim Programi',
    )
    doc.unite_info = UI
    doc.doc_title  = 'Unite Icerigi Hazirlik Materyali'

    story = make_cover(
        title    = '4. Ünite — Ünite İçeriği Hazırlık Materyali',
        subtitle = 'Bilgisayar Destekli Tasarım',
        meta_info= {
            'Sınıf'       : '7. Sınıf',
            'Ders'        : 'Teknoloji ve Tasarım',
            'Ünite Süresi': '8 Ders Saati (4 Hafta)',
        },
        document_type='Öğretmen Hazırlık Rehberi',
    )

    story += bolum1()
    story += bolum2()
    story += bolum3()
    story += bolum4()
    story += bolum5()
    story += bolum6()
    story += bolum7()
    story += bolum8()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print('OK  U4_PDF_Ogretmen_Hazirlik.pdf')


if __name__ == '__main__':
    main()
