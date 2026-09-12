# -*- coding: utf-8 -*-
"""
1. Unite - Zenginlestirme Paketi (Kombine)
Calistirir: python pdf_uretim/uret_unite1_zenginlestirme.py

Uretilen PDF: units/7_sinif/unit1/U1_Zenginlestirme_Paketi_Kombine.pdf
- Kapak sayfasi YOK
- 7 etkinlik, her biri bir sayfada
"""

import sys
import os
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
    register_fonts, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines,
)

register_fonts()

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, 'units', 'unit1')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U1_Zenginlestirme_Paketi_Kombine.pdf')
UI    = 'Teknoloji ve Tasarım - 7. Sınıf - 1. Ünite: Zenginleştirme Paketi'

# ============================================================
# STİLLER — çok kompakt
# ============================================================

S_ETK   = ParagraphStyle('z_ETK',  fontName='TR-Bold',    fontSize=11, textColor=white,
                          leading=14, alignment=TA_LEFT,
                          backColor=COLOR_PRIMARY, borderPad=5,
                          spaceBefore=0, spaceAfter=4)
S_META  = ParagraphStyle('z_META', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=3)
S_BSL   = ParagraphStyle('z_BSL',  fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceBefore=5, spaceAfter=2)
S_GOV   = ParagraphStyle('z_GOV',  fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=3, alignment=TA_JUSTIFY,
                          backColor=COLOR_VERY_LIGHT, leftIndent=5, rightIndent=5,
                          borderPad=4)
S_BODY  = ParagraphStyle('z_BODY', fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=2, alignment=TA_JUSTIFY)
S_BULL  = ParagraphStyle('z_BULL', fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1, leftIndent=12, bulletIndent=4)
S_NOTE  = ParagraphStyle('z_NOTE', fontName='TR-Italic',  fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=2)
S_LABEL = ParagraphStyle('z_LBL',  fontName='TR-Bold',    fontSize=8, textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1)
S_FILL  = ParagraphStyle('z_FILL', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=0)

def vsp(h=0.15):
    return Spacer(1, h * cm)

def hr(color=COLOR_LIGHT_GREY, thickness=0.4):
    return HRFlowable(width='100%', thickness=thickness, color=color, spaceAfter=3, spaceBefore=3)

def etkinlik_baslik(no, baslik, tur=None, sure=None, degerlendirme=None):
    """Etkinlik başlık bloğu — turuncu arka plan + meta satırı"""
    blok = []
    blok.append(Paragraph(f'ETKİNLİK {no}: {baslik}', S_ETK))
    meta_parts = []
    if tur:
        meta_parts.append(f'Tür: {tur}')
    if sure:
        meta_parts.append(f'Süre: {sure}')
    if degerlendirme:
        meta_parts.append(f'Değerlendirme: {degerlendirme}')
    if meta_parts:
        blok.append(Paragraph('  |  '.join(meta_parts), S_META))
    return blok

