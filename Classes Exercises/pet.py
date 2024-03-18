""" The pet has no species. """
class Pet():
    """Only one instance of the pet class currently exists. """

    name = None
    # How hungry a pet is, zero being completely hungry and 100 being completely full.
    # Shown to the user as a percentage.
    fullness = 0

    def __init__(self,name):
        self.name = name

    # Takes a pet instance and a number representing a certain food as input.
    def eat(self, food):
        """ Allows ths user to feed the pet carrots, grass or water. """
        print(f"{self.name} is eating {food}...")
        if food == "1": # Carrots.
            self.fullness = self.fullness + 10
        elif food == "2": # Grass.
            self.fullness = self.fullness + 5
        elif food == "3": # Water.
            self.fullness = self.fullness + 1
        else: # I might add more foods in future.
            print("That's not a food.")
        print(f"{self.name} is now {self.fullness}% full.")

# Start of program.
# Asks for owner's and pet's names.
owner_name = input("What is your name? \n")
print(f"Welcome, {owner_name}.")
name = input("What would you like to call your pet? \n")

# Creates an instance of the Pet class and sets it's name to what the user said earlier.
pet_1 = Pet(name)

# While the pet is below 100% full.
while pet_1.fullness < 100:
    print(f"\n{pet_1.name} is hungry.")
    print(f"It's currently {pet_1.fullness}% full.")
    print("Enter the number of the food you would like to feed your pet.")
    food = input("1 - Carrots. \n 2 - Grass. \n 3 - Water. \n")
    Pet.eat(pet_1, food)
    