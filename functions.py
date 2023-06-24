# The function that pick an element in a list
from random import choice, randint

# Tables to generate a name
first_nouns = ['Skull', 'Sword', 'Castle', 'Dragon', 'Lion', 'Rose']
second_nouns = ['Harpy', 'Shield', 'Torch', 'Goblet', 'Scepter', 'Crown']

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
    first_noun = choice(first_nouns)
    second_noun = choice(second_nouns)
    tavern_name = f"The {first_noun} & the {second_noun}"
    return tavern_name