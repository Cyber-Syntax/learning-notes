# Kullanıcı adı ve parola bilgilerini tutan bir veritabanı oluşturalım
users = [
    {"username": "johnsmith", "password": "password1"},
    {"username": "janesmith", "password": "password2"},
]

def login(username, password):
  # Kullanıcı adı ve parola bilgilerini kontrol etme
  for user in users:
    if user["username"] == username and user["password"] == password:
      return True
  return False

# Fonksiyonu kullanma
is_logged_in = login("johnsmith", "password1")
if is_logged_in:
  print("Başarıyla giriş yaptınız!")
else:
  print("Hatalı kullanıcı adı veya parola!")
