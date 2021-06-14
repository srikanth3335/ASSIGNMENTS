#4)	Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and
#  list2 in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for list1a,list2b in zip(list1,list2):
    print(list1a,list2b)


