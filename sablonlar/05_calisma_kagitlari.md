# 📋 Şablon: Öğrenci Çalışma Kâğıtları

> Bu şablon **`Unite[N]_Calisma_Kagitlari.md`** dosyasının yapısını gösterir.  
> Her ders saati etkinliği için **ayrı çalışma kâğıdı** olur.

---

## 📐 Genel Yapı

```markdown
# [N]. Ünite: Öğrenci Çalışma Kâğıtları

> Bu dosya, [N]. Ünite'deki **dört öğrenme çıktısına** yönelik sınıfta kullanıma hazır çalışma kâğıtlarını içerir.  
> Her çalışma kâğıdı **ayrı sayfa** olarak yazdırılmak üzere tasarlanmıştır.

---

## ÇALIŞMA KÂĞITLARI LİSTESİ

| # | Başlık | İlgili Kazanım | Ders Saati | Tahmini Süre |
|:-:|--------|:--:|:---:|:-:|
| 1 | [Çalışma kâğıdı 1 adı] | [Kazanım] | [Saat] | [Süre] |
| 2 | [...] | ... | ... | ... |
| ... | ... | ... | ... | ... |

---

## ÇALIŞMA KÂĞIDI 1: [BAŞLIK]

**Adı Soyadı:** ___________________________  **Sınıf/No:** _________  **Tarih:** ___________

---

### Yönerge

> **Yönerge:** [Yönerge metni]
> 
> **Süre:** [X] dakika  
> **Not:** [Önemli not, örn. "Doğru/yanlış cevap yok"]

---

### [Bölüm 1 Başlığı]

[İçerik — sorular, alıştırmalar, tablo, vb.]

[Yazma alanı için 3-5 satır]

---

### [Bölüm 2 Başlığı]

[İçerik]

---

### Yansıtma / Öz Değerlendirme

> Bu çalışmayı tamamladıktan sonra:
> - En iyi yaptığım: _______________
> - Zorlandığım: _______________

---

### Kontrol Listesi

✓ Yazımı kontrol et:
- [ ] [Kontrol maddesi 1]
- [ ] [Kontrol maddesi 2]
- [ ] [Kontrol maddesi 3]
- [ ] [Kontrol maddesi 4]

---
---

## ÇALIŞMA KÂĞIDI 2: [BAŞLIK]

[Aynı yapı]

[Tüm çalışma kâğıtları için bu yapı]

---

## ÖĞRETMEN NOTLARI

### Çalışma Kâğıtlarının Kullanımı

1. **Yazdırma önerisi:** Siyah-beyaz yazdırılabilir; A4 dikey format uygundur.
2. **Dosyalama:** Her öğrenciye **kişisel bir klasör** verirseniz, tüm ünite boyunca çalışma kâğıtlarını bir arada tutabilir → **portfolyo değerlendirmesi** yapabilirsiniz.
3. **Dijital versiyon:** Google Forms veya Google Classroom'a aktarılarak dijital olarak da kullanılabilir.
4. **Sınıf içi görünürlük:** Tamamlanan çalışmalar **sınıf panosuna** asılabilir.

### Farklılaştırma

- **Destekleme gerektiren öğrenciler için:** Bazı çalışma kâğıtları için **örnek cevap** versiyonu hazırlanabilir (Destekleme Paketi'nde var).
- **Zenginleştirme için:** İleri düzey öğrenciler ek soru/derinlik isteyebilir (Zenginleştirme Paketi'nde var).

### Sonuçların Kullanımı

- **İlk çalışma kâğıdı (zihin haritası vb.) saklayın!** Ünite sonunda öğrenciye iade edip farklı renkle ekleme yaptırın.
- **Öz değerlendirme bölümleri** kendi öğretim stratejinizi değerlendirmek için ipucu.
```

---

## ✅ Üretim Sırasında Dikkat Edilecekler

### Çalışma Kâğıdı Sayısı
- Her **ana etkinlik** için 1 çalışma kâğıdı (genelde her ders saatinde 1 kâğıt)
- Bazı kâğıtlar **ünite başında** (zihin haritası) ve **ünite sonunda** (öz değerlendirme) kullanılır
- **Tipik sayı:** 6-10 çalışma kâğıdı

### Adı-Soyadı / Sınıf / Tarih Alanı
**Her çalışma kâğıdının üstünde** olmalı:
```markdown
**Adı Soyadı:** ___________________________  **Sınıf/No:** _________  **Tarih:** ___________
```

PDF üretiminde bu alan otomatik **çizgi alanlı tablo** olur.

### Yönerge Kutusu
Her kâğıdın üstünde **açık turuncu arka planlı yönerge kutusu** olmalı:
```markdown
> **Yönerge:** [Net yönerge metni]
> 
> **Süre:** X dakika
```

PDF üretiminde bu otomatik kutu olur.

### Yazı Alanları
Markdown'da yazı alanı için:
- **Kısa cevap:** `[Yazma alanı için 1 satır]` (PDF'te 1 hafif gri çizgi)
- **Orta uzun:** `[Yazma alanı için 3 satır]` (3 çizgi)
- **Uzun:** `[Yazma alanı için 5 satır]` (5 çizgi)

PDF üretiminde `WritingLines(num_lines=N)` flowable olarak çıkar.

### Özel Çizimler
Eğer çalışma kâğıdında özel çizim alanı varsa (zihin haritası, Venn diyagramı, vb.):
```markdown
> **NOT:** PDF üretiminde MindMapCanvas özel flowable kullanılacak.
```

PDF üretim aşamasında **özel kod** yazılır.

### Yansıtma Bölümü
Her çalışma kâğıdının sonunda **kısa bir yansıtma**:
- "En iyi yaptığım..."
- "Zorlandığım..."
- "Bir sonraki çalışmada..."

Bu bölüm **3-5 satırlık yazı alanı** olur.

### Kontrol Listesi
Her kâğıdın sonunda **öğrencinin işini kontrol etmesi** için checkbox listesi:
```markdown
- [ ] Tüm soruları cevapladım
- [ ] Yazımı düzgün
- [ ] Adımı yazdım
```

PDF'te `Checkbox` flowable olarak çıkar.

---

## 📌 Önemli Notlar

### Süreyi Belirt
Her kâğıdın yönergesinde **net süre** olmalı:
- ✅ "Süre: 15 dakika"
- ❌ "Yeterli süre"

### Yaş-uygun Dil
- Seçilen sınıf düzeyindeki öğrenci için
- "Sen" diliyle ("yazıyorsun", "düşünüyorsun")
- Akademik jargondan kaçın

### Görsel Yönlendirme
- Adım adım işaret et (1, 2, 3, ...)
- "Adım 1", "Adım 2" gibi başlıklar
- Mümkünse ipuçları ekle

### Doğrulama
Çalışma kâğıdını öğrenci yapabilir mi? **Test et:**
1. Yönergeleri tek başına okuyup anlayabilir mi?
2. Sürede tamamlayabilir mi?
3. Cevap verecek alan yeterli mi?
4. Yazım hataları var mı?
