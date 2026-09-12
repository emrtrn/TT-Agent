# 💡 Edinilmiş İpuçları ve Öneriler

> 1. ünitenin üretiminde edinilen pratik ipuçları. Yeni öğrenilenler buraya eklenmeli.

---

## ✍️ Markdown İçerik Üretimi

### Tablolar
- **`<br>` etiketi** tablo hücrelerinde sorun çıkarır → ya hiç kullanma ya da PDF üretimi `<br/>` self-closing olarak düzeltir
- **Çok geniş tablolar** (7+ sütun) PDF'te küçük yazılır → 5-6 sütun ideali
- Tablo başlıklarında `<br/>` ile **iki satıra bölme** mantıklı (uzun başlık varsa)

### Liste Formatı
- `*` yerine `-` kullan (markdown standart)
- Numaralı listeler için `1.`, `2.` (boşluksuz `1)` değil)
- İç içe liste için 4 boşluk girinti (sekme değil)

### Vurgu
- **Kalın metin** için `**...**`
- *İtalik* için `*...*`
- ~~Üstü çizili~~ için `~~...~~`
- `Kod` için backtick

### Başlıklar
- `#` Title — sadece dosya başı (1 kez)
- `##` Heading 1 — ana bölümler
- `###` Heading 2 — alt bölümler
- `####` Heading 3 — detay bölümleri
- Başlıklarda **emoji kullanmama** stratejisi PDF'te daha temiz çıktı verir

### Yönerge Kutuları
Markdown'da `> ` ile blockquote yazınca PDF'te italic gri not olur. Eğer **vurgulu yönerge** istersen şu yapıyı kullan:

```markdown
> **Yönerge:** Aşağıdaki soruları cevapla. Süre: 15 dakika.
```

PDF üretimi bunu **açık turuncu kutu** olarak render eder.

---

## 🎨 PDF Üretiminde Edinilen İpuçları

### Sayfa Sayısı Tahmini
- **Yaklaşık 2500 karakter / sayfa** (kuralcı bir tahmin)
- Tablolar daha çok yer kaplar
- Çalışma alanları (yazı çizgileri) daha çok yer kaplar
- 4 sayfanın altıysa kapak ekleme

### Türkçe Karakter Sorunları
1. **DejaVu Sans yüklü olmalı:** `apt install fonts-dejavu`
2. **Font kaydı:** `register_fonts()` fonksiyonu çalıştırılmalı
3. **Fontu paragrafstilinde belirt:** `fontName='TR-Regular'` (DejaVu için kayıt edilen ad)

### Emoji Sorunu Çözümü
DejaVu Sans birçok emojiyi desteklemiyor → kutucuk çıkıyor. Çözüm:

```python
# md_converter.py'da clean_emojis() fonksiyonu var
UNSUPPORTED_EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002600-\U000026FF"
    "\U00002700-\U000027BF"
    "\U0001F000-\U0001F2FF"
    "]+",
    flags=re.UNICODE
)
```

Bu fonksiyon **otomatik** çalışır — markdown'da emoji bırakabilirsin (ama az kullanmak daha temiz).

### Tablo Hücrelerinde Paragraph
- Tablo hücrelerine düz metin koyarsan formatlamaz
- **Çözüm:** Her hücreyi `Paragraph` olarak yarat
- Başlık satırı için `TR-Bold`, beyaz renk
- Veri satırları için `TR-Regular`, koyu gri

### Özel Çizimler (Flowables)

#### MindMapCanvas (Zihin Haritası)
- Merkez kelime turuncu kutuda
- Etrafta 8 dal, her birinin ucunda yazı çizgisi
- Öğrenci dalın üzerine yazıyor
- **Yükseklik:** 8.5-9 cm ideal

#### VennDiagram (Venn)
- İki örtüşen daire, yarı saydam dolgu
- "Ürün 1'e Özgü", "ORTAK", "Ürün 2'ye Özgü" etiketleri
- **Yükseklik:** 7.5-8 cm ideal

