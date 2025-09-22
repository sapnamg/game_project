import sys
import random

class Character():
    def __init__(self, name = "Anon", job = "Jobless", level = 1, experience = 0, life = "Alive", status = "Healthy",
                 health = 121, magic_points = 0, attack = 0, magic = 0, physdefense = 0, magicdefense = 0,
                 equipment = [], items = {"Healing":{"Potion": 1}, "Restoring": {}, "Food":{}},spells = {}, skills = []):
        self.name = name.title()
        self.job = job
            #currently not changeable
        self.level = level
            #need mechanism to increase level
        self.experience = experience
        self.life = life
        self.status = status
        self.health = health
            #consider making health level and job based (do it here conditionally, not in job init)
        self.magic_points = magic_points
            #consider making magic_points level and job based (do it here, not in job init)
        self.attack = attack
        self.magic = magic
        self.physdefense = physdefense
        self.magicdefense = magicdefense
        self.weapon = {}
        self.armor = {}
        self.headgear = {}
        self.equipment = equipment
        self.items = items
        self.spells = spells
        self.skills = skills

    def __str__(self):
        return (f"""\
            Name: {self.name},  Job: {self.job}

            Level: {self.level},    Life: {self.life}
            Experience: {self.experience},  Status: {self.status}

            Health: {self.health},  Magic Points: {self.magic_points}

            Attack: {self.attack},  Magic: {self.magic}
            Physical Defense: {self.physdefense},   Magic Defense: {self.magicdefense}""")

    def get_stats(self):
        return (f"""
            Level: {self.level}
            Experience: {self.experience}
            Attack: {self.attack}
            Magic: {self.magic}
            Physical Defense: {self.physdefense}
            Magic Defense: {self.magicdefense}""")

    @classmethod
    def create_char(cls, job, name):
        match job.lower():
            case "ninja":
                return Ninja(name)
            case "thief":
                return Thief(name)
            case "wizard":
                return Wizard(name)


    @classmethod
    def new_character(cls):
        jobs = [cls.__name__ for cls in Character.__subclasses__()]
        jobs.remove("Enemy")
        while True:
            try:
                name = input("Name: ").capitalize()
                if not name:
                    raise ValueError()
                else:
                    while True:
                        try:
                            job: str = input(f"Select job from: {", ".join(jobs)} - ").capitalize()
                            if job in jobs:
                                print(f"\nInitializing Character...")
                                return cls.create_char(job, name)
                            else:
                                raise ValueError()
                        except ValueError:
                            print("\nError: Invalid job selection!\n")
            except ValueError:
                print("\nPlease enter something for a name!\n")
                continue
            except EOFError:
                print("\nCharacter not created\n")
                break


class Wizard(Character):
    def __init__(self, name):
        super().__init__(job = "Wizard", name = name)
        self.attack = self.level*1.10
        self.magic = self.level*1.70
        self.physdefense = self.level*1.25
        self.magicdefense = self.level*1.70
        self.spells = {Cure: 1}
        self.skills = ["Magic"]
        print (f"""
            {self.name}, {self.job}, Level {self.level} created!
            """)

class Thief(Character):
    def __init__(self, name):
        super().__init__(job = "Thief", name = name)
        self.attack = self.level*1.25
        self.magic = self.level*1.15
        self.physdefense = self.level*1.40
        self.magicdefense = self.level*1.10
        self.spells = {}
        self.skills = ["Steal"]
        print (f"""
            {self.name}, {self.job}, Level {self.level} created!
            """)

class Ninja(Character):
    def __init__(self, name):
        super().__init__(job = "Ninja", name = name)
        self.attack = self.level*1.50
        self.magic = self.level*1.01
        self.physdefense = self.level*1.50
        self.magicdefense = self.level*1.05
        self.spells = {}
        self.skills = ["Assassinate"]
        print (f"""
            {self.name}, {self.job}, Level {self.level} created!
            """)

class Enemy(Character):
    def __init__(self, job, name, level, life, status, health, magic_points, attack, magic, physdefense, magicdefense, equipment, items, spells, skills):
        super().__init__(job = "Enemy", name = name, level=level, life=life, status=status, health=health, magic_points = magic_points, attack=attack, magic=magic, physdefense=physdefense, magicdefense=magicdefense, equipment=equipment, items=items, spells=spells, skills=skills)

    def __str__(self):
        return (f"""\
            Name: {self.name}
            Level: {self.level}
            Status: {self.status}
            Health: {self.health}, Magic Points: {self.magic_points}
            Attack: {self.attack}, Magic: {self.magic}
            Physical Defense: {self.physdefense}, Magic Defense: {self.magicdefense}
            """)
