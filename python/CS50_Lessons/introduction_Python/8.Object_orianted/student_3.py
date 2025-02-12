import sys

class Student:
    # we can use self or cls to refer to the current class # mevcut sınıfa atıfta bulunmak için self veya cls kullanabiliriz
    def __init__(self, name, house, patronus): # if you want to house optional -> house=None
        self.name = name                       # or you can use empty value like this -> self.name = ""
        self.house = house
        self.patronus = patronus        
        """
        if name blank
        if not name: # if name == "" but it's not good looking
            #sys.exit("Missing name")
            raise ValueError("Missing name")
            I don't need this house value eror anymore because I created setter.
        if house not in ["Gly", "Sly", "Gry", "Ravenclaw"]:
            raise ValueError("Invalid house")
        """                
    def __str__(self):
        """ 
        Python call this when some other function 
        wants to see your object as a string.
        """
        return f"{self.name} from {self.house} patronus is {self.patronus}"

    def charm(self):
        if self.patronus == "Stag":            
            return "horse"
        # ?, It's return dog when giving empty patronus input...
        elif self.patronus == "Terrier":
            return "dog"
        elif self.patronus == "Stick":
            return "stick"
        else:
            return "unknown"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        # It's firstly sending user here when user want to set house.
        if house not in ["Gly", "Sly", "Gry", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house # we add underscore because we have named house functions



# This function is used to get the name and house of a student from the user
def get_student():    
    name = input("Name: ").title()
    house = input("House: ").title()  
    patronus = input("Patronus: ").title()
    student = Student(name, house, patronus)  
    try:  
        return student
    except ValueError as e:
        print(e)
        ...

# This function is the main function of the program
def main():
    # Call the get_student function to get the student information
    student = get_student()
    # This when programmer want to set variable but we created setter and python gonna start setter to do that if setter allow this
    #student.house = "Privet Drive" # setter gonna give error for this because house privet drive not in the list on setter
    # 1 underscore -> don't touch this 2 underscore(dunder) -> really don't touch this
    student._house = "Privet drive" # ? setter don't check this but ...
    
    # Print out the name and house of the student using string formatting
    #print(f"{student.name} from {student.house}")
    print(student)
    print(student.charm())

# This block is used to check if the code is being run as the main program or if it is being imported as a module into another program
if __name__ == "__main__":
    # If the code is being run as the main program, call the main function
    main()
