## tuples
developer = ('Alice', 34, 'Rust Developer')
print(developer[1])
print(developer)

programming_languages = ('Rust', 'Python', 'Java', 'C++', 'Rust')
## programming_languages[0] = 'React'

print(programming_languages)

numbers = (1,2,3,4,5,6)
print(numbers[-1])
## print(numbers[5])
## print(numbers[8])

designers = 'Jessica'
print(tuple(designers))

print('Rust' in programming_languages)
print('JavaScript' in programming_languages)

name, age, job = developer
print(name)
print(age)
print(job)

names, *rest = developer
print(names)
print(rest)

desserts = ('cake', 'pie', 'cookes', 'ice cream')
print(desserts[1:3])
## del developer[1]

## So when might you use a tuple over a list?

## If you need a dynamic collection of elements where you can add, 
# remove and update elements, then you should use a list. 
# If you know that you are working with a fixed and immutable 
# collection of data, then you should use a tuple.



## Common Methods for Tuples

print(programming_languages.count('Rust'))
print(programming_languages.count('JavaScript'))
print(programming_languages.index('Java'))
## print(programming_languages.index('JavaScript'))

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3))
print(programming_languages.index('Python', 2, 5))

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers))

print(sorted(programming_languages, key=len))