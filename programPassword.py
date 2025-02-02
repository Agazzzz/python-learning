#import modul
from getpass import getpass
password = getpass("Enter your password: ")
valid_password = "password"

#logic
if password == valid_password:
    print("Selamat datang Boss!")
else:
    print("Password salah, coba lagi!") 
    
print("Terima kasih sudah menggunakan aplikasi ini")