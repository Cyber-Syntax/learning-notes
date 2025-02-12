def main():
    #name = get_name()
    #house = get_house()
    #name, house = get_student()
    #print(f"{name} from {house}")
    
    # returning tuple
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()    
    #return name, house
    return [name, house] # mutable = that's mean changable


# def get_name():
#     return input("Name: ")
#     #return name

# def get_house():
#     return input("House: ")


if __name__ == "__main__":
    main()