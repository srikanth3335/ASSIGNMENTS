#4)	Accept 3 numbers from the user and print the greatest among them 
three_numbers = [ 60 , 50 , 10 ]
if three_numbers[1] <= three_numbers[0] >= three_numbers[2]:
    print(f"({three_numbers[0]} is the greatest number")
elif three_numbers[0] <= three_numbers[1] >= three_numbers[2]:
    print(f"({three_numbers[1]} is the greatest number")
else:
    print(f"({three_numbers[2]} is the greatest number")
