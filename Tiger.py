from Animal import Animal

class Tiger(Animal):
    numOfTigers = 0

    list_of_tiger_names = []

    file_path = r'animalNames.txt'
    # ----- with statement -----
    with open(file_path, 'r') as file:
        lines = file.readlines()

        line_num = 1
        # ----- for loop -----
        for line in lines:
            # Get the tiger names from line 15
            if line_num == 15:
                list_of_tiger_names.extend(line.strip().split(', '))
                # Exit the loop after processing the seventh line.
                break
            else:
                line_num += 1
        # ----- for loop -----
    # ----- with statement -----

    # ----- Constructor Method - __init__ -----
    # Define the constructor (__init__) for the Tiger class.
    def __init__(self, name="a_name", animal_id="an_id", age="age_in_years",
                 birth_date="2099-01-01", color="a_color", sex="a_sex", weight="a_weight",
                 originating_zoo="a_zoo", date_arrival="2099-01-01"):
    # ----- Constructor Method - __init__ -----

        Tiger.numOfTigers += 1

        # Call the constructor of the parent class (Animal) with tiger as the species using super().
        # Pass the species "tiger" and the other provided arguments.
        super().__init__("tiger", name, animal_id, age, birth_date, color, sex,
                         weight, originating_zoo, date_arrival)

    # ----- Function - get_tiger_name -----
    # Define a method called get_tiger_name that retrieves a tiger's name.
    # the tiger object will call this method to get an unused tiger name.
    # pop() will remove the first element from the list_of_tiger_names[]
    def get_tiger_name(self):
        # Remove and return the first name from the list_of_tiger_names list.
        return self.list_of_tiger_names.pop(0)
    # ----- Function - get_tiger_name -----