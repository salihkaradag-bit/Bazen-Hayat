import random
import time

def stat_goster(saglik, hiz, guc, zirh, ceviklik):
    print(f"""
Sağlık: {saglik}
Hız: {hiz}
Güç: {guc}
Zırh: {zirh}
Çeviklik: {ceviklik}
""")

def elf_baslangic_sahnesi(nick, ceviklik):
    print(f"""
Derin bir nefes alıyorsun {nick}.
Bulunduğun yer sessiz değil,
Ama düzenli.

Yayını kaldırıyorsun.
Nefesin yavaşlıyor.
Kalbin ritmini hissediyorsun.

Gözlerin hedefte.

On iki adım ötede duran hedef,
Ne bir adım fazla, ne bir eksik.

Yayı geriyorsun.

Bir anlık duraksama.
Sonra bırakıyorsun.

Ok havayı yarıyor.

Tak.

Tam 12'den.

Etrafında senin gibi birçok elf daha var.
Hepsi hedeflerini vurmuş durumda.
Kimse dönüp sana bakmıyor.
Kimse seni tebrik etmiyor.

Çünkü burada bu, normal.

Biraz ileride başka elfler uzun, mızrak benzeri kılıçlarla talim yapıyor.
Metal ve ahşap sesi birbirine karışıyor.
Disiplinli, sert, sessiz.

Her şey bir savaşa hazırlık gibi görünüyor.

Ama sana ne?
Sen emirleri yerine getirirsin.

Komut yükseliyor:
"Oklar toplansın."

Diğer elfler hedeflere doğru ilerliyor.

Ama senin için hâlâ bir an var.

Yay hâlâ elinde.
Bir ok daha var.

Ne yapacaksın?
""")

    while True:
        print("""
1) Okları toplayanlara katıl
2) Bir ok daha at (riskli)
        """)
        secim = input("Seçimin: ").strip()
        if secim == "1":
            print(f"""
Yayını indiriyorsun {nick}.
Disiplinden sapmıyorsun.
Burada hayatta kalmanın yolu bu.
            """)
            return "toplandi"
        elif secim == "2":
            zar = random.randint(1, 24)
            toplam = zar + ceviklik

            print(f"\nZar: {zar} | Çeviklik: {ceviklik} | Toplam: {toplam}")

            if toplam >= 12:
                print(f"""
Ok bir kez daha hedefi buluyor.

Bu sefer birkaç bakış sana çevriliyor.
Kimse konuşmuyor,
Ama seni fark ettiler.
                """)
                return "ustalik"
            else:
                print(f"""
Ok hedefi ıskalıyor.

Sessizlik ağırlaşıyor.
Kimse gülmüyor.
Ama bu hata unutulmaz.
                """)
                return "iskaladi"
        else:
            print("Geçersiz seçim.")

