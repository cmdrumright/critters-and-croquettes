###############
# Petting Zoo #
###############

# imports
from datetime import date


# define Llamma class
class Llama:
    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()


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
