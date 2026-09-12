# 🎨 Renk Paleti

> Tüm PDF'lerde kullanılan koyu turuncu temalı renk sistemi.

---

## 🟧 Ana Palet

```
┌──────────────────────────────────────────────────────┐
│  KOYU TURUNCU TEMA                                   │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ████  #C2410C   PRIMARY      Ana başlıklar          │
│  ████  #9A3412   SECONDARY    Daha koyu vurgu        │
│  ████  #EA580C   ACCENT       Alt başlıklar          │
│  ████  #FED7AA   LIGHT        Açık dolgu             │
│  ████  #FFF7ED   VERY_LIGHT   Yönerge kutusu         │
│                                                       │
│  ████  #1F2937   TEXT         Ana metin              │
│  ████  #6B7280   MUTED        Yardımcı metin         │
│  ████  #E5E7EB   LIGHT_GREY   Çerçeveler             │
│  ████  #F9FAFB   VERY_LIGHT   Tablo şeritleri        │
│  ████  #D1D5DB   WRITING      Yazı çizgileri         │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

## 📋 Detaylı Kullanım

### Birincil Renk: `#C2410C` (Koyu Turuncu)
**Kullanım yerleri:**
- Tüm başlıklar (H1, H2, H3)
- Tablo başlık satırı (zemin)
- Vurgu metinleri (`<b>` içindeki önemli kelimeler bold üzerine)
- Kapak sayfasındaki ana başlık
- Üst banttaki ince çizgi

**RGB:** `(194, 65, 12)` • **CMYK:** `0, 67, 94, 24` • **HSL:** `19°, 88%, 40%`

### İkincil Renk: `#9A3412`
**Kullanım yerleri:**
- Heading 2 (orta seviye başlıklar)
- Tablo başlık altındaki ayırıcı çizgi
- Çok güçlü vurgu metinleri
- Kod inline (`backtick` içeriği)

### Aksan Renk: `#EA580C`
**Kullanım yerleri:**
- Heading 3 (alt başlıklar)
- Kapak sayfasındaki dekoratif çizgi
- Sayfa üstündeki ince ayırıcı çizgi
- "ÖĞRETMEN REHBERİ" gibi etiket metinleri

### Açık Ton: `#FED7AA`
**Kullanım yerleri:**
- Yönerge kutusu arka planı (alternatif)
- Tablo hücresi vurgu (zorunlu hücreler)
- Önemli notlar arka planı

### Çok Açık: `#FFF7ED`
**Kullanım yerleri:**
- Yönerge kutusu arka planı (varsayılan)
- Kapak sayfası alt bilgi alanı
- Bilgilendirme kutuları

### Metin: `#1F2937`
**Kullanım yerleri:**
- Tüm gövde metni
- Tablo veri hücreleri
- Form etiketleri (Adı Soyadı, vb.)

### Yardımcı Metin: `#6B7280`
**Kullanım yerleri:**
- Üst-alt bantlardaki bilgiler
- "Süre: 5 dakika" gibi bilgiler
- Kapak meta bilgileri (Sınıf, Süre, vb.)
- Italik notlar

### Açık Gri: `#E5E7EB`
**Kullanım yerleri:**
- Tablo iç çizgileri (grid)
- Bölüm ayırıcı yatay çizgiler
- Sayfa altındaki ayırıcı çizgi

### Çok Açık Gri: `#F9FAFB`
**Kullanım yerleri:**
- Tablo alternatif satır arka planları
- Kod blokları arka planı
- Hafif vurgulu kutular

### Yazı Çizgisi: `#D1D5DB`
**Kullanım yerleri:**
- Öğrenci yazı alanları (WritingLines)
- Çizim alanı kenarları (DrawingBox)
- Form alanlarındaki "________" çizgileri

> **Bu renk, çıktıda silik görünmesi için seçildi.** Yazıcıdan çıkışta öğrenci yazıyı görünce çizgi rahatsız etmiyor.

