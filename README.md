# Banka_proje_python

Sınıflar

-Kullanici Sınıfı

Amacı:
Kullanıcı hesap bilgilerini tutar ve işlem yapma gibi işlevler içerir

Değişkenler(Özellikler)

ad: Kullanıcının adı
hesap_no: Kullanıcının hesap numarası
bakiye: Kullanıcının hesap bakiyesi

Fonksiyonlar
para_yatir(miktar): Kullanıcının bakiyesine belirtilen miktarı ekler.

para_cek(miktar): Kullanıcının bakiyesinden belirtilen miktarı çeker. Yetersiz bakiye durumunda işlem ret yer

bakiye_goster(): Kullanıcının hesap numarasını ve güncel bakiyesini gösterir.

2. Banka Sınıfı

Amacı
Kullanıcı hesaplarının yönetimini sağlar.

Değişkenler(Özellikler)

kullanicilar: Banka sistemindeki tüm kullanıcı hesaplarını tutar (hesap_no bazlı).
Fonksiyonlar

hesap_ac(ad, hesap_no, bakiye): Yeni bir kullanıcı hesabı oluşturur.

giris_yap(hesap_no): Belirtilen hesap numarasına sahip kullanıcıyı döner.
