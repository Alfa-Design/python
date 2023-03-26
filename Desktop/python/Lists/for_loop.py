"""
names = ['John', 'mike', 'Alice', 'Isa', 'loops']
for name in names:
    print(name)
    

for value in range(1,5):
    print(value)

#Using range() to Make a List of Numbers
numbers = list(range(1,11))
print(numbers)


#print even numbers between 1 and 10 in an List of Numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#square of each integer from 1 through 10).

squares = []
for value in range(11):
    square = value ** 2
    squares.append(square)
    
print(squares)

"""
#Simple Statistics with a List of Numbers

digits = []
for value in range(1, 11):
    digits.append(value)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))


#List Comprehensions | A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. List

squares = [value**3 for value in range(1, 11)]
print(squares)