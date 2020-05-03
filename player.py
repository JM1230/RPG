from bcolors import bcolors
import random

class Player:
    def __init__(self, nickname, character):
        self.nickname = nickname
        self.character = character
        self.hp = character.hp
        self.maxhp = character.maxhp
        self.mp = character.mp
        self.maxmp = character.maxmp
        self.atklow = character.atklow
        self.atkhigh = character.atkhigh
        self.power = character.power
        self.dodge = character.dodge
        self.temp_dodge = character.temp_dodge
        self.stunned = character.stunned
        self.magic = character.magic
        self.items = character.items
        self.action = character.action
        self.buff = character.buff

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp


    def generate_damage(self):
        return random.randrange(self.atklow, self.atkhigh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def mana_restore(self, dmg):
        self.mp += dmg
        if self.mp > self.maxmp:
            self.mp = self.maxmp

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

    def dodge_chance(self):
        chance = random.randrange(0, 100)
        self.dodge = chance

    def get_dodge_chance(self):
        return self.dodge

    def choose_action(self):
        i = 1
        print(bcolors.YELLOW + bcolors.BOLD + "\tAKCJE:" + bcolors.ENDC)
        for item in self.action:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.BLUE + bcolors.BOLD + "\tUMIEJĘTNOŚCI:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(koszt:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.PURPLE + bcolors.BOLD + "\tPRZEDMIOTY:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ":", item["item"].name + ":", item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.RED + bcolors.BOLD + "\tCEL:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                if enemy.nickname != []:
                    print("        " + str(i) + ".", enemy.nickname)
                    i += 1

                else:
                    print("        " + str(i) + ".", enemy.character.cl)
                    i += 1

        choice = int(input("\tWybierz cel: ")) - 1
        return choice

    def choose_ally(self, players):
        i = 1
        print("\n" + bcolors.GREEN + bcolors.BOLD + "\tSOJUSZNIK:" + bcolors.ENDC)
        for player in players:
            if player.get_hp() != 0:
                print("        " + str(i) + ".", player.nickname)
                i += 1

        choice = int(input("\tWybierz cel: ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string

        else:
            current_hp = hp_string

        print(bcolors.BOLD + current_hp + " |" + bcolors.RED + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string

        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string

        else:
            current_mp += mp_string

        print(bcolors.BOLD + current_hp + " |" + bcolors.GREEN + hp_bar + bcolors.ENDC + "|        " + bcolors.BOLD + current_mp + " |" + bcolors.BLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost:
            return spell, 0

        if spell.type == "white" and pct > 50:
            self.choose_enemy_spell()

        return spell, magic_dmg