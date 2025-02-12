sayi = 5
metin = "merhaba"

print(repr(sayi))
print(repr(metin))

# repr kullanıldığında string ve int gibi nesneleri bilir ve anlaşılır bir şekilde yaz..
# 5 
# "merhaba"

# repr kullanılmadığında
# 5
# merhaba



# realworld example 

import sqlite3

# Veritabanına bağlan
veritabani = sqlite3.connect("ornek.db")
imlec = veritabani.cursor()

# Veritabanından kayıtları oku
imlec.execute("SELECT * FROM kayitlar")
kayitlar = imlec.fetchall()

# Dosyayı aç ve kayıtları yazdır
with open("kayitlar.txt", "w") as dosya:
  for kayit in kayitlar:
    dosya.write(repr(kayit))
    dosya.write("\n")
