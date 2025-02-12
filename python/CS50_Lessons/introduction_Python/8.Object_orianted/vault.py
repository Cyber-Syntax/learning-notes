class Vault:
    # Initialize the Vault with the given number of galleons, sickles, and knuts.
    # If no values are provided, the Vault will be initialized with 0 galleons, 0 sickles, and 0 knuts.
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    # This method returns a string representation of the Vault object.
    # It is called when the object is printed or converted to a string.
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    # This method allows us to add two Vault objects together using the '+' operator.
    # It takes in another Vault object as an argument and returns a new Vault object with the combined amounts.
    def __add__(self, other):
        # Add the galleons, sickles, and knuts of the two Vault objects
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        # Return a new Vault object with the combined amounts
        return Vault(galleons, sickles, knuts)

        
# Create a Vault object with 100 galleons, 50 sickles, and 25 knuts
potter = Vault(100, 50, 25)
# Print the Vault object
print(potter)


# Create a Vault object with 25 galleons, 50 sickles, and 100 knuts
weasley = Vault(25, 50, 100)
# Print the Vault object
print(weasley)


# Add the two Vault objects together and store the result in a new variable
total = potter + weasley
# Print the combined Vault object
print(total)
