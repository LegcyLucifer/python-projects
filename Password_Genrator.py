import random

number = ['1','2','3','4','5','6','7','8','9']
symbol = ['!','2','#','$','%','^','&','*']
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']

print("Wlecome to PyPassword Genrator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols you like\n "))
nr_numbers = int(input("How many numbers you like\n "))

password = []


for num in range(1, nr_numbers + 1):
    password += random.choice(number)
    
    
for sym in range(1,nr_symbols +1):
    password += random.choice(symbol)
    
    
for lett in range(1, nr_letters +1):
    password += random.choice(letter)

random_sequence = random.sample(password, len(password))  # Get a random sequence of all elements


pas = " "

for char in random_sequence:
    pas += char

print(f"Your Password is : {pas}")