"""
ÖRNEK PDF ÜRETİM SCRIPT'İ

Bu dosya, agent'ın PDF üretirken nasıl bir yapı izleyeceğini gösterir.
Her ünite için benzer bir script üretilmeli.

Kullanım:
    python ornek_uretim.py
"""

import sys
import os

# Proje köküne ulaş
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file
from config import kapak_meta, kapak_meta_kazanim, unite_bilgisi, pdf_dosya_adi


# ============================================================
# AYARLAR — Bunları ünite başına özelleştir
# ============================================================

UNITE_NO = 1  # Hangi ünite
UNITE = unite_bilgisi(UNITE_NO)
SAAT_SAYISI = UNITE['saat']

# Kaynak markdown'lar burada
MD_DIZIN = './materials/unite-1/'
# PDF'lerin çıkacağı dizin
PDF_DIZIN = './pdfs/unite-1/'

os.makedirs(PDF_DIZIN, exist_ok=True)


# ============================================================
# GRUP 1: Öğretmen Referans Dokümanları
# ============================================================

print('=== GRUP 1: Öğretmen Referans ===')

# PDF 1: Ders Planı
md = read_md_file(f'{MD_DIZIN}Unite{UNITE_NO}_Ders_Plani.md')
build_pdf_from_md(
    md_content=md,
    output_path=f'{PDF_DIZIN}{pdf_dosya_adi(1, "Ders_Plani")}',
    title=f'{UNITE_NO}. Ünite Ders Planı',
    subtitle=UNITE['ad'],
    meta_info=kapak_meta_kazanim(SAAT_SAYISI),
    doc_type='Öğretmen Rehberi',
    add_cover=True,
    skip_top_title=True,
    unite_info=UNITE['unite_info_string'],
)
print(f'  ✓ {pdf_dosya_adi(1, "Ders_Plani")}')

# PDF 2: Genel Özet (varsa)
if os.path.exists(f'{MD_DIZIN}Unite{UNITE_NO}_Genel_Ozet.md'):
    md = read_md_file(f'{MD_DIZIN}Unite{UNITE_NO}_Genel_Ozet.md')
    build_pdf_from_md(
        md_content=md,
        output_path=f'{PDF_DIZIN}{pdf_dosya_adi(2, "Genel_Ozet")}',
        title='Genel Özet ve Uygulama Rehberi',
        subtitle=f'{UNITE_NO}. Ünite Materyal Paketi',
        meta_info=kapak_meta(SAAT_SAYISI),
        doc_type='Öğretmen Referansı',
        add_cover=True,
        skip_top_title=True,
        unite_info=UNITE['unite_info_string'],
    )
    print(f'  ✓ {pdf_dosya_adi(2, "Genel_Ozet")}')


# ============================================================
# GRUP 2: Ön Değerlendirme (3 PDF)
# ============================================================

print('\n=== GRUP 2: Ön Değerlendirme ===')

# Ön Değerlendirme markdown'ı 3 ayrı PDF'e bölünür:
# 1) Öğretmen Rehberi (cevap anahtarları dahil)
# 2) Öğrenci Uygulaması 1 (zihin haritası + tanılama + açık uçlu)
# 3) Öğrenci Uygulaması 2 (eşleştirme + boşluk doldurma)

md = read_md_file(f'{MD_DIZIN}Unite{UNITE_NO}_On_Degerlendirme.md')
lines = md.split('\n')

# Bu örnekte basitleştirilmiş - her ünitenin bölme yapısı farklı olabilir
# Gerçek üretimde bölmeyi içerik bazlı yap

# PDF 3: Tüm öğretmen kısmı (basit yaklaşım)
build_pdf_from_md(
    md_content=md,
    output_path=f'{PDF_DIZIN}{pdf_dosya_adi(3, "On_Degerlendirme_Ogretmen")}',
    title='Ön Değerlendirme — Öğretmen Rehberi',
    subtitle='Rehber, Cevap Anahtarları ve Yorumlama',
    meta_info=kapak_meta(SAAT_SAYISI, Uygulama='Ünite başlangıcı'),
    doc_type='Öğretmen Rehberi',
    add_cover=True,
    skip_top_title=True,
    unite_info=UNITE['unite_info_string'],
)
print(f'  ✓ {pdf_dosya_adi(3, "On_Degerlendirme_Ogretmen")}')


