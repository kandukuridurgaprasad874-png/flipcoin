class Animal:
    def __init__(self, species):
        self.species = species
        print("This is the Animal class")

    def sound(self):
        print(f"{self.species} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def sound(self):
        super().sound()
        print(f"{self.name} is a {self.breed} and barks loudly")
d1 = Dog("Buddy", "Golden Retriever")
d1.sound()
