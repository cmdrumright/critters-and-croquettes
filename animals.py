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


# create instances of walking classes
miss_fuzz = Llama()
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"

archibald = Donkey()
archibald.name = "Archibald"
archibald.species = "Ass"

billy = Goat()
billy.name = "Billy"
billy.species = "fainting goat"

twin_peaks = Camel()
twin_peaks.name = "Twin Peaks"
twin_peaks.species = "Saharan Camel"

fluffy = Sheep()
fluffy.name = "Fluffy"
fluffy.species = "Highland Sheep"

# create instances of slithering classes
arthur = Snake()
arthur.name = "Arthur"
arthur.species = "king snake"

sir_john = Lizard()
sir_john.name = "Sir John"
sir_john.species = "spotted rock hopper"

issac_newton = Newt()
issac_newton.name = "Issac Newton"
issac_newton.species = "science newt"

iggy = Iguana()
iggy.name = "Iggy"
iggy.species = "Australian green iguana"

kermit = Frog()
kermit.name = "Kermit"
kermit.species = "puppet frog"

# create instances of swimming classes
popeye = Goldfish()
popeye.name = "Popeye"
popeye.species = "popeye goldfish"

gary = Bass()
gary.name = "Gary"
gary.species = "Large mouth bass"

hopper = Salmon()
hopper.name = "Hopper"
hopper.species = "red salmon"

spot = Koi()
spot.name = "Spot"
spot.species = "orange koi"

whiskers = Catfish()
whiskers.name = "Whiskers"
whiskers.species = "Tennessee catfish"

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
