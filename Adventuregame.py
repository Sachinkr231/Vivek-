import random

def intro():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest with two paths: 'left' towards the river or 'right' towards the mountains.")

def river_path(choice):
    outcomes = {
        'swim': "You swim across the river safely and find a hidden treasure!" if random.choice([True, False]) else "A strong current pulls you under, but you manage to reach the shore safely.",
        'follow': "You find a small village to rest in!" if random.choice([True, False]) else "You find nothing and are now tired and hungry."
    }
    print(outcomes.get(choice, "That's not a valid option. The adventure ends here."))

def mountain_path(choice):
    outcomes = {
        'climb': "You discover a beautiful view from the top of the mountain!" if random.choice([True, False]) else "The rocks are slippery, but you manage to pull yourself to safety.",
        'rest': "You rest in the cave and meet a mysterious stranger who offers guidance." if random.choice([True, False]) else "You hear strange noises in the cave and decide to leave."
    }
    print(outcomes.get(choice, "That's not a valid option. The adventure ends here."))

def adventure_game():
    intro()
    choice1 = input("Do you go 'left' or 'right'? ").lower()
    
    if choice1 in ["left", "right"]:
        path = river_path if choice1 == "left" else mountain_path
        choice2 = input("Do you want to 'swim'/'follow' the river or 'climb'/'rest' in the cave? ").lower()
        path(choice2)
    else:
        print("That's not a valid option. The adventure ends here.")

    print("Thank you for playing!")

# Start the game
adventure_game()
