while True:
    print("\n1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Çıkış")

    secim = input("Seçim: ")

    if secim == "5":
        break

    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))

    if secim == "1":
        print("Sonuç:", a + b)
    elif secim == "2":
        print("Sonuç:", a - b)
    elif secim == "3":
        print("Sonuç:", a * b)
    elif secim == "4":
        print("Sonuç:", a / b)
