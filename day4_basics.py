## LISTS IN PYTHON
#can store different data types together
#lists are mutable(changeable)

# marks = [56.5,77,86,98,98.6,54.6,'pari']
# marks[4]='beautiful'         #strings are immutable
# print(marks)
# print(marks[5])
# print(len(marks))

# #list slicing
# print(marks[2:5])
# print(marks[ : :-1])          #reverse
# print(marks[ :5])
# print(marks[3:len(marks)])
# print(marks[3:])

#list methods
# list=[2,5,8,1,3,2]
# list.sort()                     #ascending order
# print(list)
# list.sort(reverse=True)         #descending order
# print(list)
# list.insert(3,'apple')
# print(list)
# list.reverse()
# print(list)
# list.append('pari')
# print(list)
# list.remove(2)                  #removes first occurence
# print(list)
# list.pop(4)
# print(list)
 

 ##TUPLES IN PYTHON
 #tuples are immutable
# tup =()
# print(tup)
# print(type(tup))
# tup = (3)
# print(tup)
# print(type(tup))
# tup = (3,)                        #way to store single value in tuple(,)
# print(tup)
# print(type(tup))

# #tuple methods
# tup=(2,4,3,5,3)
# print(tup.index(3))                 #returns the first index of occurence

# movie1 = input('enter first movie:')
# movie2 = input('enter second movie')
# movie3 = input('enter third movie')
# print([movie1,movie2,movie3])
# print((movie1,movie2,movie3))

# movies = []
# movies.append(input('enter first movie:'))
# movies.append(input('enter second movie:'))
# movies.append(input('enter third movie:'))
# print(movies)

list1=[1,2,1]
list[2,1,3]
copylist1=list1.copy()
copylist1.reverse()
if(copylist1==list1):
    print('palindrome')
else:
    print('not a palindrome')    

list = ['c','d','a','b','b','a','a']
list.sort()
print(list)
