class Pokemon():
        def __init__(self, entry, name, types, description, is_caught):
            self.entry = entry # Integer 
            self.name = name # String
            self.types = types # List, String
            self.description = description # String 
            self.is_caught = is_caught # Bool
        
        def speak(self):
            print(f"{self.name}! {self.name}!")

        def display_details(self):
            output = (
            f"Entry Number: {self.entry}\n"
            f"Name: {self.name}\n"
            f"Type: {self.types}\n"
            f"Description: {self.description}\n"
            f"{self.name} has already been caught!\n"        
        )
            print(output)

bulbasaur = Pokemon(
    entry=1,
    name="Bulbasaur",
    types="Grass",
    description="He has a biggol' back.",
    is_caught="Nah, we start fire.")

charmander = Pokemon(
    entry=4,
    name="Charmander",
    types="Fire",
    description="Hot a%& breath bruv...",
    is_caught="Yesssssssir!"
    )

squirtle = Pokemon(
    entry=7,
    name="Squirtle",
    types="Water",
    description="Shell hard as a rock. Bricked up.",
    is_caught="Nah, we start fire."
    )