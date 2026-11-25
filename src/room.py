class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
## todo create empty dictionary for adding npc to specific rooms later on in world