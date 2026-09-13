# ⚙️ Kullanıcı Tercihleri — Tüm Ayarlar Tek Yerde

> Bu dosya **tek doğruluk kaynağı**dır. Bir tercih hakkında kararsız kalırsan buraya bak. Yeni bir tercih kaydedildikçe **bu dosyayı güncelle**.

---

## 🎓 Sınıf ve Ders Yapısı

| Tercih | Değer |
|--------|-------|
| Sınıf | 7 veya 8 (her üretimde seçilir) |
| Ders adı | Teknoloji ve Tasarım |
| Bir ders saati | **40 dakika** (45 değil!) |
| Haftalık ders | 2 ders saati, arada 10 dakika ara ile peş peşe |
| Ders saati × hafta hesabı | 4 saat → 2 hafta, 6 saat → 3 hafta, 8 saat → 4 hafta, 10 saat → 5 hafta |
| Sınıf yapısı | İkiye bölünür (mevcut 25'i geçtiğinde) |
| Sınıf mevcudu (form/tablo için) | **20 öğrenci** |
| Atölye düzeni | 2 grup, sırayla rotasyon (atölye + sınıf) |
| Öğretmen sayısı | 2 (kullanıcı + zümre arkadaşı) |

## 🎨 PDF Tasarım Tercihleri

### Renk Paleti (Koyu Turuncu Tema)
| Rol | Hex | Açıklama |
|-----|-----|----------|
| Ana renk | `#C2410C` | Başlıklar, vurgu metinler |
| İkincil | `#9A3412` | Daha koyu, kuvvetli vurgu |
| Aksan | `#EA580C` | Alt başlıklar, dekoratif çizgiler |
| Açık ton | `#FED7AA` | Kutu arka planları, info alanları |
| Çok açık | `#FFF7ED` | Kapak ve büyük info kutu arka planı |
| Metin | `#1F2937` | Ana metin (siyah yerine) |
| Yardımcı metin | `#6B7280` | Alt notlar, italikler |
| Açık gri | `#E5E7EB` | Çerçeveler, ayırıcılar |
| Çok açık gri | `#F9FAFB` | Tablolarda alternatif satır |
| **Yazı çizgisi** | `#D1D5DB` | **Öğrenci yazı alanı çizgileri (çıktıda silik)** |

### Font
- **Aile:** DejaVu Sans (Türkçe karakter desteği için zorunlu)
- **Yol:** `/usr/share/fonts/truetype/dejavu/`
- **Varyantlar:** Regular, Bold, Italic, BoldItalic, Mono

### Boyutlar
| Element | Boyut |
|---------|-------|
| Sayfa | A4 |
| Kenar boşluğu (yan) | 2 cm |
| Kenar boşluğu (üst-alt) | 1.8 cm |
| Ana başlık (Title) | 22 pt |
| Heading 1 | 16 pt |
| Heading 2 | 13 pt |
| Heading 3 | 11 pt |
| Gövde metni | 10 pt |
| Tablo metni | 9 pt |
| Not/italik | 9 pt |
| Üst-alt bant | 8 pt |
| Kapak ana başlık | 28 pt |
| Kapak alt başlık | 16 pt |

### Sayfa Düzeni
- **Üst bant:** İnce turuncu çizgi + sol: "Teknoloji ve Tasarım • [Sınıf]. Sınıf • [Ünite]" + sağ: doküman başlığı
- **Alt bant:** Açık gri çizgi + sol: "Türkiye Yüzyılı Maarif Modeli" (italik) + sağ: "Sayfa N"

### Kapak Sayfası Kuralları
- **4+ sayfa olan dokümanlarda** otomatik ekle
- **3 ve daha az sayfalık** dokümanlarda ekleme (kâğıt tasarrufu)
- Üst etiket: ÖĞRETMEN REHBERİ / ÖĞRENCİ MATERYALİ / DESTEKLEME MATERYALİ / İLERİ DÜZEY ÖĞRENCİ MATERYALİ vb.
- Meta bilgilerde **"Uygulama Dönemi" alanını ekleme** (kullanıcı yıllarca kullanacak)
- Alt bilgi sırası:
  1. Türkiye Yüzyılı Maarif Modeli
  2. Teknoloji ve Tasarım Dersi
  3. [Sınıf]. Sınıf Öğretim Programı
  > **NOT:** "2025" tarih damgası asla yok!

## 🖨️ PDF Üretim Tercihleri

### Markdown → PDF Dönüşüm Kuralları
- Tüm başlıklar (`#`, `##`, `###`) koyu turuncu olmalı
- Tablolar: koyu turuncu başlık satırı, alternatif satır arka planları
- Madde listeleri: `•` ile başlamalı (`-` yerine)
- `> ` ile başlayan blockquotelar italik, gri renkli not olmalı
- `<br>` etiketleri tablo hücrelerinde `<br/>` olarak self-closing yapılmalı

### Emoji Kuralları
**❌ PDF'te ASLA göstermeme** (DejaVu desteklemiyor):
- 🟦 🟥 🟧 🟨 🟩 🟪 🟫 (renkli kareler)
- 📊 📈 📉 📋 📌 📎 📁 📂 📄 📑 (ofis nesneleri)
- 💡 💭 🎯 🚀 🎨 🔍 🌟 ⭐ (dekoratif)
- ✨ 🔥 💪 🤝 🎓 (motivasyonel)
- 🤖 🌐 🤳 (teknoloji)
- Diğer Unicode emoji aralığı (U+1F300-U+1F9FF)

**✅ Kullanılabilir** (DejaVu destekler):
- ● ○ ■ □ ◆ ★ ☆ (geometrik)
- → ← ↑ ↓ ↔ (oklar)
- ✓ ✗ (onay/iptal — ama yine de kontrol et)
- §, ¶, ©, ® (özel karakterler)

> Detaylar: `tasarim/04_emoji_kurallari.md`

### Özel Çizimler
Markdown'da ASCII sanat YERİNE özel flowable kullan:
- **Zihin haritası** → `MindMapCanvas` (merkez kelime + 8 dal)
- **Venn diyagramı** → `VennDiagram` (iki örtüşen daire)
- **Çizim alanı** → `DrawingBox` (boş kare, isteğe bağlı caption)
- **Yazı çizgileri** → `WritingLines` (öğrenci uzun cevap için)

> Detaylar: `tasarim/03_ozel_cizimler.md`

## 📑 Doküman Bölme Tercihleri

Bir markdown dosyası birden fazla PDF'e bölünebilir. Kurallar:

### Otomatik Ayrılması Gerekenler
| Markdown İçeriği | PDF Sayısı | Neden? |
|------------------|:---:|---------|
| Tüm öğrenci çalışma kâğıtları | 8 (her biri ayrı) | Öğretmen tek tek dağıtır |
| Sınav (öğrenci kopyası + cevap anahtarı) | 2 (kesinlikle ayrı) | Öğrenci asla cevap anahtarını görmemeli |
| Ön değerlendirme paketi | 3 (öğretmen rehberi + 2 öğrenci formu) | Cevap anahtarını öğrenciye verme |
| Yansıtma + kapanış paketi | 5 (her araç ayrı) | Her birinin kullanım anı farklı |

### Birleştirilebilir Olanlar
- Çoklu rubrikler (4-5 rubrik bir PDF'te) — ama her birinin başında ayrı bölüm
- Zenginleştirme etkinlikleri (2-3 etkinlik tek PDF'te grup halinde)

### Referans Doküman Standardı

- Öğretmen hazırlık materyali, ders planı, ön değerlendirme, bireysel çalışma kâğıtları, grup çalışma kâğıtları, öz değerlendirme, ünite sonu değerlendirme, destekleme ve zenginleştirme ayrı doküman türleri olarak ele alınır.
- Kavram kartları ile 5N1K kavram tablosu gibi üniteye özgü araçlar, hedef kitlesi, kullanım zamanı veya fiziksel dağıtım biçimi farklıysa ayrı Markdown belgesi olur.
- Aynı hedef kitleye aynı ders anında dağıtılan birden fazla kısa görev, ilgili bireysel ya da grup çalışma kâğıdı paketinde sayfa/bölüm olarak tutulabilir.

## 🎯 İçerik Üretim Tercihleri

### Yazım Tarzı
- **Türkçe** zorunlu
- **Akıcı, samimi, profesyonel** ton
- **2. tekil şahıs** öğrenci materyallerinde ("yazıyorsun", "düşünüyorsun")
- **3. çoğul şahıs** öğretmen rehberlerinde ("öğretmenler", "uygulayıcılar")

### Pedagojik Yaklaşım
- **Beceri temelli öğrenme** vurgulu (Maarif Modeli)
- **Etkinlik temelli ders** (öğrenci aktif)
- **Programlar arası bileşen entegrasyonu** (her etkinlikte KB/OB/SDB/D/E kodu)
- **Ölçme-değerlendirme süreklisi:**
  - %20 Süreç gözlem
  - %25 Ürün rubrikleri
  - %10 Akran değerlendirme
  - %10 Öz değerlendirme
  - %20 Ünite sonu sınavı
  - %15 Sunum/proje

### Uzunluk ve Ayrıntı
- Ders planı: 8-10 sayfa
- Çalışma kâğıdı: 1-3 sayfa (her biri)
- Rubrik: 1-2 sayfa
- Sunum slaytı: 30-40 slayt (4 ders × ~9 slayt)

## 🚫 Asla Yapma Listesi

1. **45 dakika** yazma → her zaman 40 dakika
2. **30 öğrencilik** form çıkarma → 20 yeter
3. **"2025"** tarih damgası → "[Sınıf]. Sınıf Öğretim Programı"
4. **"Uygulama Dönemi: 2025-2026"** → asla
5. **Cevap anahtarını** öğrenci sınavıyla aynı PDF'e koyma
6. **Dekoratif emoji** PDF içeriklerinde
7. **ASCII sanat** çalışma kâğıtlarında — özel flowable kullan
8. **Çok uzun başlık emojisi** — başlıkta 1 emoji yeterli, hatta yok
9. **Düz markdown** PDF üret demek — her zaman alt PDF'lere bölme stratejisi düşün

## ✅ Her Zaman Yap Listesi

1. Önce **markdown** üret, kullanıcı onayını al, sonra PDF
2. Her materyalin başında **kullanıcı tercihlerini** kontrol et
3. **Programlar arası bileşenleri** her etkinliğe ekle
4. Çapraz referansları **koru** (ders planı → çalışma kâğıdı X gibi)
5. Adımları **sırayla** uygula (1 → 2 → 3 → ...)
6. Kullanıcı bir tercih bildirirse **bu dosyaya kaydet**

## 🔄 Tercih Güncelleme Logu

| Tarih | Tercih | Eklendi/Değişti | Bağlam |
|-------|--------|----------------|---------|
| Ünite 1 | Ders 40 dk | İlk eklendi | Kullanıcı belirtti |
| Ünite 1 | Sınıf 20 öğrenci | İlk eklendi | T.T. dersi sınıf bölünmesi |
| Ünite 1 | "Uygulama Dönemi" yok | İlk eklendi | Yıllarca kullanım için |
| Ünite 1 | "2025" tarihi yok | İlk eklendi | Aynı sebep |
| Ünite 1 | Koyu turuncu (#C2410C) | İlk seçildi | Kullanıcı tercihi |
| Ünite 1 | Hafif gri yazı çizgileri | İlk seçildi | Çıktıda silik istenmesi |
| Ünite 1 | Kapak 4+ sayfada | İlk eklendi | Kâğıt tasarrufu |
| Ünite 1 | Haftada 2 ders peş peşe | İlk eklendi | Atölye + sınıf rotasyonu |
| Ünite 1 | İki ders arasında 10 dk ara | Eklendi | Aynı haftadaki iki ders bir bloktur; ara ödev verilmez, sonraki haftanın ödevi ikinci ders sonunda verilir |

---

> **Bu dosya canlıdır.** Her yeni tercih, her revizyon buraya kaydedilmeli.
