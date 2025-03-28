import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?><:-="
User = int(input("Masukkan panjang kata sandi:"))
Generasi_Password = ""

for i in range(User):
    Generasi_Password += random.choice(password)

print("Ini adalah kata sandi yang dihasilkan :", Generasi_Password)
