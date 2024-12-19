import random 
limit = int(input("How many number you want to add in the list : "))
l1 = [i for i in range(1,limit+1)]

choice = random.choice(l1)
print(f"Your random number from the list is : {choice}")