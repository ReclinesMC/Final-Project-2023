class Enemies:
    def __init__(self, type, modifier):
        self.type = type
        self.modifier = modifier

    def startBattle(self):

    def __str__(self):
        return str(self.type)


class Phoenix(Enemies):
    pass


class Demon(Enemies):
    pass
