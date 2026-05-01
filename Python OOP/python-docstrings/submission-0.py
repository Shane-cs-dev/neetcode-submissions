class Pet:
    """ A class to represent a pet. """
    def __init__(self, name: str, animal_type: str):
        """Attribute:
            name (str): The pet's name
            animal_type (str): The pet's type
        """
        self.name = name
        self.animal_type = animal_type

    def make_sound(self) -> str:
        """
            Initialize a new Pet instance
            Return the sound the pet makes based in its type
        """
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# Don't change the following code
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)
