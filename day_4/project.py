import random
import time
import ascii_flipper

rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("\nRock Paper Scissors Game!\n")

def get_picked(choice):
    if choice == 1:
        return {"name":"rock", "ascii": rock_ascii}
    elif choice == 2:
        return {"name":"paper", "ascii": paper_ascii}
    elif choice == 3:
        return {"name":"scissors", "ascii": scissors_ascii}
    return {}

user_choice = 1

try:
    user_choice = int(input("Please choose [1: Rock | 2: Paper | 3: Scissors]: "))
    if user_choice not in [1,2,3]:
        raise
except:
    print("\n❌ INVALID CHOICE! Defaulting to rock...")
    time.sleep(1)
    user_choice = 1

computer_choice = random.randint(1,3)

user_picked = get_picked(user_choice)
computer_picked = get_picked(computer_choice)

print("\n\nRock!")
time.sleep(0.5)
print("\tPaper!\n")
time.sleep(0.5)
print("Scissors!")
time.sleep(0.3)
print("\n\tShoot!!!")
time.sleep(0.5)

print(f"\n\n\n\n\nYou picked: {user_picked["name"]}")
print(user_picked["ascii"])

time.sleep(1)

print(f"\n\n\nComputer picked {computer_picked["name"]}")
print(ascii_flipper.ascii_flipper(computer_picked["ascii"]))

time.sleep(1)

print("\n\n\n")

if user_choice == computer_choice:
    print(f"It's a tie! You both picked {user_picked["name"]}.")

elif user_choice == 1 and computer_choice == 2:
    print("You lose! Rock lose against paper!")
elif user_choice == 1 and computer_choice == 3:
    print("You win! Rock wins against scissors!")

elif user_choice == 2 and computer_choice == 1:
    print("You win! Paper wins against rock!")
elif user_choice == 2 and computer_choice == 3:
    print("You lose! Paper lose against scissors!")

elif user_choice == 3 and computer_choice == 1:
    print("You lose! Scissors lose against rock!")
elif user_choice == 3 and computer_choice == 2:
    print("You win! Scissors wins against paper!")