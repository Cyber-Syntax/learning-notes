addresses = ['123 Main St', '456 Maple Ave', '789 Oak Dr']

formatted_addresses = [address.replace('St', 'Street').replace('Ave', 'Avenue').replace('Dr', 'Drive') for address in addresses]
print(formatted_addresses)

# Output: ['123 Main Street', '456 Maple Avenue', '789 Oak Drive']