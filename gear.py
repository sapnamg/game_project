import sys
import character

class Gear():
    def __init__(self, name="Empty", type = "None", job = [], attack=0, magic=0, physdefense=0, magicdefense=0):
        self.name = name.title()
        self.type = type.capitalize()
        self.job = job
        self.attack = attack
        self.magic = magic
        self.physdefense = physdefense
        self.magicdefense = magicdefense

    def __str__(self):
        return (f"{self.type}: {self.name} -- For: {", ".join(self.job)}, Attack: {self.attack}, Magic: {self.magic}, Physical Defense: {self.physdefense}, Magic Defense: {self.magicdefense}")

    def get_equipment_attributes(self):
        attributes = []
        for attribute in self.__dict__:
            if getattr(self, attribute) != 0:
                if attribute == "physdefense":
                    att_display = "Physical Defense"
                elif attribute == "magicdefense":
                    att_display = "Magic Defense"
                else:
                    att_display = attribute
                attributes.append(f"{att_display.capitalize()} = {getattr(self, attribute)}")
        return(f"""{"""
            """.join(attributes)}""")

    @classmethod
    def create_gear(cls):
        print("\nCreate gear!")
        try:
            while True:
                try:
                    type = input("Type (Weapon, Armor, Headgear): ").capitalize()
                    if type not in ["Weapon", "Armor", "Headgear"]:
                        raise ValueError()
                    break
                except ValueError:
                    print("\nInvalid gear type\n")

            name = input("Name: ")

            while True:
                try:
                    job = list(map(str.capitalize, input("List of jobs: ").split(", ")))
                    for person in job:
                        if person not in [cls.__name__ for cls in character.Character.__subclasses__()]:
                            raise ValueError()
                    break
                except ValueError:
                    print(f"\nInvalid job type(s). Please select from {", ".join([cls.__name__ for cls in character.Character.__subclasses__()])}\n")

            while True:
                try:
                    return cls(type = type, name = name, job = job, attack = int(input("Attack: ")), magic = int(input("Magic: ")), physdefense = int(input("Physical Defense: ")), magicdefense = int(input("Magic Defense: ")))
                except ValueError:
                    print("\nError: Invalid value entry\n")

        except EOFError:
            print("\nCanceling creation of equipment\n")

    def add_special(self, special):
        self.special = special


    def store(self, char):
        char.equipment.append(self.__dict__)
        print(f"""
            Picked up equipment:
            {self.get_equipment_attributes()}""")


    def drop(self, char):
        if next((gear for gear in char.equipment if gear["type"]==self.type and gear["name"]==self.name), False):
            try:
                if char.weapon != self.__dict__:
                    while True:
                        answer = input(f"\nAre you sure you want to drop {self.name}? (y/n) ")
                        if answer =="y":
                            char.equipment.remove(self.__dict__)
                            print(f"""
            {self.name} dropped!""")
                            break
                        else:
                            raise EOFError()
                else:
                    print("\nYou can't drop it; you have it equipped!")
            except EOFError:
                print("""
            Canceling equipment drop""")
        else:
            print("\nCan't find that in your inventory to drop!")


    #Currently can only equip on self from own equipment. May later add way to pass equip to team members (need way to store and access team) or change inventory to team inventory
    def equip(self, char):
        #check if self is in char.equipment
        if next((gear for gear in char.equipment if gear["type"]==self.type and gear["name"]==self.name), False):
            #check that job matches char.job
            if next((job for job in self.job if job == char.job), False):
                match self.type:
                    case "Weapon":
                        char.weapon.update(self.__dict__)
                    case "Amor":
                        char.armor.update(self.__dict__)
                    case "Headgear":
                        char.headgear.update(self.__dict__)
                    case _:
                        raise ValueError("\nError, gear type not recognized")
                char.attack += self.attack
                char.magic += self.magic
                char.physdefense += self.physdefense
                char.magicdefense += self.magicdefense
                #special attributes will be in the gear object and applied from within the specific object
                print(f"""
            {self.name} is equipped on {char.name}!
            New stats for {char.name}:\
            {char.get_stats()}""")

            else:
                print("\nCan't equip with this job!")
        else:
            print("\nDoesn't exist in your inventory!")


    def unequip(self, char, type):
        while True:
            try:
                answer = input(f"\nUnequip {type}? (y/n) ")
                if answer == "y":
                    match type:
                        case "Weapon":
                            char.weapon = {}
                        case "Armor":
                            char.armor = {}
                        case "Headgear":
                            char.headgear = {}
                    char.attack -= self.attack
                    char.magic -= self.magic
                    char.physdefense -= self.physdefense
                    char.magicdefense -= self.magicdefense
                    print(f"""
            {self.name} is unequipped from {char.name}!""")
                    break
                else:
                    raise EOFError()
            except EOFError:
                print("""
            Canceling unequip""")
                break
