name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))
gender = input("Please Enter Your Gender (Male or Female): ")
product = input("Enter Product: ")
weight = int(input("Enter product weight in grams: "))

making_charge = 845
current_gold_price = 5752

total_making_charges = weight * making_charge
purchase = current_gold_price * weight
total_amount = purchase + total_making_charges

discount_rate = 0

if gender == "Male" and age > 65:
    if 200000 <= purchase < 300000:
        discount_rate = 0.20
    elif 300000 <= purchase < 500000:
        discount_rate = 0.25
    elif purchase >= 500000:
        discount_rate = 0.30

elif gender == "Male" and age <= 65:
    if 200000 <= purchase < 300000:
        discount_rate = 0.15
    elif 300000 <= purchase < 500000:
        discount_rate = 0.20
    elif purchase >= 500000:
        discount_rate = 0.25

elif gender == "Female" and age > 65:
    if 200000 <= purchase < 300000:
        discount_rate = 0.25
    elif 300000 <= purchase < 500000:
        discount_rate = 0.30
    elif purchase >= 500000:
        discount_rate = 0.35

elif gender == "Female" and age <= 65:
    if 200000 <= purchase < 300000:
        discount_rate = 0.20
    elif 300000 <= purchase < 500000:
        discount_rate = 0.25
    elif purchase >= 500000:
        discount_rate = 0.30

discount_amount = purchase * discount_rate
net_amount = total_amount - discount_amount

print(f"""
Mr./Ms. {name}
Total Amount of Purchase: {purchase}
Total Making Charges: {total_making_charges}
Total Amount: {total_amount}
Discount: {discount_amount}
Total Net Amount: {net_amount}
""")
