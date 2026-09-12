"""
3. Unite - On Degerlendirme PDF Ureticisi (Ogrenci Formu)
2 sayfalik tek PDF: Sayfa 1 = Arac 1+2, Sayfa 2 = Arac 3+4+5
Calistir: python pdf_uretim/uret_unite3_on_degerlendirme.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)

from pdf_style import (
    register_fonts, add_page_number, create_doc,
    make_student_info_header,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, MindMapCanvas, HorizontalLine,
)

register_fonts()

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit3')
UI   = 'Teknoloji ve Tasarim - 7. Sinif - 3. Unite: Tasarim Odakli Surec'

# ---------- Stiller ----------

S_BAS   = ParagraphStyle('u3od_BAS',   fontName='TR-Bold',    fontSize=10,  textColor=COLOR_PRIMARY,   leading=13, spaceBefore=4, spaceAfter=2)
S_YON   = ParagraphStyle('u3od_YON',   fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,      leading=11,
                          backColor=COLOR_VERY_LIGHT, borderPad=5, spaceBefore=2, spaceAfter=3)
S_NOT   = ParagraphStyle('u3od_NOT',   fontName='TR-Italic',  fontSize=8,   textColor=COLOR_MUTED,     leading=11, spaceBefore=0, spaceAfter=1)
S_SORU  = ParagraphStyle('u3od_SORU',  fontName='TR-Bold',    fontSize=8,   textColor=COLOR_TEXT,      leading=11, spaceBefore=2, spaceAfter=1)
S_OPT   = ParagraphStyle('u3od_OPT',   fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,      leading=10, leftIndent=4)
S_NEDEN = ParagraphStyle('u3od_NEDEN', fontName='TR-Bold',    fontSize=7.5, textColor=COLOR_MUTED,     leading=10, spaceBefore=1)
S_ACK   = ParagraphStyle('u3od_ACK',   fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_TEXT,      leading=12, spaceBefore=3, spaceAfter=1)
S_KAVR  = ParagraphStyle('u3od_KAVR',  fontName='TR-Bold',    fontSize=8,   textColor=COLOR_SECONDARY, leading=11, spaceBefore=3, spaceAfter=1)
S_DOLD  = ParagraphStyle('u3od_DOLD',  fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,      leading=12, spaceBefore=1, spaceAfter=0)
S_KUTU  = ParagraphStyle('u3od_KUTU',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,      leading=11,
                          backColor=COLOR_VERY_LIGHT, borderPad=5, spaceBefore=2, spaceAfter=3)
S_SANA  = ParagraphStyle('u3od_SANA',  fontName='TR-Italic',  fontSize=8,   textColor=COLOR_MUTED,     leading=11, spaceBefore=2, spaceAfter=1)


def vsp(h=0.2):
    return Spacer(1, h * cm)


def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.4)


# ============================================================
# SAYFA 1: ARAC 1 (Zihin Haritasi) + ARAC 2 (Tanilama Testi)
# ============================================================

SORULAR = [
    ('Bir tasarimci yeni bir urun tasarlamaya hangi adimla baslamalidir?',
     ['A) Urunu hemen cizmeye baslamalidir',
      'B) Malzeme listesi hazirlamalidir',
      'C) Cozmek istedigi problemi tespit etmelidir',
      'D) Urunu renklendirmelidir']),
    ('Bir tasarimci "empati" yaparken ne yapmaktadir?',
     ['A) Urunun guzel gorunmesini saglar',
      'B) Kullanicinin yerine gecip ne hissettigi anlamaya calisir',
      'C) Malzemeleri karsilastirir',
      'D) Prototip testleri yapar']),
    ('"Prototip" ne demektir?',
     ['A) Tasarim fikrini deneme amacli ilk modelidir',
      'B) Bir urunun en son ve mukemmel halidir',
      'C) Tasarimin kagit uzerindeki taslagidir',
      'D) Urunun renkli fotografidir']),
    ('"Ergonomi" kavrami tasarimda neyi ifade eder?',
     ['A) Urunun renk ve sekil guzelligini',
      'B) Urunun uretim maliyetini',
      'C) Urunun dayaniklilik suresini',
      'D) Urunun insan vucuduna ve kullanimina uygunlugunu']),
    ('Surdurulebilir urun tasarlamak isteyen tasarimci ne tercih eder?',
     ['A) En ucuz malzemeyi secer',
      'B) Geri donusturulebilen ve uzun omurlu malzemeleri tercih eder',
      'C) En hafif malzemeyi secer',
      'D) En parlak renkli malzemeyi secer']),
    ('Test sonrasi olumsuz geri bildirim alan tasarimci ne yapmalydir?',
     ['A) Urunu oldugu gibi birakir',
      'B) Sifirdan yeni bir urun tasarlar',
      'C) Geri bildirimi dikkate alarak urunu revize eder',
      'D) Baska bir kullanici bulur']),
    ('Beyin firtinasinda hangi kural gecerlidir?',
     ['A) Hicbir fikir elestirilmez, ne kadar cok fikir o kadar iyi',
      'B) Sadece gercekci fikirler soylenir',
      'C) En cok konusanin fikirleri kabul edilir',
      'D) Fikirler not alinmaz, sadece tartisiliyr']),
    ('Tasarim Odakli Dusunmenin (Design Thinking) temel amaci nedir?',
     ['A) En ucuz urunu uretmek',
      'B) En guzel gorunen urunu yapmak',
      'C) Teknolojiyi taklit etmek',
      'D) Insan ihtiyaclarini merkeze alarak gercek sorunlara cozum uretmek']),
]

SORULAR_TR = [
    ('Bir tasarımcı yeni bir ürün tasarlamaya hangi adımla başlamalıdır?',
     ['A) Ürünü hemen çizmeye başlamalıdır',
      'B) Malzeme listesi hazırlamalıdır',
      'C) Çözmek istediği problemi tespit etmelidir',
      'D) Ürünü renklendirmelidir']),
    ('Bir tasarımcı "empati" yaparken ne yapmaktadır?',
     ['A) Ürünün güzel görünmesini sağlar',
      'B) Kullanıcının yerine geçip ne hissettiğini anlamaya çalışır',
      'C) Malzemeleri karşılaştırır',
      'D) Prototip testleri yapar']),
    ('"Prototip" ne demektir?',
     ['A) Tasarım fikrinin deneme amaçlı ilk modelidir',
      'B) Bir ürünün en son ve mükemmel halidir',
      'C) Tasarımın kâğıt üzerindeki taslağıdır',
      'D) Ürünün renkli fotoğrafıdır']),
    ('"Ergonomi" kavramı tasarımda neyi ifade eder?',
     ['A) Ürünün renk ve şekil güzelliğini',
      'B) Ürünün üretim maliyetini',
      'C) Ürünün dayanıklılık süresini',
      'D) Ürünün insan vücuduna ve kullanımına uygunluğunu']),
    ('Sürdürülebilir ürün tasarlamak isteyen tasarımcı ne tercih eder?',
     ['A) En ucuz malzemeyi seçer',
      'B) Geri dönüştürülebilen ve uzun ömürlü malzemeleri tercih eder',
      'C) En hafif malzemeyi seçer',
      'D) En parlak renkli malzemeyi seçer']),
    ('Test sonrası olumsuz geri bildirim alan tasarımcı ne yapmalıdır?',
     ['A) Ürünü olduğu gibi bırakır',
      'B) Sıfırdan yeni bir ürün tasarlar',
      'C) Geri bildirimi dikkate alarak ürünü revize eder',
      'D) Başka bir kullanıcı bulur']),
    ('Beyin fırtınasında hangi kural geçerlidir?',
     ['A) Hiçbir fikir eleştirilmez, ne kadar çok fikir o kadar iyi',
      'B) Sadece gerçekçi fikirler söylenir',
      'C) En çok konuşanın fikirleri kabul edilir',
      'D) Fikirler not alınmaz, sadece tartışılır']),
    ('Tasarım Odaklı Düşünmenin (Design Thinking) temel amacı nedir?',
     ['A) En ucuz ürünü üretmek',
      'B) En güzel görünen ürünü yapmak',
      'C) Teknolojiyi taklit etmek',
      'D) İnsan ihtiyaçlarını merkeze alarak gerçek sorunlara çözüm üretmek']),
]


def q_blok(no, soru, secenekler):
    blok = []
    blok.append(Paragraph(f'<b>{no}.</b> {soru}', S_SORU))
    for s in secenekler:
        blok.append(Paragraph(s, S_OPT))
    blok.append(Paragraph('<b>Neden?</b>', S_NEDEN))
    blok.append(WritingLines(num_lines=1, line_spacing=16))
    blok.append(vsp(0.08))
    return blok


def sayfa1():
    E = []

    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph(
        '<b>Not:</b> Bu çalışma not için değildir. Bildiklerini dürüstçe yaz — yanlış cevap olmaz!',
        S_NOT,
    ))
    E.append(sep())
    E.append(vsp(0.15))

    # ---- ARAC 1: Zihin Haritasi ----
    E.append(Paragraph('ARAÇ 1: ZİHİN HARİTASI', S_BAS))
    E.append(Paragraph(
        '<b>Yönerge:</b> Aşağıda iki anahtar kelime var: <b>TASARIM</b> ve <b>PROBLEM</b>. '
        'Bu kelimeleri duyduğunda aklına gelen her şeyi (kelime, nesne, örnek) oklarla bağlayarak yaz. '
        '<b>Süre: 5 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    mm_table = Table([[
        MindMapCanvas('TASARIM', width=8.2 * cm, height=5.5 * cm, num_branches=8),
        MindMapCanvas('PROBLEM', width=8.2 * cm, height=5.5 * cm, num_branches=8),
    ]], colWidths=[8.5 * cm, 8.5 * cm])
    mm_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    E.append(mm_table)

    E.append(vsp(0.15))
    E.append(Paragraph('<b>Son soru:</b> Sence TASARIM ile PROBLEM birbiriyle ilişkili mi? Neden?', S_SORU))
    E.append(WritingLines(num_lines=1, line_spacing=18))
    E.append(vsp(0.1))
    E.append(sep())
    E.append(vsp(0.15))

    # ---- ARAC 2: Tanilama Testi ----
    E.append(Paragraph('ARAÇ 2: İKİ AŞAMALI TANILAMA TESTİ', S_BAS))
    E.append(Paragraph(
        '<b>Yönerge:</b> Doğru seçeneği daire içine al, sonra neden o seçeneği seçtiğini kısaca açıkla. '
        '<b>Süre: 10 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.15))

    sol = []
    sag = []
    for i, (soru, secs) in enumerate(SORULAR_TR):
        if i < 4:
            sol.extend(q_blok(i + 1, soru, secs))
        else:
            sag.extend(q_blok(i + 1, soru, secs))

    col_w = 8.2 * cm
    q_tablo = Table([[sol, sag]], colWidths=[col_w, col_w])
    q_tablo.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LINEAFTER', (0, 0), (0, 0), 0.4, COLOR_LIGHT_GREY),
    ]))
    E.append(q_tablo)

    return E


# ============================================================
# SAYFA 2: ARAC 3 + ARAC 4 + ARAC 5 + SANA GORE
# ============================================================

def sayfa2():
    E = []

    E.append(vsp(0.1))

    # ---- ARAC 3: Acik Uclu Sorular ----
    E.append(Paragraph('ARAÇ 3: AÇIK UÇLU SORULAR', S_BAS))
    E.append(Paragraph(
        '<b>Yönerge:</b> Aşağıdaki soruları kendi cümlelerinle yanıtla. Doğru/yanlış yok. <b>Süre: 5 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.1))

    acik_sorular = [
        'Çevrende her gün gördüğün ya da kullandığın bir şeyi yeniden tasarlamak isteseydin ne seçerdin? Neden?',
        'Sence iyi bir tasarımcı olmak için en önemli özellik nedir? Neden?',
        '"Sürdürülebilir tasarım" ne anlama geliyor olabilir? Tahminini yaz.',
    ]
    for s in acik_sorular:
        E.append(Paragraph(s, S_ACK))
        E.append(WritingLines(num_lines=2, line_spacing=18))
        E.append(vsp(0.08))

    E.append(vsp(0.05))
    E.append(sep())
    E.append(vsp(0.15))

    # ---- ARAC 4: Eslestirme Testi ----
    E.append(Paragraph('ARAÇ 4: EŞLEŞTİRME TESTİ', S_BAS))
    E.append(Paragraph(
        '<b>Yönerge:</b> Sol sütundaki kavramları sağ sütundaki tanımlarla eşleştir. '
        'Cevabı noktalı alana yaz. <b>Süre: 4-5 dakika</b>',
        S_YON,
    ))
    E.append(vsp(0.1))

    tbl_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 1), (-1, -1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
        ('GRID', (0, 0), (-1, -1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ])

    E.append(Paragraph('<b>Bölüm A — Kavram ve Tanım</b>', S_KAVR))
    bolum_a = [
        ['#', 'Kavram', 'Cvp', 'Hrf', 'Tanım'],
        ['1', 'Ergonomi',        '...', 'A', 'Ürün veya hizmetin özgün bir çözüm sunması'],
        ['2', 'İnovasyon',       '...', 'B', 'Test kullanıcısının deneyimini anlamak için görsel araç'],
        ['3', 'Empati Haritası', '...', 'C', 'Sonraki nesillerin ihtiyaçlarını da gözeten üretim anlayışı'],
        ['4', 'Sürdürülebilirlik','...','D', 'Ürünün insan vücudu ve hareketlerine uygun tasarlanması'],
        ['5', 'Prototip',        '...', 'E', 'Tasarım fikrinin test için yapılan deneme modeli'],
    ]
    tbl_a = Table(bolum_a, colWidths=[0.7*cm, 3.5*cm, 0.9*cm, 0.7*cm, 11.2*cm])
    tbl_a.setStyle(tbl_style)
    E.append(tbl_a)

    E.append(vsp(0.1))
    E.append(Paragraph('<b>Bölüm B — Design Thinking Basamağı ve Açıklaması</b>', S_KAVR))
    bolum_b = [
        ['#', 'Basamak', 'Cvp', 'Hrf', 'Açıklama'],
        ['1', 'Problem Tespiti', '...', 'A', 'Seçilen fikri somut bir model olarak üretme'],
        ['2', 'Analiz',          '...', 'B', 'Modeli gerçek kullanıcıyla deneyerek geri bildirim alma'],
        ['3', 'Uygulama',        '...', 'C', 'Günlük hayatta insanların yaşadığı güçlüğü belirleme'],
        ['4', 'Test',            '...', 'D', 'Olumsuz geri bildirimlere göre ürünü iyileştirme'],
        ['5', 'Revize',          '...', 'E', 'Empati haritası ve gözlemle kullanıcıyı tanıma'],
    ]
    tbl_b = Table(bolum_b, colWidths=[0.7*cm, 3.0*cm, 0.9*cm, 0.7*cm, 11.7*cm])
    tbl_b.setStyle(tbl_style)
    E.append(tbl_b)

    E.append(vsp(0.1))
    E.append(sep())
    E.append(vsp(0.15))

    # ---- ARAC 5: Bosluk Doldurma ----
    E.append(Paragraph('ARAÇ 5: BOŞLUK DOLDURMA', S_BAS))
    E.append(Paragraph(
        '<b>Yönerge:</b> Boş yerleri kutu içindeki kelimelerden uygun olanıyla doldur. '
        'Her kelime yalnızca bir kez kullanılır. <b>Süre: 3-4 dakika</b>',
        S_YON,
    ))
    E.append(Paragraph(
        '<b>Kelime Kutusu:</b>  ergonomi  /  empati  /  prototip  /  geri bildirim  /  sürdürülebilirlik  /  '
        'inovasyon  /  tasarım odaklı düşünme  /  geri dönüştürülebilir  /  revize  /  problem tespiti',
        S_KUTU,
    ))

    bosluklar = [
        '1. Kullanıcının yerine geçerek ne hissettiğini anlamaya çalışmak <b>_____________________</b> olarak adlandırılır.',
        '2. Tasarımcının ilk yapması gereken şey <b>_____________________</b> aşamasıdır.',
        '3. Tasarım fikrinin deneme amaçlı ilk modeline <b>_____________________</b> denir.',
        '4. Kullanıcının ürünü test edip görüşlerini iletmesine <b>_____________________</b> denir.',
        '5. Ürünün insan vücuduna uygun tasarlanması <b>_____________________</b> ilkesiyle sağlanır.',
        '6. Uzun ömürlü, <b>_____________________</b> malzemeler kullanmak <b>_____________________</b> okuryazarlığının temelidir.',
        '7. Daha önce yapılmamış özgün çözüm üretmek <b>_____________________</b> olarak adlandırılır.',
        '8. İnsan ihtiyaçlarını merkeze alarak çözüm geliştirme yaklaşımı <b>_____________________</b> olarak bilinir.',
    ]
    for b in bosluklar:
        E.append(Paragraph(b, S_DOLD))

    return E


# ============================================================
# ANA CALISTIRICI
# ============================================================

def main():
    output_path = os.path.join(ROOT, 'U3_PDF_02_On_Degerlendirme.pdf')
    doc = create_doc(output_path, title='On Degerlendirme - Ogrenci Formu', unite_info=UI)
    doc.doc_title = 'On Degerlendirme - Ogrenci Formu'

    story = []
    story += sayfa1()
    story.append(PageBreak())
    story += sayfa2()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

    size_kb = os.path.getsize(output_path) // 1024
    pages = 2
    print(f'OK  {os.path.basename(output_path)} ({pages} sayfa, {size_kb} KB)')


if __name__ == '__main__':
    main()
