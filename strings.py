my_str = 'Hello world'
my_str_1 = 'Hello'
my_str_2 = "World"

# multi-line string uses triple double quotes or single quotes:
my_str_3 = """Multiline
string"""
my_str_4 = '''Another 
multiline 
string'''

# Use the opposite kind of quotes or \ to escape. if string contains either single or double quote
msg = "It's a sunny day" # or 'It\'s a sunny day'
quote = 'She said, "Hello World!"' # or "She said, \"Hello World\!""

# To check if a string contains one or more char python provides (in operator)
print('Hello' in my_str)
print('hey' in my_str)
print('hi' in my_str)
print('e' in my_str)
print('f' in my_str)

# To get the length of a string use (len())
print(len(my_str))

greeting = 'hi'
greeting = 'hello'
print(greeting)

# greeting[0] = 'H'

# string concatenation
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)

name = 'John doe'
age = 26

name_and_age = name + str(age) # or name_and_age += str(age)
print(name_and_age)


num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

# String Slicing
print(my_str[0]) # first index starts with 0 (H)
print(my_str[6])
print(my_str[-1]) # last char of a string d
print(my_str[-2]) # l

print(my_str[1:4]) # ell
print(my_str[:7]) # Hello w
print(my_str[8:]) # rld
print(my_str[:])

print(my_str[0:11:2]) # Hlowrd
print(my_str[::-1]) # dlrow olleH

# String Method
uppercase_str = my_str.upper()
print(uppercase_str) # HELLO WORLD

lowercase_str = my_str.lower()
print(lowercase_str)  # hello world

my_space_str = '   hello world   '
trimmed_str = my_space_str.strip()
print(trimmed_str)

replace_str = my_str.replace('Hello', 'Hi')
print(replace_str)

split_word = my_str.split()
print(split_word)

my_list = ['hello', 'world']
join_str = ' '.join(my_list)
print(join_str)

starts_with = my_str.startswith('Hello')
print(starts_with) # True

ends_with = my_str.endswith('world')
print(ends_with)

word_index = my_str.find('world')
print(word_index) # 6

count_char = my_str.count('o')
print(count_char) # 2

capitalized_str = my_str.capitalize()
print(capitalized_str)  # Hello world

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

is_all_lower = my_str.islower()
print(is_all_lower)  # False

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
