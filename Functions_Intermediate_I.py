#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
x[1] = [15,8,9]
print(x)

students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0] = {'first_name':  'Michael', 'last_name' : 'Bryant'},
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory.update({"soccer": ['Andres', 'Ronaldo', 'Rooney'] })
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0] = {'x': 10, 'y': 30}
print(z)


students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#2 Iterate Through a List of Dictionaries. This function loops  through each dictionary entry and returns each key and value
def interateDictionary(some_list: list):
    for i in some_list:
        if i:
            sorted_keys = sorted(list(i.keys()))
            pairs = [f"{k} - {i[k]}" for k in sorted_keys]
            s = ", ".join(pairs)
            print(s)
interateDictionary(students)

#3 Get Values From a List of Dictionaries. This function prints the value stored for a particular key in a dictionary

def iterateDictionary2(key_name, some_list):
    for a in some_list:
        print(a.get(key_name))

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4 Iterate Through a Dictionary with List Values. This function prints the name of each key along with the size of the list within a dictionary and the values under that list.
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for a, b in some_dict.items():
        print(f"{len(b)} {a.upper()}")
        for i in b:
            print(i)
        print("---------------")

printInfo(dojo)

