class Person:
    def __init__(self, cl, hp, mp, atk, power, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atklow = atk - 10
        self.atkhigh = atk + 10
        self.magic = magic
        self.power = power
        self.items = items
        self.action = ["Atak", "Umiejętności", "Przedmioty"]
        self.cl = cl