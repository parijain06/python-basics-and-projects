# ## CONDITIONAL STATEMENTS

# # Traffic light code
# color=input("color:")
# if(color=="red"):
#     print("Stop")
# elif(color=="yellow"):
#     print("wait")
# elif(color=="green"):
#     print("go")
# else:
#     print("broken")

# # Grades of students
# marks= int(input("marks:"))
# if(marks >=90):
#     print("A")
# elif(marks >=80 and marks <90):
#     print("B")
# elif(marks >=70 and marks <80):
#     print("C")        
# else:
#     print("D")


# '''TERNARY OPERATOR
# <VAR>=<val1> if <condition> else<val2>
# <st1>if<condition>else<st2>
# <VAR> = (false_val , true_val)[<condition>]'''

# food = input("food :")
# eat = "yes" if food=="cake" else"no"
# print("eat")

# food = input("food :")
# print("sweet")if food=="cake" or  food=="chocolate"else print("not sweet")

# age= int(input("age :"))
# vote = ("yes","no")   [age < 18]



# ## OPERATORS

# #arithmetic operators
# a=5
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)     #remainder
# print(a**b)    #a^b

# #relational operators

# a=50
# b=54
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

#assignment operators
# num = 10
# # num = num+10  #10+10
# num +=10
# print("num :",num)

#logical operators
#not opeartor
# a = 64
# b = 54
# print(not True)
# print(not(a==b))
# #and or operator
# a = True
# b = False
# print(a and b)   #multiplication
# print(a or b)    #addition


## TYPE CONVERSION(automatic)
# a = 1
# b = 2.5
# print(a + b )       #int to float conversion
# A = "2"
# B = 3.4
# print(A+B)          #type casting required


##TYPE CASTING(manual)
# C = int("2")
# D = 3.4
# print(C+D)

# A = int("Pari")
# B = 3.4
# # print(A+B)
# print(type(A))

# a = 3.14
# b = 45
# a = str(a)
# print(type(a))



# ## INPUT IN PYTHON
# input("Enter name :")
# val = input("enter some value : ")
# print(type(val),val)

# age = int(input("enter age:"))
# price = float(input("enter the price:"))
# print("age is:",age)
# print('price is:',price)

##STRINGS

# # str1 = "This is my laptop.It is kept on the table"
# str1 = "This is my laptop.\nIt is kept on the table"
# print(str1)
# str2 = "This is my laptop.\tIt is kept on the table"
# print(str2)
# str3 = 'apple is '
# str4 = 'sweet'

# print(str3+str4)
# print(len(str4))
# print(str3[5])

#string slicing
str = 'weather is pleasant'
# print(str[2:7])
# print(str[ :5])
# print(str[4: ])
# print(str[3:len(str)])

# str1 = 'beautiful'
# print(str[-7:-4])          #begins with -1 from backward

 ##String functions
# str = 'i am a coder'
# print(str.endswith("er"))
# print(str.capitalize())
# str = str.capitalize()
# print(str)
# print(str.replace("a","i"))
# print(str.find('a'))        #returns first index of first occurence
# print(str.count("c"))
# print(str.lower()) 
# print(str.upper())

# text = input("Enter a string:")
# if text == text[ : :-1]:
#     print("palindrome")
# else:
#     print("not")    

# text = input("Enter a string:")
# count = 0
# for ch in text.lower():
#     if ch in 'aeiou':
#         count+=1
# print('vowels =',count)        