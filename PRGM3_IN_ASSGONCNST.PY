#3)	A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.

student_marks = int(input("enter the student marks: "))
max_student_marks = 100
if student_marks <= 100:
    if student_marks > 80:
        print("Grade A")
    elif 60 <= student_marks<= 80:
        print("Grade B")
    elif 50 <= student_marks < 60:
        print("Grade C")
    elif 45 <= student_marks < 50:
        print("Grade C")
    elif 25 <= student_marks < 45:
        print("Grade E")
    else:
        print("Grade F")
else:
    print(f"{student_marks} is invalid ")


