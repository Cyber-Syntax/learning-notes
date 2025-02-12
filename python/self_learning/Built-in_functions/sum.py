# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the sum() function to calculate the sum of the numbers in the list
total = sum(numbers)

# Print the result
print(total)


# real world 

books = [
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "pages": 224
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "pages": 208
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "pages": 277
    }
]

# Use a list comprehension to extract the number of pages from each book
page_counts = [book["pages"] for book in books]

# Use the sum() function to calculate the total number of pages
total_pages = sum(page_counts)

# Print the result
print(total_pages)
