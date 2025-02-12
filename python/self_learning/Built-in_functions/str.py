# This is used for int to string variables because python can't write 
# integer age in string sentences.

age = 30
print("I am " + str(age) + " years old.")


# Another example


total_cost = 56.78
print("Your total cost is $" + str(total_cost))
#print("Your total cost is $" + total_cost) # WRONG => print don't know float, int.

# Another example


temperature = 25
print("The temperature is " + str(temperature) + " degrees Celsius.")


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

print("My book collection:\n " + str(books))