def degerlendirme_tablosu(olcutler):
    """Değerlendirme tablosu. olcutler: list of (str, int)"""
    data = [['Ölçüt', 'Puan']]
    for olcut, puan in olcutler:
        data.append([Paragraph(olcut, ParagraphStyle('dt_cell', fontName='TR-Regular', fontSize=7.5,
                                                      textColor=COLOR_TEXT, leading=10)),
                     str(puan)])
    data.append([Paragraph('<b>TOPLAM</b>', ParagraphStyle('dt_tot', fontName='TR-Bold', fontSize=7.5,
                                                            textColor=COLOR_TEXT, leading=10)),
                 '100'])
    t = Table(data, colWidths=[13.5*cm, 1.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR',     (0, 0), (-1, 0), white),
        ('FONTNAME',      (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTSIZE',      (0, 0), (-1, 0), 7.5),
        ('ALIGN',         (1, 0), (1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS',(0, 1), (-1, -2), [white, COLOR_VERY_LIGHT_GREY]),
        ('BACKGROUND',    (0, -1), (-1, -1), COLOR_LIGHT),
        ('FONTNAME',      (0, -1), (-1, -1), 'TR-Bold'),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 1, COLOR_SECONDARY),
    ]))
    return t

def fill_line(label):
    """Doldurma satırı: 'label ___________'"""
    return [
        Paragraph(label, S_LABEL),
        WritingLines(num_lines=1, line_spacing=14),
        vsp(0.05),
    ]

# ============================================================
# ETKİNLİK 1: 2040 SENARYOSU
# ============================================================

def etkinlik1():
    E = []
    E += etkinlik_baslik(1, '2040 SENARYOSU',
                         tur='Yaratıcı yazma + araştırma',
                         sure='1 hafta',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Sen 2040 yılında yaşıyorsun. Endüstri 5.0\'in tüm sonuçları hayatımıza girmiş. '
        'Aile büyüğün sana sorar: "Evladım, sen küçükken (2026\'da) hayat nasıldı? '
        'Biz o zaman ne farklıydık, şimdi ne farklıyız?"',
        S_GOV))
    E.append(vsp(0.1))

    E.append(Paragraph('Senaryo Yazma Yönergesi', S_BSL))
    yonerge = [
        '1500–2000 kelime arasında bir günlük hikâye yaz. Hikâyende şunlar olmalı:',
        '• Sabah uyandığında çevrenizdeki teknoloji nasıl?',
        '• Okul/iş nasıl değişmiş? Öğrenme/çalışma nerede ve nasıl oluyor?',
        '• İnsan–robot iş birliği nasıl işliyor? (Kobot kavramını kullan)',
        '• Sürdürülebilirlik nasıl sağlanmış? Fosil yakıt hâlâ var mı?',
        '• Sağlık, eğitim, eğlence nasıl dönüşmüş?',
        '• Geçmişe göre bir şey kaybolmuş mu? Nostaljiye neden olan bir şey?',
    ]
    for y in yonerge:
        E.append(Paragraph(y, S_BULL if y.startswith('•') else S_BODY))

    E.append(Paragraph('Zorunlu Kavramlar (en az 8 tanesini bağlamlı şekilde kullan)', S_BSL))
    kavramlar = ('Yapay Zekâ  •  Kobot  •  Endüstri 5.0  •  STEAM  •  Biyomimikri  •  IoT  •  '
                 'Sürdürülebilirlik  •  Antropomorfik robot  •  Dijital ikiz  •  3D yazıcı  •  '
                 'Yenilenebilir enerji  •  Kişiselleştirme')
    E.append(Paragraph(kavramlar, S_BODY))

    E.append(Paragraph('Biçim ve Teslim', S_BSL))
    bicim = [
        '• Başlık: Özgün olsun (örn. "Bilgisayarımın Doğum Günü")',
        '• Sayfa düzeni: A4, Times New Roman 12 punto, 1.15 satır aralığı',
        '• Teslim: Sınıf panosunda sergilenecek + dijital kopya Drive\'a yüklenecek',
    ]
    for b in bicim:
        E.append(Paragraph(b, S_BULL))

    E.append(Paragraph('Değerlendirme', S_BSL))
    E.append(degerlendirme_tablosu([
        ('Kavramların doğru bağlamda kullanımı', 25),
        ('Senaryonun tutarlılık ve iç mantığı', 20),
        ('Yaratıcılık ve özgünlük', 20),
        ('Dil, anlatım, imla', 15),
        ('Geçmişe göre "kayıp" unsurunu yakalamak (eleştirel derinlik)', 10),
        ('Biçim kurallarına uyum', 10),
    ]))

    E.append(vsp(0.1))
    E.append(Paragraph(
        'İpuçları: Aile büyüğüne anlatıyormuş gibi sıcak dil kullan. '
        '"2040 teknoloji tahminleri" araştır. Hem olumlu hem olumsuz yanları göster.',
        S_NOTE))
    return E

# ============================================================
# ETKİNLİK 2: AR-GE KAHRAMANLARI
# ============================================================

def etkinlik2():
    E = []
    E += etkinlik_baslik(2, 'AR-GE KAHRAMANLARI',
                         tur='Araştırma + sunum',
                         sure='2 hafta',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Türkiye\'de Ar-Ge yapan kurumlardan birini seçip derinlemesine araştır ve '
        '10 dakikalık sunum + 4–6 sayfalık yazılı rapor hazırla.',
        S_GOV))
    E.append(vsp(0.1))

    E.append(Paragraph('Araştırılacak Kurumlar (Birini Seç)', S_BSL))
    kurumlar_data = [
        [Paragraph('<b>Kurum</b>', ParagraphStyle('kh', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Alan</b>',  ParagraphStyle('kh', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10))],
        ['ASELSAN',      'Savunma elektroniği, haberleşme sistemleri'],
        ['TUSAŞ / TAI',  'Havacılık, uçak ve helikopter üretimi'],
        ['BAYKAR',       'İnsansız hava araçları (SİHA, İHA)'],
        ['HAVELSAN',     'Yazılım, simülasyon, siber güvenlik'],
        ['ROKETSAN',     'Füze ve roket sistemleri'],
        ['TOGG',         'Yerli otomobil, batarya teknolojisi'],
        ['TÜBİTAK SAGE', 'Füze, havacılık araştırmaları'],
    ]
    kt = Table(kurumlar_data, colWidths=[3.5*cm, 11.5*cm])
    kt.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR',     (0, 1), (-1, -1), COLOR_TEXT),
        ('FONTNAME',      (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',      (0, 1), (-1, -1), 7.5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 1, COLOR_SECONDARY),
    ]))
    E.append(kt)
    E.append(vsp(0.1))

    E.append(Paragraph('Araştırma Başlıkları', S_BSL))
    arastirma = [
        '1. Kuruluş Hikâyesi: Ne zaman, kim tarafından, hangi amaçla kuruldu?',
        '2. Mevcut Durum: Kaç çalışanı var? Hangi ülkelere ihracat yapılıyor? Son 5 yılın 3 önemli ürünü?',
        '3. Ar-Ge Harcamaları: Gelirinin yüzde kaçı Ar-Ge\'ye ayrılmakta? Dünya ortalamasıyla karşılaştır.',
        '4. İnsan Kaynağı: Mühendis/teknisyen sayısı, üniversite iş birlikleri.',
        '5. Gelecek Hedefleri: 2030 hedefleri, yeni ürünler.',
        '6. Gençler için Mesaj: Bu kurumda çalışmak isteyenler bugün neleri geliştirmeli?',
    ]
    for a in arastirma:
        E.append(Paragraph(a, S_BULL))

    E.append(Paragraph('Çıktı Gereksinimleri', S_BSL))
    cikti = [
        '• 10 dakikalık sunum (en az 5 görsel)',
        '• 4–6 sayfalık yazılı rapor (en az 5 güvenilir kaynak, APA formatı)',
    ]
    for c in cikti:
        E.append(Paragraph(c, S_BULL))

    E.append(Paragraph('Değerlendirme', S_BSL))
    E.append(degerlendirme_tablosu([
        ('Araştırma derinliği', 25),
        ('Kaynak çeşitliliği ve güvenilirliği', 20),
        ('Sunum akıcılığı', 20),
        ('Görsel kullanımı', 15),
        ('Özgün yorumlar / kişisel bakış', 10),
        ('Zaman yönetimi', 10),
    ]))
    return E

# ============================================================
# ETKİNLİK 3: KAVRAM İLİŞKİ AĞI
# ============================================================

def etkinlik3():
    E = []
    E += etkinlik_baslik(3, 'KAVRAM İLİŞKİ AĞI',
                         tur='İleri düzey kavramsal çalışma',
                         sure='3–4 ders',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Ünite 1\'deki 15 kavram arasındaki tüm anlamlı ilişkileri görselleştir. '
        'Bu bir kavram haritasından daha karmaşık — kavramların birbirini nasıl etkilediğini, '
        'ürettiğini, gerektirdiğini ortaya koy.',
        S_GOV))
    E.append(vsp(0.1))

    E.append(Paragraph('Yönerge', S_BSL))
    yonerge = [
        '1. A3 boyutunda kâğıda 15 kavram dağılımlı şekilde yerleştir.',
        '2. Her çift kavram arasında ilişki olup olmadığını sorgula.',
        '3. Varsa ok çiz ve ilişkinin türünü yaz. Hedef: en az 30 anlamlı ilişki.',
    ]
    for y in yonerge:
        E.append(Paragraph(y, S_BULL))

    E.append(Paragraph('İlişki Türleri', S_BSL))
    ilişki_data = [
        [Paragraph('<b>Simge</b>', ParagraphStyle('ih', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Tür</b>',   ParagraphStyle('ih', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Örnek</b>', ParagraphStyle('ih', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10))],
        ['->',   'Neden olur / üretir',        'Bilim -> Teknoloji'],
        ['<->', 'Karşılıklı etkiler',           'Tasarım <-> Estetik'],
        ['C',   'Kapsar / alt kümedir',         'End. Tasarım C Tasarım'],
        ['!=',  'Karıştırılır ama farklıdır',   'Buluş != İcat'],
        ['=>',  'Birlikte gelişir',             'Yapay Zekâ => Endüstri 4.0'],
        ['örn.','Örneğidir',                    'Grafik Tasarım örn. Afiş'],
    ]
    it = Table(ilişki_data, colWidths=[1.5*cm, 5*cm, 8.5*cm])
    it.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('FONTNAME',      (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',      (0, 1), (-1, -1), 7.5),
        ('TEXTCOLOR',     (0, 1), (-1, -1), COLOR_TEXT),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 1, COLOR_SECONDARY),
        ('ALIGN',         (0, 1), (0, -1), 'CENTER'),
    ]))
    E.append(it)
    E.append(vsp(0.1))

    E.append(Paragraph('Kâğıt Formatı', S_BSL))
    format_items = [
        '• A3 boyut (yatay), 15 kavram farklı renkli balonlarda',
        '• Oklar ve ilişki simgeleri mutlaka açıklayıcı olmalı',
        '• Her ok için 1 cümlelik gerekçe yanına yazılmalı',
    ]
    for f in format_items:
        E.append(Paragraph(f, S_BULL))

    E.append(Paragraph('Örnek İlişkiler', S_BSL))
    E.append(Paragraph(
        'Bilim → Teknoloji (neden olur)  •  End. 4.0 ⇄ Yapay Zekâ (birlikte gelişir)  '
        '•  İcat ≠ Keşif (karıştırılır)  •  STEAM ⊃ Bilim + Teknoloji + Müh. + Sanat + Mat.',
        S_NOTE))

    E.append(Paragraph('Değerlendirme', S_BSL))
    E.append(degerlendirme_tablosu([
        ('İlişkilerin sayısı (min. 30)', 20),
        ('İlişkilerin doğruluğu', 25),
        ('Gerekçelerin kalitesi', 20),
        ('Görsel düzen ve okunabilirlik', 15),
        ('Özgün bağlantılar (beklenmedik ilişkiler)', 20),
    ]))
    return E

