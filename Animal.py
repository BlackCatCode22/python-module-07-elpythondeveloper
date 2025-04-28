# Defines a new class named Animal
class Animal:

    # Define a class-level variable named numOfAnimals and initialize it to 0.
    # This variable is shared by all instances (objects) of the Animal class.
    # It keeps track of the total number of Animal objects created.
    numOfAnimals = 0

    # The Constructor Method(initializer) for the Animal class. It sets the attributes of an Animal object.
    def __init__(self, species, name, animal_id, age, birth_date, color, sex, weight, originating_zoo, date_arrival):

        # Assign the values passed in to attributes of the Animal object

        # Assigns the species to the animal's species attribute.
        self.species = species
        # Assigns the name to the animal's name attribute.
        self.name = name
        self.animal_id = animal_id
        self.age = age
        self.birth_date = birth_date
        self.color = color
        self.sex = sex
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.date_arrival = date_arrival

        # Increments the class variable numOfAnimals by 1, counting the new animal.
        Animal.numOfAnimals += 1