def patika_sahnesi_2_zirh (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print("Aşağı doğru patikadan zırhlı")

def patika_sahnesi_2 (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print("Aşağı doğru patikadan zırhsız")

def atese_dogru_sahnesi_zirh (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""zırhlı""")
    return saglik, hiz, guc, zirh, ceviklik

def atese_dogru_sahnesi (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""zırhsız""")
    return saglik, hiz, guc, zirh, ceviklik

def tirmanma_sahnesi_zirh (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
    Tepeye tırmanmaya çalışıyorsun {nick}.
    Zemin dengesiz, taşlar ayağının altında kayıyor. 
    Her adımda vücudun biraz daha ağırlaşıyor, bacakların titriyor. 
    Nefesin düzensiz, göğsün yanıyor ama durmuyorsun. 
    Aşağıya bakmıyorsun; bakarsan düşeceğini hissediyorsun.
    Ellerinle toprağa tutunuyor, bazen dizlerinin üzerinde ilerliyorsun. 
    Rüzgâr yüzüne vuruyor, duman hâlâ ciğerlerini yakıyor. 
    Her adım attıktan sonra biraz sendeliyorsun, birkaç kez neredeyse yere kapaklanıyorsun.
    Ama bu seni durduracak gibi durmuyor.
    İçindeki inat, yorgunluktan daha güçlü. Son bir hamleyle kendini yukarı çekiyorsun. 
    Ellerinin altındaki zemin sonunda düzleşiyor. Bir süre olduğun yerde kalıp nefesini toplamaya çalışıyorsun.
    En sonunda tepenin üzerindesin.
    Aşağıda yanan orman, arkanda bıraktığın kaos,
    Şimdilik burası güvende olduğun tek yer
    Bir süre ufka bakıyorsun. Dumanın arasından, uzaklarda titrek bir ışık seçiliyor. Bir ateş...
    Ve bu ateş tek başına yanıyor gibi durmuyor. Çevresinde karaltılar var. İnsanlar. 
    Ya da en azından insan olduklarını umduğun siluetler.
    Belki onlar bu yangının nedenini biliyordur.
    Belki senin kim olduğuna, buraya nasıl geldiğine dair bir şeyler öğrenebilirsin.
    Ama oraya gitmek zorunda değilsin.
    Tepenin diğer tarafında aşağı doğru inen dar bir patika görüyorsun. 
    Sessiz, karanlık ve izole. 
    Ateşten ve insanlardan uzak. 
    Eğer istersen, kimseyle karşılaşmadan yoluna devam edebilirsin""")
    while True:
        print("""
    1) Ateşin gelgiği yeri takip et
    2) Patikayı takip et
            """)
        secim3 = input("Seçimin: ").strip()
        if secim3 == "1":
            return "atese_dogru", saglik, hiz, guc, zirh, ceviklik
        elif secim3 == "2":
            return "patika", saglik, hiz, guc, zirh, ceviklik
        else:
            print("Geçersiz seçim, tekrar dene.")

def dusme_sahnesi_zirh(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
    Her 1 attığında tepe senden 2 adım uzaklaşıyor gibi hissetmeye başlıyorsun
    Yolun çok uzunmuş gibi geliyor 
    Dinç bir zamanında olsan yapanileceğininden eminsin {nick}
    Ama şuan yapabilecek birşey yok gibi duruyor
    Biraz daha kendini zorluyorsun ancak vücudun iflas eder gibi seni kitliyor
    Rüzgarın esintisi ile yuvarlanmaya başlıyorsun
    Artık vücudunun hiçbir uzvu üzerinde kontrolün yok
    Zırh seni daha da engelliyormuş gibi hissediyorsun
    Yuvarlanırken birkaç taş parçası sana çarpıyor daha doğrusu sen onlara 
    Zırhının altında eziliyorlar ama sanki onlarda seni eziyor
    En son az önceki yere vardın sonunda bu ızdırap bitti
    Sendeleyerek kalkıyorsun
    Oyun boyunca geçerli sağlığından 3 kaybettiniz ...
    """)
    saglik -= 3
    print(f"Yeni sağlığın: {saglik}")
    return saglik, hiz, guc, zirh, ceviklik

