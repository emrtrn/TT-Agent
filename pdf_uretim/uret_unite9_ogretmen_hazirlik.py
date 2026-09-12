# -*- coding: utf-8 -*-
"""
9. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit9/U9_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite9_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit9')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U9_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '9. Ünite - Yapay Zekâ ve Akıllı Ürünler'
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
        'Bu ünitenin temel kavramları — yapay zekâ, makine öğrenmesi, derin öğrenme, algoritma, '
        'istem mühendisliği, halüsinasyon, akıllı ürün ve etik — hem teknolojik hem de toplumsal '
        'boyutları olan kavramlardır. Öğrencilerin günlük teknoloji deneyimleriyle bu kavramları '
        'ilişkilendirmesi ve eleştirel bir bakış açısı geliştirmesi esas alınır.', S_BD))

    # 1.1 Yapay Zekâ
    e.append(Paragraph('1.1 Yapay Zekâ (YZ)', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Yapay zekâ, normalde insan zekâsı gerektiren görevleri (öğrenme, problem '
        'çözme, algılama, dil anlama, karar verme) gerçekleştirebilen bilgisayar sistemleri ve '
        'algoritmalar bütünüdür.', S_BD))

    yz_tablo = [
        [Paragraph('Kavram', S_TH), Paragraph('Tanım', S_TH), Paragraph('İlişki', S_TH)],
        [Paragraph('Yapay Zekâ (YZ)', S_TCB),
         Paragraph('İnsan benzeri görevleri yapan geniş alan', S_TC),
         Paragraph('En üst çerçeve', S_TC)],
        [Paragraph('Makine Öğrenmesi (MÖ)', S_TCB),
         Paragraph('YZ\'nin, veriden kural öğrenen alt dalı', S_TC),
         Paragraph('YZ içinde', S_TC)],
        [Paragraph('Derin Öğrenme', S_TCB),
         Paragraph('MÖ\'nün, yapay sinir ağlarını kullanan alt dalı', S_TC),
         Paragraph('MÖ içinde', S_TC)],
    ]
    t = Table(yz_tablo, colWidths=[CW*0.25, CW*0.50, CW*0.25])
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
        '<b>Temel döngü:</b> Veri → Model Eğitimi → Çıktı / Tahmin', S_BD))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> "YZ bir şeyi anlıyor mu?" sorusu felsefi bir tartışmadır. '
        'Teknik yanıt: YZ örüntü bulur, anlam inşa etmez. Ama bu sınır giderek bulanıklaşıyor.',
        S_NOT))

    # 1.2 Algoritma ve Model
    e.append(Paragraph('1.2 Algoritma ve Model', S_H2))
    e.append(Paragraph(
        '<b>Algoritma:</b> Belirli bir görevi yerine getirmek için izlenen adım adım talimat '
        'dizisi. Her bilgisayar programı bir algoritmadır; YZ modeli de bir algoritmadır.', S_BD))
    e.append(Paragraph(
        '<b>Model:</b> Veriden öğrenilmiş kurallara sahip, girdi alıp çıktı üreten matematiksel '
        'yapı. "Eğitilmiş" bir model; milyonlarca örneğe dayanan olasılık hesaplamalarıdır.',
        S_BD))
    e.append(Paragraph(
        '<b>Analoji:</b> Bir tarif algoritmadır, deneyimli bir aşçı modeldir. Tarif kurallıdır; '
        'aşçı öğrenilmiş sezgilere göre hareket eder.', S_NOT))

    # 1.3 Veri ve Eğitim Verisi
    e.append(Paragraph('1.3 Veri ve Eğitim Verisi', S_H2))
    e.append(Paragraph(
        '<b>Veri:</b> YZ modellerinin öğrenmesini sağlayan ham malzeme. Resim, metin, ses, '
        'sayı — her türlü yapılandırılmış veya yapılandırılmamış bilgi.', S_BD))
    e.append(Paragraph(
        '<b>Eğitim verisi:</b> Modelin "bu girdi için bu çıktı doğru" şeklinde öğrenmesini '
        'sağlayan etiketlenmiş örnekler. Eğitim verisinin kalitesi ve çeşitliliği modelin '
        'kalitesini doğrudan belirler.', S_BD))
    e.append(bilgi_kutusu(
        'Kritik Nokta: Önyargı (Bias)',
        [
            'Eğitim verisindeki önyargı (bias) modele geçer.',
            'Yalnızca belirli insan türlerinin yüzüyle eğitilmiş bir yüz tanıma sistemi '
            'diğerlerini tanıyamaz — bu teknik hata değil, veri kalitesi sorunudur.',
        ]))

    # 1.4 İstem Mühendisliği
    e.append(Paragraph('1.4 İstem Mühendisliği (Prompt Engineering)', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Üretici YZ araçlarından istenen çıktıyı elde etmek için sorular ve '
        'talimatları optimize etme sanatıdır.', S_BD))
    e.append(Paragraph('<b>İyi istem özellikleri:</b>', S_BD))
    for satir in [
        '<b>Bağlam:</b> Konuyu ve amacı belirtir. ("7. sınıf öğrencisi için...")',
        '<b>Görev:</b> Ne istediğini net ifade eder. ("3 cümlelik özet yaz")',
        '<b>Format:</b> Çıktı biçimini tanımlar. ("Madde madde listele")',
        '<b>Ton:</b> Üslup yönü verir. ("Samimi ve sade bir dille")',
        '<b>Sınır:</b> Neyin istenilmediğini de belirtir. ("Teknik jargon kullanma")',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))
    e.append(Paragraph(
        '<b>Analoji:</b> YZ\'ye sormak, kötü bir tarife göre yemek pişirmek gibidir. '
        'Talimat yetersizse sonuç da yetersiz olur.', S_NOT))

    # 1.5 Halüsinasyon
    e.append(Paragraph('1.5 Halüsinasyon', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Büyük dil modellerinin güvenle ama yanlış bilgi üretmesi durumudur. '
        'Model, istatistiksel olarak "bu bağlama uygun" gelen sözcükleri sıralar — '
        'doğruluğunu kontrol etmeden.', S_BD))
    e.append(Paragraph('<b>Örnek türler:</b>', S_BD))
    for satir in [
        'Var olmayan kaynak veya kitap adı uydurma.',
        'Gerçek kişiler hakkında yanlış bilgi sunma.',
        'Sayısal verileri yanlış hesaplama veya yanlış aktarma.',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))
    e.append(Paragraph(
        '<b>Neden olur?</b> Model "bilmiyor" değil; bilmediğini bilmiyor. Doğrulama mekanizması '
        'yoktur; yalnızca olasılık hesabı vardır.', S_BD))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> Halüsinasyon kavramı, YZ çıktılarını kaynak olarak kullanmanın '
        'neden riskli olduğunu somutlaştırır. "YZ\'nin söylediği = doğru" yanılgısını kırmak '
        'için merkezi bir kavramdır.', S_NOT))

    # 1.6 Akıllı Ürün
    e.append(Paragraph('1.6 Akıllı Ürün', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> İçine gömülü sensörler, yazılım ve bağlantı özellikleri sayesinde '
        'çevresini algılayan, veri işleyen ve kararlar alabilen ya da öğrenebilen nesne veya '
        'sistemdir.', S_BD))
    for satir in [
        '1. <b>Sensörler:</b> Çevreden veri toplar (sıcaklık, hareket, ses, görüntü).',
        '2. <b>İşlemci + Yazılım:</b> Veriyi analiz eder, YZ algoritması çalıştırır.',
        '3. <b>Eylemci/Çıktı:</b> Kararı uygulamaya koyar (ısıtma açar, uyarı gönderir).',
        '4. <b>Bağlantı:</b> İnternete veya diğer cihazlara veri paylaşır.',
    ]:
        e.append(Paragraph(satir, S_IND))
    e.append(Paragraph(
        '<b>Örnekler:</b> Akıllı termostat, akıllı konuşmacı (ses tanıma + dil modeli), '
        'tıbbi tanı yardımcısı, otonom araç sensör sistemi.', S_BD))

    # 1.7 Yapay Zekâ Etiği
    e.append(Paragraph('1.7 Yapay Zekâ Etiği', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> YZ sistemlerinin adil, şeffaf, güvenli ve insan haklarına saygılı '
        'biçimde tasarlanması, geliştirilmesi ve kullanılması üzerine kurallar, ilkeler ve '
        'sorumluluklardır.', S_BD))
    for satir in [
        '<b>Şeffaflık:</b> YZ kararlarının açıklanabilir olması.',
        '<b>Adalet:</b> Önyargısız, tüm gruplara eşit davranma.',
        '<b>Güvenlik:</b> Zararlı çıktıların engellenmesi.',
        '<b>Gizlilik:</b> Kullanıcı verisinin korunması.',
        '<b>İnsan denetimi:</b> Kritik kararların insan gözetiminde kalması.',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))
    e.append(Paragraph(
        '<b>Türkiye bağlamı:</b> Türkiye, 2023 itibarıyla ulusal YZ stratejisi geliştirme '
        'sürecindedir. Öğrenciler bu tartışmanın aktif katılımcısı olabilir.', S_NOT))

    return e


# ============================================================
# BÖLÜM 2 — TARİHSEL ARKA PLAN
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TARİHSEL ARKA PLAN')

    # 2.1 Turing
    e.append(Paragraph('2.1 YZ\'nin Temelleri: Turing\'den Dartmouth\'a (1936–1956)', S_H2))
    e.append(Paragraph(
        'Alan Turing, 1936\'da hesaplama teorisini kurdu ve 1950\'de "Bir makine düşünebilir mi?" '
        'sorusunu sormak için Turing Testi\'ni tanımladı. 1956\'da Dartmouth Konferansı\'nda '
        'John McCarthy, Marvin Minsky ve Claude Shannon bir araya geldi; "Yapay Zekâ" terimi '
        'bu konferansta doğdu.', S_BD))
    e.append(Paragraph(
        'O dönemin iyimserlikleri gerçekleşmedi; "YZ kışı" dönemleri (1970\'ler, 1980\'ler '
        'sonları) umutları frenleydi. Ancak temel kavramlar yerleşmişti.', S_BD))

    # 2.2 Uzman sistemler
    e.append(Paragraph('2.2 Uzman Sistemler ve İkinci Dalga (1980\'ler)', S_H2))
    e.append(Paragraph(
        '1980\'lerde "uzman sistemler" yükseldi: belirli bir alandaki insan uzmanlığını kurallara '
        'döküp bilgisayara kodlayan sistemler. Tıp tanısı (MYCIN), kimya analizi (DENDRAL) bu '
        'dönemin ürünleri. Başarılıydılar ama kırılgandılar: sadece önceden tanımlanmış kurallar '
        'çerçevesinde çalışıyorlardı.', S_BD))

    # 2.3 Makine Öğrenmesi
    e.append(Paragraph('2.3 Makine Öğrenmesinin Yükselişi (1990\'lar–2000\'ler)', S_H2))
    e.append(Paragraph(
        '1990\'larda kural tabanlı yaklaşımın sınırları görüldü. Araştırmacılar "kuralları insan '
        'yazar" yerine "makine veriden öğrenir" paradigmasına geçti. 1997\'de IBM\'in Deep Blue '
        'satranç bilgisayarı Dünya Şampiyonu Kasparov\'u yendi — ancak bu brute-force hesaplamayı '
        'temsil ediyordu.', S_BD))
    e.append(Paragraph(
        '2006\'da Geoffrey Hinton derin sinir ağlarının eğitilebileceğini gösterdi. '
        'Derin öğrenme çağı başladı.', S_BD))

    # 2.4 Derin Öğrenme
    e.append(Paragraph('2.4 Derin Öğrenme Devrimi (2012–2017)', S_H2))
    e.append(Paragraph(
        '2012\'de AlexNet modeli, ImageNet görüntü tanıma yarışmasında hata oranını dramatik '
        'biçimde düşürdü: insan benzeri görüntü tanıma artık mümkündü. Bu kırılma noktasından '
        'sonra YZ araştırmaları hızla büyüdü.', S_BD))
    e.append(bilgi_kutusu(
        'AlphaGo: Go\'da İnsan Sezgisini Geçmek (2016)',
        [
            '2016\'da Google DeepMind\'ın AlphaGo programı, Go oyununda dünya şampiyonu '
            'Lee Sedol\'u 4-1 yendi. Go, satranç\'tan çok daha karmaşıktır.',
            'AlphaGo, insan oyuncuların yüzyıllardır geliştirdiği sezgilerin ötesine geçen '
            'hamleler yaptı. "YZ yalnızca kurallar değil, strateji de öğrenebilir" '
            'iddiasının kanıtıydı.',
        ]))

    # 2.5 Büyük Dil Modelleri
    e.append(Paragraph('2.5 Büyük Dil Modelleri ve Üretici YZ (2018–günümüz)', S_H2))
    e.append(Paragraph(
        '2018\'de Google\'ın BERT modeli, 2020\'de OpenAI\'nin GPT-3\'ü büyük dil modellerini '
        '(large language models, LLM) ana akım haline getirdi. 2022\'de ChatGPT\'nin milyonlarca '
        'kullanıcıya ulaşması, YZ\'yi gündelik yaşamın merkezine taşıdı.', S_BD))
    e.append(Paragraph(
        'Üretici YZ (generative AI): metin, görüntü, ses, video üretebilen modeller. Yaratıcı '
        'görevlerdeki insan-makine sınırını yeniden çizdi.', S_BD))

    # 2.6 Türkiye
    e.append(Paragraph('2.6 Türkiye\'de YZ Gelişimi', S_H2))
    e.append(Paragraph(
        'Türkiye, 2021\'de Ulusal Yapay Zekâ Stratejisi\'ni yayımladı (2021–2025). TÜBİTAK '
        'YZ araştırmalarını finanse ediyor; üniversitelerde YZ lisans programları açıldı.', S_BD))
    e.append(Paragraph(
        'Milli Eğitim Bakanlığı 2023 müfredat revizyonunda dijital okuryazarlık ve YZ '
        'farkındalığını ortaokul düzeyine taşıdı — bu ünite o dönüşümün somut '
        'yansımasıdır.', S_BD))

    return e


# ============================================================
# BÖLÜM 3 — KRONOLOJİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'KRONOLOJİ')

    satir_verileri = [
        ('1936', 'Alan Turing hesaplama teorisini kurdu'),
        ('1950', 'Turing Testi tanımlandı: "Bir makine düşünebilir mi?"'),
        ('1956', 'Dartmouth Konferansı: "Yapay Zekâ" terimi doğdu'),
        ('1966', 'ELIZA chatbotu: ilk doğal dil işleme deneyi'),
        ('1980', 'Uzman sistemler dönemi; MYCIN tıp tanısı'),
        ('1997', 'Deep Blue satranç dünya şampiyonu Kasparov\'u yendi'),
        ('2006', 'Geoffrey Hinton derin sinir ağlarının eğitilebileceğini gösterdi'),
        ('2011', 'IBM Watson Jeopardy! yarışmasını kazandı'),
        ('2012', 'AlexNet: derin öğrenme ile görüntü tanımada devrim'),
        ('2016', 'AlphaGo Go oyununda dünya şampiyonunu yendi'),
        ('2017', 'Transformer mimarisi yayımlandı; dil modellerinin temeli'),
        ('2020', 'GPT-3 yayımlandı: 175 milyar parametreli büyük dil modeli'),
        ('2022', 'ChatGPT yayımlandı; 1 ayda 100 milyon kullanıcı'),
        ('2024', 'AB Yapay Zekâ Yasası yürürlüğe girdi'),
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

    e.append(Paragraph('4.1 Üretici YZ ve Gündelik Hayat', S_H2))
    e.append(Paragraph(
        '2024 itibarıyla üretici YZ araçları (ChatGPT, Gemini, Claude, Copilot, Midjourney vb.) '
        'milyarlarca kullanıcı tarafından yazma, araştırma, kodlama, görüntü oluşturma gibi '
        'görevlerde aktif kullanılmaktadır. İş, eğitim ve yaratıcı sektörlerde etkileri '
        'derinleşmektedir.', S_BD))

    e.append(Paragraph('4.2 YZ ve İstihdam', S_H2))
    e.append(Paragraph(
        'YZ, bazı meslekleri dönüştürüyor, bazılarında insan yerini alıyor, bazılarında ise '
        'yeni iş alanları açıyor. McKinsey 2023 raporuna göre küresel iş gücünün %30\'a yakını '
        '2030\'a kadar YZ etkisiyle değişime uğrayabilir.', S_BD))
    for satir in [
        '<b>En çok etkilenen:</b> veri girişi, müşteri hizmetleri, bazı muhasebe görevleri.',
        '<b>En az etkilenen:</b> el becerisine dayalı meslekler, yüksek empati gerektiren işler.',
    ]:
        e.append(Paragraph(f'• {satir}', S_IND))

    e.append(Paragraph('4.3 YZ Güvenliği ve Dezenformasyon', S_H2))
    e.append(Paragraph(
        'Deepfake (yapay ses/görüntü), YZ destekli dezenformasyon kampanyaları ve biyometrik '
        'gözetim, YZ güvenliği tartışmalarının odağındadır. "YZ okuryazarlığı" — YZ\'nin ne '
        'zaman, nasıl, kimin tarafından kullanıldığını anlama kapasitesi — 21. yüzyılın temel '
        'becerisi haline gelmiştir.', S_BD))

    e.append(Paragraph('4.4 Eğitimde YZ', S_H2))
    e.append(Paragraph(
        'YZ, kişiselleştirilmiş öğrenme, otomatik geri bildirim, içerik oluşturma alanlarında '
        'eğitimi dönüştürmektedir. "Ödev mi YZ mi?" sorusu da gündeme girmiştir. Okullar YZ '
        'kullanımına yönelik politikalar geliştirmektedir. Bu ünite, öğrencilerin hem YZ\'yi '
        'kullanmayı hem de sorgulamayı öğrenmesini hedefler.', S_BD))

    return e


# ============================================================
# BÖLÜM 5 — DİSİPLİNLERARASI BAĞLANTILAR
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'DİSİPLİNLERARASI BAĞLANTILAR')

    e.append(Paragraph('5.1 Bilişim Teknolojileri', S_H2))
    e.append(Paragraph(
        'YZ kavramları (algoritma, model, veri), Bilişim dersinin temel taşlarıyla doğrudan '
        'örtüşür. Prompt engineering pratiği dijital okuryazarlık becerisidir. Üst düzey '
        'öğrenciler için basit karar ağacı (decision tree) oluşturma, YZ mantığını '
        'somutlaştırır.', S_BD))

    e.append(Paragraph('5.2 Türkçe', S_H2))
    e.append(Paragraph(
        'YZ çıktılarını eleştirel okuma ve doğrulama, Türkçe dersinin eleştirel okuma boyutuyla '
        'kesişir. "Halüsinasyon" kavramı haberlerin kaynağını araştırma pratiğiyle doğrudan '
        'bağlantılıdır. YZ metinleri ile insan metinlerini karşılaştırma, dil farkındalığını '
        'geliştirir.', S_BD))

    e.append(Paragraph('5.3 Sosyal Bilgiler', S_H2))
    e.append(Paragraph(
        'YZ ve gizlilik, önyargı, dijital haklar, istihdam değişimi — bunlar Sosyal Bilgiler\'in '
        'vatandaşlık ve etik boyutlarıyla örtüşür. "YZ kararlarına kim hesap verecek?" sorusu '
        'doğrudan hukuk ve demokratik denetim tartışmasına bağlanır.', S_BD))

    e.append(Paragraph('5.4 Fen Bilgisi', S_H2))
    e.append(Paragraph(
        'Veri toplama, model kurma ve test etme süreçleri bilimsel yöntemle paraleldir. '
        'Makine öğrenmesindeki "hipotez → veri → sonuç" döngüsü, bilimsel yöntemin dijital '
        'uyarlamasıdır.', S_BD))

    return e


# ============================================================
# BÖLÜM 6 — YANLIŞ ANLAMALAR
# ============================================================

def bolum6():
    e = []
    e += bolum_baslik(6, 'YANLIŞ ANLAMALAR')

    yanlis = [
        ('"YZ her şeyi biliyor."',
         'YZ, eğitim verisindeki örüntüleri yansıtır. Veri kesim tarihinden sonrasını bilmez; '
         'bilmediğini bilmediği için halüsinasyon üretir.'),
        ('"YZ düşünüyor ve anlıyor."',
         '"Anlama" insana özgü bilinç ve deneyim gerektiren felsefi bir kavramdır. YZ istatistiksel '
         'örüntü bulucu; bu sınır hâlâ geçerlidir.'),
        ('"ChatGPT = Yapay Zekânın tamamı."',
         'ChatGPT bir büyük dil modelidir. YZ çok geniş: görüntü tanıma, ses sentezi, otonom '
         'araçlar, tıbbi tanı — bunların hepsi farklı YZ türleridir.'),
        ('"YZ tarafsızdır; insanlar gibi önyargılı değildir."',
         'YZ eğitim verisindeki önyargıları öğrenir. Yanlı veri → yanlı model. Bu önyargılar '
         'bazen orijinalinden daha sistematik biçimde tekrar edilir.'),
        ('"İyi prompt yazmak YZ\'yi her zaman doğru cevaplamaya zorlar."',
         'Bilginin modelde olmadığı durumlarda iyi prompt da halüsinasyonu önleyemez. '
         'Doğrulama her zaman gereklidir.'),
        ('"YZ benim işimi çalacak."',
         'YZ bazı görevleri dönüştürüyor. En savunmasız görevler rutin ve tekrarlayanlardır. '
         'Yaratıcılık, empati ve karmaşık problem çözme daha dirençlidir.'),
        ('"YZ kullanmak kopya çekmektir."',
         'YZ, kütüphane veya hesap makinesi gibi bir araçtır. Öğrenmeyi destekliyor mu, '
         'engelliyor mu? Bu soru etik değerlendirmenin merkezidir.'),
        ('"YZ hep aynı sonucu verir."',
         'Aynı prompt farklı çalıştırmalarda farklı çıktı üretebilir. Modeller stokastiktir '
         '— deterministik değil.'),
    ]

    header = [[Paragraph('Yanlış Anlama', S_TH), Paragraph('Doğrusu', S_TH)]]
    rows = [[Paragraph(y, S_TC), Paragraph(d, S_TC)] for y, d in yanlis]
    tablo = header + rows

    t = Table(tablo, colWidths=[CW*0.35, CW*0.65])
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
        'Alan Turing: "Makine Düşünebilir mi?"',
        [
            '1950\'de Alan Turing, "Computing Machinery and Intelligence" adlı makalesinde '
            'şunu sordu: "Bir makine düşünebilir mi?" Bu soruyu test etmek için "Taklit '
            'Oyunu"nu (bugün Turing Testi olarak bilinen) tasarladı.',
            'Turing, İkinci Dünya Savaşı\'nda Almanların Enigma şifreli iletişimini çözerek '
            'savaşın seyrini değiştirdi. YZ tarihi ve bilgisayar bilimleri tarihinin '
            'kesişme noktasındaki insan.',
        ],
        'Öğrencilere sorun: Turing testi günümüzde hâlâ geçerli bir ölçüt müdür?'))

    e.append(hikaye(
        'IBM Deep Blue ve Kasparov: Makine mi Kazandı?',
        [
            '1997\'de IBM\'in Deep Blue bilgisayarı, dünya satranç şampiyonu Garry Kasparov\'u '
            '6 oyunluk maçta 3,5–2,5 yendi. Kasparov sonradan itiraz etti: "Bazı hamleler bu '
            'kadar zekice olamazdı, birisi makinenin arkasındaydı." Sonuç: makine kendi '
            'başına oynamıştı.',
            'Ama Deep Blue satranç kurallarını gerçekten anlamamıştı; milyonlarca hamleyi '
            'saniyeler içinde hesaplayabilen bir optimizasyon motoruydu. "Anlama" ile '
            '"hesaplama" farkı o gün net biçimde ortaya çıktı.',
        ],
        'Mesaj: "Zeki görünmek" ile "zekâ sahibi olmak" aynı şey değildir.'))

    e.append(hikaye(
        'AlphaGo: İnsan Sezgisini Geçmek',
        [
            '2016\'da Google DeepMind\'ın AlphaGo programı, 18 kez dünya şampiyonu olan '
            'Go oyuncusu Lee Sedol\'u 4-1 yendi. Go, satranç\'tan çok daha karmaşıktır.',
            'Lee Sedol maç sonrasında: "Kendime karşı yapılan hamleleri anlamak için 1-2 '
            'saat düşünmek zorunda kaldım." AlphaGo, insan oyuncuların yüzyıllardır '
            'geliştirdiği sezgilerin ötesine geçti.',
        ],
        'Öğrencilere sorun: Bu bir kazanç mıydı, kayıp mıydı?'))

    e.append(hikaye(
        'ChatGPT: 100 Milyon Kullanıcı, 2 Ayda',
        [
            'Kasım 2022\'de OpenAI ChatGPT\'yi yayımladı. İlk 5 günde 1 milyon kullanıcıya '
            'ulaştı. 2 ayda 100 milyon — tarihte herhangi bir tüketici uygulamasının '
            'eriştiği en hızlı büyüme.',
            'Okullarda birden bire ödev sorusu değişti. Avukatlar YZ\'nin hazırladığı '
            'dilekçeleri mahkemeye verdi — ve var olmayan emsal kararlar (halüsinasyon) '
            'içerdiği ortaya çıktı. Bir teknoloji, bu kadar hızlı bu kadar çok soruyu '
            'birden açabilirdi.',
        ],
        'Öğrencilere sorun: Bu değişim sizi nasıl etkiliyor?'))

    e.append(hikaye(
        'Gizli Önyargı: Yüz Tanıma ve Hatalı Tutuklama',
        [
            '2020 yılında Detroit\'te Robert Williams adlı siyahi bir adam, yüz tanıma '
            'sisteminin "eşleşti" dediği gerekçesiyle tutuklandı. Sistem yanılmıştı. '
            'Eğitim verisindeki ırksal dengesizlik, sistemin koyu tenli yüzleri daha '
            'hatalı tanımasına yol açmıştı.',
            'Bu hata yalnızca teknik değil, adalet sorunuydu. YZ önyargısı, toplumsal '
            'ayrımcılığı ölçeklendirebilir. Algoritma "nesnel" görünür ama içindeki veri '
            'hiçbir zaman nesnel değildir.',
        ],
        'Öğrencilere sorun: Bunu önlemek için ne yapılabilir?'))

    e.append(hikaye(
        'Türkiye\'de YZ: Bir Ortaokul Öğrencisinin Prompt Keşfi',
        [
            'Bir ortaokul öğrencisi YZ\'den ödev yardımı istedi: "Atatürk hakkında 3 cümle '
            'yaz." Yanıt doğru ama yüzeyseldi. Öğrenci geliştirdi: "7. sınıf öğrencisi '
            'için, Atatürk\'ün eğitime katkısını açıkla." Daha odaklı yanıt geldi.',
            'Sonra: "Türkiye\'de 1920\'lerde okullaşma oranı ne kadardı?" YZ bir sayı '
            'verdi — öğrenci kuşkulandı, araştırdı. Sayı yakındı ama tam değildi.',
            'O gün öğrenci hem prompt mühendisliğini hem de halüsinasyon doğrulamasını '
            'yaşayarak öğrendi. Araç değerliydi; ama araçsız eleştirel düşünme olmaz.',
        ],
        'Mesaj: YZ\'yi kullanmak ile YZ\'yi sorgulamak birbirini tamamlar.'))

    return e


# ============================================================
# BÖLÜM 8 — ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ZOR SORULAR')

    qas = [
        ('YZ gerçekten "zekî" mi?',
         '"Zekâ" henüz bilimsel olarak tam tanımlanmış bir kavram değil. YZ insanın zeki '
         'saydığı görevleri yerine getirebiliyor — ama bunu nasıl yaptığı insanın düşünme '
         'biçiminden temelden farklı: istatistiksel örüntü eşleştirme. "Gerçekten zeki mi?" '
         'sorusu, "zekâ nedir?" sorusu yanıtlanmadan cevaplanamaz. Bu hem felsefi hem de '
         'bilimsel bir tartışmadır; henüz kapanmamıştır.'),
        ('YZ sonunda insanın yerini alacak mı?',
         '"Yerini almak" ikili bir kavram. Belirli görevlerde YZ insandan daha hızlı ve ucuz. '
         'Ama iş yalnızca görevlerden oluşmuyor: ilişki kurmak, belirsizliği yönetmek, etik '
         'karar vermek, yeni duruma uyum sağlamak insan becerileri olmaya devam ediyor. '
         'Büyük olasılıkla YZ bazı meslekleri dönüştürecek, bazılarını ortadan kaldıracak '
         've bugün hayal bile edemediğimiz yeni işler yaratacak — tıpkı elektrik, otomobil '
         've internet gibi.'),
        ('YZ önyargılıysa neden kullanıyoruz?',
         'Tüm sistemler bir biçimde önyargı taşır — kurumlar, yasalar, insanlar dahil. '
         'YZ önyargısını tanımak ve azaltmak üzerine aktif araştırma yapılıyor. Kullanmak '
         'ile sorgulamak birbirinin karşıtı değil; "fayda sağlar ama riskini bil" yaklaşımı '
         'en olgun olandır.'),
        ('Halüsinasyon bir hata mı, yoksa tasarım gereği mi?',
         'Her ikisi de kısmen. Büyük dil modelleri olasılık hesabına dayandığından, belirsiz '
         'sorulara "boş bırakamam" şeklinde tepki veriyor ve mevcut en olası yanıtı üretiyor '
         '— yanlış da olsa. Doğrulama mekanizması eklemeye yönelik araştırmalar var '
         '(retrieval-augmented generation gibi) ama tam çözüm henüz yok.'),
        ('Bir YZ aracını "sorumlu" biçimde kullanmak ne demek?',
         'Amacı şeffaf tutmak (öğrenmek için mi, kolaylaştırmak için mi?), çıktıyı '
         'doğrulamak, telif hakkına dikkat etmek, kişisel verileri paylaşmamak ve '
         'başkalarına zarar verecek içerik üretmemek. "Sorumlu kullanım" bir liste '
         'değil, bir düşünme alışkanlığıdır.'),
        ('Yapay zekâya güvenebilir miyiz?',
         '"Güven" bağlama bağlıdır. Spotify\'ın müzik önerisine güvenmek başka, tıbbi '
         'tanı için YZ çıktısına güvenmek başkadır. Yüksek risk taşıyan kararlar (tıp, '
         'hukuk, güvenlik) için YZ\'nin daima insan denetimiyle desteklenmesi gerekir. '
         '"Her durumda güven" veya "hiçbir durumda güven" yaklaşımlarının ikisi de yanlıştır.'),
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
        title='9. Unite - Ogretmen Hazirlik Rehberi',
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
    print('OK  U9_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
