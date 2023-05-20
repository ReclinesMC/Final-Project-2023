import os
import random as r
import time as t

import gui
import items

mapLayout = []


# for each map have a list of items
# weapons = [crystal ball, angry mushroom, pencil, kitten, flaming sword]
# Consumables = [health potion, strength potion, cooked ostrich, pepperonis]
# Treasure = [coin, pearl, star, ruby]

# In treasure rooms player will have a high chance of treasure, normal chance consumables, low chance weapons
# In empty rooms player will have a medium chance of consumables, no chance treasure, no chance weapons
# In dungeon rooms player will have a high chance of weapons, normal chance consumables, low chance weapons

def percentChance(num, success=True, unlucky=False):
    randomNum = r.randint(0, 100)
    if num <= randomNum:
        return success
    else:
        return unlucky


class Map:
    def __init__(self, difficulty=10):
        self.difficulty = difficulty
        self.maps = [Dungeon(), Empty(), Treasure()]

    def genLeft(self):
        global mapLayout
        mapLayout.append(Treasure())
        for i in range(8 + self.difficulty):
            room = percentChance(70, Treasure(), Empty())
            mapLayout.append(room)
        mapLayout.append(Boss())
        print("Have fun!")
        return mapLayout

    def genRight(self):
        global mapLayout
        mapLayout.append(Dungeon())
        for i in range(8 + self.difficulty):
            room = percentChance(70, Dungeon(), Empty())
            mapLayout.append(room)
        mapLayout.append(Boss())
        print("Fear will only get you killed.")
        return mapLayout


class Rooms:
    def __init__(self):
        self.room = None
        self.loot = []

    def enter(self):
        gui.actionMenu(self)

    def search(self):
        r.shuffle(items.weaponz)
        r.shuffle(items.consumables)
        r.shuffle(items.treasure)
        if self.room == "Dungeon":
            self.loot = [percentChance(50, r.choice(items.weaponz)), percentChance(50, r.choice(items.weaponz)),
                         percentChance(50, r.choice(items.consumables)), percentChance(30, r.choice(items.treasure))]

        elif self.room == "Treasure":
            self.loot = [percentChance(50, r.choice(items.treasure)), percentChance(50, r.choice(items.treasure)),
                         percentChance(50, r.choice(items.consumables)), percentChance(30, r.choice(items.weaponz))]

        elif self.room == "Empty":
            self.loot = [percentChance(50, r.choice(items.consumables)), percentChance(10, r.choice(items.treasure)),
                         percentChance(10, r.choice(items.weaponz))]

    def __repr__(self):
        return str(self.room)


class Dungeon(Rooms):
    def __init__(self):
        super().__init__()
        self.room = "Dungeon"

    def enter(self):
        print(f"You have entered a {self.room} room")
        super().enter()


class Treasure(Rooms):

    def __init__(self):
        super().__init__()
        self.room = "Treasure"

    def enter(self):
        print(f"You have entered a {self.room} room")
        super().enter()




class Boss(Rooms):
    def __init__(self):
        super().__init__()
        self.room = "Boss"

    def enter(self):
        print(f"You have entered The {self.room} room")
        super().enter()


class Empty(Rooms):
    def __init__(self):
        super().__init__()
        self.room = "Empty"

    def enter(self):
        print(f"You have entered an {self.room} room")
        super().enter()


