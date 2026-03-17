from printer import move, turn_left
# Run this code below here https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

square_size = 9
def circle_world(default_moves = square_size - 1, turns = 0, turn_face = "left"):
    moves = default_moves
    if turn_face == "left":
        if turns == 2:
            turns = 0
            default_moves -= 1
        while moves > 0:
            move()
            moves -= 1
        if turns == -1:
            turn_left()
            turn_left()
        else:
            turn_left()
    elif turn_face == "right":
        if turns == 2:
            turns = 0
            default_moves += 1
        while moves > 0:
            move()
            moves -=1
        turn_right()
    if turns != 2: turns += 1
    if default_moves == 0 and turn_face == "left":
        turn_left()
        turn_face = "right"
        default_moves += 1
    elif default_moves == square_size and turn_face == "right":
        turn_face = "left"
        default_moves -= 1
        turns -= 2
    circle_world(default_moves, turns, turn_face)
        
def main():
    circle_world()
main()