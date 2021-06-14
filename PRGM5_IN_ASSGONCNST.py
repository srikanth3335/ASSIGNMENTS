#5)	Write a program to accept the year from the user and check weather the year is a leap year on not ?

year = int(input("enter the year: "))

if year % 4 == 0:
    print(f"{year} is leap")
else:
    print(f"{year} is not leap")