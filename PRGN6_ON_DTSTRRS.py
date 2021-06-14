#6)	Given a Python list, find value 20 in the list, and if it is present, replace it with 200. 
#Only update the first occurrence of a value ( Hint : use index() function in list)

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    list1[3]=200
print(list1)