def patika_sahnesi_zirh (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
      O tepeye çıkmak baktıkça gözünde büyüyor.
      Yapacak birşey yok diye düşünüyorsun {nick}
      Patikayı izlemek biraz çamurlu bir yoldan ilerliyorsun...
      """)
    return saglik, hiz, guc, zirh, ceviklik

def tirmanma_sahnesi (nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
    Tepeye tırmanmaya çalışıyorsun {nick}.
    Zemin dengesiz, taşlar ayağının altında kayıyor. 
    Her adımda vücudun biraz daha ağırlaşıyor, bacakların titriyor. 
    Nefesin düzensiz, göğsün yanıyor ama durmuyorsun. 
    Aşağıya bakmıyorsun; bakarsan düşeceğini hissediyorsun.
    Ellerinle toprağa tutunuyor, bazen dizlerinin üzerinde ilerliyorsun. 
    Rüzgâr yüzüne vuruyor, duman hâlâ ciğerlerini yakıyor. 
    Her adım attıktan sonra biraz sendeliyorsun, birkaç kez neredeyse yere kapaklanıyorsun.
    Ama bu seni durduracak gibi durmuyor.
    İçindeki inat, yorgunluktan daha güçlü. Son bir hamleyle kendini yukarı çekiyorsun. 
    Ellerinin altındaki zemin sonunda düzleşiyor. Bir süre olduğun yerde kalıp nefesini toplamaya çalışıyorsun.
    En sonunda tepenin üzerindesin.
    Aşağıda yanan orman, arkanda bıraktığın kaos,
    Şimdilik burası güvende olduğun tek yer
    Bir süre ufka bakıyorsun. Dumanın arasından, uzaklarda titrek bir ışık seçiliyor. Bir ateş...
    Ve bu ateş tek başına yanıyor gibi durmuyor. Çevresinde karaltılar var. İnsanlar. 
    Ya da en azından insan olduklarını umduğun siluetler.
    Belki onlar bu yangının nedenini biliyordur.
    Belki senin kim olduğuna, buraya nasıl geldiğine dair bir şeyler öğrenebilirsin.
    Ama oraya gitmek zorunda değilsin.
    Tepenin diğer tarafında aşağı doğru inen dar bir patika görüyorsun. 
    Sessiz, karanlık ve izole. 
    Ateşten ve insanlardan uzak. 
    Eğer istersen, kimseyle karşılaşmadan yoluna devam edebilirsin""")
    while True:
        print("""
    1) Ateşin gelgiği yeri takip et
    2) Patikayı takip et
            """)
        secim3 = input("Seçimin: ").strip()
        if secim3 == "1":
            return "atese_dogru", saglik, hiz, guc, zirh, ceviklik
        elif secim3 == "2":
            return "patika", saglik, hiz, guc, zirh, ceviklik
        else:
            print("Geçersiz seçim, tekrar dene.")

def dusme_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
    Her 1 attığında tepe senden 2 adım uzaklaşıyor gibi hissetmeye başlıyorsun
    Yolun çok uzunmuş gibi geliyor 
    Dinç bir zamanında olsan yapanileceğininden eminsin {nick}
    Ama şuan yapabilecek birşey yok gibi duruyor
    Biraz daha kendini zorluyorsun ancak vücudun iflas eder gibi seni kitliyor
    Rüzgarın esintisi ile yuvarlanmaya başlıyorsun
    Artık vücudunun hiçbir uzvu üzerinde kontrolün yok
    Yuvarlanırken birkaç taş parçası sana çarpıyor daha doğrusu sen onlara 
    En son az önceki yere vardın sonunda bu ızdırap bitti
    Sendeleyerek kalkıyorsun
    Oyun boyunca geçerli sağlığından 2 kaybettiniz
    """)
    saglik -= 2
    print(f"Yeni sağlığın: {saglik}")
    return saglik, hiz, guc, zirh, ceviklik

def patika_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
      O tepeye çıkmak baktıkça gözünde büyüyor.
      Yapacak birşey yok diye düşünüyorsun {nick}
      Patikayı izlemek biraz çamurlu bir yoldan ilerliyorsun
      """)
    return saglik, hiz, guc, zirh, ceviklik

