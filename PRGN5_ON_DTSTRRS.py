#5)	Remove empty strings from the list of strings ( Hint : use filter() function)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = list(filter(None, list1))

print(list1)