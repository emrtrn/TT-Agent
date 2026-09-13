# Etkileşimli Sunum ve Öğrenme Akışı

Bu belge, sunum içeriğinin `Öğren → Pekiştir → Uygula → Materyaller` akışındaki rolünü ve ünite üretim sırasını tanımlar. Sunum yalnızca slayt metni değildir; öğretmenin ders akışını yönetir ve uygun anlarda diğer portal kaynaklarına geçiş verir.

## Temel karar

Sunum iki aşamada hazırlanır:

1. **Sunum omurgası:** Canlı MEB doğrulaması, öğretmen hazırlığı ve ders planından hemen sonra hazırlanır. Ders/slayt sırası, öğretmen yönergeleri, ölçme anları ve ihtiyaç duyulan kaynak türleri belirlenir. Bu aşama, üretilecek dokümanları yönlendiren planlama kaydıdır; tam slayt metni veya HTML değildir.
2. **Entegrasyonlu nihai sürüm:** Ön değerlendirme, çalışma kâğıtları, kavram kartları, kısa videolar, Pekiştir etkinlikleri, Uygula deneyimleri, değerlendirme araçları ve öğretmen materyalleri tamamlandıktan sonra kesin kaynak kimlikleri eklenir. Ardından tam sunum Markdown'ı ve HTML üretilir. Bağlantı ve sunuma dönüş davranışları doğrulanmadan sunum tamamlanmış sayılmaz.

Omurga için bütün materyallerin bitmesi beklenmez. Buna karşılık, kaynakları belirlenmeden hazırlanmış slayt metni veya HTML sunum nihai çıktı sayılmaz.

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
3. Üniteye özel sunum omurgasını ve entegrasyon haritasının ilk sürümünü oluştur; yalnızca kaynak türlerini ve kullanım anlarını kaydet.
4. Ön değerlendirme, çalışma kâğıtları, kavram kartları, kısa videolar, Pekiştir/Uygula içerikleri, değerlendirme araçları ve öğretmen materyallerini üret.
5. Her kaynak için gerçek katalog kimliğini, açılma biçimini ve dönüş davranışını entegrasyon haritasına işle.
6. Sunum Markdown'ını; gerçek materyal adları, nihai slayt metni ve konuşmacı notlarıyla hazırla.
7. Etkileşimli HTML sunumu üret.
8. Kaynak kataloğu, açılış, kapanış, sunuma dönüş ve akıllı tahta davranışlarını doğrula.

## Tamamlanma ölçütleri

- [ ] Her slayt bir ders saati ve öğrenme çıktısıyla ilişkilendirildi.
- [ ] Tüm bağlı dokümanlar ve etkinlikler üretilmeden tam sunum Markdown'ı veya HTML başlatılmadı.
- [ ] Öğrenme aşaması gerektiren slaytlarda açıkça belirtildi.
- [ ] Gerekli basılı/indirilebilir materyaller kullanım anlarına bağlandı.
- [ ] Sunum içi kaynak kimlikleri katalogdaki gerçek kayıtlarla eşleşiyor.
- [ ] Kısa video ve mikro etkinlikler doğru slaytlarda açılıyor.
- [ ] İlgili içerikten sunuma dönüş çalışıyor.
- [ ] Slayt değişiminde açık içerik menüsü kapanıyor.
- [ ] Masaüstü, mobil ve akıllı tahta için gerekli kontroller ayrı raporlandı.
- [ ] Otomatik doğrulama ile kullanıcı görsel kabulü ayrı kaydedildi.
