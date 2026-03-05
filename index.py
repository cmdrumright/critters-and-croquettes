###############
# Petting Zoo #
###############

# imports
from datetime import date
from walking import Camel, Donkey, Goat, Llama, Sheep
from slithering import Frog, Iguana, Lizard, Newt, Snake
from swimming import Bass, Catfish, Goldfish, Koi, Salmon

# create instances of walking classes
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "hay")

archibald = Donkey("Archibald", "Ass", "midday", "leaves")

billy = Goat("Billy", "fainting goat", "afternoon", "bark")

twin_peaks = Camel("Twin Peaks", "Saharan Camel", "morning", "shrubs")

fluffy = Sheep("Fluffy", "Highland Sheep", "midday", "grass")

cuzco = Llama("Cuzco", "emperor llama", "afternoon", "hay")

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
print(f"- species: {miss_fuzz.species}")
print(f"- shift: {miss_fuzz.shift}")
print(archibald.name)
print(billy.name)
print(twin_peaks.name)
print(fluffy.name)
print(cuzco.name)
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

# feed animals
miss_fuzz.feed()
archibald.feed()
billy.feed()
twin_peaks.feed()
fluffy.feed()
cuzco.feed()
