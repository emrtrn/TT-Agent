# Etkileşimli Sunum ve Öğrenme Akışı

Bu belge, sunum içeriğinin `Öğren → Pekiştir → Uygula → Materyaller` akışındaki rolünü ve ünite üretim sırasını tanımlar. Sunum yalnızca slayt metni değildir; öğretmenin ders akışını yönetir ve uygun anlarda diğer portal kaynaklarına geçiş verir.

## Temel karar

Sunum iki aşamada hazırlanır:

1. **Sunum taslağı:** Canlı MEB doğrulaması, öğretmen hazırlığı ve ders planından hemen sonra başlatılır. Slayt sırası, öğretmen yönergeleri, ölçme anları ve ihtiyaç duyulan kaynak türleri belirlenir.
2. **Entegrasyonlu nihai sürüm:** Ön değerlendirme, kısa videolar, Pekiştir etkinlikleri, Uygula deneyimleri ve öğretmen materyalleri üretildikçe kesin kaynak kimlikleri eklenir. Bağlantı ve sunuma dönüş davranışları doğrulanmadan sunum tamamlanmış sayılmaz.

Sunum taslağı için bütün materyallerin bitmesi beklenmez. Buna karşılık yalnızca slayt metninin yazılmış olması da sunumun tamamlandığı anlamına gelmez.

## Öğrenme aşamalarının sunumdaki karşılığı

| Aşama | Sunumun rolü | Örnek geçiş |
|---|---|---|
| Öğren | Kavramı açıklar, örneklendirir ve kısa anlatımı yönetir | Slayt → kısa dikey video |
| Pekiştir | Kavram kullanıldıktan hemen sonra 2–7 dakikalık etkinliğe yönlendirir | Slayt → kavram kartı/eşleştirme/mini quiz |
| Uygula | Öğrenciyi daha kapsamlı beceri veya ürün oluşturma deneyimine geçirir | Slayt → senaryo/simülasyon/tasarım aracı |
| Materyaller | Öğretmene kullanılacak basılı veya indirilebilir materyalin zamanını bildirir | Slayt yönergesi → ön değerlendirme/çalışma kâğıdı |

Materyal ilişkisi her zaman doğrudan bağlantı olmak zorunda değildir. Slayt, öğretmenin önceden indirdiği bir çalışma kâğıdının kullanım anını da açıkça belirtebilir.

## Sunum Markdown kaynak sözleşmesi

İlgili her slaytta aşağıdaki alanlar bulunur:

```md
### SLAYT [N] — [Başlık]

**Öğrenme aşaması:** Öğren / Pekiştir / Uygula / Materyaller
**Pedagojik amaç:** [Bu geçişin neden burada olduğu]
**Gerekli materyal:** [Yoksa “Yok”]
**İlgili kaynaklar:** [Kararlaştırılmış kaynak kimlikleri veya TASLAK]
**Kaynak türü:** Kısa video / Etkileşim / Quiz / Uygulama / Belge
**Açılma biçimi:** Portal içi görüntüleyici / Öğretmenin önceden hazırlaması
**Dönüş davranışı:** Sunuma dön / Slaytta kal
```

Kaynak kimliği henüz oluşturulmadıysa hayalî kimlik yazılmaz; `TASLAK — kimlik katalog kaydında belirlenecek` ifadesi kullanılır.

## İçerik yerleştirme ilkeleri

- Kısa ve doğrudan ilgili videolar, kavramın işlendiği slayda bağlanabilir.
- Uzun videolar sunum içi akışı kesmez; ünite sayfasında ayrı Öğren kaynağı olarak tutulur.
- Pekiştir etkinliği, ilgili kavram anlatıldıktan hemen sonra erişilebilir olmalıdır.
- Aynı etkinlik gereksiz yere birden çok slaytta tekrarlanmaz.
- Uygula deneyimleri, gerekli ön bilgi ve yönerge tamamlandıktan sonra açılır.
- Ön değerlendirme, çalışma kâğıdı ve rubrik gibi belgelerin hangi slaytta kullanılacağı sunum Markdown’ında belirtilir.
- Slayt değiştiğinde açık ilgili-içerik menüsü kapanmalıdır.
- Kaynaktan çıkış kullanıcıyı aynı üniteye ve mümkünse kaldığı sunuma döndürmelidir.

## Üretim sırası

1. Canlı MEB program ve ilgili ünite sayfasını doğrula.
2. Öğretmen hazırlığı ile ayrıntılı ders planını hazırla.
3. Üniteye özel sunum entegrasyon haritasının ilk sürümünü oluştur.
4. Sunum Markdown taslağını yaz.
5. Ön değerlendirme, kavram kartları, kısa videolar, Pekiştir/Uygula içerikleri ve materyalleri üret.
6. Entegrasyon haritasına kesin kaynak kimliklerini işle.
7. Sunum Markdown’ını nihai hâle getir ve etkileşimli HTML sunumu üret.
8. Kaynak kataloğu, açılış, kapanış, sunuma dönüş ve akıllı tahta davranışlarını doğrula.

## Tamamlanma ölçütleri

- [ ] Her slayt bir ders saati ve öğrenme çıktısıyla ilişkilendirildi.
- [ ] Öğrenme aşaması gerektiren slaytlarda açıkça belirtildi.
- [ ] Gerekli basılı/indirilebilir materyaller kullanım anlarına bağlandı.
- [ ] Sunum içi kaynak kimlikleri katalogdaki gerçek kayıtlarla eşleşiyor.
- [ ] Kısa video ve mikro etkinlikler doğru slaytlarda açılıyor.
- [ ] İlgili içerikten sunuma dönüş çalışıyor.
- [ ] Slayt değişiminde açık içerik menüsü kapanıyor.
- [ ] Masaüstü, mobil ve akıllı tahta için gerekli kontroller ayrı raporlandı.
- [ ] Otomatik doğrulama ile kullanıcı görsel kabulü ayrı kaydedildi.

