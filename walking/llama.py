"""Llama class module"""

from datetime import date


class Llama:
    """LLama Class"""

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def __repr__(self) -> str:
        return f'Llama("{self.name}","{self.species}","{self.shift}","{self.food}")'

    def __str__(self) -> str:
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")
