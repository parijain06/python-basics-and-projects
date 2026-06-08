## VARIABLES (OUTPUT)
name = 'Pari'    #string can be stored in single, double and triple 
age = 20
price = 50.22
a=None           #when we do not store any value
value = True     #always use capital letter
 
print("name")    #prints exact thing in inverted comma
print(name)      #prints the value of the variable   
print (price)    
print (name)

print("my name is :",name)
print("my age is :",age)

name1 =name
print(name1)

print(type(name1))
print(type(age))
print(type(price))
print(type(a))
print(type(value))



## SUM OF TWO NUMBERS
a = 35
b = 32
sum = a+b
print(a+b)
#or
print(sum)



##EXPRESSION EXECUTION
#String and numeric values
a,b =2,3
text = "@"
print(2*text*3)

#String and string
a,b = "2",3              #2 is treated as a string
text = "@"
print((a+text)*4)

# Numeic values can operate with arithemetic operators
a,b = 3,2
c= 4
print(a*b+c)

# Arithemetic exp with int ad float will result in float
a,b=2,5.3
c= 5
print(a-b*c)

#Result of division operator with two integers will be float
a,b = 6,3
print(a/b)

#Integer division with float and int will give int displayed as float
a,b = 2.0,4
c= a/b
print(a//b,c)   #integer division divides and rounds off the result to lower int value

#Remainder is negative when denominator is negative
a,b = -5,2
print(a%b)
 
c,d= 5,-2
print(c%d)


## INPUT IN PYTHON
name = input("name :")
age = int (input("age :"))
price = float(input("float :"))
print(name)
print(age)
print(price)
print("My name is",name,"and my age is",age)
 