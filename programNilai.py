nilai = int(input("Masukkan nilai anda: "))
grade = ""
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"
print("Grade: ", grade)
print("Terima kasih sudah menggunakan aplikasi ini")
