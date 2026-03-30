def aylik_yatirim_hesapla():
    print("--- Aylık Eklemeli Bileşik Faiz Simülasyonu ---\n")

    try:
        # Girdiler
        ana_para = float(input("Başlangıç ana parası (P): "))
        aylik_ekleme = float(input("Her ay sonu eklenecek miktar: "))

        oran_girisi = input("Yıllık faiz oranı (Örn: 48.07): ").replace(',', '.')
        yillik_oran = float(oran_girisi)

        vade_ayi = int(input("Toplam vade süresi (Ay): "))

        # Aylık faiz oranını hesapla (Yıllık oran / 12)
        aylik_faiz_orani = (yillik_oran / 100) / 12

        su_anki_bakiye = ana_para
        toplam_yatirilan = ana_para

        print("\nAY | BAŞLANGIÇ | FAİZ GETİRİSİ | EKLEME | DÖNEM SONU")
        print("-" * 60)

        for ay in range(1, vade_ayi + 1):
            baslangic = su_anki_bakiye

            # 1. Faiz işletilir
            faiz_getirisi = baslangic * aylik_faiz_orani

            # 2. Faiz eklenir
            su_anki_bakiye += faiz_getirisi

            # 3. Aylık ek para yatırılır
            su_anki_bakiye += aylik_ekleme
            toplam_yatirilan += aylik_ekleme

            print(f"{ay:2d} | {baslangic:10.2f} | {faiz_getirisi:13.2f} | {aylik_ekleme:6.2f} | {su_anki_bakiye:10.2f}")

        # Özet Sonuçlar
        print("-" * 60)
        print(f"Toplam Yatırılan Anapara: {toplam_yatirilan:,.2f} TL")
        print(f"Toplam Faiz Getirisi   : {su_anki_bakiye - toplam_yatirilan:,.2f} TL")
        print(f"Vade Sonu Toplam Bakiyesi: {su_anki_bakiye:,.2f} TL")

    except ValueError:
        print("Hata: Lütfen geçerli sayısal değerler giriniz!")


if __name__ == "__main__":
    aylik_yatirim_hesapla()
