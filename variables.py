print("Hello, world")

# variables and data type in python

name = 'John Doe' # string
age = 25 # integer

my_string_var = "freeCodeCamp" # declare a var of multiple words using Underscore
print('String:', my_string_var)
print(type(my_string_var))

my_integer_var = 30
print('Integer:', my_integer_var)
print(type(my_integer_var))

my_float_var = 4.50
print('Float:', my_float_var)
print(type(my_float_var))

my_boolean_var = True
print('Boolean:', my_boolean_var)
print(type(my_boolean_var))

my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var)
print(type(my_set_var))

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)
print(type(my_dictionary_var))

my_tuple_var = {7, 'Hello', 8.5}
print('Tuple:', my_tuple_var)
print(type(my_tuple_var))

my_range_var = range(5)
print('Range:', my_range_var)
print(type(my_range_var))

my_list = [22, 'Hello world', 3.14, True]
print(my_list)
print(type(my_list))

my_none_var = None
print('None:', my_none_var)
print(type(my_none_var))

# how type() and isinstance() functions work
developer = "Vejeh"
print(type(developer)) # the type of a the value of a var

account_balance = '12'
isinstance(account_balance, int) # instance function checks if a variable matches a specific data type.
isinstance(account_balance, (int, float)) # check against multiple data types

print(f"My name is {name} I am {age} years old")