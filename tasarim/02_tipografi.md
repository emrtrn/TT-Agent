# 🔤 Tipografi

> Yazı tipi seçimleri, boyutlar, satır aralıkları ve okunabilirlik kuralları.

---

## 📚 Font Ailesi: DejaVu Sans

**Neden DejaVu Sans?**
- ✅ **Türkçe karakter desteği eksiksiz** (Ğğ, Şş, İı, Çç, Üü, Öö)
- ✅ Açık kaynak ve ücretsiz
- ✅ Tüm Linux dağıtımlarında varsayılan yüklü
- ✅ Sans-serif (modern, profesyonel görünüm)
- ✅ Geniş Unicode desteği (matematiksel semboller, oklar)

**Neden başka değil?**
- ❌ Calibri, Arial → Türkçe karakter destekli ama lisans sorunu olabilir
- ❌ Times New Roman → Serif font okumayı zorlaştırır (özellikle ekranda)
- ❌ Comic Sans → Profesyonel değil
- ❌ Helvetica → Lisanslı, sistemde yok

---

## 📐 Font Varyantları

| Varyant | Dosya | Kullanım |
|---------|-------|----------|
| Regular | `DejaVuSans.ttf` | Gövde metni, normal yazılar |
| Bold | `DejaVuSans-Bold.ttf` | Başlıklar, vurgu metinleri |
| Italic | `DejaVuSans-Oblique.ttf` | Notlar, yardımcı bilgiler |
| BoldItalic | `DejaVuSans-BoldOblique.ttf` | Çift vurgu (nadir kullan) |
| Mono | `DejaVuSansMono.ttf` | Kod, sabit genişlikli içerik |

**Reportlab'da kayıt adları:**
- `TR-Regular`
- `TR-Bold`
- `TR-Italic`
- `TR-BoldItalic`
- `TR-Mono`

---

## 📏 Boyut Hiyerarşisi

### Doküman İçi (Standart)

