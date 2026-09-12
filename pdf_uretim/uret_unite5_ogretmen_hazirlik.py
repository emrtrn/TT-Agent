# -*- coding: utf-8 -*-
"""
5. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit5/U5_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite5_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit5')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U5_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '5. Ünite - Mimari Tasarım'
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
        'Bu ünitenin temel kavramları — mimari, antropometri, topografya, sürdürülebilir mimari, '
        'kat planı, maket, erişilebilirlik — tasarımı mekân ölçeğinde ele alır. '
        'Aşağıdaki açıklamalar ders öncesi kavramsal hazırlığı sağlamak içindir.', S_BD))

    # 1.1 Mimari
    e.append(Paragraph('1.1 Mimari: Sanat mı, Mühendislik mi?', S_H2))
    e.append(Paragraph(
        '"Mimari" kelimesi Arapça mi\'mār (inşaatçı, yapıcı) kökünden Türkçeye geçmiştir. '
        'İngilizce "architecture" ise Yunanca arkhitekton — arkhi (baş, birinci) + tekton '
        '(yapıcı, marangoz) — kökünden gelir: "baş yapıcı."', S_BD))
    e.append(Paragraph(
        '<b>Mimarlık ne sanat ne de saf mühendisliktir; ikisinin kesiştiği bir alandır.</b> '
        'Mimar şunu sorar: Bu yapı hem yükü taşısın, hem içinde yaşayan insanı onurlandırsın, '
        'hem çevreyle uyum içinde olsun. Bu üç gerilimi aynı anda yönetmek mimarlıktır.', S_BD))
    e.append(bilgi_kutusu(
        'Vitruvius\'un İki Bin Yıllık Üçlüsü',
        ['Romalı mimar Vitruvius bu üçlüyü M.Ö. 1. yüzyılda tanımladı.',
         'Firmitas (Sağlamlık): Yapı yükleri taşımalı, çevresel koşullara dayanmalı.',
         'Utilitas (Kullanışlılık): Yapı içinde yaşayanların ihtiyaçlarına yanıt vermeli.',
         'Venustas (Güzellik): Yapı çevresiyle estetik bir uyum içinde olmalı.',
         'Bu üçlü bugün de mimarlığın temel çerçevesidir. Derste buna sürdürülebilirlik '
         'boyutunu ekleyerek "4 ölçüt" olarak işliyoruz.']))

    # 1.2 Antropometri
    e.append(Paragraph('1.2 Antropometri: İnsan Bedeninin Dili', S_H2))
    e.append(Paragraph(
        '"Anthropometry" kelimesi Yunanca anthropos (insan) + metron (ölçü) kökünden gelir. '
        'Mimaride kullanılan büyük ölçüde statik antropometridir.', S_BD))
    antro_data = [
        [Paragraph('Ölçü', S_TH), Paragraph('Değer', S_TH), Paragraph('Nedeni', S_TH)],
        [Paragraph('Kapı yüksekliği', S_TC),
         Paragraph('210 cm', S_TC),
         Paragraph('Ortalama yetişkin boyuna 30 cm pay', S_TC)],
        [Paragraph('Merdiven yüksekliği', S_TC),
         Paragraph('17–19 cm', S_TC),
         Paragraph('Bacağın rahat kaldırabileceği yükseklik', S_TC)],
        [Paragraph('Tezgah yüksekliği', S_TC),
         Paragraph('85–90 cm', S_TC),
         Paragraph('Dirsek yüksekliğinin biraz altında çalışmak en az yorucu', S_TC)],
    ]
    antro_t = Table(antro_data, colWidths=[CW*0.30, CW*0.20, CW*0.50])
    antro_t.setStyle(TableStyle([
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
    e.append(KeepTogether([antro_t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>Önemli ayrım:</b> Antropometri standartları ortalama insana göre tasarlar. '
        'Ama iyi mimar ortalamanın dışındakileri de düşünür — bu erişilebilirliğe açılan kapıdır. '
        '<b>Türkiye bağlantısı:</b> TSE 9111 "Engelliler için Yapılarda Ulaşılabilirlik" standardı '
        'rampa eğiminden asansör boyutuna kadar tüm ölçüleri kapsar.', S_BD))

    # 1.3 Topografya
    e.append(Paragraph('1.3 Topografya: Arazinin Karakteri', S_H2))
    e.append(Paragraph(
        '"Topography" kelimesi Yunanca topos (yer) + graphia (yazma, çizme) kökünden gelir. '
        'Topografya arazinin fiziksel biçimini — eğimini, yükseltisini, zemin yapısını — '
        'inceler. Mimar için topografya hem kısıt hem fırsattır.', S_BD))
    e.append(bilgi_kutusu(
        'Eğimli Arazide Üç Temel Çözüm',
        ['Teraslama: Araziyi düzleştirerek kademeli platformlar oluşturma. '
         'Mardin\'in yamaç üzerindeki evleri, Trabzon\'un dağ köyleri bu sistemi kullanır.',
         'Arazi göme: Yapının bir yanını toprağa gömerek doğal yalıtım ve görsel entegrasyon sağlama.',
         'Yükseltme: Kazık veya kolon üzerine yapı kurarak araziye en az müdahale etme.',
         'Her çözümün maliyet, görünüm ve sürdürülebilirlik açısından farklı sonuçları vardır.']))

    # 1.4 Sürdürülebilir Mimari
    e.append(Paragraph('1.4 Sürdürülebilir Mimari: Üç Nesil Düşünmek', S_H2))
    e.append(Paragraph(
        'Sürdürülebilir mimari, bir yapının tasarımından yıkımına kadar tüm süreçte çevresel, '
        'ekonomik ve sosyal etkileri en aza indirmeyi hedefler. Doğru yön kararı, kalın yalıtım, '
        'çift cam ve saçak tasarımı — bunların tümü enerji faturasına ve karbon ayak izine '
        'doğrudan etki eder.', S_BD))
    sert_data = [
        [Paragraph('Sertifika', S_TH), Paragraph('Köken', S_TH), Paragraph('Açıklama', S_TH)],
        [Paragraph('LEED', S_TC),
         Paragraph('ABD', S_TC),
         Paragraph('Leadership in Energy and Environmental Design; dünya genelinde yaygın', S_TC)],
        [Paragraph('BREEAM', S_TC),
         Paragraph('Avrupa', S_TC),
         Paragraph('Building Research Establishment Environmental Assessment Method', S_TC)],
        [Paragraph('YEŞİL BİNA', S_TC),
         Paragraph('Türkiye', S_TC),
         Paragraph('Çevre, Şehircilik ve İklim Değişikliği Bakanlığı\'nın yerli sertifikasyon programı', S_TC)],
    ]
    sert_t = Table(sert_data, colWidths=[CW*0.20, CW*0.15, CW*0.65])
    sert_t.setStyle(TableStyle([
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
    e.append(KeepTogether([sert_t, vsp(0.15)]))

    # 1.5 Kat Planı
    e.append(Paragraph('1.5 Kat Planı: Binanın Ortak Dili', S_H2))
    e.append(Paragraph(
        'Kat planı, bir binanın belirli bir yükseklikten (genellikle yerden yaklaşık 1,2 metre) '
        'yatay olarak kesildiğinde görünen üstten görünüşüdür. Sanki binayı bir makasla yatay '
        'kesersiniz ve üstten bakarsınız.', S_BD))
    e.append(Paragraph(
        '<b>Neden o yükseklik?</b> 1,2 metre, kapı ve pencerelerin büyük çoğunluğunu kesen '
        'yüksekliktir — bu sayede plan, mekânın kullanım biçimini en iyi aktaran kesiti verir. '
        '<b>Ölçek zorunluluğu:</b> Kat planı her zaman bir ölçekle çizilir. Ölçek belirtilmemiş '
        'bir plan "teknik çizim" değil, "şema"dır.', S_BD))

    # 1.6 Maket
    e.append(Paragraph('1.6 Maket: Fikri Dokunulabilir Kılmak', S_H2))
    e.append(Paragraph(
        'Maket, binanın fiziksel küçük ölçekli modelidir. Mimarlar için maket iki farklı '
        'işlev görür:', S_BD))
    maket_liste = [
        '<b>Tasarım maketi:</b> Kendi kararlarını test etmek için. Işığın içeriye nasıl '
        'girdiğini görmek, oranları hissetmek, sorunları erken fark etmek için.',
        '<b>Sunum maketi:</b> Müşteriye, belediyeye ya da kamuoyuna projeyi anlatmak için.',
    ]
    for m in maket_liste:
        e.append(Paragraph(f'• {m}', S_BUL))
    e.append(Paragraph(
        'Bugün dijital modeller çok daha hızlı ve ucuz olsa da bazı mimarlar hâlâ fiziksel maket '
        'yapmayı tercih eder — çünkü üç boyutlu bir nesneyi elinizle tutmak, ekranda döndürmekten '
        'farklı bir anlayış sağlar.', S_BD))

    # 1.7 Erişilebilirlik
    e.append(Paragraph('1.7 Erişilebilirlik: Tasarımın Etik Boyutu', S_H2))
    e.append(Paragraph(
        'Erişilebilirlik, bir mekânın yaşlı, engelli, hamile, çocuk ya da geçici yaralanmalı '
        'bireyler dahil tüm kullanıcılar tarafından bağımsız biçimde kullanılabilmesini ifade eder.', S_BD))
    e.append(bilgi_kutusu(
        'Türkiye\'de Yasal Durum ve Evrensel Tasarım',
        ['2005 yılında yürürlüğe giren 5378 sayılı Engelliler Hakkında Kanun, kamuya açık '
         'yapıların erişilebilir olmasını yasal zorunluluk haline getirmiştir.',
         '"Universal Design" (Evrensel Tasarım) kavramı: 1997\'de mimar Ron Mace tarafından '
         'geliştirilen bu yaklaşım, "engelliler için özel tasarım" yerine "herkes için tasarım" '
         'ilkesini savunur.',
         'Rampa sadece tekerlekli sandalye kullananlar için değil; bebek arabası iten ebeveynler, '
         'kırık bacaklı atletler, ağır market torbası taşıyanlar için de aynı kolaylığı sağlar.']))

    return e


# ============================================================
# BÖLÜM 2 — MİMARLIĞIN TARİHSEL ARKA PLANI
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'MİMARLIĞIN TARİHSEL ARKA PLANI')
    e.append(Paragraph(
        'Mimarlık tarihi yalnızca yapılar tarihi değildir; her dönemin dünya görüşünü, '
        'teknolojisini ve toplumsal değerlerini yansıtan bir fikirler tarihidir.', S_BD))

    # 2.1 Vitruvius
    e.append(Paragraph('2.1 Vitruvius: İki Bin Yıllık Çerçeve', S_H2))
    e.append(Paragraph(
        'Marcus Vitruvius Pollio, M.Ö. 1. yüzyılda yaşamış Romalı bir mühendis ve mimardır. '
        'De Architectura adlı 10 ciltlik eseri, antik dönemden günümüze ulaşan tek tam '
        'mimarlık kuramı kitabıdır.', S_BD))
    e.append(Paragraph(
        'Öğrencilere şunu sormak iyi bir giriş noktasıdır: "Oturduğunuz evin duvarları '
        'sağlam mı? (firmitas) İçinde rahat mı yaşıyorsunuz? (utilitas) Güzel mi? (venustas)" '
        'Genellikle üçü aynı anda tam değildir.', S_BD))

    # 2.2 Mimar Sinan
    e.append(Paragraph('2.2 Mimar Sinan: Sınırları Zorlayan Akıl', S_H2))
    e.append(Paragraph(
        'Mimar Sinan (yaklaşık 1490-1588), Osmanlı İmparatorluğu\'nun üç padişahı döneminde '
        'baş mimar olarak görev yaptı. Hayatı boyunca 374\'ten fazla yapı inşa ettiği '
        'kayıtlara geçmiştir: camiler, köprüler, kervansaraylar, medreseler, hamamlar.', S_BD))
    e.append(bilgi_kutusu(
        'Selimiye: Ölçüde Değil, Fikirde Kazanmak',
        ['Sinan Selimiye Camii\'ni yaklaşık 80 yaşında tamamladı. Hedefi: Ayasofya\'yı aşmak.',
         'Ayasofya\'nın kubbe çapı 31,87 metre; Selimiye\'ninki 31,25 metre — rakamda 62 cm geride.',
         'Ama Sinan farklı bir şey yaptı: 8 sütun üzerine oturan kubbe altında tamamen bölünsüz, '
         'açık bir iç mekân yarattı. Ayasofya\'da iç taşıyıcılar mekânı parçalar; Selimiye\'de '
         'tek bir nefes vardır.',
         'Bugün mimarlık tarihçilerinin büyük çoğunluğu Selimiye\'yi teknik açıdan daha büyük '
         'bir başarı olarak değerlendirir.',
         'Modern incelemeler: Sinan\'ın yapıları deprem yükleri konusunda döneminin çok ötesinde '
         'çözümler içermektedir — sistematik zemin araştırması ve esnek derz uygulamaları.']))

    # 2.3 Osmanlı Sivil Mimarisi
    e.append(Paragraph('2.3 Osmanlı Sivil Mimarisi: Safranbolu Modeli', S_H2))
    e.append(Paragraph(
        'Safranbolu\'nun geleneksel konutları, Osmanlı sivil mimarisinin en iyi korunmuş '
        'örnekleridir. 1994\'te UNESCO Dünya Mirası Listesi\'ne alınmıştır.', S_BD))
    e.append(bilgi_kutusu(
        'Cumba (Çıkma) Neden Var?',
        ['Alt katta ahır, depo ve servis mekânları yer alırdı — büyük kapı açıklıklarına '
         'ihtiyaç vardı.',
         'Üst katta yaşam alanı genişletilmek isteniyordu.',
         'Çözüm: Ahşap konstrüksiyonla üst katı sokağın üzerine taşımak. Böylece hem alt katta '
         'geniş açıklık hem de üst katta geniş oda elde edildi.',
         'Cumba aynı zamanda pasif güneş kontrolü sağlar: yüksek tahta kafes pencereleri '
         'mahremiyet sağlarken ışığı içeriye alır; saçak yazın gölge yapar.']))

    # 2.4 Mardin
    e.append(Paragraph('2.4 Mardin: Topoğrafik Zekâ', S_H2))
    e.append(Paragraph(
        'Mardin, güneydoğu Anadolu\'da bir yamaç üzerine kurulmuş antik bir kenttir. '
        'Yapıların birbirine bitişik ve kademeli dizilişi tesadüf değil, iklim mühendisliğidir.', S_BD))
    mardin_liste = [
        'Her bina komşusunun gölgesinde serinler — kolektif gölge sistemi.',
        'Sarı kireç taşı hem bol bulunur hem yavaş ısınır/soğur — doğal termal kütle.',
        'İç avlular hava sirkülasyonu sağlar; mahremiyeti korurken serinletir.',
        'Düz çatılar yağışın az olduğu bu iklimde terasa dönüşür.',
    ]
    for m in mardin_liste:
        e.append(Paragraph(f'• {m}', S_BUL))
    e.append(Paragraph(
        '"Mardin\'deki yapılar birbirinin düşmanı değil, ortağı gibi tasarlanmış" — bu cümle '
        'öğrencilere mimari ölçeğin tek yapıyla sınırlı olmadığını anlatmanın iyi bir yoludur.', S_NOT))

    # 2.5 Le Corbusier
    e.append(Paragraph('2.5 Le Corbusier ve Modernizm: İşlevsellik Öne Çıktığında', S_H2))
    e.append(Paragraph(
        'İsviçreli-Fransız mimar Le Corbusier (1887-1965), 20. yüzyıl mimarisinin en etkili '
        'isimlerinden biridir. Evi "yaşamak için makine" olarak tanımladı.', S_BD))
    e.append(Paragraph(
        'Bu tanım hem devrimci hem sorunluydu. Devrimci: Süsleme gereksizdir, her form bir '
        'işlevi hizmet etmeli. Sorunlu: İnsanlar yalnızca "verimli" mekânlarda değil, anlam '
        'taşıyan, tarihle bağlantılı mekânlarda yaşamak ister. Le Corbusier\'nin tasarladığı '
        'kentler bugün hem büyük mimari başarı hem de "soğuk ve insansız" eleştirisiyle anılır.', S_BD))

    # 2.6 Sedad Hakkı Eldem
    e.append(Paragraph('2.6 Sedad Hakkı Eldem: Türk Ev Geleneğini Çağdaşa Taşımak', S_H2))
    e.append(Paragraph(
        'Sedad Hakkı Eldem (1908-1988), modernizmle geleneksel Osmanlı konut mimarisini '
        'birleştirmeyi düşünen mimarlar arasında en önemli isimdir.', S_BD))
    e.append(Paragraph(
        'Eldem 1930\'larda Türk evi üzerine kapsamlı bir araştırma yürüttü: Safranbolu, '
        'Edirne, Bursa ve Kuzey Ege\'deki geleneksel konutları belgeleyerek ortak ilkeleri '
        'tespit etti — esnek oda kurgusu, cumba, ahşap konstrüksiyon, merdivenin merkezi '
        'konumu. Bu araştırmayı kendi projelerine de uyguladı.', S_BD))

    return e


# ============================================================
# BÖLÜM 3 — KRONOLOJİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'MİMARLIK TARİHİNİN KRONOLOJİSİ')

    kron_data = [
        [Paragraph('Dönem', S_TH), Paragraph('Gelişme', S_TH)],
        [Paragraph('M.Ö. 1. yy', S_TC), Paragraph('Vitruvius De Architectura\'yı yazdı; firmitas-utilitas-venustas üçlüsünü tanımladı', S_TC)],
        [Paragraph('M.S. 537', S_TC), Paragraph('Ayasofya tamamlandı; 31,87 m çaplı kubbeyle çağının en büyük yapısı oldu', S_TC)],
        [Paragraph('1194-1220', S_TC), Paragraph('Chartres Katedrali; gotik mimarinin doruk noktası — statik hesap olmadan', S_TC)],
        [Paragraph('1574', S_TC), Paragraph('Mimar Sinan Selimiye Camii\'ni yaklaşık 80 yaşında tamamladı; Edirne', S_TC)],
        [Paragraph('1889', S_TC), Paragraph('Eiffel Kulesi inşa edildi; demir-çelik yapı mühendisliğinin sembolü', S_TC)],
        [Paragraph('1919', S_TC), Paragraph('Bauhaus okulu kuruldu; "biçim işlevi izler" ilkesi', S_TC)],
        [Paragraph('1930\'lar', S_TC), Paragraph('Le Corbusier "ev yaşamak için makine" anlayışını yaydı; modernizm yükseldi', S_TC)],
        [Paragraph('1950\'ler', S_TC), Paragraph('Sedad Hakkı Eldem Türk evi araştırmasını yayımladı', S_TC)],
        [Paragraph('1972', S_TC), Paragraph('Pruitt-Igoe sosyal konut bloklarının yıkılması; modernizmin iflası olarak yorumlandı', S_TC)],
        [Paragraph('1991', S_TC), Paragraph('Zaha Hadid ilk büyük projesini kazandı; parametrik mimari başladı', S_TC)],
        [Paragraph('1994', S_TC), Paragraph('Safranbolu UNESCO Dünya Mirası Listesi\'ne alındı', S_TC)],
        [Paragraph('2005', S_TC), Paragraph('Türkiye\'de 5378 sayılı Engelliler Kanunu yürürlüğe girdi', S_TC)],
        [Paragraph('2010\'lar', S_TC), Paragraph('BIM (Building Information Modeling) yaygınlaştı; dijital maket yerleşik standart oldu', S_TC)],
    ]
    kron_t = Table(kron_data, colWidths=[CW*0.16, CW*0.84])
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
    e += bolum_baslik(4, 'GÜNCEL DURUM: MİMARLIK BUGÜN NEREDE?')

    e.append(Paragraph('4.1 Parametrik Mimari: Bilgisayarın Şekillendirdiği Formlar', S_H2))
    e.append(Paragraph(
        'Parametrik tasarımda mimar bir formu doğrudan çizmez; bir kurallar sistemi tanımlar. '
        '"Bu kubbenin yarıçapı, ışık açısına göre değişsin" gibi. Sonuç, elle çizilemeyecek '
        'karmaşıklıkta formlar olabilir.', S_BD))
    e.append(Paragraph(
        'Zaha Hadid Architects\'in binaları bu yaklaşımın en bilinen örnekleridir. '
        'İstanbul\'daki Koç Üniversitesi ANAMED binası Türkiye\'de parametrik tasarımın '
        'uygulandığı yapılardandır.', S_BD))

    e.append(Paragraph('4.2 Yeşil Bina Hareketi: Rakamlarla', S_H2))
    e.append(Paragraph(
        'Dünya genelinde binaların enerji tüketiminden yaklaşık yüzde kırkından sorumlu '
        'olduğu tahmin edilmektedir. Bu nedenle inşaat sektörü iklim değişikliğiyle '
        'mücadelede kritik bir alan haline geldi.', S_BD))
    e.append(Paragraph(
        '<b>Türkiye\'de tablo:</b> Türkiye\'de son yıllarda yeşil bina sertifikası alan '
        'yapıların sayısı hızla artmaktadır. İstanbul Finans Merkezi, LEED Platin '
        'sertifikasıyla Türkiye\'nin en büyük yeşil bina projelerinden biri oldu.', S_BD))

    e.append(Paragraph('4.3 Turgut Cansever: Türkiye\'den Dünyaya', S_H2))
    e.append(Paragraph(
        'Turgut Cansever (1920-2009), Türk mimarlığının 20. yüzyıldaki en özgün isimlerinden '
        'biridir. Ağa Han Mimarlık Ödülü\'nü iki kez (1980 ve 1992) kazanmıştır — Türkiye\'den '
        'bu ödülü iki kez alan tek kişidir.', S_BD))
    e.append(Paragraph(
        'Cansever\'in felsefesi: Modern teknoloji ile İslam-Osmanlı mekân anlayışını '
        'uzlaştırmak. Demir dövme, ahşap oymacılık gibi geleneksel ustalık dallarını çağdaş '
        'binayla bütünleştirdi. Restore ettiği tarihi evler ve Bodrum\'daki Demir Evleri '
        'bu felsefenin somut örnekleridir.', S_BD))

    return e


# ============================================================
# BÖLÜM 5 — DİSİPLİNLERARASI BAĞLANTI
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'DİSİPLİNLERARASI BAĞLANTI')

    e.append(Paragraph('5.1 Coğrafya ve Sosyal Bilgiler: İklim Bölgeleri', S_H2))
    e.append(Paragraph(
        'Bölgesel mimariyi anlamak için Türkiye\'nin iklim bölgelerini bilmek şarttır:', S_BD))
    iklim_liste = [
        'Karadeniz\'in yüksek yağışı → ahşap malzeme, dik çatı',
        'İç Anadolu\'nun karasal iklimi → kerpiç ve taş, küçük pencere',
        'Akdeniz\'in sıcak-kuru yazı → açık avlu, ince duvar, geniş saçak',
        'Güneydoğu\'nun sıcak-kurak iklimi → sarı kireç taşı, iç avlu, düz teras çatı',
    ]
    for i in iklim_liste:
        e.append(Paragraph(f'• {i}', S_BUL))
    e.append(Paragraph(
        '"Bir bölgenin evlerine bakarak o bölgenin iklimini, tarihini ve ekonomisini okumak '
        'mümkündür" — ders boyunca kullanılabilecek güçlü bir çerçeve.', S_NOT))

    e.append(Paragraph('5.2 Matematik: Ölçek, Alan ve Oran', S_H2))
    e.append(Paragraph(
        'Kat planı çizimi matematiği zorunlu kılar:', S_BD))
    mat_liste = [
        '<b>Ölçek hesabı:</b> Gerçek ölçü (cm) ÷ 50 = kağıttaki ölçü (cm). 5 m\'lik bir oda kağıtta 10 cm olur.',
        '<b>Alan hesabı:</b> Odanın gerçek alanı = (plan ölçüsü × 50)² / 10000 m²',
        '<b>Oran:</b> Kapı yüksekliğinin genişliğe oranı, merdiven basamağının yükseklik-derinlik oranı',
    ]
    for m in mat_liste:
        e.append(Paragraph(f'• {m}', S_BUL))
    e.append(Paragraph(
        'Bu hesaplar canlı ve bağlamsal matematik pratiğidir. Öğrenci neden hesap yaptığını '
        'bilir — planı doğru çizmek için.', S_BD))

    e.append(Paragraph('5.3 Fen Bilgisi: Isı ve Malzeme', S_H2))
    fen_liste = [
        '<b>Isıl kütle:</b> Taş ve beton yavaş ısınır, yavaş soğur — yazın serin, kışın ılık tutar. Ahşap daha hızlı ısınır ama daha hızlı soğur.',
        '<b>Yalıtım:</b> Hava cepleri ısı geçişini yavaşlatır — çift cam, taş yünü yalıtım, hava boşluklu duvar bu ilkeyi kullanır.',
        '<b>Güneş enerjisi:</b> Güneye açık bir pencere kışın pasif ısıtma sağlar; doğru hesaplanmış saçak yazın güneşi keser, kışın içeriye alır.',
    ]
    for f in fen_liste:
        e.append(Paragraph(f'• {f}', S_BUL))

    e.append(Paragraph('5.4 Matematik: Fibonacci ve Altın Oran Mimaride', S_H2))
    e.append(Paragraph(
        'Mimari cephelerde orantı önemlidir. Pek çok tarihi yapıda altın orana yakın oranlar '
        'bulunabilir — ama bu bilinçli uygulama mı yoksa sezgisel sonuç mu olduğu tartışmaya '
        'açıktır. Öğrencilere şunu sormak verimlidir: "Güzel bulduğunuz bir binanın '
        'fotoğrafında oranları sayar mısınız?"', S_BD))

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
        ('"Mimar sadece binaların dışını tasarlar — estetik kararlar alır."',
         'Mimar hem iç hem dış mekânı, hem yapıyı hem altyapıyı tasarlar. Yapısal hesap, '
         'ısıtma sistemi yerleşimi, erişilebilirlik düzenlemeleri hepsi mimarın kararlarıdır.'),
        ('"Güzel bina = pahalı bina."',
         'Safranbolu evleri ya da Mardin taş yapıları dönemin en yaygın ve ucuz malzemiyle '
         'yapılmıştır. Güzellik orantı, bağlam uyumu ve ustalıktan gelir, pahalı malzemeden değil.'),
        ('"Kat planı sadece üstten görünüş çizimidir — 3B düşünmeye gerek yok."',
         'Kat planı, üç boyutlu bir mekânın iki boyutlu anlatımıdır. İyi kat planı okuması, '
         'zihinsel olarak o mekânda dolaşabilmeyi gerektirir. Kapı yayları hangi yöne açılır? '
         'Pencere hangi cepheye bakar? Bunlar 3B sorulardır.'),
        ('"Erişilebilirlik yalnızca tekerlekli sandalye kullananlar içindir."',
         'Erişilebilirlik herkese yarar: rampa bebek arabası iten ebeveyn için, sesli uyarı '
         'gözlük kıran biri için de kolaylık sağlar. "Universal Design" felsefesi bunu '
         'herkes için tasarım olarak tanımlar.'),
        ('"Türk mimarisi Osmanlı mimarisidir — Selimiye ve Süleymaniye."',
         'Türkiye\'de bölgeden bölgeye radikal farklılıklar gösteren zengin bir sivil mimari '
         'geleneği vardır: Karadeniz ahşap evleri, Ege bağ evleri, Mardin taş yapıları, '
         'Erzurum taş hanları. Osmanlı anıt mimarisi bu çeşitliliğin yalnızca bir boyutudur.'),
        ('"Sürdürülebilir mimari yeni bir kavramdır."',
         'Geleneksel mimari zaten sürdürülebilirdi — başka türlü yapılamazdı çünkü uzak malzeme '
         'taşımak mümkün değildi. Kalın taş duvarlar ısı yalıtımı, iç avlular doğal '
         'havalandırma, çatıdan toplanan su kaynaktı. Modern sürdürülebilirlik bu bilgeliği '
         'yeniden keşfediyor.'),
        ('"Maket yapımı son aşamadır — önce tasarım bitince maket yapılır."',
         'Maketler tasarım sürecinin ortasında da yapılır; kararları test etmek ve yanlışları '
         'erken görmek için. Işığın pencereden nasıl girdiğini, odaların oranını bir maket '
         'çok daha net ortaya koyar.'),
        ('"Ölçek ve oran aynı şeydir."',
         'Ölçek, gerçek boyutun çizim boyutuna oranıdır (1:50 gibi sayısal). Oran ise iki '
         'boyut arasındaki ilişkidir (kapının genişlik-yükseklik ilişkisi gibi). Bir planda '
         'ölçek doğru olabilir ama oranlar kötü seçilmiş olabilir.'),
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
        'İki Kubbenin Mücadelesi — Sinan ve Ayasofya',
        ['Mimar Sinan Edirne\'ye gönderildiğinde yaklaşık 80 yaşına geliyordu. Hedefi netti: '
         'Osmanlı\'nın, Bizans\'ın en büyük yapısı olan Ayasofya\'yı aşması gerekiyordu.',
         'Rakamlar ona kâbus gibiydi: Ayasofya\'nın kubbe çapı 31,87 metreydi. Sinan 31,25 '
         'metre ile kapandı — 62 santimetre geride.',
         'Ama Sinan farklı bir soru sordu: Büyük olmak mı önemli, yoksa daha iyi olmak mı? '
         'Ayasofya\'nın içindeki taşıyıcılar iç mekânı parçalıyor. Sinan Selimiye\'de 8 sütun '
         'üzerine oturan kubbe altında tamamen bölünsüz bir iç mekân yarattı — tek bir nefes '
         'gibi akan hacim.',
         'Bugün mimarlık tarihçilerinin büyük çoğunluğu Selimiye\'yi teknik açıdan daha büyük '
         'bir başarı saymaktadır. Çünkü Sinan ölçekte değil, fikirdeydi.'],
        'Bağlantı: "İyi tasarım kısıtları aşmaz, onlarla yaratıcı olur." Aynı zamanda Türk '
        'mimarisi için gurur ve özgüven kaynağı.'))

    e.append(hikaye(
        'Demirin Şiiri — Eiffel Kulesi\'ne Kimse Güvenmedi',
        ['1886\'da Paris\'in önde gelen sanatçı ve aydınları bir imza kampanyası başlattı. '
         'Dilekçeyi 300 kişi imzaladı. İçeriği şuydu: "Bu metal çirkinliği Paris siluetini '
         'mahvedecek."',
         'Kule 1889 Paris Fuarı için inşa edilmişti ve 20 yıl sonra yıkılması planlanıyordu. '
         'Gustave Eiffel dinlemedi.',
         '20 yıl dolduğunda kule yıkılmadı: telgraf ve radyo anteni olarak son derece '
         'kullanışlıydı. Yıkılmak yerine hayatta kaldı.',
         'Bugün Eiffel Kulesi dünyanın en çok ziyaret edilen yapılarından biridir. '
         'Ve o 300 imzacının adını kimse hatırlamıyor.'],
        'Bağlantı: Yeni bir yapı ya da tasarım ilk görüldüğünde sıklıkla reddedilir. '
        '"Bu çirkin" ile "Bu yanlış" farklı şeylerdir.'))

    e.append(hikaye(
        'Gece Yarısı Parisiyle Koşuşturmak — Le Corbusier\'nin Yanılgısı',
        ['Le Corbusier 1925\'te "Plan Voisin" adlı projesini açıkladı: Paris\'in tarihi '
         'merkezini yıkıp yerine 18 adet eşit yükseklikte cam kule dikmek.',
         'Geniş yeşil alanlar, geniş caddeler, verimli ışık — kâğıt üzerinde mükemmeldi. '
         'Paris\'teki dar sokaklar, tarihi binalar, insanlar arası temas, fırının kokusu, '
         'komşunun sesi — bunlar hesaba katılmamıştı.',
         'Proje hiç uygulanmadı. Ama benzeri fikirler 1960\'ların sosyal konut bloklarına '
         'ilham verdi. Ve o blokların büyük çoğunluğu bugün ya yıkılmış ya da sorunlu '
         'mekânlar olarak bilinmektedir.'],
        'Bağlantı: "Kâğıt üzerinde mükemmel olan tasarım, insan hayatında mükemmel olmayabilir." '
        'İşlevsellik tek ölçüt değildir; insanın sosyal ihtiyaçları ve tarihsel bağ da önemlidir.'))

    e.append(hikaye(
        'Hastane Tuvalet Kapısının Yönü — Küçük Kararın Büyük Sonucu',
        ['Standart bir konut tuvaletinin kapısı içeriye doğru açılır. Ama hastane ve kamu '
         'binalarındaki tuvalet kapılarının büyük çoğunluğu dışarıya açılır. Neden?',
         'Çünkü içeride birinin bayıldığını düşünün. Kapı içeriye açılıyorsa o kişi kapının '
         'önüne düşerse kapı açılamaz. Dışarıya açılan kapıda bu sorun yoktur.',
         'Bu karar estetik değil, ergonomik ve güvenlik odaklıdır. Hiçbir kullanıcı fark '
         'etmez; ama bir acil durumda hayat kurtarır.'],
        'Bağlantı: İyi mimari kararları çoğu zaman görünmez. Görülenlerin arkasında sayısız '
        'görünmez karar vardır. "Tasarım sorun çözmektir" ilkesinin mimari bağlamdaki somut örneği.'))

    e.append(hikaye(
        'Termitlerden Öğrenilen Bina — Eastgate Centre',
        ['Harare, Zimbabwe\'nin en büyük alışveriş merkezlerinden biri olan Eastgate Centre, '
         '1996\'da mimar Mick Pearce tarafından tasarlandı. Bina merkezi iklimlendirme sistemi '
         'olmadan çalışır.',
         'Pearce bu başarının sırrını Afrika termitlerinden öğrendi. Termit yuvaları iç '
         'sıcaklığı 31 derece tutarak dışarıdaki 40 derecelik sıcakta sabit kalır. Termitler '
         'bunu baca ve tünel sistemiyle sağlar: gece soğuk hava içeri alınır, gündüz yavaşça '
         'dışarı verilir.',
         'Pearce aynı prensibi binaya uyarladı: betonda toplanan gece soğukluğu gündüz binayı '
         'serin tutar. Sonuç: Karşılaştırılabilir büyüklükteki binadan yüzde elli daha az '
         'enerji tüketen bir yapı.'],
        'Bağlantı: Sürdürülebilir mimari ile doğadan öğrenmenin (biyomimikri) buluşması. '
        '6. Ünite\'ye de köprü kurar.'))

    e.append(hikaye(
        'Sürgündeki Mimar — Jorn Utzon ve Sydney Opera House',
        ['1957\'de 233 tasarım arasından seçilen Danimarkalı genç mimar Jorn Utzon\'un Sydney '
         'Opera House projesi, teknik olarak "imkânsız" sayılıyordu. Birbiri üzerine binen '
         'beyaz kabuklar o güne kadar hesaplanamamış bir formdu.',
         'İnşaat 14 yıl sürdü, bütçe 14 katına çıktı. Utzon Avustralyalı yetkililerle '
         'anlaşmazlığa düştü ve 1966\'da görevden ayrıldı. İnşaat başkalarının yönetiminde '
         'tamamlandı.',
         '2003\'te Utzon mimarlığın Nobel\'i olan Pritzker Ödülü\'nü aldı. Jüri gerekçesinde '
         'Sydney Opera House\'u "dünya mimarisinin ikonları arasında" saydı. Utzon ödülü '
         'hayatta alabildi; ama kendi tasarladığı binaya hiç gidemedi. 2008\'de hayatını '
         'kaybetti.'],
        'Bağlantı: Tasarım vizyonu ile uygulama gerçekliği arasındaki gerilim. Bir tasarımın '
        'değeri, onu tasarlayanın hayattayken görüp göremediğinden bağımsızdır.'))

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
        ('"Mimarlar her şeyi düşünüyor ama depremde binalar yine de yıkılıyor — neden?"',
         'Mühendislik ve mimarlık her döneme ait bilginin sınırları içinde çalışır. 1960\'larda '
         'inşa edilen bir binanın tasarımcısı o günün deprem yönetmeliğine uymaktaydı — bugünün '
         'bilgisiyle bakıldığında yetersiz olan yönetmeliklere. Türkiye 1999 Marmara depremi '
         'sonrasında deprem yönetmeliğini köklü biçimde güncelledi. Bir binanın sağlamlığı '
         'yalnızca mimarın kararına değil, inşaat kalitesine, zemin koşullarına ve denetimin '
         'etkinliğine bağlıdır.'),
        ('"Türkiye\'nin her yerinde aynı tip apartmanlar var — neden bölgesel mimari kalmadı?"',
         '20. yüzyılda hızlı kentleşme, standartlaşmış inşaat tekniklerini ve malzeme '
         'tedarik zincirlerini yaygınlaştırdı. Betonarme ucuz, hızlı ve üreticisi kolay '
         'ulaşılabilir bir sistem olduğu için tercih edildi. Bu süreç Türkiye\'ye özgü değil; '
         'dünyanın büyük çoğunluğunda görülen bir sanayileşme etkisidir. Ama son yıllarda '
         'tersine bir eğilim de gözleniyor: Turgut Cansever ve Sedad Hakkı Eldem bu yolun '
         'öncüleridir.'),
        ('"Kat planı çizerken ölçek yanlış olursa ne olur?"',
         '1:50 ölçeğinde 1 cm\'lik hata, gerçekte 50 cm\'e karşılık gelir. 50 santimetre; '
         'bir kapının tam kapanmaması, bir mobilyanın odaya sığmaması ya da koridorun '
         'tekerlekli sandalyeye dar gelmesi anlamına gelebilir. Mimaride hassasiyet, '
         'estetik değil güvenlik ve kullanılabilirlik meselesidir.'),
        ('"Erişilebilir bina yapmak çok pahalı — küçük okullarda bunu yapmak mümkün mü?"',
         'Erişilebilirlik eklenti olarak değil, tasarımın başından düşünüldüğünde çok daha '
         'ucuza mal olur. Bir binayı tamamladıktan sonra rampa eklemek, başından tasarlamaktan '
         '5-10 kat daha pahalıdır. Yeni yapılan okulların büyük çoğunluğu Türk standartlarına '
         'göre erişilebilir tasarlanmak zorundadır. Mevcut binalarda ise sınırlı bütçeyle de '
         'yapılabilecekler vardır: taktil zemin, kapı genişletme, geçici rampa.'),
        ('"Safranbolu gibi tarihi binalar bugün nasıl ayakta kaldı — onları kim korudu?"',
         'Bir kısmı korundu çünkü Safranbolu gibi bazı bölgeler ticaret güzergahlarından '
         'dışlandı; bu onları "modern" yıkım-yeniden yapım döngüsünden korudu. UNESCO tescili '
         'ise 1994\'ten itibaren restorasyon yapmaya teşvik etti. Ama gerçek şu ki tarihi '
         'yapıların büyük çoğunluğu kayboldu — bugün görülenler kurtulanlar. Korunma tesadüf, '
         'ilgisizlik veya bilinçli müdahalenin karışık sonuçlarıdır.'),
        ('"Biyomimikri mimarisi güzel görünüyor ama gerçekten işe yarıyor mu?"',
         'Eastgate Centre gibi örnekler enerji tasarrufunu ölçülebilir biçimde kanıtlamıştır. '
         'Ama biyomimikri uygulamalarının tümü bu kadar net sonuç vermez. Bir termit yuvasının '
         'çalışma prensibini bir binaya uyarlamak mümkün, ama o binanın insanların kullanım '
         'alışkanlıkları ve şehrin iklimiyle birlikte çalışıp çalışmayacağı ayrı bir test '
         'gerektirir. Bilim ve mühendislik doğadan ilham alabilir; ama doğayı kopyalamak '
         'çözüm değil, başlangıç noktasıdır.'),
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
        title='5. Unite - Ogretmen Hazirlik Rehberi',
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
    print('OK  U5_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