def hafif_kacis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f""" 
{nick} Tokayı kavrıyorsun.
Parmakların yanıyor ama durmuyorsun. 
Metal sıcak, neredeyse elini yakacak kadar. 
Bir hamle, sonra bir tane daha… Sonunda zırh gevşiyor. 
Omuzlarından kayarken çıkardığı ses, alevlerin uğultusuna karışıyor.

Zırhı yere bırakıyorsun.

Bir anda hafifliyorsun. 
Nefesin açılıyor, adımların sana geri dönüyor. 
Artık koşabiliyorsun. 
Alevlerin arasından çevik hareketlerle sıyrılıyorsun, yanan dalların altından geçiyor, kıvılcımların arasından kaçıyorsun.

Ayakların yere daha sağlam basıyor.
Vücudun hâlâ acıyor ama seni tutan bir yük yok artık.

Kısa süre sonra alevler arkanda kalıyor. 
Orman hâlâ yanıyor ama sen yanmıyorsun.

Zırhsız çıktın.
Hayattasın.

Ama geride bıraktığın şey sadece metal değil.
Geçmişine dair ilk iz de alevlerin içinde kaldı

Ormandan kaçtıktan bir süre sonra artık kişisel ihtiyaçlarını fark etmeye başladın.
O andaki adrenalin düzeyi ile fark etmemiş olabilirsin ancak şuan dikkat edilmeyecek seviyede değiller
Karnın acıkmaya başlıyor, ne yapacağını bilmeden boş bir arazinin üzerinde yürürken bir tepeye varıyorsun
Tepe demek yalan olur maksimum 150 metrelik bir dağ.
Tepenin etrafında adeta bir patika açılmış 
Şuanki yorgun halinle tepeye çıkmaya çalışmayı mı istersin yoksa patikayı takip etmek mi istersin?""")
    while True:
        print("""
1) Tepeye tırman
2) Patikayı takip et
        """)
        secim2 = input("Seçimin: ").strip()
        if secim2 == "1":
            zar = random.randint(1, 24)
            toplam = zar + guc
            print(f"\nZar: {zar} | Güç: {guc} | Toplam: {toplam}")
            if toplam >= 18:
                return "tırmanma_basarili", saglik, hiz, guc, zirh, ceviklik
            else:
                return "tırmanma_basarisiz", saglik, hiz, guc, zirh, ceviklik
        elif secim2 == "2":
            return "patika", saglik, hiz, guc, zirh, ceviklik
        else:
            print("Geçersiz seçim, tekrar dene.")





def agir_kacis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
Zırhın tokaları yerinden oynamıyor.
Ellerin titriyor, metal kızgın. 
Her dokunuşta canın biraz daha yanıyor. 
Zamanın yok. 
Alevler yaklaşıyor, duman görüşünü kapatıyor. 
Bir hamle daha yapıyorsun… ama zırh seni bırakmıyor.

Dişlerini sıkıp koşmaya başlıyorsun.

Her adımda ağırlık seni yere çekiyor. 
Zırh hareketlerini kısıtlıyor, nefesin kısa ve kesik. 
Yanan dallar önüne düşüyor, kıvılcımlar zırhına çarpıp sönüyor. 
Omuzların yanıyor, sırtından ter değil, acı akıyor.

Bir an durup soluklanmak istiyorsun.
Ama durursan, burada kalacağını biliyorsun.

Zorlukla da olsa alevlerin arasından çıkmayı başarıyorsun. 
Orman arkanda kalıyor, duman yavaş yavaş dağılıyor. Ayaktasın. Yaşıyorsun.

Ama bedelsiz değil {nick}

Zırh hâlâ üzerinde.
O derece canın yandı ki biraz sağlık kaybetmeye başladın

Bu zırh, seni bir süre daha yavaşlatacak.
Oyun boyunca geçerli sağlığınızdan 1 kaybettiniz
Oyun boyunca geçerli hzınızdan 1 kaybettiniz

