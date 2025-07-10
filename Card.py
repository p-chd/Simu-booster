class Card:
    def __init__(self, id, name, rarity, type):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.type = type

    def __str__(self):
        return f"Id: {self.id} \nName: {self.name} \nRarity: {self.rarity}\nType: {self.type}\n"
    
    def toList(self):
        return [self.id, self.name, self.type, self.rarity]
    