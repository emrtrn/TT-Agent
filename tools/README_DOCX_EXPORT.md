# TT-Agent DOCX Dışa Aktarma

Markdown kaynaklarını düzenlenebilir DOCX belgelerine aktarır; kaynaklara yazmaz.

~~~powershell
python -m pip install -r tools/requirements-docx.txt
.\tools\export-tt-agent-docx.ps1 -Grade 8 -Unit unit1
~~~

Çıktılar docs/docx/8_sinif/unit1 altında oluşur. Tek dosya için kaynak yolunu,
tüm dolu üniteler için -All, farklı hedef için -OutputRoot kullanın.

Her belgede A4 mizanpajı, üst/alt bilgi, sayfa numarası, tablo sayısı, açık
sayfa sonları, Türkçe karakterler ve kaynak SHA-256 bütünlüğü doğrulanır.