Ormandan kaçtıktan bir süre sonra artık kişisel ihtiyaçlarını fark etmeye başladın.
O andaki adrenalin düzeyi ile fark etmemiş olabilirsin ancak şuan dikkat edilmeyecek seviyede değiller
Karnın acıkmaya başlıyor, ne yapacağını bilmeden boş bir arazinin üzerinde yürürken bir tepeye varıyorsun
Tepe demek yalan olur maksimum 150 metrelik bir dağ.
Tepenin etrafında adeta bir patika açılmış 
Şuanki yorgun halinle tepeye çıkmaya çalışmayı mı istersin yoksa patikayı takip etmek mi istersin?""")
    saglik -= 1
    hiz -= 3
    zirh += 10
    print(f"Yeni sağlığın: {saglik}")
    print(f"Yeni hızın: {hiz}")
    print(f"Yeni zırhın: {zirh}")
    while True:
        print("""
    1) Tepeye tırman
    2) Patikayı takip et
            """)
        secim2 = input("Seçimin: ").strip()
        if secim2 == "1":
            zar = random.randint(1, 24)
            toplam = zar + guc
            print(f"\nZar: {zar} | Güç: {guc} | Toplam: {toplam}")
            if toplam >= 18:
                return "tırmanma_basarili", saglik, hiz, guc, zirh, ceviklik
            else:
                return "tırmanma_basarisiz", saglik, hiz, guc, zirh, ceviklik
        elif secim2 == "2":
            return "patika", saglik, hiz, guc, zirh, ceviklik
        else:
            print("Geçersiz seçim, tekrar dene.")








def panik_kacis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
{nick} Alevlerin arasından koşmaya başlıyorsun.
Zırh her adımda seni aşağı çekiyor. 
Omuzlarında bir ağırlık, göğsünde boğucu bir sıcaklık var. 
Metal kızgın; sanki ateşi doğrudan tenine taşıyor. 
Nefesin düzensiz, ciğerlerin dumanla dolu ama durmuyorsun.

Yanan dallar önüne düşüyor, kıvılcımlar etrafında dans ediyor. 
Bir an sendeleyip dizlerinin üzerine düşüyorsun. 
Zırhın çıkardığı metal sesi ormanda yankılanıyor. 
Ayağa kalkmak zor geliyor ama içindeki kaçma dürtüsü seni tekrar kaldırıyor.

Her adım bir işkence.
Her saniye biraz daha yavaşlıyorsun.

Sonunda alevlerin seyrekleştiği bir noktaya ulaşıyorsun. 
Arkana baktığında orman hâlâ yanıyor. 
Sen ise ayakta kalmışsın ama bedeli ağır.

Zırhla kaçtın.
Hayattasın.
Ama gücünden çok şey kaybettin ve bu zırh, bir süre daha seninle kalacak.
Oyun boyunca geçerli gücünüzden 1 kaybettiniz
Oyun boyunca geçerli hızınızdan 1 kaybettiniz

Ormandan kaçtıktan bir süre sonra artık kişisel ihtiyaçlarını fark etmeye başladın.
O andaki adrenalin düzeyi ile fark etmemiş olabilirsin ancak şuan dikkat edilmeyecek seviyede değiller
Karnın acıkmaya başlıyor, ne yapacağını bilmeden boş bir arazinin üzerinde yürürken bir tepeye varıyorsun
Tepe demek yalan olur maksimum 150 metrelik bir dağ.
Tepenin etrafında adeta bir patika açılmış 
Şuanki yorgun halinle tepeye çıkmaya çalışmayı mı istersin yoksa patikayı takip etmek mi istersin?""")
    guc-= 1
    hiz-= 3
    zirh += 10
    print(f"Yeni gücün: {guc}")
    print(f"Yeni hızın: {hiz}")
    print(f"Yeni zırhın: {zirh}")
    while True:
        print("""
    1) Tepeye tırman
    2) Patikayı takip et
            """)
        secim2 = input("Seçimin: ").strip()
        if secim2 == "1":
            zar = random.randint(1, 24)
            toplam = zar + guc
            print(f"\nZar: {zar} | Güç: {guc} | Toplam: {toplam}")
            if toplam >= 18:
                return "tırmanma_basarili", saglik, hiz, guc, zirh, ceviklik
            else:
                saglik -= 2
                print(f"Yuvarlanma sırasında can kaybettin! Yeni sağlığın: {saglik}")
                return "tırmanma_basarisiz", saglik, hiz, guc, zirh, ceviklik
        elif secim2 == "2":
            return "patika", saglik, hiz, guc, zirh, ceviklik
        else:
            print("Geçersiz seçim, tekrar dene.")





