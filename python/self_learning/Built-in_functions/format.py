# Suppose you are building a program that generates reports from data stored in 
# a database. The data includes dates, and you want to display the dates in a 
# human-readable format (e.g., "January 1, 2021") in the reports. 
# Here is how you could use the format() function to format dates in the reports:


# Define a date in the database
date = "2021-01-01"

# Use the format() function to format the date in a human-readable way
formatted_date = date.format("{}-{}-{}", "{month} {day}, {year}")

# Print the formatted date
print("Formatted date:", formatted_date)


# Another example
# Örneğin, bir hesap makinesi programı geliştiriyorsunuz. 
# Program, kullanıcıdan alınan sayıları ekrana yazdırır ve 
# bu sayıların ondalıklı kısımları varsa, ondalık kısmını belirtmek 
# için nokta kullanır. Ancak, bazı ülkelerde ondalık kısımlar için virgül kullanılır. 
# Bu nedenle, programın ondalık kısımlar için virgül kullanarak ekrana 
# gerekir. İşte format() fonksiyonunu bu amaçla nasıl kullanabilirsiniz: 

# Kullanıcıdan bir sayı alın
number = input("Enter a number: ")

# Sayıyı ondalıklı sayıya dönüştürün
number = float(number)

# format() fonksiyonunu kullanarak sayıyı virgülle ayrılmış bir biçimde yazdırın
formatted_number = "{:,.2f}".format(number)

# Biçimlendirilmiş sayıyı yazdırın
print("Formatted number:", formatted_number)

