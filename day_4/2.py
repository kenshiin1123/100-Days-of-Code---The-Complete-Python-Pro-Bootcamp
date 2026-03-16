import random
import time

print("Heads or Tails!")

def main():
    user_guess = int(input("Which one would win?\n\n[1: Heads, 2: Tails]: "))
    print("")
    if(user_guess != 1 and user_guess != 2):
        print("Please input 1 or 2.")
        return

    heads_score = 0
    tails_score = 0

    for _ in range(50):
        is_true = (random.randint(1,100) % 2) == 0
        if is_true:
            print("Heads!\n")
            heads_score+=1
        else:
            print("Tails!\n")
            tails_score+=1
        time.sleep(0.05)

    winner = ""

    if heads_score > tails_score:
        winner = "heads"
    elif tails_score > heads_score:
        winner = "tails"
    else:
        winner = "tied"

    print("\nScores:")
    print("\tHeads: " + str(heads_score))
    print("\tTails: " + str(tails_score) + "\n")
    
    if user_guess == 1 and winner == "heads":
        print("You win! You have guessed that Heads will win!\n\n\n")
    elif int(user_guess) == 2 and winner == "tails":
        print("You win! You have guessed that Tails will win!\n\n\n")
    elif winner == "tied":
        print("It's a tie!")
    else:
        print(f"\nYou lose this time! You guessed {"Heads" if user_guess == 1 else "Tails"}, but the {winner} wins!\n\n\n")
        
if __name__ == "__main__":
    main()