import random as r
import os
import time as t
import gui

mapLayout = []

class Map:
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.maps = [Dungeon(), Empty(), Treasure()]

    def genLeft(self):
        global mapLayout
        mapLayout.append(Treasure())
        for i in range(8 + self.difficulty):
            room = r.randint(1, 2)
            mapLayout.append(self.maps[room])
        mapLayout.append(Boss())
        return mapLayout

    def genRight(self):
        global mapLayout
        mapLayout.append(Dungeon())
        for i in range(8 + self.difficulty):
            room = r.randint(0, 1)
            mapLayout.append(self.maps[room])
        mapLayout.append(Boss())
        return mapLayout


class Rooms:
    def __init__(self):
        self.room = None

    def enter(self):
        gui.actionMenu(self)

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
      
    def search(self):
      pickup = True
      print("You have found treasure!")
      print("It happens to be a weapon! (probably because im too lazy to implement anything else")
      while pickup:
        print("Would you like to pick it up? (y/n)")
        pick = input(">")
        
        if pick.lower() == "y":
          print("Item picked up")
          pickup = False
          
        
        elif pick.lower() == "n":
          print("Item not picked up.")
          pickup = False
          
        
        else:
          print("Invalid input\n")


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


class Shop:
    def __init__(self):
        os.system("clear")
        t.sleep(0.1)
        print("Welcome to the shop!")
        t.sleep(1)
        print("What would you like to buy?")
        print("This feature will be implemented later")
        t.sleep(2)
      
      