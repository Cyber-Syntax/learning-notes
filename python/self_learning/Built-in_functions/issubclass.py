class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


class Tiger(Cat):
    def __init__(self, name, color, stripe_pattern):
        super().__init__(name, color)
        self.stripe_pattern = stripe_pattern


# Check if Cat is a subclass of Animal
print(issubclass(Cat, Animal))  # Output: True

# Check if Tiger is a subclass of Cat
print(issubclass(Tiger, Cat))  # Output: True

# Check if Animal is a subclass of Cat
print(issubclass(Animal, Cat))  # Output: False


# Another example

class MyParentClass:
  # Tanımlamalar...


class MyChildClass(MyParentClass):
  # Tanımlamalar...


    # issubclass() fonksiyonunu kullanarak MyChildClass sınıfının MyParentClass sınıfının alt sınıfı olup olmadığını kontrol edin
is_subclass = issubclass(MyChildClass, MyParentClass)

# Eğer MyChildClass MyParentClass sınıfının alt sınıfıysa ekrana "MyChildClass is a subclass of MyParentClass" yazdırın
if is_subclass:
    print("MyChildClass is a subclass of MyParentClass")
