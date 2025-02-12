# Convert a number to a hexadecimal string
number = 255
hex_string = hex(number)
print(hex_string)  # Output: 0xff


# Another example 

# Örnek kullanım
ip_address = "192.168.0.1"
ip_address_in_hex = hex(int(ip_address.replace(".", "")))
print(ip_address_in_hex)  # Bu ekrana '0xC0A80001' yazdırır
