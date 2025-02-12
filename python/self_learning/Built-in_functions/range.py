# Bir for döngüsünde range() işlevini kullanarak 1'den 10'a kadar sayıları yazdırın
for i in range(1, 11):
    print(i)

# Bu örnekte, range() işlevi bir for döngüsünde kullanılır. range(1, 11) ifadesi,
#  1'den başlayarak 11 dahil olmamak üzere bir dizi oluşturur. Döngü bu dizideki 
# sayıları bir bir alır ve her bir sayı için belirtilen işlemleri 
# (burada yazdırma işlemi) yapar.,

# Another example

urunler = ["ayakkabı", "elbise", "gömlek", "mont", "pantolon"]

for i in range(len(urunler)):
  print(f"{i+1}. ürün: {urunler[i]}")



# Bir restoranda siparişleri yöneten bir program yazın

def place_order(menu, table_number):
    # Sipariş numarasını hesaplayın
    order_number = 1
    for order in orders:
        if order.order_number >= order_number:
            order_number = order.order_number + 1

    # Siparişi oluşturun ve siparişler listesine ekleyin
    order = Order(order_number, table_number, menu)
    orders.append(order)

    # Sipariş numarasını döndürün
    return order_number

# Menüyü oluşturun
menu = [
    MenuItem('Pizza', 10),
    MenuItem('Hamburger', 8),
    MenuItem('Salad', 5),
]

# Siparişler listesini oluşturun
orders = []

# Masa 1 için sipariş verin
table_number = 1
order_number = place_order(menu, table_number)
print(f'Sipariş numarası: {order_number}')



# Range işlevi olamadan for ile range kullanmadan yapılmış bir örnek:
# Bir şirketin çalışanlarının maaşlarının ortalamasını hesaplayın

def calculate_average_salary(employees):
    # Maaşları toplamını hesaplayın
    total_salary = 0
    for employee in employees:
        total_salary += employee.salary

    # Çalışan sayısını hesaplayın
    num_employees = len(employees)

    # Maaşların ortalamasını hesaplayın
    average_salary = total_salary / num_employees
    return average_salary

# Çalışanların listesini oluşturun
employees = [
    Employee('John Doe', 50000),
    Employee('Jane Smith', 60000),
    Employee('Bob Johnson', 75000),
]

# Çalışanların maaş ortalamasını hesaplayın
average_salary = calculate_average_salary(employees)
print(average_salary)
