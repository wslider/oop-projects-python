import random

def game_test():
    # Get player name
    player = input("Enter your name: ").strip()

    # Place Class
    class Place:
        def __init__(self, name, level):
            self.name = name
            self.level = level

        def greeting(self):
            print(f"Welcome {player} to Level {self.level}: {self.name}")


    # Character Class
    class Character:
        def __init__(self, name, species, ability):
            self.name = name
            self.species = species
            self.ability = ability

        def greeting(self):
            if "human" in self.species.lower():
                print(f"Greetings {player}! I am {self.name} the {self.species}, and I have the power of {self.ability}.")

            elif "dog" in self.species.lower():
                print(f"Woof woof! {player}! I am {self.name} the {self.species}, and I have the power of {self.ability}.")

            elif "rabbit" in self.species.lower():
                print(f"Squeak! {player}! I am {self.name} the {self.species}, and I have the power of {self.ability}.")

            else:
                print(f"Greetings {player}! I am {self.name} the {self.species}, and I have the power of {self.ability}.")


    # Create lists of instances
    places = [
        Place("Limestone Cafe", 0),
        Place("Hidden Grotto", 1),
        Place("Cave of Mystery", 2)
    ]

    characters = [
        Character("Bill", "human", "super sleep"),
        Character("Star", "hound dog", "super smell"),
        Character("Little", "lionhead rabbit", "finding medicinal herbs"),
        Character("Zor", "alien", "telepathy")
    ]

    # Random selection variables 
    random_place = random.choice(places)
    random_character = random.choice(characters)

    # Call the methods 
    random_place.greeting()
    random_character.greeting()


# Run the game
if __name__ == "__main__":
    game_test()