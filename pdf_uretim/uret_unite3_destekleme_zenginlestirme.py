"""
3. Unite - Destekleme ve Zenginlestirme PDF Ureticisi
Uretir:
  U3_PDF_05_Destekleme.pdf   (6 materyal, 6 sayfa)
  U3_PDF_06_Zenginlestirme.pdf (5 etkinlik, 5 sayfa)
Calistir: python pdf_uretim/uret_unite3_destekleme_zenginlestirme.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether,
)
from pdf_style import (
    register_fonts, add_page_number, create_doc, make_student_info_header,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, HorizontalLine,
)

register_fonts()

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit3')
UI   = 'Teknoloji ve Tasarim - 7. Sinif - 3. Unite: Tasarim Odakli Surec'

# ============================================================
# STILLER
# ============================================================

S_BAS  = ParagraphStyle('u3dz_BAS',  fontName='TR-Bold',    fontSize=11.5, textColor=white,
                         backColor=COLOR_PRIMARY, borderPad=7, spaceBefore=0, spaceAfter=4, leading=15)
S_BLM  = ParagraphStyle('u3dz_BLM',  fontName='TR-Bold',    fontSize=9,    textColor=COLOR_SECONDARY,
                         leading=12, spaceBefore=5, spaceAfter=2)
S_BLM2 = ParagraphStyle('u3dz_BLM2', fontName='TR-Bold',    fontSize=8.5,  textColor=COLOR_ACCENT,
                         leading=11, spaceBefore=4, spaceAfter=1)
S_GOV  = ParagraphStyle('u3dz_GOV',  fontName='TR-Regular', fontSize=8.5,  textColor=COLOR_TEXT,
                         leading=12, spaceBefore=1, spaceAfter=1)
S_YON  = ParagraphStyle('u3dz_YON',  fontName='TR-Regular', fontSize=8,    textColor=COLOR_TEXT,
                         leading=11, backColor=COLOR_VERY_LIGHT, borderPad=5, spaceBefore=2, spaceAfter=3)
S_LST  = ParagraphStyle('u3dz_LST',  fontName='TR-Regular', fontSize=8,    textColor=COLOR_TEXT,
                         leading=11, leftIndent=10, spaceBefore=1)
S_NOT  = ParagraphStyle('u3dz_NOT',  fontName='TR-Italic',  fontSize=7.5,  textColor=COLOR_MUTED,
                         leading=10, spaceBefore=1, spaceAfter=2)
S_LBL  = ParagraphStyle('u3dz_LBL',  fontName='TR-Bold',    fontSize=8.5,  textColor=COLOR_TEXT,
                         leading=12, spaceBefore=3, spaceAfter=1)
S_ADM  = ParagraphStyle('u3dz_ADM',  fontName='TR-Bold',    fontSize=9,    textColor=COLOR_PRIMARY,
                         leading=12, spaceBefore=5, spaceAfter=1)
S_ADM_A= ParagraphStyle('u3dz_ADMA', fontName='TR-Italic',  fontSize=8,    textColor=COLOR_MUTED,
                         leading=11, spaceBefore=0, spaceAfter=1)
# Mini kart stilleri (Mat 6)
S_KH   = ParagraphStyle('u3dz_KH',   fontName='TR-Bold',    fontSize=7.5,  textColor=white,
                         backColor=COLOR_SECONDARY, borderPad=3, leading=10, spaceBefore=0, spaceAfter=2)
S_KM   = ParagraphStyle('u3dz_KM',   fontName='TR-Regular', fontSize=6.5,  textColor=COLOR_MUTED,
                         leading=9,  spaceBefore=0, spaceAfter=1)
S_KI   = ParagraphStyle('u3dz_KI',   fontName='TR-Regular', fontSize=6.5,  textColor=COLOR_TEXT,
                         leading=9,  spaceBefore=0, spaceAfter=0, leftIndent=2)
S_KS   = ParagraphStyle('u3dz_KS',   fontName='TR-Bold',    fontSize=6.5,  textColor=COLOR_TEXT,
                         leading=9,  spaceBefore=1, spaceAfter=0)
# Zenginlestirme gorev kutusu
S_ZGV  = ParagraphStyle('u3dz_ZGV',  fontName='TR-Regular', fontSize=8.5,  textColor=COLOR_TEXT,
                         leading=12, backColor=COLOR_VERY_LIGHT, borderPad=6, spaceBefore=0, spaceAfter=4)


def vsp(h=0.2):
    return Spacer(1, h * cm)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.4)

def des_baslik(no, baslik):
    return [Paragraph(f'Destekleme Materyali {no} — {baslik}', S_BAS), vsp(0.1)]

def zen_baslik(no, baslik):
    return [Paragraph(f'Zenginleştirme Etkinliği {no} — {baslik}', S_BAS), vsp(0.1)]

def numarali(items):
    return [Paragraph(f'{i+1}. {t}', S_LST) for i, t in enumerate(items)]

def madde(items):
    return [Paragraph(f'•  {t}', S_LST) for t in items]

def deg_tablo(olcutler):
    """[(olcut_str, puan_int), ...]  sonuna TOPLAM ekler"""
    toplam = sum(p for _, p in olcutler)
    data = [['Ölçüt', 'Puan']]
    for o, p in olcutler:
        data.append([o, str(p)])
    data.append([Paragraph('<b>TOPLAM</b>', ParagraphStyle('tot', fontName='TR-Bold', fontSize=8, textColor=COLOR_TEXT, leading=10)), Paragraph(f'<b>{toplam}</b>', ParagraphStyle('tot2', fontName='TR-Bold', fontSize=8, textColor=COLOR_TEXT, leading=10, alignment=TA_CENTER))])
    t = Table(data, colWidths=[13.5*cm, 3*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'TR-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,1), (-1,-2), 'TR-Regular'),
        ('TEXTCOLOR', (0,1), (-1,-1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [white, COLOR_VERY_LIGHT]),
        ('BACKGROUND', (0,-1), (-1,-1), COLOR_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    return t

def bilgi_kutusu(items):
    """Format/Sure/Teslim satirlari [(label, deger)]"""
    data = [[Paragraph(f'<b>{l}:</b>', S_LST), Paragraph(d, S_LST)] for l, d in items]
    t = Table(data, colWidths=[3*cm, 13.5*cm])
    t.setStyle(TableStyle([
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    return t


# ============================================================
# DESTEKLEME: 6 Materyal
# ============================================================

def build_des1():
    E = des_baslik(1, 'Görsel Design Thinking Döngüsü Kartı')
    E.append(Paragraph('<b>Adımları sırayla oku. Çalışırken bu kartı masanda tut.</b>', S_NOT))
    E.append(vsp(0.1))

    adimlar = [
        ('ADIM 1 — Problem Tespiti',
         'Ne yapıyorum: Çevremde gerçekten var olan bir sorunu fark ediyorum.',
         '"Kimin hayatını kolaylaştırabilir ya da güzelleştirebilirim?"'),
        ('ADIM 2 — Empati',
         'Ne yapıyorum: Problemi yaşayan kişinin yerine geçerek duygularını ve ihtiyaçlarını anlıyorum.',
         '"Bu kişi ne hissediyor? Ne istiyor? Neyi zor buluyor?"'),
        ('ADIM 3 — Fikir Üretimi',
         'Ne yapıyorum: Sorun için olabildiğince çok ve farklı fikir üretiyorum. Hiçbir fikri elemiyorum.',
         '"En saçma fikrim bile bu listeye giriyor mu?"'),
        ('ADIM 4 — Eskiz / Taslak',
         'Ne yapıyorum: En iyi fikrimi çiziyorum. Malzemeleri ve nasıl yapılacağını planlıyorum.',
         '"Bunu gerçekten yapabilir miyim? Neye ihtiyacım var?"'),
        ('ADIM 5 — Uygulama / Prototip',
         'Ne yapıyorum: Fikri somut bir nesneye, makete ya da modele dönüştürüyorum.',
         '"Bu prototip problemi çözüyor mu? Kullanıcı bunu kullanabilir mi?"'),
        ('ADIM 6 — Test / Geri Bildirim',
         'Ne yapıyorum: Prototipi gerçek bir kişiye gösteriyor ya da denettiriyorum.',
         '"Neyin işe yaradığını öğrendim? Neyin değişmesi gerekiyor?"'),
        ('ADIM 7 — Revize',
         'Ne yapıyorum: Geri bildirimlere göre tasarımımı düzeltiyorum. Süreç burada bitmez.',
         '"Bu değişiklik kullanıcı için gerçekten daha iyi mi?"'),
    ]

    for baslik, aciklama, soru in adimlar:
        blok = [
            Paragraph(baslik, S_ADM),
            Paragraph(aciklama, S_ADM_A),
            Paragraph(f'→  <i>{soru}</i>', S_ADM_A),
            vsp(0.08),
            HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.4),
        ]
        E.append(KeepTogether(blok))

    E.append(vsp(0.2))
    E.append(Paragraph('Döngü İpuçları', S_BLM))
    ipuclari = [
        ['Adımlar sırayla gider — ama geri dönmek mümkündür', 'Tasarım doğrusal değil, döngüseldir'],
        ['Empati atlanırsa çözüm kullanıcıyı değil, seni tatmin eder', 'Asıl kullanıcı senin dışındadır'],
        ['Test aşamasında "beğendin mi?" değil "ne değiştirirdin?" sor', 'Eleştiri iyileştirmenin yakıtıdır'],
    ]
    ip_tbl = Table([['Dikkat!', 'Neden?']] + ipuclari, colWidths=[8.5*cm, 8*cm])
    ip_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_LIGHT),
        ('FONTNAME', (0,0), (-1,0), 'TR-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('FONTNAME', (0,1), (-1,-1), 'TR-Regular'),
        ('TEXTCOLOR', (0,0), (-1,-1), COLOR_TEXT),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    E.append(ip_tbl)
    return E


def build_des2():
    E = des_baslik(2, 'Adım Adım Prototip Yapım Rehberi')
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph('<i>Prototip yapmak zor görünebilir. Ama bunu adım adım yaparsak kolaylaşır. '
                       'Her adımı tamamladığında kutuyu işaretle.</i>', S_NOT))
    E.append(vsp(0.1))

    E.append(Paragraph('Başlamadan Önce: Eskizini Kontrol Et', S_BLM))
    on_data = [
        ['Neyi yapmaya çalışıyorum? (1 cümle)', ''],
        ['Hangi malzemeleri kullanacağım?', ''],
        ['Ne kadar zamana ihtiyacım var?', ''],
        ['Yardıma ihtiyacım olacak mı?', ''],
    ]
    on_tbl = Table(on_data, colWidths=[7*cm, 9.5*cm])
    on_tbl.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'TR-Regular'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TEXTCOLOR', (0,0), (-1,-1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [white, COLOR_VERY_LIGHT]),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    E.append(on_tbl)
    E.append(vsp(0.2))

    adimlar = [
        ('Adım 1: Malzeme Hazırla',
         'Eskizinde yazan malzemeleri masana koy.',
         [('Eksik malzeme var mı?', '( ) Hayır, hepsi hazır    ( ) Evet, şu eksik: ________________________'),
          ('Alternatifim:', '___________________________')]),
        ('Adım 2: Kaba Yapıyı Kur',
         'Önce ölçü veya detay düşünme. Sadece nesnenin dış iskeletini oluştur. '
         '<i>Hatırla: Mükemmel değil, işlevsel olsun — bu bir prototip.</i>',
         [('En çok zorlandığım şey:', '___________________________')]),
        ('Adım 3: Detayları Ekle',
         'Bağlantı noktaları, boyut düzeltmeleri, gerekiyorsa renk veya görsel ekle.',
         []),
        ('Adım 4: Prototipini Tanıt',
         'Prototipini bir arkadaşına ya da öğretmenine göster ve sor: "Bunu kullanmak ister miydin? Neden?"',
         [('Aldığım geri bildirim:', '___________________________')]),
        ('Adım 5: Notlarını Al',
         'Süreç günlüğüne şunları yaz: 1) En çok hangi adımda zorlandım?  '
         '2) Tekrar yapsaydım ne değiştirirdim?  3) Hangi kısım en iyi çalışıyor?',
         []),
    ]

    for baslik, aciklama, satirlar in adimlar:
        blok = [
            Paragraph(f'[  ] {baslik}', S_LBL),
            Paragraph(aciklama, S_GOV),
        ]
        for lbl, alan in satirlar:
            blok.append(Paragraph(f'<b>{lbl}</b>  {alan}', S_LST))
        blok.append(vsp(0.1))
        blok.append(sep())
        E.append(KeepTogether(blok))

    return E


def build_des3():
    E = des_baslik(3, 'Yapılandırılmış Problem Tespiti Soruları')
    E.append(make_student_info_header())
    E.append(vsp(0.15))
    E.append(Paragraph('<i>Bu sayfa, CK1 (Problem Tespiti Formu) doldurmanda sana yardımcı olur. '
                       'Her soruyu sırayla yanıtla. "Bilmiyorum" yazabilirsin.</i>', S_NOT))
    E.append(vsp(0.1))

    bolumler = [
        ('1. Başlangıç: Çevrene Bak',
         'Bugün okulda ya da evde seni rahatsız eden ya da "daha iyi olabilirdi" dediğin bir şey oldu mu?',
         2),
        ('2. Kimin Sorunu?',
         'Bu problemi sen mi yaşıyorsun, yoksa başka biri mi?\n'
         '( ) Ben yaşıyorum     ( ) Başkası yaşıyor: ___________________________     ( ) İkimiz de',
         0),
        ('3. Problemi Somutlaştır',
         '"Ne zaman" sorusu: _______________\n'
         '"Nerede" sorusu: _______________\n'
         '"Neden" sorusu: _______________',
         0),
        ('4. Büyüklüğünü Ölç',
         'Kaç kişi yaşıyor?  ( ) 1–2 kişi     ( ) 5–10 kişi     ( ) 10+ kişi\n'
         'Ne sıklıkla oluyor?  ( ) Her gün     ( ) Haftada birkaç kez     ( ) Ara sıra',
         0),
        ('5. Daha Önce Çözülmüş mü?',
         'Biri bu problemi çözmeye çalışmış mı? Sonuç ne olmuş?',
         1),
        ('6. Problemini Tek Cümleyle Yaz',
         '"___________ problemi var çünkü ___________, bu durum ___________ yaratıyor."',
         1),
    ]

    for baslik, aciklama, satirlar in bolumler:
        blok = [Paragraph(baslik, S_BLM2)]
        for satir in aciklama.split('\n'):
            blok.append(Paragraph(satir, S_GOV))
        if satirlar:
            blok.append(WritingLines(num_lines=satirlar, line_spacing=18))
        blok.append(vsp(0.1))
        blok.append(sep())
        E.append(KeepTogether(blok))

    return E


def build_des4():
    E = des_baslik(4, 'Örnek Cevaplı Empati Haritası')
    E.append(Paragraph(
        '<i>Önce sol taraftaki örneği oku. Sonra sağ tarafı kendi kullanıcın için doldur.</i>',
        S_NOT,
    ))
    E.append(vsp(0.1))

    bolumler = ['NE DÜŞÜNÜYOR?', 'NE HİSSEDİYOR?', 'NE SÖYLÜYOR?', 'NE YAPIYOR?']
    ornek = [
        '"Keşke birisi beni markete götürebilse. Torunlarım geliyor ama çok meşguller."',
        'Yalnızlık, bağımsızlığını kaybetme korkusu, ama aynı zamanda umut.',
        '"Bugün hava biraz daha iyi olursa çıkarım." / "Kaldırımlara tuz serpilse..."',
        'Dışarı çıkmaktan vazgeçiyor, telefonla komşuları arıyor.',
    ]

    header_row = [
        Paragraph('<b>ÖRNEK — Ayşe\'nin Empati Haritası</b>\n'
                  '<i>Kullanıcı: Mehmet Amca, 68 yaşında, kaldırımlar karlı olduğu için markete gidememiş.</i>', S_NOT),
        Paragraph('<b>SENİN ÇALIŞMAN</b>\n<i>Kullanıcım: ___________________________</i>', S_NOT),
    ]

    rows = [header_row]
    for bolum, orn in zip(bolumler, ornek):
        sol = [Paragraph(f'<b>{bolum}</b>', S_BLM2), Paragraph(orn, S_GOV)]
        sag = [Paragraph(f'<b>{bolum}</b>', S_BLM2), WritingLines(num_lines=2, line_spacing=16)]
        rows.append([sol, sag])

    son_row = [
        [Paragraph('<b>EN BÜYÜK ZORLUK:</b>', S_BLM2),
         Paragraph('Karlı kaldırımlarda düşme korkusu', S_GOV),
         Paragraph('<b>TEMEL İHTİYAÇ:</b>', S_BLM2),
         Paragraph('Güvenli ve bağımsız hareket edebilmek', S_GOV)],
        [Paragraph('<b>EN BÜYÜK ZORLUK:</b>', S_BLM2),
         WritingLines(num_lines=1, line_spacing=16),
         Paragraph('<b>TEMEL İHTİYAÇ:</b>', S_BLM2),
         WritingLines(num_lines=1, line_spacing=16)],
    ]
    rows.append(son_row)

    tbl = Table(rows, colWidths=[8.4*cm, 8.4*cm])
    tbl.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('BACKGROUND', (0,0), (-1,0), COLOR_VERY_LIGHT),
        ('LINEAFTER', (0,0), (0,-1), 1, COLOR_ACCENT),
    ]))
    E.append(tbl)
    return E


def build_des5():
    E = des_baslik(5, 'Malzeme–Özellik Eşleştirme')
    E.append(Paragraph(
        '<b>Yönerge:</b> Sol sütundaki her malzeme için, sağ sütundan uygun özellikleri seç ve harf kodunu yaz. '
        'Birden fazla özellik seçebilirsin!',
        S_YON,
    ))
    E.append(vsp(0.15))

    malzemeler = [
        'Karton / Mukavva', 'Köpük (Strafor)', 'Plastik Şişe (geri dönüşüm)',
        'Tahta / Kontraplak', 'Alçı', 'Demir Tel', 'Kumaş / Keçe', 'Toprak / Kil',
    ]
    ozellikler = [
        ('A', 'Hafif ve şekillendirmesi kolay'),
        ('B', 'Dayanıklı ve uzun ömürlü'),
        ('C', 'Geri dönüştürülebilir'),
        ('D', 'Su geçirmez'),
        ('E', 'Isıya dayanıklı'),
        ('F', 'Esnek ve bükülebilir'),
        ('G', 'Doğal malzeme'),
        ('H', 'Düşük maliyetli'),
        ('I', 'Kolay kesilebilir'),
        ('J', 'Yapıştırıcıya iyi tutunur'),
    ]

    # Sol tablo: Malzeme + cevap kutusu
    mal_data = [['#', 'Malzeme', 'Uygun Özellik Kodları']]
    for i, m in enumerate(malzemeler, 1):
        mal_data.append([str(i), m, ''])
    mal_tbl = Table(mal_data, colWidths=[0.7*cm, 5*cm, 5.8*cm])
    mal_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'TR-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'TR-Regular'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TEXTCOLOR', (0,1), (-1,-1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, COLOR_VERY_LIGHT]),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ]))

    # Sag tablo: Özellikler
    ozl_data = [['Hrf', 'Özellik']]
    for hrf, ac in ozellikler:
        ozl_data.append([hrf, ac])
    ozl_tbl = Table(ozl_data, colWidths=[0.8*cm, 4.5*cm])
    ozl_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'TR-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'TR-Regular'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TEXTCOLOR', (0,1), (-1,-1), COLOR_TEXT),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, COLOR_VERY_LIGHT]),
        ('GRID', (0,0), (-1,-1), 0.4, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ]))

    iki_sutun = Table([[mal_tbl, ozl_tbl]], colWidths=[12*cm, 5.5*cm])
    iki_sutun.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (0,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    E.append(iki_sutun)

    E.append(vsp(0.2))
    E.append(sep())
    E.append(vsp(0.15))
    E.append(Paragraph('Oyun Modları', S_BLM))
    oyunlar = [
        '<b>Oyun 1 — Eşleştirme:</b> Malzeme seç, özellik kodlarını yaz.',
        '<b>Oyun 2 — "En Uygun Malzeme Kim?":</b> Öğretmen bir amaç söyler (ör. "suya dayanıklı, hafif stand"). '
        'Hangi malzemeyi seçerdin? Neden?',
        '<b>Oyun 3 — Sürdürülebilirlik Turu:</b> Her malzeme için "Bu malzeme çevreye ne kadar dost?" diye sor. '
        '1 (en az dost) ile 5 (en çok dost) arasında sırala.',
    ]
    for o in oyunlar:
        E.append(Paragraph(o, S_LST))
    return E


def build_des6():
    E = des_baslik(6, '"Nerede Kaldım?" Kontrol Kartları')
    E.append(Paragraph(
        '<i>Her ders sonunda ilgili kartı doldur. Hiç not verilmez — bu sadece senin için!'
        '  V = Evet     /\\ = Biraz     X = Henüz hayır</i>',
        S_NOT,
    ))
    E.append(vsp(0.1))

    KARTLAR = [
        ('1. Ders', 'Tasarım Nedir?',
         ['Design Thinking\'i anlattım', '7 adımın adlarını biliyorum', 'Günlük örnekle anlatabildim'],
         'En çok ilgimi çeken:', 'Sormak istediğim:'),
        ('2. Ders', 'Problem Tespiti',
         ['Gerçek bir problem tespit ettim', 'Problem tespiti formumu doldurdum', 'Problemi 1 cümleyle yazdım'],
         'En çok ilgimi çeken:', 'Sormak istediğim:'),
        ('3. Ders', 'Empati',
         ['Empati ile sempatiyi ayırt ettim', 'Kullanıcımı gözlemledim / düşündüm', 'Empati haritamı doldurdum'],
         'En çok ilgimi çeken:', 'Sormak istediğim:'),
        ('4. Ders', 'Fikir Üretimi',
         ['Crazy 8\'e en az 4 fikir yazdım', 'Fikirleri matrise göre değerlendirdim', 'En güçlü fikri seçtim'],
         'En çok ilgimi çeken:', 'Sormak istediğim:'),
        ('5. Ders', 'Eskiz ve Planlama',
         ['Tasarımımın eskizini çizdim', 'Malzemeleri belirledim', 'Malzeme planlama tabloma yazdım'],
         'En çok ilgimi çeken:', 'Sormak istediğim:'),
        ('6–7. Ders', 'Prototip Yapımı',
         ['Kaba yapıyı tamamladım', 'Süreç günlüğüme bugünü yazdım', 'Zorlukla karşılaştım, çözüm aradım'],
         'En çok zorlandığım:', 'Yarın devam etmem gereken:'),
        ('8. Ders', 'Test ve Geri Bildirim',
         ['Prototipi en az 1 kişiye gösterdim', 'Geri bildirim formumu doldurdum', 'Değişmesi gerekeni not aldım'],
         'En değerli geri bildirim:', 'Sormak istediğim:'),
        ('9. Ders', 'Revize',
         ['En az 1 şeyi değiştirdim', 'Revize planımı doldurdum', 'Sürdürülebilirlik kontrolü yaptım'],
         'En çok fark yaratan değişiklik:', 'Sormak istediğim:'),
        ('10. Ders', 'Sunum ve Ünite Sonu',
         ['Sunum şablonumu doldurdum', 'Tasarım sürecimi sınıfa anlattım', 'Arkadaşımın sunumunu dinledim'],
         'Aklımda kalacak en önemli şey:', 'Design Thinking\'i nerede kullanabilirim?'),
    ]

    def mini_kart(no, konu, kontroller, s1, s2):
        return [
            Paragraph(f'<b>{no} — {konu}</b>', S_KH),
            Paragraph('Ad: _________________  Tarih: ___________', S_KM),
        ] + [Paragraph(f'[ ]  {k}', S_KI) for k in kontroller] + [
            Paragraph(f'<b>{s1}</b>', S_KS),
            WritingLines(num_lines=1, line_spacing=13),
            Paragraph(f'<b>{s2}</b>', S_KS),
            WritingLines(num_lines=1, line_spacing=13),
        ]

    # 5 satirlik grid: sol = ders 1-5, sag = ders 6-10
    sol_kartlar = [mini_kart(*KARTLAR[i]) for i in range(5)]
    sag_kartlar = [mini_kart(*KARTLAR[i]) for i in range(5, 9)] + [[]]

    grid_data = [[sol_kartlar[i], sag_kartlar[i]] for i in range(5)]
    grid = Table(grid_data, colWidths=[8.3*cm, 8.3*cm], rowHeights=[4.3*cm]*5)
    grid.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_LIGHT_GREY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    E.append(grid)
    return E


# ============================================================
# ZENGINLESTİRME: 5 Etkinlik
# ============================================================

def zen_sayfa(no, baslik, gorev, yonerge_items, zorunlu_items, bilgi, olcutler, ipuclari=None, ekstra=None):
    E = zen_baslik(no, baslik)
    E.append(Paragraph(gorev, S_ZGV))

    if ekstra:
        for blok in ekstra:
            E.append(blok)

    E.append(Paragraph('Yönerge', S_BLM))
    E += numarali(yonerge_items)

    E.append(vsp(0.1))
    E.append(Paragraph('Zorunlu Öğeler', S_BLM))
    E += madde(zorunlu_items)

    E.append(vsp(0.1))
    E.append(Paragraph('Biçim ve Teslim', S_BLM))
    E.append(bilgi_kutusu(bilgi))

    E.append(vsp(0.1))
    E.append(sep())
    E.append(vsp(0.1))
    E.append(Paragraph('Değerlendirme', S_BLM))
    E.append(deg_tablo(olcutler))

    if ipuclari:
        E.append(vsp(0.1))
        E.append(Paragraph('İpuçları', S_BLM))
        E += madde(ipuclari)

    return E


def build_zen1():
    return zen_sayfa(
        1, 'Gerçek Sosyal Probleme Tam Design Thinking',
        'Ders boyunca Design Thinking döngüsünü bir öğrenme konusu olarak gördün. '
        'Şimdi bu döngüyü gerçek bir toplumsal sorun için baştan sona kendin uygulayacaksın. '
        'Seçeceğin problem sınıfta çözülecek kadar küçük olmamalı — ama tek başına çözülemeyecek kadar büyük de olmamalı.',
        [
            'Problem Tespiti: Okulun, mahallenin ya da ailen içinden gerçek, gözlemlediğin bir problemi seç.',
            'Empati Kurma: Problemi yaşayan en az 2 farklı kişiyle kısa görüşme veya gözlem yap. Empati haritalarını doldur.',
            'Problem Tanımı Yaz: "Kullanıcı ... ihtiyaç duyar, çünkü ..." formatında net bir tanım üret.',
            'Fikir Geliştirme: En az 8 fikir üret (Crazy 8). Matris ile en güçlü 1\'ini seç.',
            'Prototip: Düşük maliyetli bir prototip ya da hizmet taslağı hazırla.',
            'Test: Prototipi en az 1 gerçek kullanıcıyla test et, geri bildirim al.',
            'Revize: Geri bildirime göre en az 1 iyileştirme yap.',
            'Sunum: 5 dakikalık sunum yap — "Problemi nasıl seçtim, ne öğrendim, ne değiştirdim" sorusunu yanıtla.',
        ],
        [
            'Problem tespiti formu (gerçek gözlem veya görüşme notları)',
            'En az 2 empati haritası',
            'Yazılı problem tanımı ("Kullanıcı / İhtiyaç / Çünkü" formatı)',
            'Crazy 8 kâğıdı + fikir seçim matrisi',
            'Prototip fotoğrafı veya detaylı eskiz',
            'Test notu (kim test etti, ne söyledi, ne değiştirdim)',
            '5 dakikalık sözlü sunum',
        ],
        [('Format', 'Süreç dosyası (tüm aşamalar) + sözlü sunum'),
         ('Süre', '2–3 hafta'),
         ('Teslim', 'Sınıfa sunum + öğretmene dosya')],
        [('Problemin gerçekliği ve empatinin derinliği', 25),
         ('Design Thinking aşamalarına eksiksiz uyum', 30),
         ('Çözümün özgünlüğü ve uygulanabilirliği', 25),
         ('Sunum akıcılığı ve yansıtmanın gücü', 20)],
        ipuclari=[
            '"Mükemmel bir ürün değil, doğru soruya cevap" aramak bu etkinliğin özüdür.',
            'Prototip kâğıt, karton ya da dijital taslak da olabilir — pahalı malzeme şart değil.',
            'Test ederken "Ne kadar beğendin?" değil "Neyi değiştirirdin?" sorusunu sor.',
        ],
    )


def build_zen2():
    return zen_sayfa(
        2, 'Tasarım Portföyü',
        'Bir tasarımcı; daha önce ne ürettiğini, nasıl düşündüğünü ve nasıl geliştiğini gösteren bir portföy tutar. '
        'Bu ünite boyunca ürettiğin tüm çalışmalar aslında senin tasarım portföyünün ilk sayfalarıdır. '
        'Portföyünü oluştururken sadece çalışmalarını derlemeyeceksin — her adımın arkasındaki düşünceyi görünür kılacaksın.',
        [
            'Ünite boyunca doldurduğun tüm çalışma kâğıtlarını (CK1–CK11) bir dosyaya topla.',
            'Her çalışma kâğıdı için 1 yansıtma notu ekle: "Bu adımda ne öğrendim?" ve "Ne değiştirirdim şimdi?"',
            'En anlamlı bulduğun 3 anı / dönüm noktasını seç. Her biri için yarım sayfa yaz: "Neden önemliydi?"',
            'Prototipinin fotoğrafını veya detaylı eskizini portföye ekle.',
            'Kapak sayfası tasarla: Adın, bir tasarım sloganın ve portföyünü yansıtan bir görsel.',
            'Sonuç sayfasına şunu yaz: "Design Thinking bana ne öğretti?" (en az 200 kelime)',
        ],
        [
            'CK1–CK11 tümü (veya seçilmiş en az 7\'si) + yansıtma notları',
            '3 dönüm noktası yazısı (toplam ~1,5 sayfa)',
            'Prototip fotoğrafı veya eskizi',
            'Özgün kapak tasarımı',
            'Sonuç yazısı (en az 200 kelime)',
        ],
        [('Format', 'Fiziksel dosya (klasör/defter) veya dijital PDF'),
         ('Süre', 'Ünite boyunca sürekli güncellenir; final teslim 10. derste'),
         ('Teslim', 'Öğretmene veya sınıf sergisine')],
        [('Çalışmaların eksiksiz toplanması', 20),
         ('Yansıtma notlarının derinliği ve dürüstlüğü', 30),
         ('Dönüm noktası yazılarının anlamı', 25),
         ('Kapak ve genel düzenin özgünlüğü', 10),
         ('Sonuç yazısının kavramsal gücü', 15)],
        ipuclari=[
            'Portföy "güzel görünen" değil, "gerçeği gösteren" belgedir. Hataları da ekle — büyüme orada görünür.',
            'Yansıtma notları "güzel oldu" yerine "şunu fark ettim" ile başlamalı.',
            'Sınıf sonunda portföyü bir sergi olarak paylaşabilirsiniz.',
        ],
    )


def build_zen3():
    return zen_sayfa(
        3, 'IDEO ve Frog Design — Profesyoneller Nasıl Düşünür?',
        'Dünyanın önde gelen tasarım şirketleri olan IDEO ve Frog Design, Design Thinking\'i hayata geçiren firmalardır. '
        'IDEO sağlıktan eğitime; Frog Design teknolojiden sürdürülebilirliğe kadar pek çok alanda insan merkezli tasarım '
        'anlayışıyla ürünler ve sistemler geliştirmiştir. Bu etkinlikte bu iki firmanın yaklaşımını araştırarak '
        'kendi "tasarım felsefeni" geliştirmek için ilham alacaksın.',
        [
            'IDEO ve Frog Design hakkında araştırma yap: Her firmanın tasarım felsefesini öğren.',
            'Her firmadan 1 gerçek proje incele: "Hangi problemi çözdüler? Nasıl?" sorusunu yanıtla.',
            'İki firmanın yaklaşımını karşılaştır: Benzerlikler ve farklılıklar (en az 5 madde).',
            '"Hangi firmanın yaklaşımı sana daha yakın geliyor? Neden?" sorusunu cevapla.',
            'Kendi 3 maddelik "Tasarım Manifestom" yaz: "Tasarlarken şunlara inanıyorum: ..."',
            'Sunumunu hazırla: Sınıfa 5 dakika.',
        ],
        [
            'Her firma için proje analizi (kim, ne sorunu, nasıl çözdü)',
            'Karşılaştırma tablosu (en az 5 madde)',
            '"Hangisi daha yakın?" gerekçesi (en az 150 kelime)',
            '3 maddelik kişisel Tasarım Manifestosu',
            '5 dakikalık sözlü sunum veya A4 poster',
        ],
        [('Format', 'Araştırma notu (A4) + sözlü sunum veya poster'),
         ('Süre', '1–2 hafta'),
         ('Teslim', 'Sınıf sunumu veya öğretmene')],
        [('Araştırmanın kapsamı ve doğruluğu', 30),
         ('Karşılaştırmanın analitik derinliği', 25),
         ('Tasarım Manifestosunun özgünlüğü', 25),
         ('Sunum ya da posterin iletişim gücü', 20)],
        ipuclari=[
            'IDEO.org ve TED.com (David Kelley: "How to build your creative confidence") iyi başlangıç noktalarıdır.',
            'İngilizce kaynak okuyorsan öğretmenle birlikte önemli kısımları Türkçeye çevirebilirsin.',
        ],
    )


def build_zen4():
    return zen_sayfa(
        4, 'Sürdürülebilir Malzeme Karşılaştırma Raporu',
        'Bir prototip yaparken seçtiğimiz malzeme yalnızca "ne kadar işe yarıyor" sorusuna değil, '
        '"dünyaya ne maliyeti var" sorusuna da yanıt vermek zorundadır. Sürdürülebilirlik — doğayı tüketmeden, '
        'geri dönüştürülebilir ve uzun ömürlü çözümler üretmek — modern tasarımın merkezindedir.',
        [
            'Şu malzeme kategorilerinden en az 3\'ünü seç: Plastik, Ahşap, Alüminyum, Geri dönüştürülmüş kâğıt, '
            'Doğal elyaf (jüt/pamuk), Biyobozunur plastik.',
            'Her malzeme için şu başlıkları araştır: üretim kaynağı, yaşam döngüsü, '
            'geri dönüşüm oranı, karbon izi, maliyet ve erişilebilirlik.',
            'Karşılaştırma matrisini doldur (satır: malzeme, sütun: kriter).',
            '"Bir okul atölyesi için en sürdürülebilir 2 malzeme hangisi?" sorusunu gerekçeyle cevapla.',
            'Raporunu bir A4 sayfasında özetle — öğretmenin veliler toplantısında kullanabileceği biçimde.',
        ],
        [
            'En az 3 malzeme analizi (her biri 5 kriter üzerinden)',
            'Karşılaştırma matrisi',
            'Sonuç ve tavsiye (en az 100 kelime, gerekçeli)',
            '1 sayfa özet rapor',
        ],
        [('Format', 'Araştırma raporu (A4, 2–3 sayfa) + 1 sayfa özet'),
         ('Süre', '1 hafta'),
         ('Teslim', 'Öğretmene')],
        [('Araştırmanın kapsamı ve kaynak güvenilirliği', 30),
         ('Karşılaştırma matrisinin tamlığı', 25),
         ('Sonuç ve tavsiyenin gerekçeli olması', 30),
         ('Özet raporun iletişim kalitesi', 15)],
        ipuclari=[
            '"Sürdürülebilir" ile "geri dönüştürülebilir" aynı anlama gelmiyor — farkını araştır.',
            'Maliyetin yalnızca para olmadığını unutma: zaman maliyeti, çevre maliyeti de var.',
            'Raporun sonunda bir "öneri" içermeli — sadece bilgi vermek yetmez.',
        ],
    )


def build_zen5():
    senaryo_ekstra = [
        Paragraph('Senaryo: Okul Bahçesindeki Bekleme Sorunu', S_BLM),
        Paragraph('<b>Problem:</b> 40 dakikalık teneffüste öğrenciler okul bahçesinde '
                  'oturacak yer bulamıyor, özellikle kış aylarında.', S_GOV),
        vsp(0.1),
        Paragraph('<b>Çözüm A — Ahmet\'in Tasarımı:</b> Ahşaptan, rüzgâr kesen cam panelli, 6 kişilik '
                  'kapalı bekleme kabini. Maliyet yüksek, az yer kaplıyor. Test: "sıcak ama karanlık" — '
                  'cam yüzeyi artırılmış. Ergonomi iyi, sürdürülebilirlik orta.', S_GOV),
        Paragraph('<b>Çözüm B — Elif\'in Tasarımı:</b> Eski ahşap paletlerden, sınıfların boyadığı modüler '
                  'oturma köşeleri. Her köşe farklı sınıfın sorumluluğunda. Maliyet düşük, geri dönüşümlü. '
                  'Test: "soğuktan korunmuyor" — bez tenteler eklenmiş. Ergonomi orta, sürdürülebilirlik yüksek.', S_GOV),
        vsp(0.1),
        sep(),
        vsp(0.05),
    ]
    return zen_sayfa(
        5, 'Çeliştirici Tasarım Senaryosu — Hangisi Daha İyi?',
        'Tasarım sürecinde bazen iki farklı tasarımcı aynı probleme tamamen farklı çözümler üretir. '
        'Her ikisi de empati kurmuş, test etmiş, revize etmiştir — yine de sonuçlar birbirinden çok farklıdır. '
        'Sana verilen iki tasarımı Design Thinking açısından analiz et.',
        [
            'Her iki tasarımı şu 5 kriter açısından değerlendir: Empati, özgünlük, test/revize kalitesi, ergonomi, sürdürülebilirlik.',
            'Her iki tasarım için bir "savunma" yaz: "Bu tasarım şu açılardan güçlü..."',
            'Her iki tasarım için bir "eleştiri" yaz: "Bu tasarım şu açılardan geliştirilebilir..."',
            'Kendi değerlendirmeni yaz: "Hangisini seçerdim ve neden?" (en az 150 kelime, Design Thinking kriterlerine dayalı)',
            'Bonus: İki tasarımı birleştirsen nasıl bir çözüm ortaya çıkardı?',
        ],
        [
            'Her iki tasarım için 5 kriterli analiz tablosu',
            'Her tasarım için 1 savunma + 1 eleştiri paragrafı',
            'Kişisel değerlendirme (en az 150 kelime)',
            'Bonus birleşik çözüm önerisi (isteğe bağlı ama önerilir)',
        ],
        [('Format', 'A4 yazılı çalışma'),
         ('Süre', '1–2 ders (ev ödevi olarak da tamamlanabilir)'),
         ('Teslim', 'Öğretmene')],
        [('Her iki analizin Design Thinking kriterlerine uygunluğu', 30),
         ('Savunma ve eleştirilerin gerekçeli olması', 30),
         ('Kişisel değerlendirmenin analitik derinliği', 30),
         ('Yazılı anlatımın netliği', 10)],
        ekstra=senaryo_ekstra,
    )


# ============================================================
# ANA CALISTIRICI
# ============================================================

def uret_destekleme():
    out = os.path.join(ROOT, 'U3_PDF_05_Destekleme.pdf')
    doc = create_doc(out, title='Destekleme Paketi - 3. Unite', unite_info=UI)
    doc.doc_title = 'Destekleme Paketi'

    sayfalar = [build_des1, build_des2, build_des3, build_des4, build_des5, build_des6]
    story = []
    for i, f in enumerate(sayfalar):
        story += f()
        if i < len(sayfalar) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    kb = os.path.getsize(out) // 1024
    print(f'OK  U3_PDF_05_Destekleme.pdf  (6 sayfa, {kb} KB)')


def uret_zenginlestirme():
    out = os.path.join(ROOT, 'U3_PDF_06_Zenginlestirme.pdf')
    doc = create_doc(out, title='Zenginlestirme Paketi - 3. Unite', unite_info=UI)
    doc.doc_title = 'Zenginlestirme Paketi'

    sayfalar = [build_zen1, build_zen2, build_zen3, build_zen4, build_zen5]
    story = []
    for i, f in enumerate(sayfalar):
        story += f()
        if i < len(sayfalar) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    kb = os.path.getsize(out) // 1024
    print(f'OK  U3_PDF_06_Zenginlestirme.pdf  (5 sayfa, {kb} KB)')


if __name__ == '__main__':
    print('3. Unite Destekleme + Zenginlestirme PDF uretiliyor...')
    uret_destekleme()
    uret_zenginlestirme()
    print('Tamamlandi.')
