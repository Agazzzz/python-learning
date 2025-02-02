ulangi = input("Apakah anda ingin mengulanginya lagi? (yes/no) : ")
print("Start")
counter = 0

while ulangi == "yes":
    counter += 1
    print("Perulangan ke " + str(counter))
    ulangi = input("Apakah anda ingin mengulanginya lagi? (yes/no) : ")
print("Selesai")
print("Terima kasih sudah menggunakan aplikasi ini")