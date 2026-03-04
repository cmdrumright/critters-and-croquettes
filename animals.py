###############
# Petting Zoo #
###############

# imports
from datetime import date


# define walking classes
class Llama:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Donkey:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Goat:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Camel:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Sheep:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# define slithering classes
class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Lizard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Newt:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Iguana:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


# define swimming classes
class Goldfish:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Bass:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Salmon:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Koi:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Catfish:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# create instances of walking classes
miss_fuzz = Llama("Miss Fuzz", "domestic llama")

archibald = Donkey("Archibald", "Ass")

billy = Goat("Billy", "fainting goat")

twin_peaks = Camel("Twin Peaks", "Saharan Camel")

fluffy = Sheep("Fluffy", "Highland Sheep")

# create instances of slithering classes
arthur = Snake("Arthur", "king snake")

sir_john = Lizard("Sir John", "spotted rock hopper")

issac_newton = Newt("Issac Newton", "science newt")

iggy = Iguana("Iggy", "Australian green iguana")

kermit = Frog("Kermit", "puppet frog")

# create instances of swimming classes
popeye = Goldfish("Popeye", "popeye goldfish")

gary = Bass("Gary", "Large mouth bass")

hopper = Salmon("Hopper", "red salmon")

spot = Koi("Spot", "orange koi")

whiskers = Catfish("Whiskers", "Tennessee catfish")

# print walker objects
print("Petting Area:")
print(miss_fuzz.name)
print(archibald.name)
print(billy.name)
print(twin_peaks.name)
print(fluffy.name)
print("")

# print slithering objects
print("Tank:")
print(arthur.name)
print(sir_john.name)
print(issac_newton.name)
print(iggy.name)
print(kermit.name)
print("")

# print swimming objects
print("Pond:")
print(popeye.name)
print(gary.name)
print(hopper.name)
print(spot.name)
print(whiskers.name)
