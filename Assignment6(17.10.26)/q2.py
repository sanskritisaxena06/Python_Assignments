# Question: Create a Python function named calculate_discount() that accepts
# a bill amount and an optional discount percentage. The default discount
# should be 5%.
#
# Apply the following conditions:
# 1. If the bill amount is less than or equal to 0, display "Invalid Bill Amount".
# 2. If the bill amount is less than 1000, apply a 5% discount.
# 3. If the bill amount is between 1000 and 4999, apply a 10% discount.
# 4. If the bill amount is between 5000 and 9999, apply a 15% discount.
# 5. If the bill amount is 10000 or more, apply a 20% discount.
# 6. If the customer provides a custom discount, use it instead of the default slab discount.
# 7. The discount must be between 0% and 100%.
# 8. Display the original bill, discount percentage, discount amount,
#    and final payable amount.

print("By sanskriti saxena")

def calculate_discount(bill_amount, discount_percentage=None):
    if bill_amount <= 0:
        print("Invalid Bill Amount")
        return

    if discount_percentage is None:
        if bill_amount < 1000:
            discount_percentage = 5
        elif bill_amount < 5000:
            discount_percentage = 10
        elif bill_amount < 10000:
            discount_percentage = 15
        else:
            discount_percentage = 20

    if not 0 <= discount_percentage <= 100:
        print("Invalid Discount Percentage")
        return

    discount_amount = bill_amount * discount_percentage / 100
    final_amount = bill_amount - discount_amount

    print("Original Bill:", bill_amount)
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount:", discount_amount)
    print("Final Payable Amount:", final_amount)


calculate_discount(800)
calculate_discount(3000)
calculate_discount(7000)
calculate_discount(12000)
calculate_discount(5000, 25)