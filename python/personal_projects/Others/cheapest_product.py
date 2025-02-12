# Define a list of products and their prices from your shop's webpages
products = [
  {'name': 'Echo Dot', 'price': 39.99},
  {'name': 'Fire TV Stick', 'price': 29.99},
  {'name': 'Kindle Paperwhite', 'price': 119.99},
  {'name': 'Echo Show', 'price': 179.99}
]

# Define the name of the product you want to find the cheapest price for
product_name = 'Echo Dot'

# Use a for loop to iterate through the list of products
cheapest_price = float('inf')
for product in products:
  # Check if the current product is the one you want to find the cheapest price for
  if product['name'] == product_name:
    # Use the min() function to find the cheapest price for the product
    cheapest_price = min(cheapest_price, product['price'])

# Display the cheapest price for the product
print("The cheapest price for the " + product_name + " is: " + str(cheapest_price))
