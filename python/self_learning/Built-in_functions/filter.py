#  filter() fonksiyonunun kullanımı sadece filtreleme işlemini 
# gerçekleştirmek için değil, aynı zamanda filtrelenmiş elemanları 
# saklamak ve daha sonraki işlemlerde kullanmak için de kullanışlıdır.


# Bir sayı listesi tanımlayın
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bir sayının tek olup olmadığını kontrol eden bir fonksiyon tanımlayın
def is_odd(x):
    return x % 2 != 0

# filter() fonksiyonunu kullanarak tüm çift sayıları filtreleyin
odd_numbers = filter(is_odd, numbers)

# Tek sayılar listesini yazdırın
print(list(odd_numbers))


# Another example:

# Bir dize listesi tanımlayın
strings = ["hello", "world", "python", "programming", "openai"]

# Bir dizenin belirli bir uzunlukta olup olmadığını kontrol eden bir fonksiyon tanımlayın
def is_length(x, length):
    return len(x) == length

# filter() fonksiyonunu kullanarak belirli bir uzunlukta olan dizeleri filtreleyin
length_5_strings = filter(is_length, strings, 5)

# Filtrelenen dizeleri yazdırın
print(list(length_5_strings))
