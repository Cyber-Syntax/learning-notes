# Pow() fonksiyonunu kullanarak bir sayının karesini bulun

# Öncelikle sayıyı tanımlayalım
number = 3

# Sayının karesini hesaplayalım
square = pow(number, 2)

# Karesini ekrana yazdıralım
print(square)

# Calculate the electricity bill for a certain number of kilowatt-hours

def calculate_electricity_bill(kwh):
    base_charge = pow(10, -2) # 10^-2 , 10 üzeri -2
    kwh_charge = 0.12
    bill = base_charge + (kwh * kwh_charge)
    return bill

# Calculate the bill for a customer who used 500 kwh
bill = calculate_electricity_bill(1000)
print(bill)

