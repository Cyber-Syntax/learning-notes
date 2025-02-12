# Ancak unutmayın ki, bu fonksiyon genellikle kodunuzda globals() fonksiyonunu 
# kullanmak için bir neden yoktur ve bu fonksiyonun kullanımı genellikle yanlış 
# kod yazımına yol açar.


# Global değişken
x = "global"

def my_function():
  # globals() fonksiyonunu kullanma
  print(globals()["x"])

my_function()  # "global"


# Another example:

