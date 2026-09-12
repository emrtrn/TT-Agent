# -*- coding: utf-8 -*-
"""
2. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit2/U2_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite2_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit2')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U2_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '2. Unite - Temel Tasarim'
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
S_BH  = ParagraphStyle('bh',  fontName='TR-Bold',    fontSize=9,  textColor=white, leading=12)
S_BB  = ParagraphStyle('bb',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, alignment=TA_JUSTIFY)
S_SH  = ParagraphStyle('sh',  fontName='TR-Bold',    fontSize=9,  textColor=white, leading=12)
S_SB  = ParagraphStyle('sb',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, alignment=TA_JUSTIFY)
S_SC  = ParagraphStyle('sc',  fontName='TR-Italic',  fontSize=8.5, textColor=COLOR_SECONDARY,
                         leading=12)
S_QQ  = ParagraphStyle('qq',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY,
                         leading=13, spaceBefore=6, spaceAfter=2)
S_QA  = ParagraphStyle('qa',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                         leading=13, spaceAfter=5, alignment=TA_JUSTIFY, leftIndent=10)
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
# BÖLÜM 1 — TASARIM ELEMANLARININ ANATOMİSİ
# ============================================================

def bolum1():
    e = []
    e += bolum_baslik(1, 'TASARIM ELEMANLARININ ANATOMİSİ')
    e.append(Paragraph(
        'Tasarım elemanları "görselliğin alfabesi" olarak tanımlanır. Nasıl ki Türkçenin 29 harfi '
        'birleşerek bütün metinleri oluşturuyorsa, bu sekiz eleman da birleşerek dünyadaki tüm görsel '
        'tasarımları oluşturur. Ancak harflerin aksine, tasarım elemanlarının tek başına anlamı yoktur — '
        'anlam kombinasyondan doğar.', S_BD))

    # 1.1 Nokta
    e.append(Paragraph('1.1 Nokta', S_H2))
    e.append(Paragraph(
        'Noktanın tasarımdaki rolü küçümsenmemelidir. Görsel ağırlık noktadan başlar.', S_BD))
    e.append(Paragraph(
        '<b>Tarihsel bağlam:</b> Empresyonist ressam Georges Seurat 1886\'da "Büyükada\'da Bir Pazar '
        'Öğleden Sonrası" adlı tablosunu sergiledi. Tablo tamamen noktalardan oluşuyordu — 2 milyon '
        'küçük nokta, iki yılda. Bu teknik Puentilizm olarak adlandırıldı. Seurat\'ın teorisi: '
        'Renkleri fırça darbeleriyle karıştırmak yerine gözde karışmasını sağlarsan renk daha canlı '
        'görünür. Optik bir yanılsama. Bugün dijital görüntülerin piksel mantığının ilk atasıdır.', S_BD))
    e.append(Paragraph(
        '<b>Günümüze taşıyın:</b> Her dijital fotoğraf ve ekran görüntüsü aslında noktalardan oluşur. '
        'Bir telefon ekranında 400 piksel/inç yoğunlukta milyonlarca nokta var. Seurat\'ın iki yılda '
        'yaptığını cebinizdeki cihaz saniyenin milyonda birinde yapıyor.', S_BD))
    e.append(Paragraph(
        '<b>Sınıfta kullanım:</b> "Kağıda tek bir nokta koyun. Sonra ikinci bir nokta koyun — ama '
        'ilkinden farklı bir yerde. Ne değişti?" Gözler iki nokta arasında gezinmeye başlar. Bu '
        'hareketin ta kendisi bir ilkedir: ritim.', S_NOT))

    # 1.2 Çizgi
    e.append(Paragraph('1.2 Çizgi', S_H2))
    e.append(Paragraph('Çizgi yönün, hızın ve duygunun taşıyıcısıdır.', S_BD))
    e.append(bilgi_kutusu(
        'Çizgi Türlerinin Psikolojisi',
        ['Yatay çizgiler: Sakinlik, istikrar, ufuk. Yatan insan, sakin deniz — hepsi yatay.',
         'Dikey çizgiler: Güç, resmiyet, yükseklik. Gotik katedrallerin dikey çizgileri "gözü '
         'gökyüzüne yönlendir" amacıyla tasarlanmıştır.',
         'Eğri çizgiler: Hareket, yumuşaklık, doğallık. Doğada düz çizgi nadirdir.',
         'Zikzak çizgiler: Heyecan, tehlike, enerji. Dikkat işaretleri ve elektrik sembolleri '
         'neden zikzaktır?']))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Türk çini sanatındaki "rumi motif" kıvrım hatları, Selçuklu '
        'döneminde geometrik motiflerle birleşerek özgün bir dil oluşturdu. Aynı çizgi dili Osmanlı '
        'mimarisinde kemerlere, yazmalara ve halılara yansıdı.', S_BD))

    # 1.3 Renk
    e.append(Paragraph('1.3 Renk', S_H2))
    e.append(Paragraph(
        'Renk, tasarım elemanlarının en güçlüsü ve en karmaşığıdır. Hem fizik hem kimya hem psikoloji '
        'hem kültürdür.', S_BD))
    e.append(Paragraph(
        '<b>Fiziksel gerçeklik:</b> Renk nesnenin kendisinde değil, ışıkta vardır. Bir domates kırmızı '
        'değildir — yüzeyindeki pigmentler kırmızı dalga boyunu yansıtır, diğerlerini emer. Newton '
        '1666\'da bir prizmadan geçirdiği beyaz ışığın yedi renge ayrıldığını gösterdi.', S_BD))

    renk_data = [
        [Paragraph('Renk', S_TH), Paragraph('Türkiye / İslam', S_TH), Paragraph('Batı', S_TH), Paragraph('Asya', S_TH)],
        [Paragraph('Beyaz', S_TC), Paragraph('Saflık', S_TC), Paragraph('Düğün, saflık', S_TC), Paragraph('Yas (Çin, Japonya)', S_TC)],
        [Paragraph('Kırmızı', S_TC), Paragraph('Cesaret, şehitlik', S_TC), Paragraph('Tehlike, dur', S_TC), Paragraph('Şans, mutluluk', S_TC)],
        [Paragraph('Yeşil', S_TC), Paragraph('Cennet rengi', S_TC), Paragraph('Çevre, doğa', S_TC), Paragraph('Verimlilik', S_TC)],
    ]
    renk_t = Table(renk_data, colWidths=[CW*0.18, CW*0.27, CW*0.27, CW*0.28])
    renk_t.setStyle(TableStyle([
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
    e.append(KeepTogether([renk_t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>İlginç gerçek:</b> McDonald\'s neden kırmızı ve sarı? Bu kombinasyonun iştah açtığı '
        've hızlı yemeğe uygun ruh hali yarattığı araştırmalarla desteklenmiştir. Mavi renk ise '
        'iştahı baskıladığı için fast food zincirlerinde neredeyse hiç kullanılmaz.', S_BD))

    # 1.4 Doku
    e.append(Paragraph('1.4 Doku', S_H2))
    e.append(Paragraph(
        'Doku hem görsel hem dokunsal bir elemandır. Gerçek (taktil) doku dokunulduğunda hissedilir; '
        'görsel (simüle) doku ise görüntüde var olan ama elle hissedilmeyen dokudur — bir fotoğraftaki '
        'ahşap desen gibi.', S_BD))
    e.append(Paragraph(
        '<b>Neden önemli?</b> Doku güven ve kalite algısını doğrudan etkiler. Araştırmalar ağır ve '
        'sert hissettiren nesnelerin daha kaliteli algılandığını göstermiştir. Lüks araba kapıları '
        'kasıtlı olarak ağır yapılır — kapıyı kapatırken duyulan "tok" ses mühendislerin tasarladığı '
        'bir kalite sinyalidir.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Bir Hereke halısında metrekare başına 1 milyon düğüm olabilir. '
        'Bu yoğunluk, dokunulduğunda hissedilen kadife gibi yumuşaklığı ve görsel olarak algılanan '
        'renk derinliğini aynı anda yaratır. Hereke halıları bugün müzelik eserler olarak değerlendiriliyor.', S_BD))

    # 1.5 Şekil
    e.append(Paragraph('1.5 Şekil', S_H2))
    e.append(Paragraph(
        'Şekil, sınırlı bir alanı çevreleyen formun iki boyutlu ifadesidir. Üç temel kategori: '
        '<b>Geometrik</b> (kare, daire, üçgen), <b>Organik / biyomorfik</b> (yaprak şekli, nehir '
        'kolları) ve <b>Sembolik</b> (kalp, yıldız, hilal).', S_BD))
    e.append(bilgi_kutusu(
        'Gestalt Teorisi: Beyin Parçaları Değil Bütünü Algılar',
        ['Alman psikologlar 20. yüzyıl başında Gestalt (Almanca: bütün, form) teorisini geliştirdi.',
         'Temel ilke: Beyin parçaları tek tek değil, bütün olarak algılar. Tamamlanmamış şekilleri '
         'bile tamamlar — bir daire eksik olsa bile daire olarak görürsünüz.',
         'WWF amblemi: Siyah-beyaz lekeler tam bir panda çizimi değildir. Gestalt ilkesi sayesinde '
         'beyin eksik bilgiyi tamamlar. Daha az çizgiyle daha güçlü bir görsel elde edilir.',
         'Tasarımcılar bu psikolojik eğilimi bilinçli olarak kullanır.']))

    # 1.6 Ton ve Valör
    e.append(Paragraph('1.6 Ton ve Valör', S_H2))
    e.append(Paragraph(
        'Bu iki kavram genellikle birbirine karışır. <b>Ton:</b> Bir rengin açıklık-koyuluk derecesi '
        '(açık mavi, koyu mavi). <b>Valör:</b> Siyah ile beyaz arasındaki gri skalasında konum — '
        'renk değil, parlaklık-koyuluk ilişkisi.', S_BD))
    e.append(Paragraph(
        '<b>Neden ressamlar tonu öğrenir?</b> Işık ve gölge olmadan üç boyutluluk algısı yoktur. '
        'Karakalem çizimlerinde renk yoktur ama derinlik vardır — tamamen ton/valör sayesinde.', S_BD))
    e.append(Paragraph(
        '<b>Sınıfta kullanım:</b> Renkli bir fotoğrafın siyah-beyaz versiyonuna bakın. Benzer tondaki '
        'renkler grayscale\'de birbirinden ayırt edilemez. Bu, renk seçiminde kontrast yaratmanın '
        'neden önemli olduğunu gösterir.', S_NOT))

    # 1.7 Mekân
    e.append(Paragraph('1.7 Mekân (Uzam)', S_H2))
    e.append(Paragraph(
        'Mekân elemanı tasarımın "nefes aldığı" alandır. Bir tasarımda kullanılmayan boş alan '
        '<b>negatif alan</b>, kullanılan dolu alan <b>pozitif alan</b> olarak adlandırılır.', S_BD))
    e.append(Paragraph(
        '<b>Negatif alanın gücü:</b> Apple\'ın ürün fotoğraflarında geniş beyaz boşluklar bırakılır. '
        'Bu "israf" değil, bilinçli bir mesajdır: Ürün o kadar önemlidir ki başka hiçbir şeye yer '
        'yoktur. Tasarım terminolojisinde buna "breathing room" (nefes alanı) denir.', S_BD))
    e.append(Paragraph(
        '<b>Mimaride mekân:</b> Selimiye Camii\'nde kubbe altındaki geniş ve bölümsüz iç alan bu '
        'ilkenin Osmanlı mimarisindeki mükemmel ifadesidir. Mimar Sinan\'ın iç mekânın orantısını '
        've kubbe altındaki boş alanı bilinçli hesapladığı bilinmektedir.', S_BD))

    # 1.8 Biçim / Form
    e.append(Paragraph('1.8 Biçim / Form', S_H2))
    e.append(Paragraph(
        'Biçim (form), şeklin üç boyutlu halidir ya da iki boyutlu bir yüzeyde üç boyutluluk izlenimi '
        'verir. Daire (şekil) → küre (biçim). Kare (şekil) → küp (biçim).', S_BD))
    e.append(Paragraph(
        '<b>Endüstriyel tasarımda biçim:</b> Jonathan Ive, Apple\'ın ürün tasarımını 20 yıl yönetti. '
        'Tasarım felsefesi: Gereksiz her şeyi kaldır. iPod ilk çıktığında rakip MP3 çalarlar onlarca '
        'düğmeye sahipti. iPod\'un click wheel\'i tek bir bileşenle her işlevi yapıyordu — minimum '
        'dışarı çıkıntı, maksimum yüzey bütünlüğü.', S_BD))

    return e


# ============================================================
# BÖLÜM 2 — TASARIM İLKELERİNİN ANATOMİSİ
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TASARIM İLKELERİNİN ANATOMİSİ')
    e.append(Paragraph(
        'Eğer elemanlar alfabeyse, ilkeler dilbilgisidir. Harfleri doğru sıralamazsanız anlamsız '
        'kelimeler çıkar; elemanları ilkelerle organize etmezseniz kaotik görüntüler ortaya çıkar. '
        'İlkeler kural değil, araçtır — bilinçli olarak kırılabilirler.', S_BD))

    # 2.1 Denge
    e.append(Paragraph('2.1 Denge', S_H2))
    e.append(Paragraph(
        'Denge, bir kompozisyondaki görsel ağırlığın dağılımıdır. Beyin dengesizliği tehlike sinyali '
        'olarak algılar — evrimsel bir miras. Bu yüzden dengesiz kompozisyonlar rahatsız eder, dengeli '
        'kompozisyonlar rahatlatır.', S_BD))

    denge_data = [
        [Paragraph('Tür', S_TH), Paragraph('Tanım', S_TH), Paragraph('Etki', S_TH)],
        [Paragraph('Simetrik', S_TC), Paragraph('Eksenin iki yanı birbirinin aynısı', S_TC), Paragraph('Güven, resmiyet, istikrar', S_TC)],
        [Paragraph('Asimetrik', S_TC), Paragraph('İki yan farklı ama görsel ağırlık eşit', S_TC), Paragraph('Dinamizm, modern his', S_TC)],
        [Paragraph('Radyal', S_TC), Paragraph('Merkezden dışarıya yayılma', S_TC), Paragraph('Hareket, güneş hissi', S_TC)],
    ]
    denge_t = Table(denge_data, colWidths=[CW*0.22, CW*0.42, CW*0.36])
    denge_t.setStyle(TableStyle([
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
    e.append(KeepTogether([denge_t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Türk bayrağı simetrik değildir — hilal ve yıldız sola '
        'kaymıştır. Bu bilinçli asimetrik denge: hareket ve dinamizm mesajı verir.', S_BD))

    # 2.2 Ritim
    e.append(Paragraph('2.2 Ritim', S_H2))
    e.append(Paragraph(
        'Ritim, tekrarlanan elemanların oluşturduğu görsel harekettir. Müzikteki ritimle aynı '
        'ilkeyi paylaşır: döngüsellik, beklenti ve tatmin. Göz ritimli bir tasarımda "ne geleceğini" '
        'öngörmeye başlar. Bu beklenti karşılandığında tatmin, bozulduğunda sürpriz yaratır.', S_BD))
    e.append(Paragraph(
        '<b>Türk sanatında ritim:</b> Türk halı dokumacılığında ve çini sanatında tekrarlanan '
        'geometrik motifler kusursuz ritim oluşturur. Yıldız, sekizgen ve baklava formları sonsuz '
        'tekrarla simetrik örüntüler oluşturur — matematiksel bir düzenin görsel ifadesidir.', S_BD))
    e.append(Paragraph(
        '<b>Dikkat çekici bağlantı:</b> Müzisyenler "senkop" kullanırlar — beklenen ritim vurgusu '
        'atlanır, sonra bir sonrakine güçlü basılır. Tasarımda da benzer teknikler var: bir tekrar '
        'serisi içinde bir eleman büyütülür ya da renklenir. Bu o noktayı vurgu noktasına '
        'dönüştürür.', S_BD))

    # 2.3 Vurgu
    e.append(Paragraph('2.3 Vurgu', S_H2))
    e.append(Paragraph(
        'Vurgu, izleyicinin gözünün ilk gideceği noktadır. Her tasarımda hiyerarşi vardır: neyin '
        'daha önce görüleceği tasarımcının kontrolündedir. Buna "görsel hiyerarşi" denir.', S_BD))
    vurgu_yollar = [
        'Boyut: Büyük olan önce görülür.',
        'Renk: Çevresiyle zıt renkli nesne öne çıkar.',
        'İzolasyon: Kalabalık içinde yalnız duran nesne.',
        'Yön: Diğer elemanların işaret ettiği nokta.',
        'Doku: Pürüzlü yüzey düz yüzeyden ayrışır.',
    ]
    for v in vurgu_yollar:
        e.append(Paragraph(f'• {v}', S_BUL))
    e.append(Paragraph(
        '<b>Gazete sayfası örneği:</b> Bir gazetenin ön sayfasındaki hiyerarşiyi analiz etmek '
        'mükemmel bir sınıf etkinliğidir. Başlık boyutu, fotoğraf yerleşimi, sütun genişlikleri — '
        'bunların tümü editörün "önce bunu okuyun" kararının görsel ifadesidir.', S_BD))

    # 2.4 Hareket
    e.append(Paragraph('2.4 Hareket', S_H2))
    e.append(Paragraph(
        'Hareket, statik bir tasarımda gözün izlediği yoldur. Tasarım dondurulmuş bir andır — '
        'ama gözünüz ona bakışta harekete geçer. Tasarımcılar bu göz hareketini yönetir.', S_BD))
    e.append(Paragraph(
        '<b>Üçgen kompozisyon:</b> Fotoğrafçılık ve resim sanatında klasik teknik; üç önemli nesneyi '
        'bir üçgen oluşturacak şekilde yerleştirmektir. Göz bu üçgende döner — soldan sağa, sonra '
        'merkeze, sonra sola. Saatlerce bakılabilecek fotoğraflar genellikle bu ilkeyi kullanır.', S_BD))
    e.append(Paragraph(
        '<b>Diyagonal çizgiler:</b> Köşeye çekilen yol fotoğraflarında göz diyagonali takip eder '
        've sonsuzluğa uzanmış gibi hisseder — perspektif derinlik yaratır, beyin derinliği hareket '
        'olarak yorumlar.', S_BD))

    # 2.5 Birlik
    e.append(Paragraph('2.5 Birlik', S_H2))
    e.append(Paragraph(
        'Birlik, tüm elemanların uyumlu bir bütün oluşturmasıdır. Birlik olmayan tasarım "parçalı" '
        've "dağınık" hissettirir. Teknikler: tekrar, yakınlık, süreklilik, ortak zemin.', S_BD))
    e.append(Paragraph(
        '<b>Marka kimliği örneği:</b> Türk Hava Yolları\'nın tüm görsel materyallerini bir düşünün — '
        'uçak gövdesi, koltuk başlıkları, yemek tabakları, bilet sistemi, hostes üniforması. '
        'Bunların hepsi aynı renk, font ve görsel dili paylaşır. Bu birlik "güvenilirlik" mesajı '
        'verir. Tek bir tutarsızlık bu mesajı zayıflatır.', S_BD))

    # 2.6 Çeşitlilik
    e.append(Paragraph('2.6 Çeşitlilik', S_H2))
    e.append(Paragraph(
        'Çeşitlilik, birliğin karşı ağırlığıdır. Tamamen birlikli tasarım monoton olur; tamamen '
        'çeşitlikli tasarım kaotik. Denge tam da bu gerilimde kurulur.', S_BD))
    e.append(Paragraph(
        '<b>Sınıfta kullanım:</b> "Siyah beyaz bir tasarım çeşitlilikten yoksun mudur?" Yanıt: '
        'Hayır. Siyah-beyaz tasarımda çeşitlilik ton/valör farklarından, boyuttan ve şekil '
        'farklılıklarından gelir. Çeşitlilik sadece renk değil, tüm elemanları kapsar.', S_NOT))

    # 2.7 Zıtlık
    e.append(Paragraph('2.7 Zıtlık (Kontrast)', S_H2))
    e.append(Paragraph(
        'Zıtlık, birbirinden farklı elemanların bir arada kullanılarak her ikisini de güçlendirmesidir. '
        'Kontrast türleri: renk zıtlığı (kırmızı-yeşil), boyut zıtlığı, ton zıtlığı (beyaz '
        'zemin + siyah metin en yüksek okunabilirlik), şekil zıtlığı, doku zıtlığı.', S_BD))
    e.append(Paragraph(
        '<b>Erişilebilirlik bağlantısı:</b> Renk körü kişiler için tasarım yaparken kontrast '
        'kritik öneme taşır. "Yalnızca renge güvenme" ilkesi bu yüzden önemlidir — şekil, boyut '
        've ton kontrastı rengi tamamlamalıdır.', S_BD))

    # 2.8 Oran-Orantı
    e.append(Paragraph('2.8 Oran-Orantı', S_H2))
    e.append(Paragraph(
        'Oran, elemanların birbirine ve bütüne göre boyutsal ilişkisidir. <b>Altın Oran:</b> '
        'Yaklaşık 1:1.618. Fibonacci dizisiyle ilişkili. Parthenon\'un cephesi, spiral kabuklar, '
        'çiçek tohumlarının dizilişi hep bu orana yakındır.', S_BD))
    e.append(Paragraph(
        '<b>Önemli not:</b> Altın oranın evrensel estetik üstünlüğü bugün sorgulanmaktadır. '
        '2015\'te yapılan büyük çaplı bir çalışmada insanların altın oranı anlamlı biçimde '
        'tercih etmediği gösterildi. Altın oran güçlü bir örgütleyici araçtır, ama "evrensel '
        'güzelliğin matematiksel kodu" değildir.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Mimar Sinan\'ın Süleymaniye Camii\'nde sütun aralıkları, '
        'pencere boyutları ve kubbe oranları birbiriyle orantılıdır. 16. yüzyıl Osmanlı mimarlığı '
        'bu matematiksel oranları sezgiyle ve deneyimle uygulamıştır; hesap makinesi yokken.', S_BD))

    return e


# ============================================================
# BÖLÜM 3 — TÜRK SANAT GELENEĞİNDE ELEMAN VE İLKELER
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'TÜRK SANAT GELENEĞİNDE ELEMAN VE İLKELER')
    e.append(Paragraph(
        'Bu bölüm, ders saatlerinde kullanılacak Türk sanat görselleri için arka plan bilgisi sunar. '
        'Her sanat dalı elemanlar ve ilkeler açısından incelenmektedir.', S_BD))

    # 3.1 Halı ve Kilim
    e.append(Paragraph('3.1 Halı ve Kilim', S_H2))
    e.append(Paragraph(
        'Türk halı geleneği dünyanın en eski ve en gelişmiş tekstil sanatlarından biridir. '
        'Hunlardan kalma en eski halı örneği olan Pazırık Halısı M.Ö. 500 yılına tarihlenir '
        've Sibirya\'da bulunmuştur. Osmanlı döneminde Hereke, Uşak, Kula ve Gördes halıları '
        'dünya çapında ün kazandı.', S_BD))
    e.append(Paragraph('Tasarım elemanları ve ilkeleri açısından:', S_H3))
    halı_liste = [
        '<b>Geometrik motifler:</b> Yıldız, sekizgen, baklava ve rumi motifleri tekrar ilkesini mükemmel biçimde uygular.',
        '<b>Renk hiyerarşisi:</b> Çerçeve rengi, zemin rengi ve motif rengi birbiriyle orantılıdır — vurgu ve birlik ilkeleri aynı anda sağlanır.',
        '<b>Simetri:</b> Halıların büyük çoğunluğu hem dikey hem yatay eksende simetriktir.',
        '<b>Sınır (bordür):</b> Halının dış çerçevesi iç alanı tamamlayan bir ritim oluşturur.',
    ]
    for h in halı_liste:
        e.append(Paragraph(f'• {h}', S_BUL))
    e.append(Paragraph(
        '<b>Sınıfta kullanım:</b> Herhangi bir geleneksel Türk halısının görselini akıllı tahtaya '
        'getirin. "Bu halıda kaç tasarım ilkesi bulabilirsiniz?" sorusu tüm ilkeleri '
        'buldurmaya yeter.', S_NOT))

    # 3.2 İznik Çini Sanatı
    e.append(Paragraph('3.2 İznik Çini Sanatı', S_H2))
    e.append(Paragraph(
        'İznik (Nicaea) 15-16. yüzyıllarda dünyanın en önemli seramik üretim merkeziydi. '
        'İznik\'te 300\'den fazla atölye çalışıyordu. Süleymaniye Camii, Topkapı Sarayı ve '
        'sayısız Osmanlı eseri İznik çinileriyle süslüdür.', S_BD))
    e.append(bilgi_kutusu(
        'İznik Kırmızısının Sırrı',
        ['"Mercan kırmızısı" ya da "İznik kırmızısı" olarak bilinen bu renk kendine özgü bir teknikle '
         'elde edilirdi — içi mercan gibi küçük tanecikler barındıran kabartmalı bir yüzey.',
         'Bu rengi Avrupalı üreticiler 200 yıl boyunca taklit etmeye çalıştı, başaramadı.',
         'Formül 17. yüzyılda unutuldu. 20. yüzyılda Türk araştırmacılar tarafından yeniden '
         'keşfedildi.']))
    e.append(Paragraph('Tasarım elemanları açısından:', S_H3))
    cini_liste = [
        '<b>Çizgi:</b> Şakayık, karanfil, lale ve asma motifleri akıcı eğri çizgilerle tanımlanır.',
        '<b>Renk:</b> Kobalt mavi + beyaz zeminin kontrastı zıtlık ilkesinin mükemmel örneğidir.',
        '<b>Ritim:</b> Tekrarlanan motifler yüzey boyunca kesintisiz ritim yaratır.',
        '<b>Birlik:</b> Her panoda renk ve motif dili tutarlıdır.',
    ]
    for c in cini_liste:
        e.append(Paragraph(f'• {c}', S_BUL))

    # 3.3 Hat Sanatı
    e.append(Paragraph('3.3 Hat Sanatı', S_H2))
    e.append(Paragraph(
        'Hat, yazı güzelliği sanatıdır. Osmanlı hat sanatı dünyanın en gelişmiş hat geleneklerinden '
        'biridir. Süleymaniye Camii\'nin içindeki levhalar bu geleneğin doruk noktalarındandır.', S_BD))
    e.append(Paragraph(
        '<b>Neden tasarım dersiyle bağlantısı güçlü?</b> Hat sanatı yazı harflerini şekil ve biçim '
        'elemanlarına dönüştürür. Hat ustası bir metnin anlamını korurken kompozisyonunu görsel bir '
        'dengeye oturtur — hem semantik (anlam) hem estetik (görsel) bir tasarım sorunudur.', S_BD))
    e.append(Paragraph(
        '<b>İlginç gerçek:</b> Osmanlı levhalarındaki bazı hat eserleri, anlam taşıyan bir kelime '
        'oluşturan ama aynı zamanda kuş, tekne ya da insan figürü şeklinde düzenlenmiş harflerden '
        'oluşur. Kelime hem okunur hem görülür. Buna "nesih figür hat" denir.', S_BD))

    # 3.4 Ebru
    e.append(Paragraph('3.4 Ebru', S_H2))
    e.append(Paragraph(
        'Ebru, su yüzeyine damlanan boya ile desen oluşturma sanatıdır. Kıvamlı su yüzeyine '
        '(kitre eriğiyle kıvamlandırılmış) boya damlatılır, ince çubuk veya tarak ile harekete '
        'geçirilir. Kağıt yüzeye bastırılarak desen transfer edilir. Her ebru tektir — '
        'aynısı bir daha yapılamaz.', S_BD))
    e.append(Paragraph(
        'Ebru çizgi, renk, doku ve hareket ilkelerinin doğal bir gösterimidir. Su üzerinde '
        'renklerin birbirine geçmesi kontrol edilebilir ama tam olarak öngörülemez. Bu belirsizlik '
        'ebruyu diğer sanat dallarından ayırır; "süreç" ile "tesadüf" ilişkisi üzerine güçlü bir '
        'sınıf tartışması açar.', S_BD))
    e.append(Paragraph(
        '<b>Kültürel miras:</b> 2014\'te UNESCO, Türk ebru sanatını "İnsanlığın Somut Olmayan '
        'Kültürel Mirası" listesine aldı.', S_BD))

    return e


# ============================================================
# BÖLÜM 4 — RENK TEORİSİ: DERİNLEMESİNE
# ============================================================

def bolum4():
    e = []
    e += bolum_baslik(4, 'RENK TEORİSİ: DERİNLEMESİNE')
    e.append(Paragraph(
        'Bu bölüm 1. ve 2. derste renk konusunda "peki neden?" sorularına hazırlar. '
        'Renk elemanı hem fiziksel hem psikolojik hem kültürel bir kavramdır; bu '
        'üç boyutun tamamını kavramak dersi zenginleştirir.', S_BD))

    # 4.1 Renk Çemberi
    e.append(Paragraph('4.1 Renk Çemberi ve Tarihsel Arka Plan', S_H2))
    e.append(Paragraph(
        '1666\'da Newton rengi fiziksel bir gerçeklik olarak tanımladı. 1810\'da Goethe "Renk '
        'Teorisi" kitabında rengin psikolojik boyutunu ele aldı. 1961\'de Johannes Itten Bauhaus\'ta '
        'renk teorisini sanatsal uygulamaya bağladı.', S_BD))

    e.append(bilgi_kutusu(
        'Temel Renk Kategorileri',
        ['Ana (Primer) renkler: Kırmızı, Sarı, Mavi. Diğerleriyle oluşturulamaz.',
         'Ara (Sekonder) renkler: İki ana rengin karışımı. Turuncu (kırmızı+sarı), '
         'Yeşil (sarı+mavi), Mor (mavi+kırmızı).',
         'Üçüncü renkler: Ana + Ara renk karışımı. Sarı-turuncu, Kırmızı-turuncu vb.',
         'Sıcak renkler: Kırmızı, turuncu, sarı — enerji, ateş, güneş; yakınlaştırıcı.',
         'Soğuk renkler: Mavi, yeşil, mor — su, gökyüzü, gölge; uzaklaştırıcı.']))

    # 4.2 Tamamlayıcı Renkler
    e.append(Paragraph('4.2 Tamamlayıcı Renkler', S_H2))
    e.append(Paragraph(
        'Renk çemberinde karşılıklı duran renkler birbirinin tamamlayıcısıdır: kırmızı-yeşil, '
        'sarı-mor, turuncu-mavi. Yan yana getirildiğinde her ikisi de daha canlı görünür — '
        'simultane kontrast etkisi.', S_BD))
    e.append(Paragraph(
        '<b>İlginç uygulama:</b> Neden hemşireler ve cerrahlar yeşil önlük giyer? Ameliyat '
        'boyunca kırmızı kana bakan göz, tamamlayıcı renk olan yeşilin artı görüntüsüne sahip '
        'olur. Yeşil önlük bu artı görüntüyü maskeler, görsel yorgunluğu azaltır.', S_BD))
    e.append(Paragraph(
        '<b>Tasarım uygulaması:</b> Tamamlayıcı renk çiftleri güçlü kontrast yaratır. Ama '
        'dikkatli kullanılmazsa "titreşim" etkisi oluşur — eşit yoğunluktaki tamamlayıcı '
        'renkler yan yana gelince göz yorucu bir titreşim hissi verir. Bu yüzden genellikle '
        'biri baskın, diğeri vurgu rengi olarak kullanılır.', S_BD))

    return e


# ============================================================
# BÖLÜM 5 — YENİDEN YORUMLAMA VE ANALOJİ
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'YENİDEN YORUMLAMA VE ANALOJİ')
    e.append(Paragraph(
        'Bu ünite iki kritik düşünce becerisi içerir: yeniden yorumlama ve analoji. Her ikisi de '
        'öğrencilerin sezgiyle uyguladığı ama kavramsal olarak tanımlamakta zorlandığı '
        'süreçlerdir.', S_BD))

    # 5.1 Yeniden Yorumlama
    e.append(Paragraph('5.1 Yeniden Yorumlama Nedir?', S_H2))
    e.append(Paragraph(
        'Yeniden yorumlama, bir eserin bağlamını ve özünü koruyarak onu yeni bir bakış açısı '
        'veya teknikle ifade etmektir.', S_BD))
    e.append(bilgi_kutusu(
        'Kopyalamadan Farkı',
        ['Kopyalama: Orijinalin birebir tekrarı. Öğrenme aracı olarak değerlidir ama yaratıcılık '
         'yoktur.',
         'Yeniden yorumlama: Özü koruyarak dönüştürme. Hem orijinale saygı hem yaratıcı katkı.',
         'Picasso: "İyi sanatçılar kopyalar, büyük sanatçılar çalar." Kastettiği: Büyük sanatçı bir '
         'eserden etkilenerek onu sindirip kendi perspektifinden yeniden üretir, özgün bir şey '
         'ortaya çıkar.']))
    e.append(Paragraph(
        '<b>Müzikteki paralel:</b> Tema ve varyasyon formu. Beethoven, Mozart ve Brahms aynı temayı '
        'yorumladı — her biri farklı bir eser ortaya koydu. Tema aynı, yorum farklı. '
        '3. derste öğrencilerden istenen şey budur.', S_BD))

    # 5.2 Analoji
    e.append(Paragraph('5.2 Analoji Nedir ve Neden Güçlüdür?', S_H2))
    e.append(Paragraph(
        'Analoji, iki farklı alan arasında benzerlik kurarak bilinenden bilinmeyene geçiş '
        'yapmaktır. Beyin yeni bilgiyi bildiği kavramsal çerçevelere bağlayarak öğrenir; '
        'analoji bu köprünün ta kendisidir.', S_BD))
    e.append(Paragraph('Tasarımda analoji iki biçimde ortaya çıkar:', S_H3))
    e.append(Paragraph(
        '<b>Biyomimikri:</b> Doğadaki bir formdan veya süreçten ilham alarak tasarlama. '
        'Velcro → köpek tüyüne yapışan tohum. Shinkansen → dalgıç kuşu gagası.', S_IND))
    e.append(Paragraph(
        '<b>Metafor tasarımı:</b> Soyut bir kavramı somut bir forma çevirme. '
        '"Güçlü" bir şampuanı kaplayabileceği su miktarını gösteren grafikle sunmak '
        'bir metafor tasarımıdır.', S_IND))
    e.append(Paragraph(
        '<b>4. derste ne yapıyoruz?</b> Dörtlü analoji çalışması (sözel, görsel, soyut, nesnel) '
        'aslında tek bir konuyu dört farklı zihinsel pencereden görmelerini sağlar. Her pencere '
        'farklı bir düşünme modu gerektirir. Bir öğrencinin güçlü olduğu mod diğerinden farklı '
        'olabilir — bu çalışma bu farklılığı değerli kılar.', S_BD))

    return e


# ============================================================
# BÖLÜM 6 — YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI
# ============================================================

def bolum6():
    e = []
    e += bolum_baslik(6, 'YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI')
    e.append(Paragraph(
        'Aşağıdaki yanlış anlamalar öğrencilerin büyük çoğunluğunda görülür. Bunları ders başında '
        '"tuzak soru" olarak kullanabilir ya da akışta düzeltme fırsatı çıktığında '
        'hazırlıklı olabilirsiniz.', S_BD))

    yanlis = [
        ('"Tasarım elemanları sadece resim veya grafik işler için"',
         'Her tasarlanmış nesne bu elemanları içerir. Bir sandalye (biçim, doku, renk), müzik aleti '
         '(biçim, orantı), köprü (çizgi, denge, hareket). Eleman bir sınıflandırma aracıdır.'),
        ('"İlkeler kurallardır — bunlara uymak zorundayım"',
         'İlkeler kural değil, araçtır. Bilinçli kırabilirsiniz. "Neden bu ilkeyi kırdım, hangi '
         'etkiyi elde ettim?" sorusuna cevap verebiliyorsanız bu da tasarım kararıdır.'),
        ('"Denge = simetri"',
         'Simetri bir tür dengedir ama tek tür değil. Asimetrik denge genellikle daha ilgi çekicidir. '
         'Çoğu çağdaş tasarım asimetrik dengede kurulur.'),
        ('"Siyah-beyaz çalışmak güzellik yokluğu"',
         'Ansel Adams\'ın siyah-beyaz fotoğrafları renksiz ama güçlüdür. Güzellik renk kombinasyonundan '
         'değil, elemanlar ve ilkelerin ustalıklı kullanımından gelir.'),
        ('"Geleneksel Türk sanatı modası geçmiş"',
         '"Neo-ethnic" trendi — kültürel miras motiflerinin çağdaş tasarıma entegrasyonu — '
         '21. yüzyılın en çok aranan tasarım trendlerinden biri. Dünyanın önde gelen moda evleri '
         'Türk kilim motiflerini koleksiyonlarında kullandı.'),
        ('"Yeniden yorumlama kopyalamaktır"',
         'Bir evi yeniden dekore etmek onu kopyalamak değildir. Bağlamı koruyarak özgün bir katkıda '
         'bulunmak yorumlamaktır; kopyalama birebir taklit etmektir.'),
        ('"Analoji sadece sözel bir eştir — benzetmedir"',
         'Analoji zihinsel bir araçtır, dil biçimi değil. Görsel analoji çizmek, sesle analoji '
         'kurmak, dokunmayla analoji hissetmek mümkündür. 4. derste dört farklı analoji '
         'biçimini deneyimleyecekler.'),
        ('"Negatif alan boş alandır, israftır"',
         'Apple\'ın ürün fotoğraflarındaki geniş beyaz boşluklar "israf" değil, bilinçli bir '
         'mesajdır. Fazla bilgi ve görsel içeren tasarımlar bunaltıcı hissettirir; negatif alan '
         'dinginlik ve önem mesajı verir.'),
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
        'Somut hikayeler soyut kavramları kalıcı hale getirir. Aşağıdaki anlatılar ilgili '
        'kavramlara bağlanarak ders akışına doğal biçimde yerleştirilebilir.', S_BD))

    e.append(hikaye(
        'Tasarımın Görünmez Dili — FedEx Okun Gizemi',
        ['1994 yılında Landor Associates firması FedEx\'in yeni logosunu tasarladı. Tasarımcı '
         'Lindon Leader iki harfin arasına, hiç beklenmedik bir yere bir şey sakladı: E ve x '
         'harfleri arasında mükemmel bir ok.',
         'Bu ok tesadüf değildi. Leader bunu kasıtlı yerleştirdi: ilerleme, hız, hedefe ulaşma. '
         'Ama oka dikkat çekmedi — bilinçdışında işlemesi için.',
         'Bugün bu logo tasarım okullarında "negatif alan kullanımı"nın en iyi örneği olarak '
         'gösterilir. Görünce bir daha görmezden gelemezsiniz.'],
        'Negatif alan (mekân elemanı) ve tasarımın bilinçdışı iletişim boyutu konuşmalarına.'))

    e.append(hikaye(
        'Renk Neden Satın Alımı Etkiler? — McDonald\'s\'ın Kırmızı-Sarı Tercihi',
        ['1953\'te Richard ve Maurice McDonald kardeşlerin restoranı. Renk seçimini sanatçı '
         'Jim Schindler yaptı: kırmızı ve sarı kombinasyonu.',
         'Araştırmalar ondan yıllar sonra geldi: Kırmızı fizyolojik uyarılmayı artırır — kalp '
         'atışı hızlanır, iştah artar. Sarı neşe ve enerjiyi çağrıştırır. İkisi birlikte '
         '"hızlı ye, eğlenceli hisset" mesajını destekler.',
         'Bugün kırmızı-sarı kombinasyonu fast food sektöründe o kadar yerleşti ki rakiplerin '
         'büyük çoğunluğu aynı renk paletini kullanıyor.'],
        'Renk psikolojisi ve renk-duygu ilişkisi konuşmalarına.'))

    e.append(hikaye(
        'Kazanmak İçin Kaybetmek — Altın Oran Yanılgısı',
        ['1876\'da Gustav Fechner 10.000 kişiye farklı boyutlarda dikdörtgenler gösterdi ve '
         '"en güzel hangisi?" diye sordu. Katılımcıların yüzde altmışından fazlası 1:1.618 '
         'oranındaki dikdörtgeni seçti — altın oran.',
         'Bu araştırma altın oranın estetik üstünlüğünü "kanıtladı" sanıldı. Yüzyıl boyunca '
         'grafik tasarım kitaplarına girdi.',
         'Ama 1990\'lardan itibaren araştırmacılar Fechner\'in yöntemini sorguladı. 2015\'te '
         'büyük çaplı bir çalışmada insanların altın oranı anlamlı biçimde tercih etmediği '
         'gösterildi. Altın oran güçlü bir araçtır — ama "evrensel güzelliğin kodu" değildir.'],
        'Oran-orantı ilkesi ve "tasarımda evrensel kural var mı?" tartışmasına.'))

    e.append(hikaye(
        'Görsel Dilin Sessiz Gücü — Sydney Opera House',
        ['1957 yılında Danimarkalı genç mimar Jorn Utzon\'un projesi 233 proje arasından seçildi. '
         'Bina yaşayan bir sanat eseri gibiydi — birbirinin üzerine binen beyaz kabuklar, sanki '
         'yelkenler ya da turunçgil kabukları gibi. Teknik olarak "imkansız" sayılıyordu.',
         'İnşaat 14 yıl sürdü. Utzon yöneticilerle anlaşamayınca görevden alındı. 2003\'te '
         'mimarlığın Nobel\'i olan Pritzker Ödülü\'nü aldı. Ama o güne kadar kendi tasarladığı '
         'binaya hiç gitmedi.'],
        'Biçim elemanı ve "tasarım vizyonu ile uygulama gerçekliği" arasındaki gerilime.'))

    e.append(hikaye(
        'Hata Kullanıcıda Değil Tasarımda — Norman Kapısı',
        ['1988\'de bilişsel bilimci Don Norman "The Design of Everyday Things" kitabını yayımladı.',
         'Norman bir problemi tanımladı: Kapılar. Ötmesi gereken kapıyı itmek, itilmesi gereken '
         'kapıyı ötemek — bu evrensel bir deneyimdir. Hata kullanıcıda değil, tasarımcıdadır.',
         'İyi tasarım kullanım kılavuzuna ihtiyaç bırakmaz. Ürün kendi kullanımını anlatır. '
         'Buna "affordance" (karşılayıcılık) denir.',
         '"Norman Kapısı": Nasıl kullanılacağını sezgisel olarak aktarmayan, kullanıcıyı '
         'yanıltan her tasarım.'],
        '"Tasarım problemi çözümdür" fikrine. "Okulda Norman Kapısı var mı?" sorusu güzel '
        'bir gözlem etkinliği açar.'))

    return e


# ============================================================
# BÖLÜM 8 — ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR')
    e.append(Paragraph(
        'Bazı sorular anında yanıt gerektirmez. "Harika soru — düşünmem lazım" ya da "Bu konuyu '
        'ileride daha ayrıntılı ele alacağız" demek tamamen uygundur. Aşağıdaki yanıtlar bir '
        'başlangıç noktasıdır.', S_BD))

    qas = [
        ('"Tasarım elemanları listesi kimler tarafından belirlendi? Neden tam sekiz?"',
         'Bu liste 20. yüzyıl başında Bauhaus ve başka sanat okullarında öğretimde kullanılan '
         'kategorilerden gelişti. "Sekiz eleman" değişmez bir doğa yasası değil, tasarımı '
         'öğretmeye ve analiz etmeye yarayan bir çerçevedir. Bazı kaynaklar farklı sayıda eleman '
         'sayar — önemli olan kavramları anlamak, sayıyı ezberlemek değil.'),
        ('"Tamamlayıcı renkler güzel görünür diyorsunuz, ama ben güzel bulmuyorum."',
         'Bu dürüst ve önemli bir itiraz. Renk algısı kısmen kültürel, kısmen bireyseldir. '
         '"Tamamlayıcı renkler canlı kontrast yaratır" demek daha doğru olur — "güzel" diye '
         'nitelendirmek kişiden kişiye değişir. Tasarımda "güzel" değil, "işlevi için etkili" '
         'sorusu daha verimlidir. Bir uyarı işareti kırmızı-yeşil olabilir ve güzel olmak zorunda '
         'değildir — dikkat çekmesi yeterlidir.'),
        ('"Yeniden yorumlama ile kopya arasındaki sınırı kim belirler?"',
         'Hukuki açıdan telif hakkı hukuku belirler; ama sanat dünyasında bu çok tartışmalıdır. '
         'Genel kabul gören kriter şudur: Orijinalden "önemli ölçüde dönüştürme" yapıldıysa '
         'yorum, birebir taklit varsa kopya. Ama "önemli ölçüde" kelimesi mahkemelerde hâlâ '
         'tartışılmaktadır. Bu soruya kesin yanıt yok — tartışılmaya devam eden bir sınır.'),
        ('"Türk geleneksel sanatında tasarım ilkeleri bilinçli mi uygulanıyordu?"',
         'Büyük ihtimalle ikisi de: Hem bilinçli kural hem sezgisel gelenek. Ustalar çıraklarına '
         '"denge böyle olur, ritim böyle kurulur" diye öğretti — bu bilinçli uygulama. Ama '
         '"Neden?" sorusuna "Güzel göründüğü için" ya da "Böyle yapılır" cevabı geliyorsa bu '
         'sezgisel bir uygulama. Günümüzde o sezgileri analiz ederek adlandırıyoruz. Kural sonradan '
         'gözlemlendi, önce yaratım vardı.'),
        ('"Bir tasarım tüm ilkeleri aynı anda kullanmak zorunda mı?"',
         'Hayır. Hatta tüm ilkeleri eşit ağırlıkta uygulamak çoğu zaman karmaşa yaratır. İyi '
         'tasarım genellikle birkaç ilkeyi öne çıkarır, diğerlerini arka planda tutar. Önemli '
         'olan hangisini neden seçtiğinizi bilmektir. Bir itiraz afişi maksimum zıtlık ve vurgu '
         'ister; bir bebek odası müdahalesi minimum zıtlık ve maksimum birlik ister.'),
        ('"Altın oran evrensel değilse sanat eserleri neden hâlâ güzel görünüyor?"',
         'Çok iyi soru. Altın oranı "güzellik yaratan özel formül" değil, "iyi bir orantı '
         'sistemi" olarak düşünün. Birçok farklı oran sistemi işe yarar. Güzellik algısı büyük '
         'ölçüde tanıdıklık, kültürel bağlam ve bireysel deneyimle şekillenir. Parthenon güzel '
         'çünkü altın oran içeriyor değil, çünkü orantılar tutarlı, elemanlar dengeli ve yapı '
         'binlerce yıl boyunca "güzel mimari" olarak gösterildi. Tekrar ve kültürel anlam da '
         'güzellik algısı yaratır.'),
    ]

    for soru, cevap in qas:
        e.append(KeepTogether([
            Paragraph(soru, S_QQ),
            Paragraph(cevap, S_QA),
        ]))

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
        title='2. Unite - Ogretmen Hazirlik Rehberi',
        author='Teknoloji ve Tasarim Ogretim Programi',
    )
    doc.unite_info = UI
    doc.doc_title  = 'Unite Icerigi Hazirlik Materyali'

    story = []

    story += bolum1()
    story += bolum2()
    story += bolum3()
    story += bolum4()
    story += bolum5()
    story += bolum6()
    story += bolum7()
    story += bolum8()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print('OK  U2_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
