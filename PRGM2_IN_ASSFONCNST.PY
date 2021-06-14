#2)	A college decides to give scholarship of 5% for the students  who have scored more than 80%. 
# Assume the fees is 30000.Ask for the students percentage and Find out the discounted fee.
student_percentage = float(input("enter the number student percentage: "))
fees = 30000
max_student_percentage = 100
if student_percentage <= 100:
    if   student_percentage > 80 :
        scholarship = fees * 0.05
        print(f"scholarship that can be awarded is {scholarship}")
    else:
         print("scholarship will not be awarded")
else:
    print(f'{student_percentage} is invalid input ')



