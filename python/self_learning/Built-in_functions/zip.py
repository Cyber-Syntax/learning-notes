names = ["John", "Jane", "Joe", "Jill"]
scores = [90, 80, 85, 95]

students = {name: score for name, score in zip(names, scores)}
print(students)  # Output: {'John': 90, 'Jane': 80, 'Joe': 85, 'Jill': 95}

# Another example 

words1 = ["Hello", "world", "Python"]
words2 = ["Beautiful", "is", "fun"]

new_words = [w1 + " " + w2 for w1, w2 in zip(words1, words2)]
print(new_words)  # Output: ['Hello Beautiful', 'world is', 'Python fun']

