tasks = []

while True:
    print("\n1- Görev ekle")
    print("2- Görevleri göster")
    print("3- Görev sil")
    print("4- Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        gorev = input("Görev: ")
        tasks.append(gorev)
        print("Eklendi!")

    elif secim == "2":
        for i, t in enumerate(tasks):
            print(i+1, t)

    elif secim == "3":
        print(tasks)
        sil = int(input("Silinecek numara: "))
        tasks.pop(sil-1)

    elif secim == "4":
        break
