print("====================================================================")
print("                        UNKNOWN ISLAND                              ")
print("====================================================================")

print("You got stranded on an island after your ship sunked in the bottom of the ocean!.")
print("Do you want to go to the  CABIN, run to the FOREST, or visit the VILLAGE?")

choice = input("Type inside, forest, or village: ")

if choice == "inside":
    print("You open the door... it's dark.")
    action = input("Do you want to TURN ON the light?.")
    if action.lower() == "turn on":
        print("The light flickers... and saw that the CABIN was full of treasure! you made a both and saild off in the unknown! you win")
    elif action.lower() == "run":
        print("You run away screaming. you tripped, fall, then died, Game over.")
    else:
        print("You just stand there... a ghost scares you!")  

elif choice == "forest":
    print("You walk into the forest. It's quiet...")
    action = input("Do you want to CLIMB a tree or KEEP walking? ")
    if action.lower() == "climb":
        print("You climb up and see a dragon! you run for you life but sadly, you tripped and got eaten! game over.")
    elif action.lower() == "keep walking":   
        print("You find a shiny sword on the ground. you picked it up and and sense that you got stronger! you fought a dragon and won with ease, now a few days went by and decided that you wanted to stay and have a life here in the forest, the end.")
    else:
        print("You get lost in the dark forest...")

elif choice == "village":
    print("You arrive at a small village.")
    action = input("Do you want to TALK to people or REST at the inn? ")
    if action.lower() == "talk":
        print("The villagers give you food. Nice!")
    elif action.lower() == "rest":
        print("You sleep well and feel strong again.")
    else:
        print("You wander around and waste time.")

else:
    print("You didn't pick a valid option. Game over.")