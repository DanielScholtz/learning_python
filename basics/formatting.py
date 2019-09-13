# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

float_number = 23.0
print("the number is in 4 digits %4f." % float_number)

my_list = [1,2,3]
print("the list data is %s" % my_list)

