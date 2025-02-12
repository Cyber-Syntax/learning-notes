# static method sadece myclass da kullanılabilir.

class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # Do something with the arguments
        result = arg1 + arg2
        return result

# Create an instance of the MyClass class
my_instance = MyClass()

# Call the static method on the class
result = MyClass.my_static_method(1, 2)
print(result) # Prints 3

# Call the static method on the instance
result = my_instance.my_static_method(1, 2)
print(result) # Prints 3


# real world example

# static method kullandığımız yerlerde sadece belirttiğimiz class'da kullanılabilir.
# Haliyle user class'da şifre değiştirme güncelleme işlemleri sadece user classda
# gerçekleştirilir.
import hashlib

class User:
    @staticmethod
    def generate_password_hash(password):
        # Use the hashlib library to generate a hashed version of the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def update_password(self, new_password):
        # Generate a hashed version of the new password
        hashed_password = self.generate_password_hash(new_password)

        # Update the user's password in the database
        # ...
# This is for example the addedable for code.
# Create an instance of the User class
user = User()

# Call the update_password() method on the instance
user.update_password("mynewpassword")
