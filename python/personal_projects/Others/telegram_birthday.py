import datetime
import telegram

# Telegram botunuz için gerekli olan API anahtarını buraya girin
api_key = "<TELEGRAM_API_KEY>"

# Botu oluşturun
bot = telegram.Bot(token=api_key)

# Kullanıcıları ve doğum günlerini burada tutacağız
users = {
    "ali": datetime.datetime(2022, 10, 11),
    "ayse": datetime.datetime(2022, 12, 14),
    "ahmet": datetime.datetime(2022, 11, 15),
}

# İşlemleri sürekli tekrarlayan bir döngü oluşturun
while True:
    # Tarihi ve saati alın
    now = datetime.datetime.now()

    # Tüm kullanıcıları gezin
    for username, birthday in users.items():
        # Kullanıcının doğum günü bu ay ve gün mü?
        if now.month == birthday.month and now.day == birthday.day:
            # Eğer evet, kullanıcıya bir doğum günü mesajı gönderin
            bot.send_message(chat_id=username, text="İyi ki doğdun, iyi ki varsın :) Nice senelere!")

    # Her 10 saniyede bir döngüyü tekrarlayın
    time.sleep(10)
