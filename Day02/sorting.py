

student_list = []

while True:
    data = input("Enter name, age and score: ")
    
    if not data:
        break
    
    name, age, marks = data.split(",")
    
    student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)