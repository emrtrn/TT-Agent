# 📋 Şablon: Sunum Slaytları İçeriği

> Bu şablon **`Unite[N]_Sunum_Icerigi.md`** dosyasının yapısını gösterir.  
> Sunum, `Öğren → Pekiştir → Uygula → Materyaller` akışını yöneten etkileşimli ders omurgasıdır.  
> Ortak entegrasyon kuralları için `workflow/04_etkilesimli_sunum_entegrasyonu.md` okunur.

---

## 📐 Genel Yapı

```markdown
# [N]. Ünite: Sunum Slaytları İçeriği
## [Ünite Adı] — [X] Ders Saati İçin Hazır Slayt Akışı

> Bu dosya, etkileşimli HTML sunumun içerik ve entegrasyon kaynağı olarak hazırlanmıştır; gerektiğinde PowerPoint / Google Slides / Canva için de kullanılabilir.  
> Her slayt için: **başlık, içerik, görsel önerisi, konuşma notu (speaker notes)** verilmiştir.  
> Toplam slayt sayısı: **~[N]** ([X] ders saatine bölünmüş).

**Sürüm durumu:** İlk taslak / Entegrasyon bekliyor / Nihai  
**Entegrasyon haritası:** `Unite[N]_Sunum_Entegrasyon_Haritasi.md`

---

## TASARIM ÖNERİLERİ

**Renk Paleti:**
- Ana renk: Koyu turuncu (#C2410C)
- Vurgu: Mavi (#1E3A8A) veya yeşil (#15803D)
- Arka plan: Beyaz / Çok açık gri (#F8FAFC)
- Başlık yazısı: Koyu turuncu • Gövde yazısı: Siyah

**Yazı Tipleri:**
- Başlıklar: **Poppins Bold** / Montserrat Bold / Impact
- Gövde metin: Open Sans / Roboto / Calibri

**Slayt Boyutu:** 16:9 widescreen

**Ortak Bileşenler:**
- Her slaytın altında küçük logo alanı + slayt numarası
- Sayfa başlığı: Üniteyi tanımlayan kısa bir banner
- Bölüm geçişlerinde "Ara Slayt" koy (görsel + büyük puntolu başlık)

---

## BÖLÜM 1: GİRİŞ (Slayt 1-3)

### SLAYT 1 — Başlık Slaytı

**Başlık:** [N]. ÜNİTE  
**Alt Başlık:** [ÜNİTE ADI]  
**Altında:** [Sınıf]. Sınıf • Teknoloji ve Tasarım Dersi

**Görsel Önerisi:**
- [Görsel önerisi açıklaması]

**Konuşma Notu:**
> "[Öğretmenin söyleyeceği sözler — sahne girişi]"

---

### SLAYT 2 — Ünite Amacı

**Başlık:** Bu Ünitenin Sonunda Neler Öğreneceksiniz?

**İçerik:**
- ✅ [Kazanım 1 öğrenci diliyle]
- ✅ [Kazanım 2 öğrenci diliyle]
- ✅ [Kazanım 3 öğrenci diliyle]
- ✅ [Kazanım 4 öğrenci diliyle]

**Görsel Önerisi:**
- [Açıklama]

**Konuşma Notu:**
> "[Açıklama metni]"

---

### SLAYT 3 — Ünitenin Yol Haritası

**Başlık:** [X] Haftada Bizi Neler Bekliyor?

**İçerik:** (Bir zaman çizelgesi üzerinde)

| Hafta | Konu | Anahtar Etkinlik |
|:---:|------|-----------------|
| 1 | [Konu] | [Etkinlik] |
| 2 | [Konu] | [Etkinlik] |
| ... | ... | ... |

**Görsel Önerisi:** Yatay bir yol (road) grafiği, her hafta bir durak olarak işaretlenmiş.

**Konuşma Notu:**
> "[Açıklama]"

---

## BÖLÜM 2: 1. DERS SAATİ — [BÖLÜM ADI] (Slayt 4-N)

[Her ders saati için ~8-10 slayt]

### SLAYT [N] — [Slayt başlığı]

**Öğrenme çıktısı:** [TT.8.N.X]  
**Öğrenme aşaması:** [Öğren / Pekiştir / Uygula / Materyaller]  
**Pedagojik amaç:** [Bu slaydın veya geçişin neden burada olduğu]  
**Gerekli materyal:** [Belge adı veya Yok]  
**İlgili kaynaklar:** [Gerçek kaynak kimlikleri veya TASLAK — katalog kaydında belirlenecek]  
**Kaynak türü:** [Kısa video / Etkileşim / Quiz / Uygulama / Belge / Yok]  
**Açılma biçimi:** [Portal içi görüntüleyici / Öğretmenin önceden hazırlaması / Slaytta kal]  
**Dönüş davranışı:** [Sunuma dön / Slaytta kal]

**Başlık:** [Başlık]

**İçerik:**
> [Slayt içeriği — kısa, görsel ağırlıklı]

**Görsel Önerisi:** [Açıklama]

**Konuşma Notu:**
> "[Öğretmenin sahnede söyleyeceği]"

---

[Tüm slaytlar için aynı yapı]

---

## SLAYT GELİŞTİRME İPUÇLARI

### Üretim için:
1. Canlı MEB ünitesi, öğretmen hazırlığı ve ders planıyla slayt omurgasını oluşturun.
2. Üniteye özel entegrasyon haritasına her ölçme, video, Pekiştir, Uygula ve Materyal geçişini yazın.
3. Kaynak henüz üretilmediyse hayalî bağlantı vermeyin; `TASLAK` olarak işaretleyin.
4. Kaynak kataloğu oluşturulduktan sonra kesin kimlikleri Markdown ve entegrasyon haritasına birlikte işleyin.
5. Etkileşimli HTML sunumu üretip açılış ve sunuma dönüş davranışlarını test edin.

### Etkileşim için:
- Kısa videoyu ilgili kavram slaydına bağlayın; uzun videoyu ayrı Öğren kaynağı olarak tutun.
- Kavram kartı, eşleştirme, sınıflandırma ve mini quizleri ilgili anlatımdan hemen sonra konumlandırın.
- Uygula içeriğini gerekli yönerge ve ön bilgi tamamlandıktan sonra açın.
- Ön değerlendirme ve çalışma kâğıtlarının kullanım anını slaytta açıkça belirtin.
- Kaynaktan çıkışta `Sunuma dön` akışını koruyun.

### Sunum Öncesi Kontrol:
- [ ] Fontlar herkesin cihazında çalışıyor mu?
- [ ] Görseller yüksek çözünürlüklü mü?
- [ ] Renkler akıllı tahtada net görünüyor mu?
- [ ] Metin miktarı fazla mı? (Her slayt **en fazla 5-6 madde**)
- [ ] Animasyonlar dikkat dağıtıcı mı?
- [ ] Slayda bağlı kaynak kimlikleri katalogdaki gerçek kayıtlarla eşleşiyor mu?
- [ ] İlgili içerik doğru slaytta açılıyor mu?
- [ ] Kaynak kapatıldığında sunuma dönülüyor mu?
- [ ] Slayt değiştiğinde açık ilgili-içerik menüsü kapanıyor mu?
```

