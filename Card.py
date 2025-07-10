class Card:
    """Represente une carte"""
    def __init__(self, id:int, name:str, rarity:str, type:str):
        """
        Initialise une carte.
        
        Args:
            id (int): L'id **unique** de la carte.
            name (string): Le nom de la carte.
            rarity (string): La rarete de la carte. Valeurs possible: 
                -"common"
                -"uncommon"
                -"rare"
                -"ultra_rare"
            type (string): Le type/famille de la carte.
            """
        self.id = id
        self.name = name
        self.rarity = rarity
        self.type = type

    def __str__(self):
        """
        Formate la classe en String.
        """
        return f"Id: {self.id} \nName: {self.name} \nRarity: {self.rarity}\nType: {self.type}\n"
    
    def toList(self):
        """
        Renvoie une liste contenant chaque champs de la carte.
        """
        return [self.id, self.name, self.type, self.rarity]
    