def convert_to_octal(number, base):
    # Convert the number to decimal using the int() function
    decimal_value = int(number, base)
    
    # Convert the decimal value to octal using the oct() function
    octal_value = oct(decimal_value)
    
    # Return the octal value
    return octal_value



octal_value = convert_to_octal('1010', 2)


# Oct() yöntemini kullanarak bir sayıyı octal tabana dönüştürün

# Dönüştürülecek sayıyı tanımlayalım
number = 20

# Sayıyı octal tabana dönüştürelim
octal_number = int(str(number), 8)

# Dönüştürülmüş sayıyı ekrana yazdıralım
print(octal_number)



# Octal tabandaki bir sayıyı dönüştürün

# Dönüştürülecek sayıyı tanımlayalım
number = 35

# Sayıyı string veri türüne dönüştürelim
number_str = str(number)

# String veri türündeki sayıyı octal tabana dönüştürelim
octal_number = int(number_str, 8)

# Dönüştürülmüş sayıyı ekrana yazdıralım
print(octal_number)


