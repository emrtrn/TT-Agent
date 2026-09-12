# 🗺️ Yol Haritası — 7 Adımlık Ünite Üretim Süreci

> Bir ünitenin tüm materyallerini üretirken **bu sıralamayı takip et**. Her adımın çıktısı bir sonraki adımın referansıdır.

> **Etkileşimli sunum kuralı:** Sunum taslağı ders planından hemen sonra başlatılır; bağlı kaynaklar üretildikçe geliştirilir ve entegrasyon testlerinden sonra nihai kabul edilir. Ayrıntılar: `workflow/04_etkilesimli_sunum_entegrasyonu.md`.

---

## ⏱️ Adım Süresi Tahmini

| Adım | Süre |
|:----:|:---:|
| 1. Ders Planı | ~15-20 dk |
| 2. Ön Değerlendirme | ~10-15 dk |
| 3. Sunum omurgası + entegrasyon + kavram kartları | ~30-40 dk |
| 4. Çalışma Kâğıtları | ~15-20 dk |
| 5. Değerlendirme Araçları | ~15-20 dk |
| 6. Farklılaştırma | ~20-25 dk |
| 7. Yansıtma + Kapanış | ~10-15 dk |
| **Toplam markdown** | **~2-2.5 saat** |
| PDF üretim | ~30-45 dk |

---

## 📋 ADIM 1 — Ayrıntılı Ünite Ders Planı

**Çıktı:** `Unite[N]_Ders_Plani.md` *(N = ünite numarası)*

**Öncelik:** Bu adım **ilk** yapılır çünkü diğer tüm materyaller bu plana referans verir.

### Yapılacaklar
1. `referans/8_sinif/00_resmi_kaynak.md` dosyasındaki canlı MEB bağlantısını aç; ilgili resmî ünite sayfasındaki ders saati, öğrenme çıktıları ve süreç bileşenlerini doğrula
2. `sablonlar/01_ders_plani.md` şablonunu izle
3. Ders saati başına şu yapıyı kur:
   - Köprü Kurma (5 dk)
   - Önceden bilineni hatırlatma (5 dk)
   - Ana etkinlik (20-25 dk)
   - Sentez/sunum (5-10 dk)
   - Kapanış + ödev (5 dk)
4. Programlar arası bileşenleri (KB, OB, SDB, D, E) her ders saatine **mutlaka** ekle
5. Ölçme-değerlendirme yöntemini her saat için belirt
6. Materyal listesi yap (sınıfta gerekli olanlar)

### Onay Sinyali
Kullanıcıya markdown'ı sun, "Ders planı uygun mu?" diye sor. Onay alınca Adım 2'ye geç.

---

## 📋 ADIM 2 — Ön Değerlendirme Aracı

**Çıktı:** `Unite[N]_On_Degerlendirme.md`

**Amaç:** Üniteye başlamadan önce öğrencinin mevcut bilgi düzeyini ölçmek.

### Yapılacaklar
1. `sablonlar/02_on_degerlendirme.md` şablonunu izle
2. **5 farklı araç** üret:
   - Araç 1: **Zihin Haritası** (kavram/zihin haritası, ünite anahtar kavramları)
   - Araç 2: **İki Aşamalı Tanılama Testi** (8 soru, doğru cevap + gerekçe)
   - Araç 3: **Açık Uçlu Sorular** (3-5 soru)
   - Araç 4: **Eşleştirme Testi** (kavram-tanım eşleşmesi)
   - Araç 5: **Boşluk Doldurma** (kısa cümleler)
3. Her aracın sonuna **öğretmen değerlendirme rehberi** ekle
4. Toplu değerlendirme formu ekle (sınıf bazında bilinirlik haritası)

### Önemli
- Zihin haritası kâğıdı **saklanır**, ünite sonunda öğrenciye iade edilir → öğrenci farklı renkte ekleme yapar (öğrenmenin somut kanıtı)

---

## 📋 ADIM 3 — Sunum Omurgası + Kavram Kartları

**Çıktılar:**
- `Unite[N]_Kavram_Kartlari.md`
- `Unite[N]_Sunum_Icerigi.md`
- `Unite[N]_Sunum_Entegrasyon_Haritasi.md`

### 3a. Sunum Entegrasyon Haritası ve İlk Sunum Taslağı
1. `workflow/04_etkilesimli_sunum_entegrasyonu.md` kurallarını uygula
2. Ders planındaki her ölçme, video, Pekiştir, Uygula ve Materyal geçişini entegrasyon haritasına yaz
3. `sablonlar/04_sunum_icerigi.md` ile ilk sunum taslağını hazırla
4. Henüz üretilmemiş kaynaklar için hayalî kimlik verme; `TASLAK` kullan

