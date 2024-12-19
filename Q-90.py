int = int(input("Enter Odd Number : "))

try:
    if int % 2 != 0:
        print(f"Your number {int} is Odd number. ")
except ValueError :
    print("! invalid input ! please Enter correct value ")
else :
    print("! Your number is even ! please enter Odd number ")