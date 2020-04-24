from bcolors import bcolors
import random

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

    def generate_damage(self):
        return random.randrange(self.atklow, self.atkhigh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.BLUE + bcolors.BOLD + "    AKCJE:" + bcolors.ENDC)
        for item in self.action:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.BLUE + bcolors.BOLD + "    UMIEJĘTNOŚCI:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(koszt:", str(spell.cost) + ")")
            i += 1