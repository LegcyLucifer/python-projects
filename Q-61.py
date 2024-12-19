def factorial(num):
    a = 1
    for i in range(1,num+1):
        a *= i
    return a
    
choice = int(input("Enter a number which you want to factorial value : "))

print(factorial(choice))