def orman_uyanis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik):
    stat_goster(saglik, hiz, guc, zirh, ceviklik)
    print(f"""
Gözlerini açtığında keskin bir sıcaklık yüzüne vuruyor {nick}.

Ama bu güneşin sıcaklığı değil,
Bu, ateşin sıcaklığı.

Etrafındaki orman alevler içinde.
Ağaçlar çıtırdayarak yanıyor, duman ciğerlerini yakıyor.
Hava gri, görüş mesafen birkaç adımdan fazla değil.

Bir an durup düşünmeye çalışıyorsun,
Ama zihnin bomboş.

Burada ne işin var?
Asıl soru şu:
Sen kimsin?

Ayağa kalkmaya çalışıyorsun.
Bacakların titriyor ama sonunda sendeleyerek doğruluyorsun.

Üzerinde kanlarla boyanmış bir zırh var.
Kan kimin, neden buradasın, neden zırhlısın,
Hiçbirini bilmiyorsun.

Bildiğin tek şey şu:
Buradan kaçmalısın.

Ama bu zırhla kaçmak,
Pek mümkün görünmüyor.
    """)

    while True:
        print("""
1) Zırhı çıkarmaya çalış
2) Zırhla kaç
        """)
        secim = input("Seçimin: ").strip()
        if secim == "1":
            zar = random.randint(1, 24)
            toplam = zar + guc
            print(f"\nZar: {zar} | Güç: {guc} | Toplam: {toplam}")
            if toplam >= 18:
                return "zirh_cikti"
            else:
                return "zirh_cikmadi"
        elif secim == "2":
            return "zirhla_kacti"
        else:
            print("Geçersiz seçim.")







print ("Öncelikle Katrosa hoşgeldiniz Bay/Bayan ... ")
isim=input("Adınız? ").strip()
print (f"{isim} ,diyarımıza hoşgeldin")

while True :
    soru1= input(f"{isim} rpg veya frp hakkında bir bilginiz var mı? ").lower().strip()
    if soru1 == "var":
        print("O zaman oyunumuza devam edelim")
        break
    elif soru1 == "yok":
       print("""
       Rpg (Role playing game) Rol yapma oyunu. Olayınız rol yapmaktır. Bir memur olabilir veya bir ev kadını olabilir ve hatta bir kertenkele bile olabilirsiniz ayrıca tadı masaüstünde çıkar.
       Frp (Fantasy role playing) Fantastik rol yapma oyunu. Olayınız fantastik bir dünyada rol yapmaktır. Yani günümüzde bir memur veya bir ev kadını olamazsınız. Rol yaptığınız dünya fantastik ve human creativist öğeler taşımalı.""")
       break

print ("""
Oyun temelinde seçeceğiniz karakterler nezlinde devam edecek ve en başta yaptığınız seçimi özel durumlar dışında değiştiremeyeceksiniz. 
Seçeceğimiz karakterde örneğin zeka az olsun ancak kas gücü fazla olsun bu durumda oyun içinde gelen olaylarda kas gücü gerektiren olaylar size fdaha kolay gelirken zeka gerektiren olaylar sizi daha zorlayacaktır
Böyle durumlarda unutmayın ki her zaman üçüncü bir seçenek vardır o ise -Uzak Durmak-
Seçimleriniz dahilinde oyuncunuz ölürse oyunun zorluk derecine bağlı olarak hayata dönme şansınız bulunucak veya bulunmayacak
Soru sormadan çıkmak için q ya basınız""")

sorular = {
    "1": "Oyunda başarmak veya başarmamak neye bağlıdır?",
    "2": "Oyunun hikayesini nasıl öğreneceğim?",
    "3": "Yapacağım seçimler ne kadar önemli?",
    "4": "Oyunu yarıda bırakır ve gidersem ne olur?"
}

