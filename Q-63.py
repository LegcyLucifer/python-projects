def perfect(n):
    sum = 0
    
    for i in range(1,n):
        if n % i == 0:
            sum+=i
            
    return sum == n 

number = int(input("Enter A number : "))
print(perfect(number))