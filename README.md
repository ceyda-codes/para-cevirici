# Para Birimi Çevirici (Currency Converter)

Bu Python projesi, Frankfurter API kullanarak iki para birimi arasında gerçek zamanlı döviz kuru dönüşümü yapar.

## Özellikler
- Kullanıcıdan miktar ve para birimi girişi
- Gerçek zamanlı API ile dönüşüm
- Hatalı para birimi kontrolü
- Döviz kuru tarihini gösterir
- Kullanıcı isterse tekrar tekrar işlem yapabilir

## Kullanım
1. `requests` kütüphanesinin kurulu olduğundan emin olun:
   ```bash
   pip install requests

2. Teminalden çalıştırın:
   python para_cevirici.py

Örnek

Çevirmek istediğin miktarı gir: 100
Hangi para biriminden? (Örn: EUR): USD
Hangi para birimine? (Örn: TRY): EUR

Döviz kuru tarihi: 2025-04-11  
100 USD = 91.45 EUR

API
Veriler Frankfurter API üzerinden alınmaktadır:
https://www.frankfurter.app/

Kaydet ve kapat.

---

### **3. Adım: GitHub’a yükle**

Şimdi tekrar terminale dön ve şunu yaz:

```bash
git add README.md
git commit -m "README dosyası eklendi"
git push
