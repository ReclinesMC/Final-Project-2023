import os
import time as t

import map
import map as m

header = "{ Dragon Trail }".center(50, "~") + "\n"


def Shop():
    os.system("clear")
    t.sleep(0.1)
    print(header)
    print("Welcome to the shop!")
    t.sleep(1)
    inShop = True
    while inShop:
        print(header)
        print("What would you like to buy?")
        print("This feature will be implemented later")
        t.sleep(2)


def introducePlayer():
    path = ""
    delay = 0
    print("You are a young adventurer")
    t.sleep(delay)
    print("Your goal is to defeat the evil dragon")
    t.sleep(delay)
    print("To do this, you must choose a path...")
    t.sleep(delay * 2)

    while path != "1" and path != "2":
        os.system("clear")
        t.sleep(0.1)
        print("[ The Paths ]".center(60, "="))
        print("💎 Left 💎".center(26) + "|" + "🔥 Right 🔥".center(29))
        print("-".center(29) + "|" + " -".center(29))
        print("|".center(60))
        print("Treasure Rooms".center(29) + "|" + "Creature Rooms".center(29))
        print("Common Loot".center(29) + "|" + "Rare Loot".center(29))
        print("Beginner Friendly".center(29) + "|" + "Many Battles".center(29))
        print("   ".center(60, "="))
        print("\n")
        print("1. Left 💎")
        print("2. Right 🔥")
        path = input("\nChoose a path >>")
        if path == "1":
            m.Map().genLeft()
        elif path == "2":
            m.Map().genRight()
            continue
        else:
            print("\nIncorrect Input! A number is required")
            input("Press ENTER to continue")
        # Izzy was here loser
    gameplay()


def gameplay():
    for i in map.mapLayout:
        input("Press ENTER to continue")
        os.system("clear")
        t.sleep(0.1)
        print(header)
        i.enter()


def actionMenu(currentRoom):
    inRoom = True
    searchedRoom = False
    while inRoom:
        print("What would you like to do?")
        print("1. Look around")
        print("2. Move to the next room")
        print("3. Open the shop")
        choice = input(">")
        if choice == "1":
            if not searchedRoom:
                currentRoom.search()
                searchedRoom = True
            else:
                print("You have already searched this room!")

        elif choice == "2":
            if currentRoom.room != "Boss":
                inRoom = False
            else:
                os.system("clear")
                t.sleep(0.1)
                print(header)
                print("You cannot move forward! You must fight the boss :D")


        elif choice == "3":
            Shop()
