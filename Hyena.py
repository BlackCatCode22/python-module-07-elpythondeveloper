# Import the Animal class from the Animal module
from Animal import Animal

# Define the Hyena class, which inherits from the Animal class.
class Hyena(Animal):
    # Variable to keep track of the total number of Hyenas created.  It's initialized to 0.
    numOfHyenas = 0
    # Variable to store a list of hyena names.  It's initialized as an empty list.
    list_of_hyena_names = []
    # Variable to store the file path of the animal names text file.
    file_path = r'animalNames.txt'
    # ----- with statement -----
    # Open the file specified by file_path in read mode (r).
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them as a list in the lines variable.
        lines = file.readlines()
        # Initialize a counter variable called line_num to 1.
        line_num = 1
        # ----- for loop -----
        # Start a loop that iterates through each line in the lines list.
        for line in lines:
            # Check if the current line number is 3. Checks line 3 of the text file for Hyena names
            if line_num == 3:
                # If it's the third line, remove leading/trailing whitespace from the line
                # using strip() and then split the line into a list of names using comma as the delimiter.
                # Extend the list_of_hyena_names list with the resulting list of names.
                list_of_hyena_names.extend(line.strip().split(', '))
                # Exit the loop after processing the third line.
                break
            else:
                # If the line number is not 3, Increment the line number.
                line_num += 1
        # ----- for loop -----
    # ----- with statement -----

    # ----- Constructor Method - __init__ -----
    # The Constructor Method(initializer) for the Hyena class.
    # It initializes the attributes of a Hyena object,
    # and calls the constructor of the parent class (Animal).
    def __init__(self, name="a_name", animal_id="an_id", age="age_in_years",
                 birth_date="2099-01-01", color="a_color", sex="a_sex", weight="a_weight",
                 originating_zoo="a_zoo", date_arrival="2099-01-01"):
    # ----- Constructor Method - __init__ -----

        # Increments the class variable numOfHyenas (specific to the Hyena class) by 1.
        Hyena.numOfHyenas += 1

        # Call to the constructor method of the parent class.
        # Calls the __init__ method of the parent class (Animal)
        # to initialize the common animal attributes.
        # The hyena string is passed as the species.
        super().__init__("hyena", name, animal_id, age, birth_date, color, sex,
                         weight, originating_zoo, date_arrival)

    # ----- Function - get_hyena_name -----
    # Defines a method called get_hyena_name that retrieves a hyena's name.
    # The hyena object will call this method to get an unused hyena name.
    # pop() will remove the first element from the list_of_hyena_names[]
    def get_hyena_name(self):
        # Remove and return the first name from the list_of_hyena_names list.
        return self.list_of_hyena_names.pop(0)
    # ----- Function - get_hyena_name -----