# ============================================================
# ETKİNLİK 4: ÇELİŞKİ ANALİZİ
# ============================================================

def etkinlik4():
    E = []
    E += etkinlik_baslik(4, '"BİRİ YANILIYOR" ÇELİŞKİ ANALİZİ',
                         tur='Eleştirel düşünme',
                         sure='1 ders',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        '"Yapay zekânın gelecekte insan işlerini elinden alıp almayacağı" konusunda üç farklı yazar '
        'üç farklı görüş belirtmiş. Kaynaklar: bilimsel dergi makalesi, gazete köşe yazısı, sosyal medya paylaşımı. '
        'Görevin: çelişkiyi çözmek ve kendi kanaatini oluşturmak.',
        S_GOV))
    E.append(vsp(0.1))

    E.append(Paragraph('Analiz Şablonu', S_BSL))
    ana_data = [
        [Paragraph('<b>Soru</b>',       ParagraphStyle('ah', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Kaynak 1</b>',   ParagraphStyle('ah', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Kaynak 2</b>',   ParagraphStyle('ah', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Kaynak 3</b>',   ParagraphStyle('ah', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10))],
        ['Ana iddia ne?', '', '', ''],
        ['Hangi kanıtları sunuyor?', '', '', ''],
        ['Uzmanlık alanı var mı?', '', '', ''],
        ['Tarafsız mı, duygusal mı?', '', '', ''],
        ['Hangi varsayımlar üzerine kurulu?', '', '', ''],
        ['Güçlü / zayıf noktaları?', '', '', ''],
    ]
    cell_s = ParagraphStyle('ac', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT, leading=10)
    for i in range(1, len(ana_data)):
        ana_data[i][0] = Paragraph(ana_data[i][0], cell_s)
    at = Table(ana_data, colWidths=[4.5*cm, 3.5*cm, 3.5*cm, 3.5*cm])
    at.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('FONTNAME',      (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',      (0, 1), (-1, -1), 7.5),
        ('TEXTCOLOR',     (0, 1), (-1, -1), COLOR_TEXT),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 1, COLOR_SECONDARY),
    ]))
    E.append(at)
    E.append(vsp(0.1))

    E.append(Paragraph('Kanaat Yazısı (400–500 kelime)', S_BSL))
    kanaat_items = [
        '• Kaynakların temel farkları neydi?',
        '• Sence hangi kaynak daha güvenilir? Neden?',
        '• Hepsi yanılıyor olabilir mi? Neden?',
        '• Senin kendi görüşün ne? Hangi gerekçelerle?',
    ]
    for k in kanaat_items:
        E.append(Paragraph(k, S_BULL))

    E.append(Paragraph('Değerlendirme', S_BSL))
    E.append(degerlendirme_tablosu([
        ('Tablo analizinin derinliği', 25),
        ('Kaynaklar arası tutarsızlığı yakalama', 20),
        ('Eleştirel düşünme', 20),
        ('Kendi kanaatinin gerekçelendirilmesi', 25),
        ('Yazı dili', 10),
    ]))
    return E

# ============================================================
# ETKİNLİK 5: MİNİ TED KONUŞMASI
# ============================================================

def etkinlik5():
    E = []
    E += etkinlik_baslik(5, 'MİNİ TED KONUŞMASI',
                         tur='Sunum',
                         sure='1–2 hafta',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Ünite 1\'deki bir kavram hakkında 5 dakikalık TED tarzı bir konuşma hazırla ve sınıfa sun.',
        S_GOV))
    E.append(vsp(0.1))

    E.append(Paragraph('TED Konuşmasının Kuralları', S_BSL))
    kurallar = [
        '• Hikâye ile başla — anekdot, soru veya gözlem',
        '• Tek ana fikir — seyircinin aklından çıkmayacak',
        '• Somut örnekler ve veriler',
        '• Eyleme çağrı ile bitir — "Bu bilgiyle sen ne yapacaksın?"',
    ]
    for k in kurallar:
        E.append(Paragraph(k, S_BULL))

    E.append(Paragraph('Konu Örnekleri', S_BSL))
    konular = ('"Yapay Zekânın Gizli Tarafı"  •  "Biz Tasarımcılar Dünyayı Nasıl Değiştiriyoruz"  '
               '•  "Endüstri 5.0 Neden Geçmiş Değil"  •  "STEAM Bir Harf Kombinasyonundan Çok Daha Fazlası"')
    E.append(Paragraph(konular, S_NOTE))

    E.append(Paragraph('Hazırlık Süreci', S_BSL))
    hazirlik = [
        '1. Araştırma (2–3 gün)',
        '2. Metin yazma (1–2 gün)',
        '3. Slayt hazırlama (maks. 8 slayt, minimum metin)',
        '4. Prova (en az 3 kez)',
        '5. Sunum',
    ]
    for h in hazirlik:
        E.append(Paragraph(h, S_BULL))

    E.append(Paragraph('Sunum Gereksinimleri', S_BSL))
    gereksin = [
        '• 5–6 dakika (kesin süre)  •  6–8 görsel ağırlıklı slayt',
        '• Kâğıttan okuma yok (kartlarla destek verilebilir)',
        '• İsteğe bağlı: Evde kayıt yap, YouTube\'a yükle',
    ]
    for g in gereksin:
        E.append(Paragraph(g, S_BULL))

    E.append(Paragraph('Değerlendirme', S_BSL))
    E.append(degerlendirme_tablosu([
        ('Konunun derinliği', 20),
        ('Konuşmanın hikâyeleştirilmesi', 20),
        ('Beden dili ve sahne hakimiyeti', 15),
        ('Slayt tasarımı', 15),
        ('Zaman kullanımı', 10),
        ('Eyleme çağrı ve etkileyicilik', 20),
    ]))
    E.append(vsp(0.1))
    E.append(Paragraph(
        'En iyi 3 konuşma okul panosunda tanıtılabilir veya okul YouTube kanalında paylaşılabilir.',
        S_NOTE))
    return E

# ============================================================
# ETKİNLİK 6: GELECEĞİN MESLEĞİ TASARIMI
# ============================================================

def etkinlik6():
    E = []
    E += etkinlik_baslik(6, 'GELECEĞİN MESLEĞİ TASARIMI',
                         tur='Tasarım projesi',
                         sure='1 hafta',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Endüstri 4.0 ve 5.0 ile birlikte meslekler değişiyor. '
        'Görevin: 2035\'te var olabilecek yeni bir meslek tasarlamak.',
        S_GOV))
    E.append(vsp(0.05))

    # 2 sütunlu yerleşim: Sol — doldurma alanları, Sağ — tablo + sunum
    sol = []
    sol.append(Paragraph('Meslek Tasarım Şablonu', S_BSL))
    sol += fill_line('1. Meslek Adı:')
    sol += fill_line('2. Bu Meslek Ne İş Yapar?')
    sol.append(WritingLines(num_lines=1, line_spacing=14))
    sol += fill_line('3. Neden Bu Meslek Gerekli Hale Geldi?')
    sol.append(WritingLines(num_lines=1, line_spacing=14))
    sol.append(Paragraph('4. Gerekli Beceriler:', S_LABEL))
    sol += fill_line('   Teknik beceriler:')
    sol += fill_line('   Sosyal-duygusal beceriler:')
    sol += fill_line('   Hangi dersler?')
    sol.append(Paragraph('5. Günlük Hayat Sahnesi (200 kelime):', S_LABEL))
    sol.append(WritingLines(num_lines=3, line_spacing=14))
    sol += fill_line('6. Bu Meslek Hangi Mesleklerin Yerine Geçti?')
    sol += fill_line('7. İş Verenler / Çalışma Ortamı:')
    sol += fill_line('8. Tahmini Maaş Aralığı:')
    sol += fill_line('9. Bu Meslek Sana Çekici Geliyor mu? Neden?')
    sol.append(WritingLines(num_lines=1, line_spacing=14))

    sag = []
    sag.append(Paragraph('Eğitim Yolu', S_BSL))
    egitim_data = [
        [Paragraph('<b>Aşama</b>',       ParagraphStyle('eh', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Süre</b>',         ParagraphStyle('eh', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10)),
         Paragraph('<b>Ne Öğrenilir?</b>',ParagraphStyle('eh', fontName='TR-Bold', fontSize=7.5, textColor=white, leading=10))],
        ['Lise',        '4 yıl', ''],
        ['Üniversite',  '4 yıl', ''],
        ['Uzmanlık',    '2 yıl', ''],
    ]
    et = Table(egitim_data, colWidths=[1.8*cm, 1.3*cm, 4*cm])
    et.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('FONTNAME',      (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',      (0, 1), (-1, -1), 7.5),
        ('TEXTCOLOR',     (0, 1), (-1, -1), COLOR_TEXT),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 3),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 1, COLOR_SECONDARY),
    ]))
    sag.append(et)
    sag.append(vsp(0.2))

    sag.append(Paragraph('Sunum Materyali', S_BSL))
    sag_items = [
        '• Meslek için iş ilanı afişi tasarla (Canva kullanabilirsin)',
        '• Afiş içeriği: Meslek adı, aranan özellikler,',
        '  sunulan imkânlar, ilgi çekici görsel',
    ]
    for s in sag_items:
        sag.append(Paragraph(s, S_BULL))

    sag.append(vsp(0.2))
    sag.append(Paragraph('Değerlendirme', S_BSL))
    sag.append(degerlendirme_tablosu([
        ('Mesleğin özgünlüğü', 25),
        ('İç tutarlılık', 20),
        ('Gerçekçi öngörüler', 20),
        ('Eğitim yolunun detayı', 10),
        ('Afiş tasarımı', 15),
        ('Kişisel yansıtma', 10),
    ]))

    # 2 sütunlu layout
    layout_data = [[sol, sag]]
    lt = Table(layout_data, colWidths=[9.5*cm, 7.5*cm])
    lt.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
    ]))
    E.append(lt)
    return E

