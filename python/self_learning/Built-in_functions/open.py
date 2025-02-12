# Open() fonksiyonunu kullanarak bir dosyayı okuyun

# Öncelikle open() fonksiyonunu kullanarak dosyayı açalım
# Dosya adı: "my_file.txt"
# Dosya modu: "r" (read/okuma)
f = open("my_file.txt", "r")

# Dosyayı satır satır okuyalım
for line in f:
    # Her satırı ekrana yazdıralım
    print(line)

# Dosyayı kapatalım
f.close()
