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
        Place("Cave of Mystery", 2)
    ]

    characters = [
        Character("Bill", "human", "super sleep"),
        Character("Star", "hound dog", "super smell"),
        Character("Little", "lionhead rabbit", "finding medicinal herbs"),
        Character("Zor", "alien", "telepathy")
    ]

    # Random selection
    random_place = random.choice(places)
    random_character = random.choice(characters)

    # Method calls on the place and character
    random_place.greet(player)
    random_character.greet(player)


if __name__ == "__main__":
    game_test()