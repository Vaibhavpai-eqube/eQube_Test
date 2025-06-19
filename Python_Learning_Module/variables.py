"""
IN python variables are not net of which type they can be written directly,
and they even changed type during the execution of the program.
you can know tyle of data stored in a variable using type() function.
"""
x = 5
y = "Hello, World!"
print(x, "is of type", type(x))
print(y, "is of type", type(y))
x ="eQube"
print(x, "is of type", type(x))

# case sensitive variables
a = 10
A = "eQube"
print(a, "is of type", type(a))
print(A, "is of type", type(A))

"""
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
# legal varibles
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(type(myvar))
print(type(my_var))
print(type(_my_var))
print(type(myVar))
print(type(MYVAR))
print(type(myvar2))

# multiline variables
name1, name2, name3 = "John", "Doe", "Smith"
print(name1)
print(name2)
print(name3)
# multi-value equal variable
first_name = middle_name = last_name = "John"
print(first_name)
print(middle_name)
print(last_name)

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc.
Python allows you to extract the values into variables.
This is called unpacking.
"""
name = ("John", "Doe", "Smith")
x,y,z = name;
print(x)
print(y)
print(z)

# variable scope
popu = "jana"
def people():
    # declaring 'global' variable inside a function
    global mind
    mind = "mana"
    print("Calling from people(): " + popu)
    print("calling global keyword from inside of func people(): " + mind)
people()
print("calling from outside of function: " + popu)
print("calling global keyword from outside of func people(): " + mind)
exit()