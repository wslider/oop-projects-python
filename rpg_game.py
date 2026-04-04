import random

class Place:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def greet(self, player):
        print(f"Welcome {player} to Level {self.level}: {self.name}")


class Character:
    def __init__(self, name, species, ability):
        self.name = name
        self.species = species
        self.ability = ability

    def greet(self, player):
        if "human" in self.species.lower():
            print(f"Greetings {player}! My name is {self.name} and I have the power of {self.ability}.")
        elif "dog" in self.species.lower() or "hound" in self.species.lower():
            print(f"Woof! {player}! My name is {self.name} and I have the power of {self.ability}.")
        elif "rabbit" in self.species.lower():
            print(f"Squeak! {player}! My name is {self.name} and I have the power of {self.ability}.")
        else:
            print(f"Greetings {player}! My name is {self.name} and I have the power of {self.ability}.")


def game_test():
    player = input("Enter your name: ").strip()

    places = [
        Place("Limestone Cafe", 0),
        Place("Hidden Grotto", 1),
        Place("Fozberry Falls", 2), 
        Place("Abandoned Mine", 3), 
        Place("Deep Canyon Trail", 4), 
        Place("Whispering Stream", 5), 
        Place("Mushroom Forest", 6), 
        Place("Underground Crystal Palace", 7), 
        Place("Secret Bunker", 8),
        Place("Cave of Mystery", 9)
    ]

    characters = [
        Character("Bill", "human old man", "super sleep"),
        Character("Liz", "human waitress", "super memory"),
        Character("Star", "coonhound mix dog", "super bark"),
        Character("Jenny", "jackabee mix dog", "super smell"), 
        Character("Little", "male lionhead rabbit", "finding medicinal herbs"),
        Character("Zor", "semi-visible alien", "telepathy")
    ]

    # Random selection
    random_place = random.choice(places)
    random_character = random.choice(characters)

    # Method calls on the place and character
    random_place.greet(player)
    random_character.greet(player)


if __name__ == "__main__":
    game_test()