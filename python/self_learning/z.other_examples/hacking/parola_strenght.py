import random
import string

# Parolanın doğru tahmin edilmesi için gereken iterasyon sayısı
ITERATION_COUNT = 10000

# Kullanıcıdan parola alın
password = input("Lütfen parolanızı girin: ")
int_password = int(password)
# Parolanın doğru tahmin edilmesi için gereken iterasyonlar
for i in range(ITERATION_COUNT):
  # Rastgele bir parola oluştur
  guess = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  int_guess = int(guess)  
  # Parolayı doğru tahmin edildi mi?
  password_correct = True
  for j in range(len(guess)):
    if int_guess[j] != password[j]:
      password_correct = False
      break

  # Eğer parola doğru tahmin edildi, döngüden çık
  if password_correct:
    print("this is your password= ", int_guess)
    break
