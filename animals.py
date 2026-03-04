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