# ============================================================
# ETKİNLİK 7: ENDÜSTRİ DEVRİMLERİ TARİH ŞERİDİ
# ============================================================

def etkinlik7():
    E = []
    E += etkinlik_baslik(7, 'ENDÜSTRİ DEVRİMLERİ TARİH ŞERİDİ',
                         tur='Görsel proje',
                         sure='1–2 hafta',
                         degerlendirme='Rubriğe göre 100 puan')
    E.append(vsp(0.1))
    E.append(Paragraph(
        'Endüstri 1.0\'dan 5.0\'a uzanan 250 yıllık süreci görsel ve kavramsal olarak '
        'bir tarih şeridi üzerinde anlat.',
        S_GOV))
    E.append(vsp(0.1))

    E.append(Paragraph('Şerit İçeriği — Her Dönem için:', S_BSL))
    donemler = [
        ('Endüstri 1.0 (~1784)', 'Buhar gücü, buharlı motor, mekanik tezgâh',             'Fabrikaların doğuşu',       '~1 milyar'),
        ('Endüstri 2.0 (~1870)', 'Elektrik, seri üretim; ampul, telefon, otomobil',        'Kentleşme, işçi sınıfı',    '~1.6 milyar'),
        ('Endüstri 3.0 (~1970)', 'Bilgisayar, otomasyon; PC, İnternet, robot',             'Bilgi toplumu',             '~3.7 milyar'),
        ('Endüstri 4.0 (~2011)', 'IoT, yapay zekâ, büyük veri; akıllı fabrikalar, 3D yazıcılar', 'Dijital devrim',    '~7 milyar'),
        ('Endüstri 5.0 (~2020+)','İnsan-makine iş birliği, sürdürülebilirlik; kobotlar, dijital ikizler', 'Kişiselleşme + etik', '~8 milyar'),
    ]
    hdr_s  = ParagraphStyle('dh',    fontName='TR-Bold',    fontSize=7.5, textColor=white,        leading=10)
    cell_s = ParagraphStyle('dc',    fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,   leading=10)
    bold_s = ParagraphStyle('dbold', fontName='TR-Bold',    fontSize=7.5, textColor=COLOR_SECONDARY, leading=10)
    donem_data = [
        [Paragraph('<b>Dönem</b>', hdr_s),
         Paragraph('<b>Anahtar Teknoloji / İcatlar</b>', hdr_s),
         Paragraph('<b>Toplumsal Değişim</b>', hdr_s),
         Paragraph('<b>Nüfus</b>', hdr_s)],
    ]
    for d in donemler:
        donem_data.append([
            Paragraph(d[0], bold_s),
            Paragraph(d[1], cell_s),
            Paragraph(d[2], cell_s),
            Paragraph(d[3], cell_s),
        ])
    dt = Table(donem_data, colWidths=[3.2*cm, 6.5*cm, 3.5*cm, 1.8*cm])
    dt.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
        ('FONTNAME',      (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE',      (0, 1), (-1, -1), 7.5),
        ('TEXTCOLOR',     (0, 1), (-1, -1), COLOR_TEXT),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID',          (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0), 1, COLOR_SECONDARY),
    ]))
    E.append(dt)
    E.append(vsp(0.1))

    E.append(Paragraph('Görsel Form Seçenekleri (Birini Seç)', S_BSL))
    formlar = [
        '1. Klasik Şerit Posteri (A2 yatay)',
        '2. İnteraktif Web Sayfası (Canva veya Padlet)',
        '3. Video Tarih Şeridi (3–5 dakika, iMovie/CapCut)',
        '4. Kart Seti (5 kart, her biri bir dönemi anlatıyor)',
        '5. Dijital Flip Book',
    ]
    for f in formlar:
        E.append(Paragraph(f, S_BULL))

    E.append(Paragraph('Araştırma İpuçları', S_BSL))
    ipuclari = [
        '• Türkiye\'nin endüstri devrimi hikâyesi: hangi dönemde, hangi kurumlar/fabrikalar?',
        '• Osmanlı\'nın son dönemindeki endüstrileşme çabaları',
        '• Atatürk\'ün sanayi atılımları — Sümerbank, Etibank',
        '• TOGG neden önemli? Endüstri 4.0/5.0 bağlamında',
    ]
    for i in ipuclari:
        E.append(Paragraph(i, S_BULL))

    E.append(Paragraph('Değerlendirme', S_BSL))
    E.append(degerlendirme_tablosu([
        ('Bilgi doğruluğu', 20),
        ('Görsel tasarım kalitesi', 20),
        ('Kavramsal bütünlük', 15),
        ('Türkiye boyutunun işlenmesi', 15),
        ('Araştırma derinliği', 15),
        ('Sunum/açıklama', 15),
    ]))
    return E

# ============================================================
# ANA CALISTIRICI
# ============================================================

if __name__ == '__main__':
    doc = SimpleDocTemplate(
        CIKTI,
        pagesize=A4,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm,
        leftMargin=2*cm,
        rightMargin=2*cm,
        title='1. Unite Zenginlestirme Paketi - Kombine',
        author='Teknoloji ve Tasarim Ogretim Programi',
    )
    doc.doc_title = '1. Ünite - Zenginleştirme Paketi (7 Etkinlik)'
    doc.unite_info = UI

    E = []

    fonksiyonlar = [
        ('Etkinlik 1',  etkinlik1),
        ('Etkinlik 2',  etkinlik2),
        ('Etkinlik 3',  etkinlik3),
        ('Etkinlik 4',  etkinlik4),
        ('Etkinlik 5',  etkinlik5),
        ('Etkinlik 6',  etkinlik6),
        ('Etkinlik 7',  etkinlik7),
    ]

    for i, (isim, fonk) in enumerate(fonksiyonlar):
        if i > 0:
            E.append(PageBreak())
        E += fonk()
        print('  OK  ' + isim)

    doc.build(E, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print()
    print('PDF uretildi: ' + CIKTI)
