import weapons
import map

# Player will have an amount of coins and pearls
# Player will have strength and health
# Inventory will contian weapons, consumables, stars, and rubies, NOT coins or pearls
# Player will have a weapon equipped
# Player will have a name
# Location of the player will always be map.mapLayout[0]
# Player needs a method for taking damage and handling death
# Player needs a method for attacking
# Player needs a method for picking up items
# Player needs a method for using items
# Player needs a method for equipping weapon (will uneqip current weapon)
# Player needs a method for buying items
#

class Person:
    def __init__(self):
        self.weapon = weapons.Pencil()
        self.inventory = []
        self.coins = 0
        self.pearls = 0
        self.strength = 0
        self.health = 100

    def __str__(self):
        return str(self.name)

    def pickUp(self, item):
        self.inventory.append(item)

    def attack(self, enemy):
        damage = self.weapon.damage
        print("You attacked {enemy} for {damage} damage!")
        enemy.takeDamage(damage)

    def takeDamage(self, damage, enemy):
        print("{enemy} attacked you for {damage} damage")
        self.health -= damage
    


Player = Person()
