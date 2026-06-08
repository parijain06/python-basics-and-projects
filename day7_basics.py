##FUNCTIONS IN PYTHON
#used to reduce repeatability or redundancy of code

# a = 2
# b = 3
# sum = a+b
# print(sum)
# #more lines of code
# a = 8
# b = 9
# sum = a+b
# print(sum)
# #more lines of code

#now to reduce this repeatability we use function

# def calcsum (a,b):              #(a,b):parameters, def:func, calcsum:funcname like variables
#     sum = a+b
#     print(sum)
#     return sum                  #returns value back to program
# calcsum(2,3)                    #func call:func_name(arg1,arg2,..)

#parameter:input
#return:output


# def printsomething():             #no input
#     print('hello')                #no output without the three lines below
# printsomething()
# printsomething()
# printsomething()

#avg of three numbers
# def calavg(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg
# calavg(2,3,8)

#functions are of two types:
#built in(print,len,type,range) and  user defined

# def cal_prod(a=1,b=2):            #if we do not passany arg,we set default parameters
#     print(a*b)
#     return a*b
# cal_prod()                        

# def cal_prod(a=1,b=2):          
#     print(a*b)
#     return a*b
# cal_prod(3)                          #agar yaha 3 nhi hota..then it would have assumed a=1      

#wap to print elements of list
# cities = ['meerut','hapur','delhi','noida']
# color = ['red','yello','green','blue']
# def list_len(list):
#     print(len(list))
#     return len(list)
# list_len(cities)
# list_len(color)

#wap to print elements of list in a single line
# cities = ['meerut','hapur','delhi','noida']
# def print_list(list):
#     for val in list:
#         print(val,end=" ")
#     return(list)
# print_list(cities)

#wap to find factorial of n
# def fact_print(n):
#     fact = 1
#     i = 1
#     while i<=n:
#         fact *=i
#         i+=1
#     print('factorial is: ',fact)    
#     return fact
# fact_print(3)

# # OR

# def fact_print(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# fact_print(5)    


##RECURSION IN PYTHON
#used to call a function repeatedly(similar to loops)
# def show(n):
#     if(n==0):                   #base case(stopping condition)
#         return
#     print(n)
#     show(n-1)
# show(5)

#factorial
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

# #wap to calculate sum of first n natural numbers
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+n
# print(sum(5))

#print elements of list
cities = ['meerut','hapur','delhi','noida']
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list(cities)