# ============================================================
# GRUP 4: Çalışma Kâğıtları (8 ayrı PDF)
# ============================================================

print('\n=== GRUP 4: Çalışma Kâğıtları ===')

# Her çalışma kâğıdı ayrı PDF
# Zihin haritası ve Venn diyagramı için ÖZEL üretim yap (aşağıda örnek)


def produce_zihin_haritasi(pdf_path, kazanim='Ön değerlendirme', sure='5 dakika'):
    """Özel: Zihin Haritası çalışma kâğıdı (MindMapCanvas ile)"""
    doc = create_doc(pdf_path,
                     title='Çalışma Kâğıdı 1 — Zihin Haritam',
                     unite_info=UNITE['unite_info_string'])
    styles = get_styles()
    elements = []
    
    # Öğrenci bilgi başlığı
    elements.append(make_student_info_header())
    elements.append(Spacer(1, 6))
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 8))
    
    # Ana başlık
    elements.append(Paragraph('Çalışma Kâğıdı 1 — Zihin Haritam', styles['Heading1']))
    
    # Yönerge kutusu
    yonerge_text = ('<b>Yönerge:</b> Aşağıdaki iki merkez kelimeyi görüyorsun: <b>TEKNOLOJİ</b> ve <b>TASARIM</b>. '
                    'Bu kelimeleri duyunca aklına hangi kelimeler, kavramlar, nesneler, örnekler geliyor? '
                    'Aklına gelen her şeyi oklarla bağlayarak yaz.<br/><br/>'
                    f'<b>Süre:</b> {sure} &nbsp;&nbsp;•&nbsp;&nbsp; <b>Not:</b> Doğru/yanlış cevap yok!')
    elements.append(yonerge_box(yonerge_text))
    elements.append(Spacer(1, 6))
    
    # İlk zihin haritası
    elements.append(Paragraph('TEKNOLOJİ', styles['Heading2']))
    elements.append(MindMapCanvas('TEKNOLOJİ', height=8.5*cm, num_branches=8))
    elements.append(Spacer(1, 10))
    
    # İkinci zihin haritası
    elements.append(Paragraph('TASARIM', styles['Heading2']))
    elements.append(MindMapCanvas('TASARIM', height=8.5*cm, num_branches=8))
    elements.append(Spacer(1, 10))
    
    # Son soru
    elements.append(Paragraph('Son Soru', styles['Heading2']))
    elements.append(Paragraph(
        'Sence <b>teknoloji</b> ile <b>tasarım</b> birbiriyle ilişkili mi? Neden?',
        styles['Body']
    ))
    elements.append(WritingLines(num_lines=3))
    
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'  ✓ {os.path.basename(pdf_path)} (özel)')


# Zihin haritası özel üretim
produce_zihin_haritasi(f'{PDF_DIZIN}{pdf_dosya_adi(8, "Calisma_Kagidi_1_Zihin_Haritam")}')


# ============================================================
# Diğer çalışma kâğıtları (markdown'dan otomatik)
# ============================================================

# Tek bir markdown'dan birden fazla PDF üretmek için içeriği bölmek gerekir.
# Örnek:

md_kagitlar = read_md_file(f'{MD_DIZIN}Unite{UNITE_NO}_Calisma_Kagitlari.md')

# extract_section ile her bölümü ayır
# Veya satır numarasına göre dilim al

# Bu örnekte basit gösterim:
# (Gerçek üretimde her çalışma kâğıdı için bir build_pdf_from_md çağrısı)

print('\n=== Üretim tamamlandı ===')
print(f'PDF\'ler şu dizinde: {PDF_DIZIN}')
