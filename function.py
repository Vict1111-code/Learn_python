name = input('What is your name? ')
print('Hello', name)

print(int(3.14))
print(int('42'))
print(int(True))
print(int(False))

## functions
def hello():
    print('Hello, World!')

hello()

def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

def calculate_sum(a, b):
    return a + b

calculate_sum(5, 10)

my_sum = calculate_sum(3, 1)
print(my_sum)

## scope

tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(100)) # 10.0
print(tax_rate) # 0.1
#print(tax) # NameError: name 'tax' is not defined