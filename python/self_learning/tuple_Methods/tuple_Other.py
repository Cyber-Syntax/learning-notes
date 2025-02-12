# Python Tuple Methods example for beginners

# Creating a Tuple 
Tuple1 = ('Python', 'Programming', 'Tutorial') 
print("Tuple1 = ", Tuple1) 

# Access Tuple Items 
print("\nTuple1[1] = ", Tuple1[1]) 

# Tuple Length 
print("\nLength of Tuple1 = ", len(Tuple1)) 

# Concatenating Tuples 
Tuple2 = (1, 2, 3, 4) 
print("\nTuple2 = ", Tuple2) 

# Concatenating two tuples 
Tuple3 = Tuple1 + Tuple2 
print("\nNew Tuple = ", Tuple3) 

# Repetition Operator 
Tuple4 = Tuple2 * 3
print("\nTuple4 = ", Tuple4) 

# Membership Operator 
print("\n3 in Tuple2 = ", (3 in Tuple2)) 

# Iterating through a Tuple 
for x in Tuple4: 
    print(x) 
    
# Deleting a Tuple 
del Tuple4 
print(Tuple4) # This will raise an error because Tuple4 is deleted