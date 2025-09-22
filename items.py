import sys

class Items():
    healing_items =[]
    restoring_items = []
    food_items = []
    max_limit = 15

    types = ["Healing", "Restoring", "Food"]

    def __init__(self, name = "None",type = "None"):
        self.name = name
        self.type = type

    def __str__(self):
        stats = []
        for stat in self.stat_names:
            stat_display = stat
            if stat_display == "physdefense":
                stat_display = "Physical Defense"
            elif stat_display == "magicdefense":
                stat_display = "Magic Defense"
            elif stat_display == "magic_points":
                stat_display = "Magic Points"
            if getattr(self,stat) != 0:
                stats.append(f"{stat_display.capitalize()} = {getattr(self,stat)}")
        return f"""
            {self.type}: {self.name}
            {"""
            """.join(item for item in stats)}"""

    #Method for character to pick up items
    #May eventually change where possible list of items is stored (ie may need to change from char.items)
    def pick_up_item(self, char):
        try:
            if self.name in Items.healing_items:
                if char.items["Healing"][self.name] + 1 <= Items.max_limit:
                    char.items["Healing"][self.name] += 1
                else:
                    char.items["Healing"][self.name] = Items.max_limit
            elif self.name in Items.restoring_items:
                if char.items["Restoring"][self.name] + 1 <= Items.max_limit:
                    char.items["Restoring"][self.name] += 1
                else:
                    char.items["Restoring"][self.name] = Items.max_limit
            elif self.name in Items.food_items:
                if char.items["Food"][self.name] + 1 <= Items.max_limit:
                    char.items["Food"][self.name] += 1
                else:
                    char.items["Food"][self.name] = Items.max_limit
            else:
                raise EOFError()
        except KeyError:
            match self.type:
                case "Healing":
                    char.items["Healing"][self.name] = 1
                case "Restoring":
                    char.items["Restoring"][self.name] = 1
                case "Food":
                    char.items["Food"][self.name] = 1
        except EOFError:
            print ("\nNot a valid item; can't pick up\n")
        print(f"""
            Picked up {self.type}: {self.name}!""")

    #method to apply item stats to a character
    def apply_item(self, char):
        match self.type:
            case "Healing":
                if self.health !=0:
                    char.health += (self.health/100)*char.health
                if self.health !=0:
                    char.magic_points += (self.magic_points/100)*char.magic_points
            case "Restoring":
                if self.life != "":
                    char.life = self.life
                if self.status != "":
                    char.status = self.status
                char.health += (self.health/100)*char.health
            case "Food":
                if self.experience != 0:
                    char.experience += (self.experience/100)*char.experience
                char.level += self.level
                char.attack += self.attack
                char.magic += self.magic
                char.physdefense += self.physdefense
                char.magicdefense += self.magicdefense


    #Method to 'use' item and apply relevant effect to character's stats
    #other_char is placeholder for now until create way to make a team and place to store team members
    def use_item(self, char, recipient = None):
        try:
            char_item = char.items[self.type][self.name]
            if char_item <= 0:
                raise ValueError()
            else:
                #if recipient is from team of characters (including char), recipient stays assigned to charater
                if recipient == ...:
                    ...
                else:
                    #if recipient is not specified or not in team list, need to assign a valid char object to recipient
                    while True:
                        try:
                            while True:
                                answer = input(f"Apply 1 {self.name} of your {char_item} to {char.name}? (y/n) ")
                                if answer == "n":
                                    #need to access list of created characters in team here, otherwise remove this whole loop and assume applied to char
                                    recipient = input(f"Who to apply {self.name} to? ({...}) ").capitalize()
                                    try:
                                        #change to other char from team list
                                        #if recipient str is same as otherchar.name
                                        if recipient == "Jo":
                                            #assign recipient to otherchar
                                            recipient = ...
                                            break
                                        else:
                                            raise ValueError()
                                    except (ValueError, IndexError, TypeError):
                                        print("\nCharacter doesn't exist in your team!\n")
                                elif answer == "y":
                                    recipient = char
                                    break
                                else:
                                    raise ValueError()
                        except ValueError:
                            print("\nType y or n: ")
                            continue
                        except EOFError:
                            print(f"\nCanceling item use\n")
                            break
                        break
                char.items[self.type][self.name] -= 1
                self.apply_item(recipient)
                stats = []
                for stat in self.stat_names:
                    stat_display = stat
                    if stat_display == "physdefense":
                        stat_display = "Physical Defense"
                    elif stat_display == "magicdefense":
                        stat_display = "Magic Defense"
                    elif stat_display == "magic_points":
                        stat_display = "Magic Points"
                    if getattr(self,stat) != 0:
                        stats.append(f"{stat_display.capitalize()} = {getattr(recipient,stat)}")
                print (f"""
            {self.name} used on {recipient.name}!
            {char.name} has {self.name}: {char.items[self.type][self.name]} remaining.
            Changed stats of {recipient.name}:
            {"""
            """.join(item for item in stats)}""")
        except (IndexError, ValueError):
            print(f"\nYou don't have any {self.name}!\n")


#Classes for creating items by game/programmer
class Healing_Item(Items):
    def __init__(self, name, health = 0, magic_points = 0, type = "Healing"):
        super().__init__(name, type)
        self.health = health
        self.magic_points = magic_points
        self.stat_names = ["health", "magic_points"]


class Restoring_Item(Items):
    def __init__(self, name, life = "Alive", status = "Healthy", health = 0, type = "Restoring"):
        super().__init__(name, type)
        self.life = life
        self.status = status
        self.health = health
        self.stat_names = ["health", "life", "status"]


class Food_Item(Items):
    def __init__(self, name, experience = 0, level = 0, attack = 0,  magic = 0, physdefense = 0, magicdefense = 0, type = "Food"):
        super().__init__(name, type)
        self.experience = experience
        self.level = level
        self.attack = attack
        self.magic = magic
        self.physdefense = physdefense
        self.magicdefense = magicdefense
        self.stat_names = ["experience", "level", "attack", "magic", "physdefense", "magicdefense"]

if __name__ == "__main__":
    main()
