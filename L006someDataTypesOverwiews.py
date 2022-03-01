# -----------------------------
# type() datanın tipini döndürür
# All Data in python is Object
# ------------------------------

print(10)
print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(10.9))  # float => Floating Point Number
print(type(1.455849))  # float => Floating Point Number
print(type(-100.95645))  # float => Floating Point Number

print(type("HEllo Python"))  # dtr => String

# list => List is written within (square) angel brackets, in some languages is Array
print(type([1, 2, 3, 5]))
# In python there is an array but it needs to install a specific module for it
# will be discused later

print(type((1, 2, 3, 4)))  # tuple => Tuple is written within parantheses

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(2 == 2)  # bool => Boolean
print(type(2 == 4))
