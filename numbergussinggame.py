import random

print("GUESS THE NUMBER")

condition = True
count0 = 0
count1 = 0
count2 = 0
level_base = random.randint(1, 100)

while condition and count0 < 5:
    user_input = int(input("Please enter a Number Between 1 and 100:"))
    
    if user_input > level_base:
        count0 += 1
        print("Hint: Lower.")
        print(level_base)
    elif user_input < level_base:
        count0 += 1
        print("Hint: Higher")
    else:
        print("You Won")
        print("To Level 1")
        level_1 = random.randint(101, 150)
        count1 = 0
        
        while condition and count1 < 4:
            user_input = int(input("Please enter a Number Between 101 and 150:"))
            
            if user_input > level_1:
                count1 += 1
                print("Hint: Lower.")
            elif user_input < level_1:
                count1 += 1
                print("Hint: Higher")
            else:
                print("You Won")
                print("To Level 2")
                level_2 = random.randint(151, 200)
                count2 = 0
                
                while condition and count2 < 3:
                    user_input = int(input("Please enter a Number Between 151 and 200:"))
                    
                    if user_input > level_2:
                        count2 += 1
                        print("Hint: Lower.")
                    elif user_input < level_2:
                        count2 += 1
                        print("Hint: Higher")
                    else:
                        print("You Won")
                        condition = False
                        break
                else:
                    print("Game Over. You used your chance.")
                break
        else:
            print("Game Over. You used your chance.")
        break

if count0 >= 5:
    print("Game Over. The number was:", level_base)
