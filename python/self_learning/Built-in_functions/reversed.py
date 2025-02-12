sayilar = [1, 2, 3, 4, 5]

# Dizinin elemanlarını tersine çevir
ters_sayilar = list(reversed(sayilar))

print(ters_sayilar)


# real world example 

# Kullanıcının en son ziyaret ettiği sayfalar
sayfalar = ["sayfa1.html", "sayfa2.html", "sayfa3.html"]

# Sayfaları tersine çevir
ters_sayfalar = list(reversed(sayfalar))

# Tersine çevrilmiş sayfaları yazdır
for sayfa in ters_sayfalar:
  print(sayfa)


# cybersecurity example 

# Saldırganın oluşturduğu şifre listesi
sifre_listesi = ["123456", "password", "qwerty", "abc123"]

# Şifre listesini tersine çevir
ters_sifre_listesi = list(reversed(sifre_listesi))

# Tersine çevrilmiş şifre listesi ile kullanıcının girdiği şifreyi karşılaştır
kullanici_sifresi = input("Lütfen bir şifre girin: ")

if kullanici_sifresi in ters_sifre_listesi:
  print("Geçersiz şifre. Lütfen başka bir şifre girin.")
 
else:
  print("Şifreniz başarıyla doğrulandı.")

# while true ekleyeceğim.
