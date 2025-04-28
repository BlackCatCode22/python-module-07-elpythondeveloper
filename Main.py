# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Assignment: Zookeeper's Challenge
# File: Main.py - This is the driver file for the program.
# Description: This program reads text describing animals from a text file called arrivingAnimals.txt.
#              The text file has 16 lines. Each line describes one animal.
#              There are 4 hyenas, 4 lions, 4 tigers and 4 bears in the text file.
#              This program also reads a list of animal names from a text file called animalNames.txt.
#              The program uses a function called gen_unique_id to generate a unique id for each animal.
#              The program uses a function called gen_birth_date to generate a birthdate for each animal.
#              After reading the animal date from the text file the program creates an animal object
#              from an animal class and then creates a report describing all the animals putting each
#              animal species in its own habitat in the report. The program creates a text file
#              called zooPopulation.txt and outputs the report in the text file.

# Imports the Animal class from the Animal.py file.
from Animal import Animal
# Imports the Hyena class from the Hyena.py file.
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear
# Imports the ddate class from the _datetime module.
from _datetime import date

# ~~~~~~~~~~ Lists Of Animals ~~~~~~~~~~
# Creates an empty list called list_of_hyenas.  This list will store Hyena objects.
list_of_hyenas = []
# Creates an empty list called list_of_lions.  This list will store Lion objects.
list_of_lions = []
# Creates an empty list called list_of_tigers.
list_of_tigers = []
# Creates an empty list called list_of_bears.
list_of_bears = []
# ~~~~~~~~~~ Lists Of Animals ~~~~~~~~~~

# ~~~~~~~~~~ Lists Of Animal Sounds ~~~~~~~~~~
# ----- hyena -----
# Create list of hyena laughs and store in a variable called list_of_hyena_laughs
list_of_hyena_laughs = ["haha", "hehe", "xaxa", "chacha"]
# Initializes the variable hyena_laugh_index to 0.
# By setting it to 0, ensures that the code starts by using the first element of
# the list_of_hyena_laughs which is "haha".
list_of_hyena_laughs_index = 0
# ----- hyena -----
# ----- lion -----
# Create list of lion roars and store in a variable called list_of_lion_roars
list_of_lion_roars = ["Roarrr", "RoooarRoooar", "Roaaar!", "Rrrrroarrrr"]
list_of_lion_roars_index = 0
# ----- lion -----
# ----- tiger -----
# Create list of tiger roars and store in a variable called list_of_tiger_roars
list_of_tiger_roars = ["Mew", "Meowww", "Mrrrrew!", "Mew! Mew!"]
list_of_tiger_roar_index = 0
# ----- tiger -----
# ----- bear -----
# Create list of bear roars and store in a variable called list_of_bear_roars
list_of_bear_roars = ["Grrrrr", "RrrrRrrr", "Gruff!", "Rrruff"]
list_of_bear_roar_index = 0
# ----- bear -----
# ~~~~~~~~~~ Lists Of Animal Sounds ~~~~~~~~~~

# Initialize a counter for unique IDs
animal_id_counter = 0
hyena_id_counter = 0
lion_id_counter = 0
tiger_id_counter = 0
bear_id_counter = 0

# save today's date in variable called current_date
current_date = date.today()
# save the current year in a variable called current_year
current_year = current_date.year

# ----- Function - gen_birth_date -----
def gen_birth_date(the_season, the_years):

    # Calculates the year of birth by subtracting the age in years from the current year.
    # It converts both values to integers to ensure correct arithmetic.
    year_of_birthday = int(current_year) - int(the_years)

    # ----- if statement -----
    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    # if the birth season is unknown
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"
    # ----- if statement -----

    # Returns string.
    return the_birth_day
# ----- Function - gen_birth_date -----

