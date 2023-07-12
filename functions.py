# The function that pick an element in a list and a random int
from random import choice, randint
import json

# Tables to generate a name
with open('random_tables/naming_creatures.json', 'r') as creatures:
    creature_naming_table = json.load(creatures)

with open('random_tables/naming_descriptive.json', 'r') as descriptions:
    description_naming_table = json.load(descriptions)

with open('random_tables/naming_creatures.json', 'r') as objects:
    object_naming_table = json.load(objects)

with open('random_tables/naming_creatures.json', 'r') as others:
    other_naming_table = json.load(others)

with open('random_tables/naming_creatures.json', 'r') as people:
    people_naming_table = json.load(people)
    
### NAMING FUNCTIONS ###
def roll_description_table():
    dice = randint(1,100)
    description = description_naming_table[dice]
    description = description["attribute"]
    return description

def roll_creature_table():
    dice = randint(1,100)
    creature = creature_naming_table[dice]
    creature = creature["attribute"]
    return creature

def roll_object_table():
    dice = randint(1,100)
    object = object_naming_table[dice]
    object = object["attribute"]
    return object

def roll_people_table():
    dice = randint(1,100)
    people = people_naming_table[dice]
    people = people["attribute"]
    return people

def roll_other_table():
    dice = randint(1,100)
    other = other_naming_table[dice]
    other = other["attribute"]
    return other

def roll_random_subject(dice=None):
    if dice == None:
        dice = randint(1,3)
    match dice:
        case 1:
            subject = roll_creature_table()
        case 2:
            subject = roll_people_table()
        case 3:
            subject = roll_object_table()
    return subject

french_male_first_names = ['Alexis', 'Antoine', 'Benjamin', 'Édouard', 'Guillame', 'Matthieu', 'Nicholas', 'Pierre', 'Thibaud', 'Thomas']
french_female_first_names = ['Aurélie', 'Camille', 'Caroline', 'Charlotte', 'Claire', 'Émilie', 'Marie', 'Pauline', 'Sophie', 'Stéphanie']
french_surnames = ['Bernard', 'Bertrand', 'David', 'Dubois', 'Durand', 'Fournier', 'Garcia', 'Girard', 'Laurent', 'Lefèbvre', 'Leroy', 'Martin', 'Michel', 'Moreau', 'Petit', 'Richard', 'Robert', 'Roux', 'Simon', 'Thomas']

'''
PEOPLE
'''
def generate_npc_gender():
    genders = ['male', 'female']
    gender = choice(genders)
    return gender

def generate_npc_name(gender=''):
    if gender == None:
        gender = generate_npc_gender()

    elif gender == 'male':
        first_name = choice(french_male_first_names)
    else:
        first_name = choice(french_female_first_names)
    
    last_name = choice(french_surnames)

    full_name = f'{first_name} {last_name}'

    return full_name

def generate_bare_bone_npc():
    gender = generate_npc_gender()
    name = generate_npc_name(gender)
    npc = {
            'gender': gender,
            'name': name
                }
    return npc

'''
TAVERN FUNCTIONS
''' 
def generate_tavern_name():
    # Pick the method randomly
    dice = randint(1,3)

    # Do the different methods
    match dice:
        # The DESCRIPTIVE CREATURE/PEOPLE/OBJECT
        case 1:
            first_part_name = roll_description_table()
            second_part_name = roll_random_subject()
            tavern_name = f"The {first_part_name} {second_part_name}"
            return tavern_name
        # The SUBJECT and SUBJECT            
        case 2:
            first_dice = randint(1,3)
            second_dice = randint(1,3)

            while first_dice == second_dice:
                second_dice = randint(1,3)

            first_part_name = roll_random_subject(first_dice)
            second_part_name = roll_random_subject(second_dice)
            tavern_name = f"The {first_part_name} & the {second_part_name}"
            return tavern_name
        # The SUBJECT and SUBJECT (same table)
        case 3:
            dice = randint(1,3)
            first_part_name = roll_random_subject(dice)
            second_part_name = roll_random_subject(dice)
            tavern_name = f"The {first_part_name} & the {second_part_name}"
            return tavern_name