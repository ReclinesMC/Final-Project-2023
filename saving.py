import os


# need a function to check if there is a save file
# need a function to load the save file
# need a function to save to the save file
# need a function to delete the save file on death
# need a function to check if the save file is valid

def checkSave():
    if os.path.isfile("save.yml"):
        print("Found a save file")
        print("Saving will be implemented later")
        return True
    else:
        return False


def loadSave():
    pass
