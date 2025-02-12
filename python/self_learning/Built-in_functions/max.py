# List of items with their corresponding number of sales
items = [('item1', 100), ('item2', 120), ('item3', 180), ('item4', 150)]

# Use the max() function to find the item with the most number of sales
most_popular_item = max(items, key=lambda x: x[1])

# Print the most popular item
print(f'The most popular item is: {most_popular_item[0]}')
