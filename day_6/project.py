from printer import at_goal,move,turn_left,front_is_clear, right_is_clear

def turn_right():
    turn_left()
    turn_left()    
    turn_left()

def move_if_clear():
    while front_is_clear():
        move()

def turn_if_not_clear():
    while not front_is_clear():
        if not right_is_clear():
            turn_left()
        else:
            turn_right()
            
while not at_goal():
    move_if_clear()
    turn_if_not_clear()