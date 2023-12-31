# The function that pick an element in a list and a random int
from random import choice, randint
import json

'''
RESOURCES LOADING
'''
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

with open('random_tables/general_wealth_level.json', 'r') as wealth:
    wealth_level_table = json.load(wealth)
'''
GLOBAL FUNCTIONS
'''
# Database interactions
def fetch_element_by_id(graph, id):
    # Fetch the element based on the id and reset the query
    query = "MATCH (n) WHERE ID(n)={id} RETURN n".format(id=id)
    records = graph.run(query)
    query = None
        
    # Extract data from the records. Here it's a dictionary and each row could contain one full node, hence the 'n'
    record = records.data()
    database_infos = record[0]['n']
    return database_infos

def update_element_in_bulk(graph, id, changes):
    for change in changes:
        if isinstance(change['value'], str):
            query = "MATCH (n) WHERE ID(n)={id} SET n.{attribute} = '{value}'".format(id=id, attribute=change['attribute'], value=change['value'])
            graph.run(query)
            query = None
        else:
            query = "MATCH (n) WHERE ID(n)={id} SET n.{attribute} = {value}".format(id=id, attribute=change['attribute'], value=change['value'])
            graph.run(query)
            query = None
    return

# Tables interactions
def roll_on_tables(table_path):
    # Unpack the table
    with open(table_path, 'r') as file:
        table = json.load(file)

    # Pick the good dice and roll it
    MAX_DICE = len(table)-1
    dice = randint(0,MAX_DICE)

    # Roll it on the table
    table_result = table[dice]
    table_result = table_result["attribute"]
    
    return table_result

# HTML interactions
def generate_ul_list_of_properties(data):
    ul_list = []
    
    for row in data:
        ul_list.append(f'{row["attribute"]}: {row["value"]}')
    
    return ul_list

### NAMING FUNCTIONS
def roll_description_table():
    dice = randint(0,99)
    description = description_naming_table[dice]
    description = description["attribute"]
    return description

def roll_creature_table():
    dice = randint(0,99)
    creature = creature_naming_table[dice]
    creature = creature["attribute"]
    return creature

def roll_object_table():
    dice = randint(0,99)
    object = object_naming_table[dice]
    object = object["attribute"]
    return object

def roll_people_table():
    dice = randint(0,99)
    people = people_naming_table[dice]
    people = people["attribute"]
    return people

def roll_other_table():
    dice = randint(0,99)
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
# TAVERN LEVEL 1 - "HEARD OF" 
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

# TAVERN LEVEL 2 - "FIRST GLANCE" 
def generate_tavern_size():
    table_path = 'random_tables/tavern_size.json'
    tavern_size = roll_on_tables(table_path)
    return tavern_size

def generate_tavern_atmosphere():
    table_path = 'random_tables/tavern_atmosphere.json'
    tavern_atmosphere = roll_on_tables(table_path)
    return tavern_atmosphere

def generate_tavern_clientele():
    table_path = 'random_tables/tavern_clientele.json'
    tavern_clientele = roll_on_tables(table_path)
    return tavern_clientele

def generate_tavern_standing():
    table_path = 'random_tables/general_wealth_level.json'
    tavern_standing = roll_on_tables(table_path)
    return tavern_standing

def generate_tavern_description():
    table_path = 'random_tables/tavern_description.json'
    tavern_description = roll_on_tables(table_path)
    return tavern_description

def generate_tavern_description_details(description):
    match description:
        case "timber and thatch":
         table_path = 'random_tables/tavern_description_timber_thatch.json'
         tavern_details = roll_on_tables(table_path)
         return tavern_details
    return 'none'

def generate_tavern_level_two():
    tavern_description = generate_tavern_description()
    tavern_details = generate_tavern_description_details(tavern_description)
    changes = [
        {"attribute": 'size', "value": generate_tavern_size()},
        {"attribute": 'atmosphere', "value": generate_tavern_atmosphere()},
        {"attribute": 'clientele', "value": generate_tavern_clientele()},
        {"attribute": 'standing', "value": generate_tavern_standing()},
        {"attribute": 'description', "value": tavern_description},
        {"attribute": 'detail', "value": tavern_details}
    ]
    return changes