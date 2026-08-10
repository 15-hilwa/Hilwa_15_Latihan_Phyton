nilai = int(input("Masukkan nilai: "))

if nilai % 2 == 0:
    print("Nilai", nilai, "adalah bilangan genap")
else:
    print("Nilai", nilai, "adalah bilangan ganjil")
while True:
    inputan = input("Masukkan bilangan (tekan 'q' untuk keluar): ") 

    if inputan.lower() == "q":
        print("Program dihentikan.")
        break

    angka = int(inputan)

    if angka % 2 == 0:
        print(angka, "adalah bilangan genap")
    else:
        print(angka, "adalah bilangan ganjil")