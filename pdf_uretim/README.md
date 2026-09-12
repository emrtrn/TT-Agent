# 🐍 PDF Üretim Modülü

> Bu klasör, markdown dosyalarını profesyonel PDF'lere dönüştüren Python kodlarını içerir.

> **8. sınıf notu:** `pdf_style.py`, `md_converter.py` ve `config.py` ortak altyapıdır. Mevcut `uret_*.py` dosyaları ile `ornek_uretim.py` eski 7. sınıf üretimlerinden kalmıştır; 8. sınıf için doğrudan çalıştırılmaz. Her 8. sınıf üretim betiği güncel MEB ünite içeriğine ve `units/8_sinif/unitN/` yoluna göre ayrıca hazırlanır.

---

## 📂 Dosyalar

| Dosya | Görev |
|-------|-------|
| `pdf_style.py` | Ortak stil (font, renk, paragraf stili, özel flowable'lar) |
| `md_converter.py` | Markdown → PDF dönüştürücü (otomatik emoji temizleme, tablo, başlık) |
| `config.py` | Merkezi tercih ayarları (40 dk, 20 öğrenci, vb.) |
| `ornek_uretim.py` | Eski 7. sınıf akışını gösteren, yalnızca mimari referans niteliğinde örnek |

---

## 🔧 Gereksinimler

```bash
pip install reportlab pypdf pdf2image
```

### Sistem Gereksinimleri (Türkçe karakter için)

```bash
# Ubuntu / Debian
sudo apt install fonts-dejavu

# macOS (Homebrew)
brew install --cask font-dejavu
```

DejaVu fontları yoksa Türkçe karakterler düzgün gözükmez!

---

## 🚀 Hızlı Başlangıç

```python
import sys
sys.path.insert(0, '/path/to/agent-paket/pdf_uretim')

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file
from config import kapak_meta

# Markdown'ı oku
md = read_md_file('Unite1_Ders_Plani.md')

# PDF'e çevir
build_pdf_from_md(
    md_content=md,
    output_path='01_Ders_Plani.pdf',
    title='1. Ünite Ders Planı',
    subtitle='Teknoloji ve Tasarım Öğreniyorum',
    meta_info=kapak_meta(saat_sayisi=4),
    doc_type='Öğretmen Rehberi',
    add_cover=True,
    skip_top_title=True,
)
```

---

## 🎨 Tasarım Sistemi

### Renkler (`pdf_style.py`)

| Değişken | Hex | Kullanım |
|----------|-----|----------|
| `COLOR_PRIMARY` | `#C2410C` | Ana başlıklar |
| `COLOR_SECONDARY` | `#9A3412` | Alt vurgu |
| `COLOR_ACCENT` | `#EA580C` | Alt başlıklar |
| `COLOR_LIGHT` | `#FED7AA` | Açık dolgu |
| `COLOR_VERY_LIGHT` | `#FFF7ED` | Yönerge kutusu arka plan |
| `COLOR_TEXT` | `#1F2937` | Ana metin |
| `COLOR_MUTED` | `#6B7280` | Yardımcı metin |
| `COLOR_WRITING_LINE` | `#D1D5DB` | Öğrenci yazı çizgileri |

### Font

DejaVu Sans ailesi (Türkçe karakter destekli):
- `TR-Regular`
- `TR-Bold`
- `TR-Italic`
- `TR-BoldItalic`
- `TR-Mono`

`register_fonts()` fonksiyonu otomatik çalışır.

---

## 🔄 Markdown → PDF Dönüşüm Kuralları

| Markdown | PDF Çıktısı |
|----------|-------------|
| `# Başlık` | Heading 1 (16pt, koyu turuncu) |
| `## Alt Başlık` | Heading 2 (13pt, koyu turuncu) |
| `### Detay` | Heading 3 (11pt, turuncu) |
| `**kalın**` | **Kalın metin** |
| `*italik*` | *İtalik metin* |
| `` `kod` `` | `Mono fontla kod` |
| `- madde` | • madde (bullet point) |
| `1. madde` | 1. madde (numbered) |
| `> not` | İtalik gri not |
| `\| tablo \|` | Koyu turuncu başlıklı tablo |
| `---` | Yatay çizgi |
| `[çizgi alanı]` | Hafif gri yazı çizgisi (özel) |

---

## ⚙️ Ana Fonksiyonlar

### `pdf_style.py`

#### `register_fonts()`
Türkçe destekli fontları kaydet. **Otomatik çalışır.**

#### `get_styles() -> dict`
Tüm paragraf stillerini döndürür: Title, Heading1-3, Body, Bullet, Note, Yonerge, vb.

#### `create_doc(filename, title, unite_info=None) -> SimpleDocTemplate`
Standart A4 doküman oluştur.

#### `add_page_number(canvas, doc)`
Her sayfanın üst-alt bantlarını çizer. `doc.build()` çağrısında parametre olarak ver.

#### `make_cover(title, subtitle, meta_info, document_type) -> List`
Kapak sayfası flowable'ları oluşturur.

#### `make_student_info_header() -> Table`
Öğrenci bilgi alanı (Adı-Soyadı / Sınıf / Tarih çizgili tablosu).

### `md_converter.py`

#### `build_pdf_from_md(md_content, output_path, title, ...) -> str`
Markdown içeriğini doğrudan PDF'e çevirir. **Ana giriş noktası.**

Parametreler:
- `md_content`: Markdown metni
- `output_path`: PDF çıktı yolu
- `title`: Doküman başlığı
- `subtitle`: Alt başlık (kapakta)
- `meta_info`: Kapak meta bilgileri (dict)
- `doc_type`: "Öğretmen Rehberi" / "Öğrenci Materyali" / vb.
- `add_cover`: True / False / None (None: 4+ sayfada otomatik)
- `skip_top_title`: True ise üstteki ilk `# Başlık`'ı atlar (kapakta var diye)
- `unite_info`: Sayfa üstündeki bilgi metni

#### `clean_emojis(text) -> str`
Desteklenmeyen emojileri temizler. **build_pdf_from_md otomatik çağırır.**

#### `extract_section(md_content, start_marker, end_marker) -> str`
Markdown'dan bir bölümü çıkarır.

---

## 🎨 Özel Flowable'lar

### `MindMapCanvas(center_word, ...)`
Zihin haritası: merkez kelime + 8 dal.

```python
elements.append(MindMapCanvas('TEKNOLOJİ', height=8.5*cm, num_branches=8))
```

### `VennDiagram(label1, label2, ...)`
İki örtüşen Venn dairesi.

```python
elements.append(VennDiagram(label1='Ürün 1', label2='Ürün 2', height=8*cm))
```

### `WritingLines(num_lines, ...)`
Öğrenci yazı çizgileri (hafif gri).

```python
elements.append(WritingLines(num_lines=4))
```

### `DrawingBox(width, height, caption)`
Boş çizim alanı (öğrenci için).

```python
elements.append(DrawingBox(height=6*cm, caption='Buraya çizim yap'))
```

### `Checkbox()`
Tek bir onay kutusu.

```python
elements.append(Checkbox(size=10))
```

### `HorizontalLine(color, thickness)`
Dekoratif yatay çizgi.

```python
elements.append(HorizontalLine(color=COLOR_ACCENT, thickness=2))
```

---

## 🚫 Bilinen Sınırlamalar

### 1. Emoji Sorunu
DejaVu Sans birçok emojiyi desteklemiyor. **Otomatik olarak temizlenir.**

Desteklenen: `→ ← ↑ ↓ ✓ ✗ ● ○ ■ □ ★ ☆`  
Desteklenmeyen: `🟦 📊 💡 🎯 📋 📝 🚀 🎨 🔍 (otomatik temizlenir)`

### 2. Tablolarda `<br>` Etiketi
HTML `<br>` etiketi reportlab'da hata verir. **Otomatik olarak `<br/>` self-closing'e çevrilir.**

### 3. Markdown İç İçe Listeler
Karmaşık iç içe listeler hata verebilir. Düz liste tercih et.

### 4. Görseller
Şu an dış görsel desteği YOK. Sadece içsel çizimler (Mind map, Venn vs.) destekleniyor.

---

## 🐛 Sorun Giderme

### Türkçe karakterler kutucuk olarak görünüyor
- `register_fonts()` fonksiyonu çalıştı mı? `from pdf_style import *` ile otomatik çalışmalı
- `/usr/share/fonts/truetype/dejavu/` dizinindeki fontlar mevcut mu?
- `fc-list | grep DejaVu` ile kontrol et

### Tablo `<br>` hatası
- `md_converter.py` v2'den itibaren otomatik düzeltilir
- Manuel olarak `<br>` yerine `<br/>` kullan

### Sayfa numarası gözükmüyor
- `doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)` parametrelerini kontrol et

### Kapak sayfası gözükmüyor
- `add_cover=True` parametresi verildi mi?
- Doküman 4+ sayfa mı? (None ise otomatik 4+'ta ekler)

### Emoji kalıntısı
- `clean_emojis()` çağrılıyor mu? `build_pdf_from_md` otomatik çağırır
- Yeni bir emoji türü mü var? Pattern'a ekle

---

## 📦 Tipik Üretim Akışı

```python
# 1. Stil ve config yükle
from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file
from config import kapak_meta, unite_bilgisi

UNITE_NO = 1
UNITE = unite_bilgisi(UNITE_NO)

# 2. Çıktı dizini hazırla
import os
os.makedirs('./pdfs/', exist_ok=True)

# 3. Markdown'ları oku ve PDF üret
md = read_md_file('./materials/Unite1_Ders_Plani.md')

build_pdf_from_md(
    md_content=md,
    output_path='./pdfs/01_Ders_Plani.pdf',
    title=f'{UNITE_NO}. Ünite Ders Planı',
    subtitle=UNITE['ad'],
    meta_info=kapak_meta(saat_sayisi=UNITE['saat']),
    doc_type='Öğretmen Rehberi',
    add_cover=True,
    skip_top_title=True,
    unite_info=UNITE['unite_info_string'],
)

# 4. Kontrol
from pypdf import PdfReader
r = PdfReader('./pdfs/01_Ders_Plani.pdf')
print(f'Toplam sayfa: {len(r.pages)}')
```

---

## 🎯 Yaygın PDF Üretim Yapıları

### Bir markdown → 1 PDF
Çoğu durum için. Üstteki örnek.

### Bir markdown → N PDF (bölme)
Markdown'ı satır numarasına göre dilimle:
```python
md = read_md_file('Unite1_Calisma_Kagitlari.md')
lines = md.split('\n')

# Çalışma kâğıdı 1: satır 26-107
md_kagit_1 = '\n'.join(lines[26:107])
build_pdf_from_md(md_content=md_kagit_1, ...)

# Çalışma kâğıdı 2: satır 108-183
md_kagit_2 = '\n'.join(lines[108:183])
build_pdf_from_md(md_content=md_kagit_2, ...)
```

### Tamamen özel (ASCII sanat yerine):
```python
doc = create_doc('output.pdf', title='Zihin Haritam')
elements = []

elements.append(make_student_info_header())
elements.append(yonerge_box('<b>Yönerge:</b> ...'))
elements.append(MindMapCanvas('TEKNOLOJİ'))  # Özel flowable!
elements.append(WritingLines(num_lines=3))

doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
```

> Bu yaklaşım Zihin Haritası, Venn diyagramı, Süreç Gözlem Formu gibi özel görseller için kullanılır.