while sorular:
    print("\nÖğrenmek istediğin konuyu seç:")
    for key, value in sorular.items():
        print(f"{key}) {value}")
    secim = input("Seçimin: ").strip()
    if secim == "q":
        print("Guide kapatıldı.")
        break
    if secim not in sorular:
        print("Geçersiz seçim, lütfen tekrar dene.")
        continue
    if secim == "1":
        print("""
        Oyun temelinde birçok zar bulunur bunun en temel örneği D&d olarak adlandırdığımız oyundur. 
        Sizin karakterinize oyun boyunca geçerli 24 yüzlü bir zar veririz ve bunun dahilinde verdiğiniz seçimlerin sonucu ve hatta vereceğiniz seçimlere sebep olan sorunları da sebebi bu zar olur 
        Örneğin okçuluk becerinse çok iyi bir elf olduğunuzu varsayalım o zaman bir sorun ile karşılaştığında yapacağınız ok atışı hem zara hem sizin yeteneklerinize bağlıdır 
        Eğer zarda karşınızdakini vurabilmeniz için en az 12 atmanız gerekiyorsa okçuluk beceriniz ve stres drumunuz gibi değişkenler de göz önüne alınarak atacağınız zarın 6 olması bile sizin onu vurmanıza yetebilir""")
    elif secim == "2":
        print("""
        Oyunda bir hikaye istiyorsanız onu gerçekleştiren sizsiniz yani temel olarak herşeyi yapabilecek olan sizsiniz ama sizden önceki hikayeyi ve çevrenizdeki olup bitenleri öğrenme kısmına gelince o tam olarak sizin kontrolünüzde değil 
        Bundan dolayı daha öncesine bilmediğiniz olayları bilmek yine sizin elinizde 
        Oyun gitişatı ile tüm tarihi tek bir kişi ile öğrenmeniz oldukça zor ancak önemli olan hikayelerin size yarayan kısımları""")
    elif secim == "3":
        print("""
        Yapacağınız seçimler oyunun başında kolay vew normal seviyede iseniz sizi korumak amaçlı biraz daha basit ilerleyecek ama tehlikeye atılmak istediğiniz zaman sizi durduran yok
        Unutmayın her seçim sizi farklı yola sokabildiği gibi hiçbir işe de yaramayabilir o yüzden herkese inanmayın""")
    elif secim == "4":
        print("Oyunda save aldığınız takdirde oyun kayıt olur ve başka zaman girdiğinizde oyuna kaldığınız yerden devam edebilirsiniz")
    del sorular[secim]
print("\nTüm sorular tamamlandı.")

soru2= input(""" 
Oyuna başlama vakti! 
Hangi ırkla oynamak istersin? 
    "1": "İnsan":"
    "2": "Elf": ",
    "3": "Cüce": ",
    "4": "Org": "
     Seçiminiz=  """)

if soru2 == "1":
    print("Bir insan olarak oynamayı seçtiniz.")
    nick = input("Oyundaki nickiniz ne olsun? ").strip()
    guc = 20
    saglik= 20
    hiz= 10
    ceviklik= 7
    zirh= 0
    sonuc2 = None
    zirhli = False
    sonuc_tirmanma = None
    print("\n-OYUN BAŞLIYOR-")
    for i in range(3, 0, -1):
        print(i, flush=True)
        time.sleep(1)
    sonuc_orman = orman_uyanis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik)
    if sonuc_orman == "zirh_cikti":
        sonuc2, saglik, hiz, guc, zirh, ceviklik = hafif_kacis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik)
        zirhli = False
    elif sonuc_orman == "zirh_cikmadi":
        sonuc2, saglik, hiz, guc, zirh, ceviklik = agir_kacis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik)
        zirhli = True

    elif sonuc_orman == "zirhla_kacti":
        sonuc2, saglik, hiz, guc, zirh, ceviklik = panik_kacis_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik)
        zirhli = True

    if sonuc2 is None:
        print("Kaçış sonucu belirlenemedi.")
    else:
        if sonuc2 == "tırmanma_basarili":
            if zirhli:
                sonuc_tirmanma, saglik, hiz, guc, zirh, ceviklik = tirmanma_sahnesi_zirh(
                    nick, saglik, hiz, guc, zirh, ceviklik
                )
            else:
                sonuc_tirmanma, saglik, hiz, guc, zirh, ceviklik = tirmanma_sahnesi(
                    nick, saglik, hiz, guc, zirh, ceviklik
                )
        elif sonuc2 == "tırmanma_basarisiz":
            if zirhli:
                saglik, hiz, guc, zirh, ceviklik = dusme_sahnesi_zirh(
                    nick, saglik, hiz, guc, zirh, ceviklik
                )
            else:
                saglik, hiz, guc, zirh, ceviklik = dusme_sahnesi(
                    nick, saglik, hiz, guc, zirh, ceviklik
                )
        elif sonuc2 == "patika":
            if zirhli:
                saglik, hiz, guc, zirh, ceviklik = patika_sahnesi_zirh(
                    nick, saglik, hiz, guc, zirh, ceviklik
                )
            else:
                saglik, hiz, guc, zirh, ceviklik = patika_sahnesi(
                    nick, saglik, hiz, guc, zirh, ceviklik
                )

    if sonuc_tirmanma == "atese_dogru":
        if zirhli:
            atese_dogru_sahnesi_zirh(nick, saglik, hiz, guc, zirh, ceviklik)
        else:
            atese_dogru_sahnesi(nick, saglik, hiz, guc, zirh, ceviklik)

    elif sonuc_tirmanma == "patika":
        if zirhli:
            patika_sahnesi_2_zirh(nick, saglik, hiz, guc, zirh, ceviklik)
        else:
            patika_sahnesi_2(nick, saglik, hiz, guc, zirh, ceviklik)



