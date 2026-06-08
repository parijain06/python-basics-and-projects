students = {}
grades = {}
students_num = int(input('Enter number of students: '))
total = 0

#take student data
for i in range(students_num):
    name = input('Enter name of the student: ')
    marks = int(input('Enter marks of the student: '))

    students[name] = marks

    total = total + marks  

    #Grade
    if(80<= marks <=100):
        grade = "A"
    elif(60<= marks <=79 ):
        grade = "B"
    elif(40 <= marks <=59 ):
        grade = "C"
    else:
        grade = "Fail"

    print(grade)
    grades[name] = grade

# initialization
first_student = True

for name, marks in students.items():
    if first_student:
        highest_name = name
        highest_marks = marks

        lowest_name = name
        lowest_marks = marks
        first_student = False
       
    else:
        if marks > highest_marks:
            highest_name = name
            highest_marks = marks

        if marks < lowest_marks:
            lowest_name = name
            lowest_marks = marks

#Display all students
    print(name,":",marks,":",grades[name])
   
avg = (total/students_num)

print('\nSTUDENT PERFORMANCE REPORT')
print('Total marks: ',total)
print('Average marks: ',avg)
print("Highest marks scored by:", highest_name,"(",highest_marks,")")
print("Lowest marks schored by:", lowest_name,"(",lowest_marks,")")