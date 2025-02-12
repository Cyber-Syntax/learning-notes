# This function is used to get the name and house of a student from the user
def get_student():
    student = {}
    
    # Ask the user for their name and store it in the dictionary
    student["name"] = input("Name: ").title()
    
    student["house"] = input("House: ").title()
    
    return student

def main():
    student = get_student()
    
    print(f"{student['name']} from {student['house']}")

# This block is used to check if the code is being run as the main program or if it is being imported as a module into another program
if __name__ == "__main__":
    # If the code is being run as the main program, call the main function
    main()