| Element | Boyut | Stil | Renk |
|---------|:----:|------|------|
| Title (üstdeki büyük başlık) | **22pt** | Bold | Birincil (#C2410C) |
| Heading 1 (`##`) | **16pt** | Bold | Birincil |
| Heading 2 (`###`) | **13pt** | Bold | İkincil (#9A3412) |
| Heading 3 (`####`) | **11pt** | Bold | Aksan (#EA580C) |
| Body (gövde metin) | **10pt** | Regular | Metin (#1F2937) |
| Body Compact (sıkı body) | **10pt** | Regular | Metin |
| Bullet (madde listesi) | **10pt** | Regular | Metin |
| Note (italik not) | **9pt** | Italic | Yardımcı (#6B7280) |
| Highlight (vurgu) | **10pt** | Bold | İkincil |
| Form Label | **10pt** | Bold | Metin |

### Tablo Boyutları

| Tablo Tipi | Başlık | Veri |
|----------|:----:|:---:|
| Standart tablo | 9pt Bold | 9pt Regular |
| Geniş tablo (Süreç gözlem) | 9pt Bold | 9pt Regular |
| Küçük tablo (Form) | 10pt Bold | 10pt Regular |

### Üst-Alt Bant

| Bant | Boyut | Stil |
|------|:----:|------|
| Üst sol (ünite info) | 8pt | Regular |
| Üst sağ (doküman adı) | 8pt | Regular |
| Alt sol (Maarif Modeli) | 8pt | Italic |
| Alt sağ (Sayfa N) | 9pt | Regular |

### Kapak Sayfası

| Element | Boyut | Stil |
|---------|:----:|------|
| Üst etiket (ÖĞRETMEN REHBERİ) | 11pt | Bold |
| Ana başlık | **28pt** | Bold |
| Alt başlık | 16pt | Regular |
| Meta bilgi | 12pt | Regular |
| Alt bilgi (Maarif vb.) | 10pt | Italic |

---

## 📎 Satır Aralığı (Leading)

| Element | Boyut | Leading |
|---------|:----:|:-----:|
| Title | 22pt | **26pt** |
| Heading 1 | 16pt | **20pt** |
| Heading 2 | 13pt | **16pt** |
| Heading 3 | 11pt | **14pt** |
| Body | 10pt | **14pt** |
| BodyCompact | 10pt | **13pt** |
| Bullet | 10pt | **14pt** |
| Note | 9pt | **12pt** |
| Tablo metin | 9pt | **12pt** |
| Yazı çizgileri | — | **20pt aralık** |

**Genel kural:** Leading, font boyutunun **1.3-1.5 katı** olmalı. Bu, **göz dinlendirici** okumayı sağlar.

---

## 🎯 Hizalama (Alignment)

| Element | Hizalama |
|---------|----------|
| Başlıklar | TA_LEFT (sol) |
| Body metin | TA_JUSTIFY (iki yana yaslı) |
| Tablo başlık | TA_CENTER |
| Tablo veri | TA_LEFT |
| Notlar | TA_LEFT |
| Form etiketi | TA_LEFT |
| Kapak ana başlık | TA_CENTER |
| Kapak alt başlık | TA_CENTER |
| Sayfa numarası | TA_RIGHT |
| Üst-alt bant sol bilgi | TA_LEFT |
| Üst-alt bant sağ bilgi | TA_RIGHT |

---

## 📦 Kutu İçi Tipografi

### Yönerge Kutusu (`#FFF7ED` arkalı)
- Font: TR-Regular
- Boyut: 10pt
- Leading: 14pt
- Iç boşluk: 8pt
- Sol/sağ kenar boşluğu: 8pt

### Vurgu Kutusu (Bold + Bg Color)
- Font: TR-Bold
- Boyut: 10pt
- Arka plan: Çok açık gri veya açık turuncu

### Kod Bloğu
- Font: TR-Mono
- Boyut: 8pt
- Leading: 11pt
- Arka plan: Çok açık gri (#F9FAFB)
- Iç boşluk: 6pt

---

## ✏️ İnline Stil Kuralları

### Markdown → PDF Eşlemesi

| Markdown | PDF |
|----------|-----|
| `**kalın**` | `<b>kalın</b>` (TR-Bold otomatik seçilir) |
| `*italik*` | `<i>italik</i>` (TR-Italic otomatik seçilir) |
| `***kalın italik***` | `<b><i>kalın italik</i></b>` |
| `` `kod` `` | TR-Mono, 9pt, koyu kırmızımsı (#9A3412) |
| `~~üstü çizili~~` | `<strike>üstü çizili</strike>` |

### İç İçe Stil Limiti
- En fazla **2 stil** iç içe kullan: `**_metin_**` ✅
- 3 stil iç içe → karmaşıklık artar, kaçın

---

## 🎨 Vurgu Stratejisi

Bir paragrafta **vurgu sayısı** sınırlı tutulmalı:

✅ İyi:
> "Tasarım, sadece **estetik** değil, **işlevselliği** de kapsar."

❌ Kötü:
> "**Tasarım**, sadece *estetik* değil, **işlevselliği** de kapsar ve `çok önemli` bir konudur."

**Kural:** Bir paragrafta en fazla **2 vurgu** olmalı, biri **kalın**, diğeri **italik** olabilir.

---

## 🌍 Karakter Setleri

### Mutlaka Desteklenmeli
- Türkçe: ç ğ ı i ö ş ü Ç Ğ I İ Ö Ş Ü
- Latin temel: a-z A-Z 0-9
- Noktalama: . , ; : ! ? ' " " " - — …
- Para birimleri: ₺ $ €
- Matematiksel: + - × ÷ = ≤ ≥ < > ≠ ± ∞
- Yüzde, sayı: % ‰

### Sınırlı Destekli (Dikkat!)
- Oklar: → ← ↑ ↓ ↔ ⇒ ⇐ (DejaVu desteklemiyor olabilir, test et)
- Geometrik: ● ○ ■ □ ◆ ★ ☆ (genelde destekli)
- Onay: ✓ ✗ (genelde destekli)

### Desteklenmeyen (Otomatik temizlenir)
- Renkli emoji: 🟦 🎯 📊 💡 📋 🚀
- Yüz emojileri: 😀 😊 🎉
- Eşya emojileri: 📁 📄 ✏️
- Doğa: 🌳 🌟 ⭐
- vb. tüm `\U0001F300-\U0001F9FF` aralığı

> Detaylar için: `tasarim/04_emoji_kurallari.md`

---

## 🔍 Okunabilirlik İlkeleri

### Genç Okuyucu (12-13 yaş, 7. sınıf) için
- **Body metin minimum 10pt** olmalı
- **Leading 1.3-1.4 kat** olmalı
- **Çok uzun cümleler** kaçınılmalı (öğretmen rehberinde de)
- **Paragraflar 5-6 satırı geçmesin**
- **Beyaz alan bol bırak** (kenar boşlukları, paragraf araları)

### Öğretmen İçin
- **Body metin 10pt yeterli**
- **Leading 1.4 kat** ideal (uzun okuma)
- Detaylı tablolarda **9pt OK**
- Notlar **9pt italik** yeterli

### Çıktı Kalitesi
- 300 DPI baskı için **8pt'in altına inme**
- Tablolarda **8pt minimum** (çok küçük tablolar için)
- Her zaman **kontrast yeterli** olmalı (siyah-beyaz çıktıda da)

---

## 📊 Stil Karar Ağacı

Bir metin parçası için stil seçerken:

```
Bu metin ne?
│
├── Başlık mı? → Heading X (Bold + Renk)
│
├── Gövde metin mi? → Body (Regular)
│
├── Madde listesi mi? → Bullet (Regular + Indent)
│
├── Tablo içi mi? → 9pt Regular (Bold for header)
│
├── Yardımcı not mu? → Note (Italic + Muted)
│
├── Önemli vurgu mu? → Highlight (Bold + Secondary)
│
├── Kod / sabit içerik mi? → Mono
│
├── Form etiketi mi? → FormLabel (Bold + Standard)
│
└── Kapak başlığı mı? → CoverTitle (28pt Bold)
```

---

## 💻 Python Kullanım Örnekleri

### ParagraphStyle Tanımlama
```python
styles['Body'] = ParagraphStyle('Body',
    fontName='TR-Regular',     # Türkçe destekli
    fontSize=10,               # Boyut
    textColor=COLOR_TEXT,      # Renk
    alignment=TA_JUSTIFY,      # İki yana yaslı
    spaceAfter=6,              # Sonraki paragrafa boşluk
    leading=14                 # Satır aralığı
)
```

### Inline Stil Kullanımı
```python
text = '<b>Önemli:</b> <i>Bu bilgi kritiktir.</i>'
elements.append(Paragraph(text, styles['Body']))
```

### Stil İçinde Renk Değiştirme
```python
text = '<font color="#C2410C"><b>Vurgulu metin</b></font>'
elements.append(Paragraph(text, styles['Body']))
```

---

## 🎯 Kontrol Listesi

Yeni bir doküman üretirken:

- [ ] Tüm metinler **DejaVu Sans** (Türkçe karakter desteği) kullanıyor mu?
- [ ] Başlık-gövde **boyut hiyerarşisi** korunmuş mu?
- [ ] Leading **1.3-1.5 kat** mı?
- [ ] **Vurgu sayısı** her paragrafta en fazla 2 mi?
- [ ] Tablolarda **9pt Regular** veri, **9pt Bold** başlık mı?
- [ ] Üst-alt bantlar **8pt** mi?
- [ ] Kapak ana başlığı **28pt** mi?
- [ ] Hizalama **tutarlı** mı?
