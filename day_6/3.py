from printer import at_goal,move,turn_left,front_is_clear, right_is_clear

# Run this code below here https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()    
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        if right_is_clear():
            turn_right()
            while front_is_clear():
                move()
            turn_left()