# ----- Function - gen_unique_id -----
# A function called gen_unique_id that generates an animals unique id.
# Input: Takes in a string species prefix.
# For example "Hy" for Hyena, "Li" for Lion, "Ti" for Tiger, "Bi" for bear.
# Output: The function returns a unique string ID. Such as "Hy001", "Li001"
def gen_unique_id(species_prefix):

    # Access the relevant counters
    global hyena_id_counter, lion_id_counter, tiger_id_counter, bear_id_counter

    if species_prefix == "Hy":
        # if the species prefix passed in is Hy increment the hyena counter by 1
        hyena_id_counter += 1
        # return the string for the unique id
        return f"{species_prefix}{str(hyena_id_counter).zfill(3)}"
    elif species_prefix == "Li":
        lion_id_counter += 1
        return f"{species_prefix}{str(lion_id_counter).zfill(3)}"
    elif species_prefix == "Ti":
        tiger_id_counter += 1
        return f"{species_prefix}{str(tiger_id_counter).zfill(3)}"
    elif species_prefix == "Be":
        bear_id_counter += 1
        return f"{species_prefix}{str(bear_id_counter).zfill(3)}"
    else:
        return None  # Or raise an exception for an invalid prefix
# ----- Function - gen_unique_id -----

# ----- Function - process_one_line -----
# Defines a function called process_one_line that takes a single line of text as input.
# This function parses the line, extracts animal data, and creates Animal objects.
def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    a_species = ""
    a_sex = ""
    # It's initialized to 99 as a default.
    age_in_years = 99
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    # Removes leading/trailing whitespace from the line and splits it into a list of strings,
    # using the comma as the delimiter. Each element in the list represents a data field.
    groups_of_words = one_line.strip().split(",")
    # Extracts the first element from groups_of_words (which contains age, sex, and species),
    # removes leading/trailing whitespace, and splits it into a list of individual words using
    # space as the delimiter.
    single_words = groups_of_words[0].strip().split(" ")
    # Assigns the first word of the first group to the variable age_in_years
    age_in_years = single_words[0]
    # Assigns the fourth word of the first group to the variable a_sex
    a_sex = single_words[3]
    # Assigns the fifth word of the first group to the variable a_species
    a_species = single_words[4]
    # Extracts the second element from groups_of_words (which contains season),
    # removes leading/trailing whitespace, and splits it into a list of individual words.
    single_words = groups_of_words[1].strip().split(" ")
    # Assigns the third word of the second group to the variable season
    season = single_words[2]
    # Extracts the third element from groups_of_words and assigns it to color
    color = groups_of_words[2].strip();
    # Extracts the fourth element from groups_of_words and assigns it to weight
    weight = groups_of_words[3].strip();
    # Extracts the fifth element from groups_of_words and assigns it to origin_01
    origin_01 = groups_of_words[4].strip();
    # Extracts the sixth element from groups_of_words and assigns it to origin_02
    origin_02 = groups_of_words[5].strip();

    # Concatenates the origin parts into a single string with a comma and space.
    from_zoo = origin_01 + ", " + origin_02

    # Calls the gen_birth_date function to determine the birthdate
    # based on the extracted season and age, and stores the result in birth_day.
    birth_day = gen_birth_date(season, age_in_years)

    # ~~~~~~~~~~ Create a hyena object ~~~~~~~~~~
    # ----- if statement -----
    # Check if the string hyena is present in the variable a_species.
    # This condition determines if a hyena object should be created.
    if "hyena" in a_species:
        # Create a hyena object.
        # Create a new instance of the Hyena class, passing several arguments:
        # "aName", "anID", birth_day, color, a_sex, weight, from_zoo, and current_date.
        # The new Hyena object is assigned to the variable my_hyena.
        my_hyena = Hyena("aName", "anID", age_in_years, birth_day, color,
                         a_sex, weight, from_zoo, current_date)
        # Call the class method get_hyena_name
        # and pass the my_hyena object as an argument.
        # The returned name is then assigned to the name attribute of the my_hyena object.
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        # Construct a unique animal ID for the hyena.
        # Call the function called gen_unique_id and feed it the string Hy.
        # The function will return a unique identifier for each hyena.
        # The returned unique identifier is then assigned to the animal_id attribute
        # of the my_hyena object.
        my_hyena.animal_id = gen_unique_id("Hy")
        # Add the newly created my_hyena object to the list_of_hyenas list.
        list_of_hyenas.append(my_hyena)
    # ----- if statement -----
    # ~~~~~~~~~~ Create a hyena object ~~~~~~~~~~

    # ~~~~~~~~~~ Create a lion object ~~~~~~~~~~
    # ----- if statement -----
    # Check if the string lion is present in the variable a_species.
    # This condition determines if a lion object should be created.
    if "lion" in a_species:
        # Create a lion object.
        my_lion = Lion("aName", "anID", age_in_years, birth_day, color,
                       a_sex, weight, from_zoo, current_date)
        # Call the class method get_lion_name
        # and pass the my_lion object as an argument.
        # The returned name is then assigned to the name attribute of the my_lion object.
        my_lion.name = Lion.get_lion_name(my_lion)
        # Call the function called gen_unique_id and feed it the string Li.
        # The function will return a unique identifier for each lion.
        # The returned unique identifier is then assigned to the animal_id attribute
        # of the my_lion object.
        my_lion.animal_id = gen_unique_id("Li")
        # Add the newly created my_lion object to the list_of_lions list.
        list_of_lions.append(my_lion)
    # ----- if statement -----
    # ~~~~~~~~~~ Create a lion object ~~~~~~~~~~

    # ~~~~~~~~~~ Create a tiger object ~~~~~~~~~~
    # ----- if statement -----
    # Check if the string tiger is present in the variable a_species.
    # This condition determines if a tiger object should be created.
    if "tiger" in a_species:
        # Create a tiger object.
        my_tiger = Tiger("aName", "anID", age_in_years, birth_day, color,
                       a_sex, weight, from_zoo, current_date)
        # Call the class method get_tiger_name
        # and pass the my_tiger object as an argument.
        # The returned name is then assigned to the name attribute of the my_tiger object.
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        # Call the function called gen_unique_id and feed it the string Ti.
        # The function will return a unique identifier for each tiger.
        # The returned unique identifier is then assigned to the animal_id attribute
        # of the my_tiger object.
        my_tiger.animal_id = gen_unique_id("Ti")
        # Add the newly created my_tiger object to the list_of_tigers list.
        list_of_tigers.append(my_tiger)
    # ----- if statement -----
    # ~~~~~~~~~~ Create a tiger object ~~~~~~~~~~

    # ~~~~~~~~~~ Create a bear object ~~~~~~~~~~
    # ----- if statement -----
    # Check if the string bear is present in the variable a_species.
    # This condition determines if a bear object should be created.
    if "bear" in a_species:
        # Create a bear object.
        my_bear = Bear("aName", "anID", age_in_years, birth_day, color,
                       a_sex, weight, from_zoo, current_date)
        # Call the class method get_bear_name
        # and pass the my_bear object as an argument.
        # The returned name is then assigned to the name attribute of the my_bear object.
        my_bear.name = Bear.get_bear_name(my_bear)
        # Call the function called gen_unique_id and feed it the string Be.
        # The function will return a unique identifier for each bear.
        # The returned unique identifier is then assigned to the animal_id attribute
        # of the my_bear object.
        my_bear.animal_id = gen_unique_id("Be")
        # Add the newly created my_bear object to the list_of_bears list.
        list_of_bears.append(my_bear)
    # ----- if statement -----
    # ~~~~~~~~~~ Create a bear object ~~~~~~~~~~

