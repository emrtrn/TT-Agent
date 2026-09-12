# -*- coding: utf-8 -*-
"""
1. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit1/U1_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite1_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit1')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U1_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '1. Unite - Teknoloji ve Tasarim Ogreniyorum'
CW    = A4[0] - 4 * cm   # 17 cm içerik genişliği

# ============================================================
# STİLLER
# ============================================================

S_H1   = ParagraphStyle('h1',  fontName='TR-Bold',    fontSize=13, textColor=COLOR_PRIMARY,
                          leading=17, spaceBefore=16, spaceAfter=6)
S_H2   = ParagraphStyle('h2',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_SECONDARY,
                          leading=14, spaceBefore=10, spaceAfter=4)
S_H3   = ParagraphStyle('h3',  fontName='TR-Bold',    fontSize=10, textColor=COLOR_ACCENT,
                          leading=13, spaceBefore=7, spaceAfter=3)
S_BD   = ParagraphStyle('bd',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                          leading=13, spaceAfter=4, alignment=TA_JUSTIFY)
S_IND  = ParagraphStyle('ind', fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                          leading=13, spaceAfter=3, alignment=TA_JUSTIFY, leftIndent=12)
S_BUL  = ParagraphStyle('bul', fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                          leading=12, spaceAfter=2, leftIndent=16, bulletIndent=4)
S_NOT  = ParagraphStyle('not', fontName='TR-Italic',  fontSize=8.5, textColor=COLOR_MUTED,
                          leading=12, spaceAfter=4, leftIndent=8)
# bilgi kutusu
S_BH   = ParagraphStyle('bh',  fontName='TR-Bold',    fontSize=9,  textColor=white, leading=12)
S_BB   = ParagraphStyle('bb',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                          leading=13, alignment=TA_JUSTIFY)
# hikaye kutusu
S_SH   = ParagraphStyle('sh',  fontName='TR-Bold',    fontSize=9,  textColor=white, leading=12)
S_SB   = ParagraphStyle('sb',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                          leading=13, alignment=TA_JUSTIFY)
S_SC   = ParagraphStyle('sc',  fontName='TR-Italic',  fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=12)
# soru-cevap
S_QQ   = ParagraphStyle('qq',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY,
                          leading=13, spaceBefore=6, spaceAfter=2)
S_QA   = ParagraphStyle('qa',  fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,
                          leading=13, spaceAfter=5, alignment=TA_JUSTIFY, leftIndent=10)
# yanlis anlama
S_YAN  = ParagraphStyle('yan', fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=12, spaceAfter=1)
S_DUZ  = ParagraphStyle('duz', fontName='TR-Regular', fontSize=8.5, textColor=COLOR_TEXT,
                          leading=12, spaceAfter=5, leftIndent=6)
# tablo içi
S_TH   = ParagraphStyle('th',  fontName='TR-Bold',    fontSize=8.5, textColor=white,
                          leading=12, alignment=TA_CENTER)
S_TC   = ParagraphStyle('tc',  fontName='TR-Regular', fontSize=8.5, textColor=COLOR_TEXT,
                          leading=12, alignment=TA_LEFT)
S_TCB  = ParagraphStyle('tcb', fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_TEXT,
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
    """Turuncu başlık çubuğu + açık turuncu arka planlı bilgi kutusu."""
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
    """Koyu turuncu başlık + gri arka plan hikaye/anekdot kutusu."""
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

    # 1.1
    e.append(Paragraph('1.1 Karışan Üçlü: Buluş · İcat · Keşif', S_H2))
    e.append(Paragraph(
        'Bu üç kavram Türkçede sıkça birbirinin yerine kullanılır. Karışıklığın temel nedeni, '
        '"bulmak" fiilinin üçünü de kapsamasıdır. Ancak bunlar birbirinden farklı süreçleri '
        'anlatır ve öğrencilerin bu farkı içselleştirmesi ünitenin temel hedeflerinden biridir.',
        S_BD))

    # Özet karşılaştırma tablosu
    tablo_data = [
        [Paragraph('BULUŞ', S_TH), Paragraph('İCAT', S_TH), Paragraph('KEŞİF', S_TH)],
        [Paragraph('Soyut fikir, ilke, yöntem', S_TC),
         Paragraph('Somut, daha önce olmayan ürün', S_TC),
         Paragraph('Zaten var olanı ilk fark etme', S_TC)],
        [Paragraph('Newton: Hareket Yasaları\nArşimet: Kaldırma Kuvveti', S_TC),
         Paragraph('Bell: Telefon\nEdison: Ampul', S_TC),
         Paragraph('Kolomb: Amerika\nWatson-Crick: DNA yapısı', S_TC)],
        [Paragraph('Patent alınamaz', S_TC),
         Paragraph('Patent alınabilir', S_TC),
         Paragraph('Patent alınamaz', S_TC)],
    ]
    tablo = Table(tablo_data, colWidths=[CW/3, CW/3, CW/3])
    tablo.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('BACKGROUND',    (0, 1), (-1, -1), COLOR_VERY_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, COLOR_VERY_LIGHT]),
        ('GRID',          (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    e.append(KeepTogether([tablo, vsp(0.15)]))

    e.append(Paragraph('<b>Keşif:</b> Zaten var olan ama bilinmeyen bir şeyin fark edilmesi. '
        'Kolomb, Amerika\'yı icat etmedi — orada zaten insanlar vardı. Keşfetti. DNA\'nın çift '
        'sarmal yapısı, Pasifik Okyanusu, yerçekimi sabiti hepsi keşiftir. Keşif "doğanın '
        'sırlarını açmak"tır; siz aramadıysanız zaten oradaydı.', S_BD))
    e.append(Paragraph('<b>Buluş:</b> Daha önce bilinmeyen bir fikrin, ilkenin veya yasanın '
        'ortaya konması. Arşimet\'in kaldırma kuvveti, Newton\'ın hareket yasaları. Bunlar '
        'soyuttur — fiziksel olarak üretilmez, zihinde şekillenir. Türkçede "buluş" sözcüğü '
        'hem bu felsefi anlamda hem de patent dilinde kullanılır; bu karışıklığa dikkat.', S_BD))
    e.append(Paragraph('<b>İcat:</b> Daha önce var olmayan somut bir ürünün, cihazın veya '
        'sürecin yaratılması. Patent alınabilir çünkü gerçek dünyada yenidir. Önemli bağlantı: '
        'İcatların çoğu buluşların üstüne inşa edilir — telefon icat edilmeden önce '
        'elektromanyetik dalgalar Maxwell tarafından "bulunmuştu".', S_BD))

    e.append(bilgi_kutusu(
        'Sinifta Kullanilabilecek Test Sorusu',
        ['"Benden önce var miydi?" sorusunu tahtaya yazin.',
         'Evet   →   Kesif',
         'Hayir + somut urun   →   Icat',
         'Hayir + soyut ilke/fikir   →   Bulus']))

    e.append(hikaye(
        'DNA Kesfinin Gizli Kahramani: Rosalind Franklin',
        ['Rosalind Franklin, 1952\'de DNA\'nin X-isini kristalografisi goruntusunu cekti. '
         'Watson ve Crick bu goruntüyu Franklin\'in haberi olmadan kullandı ve 1953\'te '
         'yapıyı yayımladı.',
         'Nobel Ödülü 1962\'de Watson, Crick ve Wilkins\'e verildi. Franklin ödülü almak '
         'için yaşayamadı — 1958\'de kanserden hayatını kaybetti.',
         'Keşif mi, buluş mu? DNA zaten vardı → keşif. Ama yapıyı modellemek için '
         'matematik ve fizik kullandılar → buluş öğeleri de var. Sınıfta tartışılabilecek '
         'mükemmel bir "sınır sorusu".'],
        'Buluş/İcat/Keşif ayrımı tartışmasına; bilim etiği konusuna.'))

    # 1.2
    e.append(Paragraph('1.2 Bilim · Teknik · Teknoloji İlişkisi', S_H2))
    e.append(Paragraph(
        '"Teknoloji = bilgisayar" yanlışlığı son 40 yılda dijital araçların teknoloji '
        'haberlerine hâkim olmasından kaynaklanır. Oysa kaşık, tekerlek, bıçak da birer '
        'teknolojidir. "Teknoloji" sözcüğü Yunancada <i>techne</i> (zanaat) ve <i>logos</i> '
        '(bilgi) kökünden gelir.', S_BD))

    e.append(bilgi_kutusu(
        'Bilim + Teknik = Teknoloji',
        ['BİLİM: "Neden" ve "ne" sorusunu sorar. Sistematik gözlem, deney ve çıkarımla '
         'evrenin anlaşılması. Yanıtlar evrenseldir — dünyanın her yerinde aynı deneyi '
         'yapsan aynı sonucu alırsın.',
         'TEKNİK: "Nasıl" sorusunu sorar. Belirli bir işi yapmanın yolu, ustalığı. '
         'Ustadan çırağa deneyimle aktarılır; tam olarak kelimeye dökülmesi zordur '
         '(örtük bilgi / tacit knowledge).',
         'TEKNOLOJİ: İkisini birleştirir ve insan ihtiyacını karşılar. Birini kaldırın '
         'sistem çöker. Örnek: Elektrik teorisi (bilim) + tel çekme yöntemi (teknik) → '
         'Elektrik şebekesi (teknoloji).']))

    # 1.3
    e.append(Paragraph('1.3 Tasarım Kavramının Derinliği', S_H2))
    e.append(Paragraph(
        'Latince <i>designare</i> kökünden gelir: işaretlemek, planlamak, ayırt etmek. '
        'İngilizce "design" hem fiil hem isim olarak kullanılır; Türkçede bu ayrım '
        'fiil-isim olarak netleştirilmiştir — bu pedagojik bir avantajdır.', S_BD))
    e.append(Paragraph(
        '<b>İyi tasarım neden fark edilmez?</b> Don Norman\'ın "görünmez tasarım" '
        '(invisible design) kavramı: En iyi tasarımlar kullanıcının aklına bile gelmez, '
        'her şey kendiliğinden doğru çalışıyormuş gibi hissettirirler. Tersine, kötü '
        'tasarım hep kendini belli eder. Kapıda itmek mi çekmek mi bilemiyorsanız — bu '
        'bir "Norman Kapısı"dır; tasarımcı kullanım biçimini açıkça iletmeyi '
        'başaramamıştır.', S_BD))
    e.append(Paragraph(
        '<b>Sınıfta sorulabilecek soru:</b> "Bugün sabahtan beri kafanızı karıştıran '
        'bir nesne ya da yer oldu mu?" Neredeyse her yanıt bir tasarım sorununa işaret '
        'eder.', S_NOT))
    e.append(bilgi_kutusu(
        'İyi Tasarımın Üç Dengesi',
        ['İşlevsellik: Ürün amacını gerçekleştiriyor mu?',
         'Estetik: Görsel ve duyusal olarak hoş mu?',
         'Sürdürülebilirlik: Uzun ömürlü mü, çevreye etkisi nedir?',
         'Bu üçünden birini aşırı öne çıkarmak sorun yaratır. Yalnızca estetik → '
         'pahalı ama işlevsiz. Yalnızca işlevsellik → kullanılmaz hale gelir. '
         'Yalnızca sürdürülebilirlik → ticari olarak hayatta kalamaz.']))
    return e


# ============================================================
# BÖLÜM 2 — TASARIMIN ÜÇ DÜNYASI
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TASARIMIN ÜÇ DÜNYASI')

    # 2.1 Endüstriyel
    e.append(Paragraph('2.1 Endüstriyel Tasarım', S_H2))
    e.append(Paragraph(
        'Endüstriyel tasarım mesleği 20. yüzyılın başında, seri üretimle birlikte ortaya '
        'çıktı. Öncesinde her nesne bir usta tarafından tek tek yapılırdı; usta hem '
        'tasarımcıydı hem yapımcı. Fabrikalar bu ikisini ayırdı ve tasarımcılık bağımsız '
        'bir meslek oldu.', S_BD))
    e.append(Paragraph(
        '1919\'da kurulan <b>Bauhaus</b> okulu bu dönüşümün simgesidir. Sanatçılar ve '
        'mühendisler aynı çatı altında çalıştı. "Biçim işlevi izler" (Form follows function) '
        'ilkesi bu dönemden kalır: Nesnenin görünüşü ne yapacağı tarafından '
        'belirlenmelidir.', S_BD))

    e.append(Paragraph('Önemli Dünya Örnekleri', S_H3))
    ornekler = [
        ('<b>Volkswagen Beetle (1938):</b>', 'Hitler\'in "Halk Arabası" projesi olarak başladı, ama zamanla özgürlük ve gençliğin simgesi oldu. Tasarım o kadar sade ve işlevseldi ki 65 yıl üretildi.'),
        ('<b>Herman Miller Aeron (1994):</b>', 'Ergonomik araştırmadan doğdu. Tasarımcılar Stumpf ve Chadwick, insan vücudunun nasıl oturduğunu yıllarca inceledi. Başta "çirkin" bulundu; müşteri odak grupları beğenmedi. Ama ortopedistler ve ergonomi uzmanları sipariş verdi. Bugün ofis ergonomisinin referans noktası.'),
        ('<b>iPhone (2007):</b>', 'Dokunmatik ekran Apple\'ın icadı değildi. Jobs\'ın yaptığı şey: Çok kötü tasarlanmış cep telefonu deneyimini baştan düşünmek. Nokia ve Blackberry güldü. İki yıl sonra Nokia CEO\'su "Bu bir hataydı" dedi.'),
        ('<b>Ford Edsel (1957):</b>', 'Tarihin en büyük başarısızlıklarından biri. Müşteri araştırmasına milyonlar harcandı ama sonuçlar yanlış yorumlandı. Radyatör ızgarası "tuvalet çerçevesi" lakabını kazandı. 3 yılda 110.000 adet satılabildi, 250 milyon dolar zarar edildi.'),
    ]
    for bold, aciklama in ornekler:
        e.append(Paragraph(f'{bold} {aciklama}', S_IND))

    e.append(Paragraph('Türkiye\'den Örnekler', S_H3))
    e.append(Paragraph(
        '<b>Anadol (1966):</b> Türkiye\'nin ilk yerli otomobili. Vücut panelleri camfiberden '
        'yapıldı çünkü çelik presleme altyapısı yoktu. Bugünkü standartlara göre yeterli '
        'değildi ama tarihi önemi büyüktür.', S_IND))
    e.append(Paragraph(
        '<b>TOGG T10X (2023):</b> Tasarım Pininfarina\'dan (Ferrari ve Maserati\'nin '
        'tasarımcısı) alındı, mühendislik ve üretim tamamen yerli. Gemlik\'teki fabrika '
        'Endüstri 4.0 anlayışıyla kuruldu.', S_IND))

    # 2.2 Grafik
    e.append(Paragraph('2.2 Grafik Tasarım', S_H2))
    e.append(Paragraph(
        'Grafik tasarımın başlangıcı tartışmalı olsa da <b>Gutenberg\'in matbaası (1450)</b> '
        'kitlesel görsel iletişimin ilk büyük sıçramasıdır. El yazmalı kitaplar artık standart '
        'sayfalara, başlıklara ve sütunlara kavuştu. "Grafik tasarım" terimi 1922\'de William '
        'Addison Dwiggins tarafından kullanıldı.', S_BD))

    e.append(Paragraph('İlginç Gerçekler', S_H3))
    gercekler = [
        'FedEx Logosu: E ve x harflerinin arasında gizlenmiş bir ok vardır — ileriye doğru hareket ve hız. Çoğu insan yıllarca fark etmez; fark ettikten sonra görmezden gelemez.',
        'Amazon Logosu: Ok A\'dan Z\'ye uzanır (her şeyi satarlar) ve aynı zamanda bir gülümsemedir.',
        'Emoji\'nin Doğuşu: 1999\'da Japon mühendis Shigetaka Kurita 176 emojiyi tasarladı, her biri 12×12 pikseldi. Bugün Unicode 4000\'den fazla emoji tanımlıyor.',
        'Saul Bass: 1950-60\'larda Hitchcock filmlerinin açılış sekanslarını tasarladı (Vertigo, Psycho). Bir film başlamadan önce seyircinin ruh halini belirlemek — grafik tasarımın sinemaya katkısı budur.',
    ]
    for g in gercekler:
        e.append(Paragraph(f'• {g}', S_BUL))

    e.append(Paragraph('Türkiye\'den Örnekler', S_H3))
    e.append(Paragraph(
        '<b>Türk Hava Yolları Marka Kimliği:</b> Kartal ve kırmızı-beyaz renk kombinasyonu '
        'küresel ölçekte tanınır hale geldi. Uçak gövde tasarımı, koltuk düzeni, yiyecek '
        'ambalajı — bunların tümü bir grafik tasarım sisteminin parçasıdır.', S_IND))
    e.append(Paragraph(
        '<b>Türk Lirası Sembolü (₺):</b> 2011\'de açılan ulusal yarışmada Tülay Lale\'nin '
        'tasarımı seçildi. İki paralel çizgi içeren T harfi: T = Türk, çizgiler = istikrar '
        've güç. Tasarım 2012\'den itibaren uluslararası standartlara girdi.', S_IND))

    # 2.3 Mimari
    e.append(Paragraph('2.3 Mimari Tasarım', S_H2))
    e.append(Paragraph(
        'Roma dönemi mimar Vitruvius\'un üçlüsü 2000 yıl sonra hâlâ mimarinin çerçevesidir: '
        '<b>Firmitas</b> (Sağlamlık) + <b>Utilitas</b> (Kullanışlılık) + <b>Venustas</b> '
        '(Güzellik). Gotik katedraller 12. yüzyılda statik hesap ve bilgisayar olmadan '
        'inşa edildi — tasarımcılar küçük maketler yaparak yükleri test etti.', S_BD))

    e.append(Paragraph('Dünyadaki İlginç Örnekler', S_H3))
    dunya = [
        '<b>Eiffel Kulesi (1889):</b> Tasarlanırken 300 sanatçı ve aydın "metal bir köstebek" diye imza kampanyası başlattı. Gustave Eiffel dinlemedi. 20 yıl sonra yıkılması planlanıyordu ama radyo anteni olarak kullanılmaya başlandı ve kaldı. Bugün dünyanın en çok ziyaret edilen yapısı.',
        '<b>Guggenheim Bilbao (1997):</b> Frank Gehry\'nin kıvrık, titanyum kaplı yapısı tek başına İspanya\'nın küçük bir sanayi şehrini küresel kültür merkezine dönüştürdü. Bu olay "Bilbao Etkisi" olarak literatüre girdi: İyi mimari tasarım bir kenti ekonomik olarak dönüştürebilir.',
        '<b>Sydney Opera House (1973):</b> Jorn Utzon yarışmayı kazandı ama inşaat sürecindeki anlaşmazlıklar sonucu görevden alındı. Bina tamamlanınca görmeye gitmedi, vefatına kadar da gitmedi.',
    ]
    for d in dunya:
        e.append(Paragraph(f'• {d}', S_BUL))

    e.append(Paragraph('Türkiye\'den Örnekler', S_H3))
    e.append(Paragraph(
        '<b>Selimiye Camii (Mimar Sinan, 1574):</b> Sinan hayatının en büyük eserini '
        '80 yaşında tamamladı. Kubbe çapı 31.25 metredir (Ayasofya: 31.87 m). Sinan\'ın '
        'gerçek başarısı boyuttan çok, 8 sütunla taşınan bu kubbe altında tamamen açık '
        'bir iç mekân yaratmasıdır. Ayasofya\'nın kendi taşıyıcı sütunları iç mekânı '
        'böler; Selimiye\'de tek bir nefes vardır. 2011\'de UNESCO Dünya Mirası '
        'Listesi\'ne alındı.', S_IND))
    e.append(Paragraph(
        '<b>Biyografik not:</b> Sinan, devşirme kökenli Rum ya da Ermeni olduğu düşünülmektedir '
        '(tartışmalı). 50 yılı aşkın süre Osmanlı baş mimarı olarak 477\'den fazla yapı '
        'tasarladı. 90 yıl yaşadı ve son binasını 80\'li yaşlarında tamamladı.', S_IND))
    e.append(Paragraph(
        '<b>Galata Kulesi (1348):</b> Cenevizliler tarafından inşa edildi, 9 asrı aşkın '
        'süredir İstanbul siluetinin parçası. Sınıfta güzel bir soru: "Bu yapı bugün de '
        'kullanılıyor mu? Neden hâlâ ayakta?" — dayanıklılık ve adaptasyon tartışması '
        'açar.', S_IND))
    return e


# ============================================================
# BÖLÜM 3 — ENDÜSTRİ DEVRİMLERİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'ENDÜSTRİ DEVRİMLERİ')

    e.append(Paragraph(
        '"Devrim" sözcüğü önemlidir: Bu değişimler kademeli değil, kopuştur. Her devrim '
        'aynı anda üretim biçimini, enerji kaynağını ve toplumsal yapıyı dönüştürür.', S_BD))

    # Özet tablo
    dev_data = [
        [Paragraph('Dönem', S_TH), Paragraph('Yıl', S_TH),
         Paragraph('Tetikleyici', S_TH), Paragraph('Özet Etki', S_TH)],
        [Paragraph('Endüstri 1.0', S_TC), Paragraph('1784', S_TC),
         Paragraph('Buharlı makine', S_TC), Paragraph('Tarım → Sanayi toplumu', S_TC)],
        [Paragraph('Endüstri 2.0', S_TC), Paragraph('1870', S_TC),
         Paragraph('Elektrik + seri üretim', S_TC), Paragraph('Kitlesel fabrikasyon', S_TC)],
        [Paragraph('Endüstri 3.0', S_TC), Paragraph('1970', S_TC),
         Paragraph('Mikroçip + bilgisayar', S_TC), Paragraph('Otomasyon, yazılım', S_TC)],
        [Paragraph('Endüstri 4.0', S_TC), Paragraph('2011', S_TC),
         Paragraph('IoT, YZ, bulut', S_TC), Paragraph('Akıllı fabrikalar', S_TC)],
        [Paragraph('Endüstri 5.0', S_TC), Paragraph('~Günümüz', S_TC),
         Paragraph('İnsan-makine iş birliği', S_TC), Paragraph('Sürdürülebilir + insan odaklı', S_TC)],
    ]
    col_w = [CW*0.22, CW*0.13, CW*0.30, CW*0.35]
    dev_t = Table(dev_data, colWidths=col_w)
    dev_t.setStyle(TableStyle([
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
    e.append(KeepTogether([dev_t, vsp(0.2)]))

    e.append(Paragraph('Birinci Sanayi Devrimi (1784)', S_H3))
    e.append(Paragraph(
        'Watt 1769\'da Newcomen\'ın pompasını çok daha verimli hale getirdi. İngiltere\'de '
        'tarım toplumu 50 yıl içinde sanayi toplumuna dönüştü. <b>Luddist hareket:</b> '
        'İngiliz tekstil işçileri makineleri kırdı — işlerini değil, haklarını savunuyorlardı. '
        '"Luddist" terimi bugün teknolojiyi reddeden kişiler için kullanılır ama bu '
        'yanlış bir sadeleştirmedir.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Osmanlı bu dönemi kaçırdı. Buharlı gemiler ve demir '
        'yolları çok daha geç ve çoğunlukla Avrupalı şirketler aracılığıyla geldi. '
        'Bu gecikme 19. yüzyıl Osmanlı ekonomisinin yapısal sorunlarından biridir.', S_NOT))

    e.append(Paragraph('İkinci Sanayi Devrimi (1870)', S_H3))
    e.append(Paragraph(
        'Ford\'un bant sistemi (1913): Model T\'nin üretim süresi 12 saatten 93 dakikaya '
        'indi, fiyat 825 dolardan 290 dolara düştü. Ford aynı zamanda işçilerine dönemin '
        'iki katı ücret ödedi — kendi arabalarını alabilsinler diye.', S_BD))
    e.append(Paragraph(
        '<b>Tesla-Edison savaşı:</b> Edison DC (doğru akım) sistemini savundu. Nikola Tesla '
        'AC (alternatif akım) sistemini geliştirdi. Edison, AC\'nin tehlikeli olduğunu '
        'kanıtlamak için halka açık gösterilerde filler dahil büyük hayvanları elektrikle '
        'öldürttü. Tarihte kalmış bir propaganda kampanyası. Kazanan AC oldu — bugün '
        'evlerimizdeki elektrik Tesla\'nın sistemidir.', S_BD))

    e.append(Paragraph('Üçüncü Sanayi Devrimi (1970)', S_H3))
    e.append(Paragraph(
        '1971\'de Intel\'in ilk mikroçipinde (4004) 2300 transistör vardı. Bugünkü modern '
        'bir çipte 100 milyarı aşkın transistör bulunur. <b>Moore Yasası:</b> Transistör '
        'sayısı yaklaşık her iki yılda bir iki katına çıkar — bu yasa 50 yıldır tuttu. '
        'İnternet\'in kökeni: ARPANET, 1969\'da ABD Savunma Bakanlığı tarafından nükleer '
        'savaş durumunda kesintisiz iletişim için başlatıldı.', S_BD))

    e.append(Paragraph('Endüstri 4.0 (2011)', S_H3))
    e.append(Paragraph(
        'Terim ilk kez 2011 Hannover Fuarı\'nda Alman hükümeti tarafından kullanıldı — '
        'Almanya\'nın üretim üstünlüğünü korumak için yeni teknolojilere yatırım yapma '
        'stratejisinin adıydı. Temel bileşenler: IoT, büyük veri, bulut bilişim, yapay '
        'zekâ, otomasyon.', S_BD))
    e.append(Paragraph(
        '<b>Dijital ikiz:</b> Bir fabrikanın, ürünün ya da altyapının tam dijital kopyası. '
        'Gerçek değişiklik yapmadan önce dijital kopyada test edilir. BMW\'nin Munich '
        'fabrikasında 82 farklı konfigürasyonda araç üretiliyor — bu ancak dijital planlama '
        'ile mümkün.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye:</b> TOGG Gemlik Fabrikası Endüstri 4.0 anlayışıyla tasarlandı. '
        'Bayraktar TB2\'nin üretim sürecinde otomasyon yoğun biçimde kullanılıyor. '
        'Aselsan, Roketsan gibi savunma sanayi kuruluşları da bu alanda hız kazandı.', S_NOT))

    e.append(Paragraph('Endüstri 5.0 (Günümüz)', S_H3))
    e.append(bilgi_kutusu(
        '4.0 ve 5.0 Arasındaki Temel Fark',
        ['Endüstri 4.0: Verimliliği merkeze aldı. "Makineler insanın yerini alacak mı?" sorusu.',
         'Endüstri 5.0: İnsanı ve sürdürülebilirliği öne çıkarır. '
         '"Makinelerle insanın birlikte çalışacağı sistemler tasarlayalım."',
         'AB 2021 Stratejisi üç ilkeyle tanımlar: İnsan merkezli + Sürdürülebilir + Dayanıklı (resilient).',
         'Cobot (collaborative robot): İnsanla fiziksel olarak iş birliği yapan robot.']))
    return e


# ============================================================
# BÖLÜM 4 — YAPAY ZEKÂ
# ============================================================

def bolum4():
    e = []
    e += bolum_baslik(4, 'YAPAY ZEKÂ')

    e.append(Paragraph('4.1 Basit ama Doğru Tanım', S_H2))
    e.append(Paragraph(
        'Yapay zekâ sihir değildir. Temelinde <b>istatistik, büyük veri ve güçlü '
        'bilgisayarlar</b> yatar. YZ sistemleri düşünmez; örüntü tanır. Milyonlarca veri '
        'noktasına bakarak "bu durumda en olası yanıt nedir?" sorusunu çözer. Bu bazen '
        'inanılmaz derecede doğru sonuçlar verir — ama gerçeği "bilmez", sadece '
        'istatistiksel tahmin yapar.', S_BD))

    e.append(Paragraph('4.2 Kısa Tarih', S_H2))
    tarih_data = [
        [Paragraph('Yıl', S_TH), Paragraph('Olay', S_TH)],
        [Paragraph('1950', S_TC), Paragraph('Alan Turing: "Makineler düşünebilir mi?" sorusu ve Turing Testi önerisi.', S_TC)],
        [Paragraph('1956', S_TC), Paragraph('John McCarthy, "Yapay Zekâ" terimini Dartmouth Konferansı\'nda ilk kez kullandı.', S_TC)],
        [Paragraph('1997', S_TC), Paragraph('IBM Deep Blue, satranç dünya şampiyonu Kasparov\'u yendi.', S_TC)],
        [Paragraph('2016', S_TC), Paragraph('AlphaGo, Go dünya şampiyonunu 4-1 yendi. Uzmanlar "en az 10 yıl uzakta" demişti.', S_TC)],
        [Paragraph('2022', S_TC), Paragraph('ChatGPT yayınlandı. Beş günde 1 milyon kullanıcıya ulaştı (Netflix\'in 3.5 yılda ulaştığı rakam).', S_TC)],
    ]
    tarih_t = Table(tarih_data, colWidths=[CW*0.13, CW*0.87])
    tarih_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, COLOR_VERY_LIGHT]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    e.append(KeepTogether([tarih_t, vsp(0.2)]))

    e.append(Paragraph('4.3 Halüsinasyon Nedir?', S_H2))
    e.append(bilgi_kutusu(
        'YZ Halüsinasyonu — Sinifta Nasil Aciklanir?',
        ['YZ modelleri zaman zaman kesinlikle yanlış olan bilgileri doğruymuş gibi sunar.',
         'NEDEN OLUR? Model gerçeği bilmez, istatistiksel olarak en makul cevabı üretir. '
         '"Bu sorunun cevabı genellikle böyle görünür" der — cevabın doğru olup olmadığını '
         'kontrol edemez.',
         'Örnek türleri: Var olmayan kitap adları, uydurma akademik makaleler, '
         'gerçekleşmemiş olaylar.',
         'Sınıfta nasıl açıklanır: "YZ bir öğrenciye benzer — bilmediği soruyu boş '
         'bırakmak yerine makul görünen bir şey yazar. Bu yüzden her YZ cevabını '
         'başka bir kaynakla karşılaştırın."']))

    e.append(Paragraph('4.4 Etik Sorular', S_H2))
    etik = [
        '<b>İş dönüşümü:</b> McKinsey 2030 tahmini — 375 milyon iş yeniden tanımlanacak (tamamen yok olmak değil, dönüşmek). Geçmişe bakarak: Matbaa yazıcıları işsiz bıraktı, ama editör ve kütüphaneci mesleklerini doğurdu.',
        '<b>Deepfake:</b> Bir kişinin yüzü ve sesi gerçekçi biçimde taklit edilebiliyor. Siyasi dezenformasyon ve kişisel mahremiyet açısından ciddi risk.',
        '<b>Sorumluluk belirsizliği:</b> Bir YZ yanlış tıbbi teşhis koyarsa kim sorumludur — programcı mı, hastane mi, hasta mı? Bu sorular henüz çözüme kavuşmadı.',
    ]
    for e_item in etik:
        e.append(Paragraph(f'• {e_item}', S_BUL))
    return e


# ============================================================
# BÖLÜM 5 — STEAM
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'STEAM')

    e.append(Paragraph('5.1 STEM\'den STEAM\'e Neden "A" Eklendi?', S_H2))
    e.append(Paragraph(
        'STEM kavramı 1990\'larda ABD\'de mühendis açığını kapatmak için ortaya çıktı. '
        '2000\'li yıllarda fark edildi ki teknik bilgisi güçlü ama iletişim, tasarım ve '
        'yaratıcılık becerileri zayıf mezunlar iş dünyasında tutunmakta zorlanıyordu. '
        '"Arts" (Sanat ve Tasarım) eklenerek STEAM oldu.', S_BD))
    e.append(Paragraph(
        'Apple\'ın "teknoloji + insanlık bilimleri" yaklaşımı buna iyi bir örnektir. '
        'Jobs düzenli olarak en iyi ürünleri "teknoloji ile insanlık bilimlerinin '
        'kesişiminde" konumlandırırdı.', S_BD))

    e.append(Paragraph('5.2 Doğadan Tasarlama: Biyomimikri Örnekleri', S_H2))
    bio = [
        ('Velcro (1941)', 'İsviçreli mühendis George de Mestral köpeğinin tüylerine yapışan çengelli tohumları inceledi. Bir kanca, bir ilmek — bugün 60 milyar dolarlık bir endüstri.'),
        ('Shinkansen Burnu (1997)', 'Japon hızlı treni tünellerden çıkarken gürültülü patlamalar yapıyordu. Mühendis Eiji Nakatsu aynı zamanda bir kuş bilimciydi. Dalıcı kuşun (kingfisher) koni şeklindeki gagasından esinlenerek tren burnu yeniden tasarlandı. Hem gürültü hem enerji tüketimi azaldı.'),
        ('Lotus Etkisi', 'Lotus çiçeğinin yaprakları hiç ıslanmaz — su damlacıkları yuvarlanır, tozu da beraberinde götürür. Bu mikro yapı incelenerek kendi kendini temizleyen boyalar, çatı kaplamaları ve tekstil ürünleri geliştirildi.'),
    ]
    for baslik, acik in bio:
        e.append(KeepTogether([
            Paragraph(baslik, S_H3),
            Paragraph(acik, S_BD),
        ]))

    e.append(Paragraph('5.3 STEAM Türkiye\'de', S_H2))
    e.append(Paragraph(
        'TÜBİTAK "4006 Bilim Fuarları" programıyla okullarda disiplinlerarası proje '
        'çalışmalarını destekliyor. Bu ünitenin sonunda öğrenciler STEAM anlayışının ne '
        'olduğunu kavramış olacak; <b>8. Ünitede</b> (Bütünleşik Öğrenme: STEAM) ise '
        'bunu uygulamalı deneyimleyecekler.', S_BD))
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
        ('"Teknoloji = bilgisayar veya telefon"',
         'Kaşık, tekerlek, çengelli iğne de birer teknolojidir. "Teknoloji her zaman bir problemi çözer" kuralını her nesneye uygulayın.'),
        ('"Keşif = icat"',
         'Kolomb Amerika\'yı keşfetti çünkü orada zaten insanlar vardı. Telefon icat edildi çünkü daha önce yoktu. Test: "Ben yapmadan önce var mıydı?"'),
        ('"Yapay zekâ düşünür / bilinçlidir"',
         'YZ veri üzerinde istatistiksel işlem yapar. Acıkmayı, korkmayı, sevinmeyi deneyimlemez. "Düşünüyor gibi görünmek" ile "düşünmek" farklıdır.'),
        ('"Endüstri 4.0 = robot kullanmak"',
         'Robotlar İkinci Sanayi Devrimi\'nden beri var. 4.0\'ın özü: Makinelerin birbiriyle ve insanla veri paylaşarak iletişim kurması.'),
        ('"Tasarım = güzelleştirme / dekorasyon"',
         'Tasarım önce bir problemi çözer. Estetik bu çözümün bir boyutudur, tek boyutu değil. En iyi ergonomik sandalyeler başta çirkin bulundu.'),
        ('"Buluş ve icat aynı şey"',
         'Buluş soyut fikir veya ilkedir (Newton\'ın hareket yasaları). İcat somut ürün veya süreçtir (telefon). Patent hukuku bu ayrımı netleştirir.'),
        ('"Grafik tasarım = Photoshop bilmek"',
         'Araç bir şey, düşünce biçimi başka. Grafik tasarımcı bir mesajı görsel olarak iletmeyi düşünür. Photoshop sadece araçtır.'),
        ('"STEAM sadece fen lisesi için"',
         'Bir yemek tarifi bile matematik (ölçüm), kimya (pişirme), sanat (sunum) ve teknolojidir. STEAM bir düşünce biçimidir.'),
        ('"İyi tasarım = pahalı tasarım"',
         'IKEA mobilyaları, Toyota araçları, Papermate kalemleri uygun fiyatlı ve iyi tasarlanmış örneklerdir. Fiyat ile tasarım kalitesi arasında zorunlu bir ilişki yoktur.'),
        ('"Endüstri 5.0 hâlâ gelecekte"',
         '5.0\'ın bazı unsurları — kobot kullanan fabrikalar, döngüsel tasarım — bugün bazı şirketlerde uygulanıyor. Tam yaygınlaşma sürmektedir.'),
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
        'İki Adam, Aynı Gün, Aynı İcat — Telefon Patenti',
        ['14 Şubat 1876 sabahı Graham Bell\'in avukatı ABD Patent Bürosu\'nun kapısında '
         'bekliyordu. Bell sabah 9:00\'da telefon patentini aldı. Elisha Gray, aynı gün '
         'birkaç saat sonra aynı icadın patent başvurusunu yaptı.',
         'Saatler Bell\'i tarihe yazdırdı. Elisha Gray ismi ise büyük çoğunlukla bilinmez.'],
        'İcat, buluş ve patent kavramlarına geçişte kullanılabilir.'))

    e.append(hikaye(
        'Okuldan Kovulan Deha — Edison',
        ['Thomas Edison ilkokul öğretmeni tarafından "zihni bozuk, öğrenmesi mümkün değil" '
         'notu yazılarak okuldan gönderildi. Annesi Nancy Edison hem avundurmak hem kanıtlamak '
         'için onu evde okutmaya başladı. Merakını besledi, her sorusunu ciddiye aldı.',
         'Edison hayatı boyunca 1093 patent aldı: ampul, fonograf, sinema kamerası, '
         'elektrik dağıtım sistemi bunların arasında.'],
        '"Merak" bileşenine (E1.1) ve icat kavramına geçişte kullanılabilir.'))

    e.append(hikaye(
        'Gülen Son Kim Oldu? — Nokia ve iPhone',
        ['2007\'de Steve Jobs sahneye çıkıp "Bugün üç devrimci ürünü tanıtıyoruz" dedi, '
         'sonunda hepsinin tek bir cihaz olduğunu açıkladı.',
         'Nokia o yıl cep telefonu pazarının yüzde kırkını elinde tutuyordu. Her iki '
         'şirketin yöneticileri de klavyesiz telefon fikrine güldü: "Pil ömrü olmaz. '
         'Kurumsal müşteri almaz. Çok pahalı."',
         '2009\'da Nokia CEO\'su "iPhone konusunda yanıldık" dedi. 2013\'te Nokia telefon '
         'bölümünü Microsoft\'a sattı.'],
        '"Tasarım bazen kullanıcının neye ihtiyacı olduğunu kullanıcıdan önce görür."'))

    e.append(hikaye(
        'Mükemmel Teknoloji, Yanlış Tasarım — Segway',
        ['2001\'de Steve Jobs "Apple tarihindeki en önemli üründen daha büyük olacak" demişti.',
         'Segway tanıtıldı. Teknoloji şaşırtıcıydı: jiroskopik denge, elektrikli motor, '
         'şarj edilebilir pil. Düşmüyordu.',
         '20 yılda 140.000 adet satılabildi. iPhone ilk haftasında 270.000 sattı.',
         'Sorun: Gerçek bir problemi çözmüyordu. İnsanlar yürümekten şikayet etmiyordu; '
         'kaldırımda büyük araçla gitmekten utanıyordu ve şarj altyapısı yoktu.'],
        '"Teknoloji + tasarım yetmez, gerçek ihtiyaç şart." Değerlendirme ölçütlerine.'))

    e.append(hikaye(
        'Başarısızlık Farklı Bir Soruyu Çözüyor — Post-it',
        ['1968\'de 3M\'de kimyager Spencer Silver, son derece güçlü bir yapıştırıcı '
         'geliştirmeye çalışıyordu. Sonuç: Çok zayıf bir yapıştırıcı. Yapıştırıyordu '
         'ama kolayca çıkıyordu. 3M hiç işe yaramaz dedi.',
         '1974\'te meslektaşı Art Fry kilisede ilahi kitabına yer işareti arıyordu. '
         'Silver\'ın yapıştırıcısını hatırladı. Küçük kâğıt parçaları yapıştı ve kalktı '
         '— kitap zarar görmemişti. Şirket birçok kez reddetti.',
         '1980\'de piyasaya çıktı. Bugün yılda 50 milyar dolar değerinde satış.'],
        '"Bir başarısızlık farklı bir problemin çözümü olabilir."'))

    e.append(hikaye(
        'Sinan\'ın Hesabı — Selimiye Camii',
        ['Sinan, Edirne\'ye gönderildiğinde 80 yaşına yaklaşıyordu. Amacı açıktı: '
         'Ayasofya\'yı aşmak. Ama Ayasofya\'nın kubbe çapı 31.87 m; Selimiye\'ninki '
         '31.25 m. Teknik olarak çapı geçemedi.',
         'Ama Sinan başka bir şey yaptı: Sekiz sütunla taşınan kubbe altında tamamen '
         'açık, bölünsüz bir iç mekân yarattı. Ayasofya\'da iç sütunlar mekânı parçalar; '
         'Selimiye\'de tek bir nefes var.',
         'Mimarlık tarihçileri bugün büyük çoğunlukla "Selimiye daha zor bir başarıdır" der.'],
        '"İyi tasarım kısıtlarla savaşmaz, onlarla birlikte yaratıcı olur."'))

    return e


# ============================================================
# BÖLÜM 8 — ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR')
    e.append(Paragraph(
        'Bazı sorular anında yanıt gerektirmez. "Harika soru — düşünmem lazım" ya da '
        '"Bu konuyu 9. ünitede daha ayrıntılı işleyeceğiz" demek tamamen uygundur.',
        S_BD))

    qas = [
        ('"Yapay zekâ er ya da geç insanın yerini alacak mı?"',
         'Tarihsel kalıp tutarsa: Her büyük teknoloji bazı meslekleri bitirdi, yenilerini doğurdu. Matbaa yazıcıları işsiz bıraktı, ama editör ve kütüphaneci mesleklerini yarattı. Otomobil seyisleri işsiz bıraktı, ama tamirci ve trafik polisi mesleklerini doğurdu. YZ da bazı işleri dönüştürecek — hangi yeni mesleklerin doğacağını henüz bilmiyoruz.'),
        ('"ChatGPT benden daha mı akıllı?"',
         'Farklı bir zekâ türü. ChatGPT milyonlarca kitap ve makale okudu. Ama hiç acıkmadı, korkmadı, umursamadı. Sen acıktığında odaklanamadığını biliyorsun — o bilmiyor. "Hangisi daha akıllı?" sorusu belki yanlış soru. İkisi farklı.'),
        ('"Endüstri 5.0 gerçekten insan için mi, yoksa yine kâr için mi?"',
         'Dürüst yanıt: İkisi çelişmez ama gerilim var. Şirketlerin temel güdüsü kârdır. Ancak AB\'nin 5.0 stratejisi devlet düzeyinde yönlendirme içeriyor. Hangi değerlerin ön plana çıkacağı büyük ölçüde kamusal baskıya ve politika tercihlerine bağlı.'),
        ('"Türkiye neden geride?"',
         'Bazı alanlarda geride, bazı alanlarda değil. Bayraktar TB2 dünyanın en çok satan insansız hava araçlarından biri. TOGG yerli elektrikli araç. Türk yazılımcılar küresel şirketlerin çekirdek ekiplerinde çalışıyor. Getir, Trendyol, Peak Games — Türk kurucuların unicorn şirketleri. Eksik olan: Temel araştırma ve patent ekosistemi.'),
        ('"Grafik tasarımcı YZ\'den etkilenir mi?"',
         'Evet, etkileniyor. Midjourney ve DALL-E gibi araçlar saniyeler içinde görsel üretiyor. Ama grafik tasarımcıların işi yalnızca görsel üretmek değil — müşteriyi dinlemek, mesajı anlamak, hedef kitleyi tanımak, stratejik karar vermek. Bu süreçler için insana hâlâ ihtiyaç var.'),
    ]

    for soru, cevap in qas:
        e.append(KeepTogether([
            Paragraph(soru, S_QQ),
            Paragraph(cevap, S_QA),
        ]))

    e.append(vsp(0.5))
    e.append(hr(c=COLOR_LIGHT_GREY))
    e.append(Paragraph(
        '<i>Bu doküman 1. Ünite öğretim sürecinin arka planını oluşturmak amacıyla '
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
        title='1. Unite - Ogretmen Hazirlik Rehberi',
        author='Teknoloji ve Tasarim Ogretim Programi',
    )
    doc.unite_info = UI
    doc.doc_title  = 'Unite Icerigi Hazirlik Materyali'

    story = make_cover(
        title    = '1. Ünite — Ünite İçeriği Hazırlık Materyali',
        subtitle = 'Teknoloji ve Tasarım Öğreniyorum',
        meta_info= {
            'Sınıf'      : '7. Sınıf',
            'Ders'       : 'Teknoloji ve Tasarım',
            'Ünite Süresi': '4 Ders Saati (2 Hafta)',
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
    print('OK  U1_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