---

## 🎯 Renk Hiyerarşisi

Bir tasarımda renklerin **görsel önceliği**:

```
ANA BAŞLIK (#C2410C)            ← En çok dikkat çeker
   ↓
ALT BAŞLIK (#9A3412)            ← İkinci önemde
   ↓
KÜÇÜK BAŞLIK (#EA580C)          ← Üçüncü önemde
   ↓
GÖVDE METNİ (#1F2937)           ← Standart okuma
   ↓
YARDIMCI METİN (#6B7280)        ← Detay/dipnot
   ↓
ARKA PLAN ELEMANLARI (#E5E7EB)  ← Çerçeveler, ayırıcılar
```

---

## ✅ Renk Kullanım Kuralları

### Yapılması Gerekenler
- ✅ Tüm başlıklarda **birincil renk** (#C2410C)
- ✅ Tablo başlıklarında **birincil renk** (zemin), beyaz metin
- ✅ Vurgu için **kalın metin + birincil renk** birlikte
- ✅ Kapak sayfasında **dekoratif çizgi** aksan rengiyle (#EA580C)
- ✅ Tablo alternatif satırlar **çok açık gri** (#F9FAFB)

### Yapılmaması Gerekenler
- ❌ **Çok fazla renk** kullanma — palet sınırlı tutulsun
- ❌ Vurgu için **kırmızı** kullanma (turuncu paletini kır)
- ❌ Mavi/yeşil **rastgele** kullanma — sadece çapraz referanslarda
- ❌ Tüm metni **birincil renkle** yazma — okumayı zorlaştırır
- ❌ Yönerge kutusu içinde **birden fazla arka plan rengi**

---

## 🖨️ Baskı Önerileri

### Renkli Baskı
- Tüm renkler korunur
- Maliyet daha yüksek (öğrenci sayısına göre)

### Siyah-Beyaz Baskı (Ekonomik)
- **Birincil renk** → Koyu gri tonu olur (kontrastı korur)
- **Çok açık gri arkalar** → Hafif gri tonu olur (görünür)
- **Yazı çizgileri (#D1D5DB)** → Yine silik kalır (uygun)
- **Tablo başlık zemini** → Koyu gri olur, beyaz metin korunur

> Siyah-beyaz baskı için **ek değişiklik gerekmez** — palet bu durumla uyumlu.

---

## 💻 Kullanım Örneği (Python)

```python
from pdf_style import (
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT,
    COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY,
    COLOR_WRITING_LINE
)

# Tablo başlığı için
table_header_color = COLOR_PRIMARY

# Yönerge kutusu için
yonerge_arka_plan = COLOR_VERY_LIGHT

# Yazı çizgisi için
yazi_cizgi_renk = COLOR_WRITING_LINE
```

---

## 🌈 Alternatif Tema (Eğer Kullanıcı İsterse)

Mevcut palet **koyu turuncu temalı**. Eğer kullanıcı başka bir tema isterse:

### Koyu Mavi Tema
```python
COLOR_PRIMARY = HexColor('#1E3A8A')      # Donanma mavisi
COLOR_SECONDARY = HexColor('#1E40AF')
COLOR_ACCENT = HexColor('#3B82F6')
COLOR_LIGHT = HexColor('#BFDBFE')
COLOR_VERY_LIGHT = HexColor('#EFF6FF')
```

### Koyu Yeşil Tema
```python
COLOR_PRIMARY = HexColor('#065F46')
COLOR_SECONDARY = HexColor('#047857')
COLOR_ACCENT = HexColor('#10B981')
COLOR_LIGHT = HexColor('#A7F3D0')
COLOR_VERY_LIGHT = HexColor('#ECFDF5')
```

> **Kullanıcı isterse** `pdf_style.py`'da renk sabitlerini değiştirip tüm sistemde tema dönüşür.
