import functions as f

class Tavern:
    def __init__(self):
        self.name = f.generate_tavern_name()
        self.owner = f.generate_bare_bone_npc()
        
class Npc:
    def __init__(self, name, gender):
        self.basic_identity = f.generate_bare_bone_npc()
        self.name = name or self.basic_identity['name']
        self.gender = gender or self.basic_identity['gender']
        self.age = f.randint(1,100)

