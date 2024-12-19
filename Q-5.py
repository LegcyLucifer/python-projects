fact = 1
num = int(input("Enter a number : "))
for i in range(num,0,-1):
    fact *= i    
print(f"The factorial of {num} is : {fact}")