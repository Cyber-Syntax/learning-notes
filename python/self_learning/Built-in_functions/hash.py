import hashlib

password = "my_password"

# Parolayı bir sayıya (hash değeri) dönüştür
password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

# Düşük güçlü parolalar için bir kara liste oluştur
blacklisted_hashes = [
    "098f6bcd4621d373cade4e832627b4f6", # "test"
    "d8578edf8458ce06fbc5bb76a58c5ca4", # "123456"
    "7c4a8d09ca3762af61e59520943dc26494f8941b", # "password"
]

# Parolanın kara listede olup olmadığını kontrol et
if password_hash in blacklisted_hashes:
    print("Lütfen daha güçlü bir parola seçin!")