# ----- Function - process_one_line -----

# Open arrivingAnimals.txt and read it one line at a time
# Open the file in read mode
file_path = r"arrivingAnimals.txt"
# This 'with open(...)' block opens the file specified by 'file_path' in read mode ("r").
# It then iterates through each line of the file and calls the 'process_one_line' function to process the data.
# The 'with' statement ensures that the file is automatically closed when the block finishes.
with open(file_path, "r") as file:
    # Iterate through the file line by line
    for line in file:
        process_one_line(line)

# # Access the static variable numOfAnimals
# print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")
# print(f"\n\nNumber of hyenas created: {Hyena.numOfHyenas}")
# print(f"\n\nNumber of lions created: {Lion.numOfLions}")

# ~~~~~~~~~~~~~~~~~~~~ output the animals ~~~~~~~~~~~~~~~~~~~~
# this is zoo population
# These lines print the details of each hyena, lion, tiger, bear object in their respective lists.
# It iterates through the list_of_hyenas, list_of_lions, list_of_tigers, list_of_bears
# and prints the attributes of each animal object.
# Define the output file called zooPopulation can save it in variable called output_file_path
output_file_path = "zooPopulation.txt"

# Open the output zooPopulation file in write mode
with open(output_file_path, "w") as output_file:
    # write the report title string in the text file
    output_file.write("******** Zoo Population and Habitat Assignment Report ********\n\n")
    # ~~~~~~~~~~ Hyena Habitat ~~~~~~~~~~
    # Write Hyena habitat tile in text file, then move cursor down two lines.
    output_file.write("Hyena Habitat:\n\n")
    # ----- for loop -----
    # The for loop iterates through the list_of_hyenas and prints the attributes of each animal object
    for hyena in list_of_hyenas:
        # Prints the attributes of the current hyena object (animal_id, name, etc.) in a formatted string.
        # It accesses these attributes using the dot notation.
        # For example, hyena.animal_id means get the animal_id attribute of the hyena object.
        # For example, hyena.age means get the age attribute of the hyena object.
        output_file.write(
            hyena.animal_id + "; " + hyena.age + " years old; " + hyena.name + "; birthdate: "
            + str(hyena.birth_date) + "; " + hyena.color + "; " + hyena.sex + "; " + hyena.weight
            + "; " + "laugh: " + list_of_hyena_laughs[list_of_hyenas.index(hyena)] + "; "
            + hyena.originating_zoo + "; arrived: " + str(hyena.date_arrival) + "\n")
    # ----- for loop -----
    # ~~~~~~~~~~ Hyena Habitat ~~~~~~~~~~

    # ~~~~~~~~~~ Lion Habitat ~~~~~~~~~~
    # Write Lion habitat tile in text file, then move cursor down two lines.
    output_file.write("\nLion Habitat:\n\n")
    # ----- for loop -----
    # The for loop iterates through the list_of_lions and prints the attributes of each animal object
    for lion in list_of_lions:
        # Prints the attributes of the current lion object in a formatted string.
        output_file.write(
            lion.animal_id + "; " + lion.age + " years old; " + lion.name + "; birthdate: "
            + str(lion.birth_date) + "; " + lion.color + "; " + lion.sex + "; " + lion.weight
            + "; " + "roar: " + list_of_lion_roars[list_of_lions.index(lion)] + "; "
            + lion.originating_zoo + "; arrived: " + str(lion.date_arrival) + "\n")
    # ----- for loop -----
    # ~~~~~~~~~~ Lion Habitat ~~~~~~~~~~

    # ~~~~~~~~~~ Tiger Habitat ~~~~~~~~~~
    # Write Tiger habitat tile in text file, then move cursor down two lines.
    output_file.write("\nTiger Habitat:\n\n")
    # ----- for loop -----
    # The for loop iterates through the list_of_tigers and prints the attributes of each animal object
    for tiger in list_of_tigers:
        # Prints the attributes of the current tiger object in a formatted string.
        output_file.write(
            tiger.animal_id + "; " + tiger.age + " years old; " + tiger.name + "; birthdate: "
            + str(tiger.birth_date) + "; " + tiger.color + "; " + tiger.sex + "; " + tiger.weight
            + "; " + "roar: " + list_of_tiger_roars[list_of_tigers.index(tiger)] + "; "
            + tiger.originating_zoo + "; arrived: " + str(tiger.date_arrival) + "\n")
    # ----- for loop -----
    # ~~~~~~~~~~ Tiger Habitat ~~~~~~~~~~

    # ~~~~~~~~~~ Bear Habitat ~~~~~~~~~~
    # Write Bear habitat tile in text file, then move cursor down two lines.
    output_file.write("\nBear Habitat:\n\n")
    # ----- for loop -----
    # The for loop iterates through the list_of_bears and prints the attributes of each animal object
    for bear in list_of_bears:
        # Prints the attributes of the current bear object in a formatted string.
        output_file.write(
            bear.animal_id + "; " + bear.age + " years old; " + bear.name + "; birthdate: "
            + str(bear.birth_date) + "; " + bear.color + "; " + bear.sex + "; " + bear.weight
            + "; " + "roar: " + list_of_bear_roars[list_of_bears.index(bear)] + "; "
            + bear.originating_zoo + "; arrived: " + str(bear.date_arrival) + "\n")
    # ----- for loop -----
    # ~~~~~~~~~~ Bear Habitat ~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~ output the animals ~~~~~~~~~~~~~~~~~~~~