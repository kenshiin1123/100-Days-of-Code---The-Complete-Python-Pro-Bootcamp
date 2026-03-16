import random

letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
numbers = ["0", "1", "2", "3","4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

def random_generator(array):
    random_element = random.choice(array)
    return random_element

def password_order_gen():
    password_order = ["letters", "symbols", "numbers"]
    new_order=[]
    for _ in range(len(password_order)):
        random_order = random.choice(password_order)
        new_order.append(random_order)
        password_order.remove(random_order)
    return new_order

def easy_password_gen():
    print("\nGenerating from Easy password generator...\n")
    password = ""
    n_letters = int(input("How many letters would you like in your password? "))
    n_numbers = int(input("How many numbers would you like? "))
    n_symbols = int(input("How many symbols would you like? "))
    
    for _ in range(n_letters):
        password += str(random_generator(letters))
        
    for _ in range(n_symbols):
        password += str(random_generator(symbols))
        
    for _ in range(n_numbers):
        password += str(random_generator(numbers))
        
    return password

def hard_password_gen():
    print("\nGenerating from Hard password generator...\n")
    password = ""

    n_letters = int(input("How many letters would you like in your password? "))
    n_symbols = int(input("How many symbols would you like? "))
    n_numbers = int(input("How many numbers would you like? "))

    total_pass_len = n_letters + n_symbols + n_numbers

    password_dict = {
        "letters": {
            "list":letters,
            "number":n_letters,
            "current":0
        },
        "symbols": {
            "list":symbols,
            "number":n_symbols,
            "current":0
        },
        "numbers": {
            "list":numbers,
            "number":n_numbers,
            "current":0
        },
    }

    for _ in range(0,total_pass_len):
        password_order = password_order_gen()
        for j in range(0, len(password_order)):
            selected_pass_type = password_dict[password_order[j]]
            if selected_pass_type["current"] < selected_pass_type["number"]:
                password += random_generator(selected_pass_type["list"])
                password_dict[password_order[j]]["current"] += 1
    return password

def main():
    print("\nPassword Generator!")
    try:
        user_password_gen_choice = int(input("\n\tPick a password generator [1:Easy | 2:Hard]: "))
        if user_password_gen_choice not in [1,2]:
            raise
    except:
        print("❌ Invalid Input! Defaulting to easy password generator...")
    
    result = hard_password_gen()
    print("\nHere's the result: " + result)

if __name__ == "__main__":
    main()
