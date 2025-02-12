sentence = "The quick brown fox jumps over the lazy dog."

# find the index of the first occurrence of the substring 'fox'
index = sentence.index('fox')

print(index)  # prints 16

try:
  index = sentence.index('cat')
except ValueError:
  print("Substring not found")

# Another example 


animals = ['fox', 'dog', 'cat', 'rabbit']
sentence = "The quick brown cat jumps over the lazy dog."

for animal in animals:
  try:
    index = sentence.index(animal)
    print(f"Found {animal} at index {index}")
    break
  except ValueError:
    print("Substring not found")
    pass

# prints 'Found fox at index 16'


# Define lists of products and prices
products = ['apple', 'banana', 'cherry', 'orange']
prices = [0.5, 0.25, 0.75, 0.6]


# Get the index of the product in the list of products
#input("Search product for price: ", product) # WRONG
product = input("Enter the product you want to search for: ")
index = products.index(product)

# Use the index to retrieve the price of the product from the list of prices
# Fiyat listesinden ürünün fiyatını almak için dizini kullanın
price = prices[index]

# Print the price
print(price)

