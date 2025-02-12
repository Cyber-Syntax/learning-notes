# İlk olarak, gerekli olan kütüphaneleri import edin
import datetime

# Doğum günü bilgilerini belirleyin
isim = "Ahmet"
dogum_tarihi = datetime.date(1998, 12, 13)
simdiki_tarih = (2022, 12, 13)

# Şu anki tarihi alın
simdiki_tarih = datetime.date.today()

# Doğum günü kutlama mesajını hazırlayın
mesaj = "{} adlı kişinin doğum günü {}! Mutlu yıllar!".format(isim, dogum_tarihi.strftime("%d.%m.%Y"))

# Eğer şu anki tarih doğum gününe eşitse, mesajı yazdırın
if simdiki_tarih == dogum_tarihi:
  print(mesaj)
else:
    print("error")


# Another example with e-mail

import time
import smtplib

# Get the current date and time
current_time = time.localtime()

# Check if the current date is the person's birthday
if current_time.tm_mon == 4 and current_time.tm_mday == 15:
  # Connect to the SMTP server
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("your_email@gmail.com", "your_password")

  # Send the birthday message
  message = "Subject: Happy Birthday!\n\nHappy birthday, dear friend! Hope you have a great day!"
  server.sendmail("your_email@gmail.com", "friend's_email@gmail.com", message)

  # Disconnect from the SMTP server
  server.quit()
