#1)	A shop will give discount of  5% if the cost of purchased quantity is more than 5000.
#- Ask user for quantity
quantity = int(input("enter the number of quantities : "))
#- Suppose, one unit will cost 100.
one_unit_cost = 100
#- Judge and print total cost for user.
total_amount = quantity * one_unit_cost
if total_amount > 5000:
        discount_amount = total_amount * 0.05
        total_amount -= discount_amount
        print(f"total amount to be payable after discount {total_amount}")
else:
        print(f"total amount to be payable after discount {total_amount}")
