import random
import os
from hangman_pics import stages,logo
from hangman_words import word_list as random_words

def random_element(list):
    return random.choice(list)

# print("_", end=(" " if i != len(random_word) -1 else None))
def main():
    random_word = random_element(random_words)
    guessed_letters = []
    lives = 6
    is_winner = False
    
    def print_guessed_letters():
        os.system('cls')
        print(logo)
        print(stages[-(lives + 1)])
        print(f"\nYou have {lives} lives\n")
        for i in range(0,len(random_word)):
            if random_word[i] in guessed_letters:
                print(random_word[i].upper(), end=" ")
            else:
                print("_", end=" ")
        print()
            
    print_guessed_letters()
    
    def determine_winner():
        for i in range(len(random_word)):
            if random_word[i] not in guessed_letters:
                return False
        return True
    
    while lives > 0 and not is_winner:        
        user_guess = input("\nGuess a letter: ")
        
        if len(user_guess) > 1:
            print_guessed_letters()
            print("\n❌ Make sure to input 1 letter")
            continue
        
        if user_guess not in random_word:
            lives-=1
            print_guessed_letters()
        else:
            if user_guess in guessed_letters:
                lives-=1
                print_guessed_letters()
                print("\nGuess another letter!")
            else:
                guessed_letters.append(user_guess)
                print_guessed_letters()
            if determine_winner() :
                is_winner = True

    if is_winner and lives > 0:
        print("\nYou win the game!")
    else:
        print("\nYou lost the game!")
        print(f"\nThe answer is {random_word}")
    
if __name__ == "__main__":
    main()