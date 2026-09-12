# -*- coding: utf-8 -*-
"""
8. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit8/U8_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite8_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit8')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U8_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '8. Ünite - Bütünleşik Öğrenme: STEAM'
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
# BÖLÜM 1 — KAVRAMLARIN ANATOMİSİ
# ============================================================

def bolum1():
    e = []
    e += bolum_baslik(1, 'KAVRAMLARIN ANATOMİSİ')
    e.append(Paragraph(
        'Bu ünitenin temel kavramları — STEAM, bütünleşik öğrenme, mühendislik tasarım süreci, '
        'problem analizi, beyin fırtınası, prototip ve mini sergi — disiplinlerarası çalışmanın '
        'hem düşünce biçimini hem de uygulama sürecini tanımlar. Öğrencilerin bu kavramları '
        'sezgisel düzeyde yaşayarak öğrenmesi hedeflenir.', S_BD))

    # 1.1 STEAM ve STEM
    e.append(Paragraph('1.1 STEAM ve STEM', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> STEAM, Bilim (Science), Teknoloji (Technology), Mühendislik (Engineering), '
        'Sanat (Art) ve Matematik (Mathematics) disiplinlerinin tek bir problem veya proje '
        'etrafında bütünleştirildiği eğitim yaklaşımıdır. STEM\'in 1990\'larda ABD\'de ortaya çıkan '
        'önceki versiyonuna, 2000\'lerin ortasında sanatın eklenmesiyle STEAM oluşmuştur.', S_BD))

    steam_tablo = [
        [Paragraph('Boyut', S_TH), Paragraph('STEM', S_TH), Paragraph('STEAM', S_TH)],
        [Paragraph('Odak', S_TC),
         Paragraph('Teknik çözüm', S_TC),
         Paragraph('İnsan merkezli çözüm', S_TC)],
        [Paragraph('Sanat', S_TC),
         Paragraph('Dışarıda', S_TC),
         Paragraph('İçeride (tasarım, estetik, iletişim)', S_TC)],
        [Paragraph('Değerlendirme', S_TC),
         Paragraph('İşlevsellik', S_TC),
         Paragraph('İşlevsellik + kullanıcı deneyimi', S_TC)],
        [Paragraph('Yaratıcılık', S_TC),
         Paragraph('Araç', S_TC),
         Paragraph('Hedef', S_TC)],
    ]
    t = Table(steam_tablo, colWidths=[CW*0.22, CW*0.32, CW*0.46])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('BACKGROUND',    (0, 1), (-1, -1), COLOR_VERY_LIGHT),
        ('ROWBACKGROUNDS',(0, 2), (-1, -1), [COLOR_VERY_LIGHT, white]),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('GRID',          (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    e.append(KeepTogether([t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> "A" yalnızca resim veya müzik değildir; mimari çizim, grafik '
        'tasarım, sunum estetiği, mekânsal düşünme — bunların hepsi sanatsal düşünmenin '
        'biçimleridir.', S_NOT))

    # 1.2 Bütünleşik Öğrenme
    e.append(Paragraph('1.2 Bütünleşik Öğrenme', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Birden fazla disiplinin bilgi, kavram ve becerilerinin tek bir gerçek '
        'yaşam problemi etrafında birleştirildiği öğrenme biçimidir.', S_BD))
    for satir in [
        '<b>Çok disiplinli:</b> Her ders kendi konusunu ayrı ayrı işler; bağlantılar öğretmen '
        'tarafından gösterilir.',
        '<b>Disiplinlerarası:</b> Ortak bir tema veya proje üzerinden disiplinler iş birliği '
        'yapar; çakışma noktaları planlanmıştır.',
        '<b>Disiplinötesi (transdiscipliner):</b> Disiplin sınırları eriyip proje merkezli bir '
        'bütün oluşur — öğrenci hangi disiplini ne zaman kullandığını fark etmeyebilir.',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))
    e.append(Paragraph(
        '<b>Not:</b> Bu ünite <b>disiplinlerarası</b> düzeyi hedefler; tam transdisipliner '
        'geçiş için okul geneli koordinasyon gerekir.', S_NOT))

    # 1.3 Mühendislik Tasarım Süreci
    e.append(Paragraph('1.3 Mühendislik Tasarım Süreci', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Mühendislik Tasarım Süreci (MTS), bir problemi çözmek için sistematik '
        'adımlar izleyen döngüsel bir yaklaşımdır. Her adım bir öncekine geri dönüşe izin verir.',
        S_BD))
    for satir in [
        '1. <b>Tanımla:</b> Problemi net biçimde ifade et; kısıtları ve koşulları belirle.',
        '2. <b>Araştır:</b> Benzer çözümleri incele; paydaşları tanı.',
        '3. <b>Fikir Üret:</b> Beyin fırtınası ile birden fazla çözüm seçeneği oluştur.',
        '4. <b>Planla:</b> En iyi fikri seç; malzeme, görev ve zaman planı yap.',
        '5. <b>Üret:</b> Prototipi/modeli inşa et.',
        '6. <b>Test Et ve Revize Et:</b> Çözümü ölçütlere göre değerlendir; gerekirse geri dön.',
    ]:
        e.append(Paragraph(satir, S_IND))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> Öğrenciler süreci tek yönlü sanır. "Hata = geri dön" mesajını '
        'ünite boyunca sürekli pekiştirin.', S_NOT))

    # 1.4 Problem Analizi ve 5N1K
    e.append(Paragraph('1.4 Problem Analizi ve 5N1K', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> İyi bir STEAM projesi, iyi tanımlanmış bir problemle başlar. 5N1K (Ne, '
        'Nerede, Ne zaman, Neden, Nasıl, Kim) yapılandırılmış bir sorgulama çerçevesidir.',
        S_BD))
    e.append(Paragraph('<b>İyi problem kriterleri:</b>', S_BD))
    for satir in [
        'Gerçek bir ihtiyaçtan kaynaklanır (hayali değil).',
        'Atölye koşullarında çözülebilecek ölçektedir.',
        'En az 3 STEAM bileşenini harekete geçirir.',
        'Birden fazla çözüm yolu vardır (tek doğru cevap yok).',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))
    e.append(Paragraph(
        '<b>Sık karşılaşılan problem:</b> Öğrenciler "sorun" yerine "proje" seçer — '
        '"robotik araç yapalım" bir problem değil, bir çözümdür. Problemi önce sorun olarak '
        'tanımlamak gerekir.', S_NOT))

    # 1.5 Beyin Fırtınası
    e.append(Paragraph('1.5 Beyin Fırtınası', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Alex Osborn tarafından 1940\'larda formüle edilen yaratıcı fikir üretme '
        'tekniğidir. Temel ilkesi, yargılamayı erteleyerek fikir miktarını artırmak ve ardından '
        'kaliteye odaklanmaktır.', S_BD))
    e.append(bilgi_kutusu(
        'Osborn\'ın 4 Kuralı',
        [
            '1. Yargılama yok — hiçbir fikir "saçma" değil.',
            '2. Miktara odaklan — çok fikir üret.',
            '3. Garip fikirler değerli — alışılmadık düşün.',
            '4. Birleştir ve geliştir — başkasının fikri üzerine inşa et.',
        ]))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> Beyin fırtınası aşamasında "Bu olmaz" veya "Çok pahalı" gibi '
        'değerlendirmeler yapmaktan kaçının. Bu aşama serbest düşünceye ayrılmıştır; eleme '
        'sonraki adımdadır.', S_NOT))

    # 1.6 Prototip ve Model
    e.append(Paragraph('1.6 Prototip ve Model', S_H2))
    e.append(Paragraph(
        '<b>Prototip:</b> Bir ürünün işlevselliğini test etmek için üretilen deneme sürümüdür. '
        'Genellikle sade malzemeyle yapılır; görünüş değil işlev öncelidir.', S_BD))
    e.append(Paragraph(
        '<b>Model:</b> Bir ürünü, yapıyı veya sistemi temsil eden ve ölçekli veya kavramsal '
        'olabilen fiziksel ya da dijital nesne. Genellikle iletişim amacıyla kullanılır.', S_BD))
    e.append(Paragraph(
        '<b>Fark:</b> Tasarımcı "bu böyle görünecek" demek için maket (model) yapar; '
        'mühendis "bu böyle çalışacak mı?" sorusuna cevap için prototip üretir.', S_NOT))

    # 1.7 Mini Sergi
    e.append(Paragraph('1.7 Mini Sergi', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Öğrencilerin proje süreçlerini ve ürünlerini sınıf içi ya da okul '
        'genelinde paylaştığı yapılandırılmış bir sunum etkinliğidir. Bilim fuarı, maker fair '
        've proje günü formlarının okul uyarlamasıdır.', S_BD))
    e.append(Paragraph(
        '<b>Standart sunumdan farkı:</b> Standart sunumda öğrenci öğretmene anlatır; mini '
        'sergide öğrenci herkese (yaşıt, öğretmen, ziyaretçi) aynı anda kendi standında anlatır. '
        'Bu, iletişim becerisini farklı biçimde geliştirir.', S_BD))

    return e


# ============================================================
# BÖLÜM 2 — TARİHSEL ARKA PLAN
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TARİHSEL ARKA PLAN')

    # 2.1 Sputnik
    e.append(Paragraph('2.1 Sputnik Krizi ve STEM\'in Temelleri (1957–1983)', S_H2))
    e.append(Paragraph(
        '4 Ekim 1957\'de Sovyetler Birliği\'nin Sputnik uydusunu uzaya fırlatması, ABD\'de büyük '
        'bir eğitim paniğine yol açtı. 1958\'de National Defense Education Act çıkarıldı; fen '
        've matematik eğitimine yoğun kaynak ayrıldı. National Science Foundation (NSF) büyüdü; '
        'müfredat yenilemesi başladı.', S_BD))
    e.append(Paragraph(
        '1983\'te "A Nation at Risk" raporu yayımlandı: Amerikan eğitim sistemi çöküyor, gençler '
        'bilim ve matematikte zayıf. Bu rapor STEM odaklı reform hareketini yeniden ateşledi.',
        S_BD))

    # 2.2 STEM terimi
    e.append(Paragraph('2.2 "STEM" Teriminin Doğuşu (1990\'lar)', S_H2))
    e.append(Paragraph(
        'NSF yöneticisi Judith Ramaley, 1990\'ların başında "SMET" kısaltmasını kullanıyordu. '
        'Kelime çirkin geliyordu. Ramaley 2001 yılında harf sırasını değiştirerek "STEM"i yarattı. '
        'Terim hızla yayıldı ve Beyaz Saray\'a, ulusal müfredat tartışmalarına girdi.', S_BD))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> "STEM" bugün çok yaygın kullanılsa da 25 yıllık görece yeni '
        'bir kavramdır. "Bu kısaltmayı biri icat etti" demek, kavramın insan yapımı olduğunu '
        'somutlaştırır.', S_NOT))

    # 2.3 STEAM
    e.append(Paragraph('2.3 "A" Eklenmesi: STEAM Doğuyor (2006–2011)', S_H2))
    e.append(Paragraph(
        'Rhode Island School of Design (RISD) rektörü John Maeda, 2006-2008 yıllarında Sanat '
        've Tasarım\'ı STEM\'e entegre etmeyi savunmaya başladı. Argümanı şuydu: Teknolojik '
        'çözümler yalnızca mühendislikle değil, kullanıcı odaklı tasarım düşüncesiyle anlam '
        'kazanır. İnsanlar ürünleri estetik ve kullanım kolaylığı nedeniyle benimser.', S_BD))
    e.append(Paragraph(
        '2011\'de ABD Kongresi, STEM eğitimine sanatı entegre eden önerileri resmen tartışmaya '
        'açtı. "STEAM" terimi ulusal gündemde yerini aldı.', S_BD))

    # 2.4 Maker hareketi
    e.append(Paragraph('2.4 Maker Hareketi ve FabLab\'lar (2005–2015)', S_H2))
    e.append(Paragraph(
        'MIT Media Lab\'dan Neil Gershenfeld\'in 2005\'teki "Fab" kitabı, "herkes üretici '
        'olabilir" fikrini yaydı. FabLab (Fabrication Laboratory) ağı dünya genelinde büyüdü: '
        '2024 itibarıyla 60\'tan fazla ülkede 2.000\'den fazla FabLab var.', S_BD))
    e.append(bilgi_kutusu(
        'Maker Hareketi STEAM\'i Somutlaştırdı',
        [
            'Lazer kesiciler, 3D yazıcılar, elektronik prototip araçları — bunlar okulları '
            '"fabrikaya" dönüştürme imkânı verdi.',
            'Fikir + el + teknoloji bir araya geldi. Yaparak öğrenme, soyut STEAM kavramlarını '
            'somutlaştırır.',
        ]))

    # 2.5 FIRST Robotics
    e.append(Paragraph('2.5 FIRST Robotics (1992–günümüz)', S_H2))
    e.append(Paragraph(
        'Dean Kamen, 1992\'de FIRST (For Inspiration and Recognition of Science and Technology) '
        'yarışmasını kurdu. Her yıl lise takımları gerçek mühendislik problemleri için robot '
        'tasarlar ve yarışır.', S_BD))
    e.append(Paragraph(
        'FIRST bugün 100\'den fazla ülkede, milyonlarca genç katılımcıyla dünyanın en büyük '
        'gençlik STEAM programı. Temel mesaj: "Mühendisler ve bilim insanları sporculara benzer '
        'şekilde idol olabilir."', S_BD))

    # 2.6 Türkiye
    e.append(Paragraph('2.6 Türkiye\'de STEAM (2015–günümüz)', S_H2))
    e.append(Paragraph(
        'TÜBİTAK, 2015 yılında Fen, Teknoloji, Mühendislik ve Matematik\'i (FeTeMM) teşvik '
        'eden programlar başlattı; okul projelerine destek verdi. Milli Eğitim Bakanlığı, '
        '2023 Maarif Modeli reformunda bütünleşik proje tabanlı öğrenmeyi müfredata resmi '
        'olarak dahil etti.', S_BD))
    e.append(Paragraph(
        'Bu ünite, o dönüşümün sınıf ölçeğindeki uygulamasıdır.', S_BD))

    return e


# ============================================================
# BÖLÜM 3 — KRONOLOJİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'KRONOLOJİ')

    satir_verileri = [
        ('1957', 'Sputnik şoku; ABD\'de fen ve matematik eğitimine yatırım arttı'),
        ('1958', 'National Defense Education Act yürürlüğe girdi'),
        ('1983', '"A Nation at Risk" raporu; STEM reformuna zemin hazırlandı'),
        ('1992', 'Dean Kamen FIRST Robotics yarışmasını kurdu'),
        ('1993', 'NSF "STEM" kısaltmasını kullanmaya başladı'),
        ('2001', 'Judith Ramaley harf sırasını değiştirerek "STEM" terimini resmileştirdi'),
        ('2005', 'Neil Gershenfeld "Fab" kitabını yayımladı; FabLab hareketi başladı'),
        ('2006', 'John Maeda (RISD) Sanatı STEM\'e eklemeyi savundu; "STEAM" doğdu'),
        ('2008', 'Tim Brown "Design Thinking" kavramını HBR\'de mainstreamleştirdi'),
        ('2011', 'STEAM, ABD Kongresi\'nde resmi tartışma konusu oldu'),
        ('2013', 'Maker hareketi zirveye ulaştı; White House Maker Faire'),
        ('2015', 'TÜBİTAK FeTeMM programları Türkiye\'de yaygınlaştı'),
        ('2020', 'Pandemi: STEAM eğitimi dijital araçlarla evlere taşındı'),
        ('2023', 'Türkiye Maarif Modeli reformu; bütünleşik öğrenme müfredata girdi'),
    ]

    header = [[Paragraph('Yıl', S_TH), Paragraph('Gelişme', S_TH)]]
    rows = [[Paragraph(y, S_TCB), Paragraph(g, S_TC)] for y, g in satir_verileri]
    tablo = header + rows

    t = Table(tablo, colWidths=[CW*0.10, CW*0.90])
    stil = [
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('GRID',          (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]
    for i in range(1, len(tablo)):
        if i % 2 == 1:
            stil.append(('BACKGROUND', (0, i), (-1, i), COLOR_VERY_LIGHT))
    t.setStyle(TableStyle(stil))
    e.append(KeepTogether([t, vsp(0.2)]))

    return e


# ============================================================
# BÖLÜM 4 — GÜNCEL DURUM
# ============================================================

def bolum4():
    e = []
    e += bolum_baslik(4, 'GÜNCEL DURUM')

    e.append(Paragraph('4.1 Dünyada STEAM Eğitiminin Yayılması', S_H2))
    e.append(Paragraph(
        'Bugün Singapur, Finlandiya, Güney Kore ve Avustralya STEAM yaklaşımını ulusal '
        'müfredatlarına entegre etmiş durumdadır. Singapur\'un "21st Century Competencies" '
        'çerçevesi, disiplinlerarası proje tabanlı öğrenmeyi temel alır. PISA 2022 verileri, '
        'problem çözme ve yaratıcı düşünme boyutlarında bu ülkelerin öne çıktığını '
        'göstermektedir.', S_BD))

    e.append(Paragraph('4.2 Maker Eğitimi ve FabLab\'lar', S_H2))
    e.append(Paragraph(
        'Dünya genelinde 100\'ü aşkın ülkede FabLab ağı aktif durumdadır. Okullara uyarlanmış '
        '"Mini Fab" laboratuvarları, lazer kesici, 3D yazıcı ve elektronik prototipleme '
        'araçlarıyla donanmış. Türkiye\'de bazı pilot okullarda atölye dönüşümleri başladı; '
        'TÜBİTAK STEM merkezleri ülke genelinde yaygınlaşıyor.', S_BD))

    e.append(Paragraph('4.3 Yapay Zekâ ile STEAM', S_H2))
    e.append(Paragraph(
        'YZ, STEAM eğitiminin yeni bir boyutu oldu. Öğrenciler artık üretken YZ araçlarıyla '
        '"sanat bileşeni"ni destekleyebiliyor; robot kodlamada YZ yardımı alınabiliyor. '
        'Ancak risk de var: YZ\'nin süreci değil, ürünü oluşturması durumunda öğrencinin '
        'öğrenmesi gerçekleşmez.', S_BD))
    e.append(Paragraph(
        '<b>Öğretmen rehberliği:</b> "YZ, adımı yapıyor mu yoksa sen mi?" sorusu sınıfta '
        'sıklıkla sorulmalı.', S_NOT))

    e.append(Paragraph('4.4 Türkiye\'de Proje ve Yarışmalar', S_H2))
    for satir in [
        '<b>TÜBİTAK 4006 Bilim Fuarı:</b> Ortaokul öğrencilerinin bilimsel proje hazırladığı, '
        'okul ve bölge fuarlarını kapsayan ulusal program.',
        '<b>TEKNOFEST Genç Tasarımcılar:</b> 13-17 yaş grubuna yönelik prototip tasarım '
        'yarışması; bütünleşik proje yaklaşımı teşvik edilmektedir.',
        '<b>Maarif Atölyeleri:</b> Bazı illerde TT dersine bağlı atölye alanları yenileniyor.',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))

    return e


# ============================================================
# BÖLÜM 5 — DİSİPLİNLERARASI BAĞLANTILAR
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'DİSİPLİNLERARASI BAĞLANTILAR')

    e.append(Paragraph('5.1 Fen Bilgisi', S_H2))
    e.append(Paragraph(
        'Bilim bileşeni doğrudan Fen\'e dayanır: malzeme özellikleri, enerji dönüşümü, '
        'biyoloji, kimya. Problem analizi aşamasında öğrenciler fen bilgisi birikimlerini '
        'kullanır. Koordinasyon önerisi: projenin bilimsel dayanağı hangi Fen konularıyla '
        'örtüşüyor?', S_BD))

    e.append(Paragraph('5.2 Matematik', S_H2))
    e.append(Paragraph(
        'Ölçüm (uzunluk, alan, hacim), oran-orantı, veri toplama ve grafik okuma doğrudan '
        'projeye entegre edilir. Malzeme listesi hesapları, zaman çizelgesi yüzdeleri, '
        'prototip boyutlandırması — bunların tümü Matematik bileşenidir.', S_BD))

    e.append(Paragraph('5.3 Görsel Sanatlar', S_H2))
    e.append(Paragraph(
        'Eskiz çizme, renk ve biçim seçimi, prototip estetiği, sunum görselleri — bunlar '
        '"A" bileşenidir. Görsel Sanatlar öğretmeniyle ortak değerlendirme ölçütleri '
        'oluşturmak proje kalitesini artırır.', S_BD))

    e.append(Paragraph('5.4 Bilişim Teknolojileri', S_H2))
    e.append(Paragraph(
        'Araştırma, dijital sunum hazırlama, tasarım araçları (Canva, Google Slayt, '
        'Tinkercad) Bilişim bileşenini oluşturur. Üst düzey projeler Arduino veya basit '
        'kodlama içerebilir.', S_BD))

    e.append(Paragraph('5.5 Türkçe', S_H2))
    e.append(Paragraph(
        'Sunum becerisi, yazılı proje raporu, paydaş röportajı dökümü — bunlar doğrudan '
        'Türkçe dersiyle kesişir. Mini sergi sunumu, sözlü iletişim değerlendirmesi için '
        'Türkçe öğretmeniyle ortak rubrik kullanmak değerli bir iş birliği fırsatıdır.',
        S_BD))

    e.append(Paragraph('5.6 Sosyal Bilgiler', S_H2))
    e.append(Paragraph(
        'Paydaş analizi ve toplumsal etki değerlendirmesi Sosyal Bilgiler\'e bağlanır. '
        'Problemi yaşayan insanların bakış açısını anlamak (empati), kimin etkilendiğini '
        'saptamak (paydaş haritası) bu dersin yaklaşımlarıyla örtüşür.', S_BD))

    return e


# ============================================================
# BÖLÜM 6 — YANLIŞ ANLAMALAR
# ============================================================

def bolum6():
    e = []
    e += bolum_baslik(6, 'YANLIŞ ANLAMALAR')

    yanlis = [
        ('"STEAM\'de Sanat dekoratiftir; asıl önemli teknik kısımdır."',
         'Sanat, kullanıcı deneyimini, iletişim gücünü ve insan merkezli tasarımı temsil eder '
         '— işlevsel bir bileşendir.'),
        ('"STEAM ile STEM aynı şeydir, sadece harf eklendi."',
         'STEM teknik çözüme odaklanırken STEAM insan odaklı, yaratıcı ve estetik boyutu '
         'da kapsar. Yaklaşım temelden farklıdır.'),
        ('"STEAM projeleri pahalı malzeme ve özel ekipman gerektirir."',
         'Karton, tahta çubuk, plastik şişe, tel — bunlarla güçlü prototipler yapılabilir. '
         'Makerspaces güzel ama zorunlu değil.'),
        ('"Her STEAM bileşeni projede eşit ağırlık taşımalı."',
         'Projeye göre ağırlık değişir; bir sulama sistemi Mühendislik ağırlıklı olabilir. '
         'Önemli olan tüm bileşenlerin farkında olunması.'),
        ('"STEAM sadece üst düzey öğrenciler için uygundur."',
         'Farklı güçlükte katkı sağlayan roller sayesinde tüm öğrenciler dahil edilebilir; '
         'zorluk düzeyi esnektir.'),
        ('"Başarılı bir STEAM projesi çalışan bir prototip demektir."',
         'Süreç de değerlendirilir: problem tanımlama, araştırma, fikir üretme, planlama. '
         'Çalışmayan bir prototip de öğretici olabilir.'),
        ('"STEAM = müzik ve resim entegrasyonu."',
         '"A" daha geniş: mimarlık, grafik tasarım, mekânsal düşünme, sunum estetiği, '
         'hikâye anlatımı hepsi bu bileşenin kapsamındadır.'),
        ('"En güçlü öğrenci lider olmalı; diğerleri takipçi."',
         'STEAM rolleri dağıtılır: araştırmacı, yapımcı, tasarımcı, sunum uzmanı gibi '
         'farklı roller her öğrenciye özgü katkı fırsatı verir.'),
    ]

    header = [[Paragraph('Yanlış Anlama', S_TH), Paragraph('Doğrusu', S_TH)]]
    rows = [[Paragraph(y, S_TC), Paragraph(d, S_TC)] for y, d in yanlis]
    tablo = header + rows

    t = Table(tablo, colWidths=[CW*0.38, CW*0.62])
    stil = [
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('GRID',          (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]
    for i in range(1, len(tablo)):
        if i % 2 == 1:
            stil.append(('BACKGROUND', (0, i), (-1, i), COLOR_VERY_LIGHT))
    t.setStyle(TableStyle(stil))
    e.append(KeepTogether([t, vsp(0.2)]))

    return e


# ============================================================
# BÖLÜM 7 — HİKÂYELER
# ============================================================

def bolum7():
    e = []
    e += bolum_baslik(7, 'HİKÂYELER')

    e.append(hikaye(
        'James Dyson: 5.127 Prototipin Hikâyesi',
        [
            'James Dyson, 1979\'da evinin süpürgesinin çöp torbasının süpürme gücünü düşürdüğünü '
            'fark etti. "Torbasız süpürge yapılabilir mi?" sorusunu sordu. Sonraki 5 yıl boyunca '
            '5.126 prototipi yaptı — hepsi başarısız oldu. 5.127. prototip çalıştı. 1993\'te '
            'piyasaya sürdüğü G-Force modeli bugün milyarlarca dolarlık bir markanın '
            'başlangıcıydı.',
            '"Dyson\'ın 5.126 başarısız prototipi çöp değil; her biri \'bu çalışmıyor, '
            'sıradakini dene\' dersi verdi. STEAM\'de başarısızlık, yöntemin parçasıdır."',
        ],
        'Öğrencilere anlatın: Başarısızlık sayısı değil, her başarısızlıktan ne öğrenildiği önemlidir.'))

    e.append(hikaye(
        'Dean Kamen: Robot Yarışmasıyla Gençleri STEM\'e Çekmek',
        [
            'Mühendis ve mucit Dean Kamen, 1992\'de FIRST Robotics yarışmasını kurdu. Fikir '
            'basitti: Gençler sporculara hayran oluyorsa, mühendislere de hayran olabilir — '
            'ama onların da "sahnesine" ihtiyaçları var. Robot tasarlama ve yarışma bu '
            '"sahneyi" sağladı.',
            'Bugün FIRST, 100\'den fazla ülkede milyonlarca genç katılımcıya ulaşıyor ve '
            'dünyanın en büyük gençlik STEAM programıdır.',
        ],
        'Mesaj: İlham verici bir bağlam yaratmak, STEAM öğrenmesini güçlü biçimde tetikler.'))

    e.append(hikaye(
        'Nike Breaking2: Spor Bilimi, Mühendislik ve Tasarımın Buluşması',
        [
            '2017\'de Nike, bir insanın maratonun 2 saatten kısa sürede koşup koşamayacağını '
            'test etti. Biyomekanik uzmanlar, spor fizyologları, ayakkabı mühendisleri, veri '
            'analistleri ve tasarımcılar bir araya geldi: ZoomX köpük, karbon fiber tabanlık '
            'plakası, aerodinamik üst kısım — her detay hesaplanmıştı.',
            'Eliud Kipchoge 1:59:40 ile koştu. Bu, doğrudan STEAM\'in sporttaki pratiğiydi.',
        ],
        'Öğrencilere sorun: Bu projede her STEAM bileşeni nerede devreye girdi?'))

    e.append(hikaye(
        'Pixar\'ın İlk Dijital Animasyon Filmi: Toy Story (1995)',
        [
            '1995\'te vizyona giren Toy Story, dünyanın ilk uzun metrajlı tam bilgisayar '
            'animasyon filmiydi. Pixar\'ın ekibi ressamlar, hikâye yazarları, fizik '
            'mühendisleri ve matematik uzmanlarından oluşuyordu.',
            'Renk fiziği doğru çalışmalıydı, ışık hesaplamaları gerçekçi görünmeliydi, '
            'karakterler hem hareket hem ifade açısından ikna edici olmalıydı. Hiçbir '
            'disiplin tek başına yetmezdi.',
            '"İzlediğiniz her animasyon filmi bir STEAM projesidir."',
        ],
        'Mesaj: Sanat ve teknik birbirinin rakibi değil, ortağıdır.'))

    e.append(hikaye(
        'TÜBİTAK 4006 Fuarı\'ndan Bir Ortaokul Öğrencisi',
        [
            '2019 yılında Kocaeli\'den bir ortaokul öğrenci grubu, okullarının geri dönüşüm '
            'oranını artırmak için renk kodlu sensörlü çöp kutusu tasarladı. Arduino, '
            'sensörler, 3D baskılı parçalar — ve en önemlisi, sınıf arkadaşlarıyla '
            'yürüttükleri anket.',
            'Proje bölge fuarına taşındı ve ödül kazandı. Mühendislik (sensör, elektronik) '
            '+ Matematik (veri analizi) + Sosyal Bilgiler (okul anketi, toplumsal fayda) '
            '+ Görsel Sanatlar (tasarım) + Türkçe (sunum) = gerçek STEAM.',
        ],
        'Öğrencilere söyleyin: Bu ödülü alan sizin yaşınızdaki öğrencilerdi.'))

    e.append(hikaye(
        'Başarısızlık Dersi: Yarışma Sabahı Çalışmayan Kol',
        [
            'Bir lise FIRST Robotics takımı, robotun kol mekanizmasını son güne bırakmıştı. '
            'Yarışma sabahı kol çalışmadı. Kural gereği robotla sahaya çıkmak zorundaydılar '
            '— ve sıfır puan aldılar. Takım hüzünle eve döndü.',
            'Ama ertesi yıl o ekip, tarihlerinin en güçlü kolunu tasarladı; çünkü neyin '
            'işe yaramadığını tam olarak biliyorlardı.',
        ],
        'Mesaj: "Ne öğrendik?" sorusu, "ne kaybettik?" sorusunun önüne geçmelidir.'))

    return e


# ============================================================
# BÖLÜM 8 — ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ZOR SORULAR')

    qas = [
        ('STEAM\'de Sanat neden var? Teknik disiplinler yeterli değil mi?',
         'İnsanlar teknik çözümleri estetik, anlaşılabilirlik ve kullanım kolaylığı '
         'kararlarına göre benimser ya da reddeder. iPhone\'un yükselişi, Blackberry\'nin '
         'düşüşü — biri teknik olarak daha sağlamdı ama biri insan odaklı tasarlandı. '
         'Sanat, "bu çalışıyor mu?" sorusuna değil "insan bunu benimser mi?" sorusuna '
         'cevap verir.'),
        ('Beyin fırtınasında ortaya çıkan fikirlerin çoğu uygulanamaz — zaman kaybı değil mi?',
         'Beyin fırtınasının değeri "uygulanabilir fikirler üretmek" değil; "alışılmış '
         'düşüncenin dışına çıkmak"tır. Araştırmalar, yaratıcı çözümlerin genellikle beyin '
         'fırtınasının sonunda gelen "garip" fikirlerin uyarlanmasından çıktığını gösteriyor. '
         'Eleme sonra yapılır; üretim aşamasında her fikir değerlidir.'),
        ('Grubun en iyi öğrencisi lider olursa proje daha başarılı olmaz mı?',
         'Liderlik akademik başarıyla aynı şey değildir. Grupların farklı STEAM rollere '
         'ihtiyacı var: araştırmacı, yapımcı, tasarımcı, sunucu. Akademik açıdan ortalama '
         'bir öğrenci harika bir organize edici ya da sunucu olabilir. Rolü başarıya göre '
         'belirlemek hem adil değil hem de projeyi yavaşlatır.'),
        ('Prototip başarısız olursa öğrenci ne hisseder? Motivasyon düşmez mi?',
         'Düşebilir — ama bu motivasyon düşüşü "başarısızlık kaçınılmaz" görüldüğünde '
         'değil, "başarısızlık utanç verici" görüldüğünde olur. Öğretmenin görevi, '
         'başarısızlığı sürecin beklenen ve değerli bir parçası olarak konumlandırmaktır. '
         '"Ne öğrendik?" sorusu, "ne kaybettik?" sorusunun önüne geçmelidir.'),
        ('STEAM projesi için bir problem nasıl "iyi" veya "kötü" olur?',
         'İyi problem: gerçek ve gözlemlenebilir; birden fazla STEAM bileşenini gerektirir; '
         'atölye koşullarında çözülebilir ölçektedir; birden fazla çözüm yolu vardır. '
         'Kötü problem: çok geniş ("dünya açlığını çöz"), tamamen teknik ("motor tasarla"), '
         'ya da dışarıdan empoze edilmiş ("ben böyle istedim").'),
        ('Bir STEAM projesinde birden fazla "doğru" çözüm olabilir mi?',
         'Evet — ve bu, STEAM\'i geleneksel fen dersinden ayıran en temel özelliklerden '
         'biridir. Matematik probleminin genellikle tek cevabı vardır; mühendislik '
         'probleminin çok sayıda kabul edilebilir çözümü vardır. Sınıftaki farklı '
         'grupların aynı probleme farklı çözümler üretmesi bir tutarsızlık değil, '
         'bir zenginliktir.'),
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
        title='8. Unite - Ogretmen Hazirlik Rehberi',
        author='Teknoloji ve Tasarim Ogretim Programi',
    )
    doc.unite_info = UI
    doc.doc_title  = 'Ünite İçeriği Hazırlık Materyali'

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
    print('OK  U8_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
