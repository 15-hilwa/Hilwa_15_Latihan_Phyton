def ganjil_genap():
    while True:
        nilai = int(input("masukkan nilai (0 untuk kembali): "))

        if nilai == 0:
            break

        if nilai % 2 == 0:
            print("nilai", nilai, "adalah bilangan genap")
        else:
            print("nilai", nilai, "adalah bilangan ganjli")
    angka = int(inputan)

    if angka % 2 == 0:
        print(angka, "adalah bilangan genap")
    else:
        print(angka, "adalah bilangan ganjil")