---

## ✅ Üretim Sırasında Dikkat Edilecekler

### İki Aşamalı Üretim

- **İlk taslak:** Ders planının hemen ardından hazırlanır; slayt sırası ve ihtiyaç duyulan kaynaklar belirlenir.
- **Nihai sürüm:** Bağlı kaynaklar üretildikten, gerçek kimlikleri kaydedildikten ve dönüş akışı doğrulandıktan sonra tamamlanır.

### Slayt Sayısı Hesabı
- **Her ders saati için ~8-10 slayt**
- Giriş bölümü 3 slayt + Kapanış 2 slayt
- Toplam: **(ders saati × 8-10) + 5**

| Ders saati | Toplam slayt (yaklaşık) |
|:----:|:---:|
| 4 | ~38 |
| 6 | ~55 |
| 8 | ~75 |

### Slayt Başına İçerik
- **Maksimum 5-6 madde** (öğrenci okumakta zorlanmasın)
- Her slayt **bir ana fikir** içermeli
- Görsel ağırlıklı olmalı (metin destekleyici)

### Konuşma Notu (Speaker Notes)
**ÇOK ÖNEMLİ:** Konuşma notu **kelimesi kelimesine söylenecek metin değil**, öğretmenin **sahnede söyleyeceği** ana fikir/anekdot/soru olmalı.

✅ İyi konuşma notu örneği:
> "Burada öğrencilere 'Cep telefonunuzu çıkarın' deyin — biraz ürkecekler. 'İzin veriyorum' deyin gülsünler. Sonra 'Bu cihazda kaç tane buluş var?' diye sorun. Cevap beklemeyin, merak uyandırın."

❌ Kötü konuşma notu örneği:
> "Buluş, yeni bir fikir bulmaktır. Örneğin..."

### Bölüm Geçişleri
Her ders saatinin başında **ara slayt** koyun:
- Sadece büyük başlık + simge
- Öğrencinin "yeni bölüm" olduğunu hissetmesi için

### Ünite Sonu Kapanış
- Son 2 slayt **özet ve teşekkür** olmalı
- "Bir sonraki ünitede..." diye **bir köprü** kur
- Kapanış slaytı **görsel olarak güçlü** olsun

---

## ⚠️ Önemli: Bu Dosya PDF'e Çevrilmez

Sunum içeriği **PDF üretim sürecine dahil edilmez**. Çünkü:
- Kaynak Markdown, etkileşimli HTML sunumun içerik ve entegrasyon kaynağıdır.
- PDF, portal bağlantılarını ve sunuma dönüş davranışını temsil etmez.
- Konuşma notları öğretmene özel kalmalıdır.

> Üretim listesi yapılırken bu dosya **PDF dışı tutulmalı**.
