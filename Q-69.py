import random

start = int(input("Enter your starting value : "))
limit = int(input("Enter your ending value : "))

computer = random.randint(start,limit)
print()
print(f"Your randamise value is : {computer}")