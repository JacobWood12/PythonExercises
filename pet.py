class Pet():
    name = None
    fullness = 0

    def __init__(self,name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}...")
        if food == "1": # Carrots.
            self.fullness = self.fullness + 10
        elif food == "2": # Grass.
            self.fullness = self.fullness + 5
        elif food == "3": # Water.
            self.fullness = self.fullness + 1
        else:
            print("That's not a food.")
        print(f"{self.name} is now {self.fullness}% full.")

# Start of program.
# Asks for owner's and pet's names.
owner_name = input("What is your name? \n")
print(f"Welcome, {owner_name}.")
name = input("What would you like to call your pet? \n")

# Creates an instance of the Pet class and sets it's name to what the user said earlier.
pet_1 = Pet(name)

while pet_1.fullness < 100:
    print(f"\n{pet_1.name} is hungry.")
    print(f"It's currently {pet_1.fullness}% full.")
    food = input("Enter the number of the food you would like to feed your pet. \n 1 - Carrots. \n 2 - Grass. \n 3 - Water. \n")
    Pet.eat(pet_1, food)
    