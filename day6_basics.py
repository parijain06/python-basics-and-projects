##LOOPS IN PYTHON

#While loop(jab tak)
#numbers from 100 to 1
# count = 100
# while count>=1:
#       print(count)
#       count-=1
# #numbers from 1 to 100
# count = 1
# while count<=100:
#       print(count)
#       count+=1
#multiplication table of number i
# n = int(input('enter the num:'))
# i = 0
# while i<=10:
#     print(i*n)
#     i+=1
#print the elements of the following list using loop
# list = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(list):
#     print(list[idx])
#     idx+=1
#search for a number x in the following tuple
# nums = (1,4,9,16,25,36,49,64,81,100,64)
# x = int(input('enter the value of x:'))
# i = 0
# while i<len(nums):
#     if(nums[i]==x):
#         print('x found at:',i)
#     else:
#         print('finding...')    
#     i+=1    

#break and continue in loops
# count = 1
# while count<=5:
#        if(count==4):
#           break  
#        print(count)
#        count+=1

# count = 1
# while count<=5:
#        if(count==4):
#           count+=1
#           continue                                #skip
#        print(count)
#        count+=1

# nums = (1,4,9,16,25,36,49,64,81,100,64)
# x = int(input('enter the value of x:'))
# i = 0
# while i<len(nums):
#     if(nums[i]==x):
#         print('x found at:',i)
#         break
#     else:
#         print('finding...')    
#     i+=1    


#for loop
#they are used for sequential traversal(indexed)[list,strings,tuple]
# str = 'abesecinstitute'
# for char in str:
#     print(char)

# list = [2,3,5,4,7]
# for val in list:
#     print(val)

# tup = ('red','yellow','green','orange','pink')
# for val in tup:
#     print(val)    

#for loop with else
# tup = ('red','yellow','green','orange','pink')
# for val in tup:
#     print(val)    
# else:
#     print('colors')

# tup = ('red','yellow','green','orange','pink')
# for val in tup:
#     if(val=='orange'):
#         break
#     print(val)    
# else:
#     print('colors')                     #or we could have simply written print('colors)

# tup = ('red','yellow','green','orange','pink')
# for val in tup:
#     if(val=='black'):
#         break
#     print(val)    
# else:
#     print('colors')                       #else helps in such cases  

#print the elements of the following list using loop
# list = [1,4,9,16,25,36,49,64,81,100]
# for val in list:
#     print(val)

#search for a number x in the following tuple
# nums = (1,4,9,16,25,36,49,64,81,100,64)
# x = int(input('enter the value of x:'))
# idx = 0
# for val in nums:
#     if(val==x):
#         print('x found at index:',idx)
#     idx+=1    


#range in python
#returns a sequence of numbers
#starts from 0 by default
#increments by 1(by default)and stops before a specified number
#syntax: range(start,stop,step)

# for el in range(2,7,2):
#     print(el)                          #el can be used in place of val

# for el in range(10):                   #range(stop)10 not included
#     print(el)

# for el in range(2,8):                  #range(start,stop)stop not included 
#     print(el)

#num from 1 to 100
# for el in range(100,0,-1):
#     print(el)

#table of n
# n = int(input('enter the value :'))
# for el in range(1,11):
#     print(el*n)

#pass statement
#it is used as a placeholder for future code
#used with if , else, loop
# for i  in range(2):
#      #error(empty)
# print('done')

# for i  in range(2):
#     pass
# print('done')            #no error

#factorial
n = int(input('enter n: '))
fact = 1
i =1
while i <=n:
    fact*=i
    i+=1
print('factorial is:',fact)
