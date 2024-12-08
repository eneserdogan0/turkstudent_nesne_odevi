class Kullanici:
    def __init__(self, ad, hesap_no, bakiye=0.0):
        self.ad = ad
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar. Para yatırma işlemi başarısız.")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye. Çekme işlemi başarısız.")
        elif miktar > 0:
            self.bakiye -= miktar
            print(f"{miktar} TL başarıyla çekildi. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar. Çekme işlemi başarısız.")

    def bakiye_sorgula(self):
        print(f"{self.ad} adlı kullanıcının güncel bakiyesi: {self.bakiye} TL")

    def __str__(self):
        return f"Kullanıcı Adı: {self.ad}, Hesap No: {self.hesap_no}, Bakiye: {self.bakiye} TL"


class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_ac(self, ad, hesap_no, bakiye=0.0):
        if hesap_no in self.kullanicilar:
            print("Bu hesap numarası zaten mevcut.")
        else:
            self.kullanicilar[hesap_no] = Kullanici(ad, hesap_no, bakiye)
            print(f"{ad} için hesap başarıyla oluşturuldu. Hesap No: {hesap_no}, Başlangıç Bakiyesi: {bakiye} TL")

    def kullanici_giris(self, hesap_no):
        return self.kullanicilar.get(hesap_no, None)

    def tum_kullanicilari_goster(self):
        if not self.kullanicilar:
            print("Sistemde henüz kayıtlı kullanıcı yok.")
        else:
            print("\n--- Tüm Kullanıcılar ---")
            for kullanici in self.kullanicilar.values():
                print(kullanici)


def main():
    banka = Banka()

    while True:
        print("\n--- Banka Sistemi ---")
        print("1. Hesap Aç")
        print("2. Giriş Yap ve İşlem Yap")
        print("3. Tüm Kullanıcıları Görüntüle")
        print("4. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Ad: ")
            hesap_no = input("Hesap No: ")
            bakiye = float(input("Başlangıç Bakiyesi: "))
            banka.hesap_ac(ad, hesap_no, bakiye)
        elif secim == "2":
            hesap_no = input("Hesap No: ")
            kullanici = banka.kullanici_giris(hesap_no)
            if kullanici:
                print(f"{kullanici.ad} olarak giriş yaptınız.")
                while True:
                    print("\n1. Para Yatır")
                    print("2. Para Çek")
                    print("3. Bakiye Sorgula")
                    print("4. Ana Menüye Dön")
                    alt_secim = input("Seçiminiz: ")

                    if alt_secim == "1":
                        miktar = float(input("Yatırılacak Miktar: "))
                        kullanici.para_yatir(miktar)
                    elif alt_secim == "2":
                        miktar = float(input("Çekilecek Miktar: "))
                        kullanici.para_cek(miktar)
                    elif alt_secim == "3":
                        kullanici.bakiye_sorgula()
                    elif alt_secim == "4":
                        break
                    else:
                        print("Geçersiz seçim.")
            else:
                print("Hesap bulunamadı. Lütfen doğru hesap numarasını giriniz.")
        elif secim == "3":
            banka.tum_kullanicilari_goster()
        elif secim == "4":
            print("Sistemden çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
