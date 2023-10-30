print("hesap makinesi\n"
      "işlemler\n"
      "(0) çıkmak için\n"
      "(1) toplama\n"
      "(2) çıkarma\n"
      "(3) çarpma\n"
      "(4) bölme\n"
      "(5) üst alma\n")

islem = input("işlem seçiniz: ")


while True:
    if islem =="0":
        print("çıkılıyor...")
        break

    elif islem =="1":
        sayi1=int(input("sayı giriniz:"))
        sayi2= int(input("sayı giriniz: "))
        toplama = sayi1 + sayi2
        print("toplama sonucunuz: " + str(toplama))
        break

    elif islem =="2":
        sayi3 = int(input("sayı giriniz:"))
        sayi4 = int(input("sayı giriniz: "))
        cikarma= sayi3 - sayi4
        print("çıkarma sonucunuz: " + str(cikarma))
        break

    elif islem=="3":
        sayi5 = int(input("sayı giriniz:"))
        sayi6 = int(input("sayı giriniz: "))
        carpma= sayi5*sayi6
        print("çarpma sonucunuz: " + str(carpma))
        break

    elif islem=="4":
        sayi7 = int(input("sayı giriniz:"))
        sayi8 = int(input("sayı giriniz: "))
        bolme= sayi7/sayi8
        print("bölme sonucunuz: " + str(bolme))
        break

    elif islem=="5":
        sayi9 = int(input("taban giriniz:"))
        sayi0 = int(input("üst giriniz: "))
        ust= sayi9**sayi0
        print("sonucunuz: " + str(ust))
        break