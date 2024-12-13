class Kullanici:
    def __init__(self, ad, hesap_no, bakiye=0):
        self.ad = ad
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar.")

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")

    def bakiye_goster(self):
        print(f"Hesap No: {self.hesap_no}, Bakiye: {self.bakiye} TL")


class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_ac(self, ad, hesap_no, bakiye):
        if hesap_no in self.kullanicilar:
            print("Bu hesap numarası zaten kullanılıyor.")
        else:
            yeni_kullanici = Kullanici(ad, hesap_no, bakiye)
            self.kullanicilar[hesap_no] = yeni_kullanici
            print(f"Hesap açıldı: {ad}, Hesap No: {hesap_no}, Başlangıç Bakiyesi: {bakiye} TL")

    def giris_yap(self, hesap_no):
        if hesap_no in self.kullanicilar:
            return self.kullanicilar[hesap_no]
        else:
            print("Hesap bulunamadı.")
            return None


if __name__ == "__main__":
    banka = Banka()

    while True:
        print("\nBanka Sistemi:")
        print("1. Hesap Aç")
        print("2. Giriş Yap")
        print("3. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Adınızı girin: ")
            hesap_no = input("Hesap numarası girin: ")
            bakiye = float(input("Başlangıç bakiyesini girin: "))
            banka.hesap_ac(ad, hesap_no, bakiye)

        elif secim == "2":
            hesap_no = input("Hesap numaranızı girin: ")
            kullanici = banka.giris_yap(hesap_no)
            if kullanici:
                while True:
                    print("\nHesap İşlemleri:")
                    print("1. Para Yatır")
                    print("2. Para Çek")
                    print("3. Bakiye Göster")
                    print("4. Ana Menüye Dön")
                    alt_secim = input("Seçiminizi yapın: ")

                    if alt_secim == "1":
                        miktar = float(input("Yatırılacak miktar: "))
                        kullanici.para_yatir(miktar)
                    elif alt_secim == "2":
                        miktar = float(input("Çekilecek miktar: "))
                        kullanici.para_cek(miktar)
                    elif alt_secim == "3":
                        kullanici.bakiye_goster()
                    elif alt_secim == "4":
                        break
                    else:
                        print("Geçersiz seçim.")

        elif secim == "3":
            print("Çıkış yapılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim.")