### 3b. Kavram Kartları ve Bağlı Kaynaklar
1. `sablonlar/03_kavram_kartlari.md` şablonunu izle
2. Ünitenin **her anahtar kavramı için 1 kart**:
   - Ön yüz: Kavram adı + emoji + slogan
   - Arka yüz: Tanım + günlük yaşam örneği + bağlantı + ayırt etme ipucu
3. Renk kodlaması yap (kavram gruplarına göre)
4. **6 farklı sınıf etkinliği** ekle (eşleştirme, kart oyunu, vb.)

### 3c. Sunumun Entegrasyonlu Nihai Sürümü
1. Sunum taslağını ve entegrasyon haritasını birlikte güncelle
2. **Ders saati başına 8-10 slayt**, toplam ~30-40 slayt
3. Her slayt için:
   - Başlık
   - İçerik (kısa, görsel ağırlıklı)
   - Görsel önerisi (öğretmen Canva/PowerPoint'e koyar)
   - **Konuşma notu (speaker notes)** — öğretmenin söyleyeceği şeyler
   - Öğrenme aşaması ve pedagojik amaç
   - Gerekli materyal ve gerçek kaynak kimliği
   - Açılma biçimi ve sunuma dönüş davranışı
4. Bölüm geçişleri için "ara slayt" ekle
5. Etkileşimli HTML sunumu ve portal kaynak kataloğuyla eşleşmeyi doğrula

### Önemli
Sunum içeriği **PDF'e çevrilmez**. Markdown, etkileşimli HTML sunumun içerik ve entegrasyon kaynağıdır. Kaynak bağlantıları ve `Sunuma dön` akışı doğrulanmadan sunum tamamlanmış sayılmaz.

---

## 📋 ADIM 4 — Öğrenci Çalışma Kâğıtları

**Çıktı:** `Unite[N]_Calisma_Kagitlari.md`

### Yapılacaklar
1. `sablonlar/05_calisma_kagitlari.md` şablonunu izle
2. Her ders saatinin etkinliği için ayrı çalışma kâğıdı:
   - Adı-Soyadı / Sınıf / No / Tarih alanları üstte
   - Yönerge kutusu (açık turuncu arka plan)
   - Süre bilgisi belirtilmiş
   - Ana içerik (tablo, soru, çizim alanı, vb.)
   - Yansıtma bölümü (öz değerlendirme)
   - Kontrol listesi (öğrencinin işini kontrol etmesi için)

### Özel Çalışma Kâğıtları İçin Notlar
- **Zihin haritası kâğıdı:** ASCII sanat YAPMA → PDF üretiminde özel `MindMapCanvas` kullanılacak
- **Venn diyagramı:** Aynı şekilde özel `VennDiagram` kullanılacak
- **Çizim alanı gerekirse:** Boş kare belirt (`DrawingBox`)

> **Bu özel çizimler `tasarim/03_ozel_cizimler.md` içinde anlatılmıştır.**

---

## 📋 ADIM 5 — Değerlendirme Araçları (Rubrikler)

**Çıktı:** `Unite[N]_Degerlendirme_Araclari.md`

### Yapılacaklar
1. `sablonlar/06_degerlendirme_araclari.md` şablonunu izle
2. **10 araç** üret:
   - Araç 1: Süreç Gözlem Formu (20 öğrencilik tablo!)
   - Araç 2-5: Ürün rubrikleri (her bir çalışma kâğıdı için)
   - Araç 6: Proje rubriği
   - Araç 7: Sunum rubriği
   - Araç 8: Akran değerlendirme formu
   - Araç 9: Ünite Sonu Sınavı (8 ÇS + 3 KC + 1 Performans = 100p)
   - Araç 10: Genel değerlendirme tablosu (ağırlıklı puanlama)

### Rubrik Yapısı (Her birinde)
- 4 düzey: Üstün / Yeterli / Gelişiyor / Yetersiz
- Her ölçüt için 4 puan ya da 1 puan
- Toplam puan ve düzey aralıkları belirtilmiş

### Önemli
- **Sınav** öğrenci kopyası VS cevap anahtarı **ayrı PDF'lerde** olacak (bu adımda markdown tek dosya, PDF aşamasında ayrılır)

---

## 📋 ADIM 6 — Farklılaştırma Materyalleri

**Çıktılar:**
- `Unite[N]_Zenginlestirme_Paketi.md`
- `Unite[N]_Destekleme_Paketi.md`

### 6a. Zenginleştirme (İleri düzey öğrenciler için)
1. `sablonlar/07_zenginlestirme.md` şablonunu izle
2. **5-7 etkinlik** üret:
   - Senaryo yazma / yaratıcı yazma
   - Araştırma projesi
   - Kavram ilişki ağı / harita
   - Eleştirel düşünme alıştırması (çelişki analizi)
   - Sunum görevi (TED-style)
   - Tasarım projesi
   - Tarihsel/karşılaştırmalı çalışma

### 6b. Destekleme (Ek desteğe ihtiyacı olanlar için)
1. `sablonlar/08_destekleme.md` şablonunu izle
2. **6-8 materyal** üret:
   - Görsel kavram sözlüğü
   - Adım adım tanım şablonu (doldur-bul)
   - Eşleştirme oyun kartları
   - Basitleştirilmiş 5N1K şablonu
   - Kontrollü bilgi toplama formu
   - Örnek cevaplı çalışma kâğıdı
   - Akran mentörlüğü rehberi
   - "Öğrendim!" kontrol kartları (ders sonu)

### Önemli İlke
**Onur koruyucu uygulama:** Destekleme materyalleri "özel" olarak sunulmamalı; tüm öğrencilere açık bir kaynak havuzunun parçası gibi tanıtılmalı.

---

## 📋 ADIM 7 — Öğretmen Yansıtma + Ünite Kapanış

**Çıktı:** `Unite[N]_Ogretmen_Yansitma_ve_Kapanis.md`

### Yapılacaklar
1. `sablonlar/09_yansitma_kapanis.md` şablonunu izle
2. **5 araç** üret:
   - Araç 1: Öğretmen Yansıtma Günlüğü (her ders bazında + genel)
   - Araç 2: Öğrenci Dönüt Anketi (anonim, 5 bölüm)
   - Araç 3: Zümre Paylaşım Şablonu
   - Araç 4: Ünite Özet Tablosu (referans çizelge)
   - Araç 5: Sonraki Üniteye Geçiş Notları

### Çapraz Bağ
- **Bir Sonraki Üniteye Geçiş Notları**'nda bir sonraki ünitenin (varsa) anahtar kavramlarını ve hazırlık ödevini belirt
- Bu, üniteler arası kesintisiz akış için kritik

---

## 🎯 Tüm Adımlar Tamamlandığında

### Markdown Dosyaları (~9-10 adet)
```
Unite[N]_Ders_Plani.md
Unite[N]_On_Degerlendirme.md
Unite[N]_Kavram_Kartlari.md
Unite[N]_Sunum_Icerigi.md
Unite[N]_Sunum_Entegrasyon_Haritasi.md
Unite[N]_Calisma_Kagitlari.md
Unite[N]_Degerlendirme_Araclari.md
Unite[N]_Zenginlestirme_Paketi.md
Unite[N]_Destekleme_Paketi.md
Unite[N]_Ogretmen_Yansitma_ve_Kapanis.md
Unite[N]_Genel_Ozet.md (opsiyonel referans dosyası)
```

### Bonus: Genel Özet
Tüm dosyaların referans haritasını içeren bir genel özet dosyası da üretilebilir.
İçinde: tüm dosyalar listesi, ders saati bazlı zaman akışı, kazanım-materyal eşleşmesi.

---

## 🖨️ ADIM 8 (BONUS) — PDF Üretimi

Markdown'lar onaylandıktan sonra:

1. `pdf_uretim/README.md` dosyasını oku
2. Her markdown dosyasını mantıksal alt PDF'lere böl:
   - Bazıları 1:1 (ör. ders planı → 1 PDF)
   - Bazıları 1:N (ör. çalışma kâğıtları → 8 PDF, her biri ayrı)
3. **Sunum içeriği PDF'e çevrilmez!**
4. Kullanıcı tercih etmedikçe ~38 PDF üretilir
5. PDF'leri 7 grup halinde teslim et

> Detaylar: `pdf_uretim/README.md`

---

## 🔄 Akış Kontrolü

### Tek bir adıma odaklanıldığında
Kullanıcı "Çalışma kâğıtlarını hazırla" gibi tek bir adım istemişse:
- Sadece o adımı yap
- Önceki/sonraki adımlara değinme
- Yine de Adım 1'in (ders planı) varlığını kontrol et — yoksa "önce ders planına ihtiyaç var" de

### Birden fazla ünite üretilirse
Her ünite için **ayrı klasör** kullan:
```
materials/unite-1/...
materials/unite-2/...
```
Materyaller arası çapraz referansları **koru** (özellikle "Sonraki Üniteye Geçiş Notları")

---

## ✅ Her Adım Sonunda Kontrol Listesi

- [ ] Markdown sözdizimi doğru mu?
- [ ] Türkçe yazım hataları var mı?
- [ ] Programlar arası bileşenler eklendi mi?
- [ ] Süre hesabı tutarlı mı? (her etkinlik toplamı = ders saati)
- [ ] Şablondaki tüm bölümler dolduruldu mu?
- [ ] Kullanıcı tercihleri uygulandı mı? (40 dk, 20 öğrenci, vb.)
- [ ] Çapraz referanslar (diğer materyallere atıflar) doğru mu?
