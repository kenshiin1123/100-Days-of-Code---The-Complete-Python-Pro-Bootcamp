from typing import Optional


coffee_ascii = """
                        (
                          )     (
                   ___...(-------)-....___
               .-\"\"       )    (          \"\"-.
         .-'``'|-._             )         _.-|
        /  .--.|   `\"\"---...........---\"\"`   |
       /  /    |                             |
       |  |    |                             |
        \\  \\   |                             |
         `\\ `\\ |                             |
           `\\ `|                             |
           _/ /\\                             /
          (__/  \\                           /
       _..---\"\"` \\                         /`\"\"---.._
    .-'           \\                       /          '-.
   :               `-.__             __.-'              :
   :                  ) \"\"---...---\"\" (                 :
    '._               `"--...___...--"`              _.'
      \\\"\"--..__                              __..--\"\"/
       '._     \"\""----.....______.....----\"\""     _.'
          `\"\"--..,,_____            _____,,..--\"\"`
                        `\"\""----\"\""`
"""

success_ascii="""
SSSSSSSSSSSSSSS                        SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS                      SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS                    SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS                  SSSSSSSSSSSSSSS                      SSS
    SSSSSSSSSSSSSSSSSSSSS                     SSSSSS                   SSSSSSSS
         SSSSSSSSSSSSSSSSSS       SSSSSSSSSSS   SS                 SSSSSSSSSSSS
              SSSSSSSSSSSSSSS  SSSSSSSSSSSSSSSSS              SSSSSSSSSSSSSSSSS
                   SSSSSSSS  SSSSSSSSSSSSSSSSSSSSS       SSSSSSSSSSSSSSSSSSSSSS
                        SS  SSSSSSSSSSSSSSSSSSSSSSS  SSSSSSSSSSSSSSSSSSSSSSSSSS
                           SSSSS     SSS     SSSSSSS  SSSSSSSSSSSSSSSSSSSSSSSSS
                          SSSSS   SS  S   SS  SSSSSSS  SSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSS  SSSSSSSSSSS SSSSSSSSSSSSSSS  SSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSS  SSSSSSSS S   SS SSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSS  SSSSS  SSSSSSSS   SSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSS  SSS SS        SSS SSSSS  SS
SSSSSSSSSSSSSSSSSSSSSS       SSSSSSSSSSSSSSSSSSSSS  SSSSSSSS
SSSSSSSSSSSSSSSSS              SSSSS   SSSSSSSSS  SSSSSSSSSSSSSSS
SSSSSSSSSSSS                 SS   SSSSSSSSSSS   SSSSSSSSSSSSSSSSSSSSSS
SSSSSSS                    SSSSSS                 SSSSSSSSSSSSSSSSSSSSSSSSS
SS                       SSSSSSSSSSSSSSS            SSSSSSSSSSSSSSSSSSSSSSSSSSS
                       SSSSSSSSSSSSSSSSS              SSSSSSSSSSSSSSSSSSSSSSSSS
                     SSSSSSSSSSSSSSSSSSS                SSSSSSSSSSSSSSSSSSSSSSS
                   SSSSSSSSSSSSSSSSSSSSS                  SSSSSSSSSSSSSSSSSSSSS
"""

failed_ascii ="""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ \"$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
\"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  \"\"\"$$$
   \"$$$\"\"\"\"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     \"$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     \"$$$o
   o$$\"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\" \"$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$\"\"\"\"\"\"\"\"
 \"\"\"\"       $$$$    \"$$$$$$$$$$$$$$$$$$$$$$$$$$$$\"      o$$$
            \"$$$o     \"\"\"$$$$$$$$$$$$$$$$$$\"$$\"         $$$
              $$$o          \"$$\"\"$$$$$$\"\"\"\"           o$$$
               $$$$o                 oo             o$$$\"
                \"$$$$o      o$$$$$$o\"$$$$o        o$$$$
                  \"$$$$$oo     \"\"$$$$o$$$$$o   o$$$$\"\"
                     \"\"$$$$$oooo  \"$$$o$$$$$$$$$\"\"\"
                        \"\"$$$$$$$oo $$$$$$$$$$
                                \"\"\"\"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$\"
                                       \"$$$\"\"\"\"

"""

class Dialog:
    text: str
    fail_text: str | list[str]
    answer: str
    game_over_for_different_answer:  Optional[list[dict]]
    
    def __init__(self, text, fail_text, answer, game_over_for_different_answer):
        self.text = text
        self.fail_text = fail_text
        self.answer = answer
        self.game_over_for_different_answer = game_over_for_different_answer
        
print(coffee_ascii)
print("Welcome to Treasure Island. Your mission is to find the treasure")

dialogs: list[Dialog] = [
    Dialog("left or right","Fall into a hole.\nGame Over.","left", None),
    Dialog("wait or swim", "Attacked by trout.\nGame Over.", "wait", None),
    Dialog("Which door? Red | Yellow | Blue", "Game Over", "yellow", [{"red":"Burned by fire.", "yellow": "You Win!", "blue":"Eaten by beasts.\nGame Over."}])
]

for i, dialog in enumerate(dialogs):
    user_input = input(f"\n\n{dialog.text}\nYour answer: ")
    
    if user_input.lower() == dialog.answer.lower():
        if i == (len(dialogs) -1): 
            print(success_ascii)
            print("\n\nYou Win!\n\n")
        continue
    else:
        if dialog.game_over_for_different_answer != None:
            if i == (len(dialogs) -1):
                print(failed_ascii)
            for gameover in dialog.game_over_for_different_answer:
                try:
                    print(f"\n{gameover[user_input]}\n\n")
                except:
                     print(f"\n{dialog.fail_text}\n\n")
            break
        else:
            print(f"\n{dialog.fail_text}\n\n")
            break