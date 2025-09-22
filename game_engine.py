import csv
import items
import gear
import character
import sys
import random

#Create list of all items to be used in game and store in csv file. Attributes are fixed and won't be randomized or variable.
def items_generator():
    #Read csv file of all items and store in global variables to be used in game
    with open("items.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        game_items = {}
        for row in reader:
            my_str = row["name"].lower()
            if row["type"] == "Healing":
                game_items[my_str] = items.Healing_Item(name = row["name"], health = int(row["health"]), magic_points = int(row["magic_points"]))
                items.Items.healing_items.append(game_items[my_str].name)
            if row["type"] == "Restoring":
                game_items[my_str] = items.Restoring_Item(name = row["name"], life = row["life"], status = row["status"], health = int(row["health"]))
                items.Items.restoring_items.append(game_items[my_str].name)
            if row["type"] == "Food":
                game_items[my_str] = items.Food_Item(name = row["name"], experience = int(row["experience"]), level = int(row["level"]), attack = int(row["attack"]), magic = int(row["magic"]), physdefense = int(row["physdefense"]), magicdefense = int(row["magicdefense"]))
                items.Items.food_items.append(game_items[my_str].name)
        return game_items


#Writer is availble to write in new items not already in csv file
def write_new_item(type, name, **kwargs):
    with open("items.csv") as readfile:
        reader = csv.DictReader(readfile)
        for row in reader:
            if row["name"] == name:
                print(f"\n{name} already exists!\n")
                return
    for arg in kwargs:
        match arg:
            case "health":
                health = kwargs[arg]
            case experience:
                experience = kwargs[arg]

    with open("items.csv", "a", newline = "") as csvfile:
        fieldnames = ["type", "name", "life", "status", "level", "experience", "health", "magic_points", "attack", "magic", "physdefense", "magicdefense"]
        writer = csv.DictWriter(csvfile, fieldnames, restval = "", extrasaction = "ignore")
        try:
            match type:
                case "Healing":
                    new_item = items.Healing_Item(name, health, type = "Healing")
                case "Restoring":
                    new_item = items.Restoring_Item(life = input("Life: "), status = input("Status: "), health = int(input("Health: ")), type = "Restoring")
                case "Food":
                    new_item = items.Food_Item(name, experience = int(input("Experience: ")), level = int(input("Level: ")), attack = int(input("Attack: ")),  magic = int(input("Magic: ")), physdefense = int(input("Physical Defense: ")), magicdefense = int(input("Magic Defense: ")), type = "Food")
            writer.writerow(new_item.__dict__)
        except ValueError | TypeError:
            print("\nInvalid Input\n")
            return
        print("Remember to regenerate list of game items!")
        try:
            items_generator()
        except Exception:
            with open ("items.csv") as readfile:
                reader = csv.DictReader(readfile)
                for row in reader:
                    if row["name"]==name:
                        row_num = reader.line_num
####need to figure out how to remove written line if generator fails - possibly overwrite with blank line? or 
    #can add functionality to accept sys args for this function later



#Create list of all gear to be used in game. Currently attributes are fixed in imported csv.
def gear_generator():
    #Read csv file of all items and store in global variables to be used in game
    with open("gear.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        game_gear = {}
        for row in reader:
            my_str = row["name"].lower()
            job = row["job"].split(", ")
            game_gear[my_str] = gear.Gear(type = row["type"], name = row["name"], job = job, attack = int(row["attack"]), magic = int(row["magic"]), physdefense = int(row["physdefense"]), magicdefense = int(row["magicdefense"]))
        return game_gear

def write_new_gear(*kwargs):
    #Writer is availble to write in new gear not already in csv file
    #can add functionality to accept sys args for this function later
    with open("gear.csv", "a", newline = "") as csvfile:
        fieldnames = ["type", "name", "job", "attack", "magic", "physdefense", "magicdefense"]
        writer = csv.DictWriter(csvfile, fieldnames, restval = "", extrasaction = "ignore")
        writer.writerow(gear.Gear(*kwargs).__dict__)


#Create list of enemies generated for game. Basic list of enemies is read. Then new list with variability in attributes is written. Choice of items, equipment, skills, spells will be fixed, but randomness in choice will be introduced during gameplay.
def enemies_generator():
    #Read csv file of all enemy bases, create list of new enemies based on that, and store in global variables to be used in game
    fieldnames = ["job", "name", "level", "life", "status", "health", "magic_points", "attack", "magic", "physdefense", "magicdefense", "equipment", "items", "spells", "skills"]
    #erase enemies_list file in case anything exists in there, and rewrite headers:
    with open("enemies_list.csv", "w") as newcsvfile:
        newcsvfile.seek(0)
        newcsvfile.truncate()
        writer = csv.DictWriter(newcsvfile, fieldnames)
        writer.writeheader()
    with open("enemy_base.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        game_enemies = {}
        for row in reader:
            for i in range(20):
                my_str = row["name"].lower()
                equipment = row["equipment"].split(", ")
                    #eventually change this to limited random selection from gear.csv
                items = row["items"].split(", ")
                    #eventually change this to limited random selection from items.csv
                spells = row["spells"].split(", ")
                    #eventually change this to limited selection from list of spells (doesn't currently exist)
                skills = row["skills"].split(", ")
                    #will remain fixed
                level = random.randint(*(int(item) for item in row["level"].split(", ")))
                health = int(row["health"])+level*20+(random.randint(10,(100+(level*10))))
                magic_points = int(row["health"])+level*10 if row["skills"] == "Magic" else row["health"]
                attack = int(level+level*random.randint(4,7)) if row["skills"] != "Magic" else int(level+100/level)
                magic = int(level+level*random.randint(4,7)) if row["skills"] == "Magic" else int(level+100/level)
                physdefense = int(level+level*random.randint(4,7)) if row["skills"] != "Magic" else int(level+100/level)
                magicdefense = int(level+level*random.randint(4,7)) if row["skills"] == "Magic" else int(level+100/level)
                enemy = (character.Enemy(job = row["job"], name = row["name"], level = level, life = row["life"],
                                                       status = row["status"], health = health, magic_points = magic_points, attack = attack, magic = magic,
                                                       physdefense = physdefense, magicdefense = magicdefense, equipment = equipment,
                                                       items = items, spells = row["spells"], skills = row["skills"]))
                try:
                    if game_enemies[my_str]:
                        game_enemies[my_str].append(enemy)
                except KeyError:
                    game_enemies[my_str] = []
                    game_enemies[my_str].append(enemy)
                with open("enemies_list.csv", "a", newline = "") as newcsvfile:
                    writer = csv.DictWriter(newcsvfile, fieldnames, restval = "", extrasaction = "ignore")
                    writer.writerow(enemy.__dict__)
        return game_enemies

def write_new_enemy(job = "Enemy", name = "NoName", level = [1,65], life = "Alive", status = "Healthy", health = 0, magic_points = 0, attack = 0, magic = 0, physdefense = 0, magicdefense = 0, equipment = [], items = [], spells = [], skills = []):
    #Writer is availble to write in new enemies categories not already in enemy_base csv file
    #can add functionality to accept sys args for this function later
    with open("enemy_base.csv", "a", newline = "") as csvfile:
        fieldnames = ["job", "name", "level", "life", "status", "health", "magic_points", "attack", "magic",
                      "physdefense", "magicdefense", "equipment", "items", "spells", "skills"]
        writer = csv.DictWriter(csvfile, fieldnames, restval = "", extrasaction = "ignore")
        writer.writerow(character.Enemy(job, name, level, life, status, health, magic_points, attack, magic, physdefense, magicdefense, equipment, items, spells, skills).__dict__)


def dungeon_generator(level):
    pass

#enemies_generator()

#if __name__ == "__main__":
#    main()