elif soru2== "2":
    print("Bir elf olarak oynamayı seçtiyseniz hikayeye buradn devam ediyorum, Oyundaki nickiniz ne olsun efendim (insanların size hitabı)")
    nick=input("Oyundaki nickiniz ne olsun? ").strip()
    guc=5
    saglik= 12
    hiz= 12
    ceviklik= 10
    zirh= 0
    print ("-OYUN BAŞLIYOR-")
    for i in range(3, 0, -1):
      print(i, flush=True)
      time.sleep(1)
    sonuc = elf_baslangic_sahnesi(nick, ceviklik)
    if sonuc == "toplandi":
        print("Bir sonraki elf sahnesi")
    elif sonuc == "ustalik":
        print("Ustalık yolu açıldı")
    elif sonuc == "iskaladi":
        print("Disiplin cezası sahnesi") #BURADA SONUC EKLEYECEĞİM 3 ÖNCÜLEDE

elif soru2== "3":
    print("Bir cüce olarak oynamayı seçtiyseniz hikayeye buradn devam ediyorum, Oyundaki nickiniz ne olsun efendim (insanların size hitabı)")
    nick=input("Oyundaki nickiniz ne olsun? ").strip()
    guc=8
    saglik= 15
    hiz= 6
    ceviklik= 5
    zirh= 0
    print ("-OYUN BAŞLIYOR-")
    for i in range(3, 0, -1):
      print(i, flush=True)
      time.sleep(1)

elif soru2== "4":
    print("Bir org olarak oynamayı seçtiyseniz hikayeye buradn devam ediyorum, Oyundaki nickiniz ne olsun efendim (insanların size hitabı)")
    nick=input("Oyundaki nickiniz ne olsun? ").strip()
    guc=10
    saglik= 25
    hiz=4
    ceviklik= 4
    zirh= 0
    print ("-OYUN BAŞLIYOR-")
    for i in range(3, 0, -1):
       print(i, flush=True)
       time.sleep(1)
print("\n==============================")
print("     DEMO SÜRÜMÜ SONA ERDİ")
print("==============================\n")

for i in range(10, 0, -1):
    print(f"Oyun {i} saniye sonra kapanacak...")
    time.sleep(1)

exit()
# BİRKAÇ SAHNE DAHA GETİR
# TÜM CEVAPLARDAN SONRA KULLANICIYA STATLARI GÖSTER
# TÜM KARAKTERLERE TÜM STATLARI GETİR
# STATS HESAPLAMASI VE ZAR SİSTEMİNİ DÜZENLE
# ACTİVE VE PASSİVE SİSTEMİ GETİR
# SAVE SİSTEMİ GETİR



