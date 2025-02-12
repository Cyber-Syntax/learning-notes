# Bir siber güvenlik programında id fonksiyonu bir kullanıcının oturum 
# kimliğini (session ID) belirlemek için kullanılabilir. Örneğin, bir 
# kullanıcı giriş yaptıktan sonra oturum kimliğini belirleyip bu kimliği 
# bir değişkende saklayabiliriz. Daha sonra kullanıcının yaptığı 
# istekleri bu değişkende saklanan oturum kimliğine göre izleyebiliriz.

# Kullanıcı girişi yaptıktan sonra oturum kimliğini belirleyip bir değişkende saklayalım
user_id = 12345
session_id = id(user_id)

# Kullanıcının yaptığı istekleri izleyebilmek için bir sözlük oluşturalım
request_tracker = {}

# Kullanıcı bir istekte bulununca bu isteği sözlüğe ekleyelim
request_tracker[session_id]
# need other codes 
# here:
# ....

# Another example

x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)

# This value is the memory address of the object and will be 
# different every time you run the program