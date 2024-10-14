import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock ,paper ,scissors]

print("Please Enter 0 for Rock , 1 for Paper or 2 for scissor down below.")
choice = int(input("Enter You Choice :"))
print(images[choice])
random_choice = random.randint(a=0,b=2)
print(f"Computer Choose :{random_choice}")
print(images[random_choice])

if choice >= 3 or choice <0 :
    print("Invalid Input You Lose")
if random_choice == choice:
    print ("Draw")
if choice == 2 and random_choice == 0 :
    print(" You Lose.")
if random_choice == 1 and choice == 0 :
    print(" You Lose.")
if random_choice == 2  and choice == 1 :
    print(" You Lose.")
if choice == 2 and random_choice == 1 :
    print(" You Win.")
if random_choice == 1 and choice == 0 :
    print(" You Win.")
if random_choice == 2  and choice == 0 :
    print(" You Win.")            

                
            

            





