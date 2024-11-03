class Zookeeper:
    def __init__(self, name):
        self.name = name

    def clean_enclosure(self, enclosure):
        if enclosure.is_dirty:
            enclosure.is_dirty = False
            print(f"{self.name} cleaned the enclosure.")
        else:
            print(f"{self.name} found the enclosure clean.")

    def feed_animals(self, enclosure):
        for animal in enclosure.animals:
            if animal.is_hungry:
                animal.is_hungry = False
                print(f"{self.name} fed {animal.species}.")
            else:
                print(f"{animal.species} is not hungry.")


class Enclosure:
    def __init__(self):
        self.animals = []
        self.is_dirty = True
        self.is_open = True

    def add_animal(self, animal):
        self.animals.append(animal)

    def close(self):
        self.is_open = False
        print("The enclosure is now closed.")

    def open(self):
        self.is_open = True
        print("The enclosure is now open.")


class Animal:
    def __init__(self, species):
        self.species = species
        self.is_hungry = True
        self.is_happy = False

    def update_happiness(self, enclosure):
        self.is_happy = not self.is_hungry and not enclosure.is_dirty
