# -*- coding: utf-8 -*-
"""
7. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit7/U7_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite7_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit7')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U7_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '7. Ünite - Enerjinin Dönüşümü ve Tasarım'
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
        'Bu ünitenin temel kavramları — enerji türleri, enerji dönüşümü, fosil yakıtlar, '
        'yenilenebilir enerji, küresel ısınma, enerji verimliliği, karbon ayak izi — '
        'günlük hayatın her alanını doğrudan ilgilendiren kavramlardır.', S_BD))

    # 1.1 Enerji ve türleri
    e.append(Paragraph('1.1 Enerji ve Enerji Türleri', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Enerji, iş yapabilme kapasitesidir. SI birimi Joule (J); günlük '
        'pratikte kilowatt-saat (kWh) kullanılır. 1 kWh = 3.600.000 J.', S_BD))

    enerji_data = [
        [Paragraph('Enerji Türü', S_TH), Paragraph('Tanım', S_TH), Paragraph('Günlük Örnek', S_TH)],
        [Paragraph('Kinetik', S_TC),
         Paragraph('Hareket eden cismin enerjisi', S_TC),
         Paragraph('Akan nehir, koşan atlet', S_TC)],
        [Paragraph('Potansiyel', S_TC),
         Paragraph('Konumdan ya da şekilden gelen enerji', S_TC),
         Paragraph('Tepedeki taş, gerilmiş yay', S_TC)],
        [Paragraph('Isı', S_TC),
         Paragraph('Moleküllerin rastgele hareketinden kaynaklanan enerji', S_TC),
         Paragraph('Ateş, güneş ışınları', S_TC)],
        [Paragraph('Işık', S_TC),
         Paragraph('Elektromanyetik dalga enerjisi', S_TC),
         Paragraph('Ampul, güneş', S_TC)],
        [Paragraph('Kimyasal', S_TC),
         Paragraph('Kimyasal bağlarda depolanmış enerji', S_TC),
         Paragraph('Pil, benzin, yediklerimiz', S_TC)],
        [Paragraph('Elektrik', S_TC),
         Paragraph('Elektron akışından kaynaklanan enerji', S_TC),
         Paragraph('Prize takılı cihaz', S_TC)],
        [Paragraph('Ses', S_TC),
         Paragraph('Ortamda yayılan titreşim enerjisi', S_TC),
         Paragraph('Hoparlör, konuşma', S_TC)],
    ]
    enerji_t = Table(enerji_data, colWidths=[CW*0.18, CW*0.43, CW*0.39])
    enerji_t.setStyle(TableStyle([
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
    e.append(KeepTogether([enerji_t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> Öğrenciler "enerji = elektrik" yanılgısına sık düşer. '
        'Elektrik yalnızca bir enerji taşıma biçimidir, birincil kaynak değildir.', S_NOT))

    # 1.2 Enerji Dönüşümü
    e.append(Paragraph('1.2 Enerji Dönüşümü ve Korunumu', S_H2))
    e.append(bilgi_kutusu(
        'Enerjinin Korunumu Yasası (Birinci Termodinamik Yasa)',
        ['Enerji yoktan var edilemez, var olan yok edilemez; yalnızca bir türden diğerine '
         'dönüşür. Tüm evrendeki toplam enerji miktarı sabittir.',
         'Dönüşüm zinciri örneği: Kömür (kimyasal) → Buhar (ısı) → Türbin (kinetik) '
         '→ Jeneratör (elektrik) → Ampul (ışık + ısı)',
         'Verimlilik: Her dönüşümde bir miktar enerji kullanılamaz ısıya dönüşür. '
         'Akkor ampulde elektriğin %95\'i ısıya gider; LED\'de bu oran %10\'a düşer.']))

    # 1.3 Fosil Yakıtlar
    e.append(Paragraph('1.3 Fosil Yakıtlar: Geçmişin Enerjisi', S_H2))
    e.append(Paragraph(
        'Milyonlarca yıl önce yaşamış canlıların kalıntılarının yüksek basınç ve sıcaklık '
        'altında dönüşümüyle oluştu. Bir defaya mahsus kaynak — tüketilince yenilenemez.', S_BD))
    fosil_liste = [
        '<b>Kömür:</b> En eski fosil yakıt, en fazla CO2 salan. Türkiye\'de linyit '
        'rezervleri var ama verimsiz.',
        '<b>Petrol:</b> Ulaşım ve petrokimya sanayisinin omurgası. Türkiye\'nin büyük '
        'petrol rezervi yok — enerji bağımlılığının temel nedeni.',
        '<b>Doğalgaz:</b> Daha az kirletici ama hâlâ fosil. Türkiye\'nin büyük bölümünü '
        'ısıtıyor; çoğu Rusya ve İran\'dan ithal ediliyor.',
    ]
    for f in fosil_liste:
        e.append(Paragraph(f'• {f}', S_BUL))
    e.append(Paragraph(
        '<b>Bağlam:</b> Küresel enerji tüketiminin yaklaşık %80\'i hâlâ fosil yakıtlardan '
        'sağlanıyor (2023). Dönüşüm oluyor, ama yavaş.', S_BD))

    # 1.4 Yenilenebilir Enerji
    e.append(Paragraph('1.4 Yenilenebilir Enerji Kaynakları', S_H2))
    e.append(Paragraph(
        'Doğal süreçlerle sürekli yenilenen, tükenmez kaynaklardır.', S_BD))
    yen_liste = [
        '<b>Güneş:</b> Türkiye yılda ortalama 2.737 saatlik güneşlenmeyle Avrupa\'nın '
        'en şanslı ülkelerinden. PV hücreler ışığı doğrudan elektriğe çevirir.',
        '<b>Rüzgar:</b> Türkiye\'nin rüzgar kapasitesi son 15 yılda 10 kattan fazla arttı. '
        'Ege kıyıları ve İç Anadolu platolarının potansiyeli yüksek.',
        '<b>Hidroelektrik:</b> Mevcut yenilenebilir enerji içinde en büyük pay. '
        'Atatürk, Karakaya, Keban barajları büyük kapasiteli üretim merkezleri.',
        '<b>Jeotermal:</b> Türkiye dünyada jeotermal kapasitede dördüncü büyük ülke. '
        'Denizli (Sarayköy), Aydın, Manisa önde gelen merkezler.',
        '<b>Biyokütle:</b> Organik atıklardan (tarım artıkları, orman atıkları, belediye '
        'çöpleri) enerji üretimi. Türkiye\'de henüz gelişmekte olan bir alan.',
    ]
    for y in yen_liste:
        e.append(Paragraph(f'• {y}', S_BUL))

    # 1.5 Küresel Isınma
    e.append(Paragraph('1.5 Küresel Isınma ve Sera Etkisi', S_H2))
    e.append(Paragraph(
        '<b>Sera etkisi nedir?</b> Güneş ışınları atmosferi geçip yere ulaşır. Yüzeyden '
        'yansıyan ısı geri uzaya çıkmak ister; ama CO2, CH4 ve N2O gibi sera gazları bu '
        'ısıyı tutarak atmosferi ısıtır. Fosil yakıt kullanımı bu gazların yoğunlaşmasını '
        'hızlandırmıştır.', S_BD))
    e.append(bilgi_kutusu(
        'Temel Veriler',
        ['Endüstri öncesi CO2: 280 ppm → Bugün: 420+ ppm (2023)',
         '1850\'den bu yana ortalama küresel sıcaklık artışı: yaklaşık 1,1°C',
         'Paris Anlaşması hedefi: 2100\'e kadar 2°C altında, tercihen 1,5°C altında',
         'Türkiye özelinde etkiler: Akdeniz ve Ege\'de kuraklık riski artıyor; '
         'orman yangınları daha sık ve şiddetli; kıyı erozyonu hızlanıyor.']))

    # 1.6 Enerji Verimliliği
    e.append(Paragraph('1.6 Enerji Verimliliği', S_H2))
    e.append(Paragraph(
        'Aynı işi, daha az enerji harcayarak yapmak. "Temiz enerji üretmek kadar, '
        'harcanan enerjiyi azaltmak da önemlidir."', S_BD))
    verim_liste = [
        'Akkor ampul: %5 verimli (elektriğin %95\'i ısıya gidiyor)',
        'LED ampul: %80–90 verimli',
        'A+++ beyaz eşya etiketleri: aynı işi en az enerjiyle yapıyor',
        'Pasif ev tasarımı: Güneye bakan pencereler, kalın yalıtım, ısı değiştiriciler',
    ]
    for v in verim_liste:
        e.append(Paragraph(f'• {v}', S_BUL))
    e.append(Paragraph(
        '<b>Tasarım bağlantısı:</b> Enerji verimliliği bir mühendislik hedefidir; ama aynı '
        'zamanda bir tasarım kararıdır. "Bu ürün en az enerjiyle en iyi işlevi nasıl sunar?" '
        'sorusu bu ünitenin tasarım sorusudur.', S_NOT))

    # 1.7 Karbon Ayak İzi
    e.append(Paragraph('1.7 Karbon Ayak İzi', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Bir birey, kurum veya ürünün faaliyetleri sonucunda atmosfere salınan '
        'CO2 ve eşdeğeri sera gazı miktarı. Birimi: ton CO2 eşdeğeri (tCO2e). '
        'Türkiye ortalaması kişi başı yıllık yaklaşık 5–6 ton CO2e.', S_BD))
    karbon_liste = [
        '<b>Ulaşım:</b> Özellikle fosil yakıtlı araç kullanımı',
        '<b>Konut:</b> Doğalgaz ısıtma, elektrik tüketimi',
        '<b>Beslenme:</b> Kırmızı et üretiminin metan salınımı',
        '<b>Satın alma:</b> Her ürünün üretim ve taşıma sürecinde "gömülü karbon" vardır',
    ]
    for k in karbon_liste:
        e.append(Paragraph(f'• {k}', S_BUL))
    e.append(Paragraph(
        '<b>Pedagojik not:</b> Bireysel sorumluluk önemli, ama öğrencilere yalnızca bireysel '
        'çözümleri dayatmak yanıltıcıdır. Sistemik dönüşüm (enerji politikası, sanayi) '
        'en büyük payı oluşturur.', S_NOT))

    return e


# ============================================================
# BÖLÜM 2 — TARİHSEL ARKA PLAN
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TARİHSEL ARKA PLAN')
    e.append(Paragraph(
        'Enerji tarihi, teknoloji tarihiyle iç içe geçmiştir. Her büyük enerji dönüşümü '
        'hem ekonomik hem siyasi hem de çevresel bir dönüşümü beraberinde getirmiştir.', S_BD))

    # 2.1 Faraday
    e.append(Paragraph('2.1 Faraday: Ciltçi Çırağının Keşfi (1831)', S_H2))
    e.append(Paragraph(
        'Michael Faraday, 14 yaşında bir ciltçinin yanında çırak olarak işe başladı. '
        'Kendi kendini yetiştirdi. 1831\'de bir mıknatısı bakır tel sarmalına soktuğunda '
        'galvanometre ibresi kıpırdadı. Hareketin elektriği üretebileceğini kanıtlamıştı.', S_BD))
    e.append(Paragraph(
        'Tüm jeneratörler, tüm elektrik santralleri, tüm hidroelektrik barajlar — '
        'hepsi sonunda dönen bir şeyden elektrik üretiyor. Faraday hiç üniversiteye '
        'gitmedi. Merak yeterliydi.', S_BD))

    # 2.2 Edison ve Tesla
    e.append(Paragraph('2.2 Edison ve Tesla: Akım Savaşı (1880\'ler–1890\'lar)', S_H2))
    e.append(Paragraph(
        'Thomas Edison 1882\'de New York\'ta dünyanın ilk ticari elektrik santralini kurdu. '
        'Doğru akım (DC) kısa mesafelerde çalışıyordu; ama şehir geneline yaymak pahalıydı. '
        'Nikola Tesla, George Westinghouse için alternatif akım (AC) sistemini geliştirdi. '
        'AC, transformatörler aracılığıyla yüksek voltajda uzun mesafelere iletilebiliyordu.', S_BD))
    e.append(Paragraph(
        'Edison, AC\'yi "ölümcül" ilan eden kampanyalar yaptı. Ama fizik pazarlama '
        'stratejisine galip geldi. Bugün Türkiye\'nin şebekesinde akan elektrik '
        'Tesla\'nın AC standardındadır.', S_BD))

    # 2.3 Petrol ve OPEC
    e.append(Paragraph('2.3 Petrolün Keşfi ve 1973 Krizi', S_H2))
    e.append(Paragraph(
        '1859\'da Edwin Drake Pennsylvania\'da dünyanın ilk ticari petrol kuyusunu açtı. '
        'Petrol; ulaşım, sanayi ve günlük hayatı kökten değiştirdi. Ama 1973\'te OPEC '
        'petrol ambargosu bu bağımlılığın ne kadar tehlikeli olduğunu gösterdi.', S_BD))
    e.append(bilgi_kutusu(
        '1973 Petrol Krizi: Arabsız Pazar Günleri',
        ['OPEC petrol ihracatını kesti. Petrol fiyatı 3 ayda 4 katına çıktı.',
         'Avrupa\'da "arabsız Pazar" günleri ilan edildi; otoyollar bomboştu.',
         'Bu kriz yenilenebilir enerji araştırmalarını, Almanya\'da ev yalıtımı '
         'standartlarını, Japonya\'da yakıt tasarruflu araç üretimini başlattı.',
         'Bir enerji krizi, geleceğin dönüşümünün fitilini ateşleyebilir.']))

    # 2.4 Chernobyl
    e.append(Paragraph('2.4 Chernobyl: Bir Kazanın Siyasi Sonuçları (1986)', S_H2))
    e.append(Paragraph(
        '26 Nisan 1986\'da Sovyetler Birliği\'ndeki Reaktör 4 patladı. '
        '350.000 kişi tahliye edildi. Radyasyon Avrupa\'ya yayıldı. '
        'Sovyet yönetiminin ilk gizleme girişimleri öteki ülkelerin '
        'ölçüm cihazlarıyla ifşa oldu.', S_BD))
    e.append(Paragraph(
        'Bu kaza nükleer enerjiye kamuoyu güvenini sarsdı. Almanya "nükleer çıkış" '
        'sürecine girdi. Yenilenebilir enerji savunuculuğu ivme kazandı.', S_BD))

    # 2.5 Paris Anlaşması
    e.append(Paragraph('2.5 Paris Anlaşması: İklim Diplomasisinin Kilometre Taşı (2015)', S_H2))
    e.append(Paragraph(
        'Aralık 2015\'te 195 ülke şu hedefi belirledi: Küresel sıcaklık artışını '
        '2100\'e kadar 2°C altında tutmak; tercihen 1,5°C\'de sınırlamak. '
        'İlk kez hem gelişmiş hem gelişmekte olan ülkeler aynı çatı altında '
        'iklim taahhüdü verdi.', S_BD))
    e.append(Paragraph(
        '<b>Sınırlılığı:</b> Ülkelerin ulusal katkı hedefleri gönüllülük esasına dayalı; '
        'uygulama denetimi zayıf. Ama anlaşmanın sembolik ve siyasi gücü büyük: '
        'fosil yakıtlardan çıkış söylemi artık tartışma konusu değil.', S_BD))

    # 2.6 Türkiye
    e.append(Paragraph('2.6 Türkiye\'nin Enerji Dönüşümü', S_H2))
    e.append(Paragraph(
        'Türkiye elektriğinin yaklaşık %55\'ini fosil yakıtlardan, %45\'ini yenilenebilir '
        'kaynaklardan sağlıyor (2023). Son 15 yılda rüzgar ve güneş kapasitesi '
        'dramatik biçimde arttı; ancak enerji ithalatı hâlâ ciddi bir döviz çıkışına '
        'yol açıyor.', S_BD))
    turk_liste = [
        '2000: Alaçatı\'da Türkiye\'nin ilk rüzgar çiftliği',
        '2010: Jeotermal elektrik üretiminde hızlı büyüme başladı',
        '2023: Güneş paneli kurulu kapasitesi 10 GW\'ı aştı',
        '2024: Akkuyu Nükleer Santrali\'nde ilk reaktör devreye alındı',
    ]
    for t in turk_liste:
        e.append(Paragraph(f'• {t}', S_BUL))

    return e


# ============================================================
# BÖLÜM 3 — KRONOLOJİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'ENERJİ TARİHİNİN KRONOLOJİSİ')

    kron_data = [
        [Paragraph('Yıl', S_TH), Paragraph('Olay', S_TH)],
        [Paragraph('1831', S_TC), Paragraph('Faraday elektromanyetik indüksiyonu keşfetti — modern jeneratörlerin temeli', S_TC)],
        [Paragraph('1859', S_TC), Paragraph('Edwin Drake Titusville\'de dünyanın ilk ticari petrol kuyusunu açtı', S_TC)],
        [Paragraph('1882', S_TC), Paragraph('Edison New York\'ta ilk ticari elektrik santralini kurdu', S_TC)],
        [Paragraph('1888', S_TC), Paragraph('Tesla AC motor patentini aldı — bugünkü şebeke sisteminin temeli', S_TC)],
        [Paragraph('1954', S_TC), Paragraph('Bell Laboratuvarları ilk pratik fotovoltaik güneş pilini geliştirdi', S_TC)],
        [Paragraph('1973', S_TC), Paragraph('OPEC petrol ambargosu — yenilenebilir enerji araştırmalarını hızlandırdı', S_TC)],
        [Paragraph('1986', S_TC), Paragraph('Chernobyl nükleer felaketi — nükleer enerjiye küresel güven sarsıldı', S_TC)],
        [Paragraph('1992', S_TC), Paragraph('BM İklim Değişikliği Çerçeve Sözleşmesi imzalandı (Rio Zirvesi)', S_TC)],
        [Paragraph('1997', S_TC), Paragraph('Kyoto Protokolü — gelişmiş ülkelere CO2 azaltım hedefi', S_TC)],
        [Paragraph('2000', S_TC), Paragraph('Türkiye\'de ilk rüzgar çiftliği (Çeşme-Alaçatı)', S_TC)],
        [Paragraph('2011', S_TC), Paragraph('Fukushima nükleer kazası — Japonya ve Almanya politika dönüşümü', S_TC)],
        [Paragraph('2015', S_TC), Paragraph('Paris Anlaşması — 195 ülke 2°C hedefini benimsedi', S_TC)],
        [Paragraph('2020', S_TC), Paragraph('Yenilenebilir enerji küresel elektriğin %29\'unu sağladı (IEA)', S_TC)],
        [Paragraph('2023', S_TC), Paragraph('Türkiye\'de güneş kurulu kapasitesi 10 GW\'ı aştı', S_TC)],
    ]
    kron_t = Table(kron_data, colWidths=[CW*0.10, CW*0.90])
    kron_t.setStyle(TableStyle([
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
    e.append(kron_t)
    return e


# ============================================================
# BÖLÜM 4 — GÜNCEL DURUM
# ============================================================

def bolum4():
    e = []
    e += bolum_baslik(4, 'GÜNCEL DURUM: ENERJİ BUGÜN NEREDE?')

    e.append(Paragraph('4.1 Yenilenebilir Enerji Artık En Ucuz', S_H2))
    e.append(Paragraph(
        'IEA verilerine göre 2023\'te yeni kurulu güneş ve rüzgar santralleri çoğu '
        'bölgede yeni kömür veya doğalgaz santrallerinden daha ucuza elektrik üretiyor. '
        'Teknoloji maliyeti son 10 yılda güneş panelinde %90, rüzgar türbininde %70 '
        'düştü.', S_BD))

    e.append(Paragraph('4.2 Büyük Bataryalar: Depolama Sorununun Çözümü', S_H2))
    e.append(Paragraph(
        'Güneş gece, rüzgar sakin havalarda enerji üretemez. Bu "aralıklılık" sorunu '
        'yenilenebilir enerjinin en büyük kısıtıydı. Büyük ölçekli lityum-iyon pil '
        'depoları artık devreye giriyor. 2017\'de Avustralya\'ya kurulan büyük ölçekli '
        'batarya sistemi, şebeke stabilitesinde bir dönüm noktası oldu.', S_BD))

    e.append(Paragraph('4.3 Hidrojen Enerjisi', S_H2))
    e.append(Paragraph(
        'Fazla üretilen yenilenebilir elektrikle su ayrıştırılarak elde edilen "yeşil '
        'hidrojen" bir sonraki büyük adım olarak görülüyor. Türkiye\'nin güneş ve rüzgar '
        'potansiyelinin hidrojen üretimine dönüştürülmesi aktif olarak tartışılıyor; '
        'hidrojen Avrupa\'ya ihraç edilebilir.', S_BD))

    e.append(Paragraph('4.4 Türkiye\'nin Yenilenebilir Enerji Hedefleri', S_H2))
    hedef_liste = [
        '2035\'te toplam elektriğin %60\'ını yenilenebilir kaynaklardan sağlamak',
        'Deniz üstü rüzgar enerjisine ilk adımlar (Kuzey Ege)',
        'Güneş paneli yerli üretim kapasitesi oluşturma',
        'Jeotermal kapasitesini artırma (Ege ve Akdeniz bölgeleri)',
    ]
    for h in hedef_liste:
        e.append(Paragraph(f'• {h}', S_BUL))

    return e


# ============================================================
# BÖLÜM 5 — DİSİPLİNLERARASI BAĞLANTI
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'DİSİPLİNLERARASI BAĞLANTILAR')

    e.append(Paragraph('5.1 Fen Bilgisi: Enerji, Fizik ve Kimya', S_H2))
    fen_liste = [
        '<b>Fizik:</b> Enerji türleri ve dönüşümü, kinetik-potansiyel enerji ilişkisi, '
        'verimlilik hesabı — fen dersiyle doğrudan örtüşür',
        '<b>Kimya:</b> Fosil yakıtların yanma reaksiyonları, CO2 oluşumu, '
        'fotosentez ve depolanmış kimyasal enerji',
        '<b>Çevre bilimi:</b> Sera etkisi, küresel ısınma süreci, iklim modelleri',
    ]
    for f in fen_liste:
        e.append(Paragraph(f'• {f}', S_BUL))
    e.append(Paragraph(
        '<b>İşbirliği önerisi:</b> ÇK1 Enerji Dönüşüm Zinciri\'ni fen öğretmeniyle '
        'birlikte değerlendirin.', S_NOT))

    e.append(Paragraph('5.2 Matematik: Hesap, Grafik ve İstatistik', S_H2))
    mat_liste = [
        '<b>kWh hesabı:</b> Güç (W) × Süre (saat) = Enerji (Wh). '
        'ÇK4 Evimde Enerji Analizi\'nde doğrudan uygulanır.',
        '<b>Grafik okuma:</b> Türkiye\'nin enerji karmasını gösteren pasta ve çubuk '
        'grafikler — oran ve yüzde hesabı',
        '<b>İstatistik:</b> Sınıfın enerji tüketimi ortalaması; en yüksek ve en düşük '
        'tüketici karşılaştırması',
    ]
    for m in mat_liste:
        e.append(Paragraph(f'• {m}', S_BUL))

    e.append(Paragraph('5.3 Sosyal Bilgiler: Politika, Ekonomi, Çevre', S_H2))
    sos_liste = [
        'Küresel ısınma ve çevre sorunları — ÇK5 ile doğrudan bağlanır',
        'Türkiye\'nin enerji bağımlılığı ve döviz maliyeti',
        'Sürdürülebilir kalkınma hedefleri (SDG 7: Erişilebilir ve Temiz Enerji)',
        'Paris Anlaşması ve ülkelerin taahhütleri — jeopolitik tartışma',
    ]
    for s in sos_liste:
        e.append(Paragraph(f'• {s}', S_BUL))

    e.append(Paragraph('5.4 Görsel Sanatlar ve Tasarım', S_H2))
    e.append(Paragraph(
        'ÇK7 Tasarım Planlama Formu eskizlerinde görsel sanatlar öğretmeni geri '
        'bildirimi; prototip sunum kartının görsel düzeni; galeri sergisi için '
        'ürün etiketlerinin estetik tasarımı.', S_BD))

    return e


# ============================================================
# BÖLÜM 6 — YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI
# ============================================================

def bolum6():
    e = []
    e += bolum_baslik(6, 'YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI')
    e.append(Paragraph(
        'Aşağıdaki yanlış anlamalar öğrencilerin büyük çoğunluğunda görülür. Bunları '
        '"tuzak soru" olarak kullanabilir ya da akışta düzeltme fırsatı çıktığında '
        'hazırlıklı olabilirsiniz.', S_BD))

    yanlis = [
        ('"Enerji = Elektrik"',
         'Elektrik yalnızca bir enerji taşıma biçimidir; kinetik, ısı, kimyasal vb. '
         'pek çok enerji türü vardır'),
        ('"Enerji bitebilir"',
         'Enerjinin korunumu yasasına göre enerji yalnızca dönüşür — bazı kaynaklar '
         'tükenir, ama enerji yok olmaz'),
        ('"Yenilenebilir enerji ücretsizdir"',
         'Kaynak (güneş, rüzgar) ücretsizdir; ama panel, türbin, altyapı ciddi yatırım '
         'gerektirir; yaşam döngüsü maliyeti hesaplanmalıdır'),
        ('"Nükleer enerji yenilenebilirdir"',
         'Nükleer enerji düşük karbonludur ama yenilenemez; uranyum yakıtı '
         'sınırlı bir kaynaktır'),
        ('"Bireysel tercihler iklim krizini çözer"',
         'Bireysel sorumluluk önemli; ama küresel emisyonların büyük bölümü sanayi '
         've enerji sisteminden kaynaklanır — sistemik dönüşüm zorunludur'),
        ('"Güneş paneli her yerde aynı işe yarar"',
         'Güneş enerjisi potansiyeli iklim ve coğrafyaya göre değişir; aynı panel '
         'Muğla\'da İskandinavya\'ya göre 3 kat fazla enerji üretir'),
        ('"Elektrikli araç sıfır emisyon üretir"',
         'Kullanım aşamasında evet; ama batarya üretiminde ve şarj edildiği elektriğin '
         'kaynağına göre dolaylı emisyon oluşur'),
        ('"Fosil yakıtları kullanmak suçtur"',
         'Fosil yakıtlara olan bağımlılık milyarlarca insanın hayatını sürdürmesine '
         'yardımcı oldu; sorun geçiş sürecinin yönetimidir, bireysel suçlama değil'),
    ]

    y_data = [[Paragraph('Yaygın Yanlış Anlama', S_TH), Paragraph('Doğrusu', S_TH)]]
    for yan, duz in yanlis:
        y_data.append([Paragraph(yan, S_TCB), Paragraph(duz, S_TC)])

    y_t = Table(y_data, colWidths=[CW*0.35, CW*0.65])
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
        'ilgili kavramlara bağlanarak ders akışına doğal biçimde yerleştirilebilir.', S_BD))

    e.append(hikaye(
        'Ciltçi Çırağının Değişen Dünyası: Faraday\'ın Deneyi',
        ['Michael Faraday 14 yaşında bir ciltçinin yanında çırak oldu. Kendi kendini '
         'yetiştirdi. 1831\'de at nalı mıknatısını bakır tel sarmalına sokuşturduğunda '
         'galvanometre ibresi kıpırdadı. Küçük bir kıpırdama.',
         'Ama onun anlamı şuydu: Hareket, elektriği üretebilir. Tüm jeneratörler bu '
         'prensiple çalışır. Barajlardaki türbinler, rüzgar çiftlikleri, nükleer '
         'santraller — hepsi sonunda dönen bir şeyden elektrik üretiyor.',
         'Faraday\'ın 1831\'deki o küçük deneyi, her gece evinizde açtığınız ışığın '
         'atasıdır. Faraday hiç üniversiteye gitmedi. Merak yeterliydi.'],
        'Bağlantı: Enerji dönüşümü kavramına giriş — hareket enerjisinin elektriğe '
        'dönüşümünün temeli.'))

    e.append(hikaye(
        'Arabsız Pazar: 1973 Petrol Krizi',
        ['Ekim 1973, Almanya. Motorlu araçlar yalnızca görevliler, doktorlar ve '
         'itfaiye için izinliydi. Otoyollar bomboş. Bisikletliler, yayalar. '
         'Tüm bunun nedeni Orta Doğu\'da başlayan bir petrol ambargosu.',
         'OPEC ülkeleri Batı\'ya petrol ihracatını kesti. Petrol fiyatı 3 ayda 4 '
         'katına çıktı. "Ucuz ve sonsuz enerji" yanılsaması dağıldı.',
         'Bu kriz yenilenebilir enerji araştırmalarını, Almanya\'da ev yalıtımı '
         'standartlarını, Japonya\'da yakıt tasarruflu araç üretimini başlattı. '
         'Bir kriz, bir dönüşümün fitilini ateşledi.'],
        'Bağlantı: Yenilenebilir enerji gereklilik olarak değil, kriz tepkisi olarak '
        'doğdu — bu bağlam öğrenciler için güçlü bir motivasyon kaynağıdır.'))

    e.append(hikaye(
        'Tesla ve Edison\'ın Akım Savaşı',
        ['1880\'lerin New York\'unda iki vizyoner karşı karşıyaydı. Thomas Edison\'un '
         'DC sistemi çalışıyordu — ama kısa mesafelerde. Nikola Tesla\'nın AC sistemi '
         'transformatörler aracılığıyla şehre yayılabilirdi.',
         'Edison, Tesla\'yı sabote etmek için her yola başvurdu. AC\'yi "ölümcül" ilan '
         'etti. Ama fizik pazarlama stratejisine galip geldi. AC daha pratikti.',
         'Bugün Türkiye\'nin şebekesinde akan elektrik Tesla\'nın AC standardındadır. '
         'Edison\'ın adı ampule takıldı — Tesla\'nın adı ise elektrikli arabanın en '
         'büyük şirketine.'],
        'Bağlantı: Enerji altyapısı kararları teknik değil, aynı zamanda ekonomik ve '
        'siyasi kararlardır.'))

    e.append(hikaye(
        'Chernobyl: Gizlenen Kaza, İfşa Olan Sistem',
        ['26 Nisan 1986 gecesi Sovyetler Birliği\'ndeki Reaktör 4 patladı. İlk resmi '
         'açıklama bir gün bekletildi; şehir saatlerce tahliye edilmedi. 350.000 kişi '
         'yıllarca sonra tahliye edildi.',
         'Rüzgar radyasyonu Avrupa\'ya taşıdı; diğer ülkelerin ölçüm cihazları '
         'gerçeği ifşa etti. Sovyet sisteminin gizleme girişimleri çöktü.',
         'Bu kaza iki şeyi kökten değiştirdi: Nükleer enerjiye kamuoyu güveni ve '
         'Sovyet sisteminin güvenilirliğine duyulan inancı. İki yıl sonra '
         'Sovyetler Birliği çözülmeye başladı.'],
        'Bağlantı: Enerji altyapısı güvenliği ve şeffaflık ilişkisi; küresel '
        'enerji politikasının siyasi boyutuna giriş.'))

    e.append(hikaye(
        'Bir Köyün Sular Altında Kalması: Barajlar ve İnsan Maliyeti',
        ['Türkiye\'nin Güneydoğu Anadolu Projesi (GAP) kapsamında inşa edilen '
         'Atatürk Barajı 1990\'da dolmaya başladı. Enerji ve sulama için büyük '
         'bir kazanım.',
         'Ama baraj gölü alan içindeki yaklaşık 75 köy ve belde su altında kaldı. '
         'Binlerce aile göç etmek zorunda kaldı. Yüzyıllık tarihsel katmanlar '
         'da sular altında yattı.',
         'Enerji altyapısı her zaman sosyal ve çevresel maliyetler barındırır. '
         '"Yenilenebilir" sıfatı bu maliyetleri ortadan kaldırmaz — '
         'iyi mühendislik kararları bunları hesaba katar.'],
        'Bağlantı: Enerji seçimlerinin sosyal ve çevresel boyutu; '
        '"yeşil" çözümlerin gerçek maliyetini tartışmak için zemin.'))

    e.append(hikaye(
        'Sahara\'dan Avrupa\'ya Işık: DESERTEC\'in Hayal ve Gerçeği',
        ['2009\'da Avrupa\'nın en büyük sanayi şirketleri bir araya geldi ve '
         'çılgınca bir projeyi duyurdu: DESERTEC. Sahra Çölü\'nde devasa güneş '
         'enerji tarlaları kurulacak ve kablolarla Avrupa\'ya enerji aktarılacaktı.',
         '2013\'te büyük şirketler projeyi birer birer terk etti. Yatırım çok büyük, '
         'siyasi riskler çok yüksek.',
         'Ama DESERTEC tam anlamıyla ölmedi. Daha küçük ölçekli projeler hâlâ devam '
         'ediyor; Fas\'tan Portekiz\'e sualtı enerji kablosu projesi 2025\'te onay '
         'aldı. Büyük fikirler genellikle ilk formlarında gerçekleşmez — ama '
         'tohumları kalır.'],
        'Bağlantı: Enerji tasarımında vizyon ve gerçeklik arasındaki denge; '
        'uluslararası enerji iş birliğinin zorlukları.'))

    return e


# ============================================================
# BÖLÜM 8 — ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR')
    e.append(Paragraph(
        'Bazı sorular anında yanıt gerektirmez. "Harika soru — düşünmem lazım" ya da '
        '"Bu konuyu ileride daha ayrıntılı ele alacağız" demek tamamen uygundur.', S_BD))

    qas = [
        ('"Herkes yenilenebilir enerjiye geçse dünya kurtulur mu? Neden bu kadar kolay değil?"',
         'Yenilenebilir enerjiye geçiş zorunlu ve doğru yön — ama tek başına yeterli değil. '
         'Enerji tüketimi de azalmalı (verimlilik). Batarya ve depolama altyapısı kurulmalı. '
         'Fosil yakıt ekonomilerine bağımlı milyarlarca insanın geçiş desteği sağlanmalı. '
         '"Kolay değil" demek "imkânsız" demek değildir — ama dürüst bir tablodur.'),
        ('"Elektrikli araç gerçekten çevreci mi?"',
         'Kullanım aşamasında evet. Ama batarya üretiminde kobalt ve lityum madenciliği ciddi '
         'çevresel sorunlar yaratıyor. Şarj edilen elektriğin kaynağı da önemli: kömür '
         'şebekesiyle şarj edilen araç net avantaj sağlamayabilir. Türkiye\'de şebeke '
         'giderek daha fazla yenilenebilir kaynak içerdiği için elektrikli araç '
         'avantajı artıyor.'),
        ('"Barajlar yenilenebilir enerji mi sayılır? Ekosisteme zarar verdikleri halde?"',
         'Evet, yenilenebilir sayılır — kaynak (su akışı) tükenmez. Ama "yenilenebilir = '
         'çevreci" denkliği doğru değil. Büyük barajlar: göç ettirilen topluluklar, sular '
         'altında kalan ekosistemler, sediment birikimi değişimi gibi ciddi etkilere yol '
         'açabilir. Bazı ülkeler eski barajları yıkarak nehirleri yeniden doğal akışlarına '
         'kavuşturuyor.'),
        ('"Türkiye neden enerji ithal ediyor, doğal kaynağımız yok mu?"',
         'Doğal kaynağımız var — güneş, rüzgar, jeotermal, su. Ama dönüşüm zaman, '
         'yatırım ve altyapı gerektiriyor. Fosil yakıt altyapısı 150 yılda kuruldu; '
         'yenilenebilir dönüşüm onlarca yıl alıyor. Doğalgaz büyük oranda ithal ediliyor — '
         'bu bağımlılığı kırmak hem çevresel hem ekonomik hem jeopolitik önceliktir.'),
        ('"Fosil yakıt şirketleri neden yenilenebilir enerjiye geçmiyor?"',
         'Bazıları geçiyor; bazıları mevcut varlıklarını korumak için geçişi yavaşlatmaya '
         'çalışıyor. Bu bir iş kararı, aynı zamanda siyasi bir süreç. Enerji dönüşümünde '
         '"kimin kazandığı ve kimin kaybettiği" sorusu teknoloji kadar önemlidir. '
         'Hükümetlerin politika kararları bu denklemi belirler.'),
        ('"Öğrencim güneş panelli bir ev tasarladı — bunu nasıl değerlendirmeliyim?"',
         'Bu geniş bir başlangıç. Üç yönlendirici soru sorun: (1) Bu ev nerede? '
         '(iklim ve güneşlenme süresi etkiler), (2) Ne kadar enerji üretmesi gerekiyor? '
         '(tüketim analizi), (3) Yalnızca güneş yeterli mi, karma sistem düşünüldü mü? '
         'ÇK7 Tasarım Planlama Formu bu soruları yapılandırmak için kullanılabilir.'),
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
        title='7. Unite - Ogretmen Hazirlik Rehberi',
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
    print('OK  U7_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
