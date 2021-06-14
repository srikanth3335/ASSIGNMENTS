#7)	Given a Python list, remove all occurrence of 20 from the list


list1 = [5, 20, 15, 20, 25, 50, 20]  
while 20 in list1:
    list1.remove(20)
print(list1)