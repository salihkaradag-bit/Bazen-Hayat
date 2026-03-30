# Bileşik Faiz Hesaplama Uygulaması

def bilesik_faiz_hesapla():
    print("--- Bileşik Faiz Hesaplayıcıya Hoş Geldiniz ---\n")

    # Kullanıcıdan gerekli bilgileri alıyoruz
    try:
        ana_para = float(input("Başlangıç ana para tutarını girin (P): "))
        yillik_oran = float(input("Yıllık faiz oranını girin (% cinsinden, örn: 15): "))
        vade_ayi = float(input("Toplam vade süresini girin (Ay olarak): "))
        siklik = int(input("Yılda kaç kez faiz işletilecek? (Örn: Aylık için 12, Yıllık için 1): "))

        # Yüzdelik oranı ondalık sayıya çeviriyoruz (Örn: 15 -> 0.15)
        r = yillik_oran / 100
        t_yil= vade_ayi / 12

        # Bileşik faiz formülünü uyguluyoruz: A = P * (1 + r/n)**(n*t)
        toplam_tutar = ana_para * (1 + r / siklik)**(siklik * t_yil)

        # Net kazancı hesaplıyoruz
        toplam_kar = toplam_tutar - ana_para

        # Sonuçları ekrana yazdırıyoruz
        print("\n" + "=" * 30)
        print(f"Girdiğiniz Faiz Oranı: %{yillik_oran}")
        print(f"Vade Süresi: {vade_ayi} Ay")
        print(f"Vade Sonundaki Para: {toplam_tutar:,.2f} TL")
        print(f"Toplam Faiz Getirisi: {toplam_kar:,.2f} TL")
        print("=" * 30)

    except ValueError:
        print("Lütfen sadece sayısal değerler giriniz!")

# Fonksiyonu çalıştır
if __name__ == "__main__":
    bilesik_faiz_hesapla()
