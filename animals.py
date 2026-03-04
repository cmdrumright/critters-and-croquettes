###############
# Petting Zoo #
###############

# imports
from datetime import date


# define walking classes
class Llama:
    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Donkey:
    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Goat:
    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Camel:
    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Sheep:
    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


# define slithering classes
class Snake:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class Lizard:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class Newt:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class Iguana:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class Frog:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


# define swimming classes
class Goldfish:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Bass:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Salmon:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Koi:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Catfish:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


# create instance of Llamma
miss_fuzz = Llama()

# set the properties of the instance
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"

print("name:")
print(miss_fuzz.name)
print("")
print("species:")
print(miss_fuzz.species)
print("")
print(f"date_added: {miss_fuzz.date_added}")