#### WritingLines (Yazı Çizgileri)
- `num_lines` ile satır sayısı
- `line_spacing=20` standart aralık
- Renk: Çok hafif gri (#D1D5DB), çıktıda silik

#### DrawingBox (Çizim Alanı)
- Boş kare, isteğe bağlı caption (italik)
- Caption örnek: "Buraya çizim yapınız" gibi

---

## 🔧 PDF Üretim Stratejisi

### Üretim Grupları
38 PDF'i 7 grupta üret (her grupta 5-7 PDF):

| Grup | İçerik | PDF Sayısı |
|:----:|--------|:---:|
| 1 | Öğretmen referans | 2 |
| 2 | Ön değerlendirme | 3 |
| 3 | Kavram kartları | 2 |
| 4 | Çalışma kâğıtları | 8 |
| 5 | Değerlendirme araçları | 7 |
| 6 | Farklılaştırma | 11 |
| 7 | Yansıtma ve kapanış | 5 |

Her grubun sonunda `present_files` ile teslimat yap, kullanıcı kontrol etsin.

### Sayfa Numarası ve Üst-Alt Bantlar
- Üretim scriptine `onFirstPage=add_page_number` ve `onLaterPages=add_page_number` parametrelerini geç
- Bu fonksiyon `pdf_style.py`'da hazır

### Özel Üretim Gereken PDF'ler
Aşağıdakiler markdown→PDF dönüştürücüden geçmez, **özel kod** gerektirir:

| PDF | Neden? | Çözüm |
|-----|--------|-------|
| Zihin Haritası kâğıdı | ASCII sanat işlemez | `MindMapCanvas` |
| Venn Diyagramı kâğıdı | ASCII sanat işlemez | `VennDiagram` |
| Süreç Gözlem Formu | 20 satırlık tablo, sembolizm sorunu | Özel Table |
| Sınav cevap anahtarı | İçerik markdown'da yok, ayrı yazılmalı | Özel markdown |

---

## 🎯 Pedagojik İpuçları

### Programlar Arası Bileşen Kullanımı
Her ders saatinde **mutlaka** bir bileşen vurgula:
- **KB (Kavramsal Beceriler):** KB2.4 Çözümleme, KB2.7 Karşılaştırma, KB2.8 Sorgulama, KB2.17 Değerlendirme
- **OB (Okuryazarlık):** OB4.1 Bilgi okuryazarlığı, OB4.2 Görsel yorumlama, OB7.2 Veri oluşturma
- **SDB (Sosyal-Duygusal):** SDB2.1 İletişim, SDB2.2 İş birliği, SDB2.3 Sosyal farkındalık, SDB3.3 Sorumlu karar verme
- **D (Değerler):** D3 Çalışkanlık, D5 Duyarlılık, D7 Estetik, D14 Saygı
- **E (Eğilimler):** E1.1 Merak, E3.2 Odaklanma, E3.4 Gerçeği arama

### Etkinlik Tasarım Prensipleri
- **Köprü kurma** (5 dk) — günlük yaşamla bağlantı
- **Hatırlatma** (5 dk) — önceki dersin kavramları
- **Ana etkinlik** (20-25 dk) — beceri uygulaması
- **Sentez/Sunum** (5-10 dk) — öğrencilerin paylaşımı
- **Kapanış + Ödev** (5 dk) — bir sonraki derse hazırlık

### Değerlendirme Stratejisi
Ağırlık dağılımı (önemli!):
- %20 Süreç gözlem
- %25 Ürün rubrikleri
- %10 Akran değerlendirme
- %10 Öz değerlendirme
- %20 Ünite sonu sınavı
- %15 Sunum/proje

---

## 🚧 Sık Karşılaşılan Hatalar

### Hata: "ParagraphStyle parser error: br"
**Sebep:** Markdown tablosunda `<br>` var, reportlab self-closing istiyor  
**Çözüm:** `cell.replace('<br>', '<br/>')` (md_converter.py'da var)

### Hata: Türkçe karakterler kutucuk
**Sebep:** Font kayıt edilmedi  
**Çözüm:** Script başında `from pdf_style import *` (otomatik kaydolur)

### Hata: "Boş kutu" başlıklarda
**Sebep:** Markdown'da emoji var ama font desteklemiyor  
**Çözüm:** `clean_emojis()` fonksiyonu var, otomatik çalışıyor

### Hata: Tablo başlığı çok dar
**Sebep:** Sütun genişlikleri yetersiz  
**Çözüm:** `colWidths` parametresine cm cinsinden genişlik ver

### Hata: Sayfa numarası eksik
**Sebep:** `doc.build()` çağrısında `onFirstPage` ve `onLaterPages` verilmemiş  
**Çözüm:** Her zaman bu parametreleri ekle

---

## 💬 Kullanıcı İletişimi İpuçları

### Onay Stratejisi
- Her **adım sonunda** kullanıcıya onay sor
- "Bu adım tamamlandı, devam edeyim mi?" 
- Onay alınmadan sonraki adıma geçme

### PDF Sunumu
- PDF'leri **gruplar halinde** sun (5-7 PDF / mesaj)
- Her grupta `present_files` aracını kullan
- Grup sonunda kısa özet ver (PDF sayısı, sayfa toplamı, dikkat edilmesi gerekenler)

### Revizyon İstekleri
Kullanıcı bir PDF için revizyon isterse:
1. Önce ilgili **markdown** dosyasını revize et
2. Sonra PDF'i tekrar üret
3. Sadece o PDF'i tekrar sun
4. Eğer revizyon **tüm dokümanları etkiliyorsa** (örn. renk değişimi):
   - `pdf_style.py`'da değişiklik yap
   - Tüm üretim scriptlerini tekrar çalıştır

### Tool Limit Uyarısı
Eğer üretim sırasında tool limit yaklaşırsa:
1. Mevcut grupları tamamla
2. Kullanıcıya durum bildir
3. Bir sonraki mesajla devam edileceğini söyle
4. Üretilenleri **özet** olarak listele

---

## 🌱 Sürekli Gelişim Notları

### Bu paket geliştirildikçe...
- Yeni şablonlar ekle (her ünite kendi özelliğini eklemiş olabilir)
- Yeni özel flowables ekle (3D modelleme için, devre şeması için, vb.)
- Hata logu tut (hangi hata, nasıl çözüldü)

### Geri bildirim
Kullanıcıdan gelen revizyon istekleri **kalıcı** mı değişiyor mu kontrol et:
- Tek seferlik ise sadece o dokümanı revize et
- Kalıcı bir tercih değişikliği ise → `01_kullanici_tercihleri.md`'ye kaydet
