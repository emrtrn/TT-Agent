# -*- coding: utf-8 -*-
"""
6. Unite - Ogretmen Hazirlik Rehberi
PDF: units/7_sinif/unit6/U6_PDF_Ogretmen_Hazirlik_Rehberi.pdf
Calistir: python pdf_uretim/uret_unite6_ogretmen_hazirlik.py
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
PDF_DIR = os.path.join(ROOT, 'units', 'unit6')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI = os.path.join(PDF_DIR, 'U6_PDF_Ogretmen_Hazirlik_Rehberi.pdf')
UI    = '6. Ünite - Doğadan Tasarıma'
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
        'Bu ünitenin temel kavramları — biyomimikri, biyotaklit, biyomorfizm, biyofili, '
        'doğal seçilim, transfer türleri, sürdürülebilirlik — tasarımın doğadan nasıl '
        'ilham aldığını anlamak için temel çerçeveyi oluşturur.', S_BD))

    # 1.1 Biyomimikri
    e.append(Paragraph('1.1 Biyomimikri', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Doğadaki canlıların milyarlarca yıllık evrim sürecinde geliştirdiği form, '
        'süreç ve sistemlerden ilham alarak yeni ürün, süreç veya çözümler tasarlama pratiği.', S_BD))
    e.append(Paragraph(
        '<b>Köken:</b> Yunanca <i>bios</i> (yaşam) + <i>mimesis</i> (taklit). Terimi modern '
        'anlamda bilim ve tasarım dünyasına kazandıran Janine Benyus\'tur (1997, '
        '"Biomimicry: Innovation Inspired by Nature").', S_BD))
    e.append(bilgi_kutusu(
        'Doğa 3,8 Milyar Yıllık Ar-Ge Laboratuvarıdır',
        ['Doğada "başarısız prototipler" hayatta kalamadı — geriye sadece işlevsel, verimli '
         'çözümler kaldı. Biyomimikri bu birikimden bilinçli olarak yararlanır.',
         'Üç uygulama seviyesi: Form (yapının şeklini taklit), Süreç (biyolojik işleyişi taklit), '
         'Ekosistem (tüm sistemin mantığını tasarıma yansıtma).',
         'Öğrenciler için köprü sorusu: "3,8 milyar yıl boyunca test edilmiş bir çözümü neden '
         'sıfırdan icat etmeye çalışalım?"']))

    # 1.2 Biyotaklit
    e.append(Paragraph('1.2 Biyotaklit', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Bir canlının biyolojik yapısını veya davranışını mühendislik '
        'uygulamalarında birebir taklit etmek. Biyomimetik mühendislik de denir.', S_BD))
    e.append(Paragraph(
        '<b>Biyomimikri ile fark:</b> Biyomimikri daha geniş bir felsefi çerçevedir; '
        'biyotaklit bu felsefenin somut mühendislik uygulamasıdır.', S_BD))
    biyotaklit_liste = [
        'Geko ayağı → nano yapışkan yüzey (van der Waals kuvveti)',
        'Köpek balığı derisi → Speedo Fastskin kıyafeti (dentikel yapısı)',
        'Yalıçapkını gagası → Shinkansen 500 tren burnu (basınç dalgası kontrolü)',
        'Bal peteği → alüminyum honeycomb panel (minimum malzeme, maksimum dayanım)',
    ]
    for b in biyotaklit_liste:
        e.append(Paragraph(f'• {b}', S_BUL))

    # 1.3 Biyomorfizm
    e.append(Paragraph('1.3 Biyomorfizm', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> Doğal formları ve organik şekilleri estetik amaçla tasarıma yansıtmak. '
        'İşlevin doğrudan taklit edilmesi zorunlu değil; doğadan ilham alınan görsel ve biçimsel '
        'unsurlar kullanılır.', S_BD))
    e.append(Paragraph(
        '<b>Biyotaklitten fark:</b> Biyotaklit "nasıl çalışıyor?" sorusuna yanıt verirken, '
        'biyomorfizm "nasıl görünüyor?" sorusunu yanıtlar.', S_BD))
    e.append(Paragraph(
        '<b>Sınıf için not:</b> Öğrenciler zaman zaman biyomorfizmi biyomimikri sanır. '
        'Test sorusu: "Bu ürün doğanın işlevini mi taklit ediyor, yoksa sadece doğaya mı '
        'benziyor?"', S_NOT))

    # 1.4 Biyofili
    e.append(Paragraph('1.4 Biyofili', S_H2))
    e.append(Paragraph(
        '<b>Tanım:</b> İnsanın doğaya olan içgüdüsel ve evrimsel bağlılığı. Biyofilik tasarım '
        'bu bağı bilinçli olarak kullanarak iyi hissettiren, stressiz mekânlar yaratır.', S_BD))
    e.append(Paragraph(
        '<b>Bilimsel temel:</b> E.O. Wilson\'ın "Biophilia" (1984) hipotezi — insanlar '
        'milyonlarca yıl doğada yaşadı; sinir sistemimiz hâlâ doğal unsurlara olumlu tepki '
        'veriyor.', S_BD))
    biyofili_liste = [
        'Ofislerde iç mekân bitkileri → stres azalması, üretkenlik artışı',
        'Hastanelerde ahşap yüzeyler → ağrı algısı azalması',
        'Okullar için: Pencereden doğa görüşü → dikkat süresi uzaması',
    ]
    for b in biyofili_liste:
        e.append(Paragraph(f'• {b}', S_BUL))
    e.append(Paragraph(
        '<b>Öğretmen notu:</b> Biyofili ile biyomorfizmi karıştırmayın. Biyomorfizm form '
        'meselesidir; biyofili psikolojik etki ve tasarım felsefesi meselesidir.', S_NOT))

    # 1.5 Doğal Seçilim
    e.append(Paragraph('1.5 Doğal Seçilim ve Biyomimikri İlişkisi', S_H2))
    e.append(Paragraph(
        'Evrimin temel mekanizması olan doğal seçilim, başarısız çözümleri elemiş; sadece '
        'bağlamına uygun, enerji verimli ve dayanıklı çözümleri hayatta tutmuştur. '
        'Doğadaki her yapı, milyonlarca nesil boyunca seçilmiş bir "kazanan" çözümdür.', S_BD))
    e.append(Paragraph(
        '<b>Öğrenci yanılgısı:</b> "Doğa mükemmeldir" demek yanlış. Doğa "yeterince iyi" '
        'çözümler üretir — ama bu çözümler milyarlarca yılda test edilmiştir. Bağlam '
        'değişirse doğanın çözümü de yetersiz kalabilir.', S_BD))

    # 1.6 Transfer Türleri
    e.append(Paragraph('1.6 Transfer Türleri', S_H2))
    e.append(Paragraph(
        'Biyomimetik tasarımda üç farklı transfer biçimi vardır. '
        'Hangisinin kullanıldığını belirlemek hem analizi hem değerlendirmeyi keskinleştirir.', S_BD))
    trans_data = [
        [Paragraph('Transfer Türü', S_TH), Paragraph('Soru', S_TH), Paragraph('Örnek', S_TH)],
        [Paragraph('Form', S_TC),
         Paragraph('Bu şekil nasıl görünüyor?', S_TC),
         Paragraph('Yalıçapkını gagası → tren burnu', S_TC)],
        [Paragraph('İşlev', S_TC),
         Paragraph('Bu nasıl çalışıyor?', S_TC),
         Paragraph('Geko tüyleri → yapışkan yüzey', S_TC)],
        [Paragraph('Strateji', S_TC),
         Paragraph('Bu sistemi nasıl yönetiyor?', S_TC),
         Paragraph('Termit havalandırması → bina iklim kontrolü', S_TC)],
    ]
    trans_t = Table(trans_data, colWidths=[CW*0.18, CW*0.35, CW*0.47])
    trans_t.setStyle(TableStyle([
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
    e.append(KeepTogether([trans_t, vsp(0.15)]))
    e.append(Paragraph(
        '<b>Pedagojik not:</b> Öğrenciler en kolay form transferini yapar ("benziyor" transferi). '
        'Dersin asıl hedefi işlev ve strateji transferini de kavratmaktır. '
        'ÇK4 değerlendirmesinde "hangi transfer türü?" sorusu ayırt edicidir.', S_NOT))

    # 1.7 Biyomimikri ve Sürdürülebilirlik
    e.append(Paragraph('1.7 Biyomimikri ve Sürdürülebilirlik', S_H2))
    e.append(Paragraph(
        'Doğa minimum malzeme, minimum enerji, sıfır atık prensibiyle çalışır. '
        'Biyomimetik çözümler bu prensibi teknolojiye taşıdığı için doğası gereği '
        'sürdürülebilir olma eğilimindedir.', S_BD))
    surd_liste = [
        'Lotus etkili yüzeyler → deterjan ihtiyacı azalır → kimyasal atık azalır',
        'Termit havalandırması → bina klima enerji tüketimi %90 azalır',
        'Petek yapı → daha az malzeme, daha yüksek mukavemet → üretim atığı azalır',
    ]
    for s in surd_liste:
        e.append(Paragraph(f'• {s}', S_BUL))
    e.append(Paragraph(
        '<b>Önemli sınır:</b> Her biyomimetik ürün otomatik olarak sürdürülebilir değildir. '
        'Üretim süreci, malzeme seçimi ve ürün ömrü de hesaba katılmalıdır.', S_BD))

    return e


# ============================================================
# BÖLÜM 2 — TARİHSEL ARKA PLAN
# ============================================================

def bolum2():
    e = []
    e += bolum_baslik(2, 'TARİHSEL ARKA PLAN')
    e.append(Paragraph(
        'Biyomimikri yeni bir kavram değildir — ama sistematik bir tasarım pratiği olarak '
        '20. yüzyılın ikinci yarısında şekillendi. Aşağıdaki örnekler hem içerik hem de '
        'sınıfta anlatılabilecek somut hikayeler olarak kullanılabilir.', S_BD))

    # 2.1 Velcro
    e.append(Paragraph('2.1 Velcro — Bir Avcının Gözlemi (George de Mestral, 1941)', S_H2))
    e.append(Paragraph(
        'İsviçreli mühendis George de Mestral 1941\'de Alp dağlarında avlanırken köpeğinin '
        'tüylerine yapışmış iğneotu dikenleriyle karşılaşıyor. Dikeni mikroskop altında '
        'inceleyince küçük kancalar görüyor. 14 yıl deney ve geliştirme süreciyle 1955\'te '
        '"Velcro" patentini alıyor.', S_BD))
    e.append(Paragraph(
        'Bugün her yıl 60 milyon metre Velcro üretiliyor. Uzay kıyafetlerinden ameliyat '
        'önlüklerine, bebek botlarından dağcılık ekipmanına kadar her yerde. '
        'Sadece merak etmişti — bir kez.', S_BD))
    e.append(Paragraph(
        '<b>Sınıf köprüsü:</b> "Bahçede veya evde her gün gördüğünüz ama hiç sorgulamadığınız '
        'bir şey var mı?"', S_NOT))

    # 2.2 Shinkansen
    e.append(Paragraph('2.2 Shinkansen ve Yalıçapkını (Eiji Nakatsu, 1997)', S_H2))
    e.append(Paragraph(
        '500 serisi Shinkansen tünele girdiğinde sıkışan hava patlama sesi çıkartıyor ve '
        'titreşim yapıyordu. Mühendis Eiji Nakatsu hem mühendis hem kuşseverdi. Yalıçapkınını '
        'hatırlıyor — iki farklı yoğunluktaki ortam (hava–su) arasında hiç sıçrama olmadan '
        'geçebiliyordu.', S_BD))
    e.append(Paragraph(
        'Tren burnunu bu formdan ilham alarak yeniden tasarladı: %30 gürültü azalması, '
        '%15 enerji tasarrufu, %10 hız artışı. Pantograflar için baykuştan, gövde profili için '
        'Adeli penguenden de ilham aldı.', S_BD))

    # 2.3 Lotus Etkisi
    e.append(Paragraph('2.3 Lotus Etkisi — 30 Yıllık Sabır (Wilhelm Barthlott, 1970\'ler–1990\'lar)', S_H2))
    e.append(Paragraph(
        'Alman botanikçi Wilhelm Barthlott 1970\'lerde lotus yapraklarının neden her zaman '
        'temiz kaldığını araştırmaya başladı. Elektron mikroskobuyla inceledi: nano boyutlu '
        'balmumu kristalleri, su damlacıklarının kaymasını ve kiri beraberinde götürmesini '
        'sağlıyordu.', S_BD))
    e.append(bilgi_kutusu(
        '30 Yıl Kimse İlgilenmedi',
        ['1977\'de bu yapıyı bilim dünyasına tanıttı — kimse pek ilgilenmedi.',
         '1990\'ların ortasına kadar araştırmaya devam etti; 1999\'da patentt aldı.',
         'Bugün: Su geçirmez kumaşlar, kendi kendini temizleyen camlar, leke tutmayan boyalar. '
         'Tüm bu ürünler o patentten lisans alıyor.',
         'Mesaj: İyi gözlem zamana ihtiyaç duyabilir. Anlık fikirlerin ötesinde sabırla '
         'geliştirilen araştırmanın değerine örnek.']))

    # 2.4 Eastgate Centre
    e.append(Paragraph('2.4 Eastgate Centre — Termitlerin Mimarisi (Mick Pearce, 1996)', S_H2))
    e.append(Paragraph(
        'Zimbabweli mimar Mick Pearce Harare\'de ticari bir bina kompleksi tasarlıyordu. '
        'Klima bütçesi yoktu. Bir biyoloji kitabında termit tepelerinin iç sıcaklığını '
        'pasif konveksiyonla sabit tuttuğunu okudu.', S_BD))
    e.append(Paragraph(
        'Binayı bu mantıkla tasarladı: Gece soğuk hava depolanır; gündüz ısı dışarı verilir. '
        '1996\'dan bu yana merkezi klima yok. Enerji maliyeti çevresindeki benzer binalara '
        'göre %90 daha az.', S_BD))

    # 2.5 Janine Benyus
    e.append(Paragraph('2.5 Janine Benyus ve Biyomimikri Hareketi (1997–günümüz)', S_H2))
    e.append(Paragraph(
        '1997\'de Amerikalı yazar Janine Benyus "Biomimicry: Innovation Inspired by Nature" '
        'kitabını yayımladı. Biyomimikri kavramını akademiden çıkarıp tasarım ve mühendislik '
        'dünyasına taşıdı. 2006\'da Biomimicry Institute\'u kurdu, 2008\'de AskNature.org\'u '
        'açtı — doğanın çözümlerini kategorilere göre araştırmanın mümkün olduğu açık veri '
        'tabanı.', S_BD))
    e.append(Paragraph(
        '<b>Sınıf için:</b> AskNature.org öğrenciler için erişilebilir ve görsel açıdan zengin '
        'bir kaynak. "Su toplama", "yapışma", "ses soğurma" gibi mühendislik sorunlarını '
        'aratınca doğadan onlarca çözüm çıkıyor.', S_NOT))

    # 2.6 Speedo Fastskin
    e.append(Paragraph('2.6 Speedo Fastskin ve Yasak Tartışması (2000 Sydney Olimpiyatları)', S_H2))
    e.append(Paragraph(
        'Köpek balığı derisini elektron mikroskobuyla inceleyen Speedo mühendisleri, pürüzsüz '
        'görünen derinin aslında minik dentikel çıkıntılarla kaplı olduğunu ve bu yapının '
        'su turbülansını kırarak sürtünmeyi dramatik biçimde azalttığını gördü.', S_BD))
    e.append(Paragraph(
        'Fastskin kıyafeti üretildi. 2000 Sydney Olimpiyatları\'nda rekorların %83\'ü Fastskin '
        'giyilirken kırıldı. 2009\'da FINA bu tür kıyafetleri yasakladı: "Teknoloji rekabet '
        'ediyordu, insan değil."', S_BD))
    e.append(Paragraph(
        '<b>Derse bağlantı:</b> Biyomimikri etik soruları da beraberinde getirebilir. '
        'Bir tasarımın "çok iyi" olması ne zaman sorun yaratır?', S_NOT))

    return e


# ============================================================
# BÖLÜM 3 — KRONOLOJİ
# ============================================================

def bolum3():
    e = []
    e += bolum_baslik(3, 'BİYOMİMİKRİ TARİHİNİN KRONOLOJİSİ')

    kron_data = [
        [Paragraph('Yıl', S_TH), Paragraph('Olay', S_TH)],
        [Paragraph('1941', S_TC), Paragraph('George de Mestral iğneotu dikeni gözlemini yapıyor (Velcro fikri)', S_TC)],
        [Paragraph('1955', S_TC), Paragraph('Velcro patenti alındı — ilk ticari biyomimetik ürün', S_TC)],
        [Paragraph('1971', S_TC), Paragraph('Barthlott lotus yaprağı araştırmasına başlıyor', S_TC)],
        [Paragraph('1977', S_TC), Paragraph('Barthlott "lotus etkisi" kavramını bilim dünyasına tanıtıyor', S_TC)],
        [Paragraph('1984', S_TC), Paragraph('E.O. Wilson "Biophilia" kitabını yayımlıyor — biyofili kavramını sistematikleştirdi', S_TC)],
        [Paragraph('1996', S_TC), Paragraph('Mick Pearce Eastgate Centre\'ı tamamlıyor (Harare, Zimbabwe)', S_TC)],
        [Paragraph('1997', S_TC), Paragraph('Janine Benyus "Biomimicry: Innovation Inspired by Nature" yayımlandı', S_TC)],
        [Paragraph('1997', S_TC), Paragraph('Eiji Nakatsu Shinkansen 500 tren burnu tasarımını tamamlıyor', S_TC)],
        [Paragraph('1999', S_TC), Paragraph('Barthlott lotus etkisi patentini alıyor', S_TC)],
        [Paragraph('2000', S_TC), Paragraph('Speedo Fastskin — Sydney Olimpiyatları\'nda 83 rekoru kırıldı', S_TC)],
        [Paragraph('2006', S_TC), Paragraph('Biomimicry Institute kuruldu (Janine Benyus)', S_TC)],
        [Paragraph('2008', S_TC), Paragraph('AskNature.org açıldı — doğa çözümleri açık veri tabanı', S_TC)],
        [Paragraph('2009', S_TC), Paragraph('FINA yüzücü kıyafetlerine teknoloji kısıtlaması getirdi', S_TC)],
        [Paragraph('2020\'ler', S_TC), Paragraph('Biyomimikri piyasa değeri 3,5 milyar dolar; 2030\'da 30 milyar dolar bekleniyor', S_TC)],
    ]
    kron_t = Table(kron_data, colWidths=[CW*0.13, CW*0.87])
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
    e += bolum_baslik(4, 'GÜNCEL DURUM: BİYOMİMİKRİ BUGÜN NEREDE?')

    e.append(Paragraph('4.1 Endüstriyel Ölçek', S_H2))
    e.append(Paragraph(
        'Biyomimikri artık milyarlarca dolarlık bir endüstri. Sadece akademik araştırma '
        'değil — ticari ürünler, mimarlık, malzeme bilimi ve kent planlamasında aktif '
        'biçimde uygulanıyor. Piyasa değeri 2020\'de 3,5 milyar dolar olarak tahmin '
        'edilen bu alanın 2030\'da 30 milyar dolara ulaşması bekleniyor.', S_BD))

    e.append(Paragraph('4.2 Yapay Zekâ ile Biyomimikri', S_H2))
    e.append(Paragraph(
        '"Generative design" algoritmaları kemik yapısından, ağaç gövdesinden ve mercan '
        'iskeletinden ilham alan hafif ama güçlü yapılar üretiyor. Airbus\'ın uçak kanat '
        'parçaları artık balık kılçığı yapısını taklit ediyor; böylece hem hafiflik hem '
        'dayanım elde ediliyor.', S_BD))
    e.append(Paragraph(
        'NASA ve SpaceX de benzer yaklaşımları kullanıyor: Evrimsel algoritmalar bir '
        '"tasarım evrimi" gerçekleştiriyor — biyomimikri ile yapay zekânın kesiştiği yeni '
        'bir alan.', S_BD))

    e.append(Paragraph('4.3 Nanomalzeme', S_H2))
    e.append(Paragraph(
        'Geko ve lotus etkisinden ilham alan nano yüzeyler artık tekstilden uzay araçlarına '
        'kadar geniş bir alanda kullanılıyor. Stanford Üniversitesi\'nde geliştirilen '
        '"Gecko-gloves", insanın cam yüzeylerde duvara tırmanmasını mümkün kılacak kadar '
        'güçlü yapışkan kuvvetler üretebilmektedir.', S_BD))

    e.append(Paragraph('4.4 Türkiye\'deki Durum', S_H2))
    turk_liste = [
        'ODTÜ, İTÜ ve TOBB ETÜ\'de biyomimikri araştırma grupları bulunuyor',
        'Türkiye\'nin 40.000\'den fazla bitki türü ve zengin deniz biyoçeşitliliği araştırılmayı bekliyor',
        'İzmir Körfezi\'nde bulunan bazı sünger türleri malzeme bilimi için inceleniyor',
        'Karadeniz ormanlarındaki endemik türler biyomimetik malzeme araştırmalarına konu oluyor',
    ]
    for t in turk_liste:
        e.append(Paragraph(f'• {t}', S_BUL))

    return e


# ============================================================
# BÖLÜM 5 — DİSİPLİNLERARASI BAĞLANTI
# ============================================================

def bolum5():
    e = []
    e += bolum_baslik(5, 'DİSİPLİNLERARASI BAĞLANTILAR')

    e.append(Paragraph('5.1 Fen Bilgisi: Adaptasyon ve Malzeme', S_H2))
    fen_liste = [
        '<b>Hayvan adaptasyonları:</b> Biyoloji dersiyle doğrudan örtüşür — her adaptasyon '
        'bir tasarım problemidir',
        '<b>Yüzey-hacim oranı:</b> Lotus ve geko etkisini açıklamak için temel fen kavramı',
        '<b>Hidrodinamik:</b> Köpek balığı ve yalıçapkını örneklerinde akışkanlar mekaniği',
        '<b>Biyolojik malzeme yapıları:</b> Spider silk, keratin, balmumu — doğal malzemelerin '
        'mühendislik özellikleri',
    ]
    for f in fen_liste:
        e.append(Paragraph(f'• {f}', S_BUL))
    e.append(Paragraph(
        '<b>İşbirliği önerisi:</b> ÇK2 analizinde "biyolojik mekanizma" bölümünü fen '
        'öğretmeniyle birlikte değerlendirin.', S_NOT))

    e.append(Paragraph('5.2 Matematik: Fibonacci, Altın Oran ve Yüzey Hesabı', S_H2))
    e.append(Paragraph(
        'Doğal formlarda gizli matematik — ders 3\'te işlenen konu '
        'matematik dersiyle güçlü bir köprü kurar:', S_BD))
    mat_liste = [
        '<b>Fibonacci dizisi:</b> Ayçiçeği tohumları, salyangoz kabuğu spirali, kozalak pulları',
        '<b>Altın oran (φ ≈ 1,618):</b> Nautilus kabuğu, yaprak düzeni, çiçek yaprakları',
        '<b>Fraktal geometri:</b> Yaprak damarı ağı, brokoli başı (Romanesco), kıyı şeridi',
        '<b>Yüzey alanı:</b> ÇK6 boyut kararlarında sayısal ölçü zorunluluğu',
    ]
    for m in mat_liste:
        e.append(Paragraph(f'• {m}', S_BUL))

    e.append(Paragraph('5.3 Görsel Sanatlar: Form Analizi ve Model Yapımı', S_H2))
    gorsel_liste = [
        'ÇK3 doğa formu çiziminde gözlem ve çizim becerisi — görsel sanatlar öğretmeniyle paylaşılabilir',
        'Biyomorfizm estetiği: Art Nouveau\'dan Zaha Hadid\'e — sanat tarihi bağlantısı',
        'Prototip yapımı: Model kurgulama, malzeme seçimi ve sunum tasarımı',
    ]
    for g in gorsel_liste:
        e.append(Paragraph(f'• {g}', S_BUL))

    e.append(Paragraph('5.4 Sosyal Bilgiler: Biyoçeşitlilik ve Türkiye', S_H2))
    e.append(Paragraph(
        'Türkiye\'nin biyoçeşitliliği sosyal bilgiler dersiyle doğrudan bağlanır: '
        'Farklı iklim bölgelerindeki endemik türler, Türkiye\'nin doğal zenginlikleri '
        've sürdürülebilir kalkınma konuları 6. Ünite\'de somut örneklerle ele alınabilir.', S_BD))

    e.append(Paragraph('5.5 Bilişim Teknolojileri: AskNature.org Kullanımı', S_H2))
    e.append(Paragraph(
        'Ödev araştırmaları için bilişim dersinde AskNature.org kaynak değerlendirme '
        'etkinliği planlanabilir. Güvenilir kaynak araştırma ve görsel arşiv oluşturma '
        'becerileri biyomimikri örneklerinde pratik olarak geliştirilir.', S_BD))

    return e


# ============================================================
# BÖLÜM 6 — YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI
# ============================================================

def bolum6():
    e = []
    e += bolum_baslik(6, 'YAYGIN ÖĞRENCİ YANLIŞ ANLAMALARI')
    e.append(Paragraph(
        'Aşağıdaki yanlış anlamalar öğrencilerin büyük çoğunluğunda görülür. Bunları ders '
        'başında "tuzak soru" olarak kullanabilir ya da akışta düzeltme fırsatı çıktığında '
        'hazırlıklı olabilirsiniz.', S_BD))

    yanlis = [
        ('"Biyomimikri sadece doğayı taklit etmektir"',
         'Biyomimikri formu, işlevi veya sistemi taklit edebilir — her biri farklı bir '
         'yaklaşımdır; körü körüne "benzetme" değildir'),
        ('"Doğa mükemmel çözümler üretir"',
         'Doğa "yeterince iyi" çözümler üretir; mükemmel değil ama milyarlarca yılda '
         'test edilmiştir; bağlam değişirse çözüm de yetersiz kalabilir'),
        ('"Biyomorfizm ile biyomimikri aynıdır"',
         'Biyomorfizm sadece formu estetik olarak kullanır; biyomimikri işlev veya '
         'stratejiyi de taklit eder — "benziyor" demek biyomimikri değildir'),
        ('"Biyomimetik ürün otomatik olarak sürdürülebilirdir"',
         'İlham kaynağı sürdürülebilir olabilir; ama üretim süreci, malzeme seçimi ve '
         'ürün ömrü de ayrı değerlendirilmelidir'),
        ('"Biyomimikri yeni bir buluştur"',
         'Velcro 1955, lotus araştırmaları 1970\'ler — terim yeni, uygulama çok eski; '
         'insanlık tarih boyunca doğadan öğrenmiştir'),
        ('"Form transferi yeterlidir — biyomimikri budur"',
         'Bir şeye benzemiş olmak biyomimikri değildir; işlev ya da strateji de '
         'aktarılmalıdır — "benziyor" transferi biyomorfizmdir'),
        ('"Biyomimikri sadece ürün tasarımında kullanılır"',
         'Kentsel planlama, lojistik algoritmaları (sürü zekâsı), kimya, malzeme bilimi '
         've enerji sistemlerinde de geniş uygulama alanı bulur'),
        ('"Türkiye\'de biyomimikri araştırması yoktur"',
         'ODTÜ, İTÜ ve TOBB ETÜ\'de aktif araştırma grupları var; Türkiye\'nin '
         'biyoçeşitliliği bu alanda önemli fırsatlar sunuyor'),
    ]

    y_data = [[Paragraph('Yaygın Yanlış Anlama', S_TH), Paragraph('Doğrusu', S_TH)]]
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
        'Bir Diken Dünyayı Değiştirdi: Velcro',
        ['1941, İsviçre Alpları. George de Mestral avdan dönüyor. Köpeği iğneotu dikiyle '
         'kaplı. De Mestral normalde bu dikenleri sabırla çıkarır ve geçer — ama bu kez aklına '
         'farklı bir soru geliyor: "Bu nasıl yapışıyor?" Mikroskop altında görüyor: Dikenin '
         'ucunda küçük kancalar var.',
         '14 yıl deney ve geliştirme süreciyle 1955\'te Velcro patentini alıyor. Bugün her yıl '
         '60 milyon metre Velcro üretiliyor. Uzay kıyafetlerinden ameliyat önlüklerine, bebek '
         'botlarından dağcılık ekipmanına kadar her yerde. Sadece merak etmişti — bir kez.'],
        'Bağlantı: Sıradan bir gözlemin olağanüstü bir buluşa dönüşebildiği en ikonik örnek. '
        '"Bahçede dikkat etmediğimiz ne var?" sorusu iyi bir başlangıçtır.'))

    e.append(hikaye(
        'Kuşsever Mühendis ve Sessiz Tren: Shinkansen',
        ['1990\'ların sonunda Japon Demiryolları\'nda ciddi bir sorun vardı. 500 serisi '
         'Shinkansen tünele girince korkunç bir patlama sesi çıkartıyordu. Mühendisler çözüm '
         'arıyordu; ama çözüm ekipte değil, doğadaydı.',
         'Mühendis Eiji Nakatsu aynı zamanda kuşseverdi. Yalıçapkınının dalarken hiç sıçrama '
         'çıkartmadığını biliyordu — gaga formu iki farklı yoğunluğu (su ve hava) geçişte '
         'dengeli biçimde kesiyordu. Tren burnunu bu formdan ilham alarak yeniden tasarladı: '
         '%30 daha sessiz, %15 daha az enerji, %10 daha hızlı.',
         'Ardından pantograflar için baykuşa, gövde profili için penguene baktı. '
         'Bir kuşsever, Japonya\'nın simgesini daha iyi yaptı.'],
        'Bağlantı: Meslek dışı ilgi alanları tasarım çözümlerinin kaynağı olabilir. '
        '"Sizi hem tasarımcı hem başka şey yapan nedir?" sorusu öğrenciler için '
        'düşündürücü.'))

    e.append(hikaye(
        'Termitlerin Klima Sistemi: Eastgate Centre',
        ['1990\'lar, Harare/Zimbabwe. Mimar Mick Pearce ticari bir bina kompleksi '
         'tasarlıyordu. Harare\'de klima zorunlu gibiydi — ama bütçe yoktu. Pearce biyoloji '
         'kitapları okuyordu ve termit tepelerinde bir şey fark etti: Dışarısı 35°C '
         'olduğunda içerisi 30°C civarında sabit kalıyordu. Hiç enerji kullanmadan.',
         'Kanal sistemi gece soğuk havayı çekip depolayan, gündüz onu salarak binayı '
         'serinleten bir pasif konveksiyon sistemiydi. Pearce aynı mantıkla Eastgate '
         'Centre\'ı tasarladı. 1996\'dan bu yana binada merkezi klima yok. Enerji maliyeti '
         'çevresindeki benzer binalara göre %90 daha az.'],
        'Bağlantı: Sürdürülebilir mimari ile biyomimikrinin buluşması. '
        'Hem 5. Ünite (mimarlık) hem 6. Ünite (biyomimikri) için köprü.'))

    e.append(hikaye(
        'Köpek Balığının Kıyafeti ve Yasak',
        ['1990\'ların sonunda Speedo mühendisleri köpek balığı derisini elektron mikroskobuyla '
         'inceledi. Pürüzsüz görünen deri aslında minik dentikel çıkıntılarla kaplıydı; bu '
         'yapı su turbülansını parçalara ayırarak sürtünmeyi dramatik biçimde azaltıyordu. '
         'Speedo Fastskin kıyafetini üretti.',
         '2000 Sydney Olimpiyatları\'nda rekorların %83\'ü Fastskin giyilirken kırıldı. '
         '2009\'da FINA bu tür kıyafetleri yasakladı: "Teknoloji rekabet ediyordu, '
         'insan değil." Bir balık derisi, olimpiyat kurallarını değiştirdi.'],
        'Bağlantı: Biyomimikri etik soruları da beraberinde getirebilir. '
        'Bir tasarımın "çok iyi" olması ne zaman sorun yaratır?'))

    e.append(hikaye(
        'Lotus Çiçeği ve 30 Yıllık Sabır',
        ['1971\'de genç botanikçi Wilhelm Barthlott lotus bitkisini incelemeye başladı. '
         'Yaprakların neden her zaman temiz kaldığını merak ediyordu. Elektron mikroskobu '
         'cevabı gösterdi: nano boyutlu balmumu kristalleri su damlacıklarının kaymasını '
         've kiri beraberinde götürmesini sağlıyordu.',
         '1977\'de bu yapıyı bilim dünyasına tanıttı — kimse pek ilgilenmedi. '
         '1990\'ların ortasına kadar araştırmaya devam etti; 1999\'da patentt aldı. '
         'Bugün: Su geçirmez kumaşlar, kendi kendini temizleyen camlar, leke tutmayan boyalar. '
         'Ve tüm bu ürünler o patentten lisans alıyor. 30 yıl — sabır, merak ve mikroskop.'],
        'Bağlantı: İyi gözlem anlık değil, birikimsel olabilir. '
        'Sabır ve ısrar tasarımın bir parçasıdır.'))

    e.append(hikaye(
        'Namib Çölü Böceği ve Su Hasadı',
        ['Güney Afrika\'nın kurak Namib Çölü\'nde yaşayan Stenocara gracilipes adlı böcek, '
         'su kaynağına erişimi olmayan bir ortamda hayatta kalıyor. Sırtındaki çıkıntılar '
         'suyu çekiyor, aralarındaki düzgün yüzeyler ise suyu kanalize ediyor.',
         'Her sabah çöl sisi geldiğinde bu yapı suyu toplayıp doğrudan ağzına yönlendiriyor. '
         'Araştırmacılar bu prensibi taklit eden "sis hasadı" yüzeyleri geliştirdi — '
         'su kıtlığı olan bölgelerde atmosferden su toplamak için.',
         'Türkiye\'de Orta Anadolu\'nun kurak yörelerinde bu teknoloji kullanılabilir. '
         'Bir böceğin sırtı, insanlık için su çözümüdür.'],
        'Bağlantı: "Türkiye\'de gerçek bir problem — biyomimetik çözüm?" sorusuna somut örnek. '
        'ÇK5 disiplinler arası haritasına bağlanabilir.'))

    return e


# ============================================================
# BÖLÜM 8 — ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR
# ============================================================

def bolum8():
    e = []
    e += bolum_baslik(8, 'ÖĞRENCİLERDEN GELEBİLECEK ZOR SORULAR')
    e.append(Paragraph(
        'Bazı sorular anında yanıt gerektirmez. "Harika soru — düşünmem lazım" ya da '
        '"Bu konuyu ileride daha ayrıntılı ele alacağız" demek tamamen uygundur. '
        'Aşağıdaki yanıtlar bir başlangıç noktasıdır.', S_BD))

    qas = [
        ('"Biyomimikri \'doğayı taklit et\' diyorsa, zehir de doğanın çözümü — onu da taklit edelim mi?"',
         'Biyomimikri etik bir çerçeve de içerir. Janine Benyus ve Biomimicry Institute '
         '"Life\'s Principles" adlı bir set geliştirdi: insanlık yararına uyarlanabilecek '
         'prensipler. Zehir de bir çözüm — ama bağlama göre. Kobra zehiri pıhtılaşma '
         'ilaçlarında kullanılıyor. "Doğadan öğrenmek" körü körüne taklit değil, akıllı '
         'seçimdir. Etik karar insana ait.'),
        ('"Biyomimikri sürdürülebilirdir deniyor — ama nano kaplama üretimi de enerji yoğun. Gerçekten yeşil mi?"',
         'Bu, alanın en ciddi eleştirisi. Ürünün ilham kaynağı sürdürülebilir olabilir; ama '
         'üretim süreci ayrı değerlendirilmeli. "Yaşam döngüsü analizi" burada devreye '
         'giriyor — sadece kullanım değil, üretim, taşıma ve atık da hesaba katılmalı. '
         'Biyomimikri sürdürülebilirliği garanti etmez; ama doğru uygulandığında '
         'anlamlı ölçüde artırır.'),
        ('"Yapay zekâ biyomimetik tasarımı otomatikleştirirse, insan tasarımcıların rolü ne kalır?"',
         '"Generative design" algoritmaları kemik yapısı gibi organik formları hesaplıyor. '
         'Airbus ve NASA bu yaklaşımı fiilen kullanıyor. Ama "hangi problemi çözmek '
         'istiyoruz?" sorusu hâlâ insana ait. Algoritma form optimizasyonu yapabilir; '
         'kullanıcı ihtiyacını yorumlamak, etik sınırları belirlemek ve anlam yerleştirmek '
         'insanın işi olmayı sürdürüyor.'),
        ('"Türkiye\'nin biyoçeşitliliğini tasarım için \'kaynak\' gibi görürsek, bu da sömürü olmaz mı?"',
         'Biyomimikri etik tartışmalarından biri tam da bu. "Doğa için tasarım" ile '
         '"doğadan tasarım" arasında fark var. Janine Benyus bu tartışmayı "etik biyomimikri" '
         'çerçevesinde ele alıyor: Doğadan öğreniyorsak, doğayı koruma yükümlülüğümüz de '
         'artıyor. Araştırılan habitatların korunması, yerel bilgiye saygı — bunlar '
         'biyomimikri etiğinin gündemi.'),
        ('"Öğrencim \'lotus etkisi gibi bir şey buldum\' dedi ama farklı bir şeyden bahsetti. Yanlış anlama mı?"',
         'Değerlendirmede "biyomimikri bağlantısının gerçekliği" kritik. Öğrencinin iddiası '
         'üç soruyla test edilebilir: (1) Hangi canlı veya yapı ilham verdi? (2) Hangi '
         'özellik — form, işlev veya strateji — taklit ediliyor? (3) Transfer gerçek mi, '
         'yoksa sadece benzetme mi? Bu üç soruya somut yanıt verilebiliyorsa biyomimikri '
         'var demektir.'),
        ('"Biyomimikri ile yerli ve millî tasarım arasında nasıl bir ilişki kurulabilir?"',
         'Türkiye\'nin biyoçeşitliliği bu ilişki için güçlü bir zemin sunuyor. Tuz Gölü '
         'kuşlarının tuz filtrasyonu, Karadeniz fındıkselisinin kabuk yapısı, Ege\'nin deniz '
         'kekiği gibi endemik türlerin özellikleri araştırılmayı bekliyor. "Yerli biyomimikri" '
         '— Türkiye\'ye özgü canlıların özelliklerinden ilham alan yerli ürün tasarımı — '
         'hem ekolojik hem ekonomik değer üretme potansiyeli taşıyor.'),
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
        title='6. Unite - Ogretmen Hazirlik Rehberi',
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
    print('OK  U6_PDF_Ogretmen_Hazirlik_Rehberi.pdf')


if __name__ == '__main__':
    main()
