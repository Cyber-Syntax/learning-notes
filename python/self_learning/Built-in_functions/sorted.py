# Define a list of numbers to sort
numbers = [3, 5, 2, 1, 4]

# Use the sorted() function to sort the list in ascending order(artan düzen)
# decending order need to revers=True
sorted_numbers = sorted(numbers, reverse=True)
# reversed_numbers = reversed(numbers) # WRONG

# Print the sorted list
print(sorted_numbers) # Prints [1, 2, 3, 4, 5]

# Another example:


# Define a list of IP addresses to sort
ip_addresses = ["192.168.1.100", "192.168.1.1", "192.168.1.200", "192.168.1.50"]

# Use the sorted() function to sort the list of IP addresses in ascending order
sorted_ip_addresses = sorted(ip_addresses)

# Print the sorted list of IP addresses
print(sorted_ip_addresses) # Prints ["192.168.1.1", "192.168.1.50", "192.168.1.100", "192.168.1.200"]

