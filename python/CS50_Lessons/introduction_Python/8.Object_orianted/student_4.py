import sys
# TODO, add comment!!
# Define a Student class to store the information of a student
class Student:    
    # Initialize the Student with a name, house, and patronus
    def __init__(self, name, house, patronus):       
        self.name = name         
        self.house = house
        self.patronus = patronus
    
    # This method returns a string representation of the Student object.
    # It is called when the object is printed or converted to a string.
    def __str__(self):
        return f"{self.name} from {self.house} and his/her friend {self.patronus}"

    # This method returns a string based on the value of the patronus attribute.
    # TODO later, this method didn't work anymore. Maybe I can change this to work 
    def patronus(self):
        if self.patronus == "Stag":            
            return "Horse"        
        elif "Terrier":
            return "Dog"
        elif "Yoda":
            return "It's to dangerous to go along. Take him."
        else:
            return "Stick"
    
    # This is a class method that allows us to create a Student object by prompting the user for input.
    @classmethod
    def get(cls):
        name = input("Name: ").title()
        house = input("House: ").title()
        patronus = input("Patronus: ").title()
        return cls(name, house, patronus)
    
    # This is a getter for the name attribute.
    # It is called when we try to access the attribute using dot notation (e.g. student.name).
    @property
    def name(self):
        return self._name

    # This is a setter for the name attribute.
    # It is called when we try to assign a value to the attribute using dot notation (e.g. student.name = "Harry").
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # This is a getter for the house attribute.
    # It is called when we try to access the attribute using dot notation (e.g. student.house).
    # Getter
    @property
    def house(self):
        return self._house

    # This is a setter for the house attribute.
    # It is called when we try to assign a value to the attribute using dot notation (e.g. student.house = "Gryffindor")
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gly", "Sly", "Gry", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house 
    
    @property
    def patronus(self):
        return self._patronus

    @patronus.setter
    def patronus(self, patronus):
        if patronus not in ["Stag", "Terrier", "Yoda"]:
            raise ValueError("Invalid patronus")
        self._patronus = patronus

# This function is the main function of the program
def main():    
    student = Student.get()
    print(student)

# If the script is run directly, run the main function
if __name__ == "__main__":    
    main()
