class Person:
    def __init__(self, cl, buff, hp, mp, atk, power, dodge, stunned, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atklow = atk - 10
        self.atkhigh = atk + 10
        self.magic = magic
        self.power = power
        self.dodge = dodge
        self.temp_dodge = dodge
        self.stunned = stunned
        self.items = items
        self.action = ["Atak", "Umiejętności", "Przedmioty"]
        self.cl = cl
        self.buff = buff