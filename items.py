import weapons as w


# Coins are used to buy items from the shop
# Pearls are used to buy rare items from the shop
# Stars are used to boost your max HP
# Rubies are used to boost your damage
# Potion of health heals yourself
# Potion of strength boosts your strength
# Cooked ostrich heals yourself
# Pepperonis heal yourself


# Treasure

class Coin:
    def __str__(self):
        return "A shiny object that allows you to use the shop"

    def __repr__(self):
        return "Coin"


class Pearl:
    def __str__(self):
        return "A rare object that allows you to purchase rare items"

    def __repr__(self):
        return "Pearl"


class Star:
    def __str__(self):
        return "Boosts your max HP while in your inventory"

    def __repr__(self):
        return "Star"


class Ruby:
    def __str__(self):
        return "Boosts your damage while in your inventory"

    def __repr__(self):
        return "Ruby"



class HealthPot:
    def __str__(self):
        return "Gives 50 HP"

    def __repr__(self):
        return "Health Potion"


class StrengthPot:
    def __str__(self):
        return "Gives 10 Strength"

    def __repr__(self):
        return "Strength Potion"


class CookedOstrich:
    def __str__(self):
        return "Gives 20 HP"

    def __repr__(self):
        return "Cooked Ostrich"


class Pepperoni:
    def __str__(self):
        return "Gives 10 HP"

    def __repr__(self):
        return "Pepperoni"


weaponz = [w.CrystalBall(), w.CrystalBall(), w.CrystalBall(), w.CrystalBall(), w.AngryMushroom(), w.AngryMushroom(),
           w.AngryMushroom(), w.AngryMushroom(), w.AngryMushroom(), w.AngryMushroom(), w.AngryMushroom(),
           w.AngryMushroom(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(),
           w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(), w.Kitten(),
           w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(),
           w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(),
           w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(),
           w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil(), w.Pencil()]

consumables = [HealthPot(), HealthPot(), HealthPot(), HealthPot(), StrengthPot(), StrengthPot(), StrengthPot(),
               StrengthPot(), StrengthPot(), StrengthPot(), StrengthPot(), StrengthPot(), CookedOstrich(),
               CookedOstrich(), CookedOstrich(), CookedOstrich(), CookedOstrich(), CookedOstrich(), CookedOstrich(),
               CookedOstrich(), CookedOstrich(), CookedOstrich(), CookedOstrich(), CookedOstrich(), CookedOstrich(),
               CookedOstrich(), CookedOstrich(), CookedOstrich(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(),
               Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(),
               Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(),
               Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni(),
               Pepperoni(), Pepperoni(), Pepperoni(), Pepperoni()]

treasure = [Pearl(), Pearl(), Pearl(), Pearl(), Star(), Star(), Star(), Star(), Star(), Star(), Star(), Star(), Ruby(),
            Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(), Ruby(),
            Ruby(), Ruby(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(),
            Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(),
            Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin(), Coin()]

# lootGenerator= []
# amount = 2
# for i in treasure:
#   amount *= 2
#   for b in range(amount):
#     lootGenerator.append(i)
# print(lootGenerator)
