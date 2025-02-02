def kali(a, b):
    hasil_kali = a * b
    print("Hasil kali: " + str(hasil_kali))
    return hasil_kali

c = kali(5, 3)  #output: 15
d = kali(10, 2)  #output: 20
e = kali(7, 8)  #output: 56

def kurang(a, b):
    hasil_bagi = a / b
    return hasil_bagi
hasilKurang = kurang(c, d)  #output: 0.75
print(hasilKurang)