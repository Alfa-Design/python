"""
Dictionaries: in Python is a collection of keys values, used to store data values like a map, which, 
unlike other data types which hold only a single value as an element. 
Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimized.
"""

dictionary = {1:'johndoe', 2:'Mike', 3:'Kingstones', 4:'The forth Dictionary'}
#print(dictionary) #prints the entire dictionary
#print(dictionary.keys()) #ptints the keys of the dictionary
#print(dictionary.values()) #ptints the values of the dictionary
#print(dictionary[2]) #ptints the value 2 of the dictionary
#print(dictionary.get(2)) #gets the value 2 of the dictionary
#print(dictionary.get(10, 'Not found')) #if what is called is not in the dictionary, returns Not found

#Join the lists using Dictionary

names = ['John', 'Oumar', 'Otieno', 'Divine', 'Ary']
prog_languages = ['Python', 'Java', 'JavaScript', 'CSS', 'C#']
data = dict(zip(names, prog_languages))
print(data)
data['Belinder'] = 'PHP'
print(data)

#Dictionary within a dictionary and List within a dictionary.add()

prog = {'JS': 'Atom', 'CSS': 'VS', 'Python': ['pycham', 'sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
print(prog)
print(prog['Python'])
print(prog['Python'][0])