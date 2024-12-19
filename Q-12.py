num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

if num1 == num2 or num1 == num3 or num2 == num3:
    sum = 0
    print(sum)
else: 
    sum = num1 + num2 + num3
    print(f"{num1} + {num2} + {num3} = {sum}")