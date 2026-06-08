##DICTIONARY IN PYTHON
#mutable,unordered(no index)
#no duplication allowed
#stores data in the form of key:value pair

# dict = {
#     'name': 'Pari',
#     'age' : 20,
#     'subjects': ['python','java','cpp'],
#     'topics': ['sets','dictionery'],
#     'is_adult':True
# }
# print(dict)
# print(type(dict))
# print(dict['name'])
# dict['name']='Sakhi'         #overwrite
# dict['surname']='Jain'
# print(dict)

# nulldict={}
# print(nulldict)

#nested dictionery
# dict = {
#     'name': 'Pari',
#     'age': {
#         'age1': 56,
#         'age2': 64,
#         'age3': 32
#     },  # ← missing comma added here
#     'subjects': ['python', 'java', 'cpp'],
#     'topics': ['sets', 'dictionary'],  # spelling corrected
#     'is_adult': True
# }

# print(dict['age'])
# print(dict['age']['age1'])

# #dictionery methods
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get('topics'))
# print(len(dict))
# print(dict['color'])             #error
# print(dict.get('color'))          #no error(returns none)

# dict.update({'city':'meerut'})
# print(dict)
# newdict ={'city':'meerut','age':20,'name':'Pari'}
# dict.update(newdict)
# print(dict)


##SETS IN PYTHON
#sets are mutable
#elements of set are immutable,unordered(unindexed)
#each element must be unique
#duplicate values are ignored
# set = {1,2,3,4,'Pari','hello','Ishan','Ishan'}
# print(set)
# print(type(set))
# nullset = {}            #synatx of empty dictionery
# print(nullset)
# print(type(nullset))
# nullset1 = set()        #correct syntax for set
# print(nullset1)
# print(type(nullset1))

#set methods
# set1 = {1,2,3,4,'Pari','hello'}
# set.add('orange')
# print(set)
# set.remove(3)
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)
# set2 = {2,1,3,'Pari','red','car',7,9}
# print(set1.union(set2))
# print(set1.intersection(set2))

# marks={}
# x= int(input('enter marks of phy:'))
# marks.update({'phy':x})
# x= int(input('enter marks of math:'))
# marks.update({'math':x})
# x= int(input('enter marks of chem:'))
# marks.update({'chem':x})
# print(marks)

#figure out a way to store 9 and 9.0 as seperate value
# set = {'9.0',9}
# print(set)
# #OR
# set = {('int',9),('float',9.0)}
# print(set)
students = {
    "pari": 97,
    "ishan": 99
}

print(students.items())