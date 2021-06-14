#3)	Given a Python list. Turn every item of a list into its square ( Hint : use [x * x for x in aList])

aList = [1, 2, 3, 4, 5, 6, 7]
list = []
for x in aList:
    square = x * x
    list.append(square)
print(list)
