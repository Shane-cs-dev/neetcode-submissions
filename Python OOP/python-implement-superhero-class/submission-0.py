class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
superhero1 = SuperHero("Batman", "Intelligence", 100)
superhero2 = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero
print(f"{superhero1.name}")
print(f"{superhero1.power}")
print(f"{superhero1.health}")
print(f"{superhero2.name}")
print(f"{superhero2.power}")
print(f"{superhero2.health}")