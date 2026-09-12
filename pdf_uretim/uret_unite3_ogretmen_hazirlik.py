# -*- coding: utf-8 -*-
"""
3. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit3/U3_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite3_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit3')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U3_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '3. Ünite - Tasarım Odaklı Süreç'
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
        'Bu ünitenin temel kavramları — tasarım odaklı düşünme, empati, prototip, ergonomi, '
        'sürdürülebilirlik, inovasyon — günlük dilde kullanılagelen ama tasarımda farklı anlam '
        'taşıyan terimlerdir. Aşağıdaki açıklamalar, ders öncesi kavramsal hazırlığı '
        'sağlamak içindir.', S_BD))

    # 1.1 Tasarım Odaklı Düşünme
    e.append(Paragraph('1.1 Tasarım Odaklı Düşünme: Sezgiden Yönteme', S_H2))
    e.append(Paragraph(
        'Tasarım odaklı düşünme (Design Thinking) bir problemi çözmeye başlamadan önce '
        'o problemi yaşayan insanı anlamak üzerine kuruludur.', S_BD))
    e.append(Paragraph(
        '<b>Geleneksel problem çözme:</b> Problem nedir? Çözüm nedir? Uygula. Bu yaklaşım '
        'mühendislik problemlerinde güçlüdür — taşıması gereken yükü biliyorsunuz, hesaplarsınız, '
        'inşa edersiniz. Ama insan hayatıyla ilgili problemlerde bu yaklaşım çoğunlukla '
        'başarısız olur: insanlar neye ihtiyaç duyduklarını her zaman bilemez, bildiklerini '
        'her zaman doğru ifade edemez.', S_BD))
    e.append(bilgi_kutusu(
        'Tarihsel Not: Herbert Simon ve "Yapay Bilimler"',
        ['1969\'da Nobel Ekonomi Ödülü sahibi Herbert Simon "The Sciences of the Artificial" '
         'adlı kitabını yayımladı.',
         'Tasarımı "mevcut durumları tercih edilen durumlara dönüştürme sanatı" olarak tanımladı.',
         'Bu tanım, tasarımı ilk kez bilimsel bir disiplin olarak çerçeveledi ve Design Thinking '
         'yönteminin felsefi temelidir.',
         'Simon\'a göre tasarlamak hem bir düşünce biçimidir hem de öğretilip öğrenilebilir '
         'bir beceridir.']))

    # 1.2 Empati
    e.append(Paragraph('1.2 Empati: Acımak Değil, Anlamak', S_H2))
    e.append(Paragraph(
        'Empati kelimesi Yunanca em (içinde) + pathos (duygu, acı) kökünden gelir. '
        'Türkçede "duygudaşlık" olarak çevrilir. Ancak tasarımda empati, duygusal acıma '
        'değil, bilişsel bir eylemdir: kullanıcının bakış açısını içselleştirmek.', S_BD))
    e.append(bilgi_kutusu(
        'İki Empati Türü',
        ['Duygusal empati: "Onun acısını hissediyorum." Güçlü ve değerli, ama tek başına '
         'tasarıma dönüşmez.',
         'Bilişsel empati: "Onun neden böyle düşündüğünü anlıyorum." Tasarımcının geliştirmesi '
         'gereken tür.',
         'Empati haritası tam olarak bilişsel empatiyi yapılandırır: Ne söylüyor? Ne düşünüyor? '
         'Ne hissediyor? Ne yapıyor? — Bu dört alan birbirinden farklı ve hepsi ayrı ayrı '
         'değerlidir.']))
    e.append(Paragraph(
        '<b>Neden öğrenciler empatiyi zor buluyor?</b> Çünkü "ben ne isterim?" sorusu otomatik, '
        '"o ne ister?" sorusu ise bilinçli çaba gerektirir. Beyin varsayılan olarak kendisini '
        'referans alır. Tasarım sürecinde en büyük yanlış da burada yapılır: tasarımcının '
        'ihtiyacı değil, kullanıcının ihtiyacı merkeze alınmalıdır.', S_BD))

    # 1.3 Prototip
    e.append(Paragraph('1.3 Prototip: Başarısızlığı Ucuza Satın Almak', S_H2))
    e.append(Paragraph(
        '"Prototype" kelimesi Yunanca protos (ilk) + typos (iz, kalıp) kökünden gelir. '
        '"İlk kalıp" demektir. Prototip, tasarım sürecinde şu soruyu sormayı kolaylaştırır: '
        'Ürünü üretmeden önce, doğru ürünü mü üretiyorum?', S_BD))
    e.append(Paragraph(
        '<b>Prototip, yarım ürün değil, kasıtlı olarak sınırlı bir modeldir.</b> Amacı: pahalı '
        'kaynaklara yatırım yapmadan önce fikrin işe yarayıp yaramadığını test etmek.', S_BD))
    prototip_data = [
        [Paragraph('Tür', S_TH), Paragraph('Tanım', S_TH), Paragraph('Bu Ünitede', S_TH)],
        [Paragraph('Kağıt prototipi', S_TC),
         Paragraph('En hızlı ve en ucuzu; bir uygulamayı kağıda çizmek gibi', S_TC),
         Paragraph('Eskiz aşamasında', S_TC)],
        [Paragraph('Düşük sadakatli', S_TC),
         Paragraph('Malzeme doğru olmayabilir, boyutlar yaklaşık', S_TC),
         Paragraph('Atölye üretimleri', S_TC)],
        [Paragraph('Yüksek sadakatli', S_TC),
         Paragraph('Gerçek malzeme, gerçek boyut; üretim öncesi kullanıcı testi', S_TC),
         Paragraph('Kapsam dışında', S_TC)],
    ]
    prototip_t = Table(prototip_data, colWidths=[CW*0.28, CW*0.44, CW*0.28])
    prototip_t.setStyle(TableStyle([
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
    e.append(KeepTogether([prototip_t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>Silikon Vadisi\'nde sık kullanılan bir ifade:</b> "Fail fast, fail cheap" — Hızlı '
        'başarısız ol, ucuza başarısız ol. Bir prototip başarısız olduğunda aslında başarılı '
        'olmuştur — çünkü sizi daha büyük bir başarısızlıktan korumuştur.', S_BD))

    # 1.4 Ergonomi
    e.append(Paragraph('1.4 Ergonomi: İnsan-Nesne Diyaloğu', S_H2))
    e.append(Paragraph(
        'Ergonomi kelimesi Yunanca ergon (iş, eylem) + nomos (kural, yasa) kökünden gelir. '
        '"Çalışmanın yasaları" demektir. İngilizce\'de "Human Factors" (İnsan Faktörleri) '
        'olarak da bilinir.', S_BD))
    e.append(bilgi_kutusu(
        'Ergonominin Üç Boyutu',
        ['Fiziksel ergonomi: Vücut ölçüleri, kas-iskelet sistemi, postür. Sandalye yükseklikleri, '
         'klavye açısı, alet sap uzunlukları.',
         'Bilişsel ergonomi: Zihinsel iş yükü, dikkat, hafıza. Bir arabanın gösterge paneli, '
         'bir telefon arayüzü bilişsel ergonomiyi ilgilendirir.',
         'Örgütsel ergonomi: İş süreçleri, takım çalışması, çalışma saatleri. Vardiya sistemi '
         'insanı ne kadar yorar?']))
    e.append(Paragraph(
        '<b>Neden öğrenciler için önemli?</b> Bir ortaokul öğrencisi fiziksel ergonomiyi sezgisel '
        'olarak anlayabilir: "Bunu tutmak zor, çünkü sap çok kalın / çok ince." Bu sezgiyi bilinçli '
        'bir tasarım ölçütüne dönüştürmek bu ünitenin hedeflerinden biridir.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> Türkiye 1988\'de Ergonomi Derneği\'ni kurdu. Türk Standartları '
        'Enstitüsü (TSE) ergonomi standartlarını düzenler. İş güvenliği mevzuatının önemli bir '
        'bölümü ergonomi ilkelerine dayanır.', S_BD))

    # 1.5 Sürdürülebilirlik
    e.append(Paragraph('1.5 Sürdürülebilirlik: Üç Ayak', S_H2))
    e.append(Paragraph(
        '"Sürdürülebilir kalkınma" kavramı ilk kez 1987 BM Brundtland Raporu\'nda tanımlandı: '
        '"Bugünkü neslin ihtiyaçlarını, gelecek nesillerin kendi ihtiyaçlarını karşılama '
        'kapasitesini tehlikeye atmadan karşılamak."', S_BD))
    e.append(Paragraph(
        '<b>Sınıfta somutlaştırma:</b> "Babanız arabasını kullanıyor. Araba petrol tüketiyor. '
        'Petrol biterse torunlarınız bu arabayı kullanamaz. Bu kullanım sürdürülebilir mi?"', S_BD))
    uc_ayak = [
        [Paragraph('Boyut', S_TH), Paragraph('Kapsam', S_TH), Paragraph('Tasarım Sorusu', S_TH)],
        [Paragraph('Çevresel', S_TC),
         Paragraph('Doğal kaynaklar, geri dönüşüm, karbon ayak izi', S_TC),
         Paragraph('Bu malzeme geri dönüştürülebilir mi?', S_TC)],
        [Paragraph('Ekonomik', S_TC),
         Paragraph('Uzun vadeli maliyet, bakım, tek kullanımlık mı?', S_TC),
         Paragraph('Kaç yıl kullanılabilir?', S_TC)],
        [Paragraph('Sosyal', S_TC),
         Paragraph('Üretimde adil çalışma, toplumsal erişim', S_TC),
         Paragraph('Kim üretecek, kim kullanacak?', S_TC)],
    ]
    uc_t = Table(uc_ayak, colWidths=[CW*0.20, CW*0.44, CW*0.36])
    uc_t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, COLOR_VERY_LIGHT]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    e.append(KeepTogether([uc_t, vsp(0.15)]))

    # 1.6 İnovasyon
    e.append(Paragraph('1.6 İnovasyon: Farklılığın Ölçüsü', S_H2))
    e.append(Paragraph(
        'İnovasyon kelimesi Latince innovare (yenilemek, değiştirmek) kökünden gelir.', S_BD))
    e.append(bilgi_kutusu(
        'İnovasyon ile İcat Arasındaki Fark',
        ['İcat: Daha önce var olmayan bir şey yaratmak. Daha nadirdir.',
         'İnovasyon: Var olan bir şeyi anlamlı biçimde geliştirmek ya da yeni bir bağlamda '
         'uygulamak. Daha yaygındır.',
         'Cep telefonu bir icat değil, birçok icadın (telefon, bilgisayar, kamera, GPS) bir '
         'araya getirilmesidir — bu bir inovasyondur.',
         'Öğrencilerin bu ünitede ürettiği prototipler çoğunlukla icat değil, inovasyon '
         'içerecektir. Bu beklenen ve değerli bir sonuçtur.']))

    return e


# ============================================================
# BÖLÜM 2 — TASARIM ODAKLI DÜŞÜNCENİN TARİHSEL ARKA PLANI
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TASARIM ODAKLI DÜŞÜNCENİN TARİHSEL ARKA PLANI')
    e.append(Paragraph(
        'Design Thinking bir gecede ortaya çıkmadı. Arkasından on yıllık akademik ve pratik '
        'birikim var. Bu bölüm, yöntemi tarihsel bağlamına oturtmak için gerekli arka planı '
        'sunmaktadır.', S_BD))

    # 2.1 Wicked Problems
    e.append(Paragraph('2.1 Bir Yöntemin Doğuşu: Wicked Problems', S_H2))
    e.append(Paragraph(
        '1973\'te plancı Horst Rittel ve Melvin Webber "Dilemmas in a General Theory of '
        'Planning" adlı makaleyi yayımladı. Bu makale tasarım tarihinin dönüm noktalarından '
        'biridir.', S_BD))
    e.append(bilgi_kutusu(
        'Wicked Problems: İnatçı, Çözümsüz Problemler',
        ['Rittel ve Webber, bazı problemlerin wicked (inatçı, kötücül) olduğunu öne sürdü.',
         'Özellikleri: Tam olarak tanımlanamaz; her çözüm girişimi yeni problemler doğurur; '
         '"doğru" ya da "yanlış" çözüm yoktur, "daha iyi" ya da "daha kötü" çözüm vardır; '
         'benzersizdir — geçmişteki çözüm bu probleme uygulanamaz.',
         'Sosyal politika, kentsel planlama, eğitim, sağlık — bunların hepsi wicked problem '
         'alanlarıdır.',
         'Tasarım sürecinin gerçek değeri tam da bu tür problemlerde ortaya çıkar: formüle '
         'göre değil, insanı anlayarak hareket etmek.']))

    # 2.2 Stanford d.school
    e.append(Paragraph('2.2 Stanford d.school: Yöntemin Okullaşması', S_H2))
    e.append(Paragraph(
        '1991\'de IDEO\'nun kurucusu David Kelley, Stanford Üniversitesi\'nde Hasso Plattner '
        'Institute of Design — kısaca d.school — adlı bir kurum kurdu.', S_BD))
    e.append(Paragraph(
        'd.school\'un felsefesi: Tasarım bir sanat dalına ya da mühendislik bölümüne özgü '
        'değildir. Hukuk, tıp, işletme, mühendislik — hepsi tasarım odaklı düşünmeyi '
        'öğrenebilir.', S_BD))
    e.append(bilgi_kutusu(
        'd.school Modeli (5 Adım) ile Bizim Modelimizin Karşılaştırması',
        ['d.school: Empathize (Empati Kur) — Define (Tanımla) — Ideate (Fikir Üret) — '
         'Prototype (Prototip Yap) — Test (Test Et)',
         'Bizim 7 adımlı modelimiz bu temel çerçeveye Problem Tespiti ve Revize basamaklarını '
         'ekleyerek genişletilmiş bir versiyondur.',
         'Her iki model de döngüseldir: Test sonucu sizi Problem Tespiti\'ne bile '
         'götürebilir.']))

    # 2.3 IDEO
    e.append(Paragraph('2.3 IDEO: Tasarım Düşüncesini Şirkete Taşımak', S_H2))
    e.append(Paragraph(
        'IDEO 1991\'de San Francisco\'da kuruldu. Bugün dünyanın en etkili tasarım '
        'danışmanlık firmalarından biri. IDEO\'nun yöntemi: Kullanıcının yaşadığını '
        'anlamadan üretemezsin.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye bağlantısı:</b> IDEO\'nun Istanbul Design Lab projesi kapsamında Türk '
        'şirketleriyle iş birliği çalışmaları yürütülmüştür. Arçelik ve Türk Telekom gibi '
        'şirketler tasarım odaklı düşünce yöntemlerini kurumsal süreçlerine entegre '
        'etmiştir.', S_BD))

    return e


# ============================================================
# BÖLÜM 3 — KRONOLOJİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'TASARIM ODAKLI DÜŞÜNCENİN KRONOLOJİSİ')

    kron_data = [
        [Paragraph('Yıl', S_TH), Paragraph('Gelişme', S_TH)],
        [Paragraph('1969', S_TC), Paragraph('Herbert Simon "The Sciences of the Artificial"ı yayımladı; tasarımı bilimsel bir disiplin olarak tanımladı', S_TC)],
        [Paragraph('1973', S_TC), Paragraph('Horst Rittel "wicked problems" kavramını ortaya attı; tasarım süreci akademik ilgi gördü', S_TC)],
        [Paragraph('1991', S_TC), Paragraph('IDEO kuruldu; David Kelley Stanford d.school\'un temellerini attı', S_TC)],
        [Paragraph('1999', S_TC), Paragraph('IDEO\'nun alışveriş arabası projesi (ABC Nightline) geniş kamuoyuna yayıldı', S_TC)],
        [Paragraph('2004', S_TC), Paragraph('Stanford d.school resmi olarak açıldı', S_TC)],
        [Paragraph('2009', S_TC), Paragraph('Tim Brown "Change by Design" kitabını yayımladı; DT iş dünyasında ana akıma girdi', S_TC)],
        [Paragraph('2012', S_TC), Paragraph('IBM "Design Thinking at Scale" programını başlattı: 1.000 tasarım düşüncesi danışmanı', S_TC)],
        [Paragraph('2015', S_TC), Paragraph('d.school beş adımlı modelini açık kaynak olarak dünyayla paylaştı', S_TC)],
        [Paragraph('2020+', S_TC), Paragraph('Pandemi sonrası uzaktan DT atölyeleri yaygınlaştı; dijital prototipleme araçları gelişti', S_TC)],
    ]
    kron_t = Table(kron_data, colWidths=[CW*0.14, CW*0.86])
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
    e += bolum_baslik(4, 'GÜNCEL DURUM: TASARIM DÜŞÜNCESİ BUGÜN NEREDE?')

    e.append(Paragraph('4.1 Kurumsal Dünyada Design Thinking', S_H2))
    e.append(Paragraph(
        'Bugün Fortune 500 şirketlerinin büyük çoğunluğu DT çerçevesini ürün geliştirme, '
        'inovasyon veya müşteri deneyimi süreçlerinde kullanmaktadır.', S_BD))
    e.append(Paragraph(
        '<b>Airbnb örneği:</b> 2009\'da Airbnb iflasin eşiğindeydi. Kurucular New York\'a '
        'giderek ev sahipleriyle yüz yüze görüştü, odaları gördü. İçgörü son derece basitti: '
        'Fotoğraflar berbattı. Çözüm teknik değil, empati kaynaklıydı. Airbnb kendi parasıyla '
        'profesyonel fotoğraf çekimi sundu. İki haftada New York geliri iki katına çıktı. Bu '
        'karar bir algoritma değil, empati sonucuydu.', S_BD))
    e.append(Paragraph(
        '<b>Uber\'in dersi:</b> Uber şehir içi ulaşım problemini DT yaklaşımıyla çözdü. Ama '
        'sürücülerin deneyimini ihmal etti. Bu, kullanıcı empatisinin yalnızca bir taraf için '
        'çalışmasının sınırını göstermektedir.', S_BD))

    e.append(Paragraph('4.2 Eğitimde Design Thinking', S_H2))
    e.append(Paragraph(
        'Türkiye dahil pek çok ülkede DT artık K-12 müfredatlarında yer alıyor. Bunun nedeni: '
        'DT yalnızca bir tasarım aracı değil, düşünme biçimi olarak öğretiliyor. Eleştirel '
        'düşünme (KB2.9) + yaratıcı düşünme (KB2.10) + problem çözme (KB2.19) — bu beceriler '
        'DT sürecinin doğal çıktılarıdır.', S_BD))

    e.append(Paragraph('4.3 Türkiye\'de Tasarım Odaklı Düşünme', S_H2))
    e.append(Paragraph(
        'Türkiye Cumhurbaşkanlığı İnsan Kaynakları Ofisi ve TÜBİTAK, 2020\'lerden itibaren DT '
        'eğitimini kamu sektörüne yaymak için programlar geliştirmiştir. Büyük şehirlerdeki '
        'tasarım atölyelerinde (Makerspace, FabLab) DT çerçevesi pratiğe aktarılmaktadır. '
        'Ankara ve İstanbul\'daki tasarım merkezlerinde Türk gençleri DT yöntemiyle kentsel '
        'problemlere çözüm üretmektedir.', S_BD))

    return e


# ============================================================
# BÖLÜM 5 — DİSİPLİNLERARASI BAĞLANTI
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'DİSİPLİNLERARASI BAĞLANTI')

    e.append(Paragraph('5.1 Fen Bilgisi: Malzeme Bilimi', S_H2))
    e.append(Paragraph(
        'Prototip üretiminin kalbinde malzeme seçimi var. Şu sorular Fen Bilgisi bağlantısını '
        'oluşturur:', S_BD))
    fen_liste = [
        '<b>Yoğunluk ve ağırlık:</b> Hafif prototip için hangi malzeme? Köpük mü, mukavva mı, balsa mı?',
        '<b>Esneklik ve sertlik:</b> Menteşe gerektiren parçada hangi malzeme esner, hangisi kırılır?',
        '<b>Geri dönüşüm:</b> Plastik sembollerinin anlamı (PET, HDPE, PP) — hangisi geri dönüştürülebilir?',
        '<b>Isı dayanımı:</b> Sıcak tutacak bir prototipte hangi malzeme uygun?',
    ]
    for f in fen_liste:
        e.append(Paragraph(f'• {f}', S_BUL))

    e.append(Paragraph('5.2 Matematik: Ölçek ve Oran', S_H2))
    mat_liste = [
        'Gerçek boyutun dörtte birini çizmek: 1:4 ölçeği',
        'Malzeme miktarını hesaplamak: alan ve hacim hesabı',
        'Fikir seçim matrisinde puanlama: oransal karar verme',
    ]
    for m in mat_liste:
        e.append(Paragraph(f'• {m}', S_BUL))

    e.append(Paragraph('5.3 Türkçe: Empati Dili ve Sunum', S_H2))
    tur_liste = [
        '<b>Empati haritası:</b> Kullanıcının duygularını yazılı ifade etmek, duygu kelime dağarcığını genişletir.',
        '<b>Problem tanımı cümlesi:</b> "Kim, ne zaman, neden" yapısı metin üretimi becerisiyle örtüşür.',
        '<b>Final sunumu:</b> Argüman yapısı, bağlaçların doğru kullanımı, dinleyiciyi ikna etmek.',
    ]
    for t in tur_liste:
        e.append(Paragraph(f'• {t}', S_BUL))

    e.append(Paragraph('5.4 Görsel Sanatlar: Eskiz ve Estetik', S_H2))
    e.append(Paragraph(
        'Tasarım eskizi, güzel sanatlar çiziminden farklıdır: iletişim öncelikli, estetik ikincil. '
        'Ancak iki boyutlu çizimden üç boyutlu düşünmeye geçiş, Görsel Sanatlar dersindeki '
        'perspektif çalışmalarıyla doğrudan ilişkilidir.', S_BD))

    e.append(Paragraph('5.5 Sosyal Bilgiler: Sürdürülebilir Tüketim', S_H2))
    e.append(Paragraph(
        'Malzeme seçimindeki sürdürülebilirlik tartışması, Sosyal Bilgiler\'deki çevre ve '
        'tüketim konularıyla örtüşür. "Bu malzeme nereden geliyor, kim üretiyor, nasıl elden '
        'çıkıyor?" sorusu disiplinlerarası bir sorudur.', S_BD))

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
        ('"Tasarım odaklı süreç düz bir çizgidir"',
         'Süreç döngüseldir. Test aşamasında elde edilen geri bildirim sizi Problem Tespiti\'ne '
         'bile geri götürebilir. Bu regresyon başarısızlık değil, olgunlaşmadır.'),
        ('"Empati = acımak / sempati duymak"',
         'Empati tasarımda bilişsel bir eylemdir: kullanıcının bakış açısını içselleştirmek. '
         'Acımak duygusal; empati zihinsel. Tasarımcı kullanıcı için üzülmez, kullanıcının '
         'ne yaşadığını anlar.'),
        ('"Prototypim başarısız olursa proje başarısız olmuştur"',
         'Tam tersi. Prototip başarısız olduğunda aslında ucuza bir şey öğrenilmiştir: bu fikir bu şekilde '
         'işe yaramıyor. Bu bilgi, pahalı kaynaklara yatırım yapmadan önce elde edilmiştir.'),
        ('"Ergonomi sadece sandalye veya oturma eşyalarıyla ilgilidir"',
         'Ergonomi her nesne için geçerlidir: kalem, çanta, kapı kolu, sınıf tahtası, merdiven '
         'basamak yüksekliği. "Bu nesneyle bedenimin diyaloğu nasıl?" sorusu ergonomi sorusudur.'),
        ('"Sürdürülebilir tasarım = geri dönüştürülmüş malzeme kullanmak"',
         'Sürdürülebilirlik üç boyutludur: çevresel, ekonomik, sosyal. Uzun ömürlü tasarım da '
         'sürdürülebilirdir. Bir kez kullanıp atılan geri dönüştürülmüş ürün, uzun yıllar '
         'kullanılan "normal" malzemeli bir ürünten daha az sürdürülebilir olabilir.'),
        ('"İnovasyon = icat etmek, hiç var olmayan bir şey yaratmak"',
         'İnovasyon çoğunlukla var olanı anlamlı biçimde iyileştirmektir. iPhone bir icat değildi '
         '— dokunmatik ekran, taşınabilir bilgisayar, cep telefonu vardı. Jobs bunları yeniden '
         'birleştirdi. Bu inovasyondu.'),
        ('"Beyin fırtınasında çılgın fikir üretmek zaman kaybıdır"',
         'Eleştiriden muaf bir ortamda üretilen fikir sayısı artar ve çeşitlenir. "Çılgın" fikirler '
         'doğrudan kullanılmasa da beklenmedik kombinasyonlara ilham verebilir. '
         'Crazy 8\'in değeri miktar içindedir.'),
        ('"Kullanıcı geri bildirimi kötü çıkarsa tasarımım kötüdür"',
         'Geri bildirim yargı değil, veridir. "Bu kısım işe yaramadı" bilgisi tasarımcıya ürünün '
         'neresinin geliştirileceğini söyler. İyi tasarımcılar savunmaya geçmez, not alır.'),
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
        'Başarısızlıktan Doğan İcat — Post-it\'in Hikayesi',
        ['1968 yılında 3M şirketinde kimyager Spencer Silver, çok güçlü bir yapıştırıcı '
         'geliştirmeye çalışıyordu. Sonuç tam tersi oldu: çok zayıf bir yapıştırıcı. '
         'Yapıştırıyordu, ama kolayca çıkıyordu. 3M için değersiz görüldü ve rafa kaldırıldı.',
         'Altı yıl sonra, 1974\'te Silver\'ın meslektaşı Art Fry kilisede ilahi kitabındaki '
         'yerini işaret eden kağıt parçalarının sürekli düştüğünden yakınıyordu. Silver\'ın '
         '"değersiz" yapıştırıcısını hatırladı. Küçük kağıt parçalarına o yapıştırıcıyı sürdü — '
         'yapıştı, söküldü, kitap zarar görmedi.',
         '3M bu ürünü defalarca reddetti. 1980\'de piyasaya çıktı. Bugün Post-it, 3M\'in '
         'en kârlı ürünlerinden biridir. Yılda 50 milyarı aşan bir piyasa değeri yaratır.'],
        'Bağlantı: Başarısız prototip aslında farklı bir problemi çözen prototipti. Tasarım '
        'sürecinde sonuç her zaman planladığınız gibi olmaz — bazen daha değerli bir yere '
        'çıkarsınız.'))

    e.append(hikaye(
        'Alışveriş Arabasını Yeniden Tasarlamak — IDEO\'nun Beş Günü',
        ['1999\'da ABC News, IDEO\'ya bir görev verdi: sıradan bir alışveriş arabasını beş '
         'günde yeniden tasarlayın.',
         'IDEO ekibi ilk gün fabrikaya gitmedi, süpermarkete gitti. Saatlerce gözlemlediler: '
         'Ebeveynler çocukları arabaya otururken zorlanıyordu. Müşteriler ödeme sırasında '
         'arabayı nereye bırakacaklarını bilemiyordu. Sepet içindeki ürünler eziliyordu.',
         'Beş günün sonunda ortaya çıkan araç: çalınmaya karşı bireysel sepet sistemi, '
         'çocuklar için güvenli platform, müşteri eşyalarını kolayca takip edebileceği düzen.',
         'Asıl yenilik tasarım ürünü değil, tasarım süreciydi. Çözüm gözlemden başlamıştı.'],
        'Bağlantı: Empati haritası ve kullanıcı analizi basamakları. "Problemi çözmeden önce '
        'problemi yaşayan insanı izle."'))

    e.append(hikaye(
        'Sesi Dinlemek — Airbnb\'nin İflasın Eşiğindeki Kararı',
        ['2009 yılında Airbnb henüz küçük bir girişimdi ve iflasin eşiğindeydi. Gelirler '
         'artmıyordu; rezervasyonlar yapılıyordu ama tekrar eden müşteri yoktu.',
         'Kurucular Joe Gebbia ve Brian Chesky, New York\'a giderek ev sahipleriyle bizzat '
         'görüştü. Evlere girdi, oturma odalarında oturdu, ev sahiplerini dinledi. İçgörü '
         'basitti: Fotoğraflar berbattı. Evler gerçekte güzeldi — ama düşük kaliteli '
         'fotoğraflar nedeniyle kimse rezervasyon yapmıyordu.',
         'Airbnb kendi parasıyla profesyonel fotoğrafçı tuttu ve ev sahiplerine bedava '
         'fotoğraf çekimi sundu. İki haftada New York geliri iki katına çıktı.'],
        'Bağlantı: Problem Tespiti ve Analiz basamakları. "Veri bazen sayıda değil, '
        'insanla kurulan bağlantıda gizlidir."'))

    e.append(hikaye(
        'Kuşu Taklit Etmek — Shinkansen\'in Gagası',
        ['Japonya\'nın yüksek hızlı treni Shinkansen, tünellerden çıkarken 70-80 desibel '
         'gürültüyle büyük bir hava patlaması yaratıyordu.',
         'Baş mühendis Eiji Nakatsu aynı zamanda deneyimli bir kuş gözlemcisiydi. Yıllar '
         'boyunca dalıcı kuşu (kingfisher) izlemişti: Havadan suya dalarken neredeyse hiç '
         'ses çıkarmıyordu. Koni şeklindeki gagası iki ortam arasındaki farkı neredeyse '
         'sessizce aşıyordu.',
         'Nakatsu trenin burnunu o gagadan ilhamla yeniden tasarladı. Gürültü azaldı, enerji '
         'tüketimi yüzde on düştü, hız arttı.',
         'Bu yaklaşım biyomimikri olarak adlandırılır: Doğadan öğrenerek tasarlamak.'],
        'Bağlantı: Farklı kaynaklardan ilham alma, çözümü beklenmedik yerlerde arama. '
        'Öğrencilere: "Tasarımın çözdüğü probleme benzer bir şeyi doğada kim ya da ne '
        'çözüyor?"'))

    e.append(hikaye(
        'İnşa Et, Ölç, Öğren — Minimum Uygulanabilir Ürün',
        ['2000\'li yıllarda Silikon Vadisi\'nde "Lean Startup" (Yalın Girişim) yaklaşımı '
         'yaygınlaştı. Eric Ries bu yaklaşımı "İnşa Et - Ölç - Öğren" döngüsüyle tarif etti.',
         'Temel fikir: Mükemmel ürünü aylarca geliştirip piyasaya sürmek yerine, işe yarayıp '
         'yaramadığını test edebilecek en yalın versiyonu mümkün olan en kısa sürede '
         'kullanıcıyla buluştur. Buna MVP (Minimum Viable Product) dendi.',
         'Dropbox bu fikri şöyle uyguladı: Ürünü kodlamadan önce ürünün nasıl çalışacağını '
         'anlatan iki dakikalık bir video yaptılar. Bu video aslında bir prototipti — '
         'fiziksel değil, kavramsal. Gece yayımlandı, sabahında 75.000 kişi bekleme '
         'listesine yazıldı. Ürün daha kodlanmamıştı.'],
        'Bağlantı: Prototip döngüsü ve "erken test et, ucuza öğren" mantığı. Öğrencilere: '
        '"Bu son ürününüz değil. Bu, öğrenme aracınız."'))

    e.append(hikaye(
        'Hata Kullanıcıda Değil Tasarımda — Norman Kapısı',
        ['1988\'de bilişsel bilimci Don Norman "The Design of Everyday Things" kitabını '
         'yayımladı.',
         'Norman bir problemi tanımladı: kapılar. Öylesi gerekeni iterken çekmek, iterek '
         'açılması gerekeni çekmek — bu evrensel bir deneyimdir. Hata kullanıcıda değil, '
         'tasarımcıdadır.',
         'İyi tasarım kullanım kılavuzuna ihtiyaç bırakmaz. Ürün kendi kullanımını anlatır. '
         'Buna "affordance" (karşılayıcılık) denir.',
         '"Norman Kapısı": Nasıl kullanılacağını sezgisel olarak aktarmayan, kullanıcıyı '
         'yanıltan her tasarım.'],
        'Bağlantı: Ergonomi ve kullanıcı merkezli tasarım. Öğrencilere: '
        '"Okulda Norman Kapısı var mı?" gözlem etkinliği açabilirsiniz.'))

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
        ('"Beyin fırtınasında hiç fikrim yoksa ne yapacağım?"',
         'Boş kalmak beynin "sıfırlandığı" andır — aslında kötü bir başlangıç noktası değildir. '
         'İki pratik yol: Birincisi, en aptalca çözümü düşün — "Bu problemi en kötü şekilde '
         'nasıl çözerim?" sorusu zihni açar. İkincisi, başkasının problemini düşün — empati '
         'kurduğunuzda fikirler daha kolay akar. Crazy 8\'de sekiz fikir üretemeyen öğrenci, '
         'sekiz deneme üretebilir — bu da yeterlidir.'),
        ('"Tasarladığım şey zaten var. Bu kopya mı sayılır?"',
         'Hayır. Tasarım dünyasında "fikri sahiplenmek" değil, "sorunu çözmek" önemlidir. '
         'Var olan bir çözümü daha iyi yapman inovasyondur. Kendi bağlamına uyarlamak da '
         'tasarım kararıdır. Önemli olan: senin çözümün özgün bir karar içeriyor mu? Malzeme '
         'seçimi mi, kullanım biçimi mi, ergonomi mi — bir yerde senin imzanı taşıyorsa '
         'bu özgündür.'),
        ('"Kullanıcım prototipimi beğenmedi. Bu başarısızlık mı?"',
         'Beğenmemek en değerli geri bildirimdir. "Beğendim" diyen bir kullanıcı size tasarımın '
         'neresini geliştireceğinizi söylemez. "Beğenmedim, çünkü..." diyen kullanıcı söyler. '
         'Tasarım sürecinde test aşamasının var olma nedeni budur: prototip sınıfta değil, '
         'gerçek kullanımı simüle ederek sınanır. Geri bildirimi not al, savunmaya geçme.'),
        ('"Sürdürülebilir malzeme bulamıyorum ya da çok pahalı — ne yapayım?"',
         'İki seçenek var. Birincisi: Uzun ömürlülük de sürdürülebilirliktir. Dayanıklı ve tamir '
         'edilebilir bir tasarım, tek kullanımlık ama "yeşil" malzemeden daha sürdürülebilir '
         'olabilir. İkincisi: Revize planında "şu anda bu malzemeyi kullanıyorum ama ileride '
         'şununla değiştirebilirim" yazmak da geçerli bir tasarım kararıdır.'),
        ('"Büyük şirketler gerçekten kullanıcı için mi tasarlıyor, yoksa sadece para için mi?"',
         'Dürüst yanıt: Çoğu zaman ikisi çelişmez — iyi kullanıcı deneyimi uzun vadede daha '
         'fazla gelir getirir. Ama şirketlerin yalnızca kullanıcı değil, kendi çıkarları için '
         'de tasarladığı açıktır. Dark pattern (karanlık örüntüler) buna iyi bir örnektir: '
         'bir uygulamadan çıkış yapmayı kasıtlı olarak zorlaştırmak kullanıcı için değil, '
         'şirket için tasarımdır. Tasarımın etik boyutu tam da burada başlar.'),
        ('"Tasarım odaklı sürecin bir sonu var mı?"',
         'Kural olarak yok. IDEO tasarımcılarından birinin dediği gibi: "Tasarım hiç bitmez, '
         'sadece yayımlanır." Bir ürünü piyasaya sürdükten sonra kullanıcı geri bildirimleri '
         'toplanır ve döngü yeniden başlar. Bizim ünitede "revize" son basamak gibi görünse de '
         'aslında yeni bir döngünün başlangıcıdır. Tasarım odaklı düşünme bir bitiş noktasına '
         'değil, sürekli iyileşmeye yönelir.'),
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
        title='3. Unite - Ogretmen Hazirlik Rehberi',
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
    print('OK  U3_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
