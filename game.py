
import random

def start_game():
    print("Welcome to the Adventure Game!")
    player_name = input("Enter your character's name: ")
    
    # Initialize player's attributes
    player = {
        "name": player_name,
        "health": 100,
        "strength": 10,
        "inventory": []
    }
    
    # Start the game's story by calling different functions
    forest_encounter(player)

def forest_encounter(player):
    print(f"{player['name']}, you find yourself in a mysterious forest...")
    choice = input("What do you want to do? (1. Explore the forest, 2. Leave): ")
    
    if choice == '1':
        # Random outcome
        if random.random() < 0.5:
            print("You discover a hidden treasure!")
            player['inventory'].append("Treasure")
        else:
            print("You encounter a dangerous beast and lose health.")
            player['health'] -= 20
        
        # Continue the story by calling other functions or encounters
        village_visit(player)
    else:
        print("You leave the forest and continue your journey.")
        # Implement other parts of the story here

def village_visit(player):
    print("You arrive at a peaceful village...")
    choice = input("What do you want to do? (1. Rest, 2. Buy equipment, 3. Leave): ")
    
    if choice == '1':
        player['health'] += 30
        print("You rest and regain some health.")
        # Continue the story
    elif choice == '2':
        player['inventory'].append("Sword")
        print("You buy a powerful sword.")
        # Continue the story
    else:
        print("You leave the village and continue your journey.")
        # Continue the story

# You can continue to create functions for other parts of the game

start_game()