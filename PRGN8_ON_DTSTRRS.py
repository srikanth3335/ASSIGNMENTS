#8)	Below are the two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30] 

for key, value in zip(keys,values):
    print(f"'{key}':{value}",end=",")

    