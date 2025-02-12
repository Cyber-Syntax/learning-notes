user_input = input("Lütfen bir sayı girin: ")
# input bizden girileni string olarak aldığı için integar'a çeviriyoruz.
num = int(user_input)

if isinstance(num, int):    
    print("You entered the number " + str(num))
else:
    print("You did not enter a number.")


# Another Example 

numbers = {
    "one": 1,
    "two": 2,
    "three": 3
}

# Sözlükteki tüm anahtarlar ve değerler bir sayı tipinde olmalıdır
if all(isinstance(value, int) for value in numbers.values()):
    # Tüm anahtarlar ve değerler bir sayı tipinde
    # Bu yüzden sözlükteki sayıları toplayabiliriz
    total = sum(numbers.values())
    print("Sözlükteki sayıların toplamı:", total)
else:
    # Sözlükteki bazı anahtarlar veya değerler bir sayı tipinde değil
    print("Sözlükteki bazı anahtarlar veya değerler bir sayı tipinde değil!")

