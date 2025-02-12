from cryptography.fernet import Fernet
import os

# Dosya yolunu oluştur
file_name = "secretkey"
file_path = os.path.join("/home/developer/Documents/Code/python", "keys", file_name)

# Anahtar dosyasını oku
with open("secretkey.txt", "rb") as key_file:
    key = key_file.read()

# Dosyayı şifrele
with open("secretkey.txt", "rb") as input_file:
    input_data = input_file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(input_data)

# Şifrelenmiş dosyayı kaydet
with open("secretkey.txt.encrypted", "wb") as output_file:
    output_file.write(encrypted_data)
