import items
import game_engine
import character
import actions
import gear
import random
#import csv
#import sys


char = character.Character(name = "Rad", job = "Wizard")
#char2 = character.Character.new_character()
#staff = gear.Gear(name = "Staff", type = "Weapon", job = ["Wizard"], attack = 1, magic = 10)
#sword = gear.Gear(name = "Sword", type = "Weapon", job = ["Ninja", "Thief"], attack = 10, magic = 1)
#dagger = gear.Gear.create_gear()
#sword.store(char)
#staff.store(char)

#gear["staff"].store(char)
#gear["staff"].equip(char)
#print(char.equipment)
#staff.equip(char)
#sword.drop(char)
#staff.unequip(char, "Weapon")
#print(char.weapon, char.attack, char.magic, char.equipment)

#lemon = items.Food_Item(name = "Lemon")
#potion = items.Healing_Item(name = "Potion", health = 10)
#spinach = items.Food_Item("Spinach")
#life_bottle = items.Restoring_Item("Life Bottle")
#potion = items.Healing_Item("Potion")
#print(char.items)
#potion.pick_up_item(char)
#life_bottle.pick_up_item(char)
#print(char.items)

#items["potion"].pick_up_item(char)
#print(char.items)
#lemon.use_item(char)
#potion.use_item(char, char)


def main():
    game_gear = game_engine.gear_generator()
    game_items = game_engine.items_generator()
    game_enemies = game_engine.enemies_generator()
    #print("Create your avatar!")
    #char_1 = character.Character.new_character()
    #print(char_1)
    #for keys, values in game_enemies.items():
    #    print(*values)
    #print(items.Items.restoring_items)
    #for keys, values in game_enemies.items():
    #    for enemy in values:
    #        if enemy.skills == "Magic" and enemy.level >58:
    #            print(enemy)
    game_engine.write_new_item(type = "Food", name = "Pesto")
    game_items = game_engine.items_generator()
    print(*game_items.values(), sep="\n")

def custom_1():
    ...

def custom_2():
    ...

def custom_3():
    ...

if __name__ == "__main__":
    main()
