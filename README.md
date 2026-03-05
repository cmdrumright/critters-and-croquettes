# Critters and Croquettes

Python Practice

## Lessons

- Creating classes
  ```py
  class Llama:
    def __init__(self):
      # Establish the properties of each animal
      # with a default value
      self.name = ""
      self.species = ""
      self.date_added = date.today()
  ```
- Creating instance of class
  ```py
  miss_fuzz = Llama()
  ```
- Constructing instance with arguments

  ```py
  class Llama:
      def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()

  miss_fuzz = Llama("Miss Fuss", "domestic llama")
  ```

- Packaging Modules
  - move class declaration into their own files
  - move files into a package folder
  - create `__init__.py` file and import modules into into

  ```py
  from .llama import Llama
  ```

- Methods

  ```py
  class Llama:
  ...

      def feed(self):
          print(f"{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}")


  miss_fuzz.feed()

  ```

- Dunder Methods `__str__` and `__repr__`
  - str for human readable output
  - repr for machine readable output

  ```py
  class Llama:
      """LLama Class"""
      ...

      def __repr__(self) -> str:
          return f'Llama("{self.name}","{self.species}","{self.shift}","{self.food}")'

      def __str__(self) -> str:
          return f"{self.name} is a {self.species}"
  ```
