number = float(input("\nEnter the number that you want to check if it's odd or even: "))
is_odd = True

if number % 2 == 0:
    is_odd = False
else:
    is_odd = True

print(f"\n\nThis number \"{number}\" is an {"odd" if is_odd else "even"} number! 😊\n")