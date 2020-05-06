from person import Person
from magic import Spell
from inventory import Item
from player import Player
from description import description
from battle import battle
from battle2 import PvP
from cube import cube
from bcolors import bcolors
import random

# Umiejętności
power_hit = Spell("Potężne Uderzenie", 30, 180, "black")
smash = Spell("Miazga", 40, 220, "black")
ignite = Spell("Podpalenie", 30, 110, "black")
meteor = Spell("Meteor", 40, 200, "black")
smite = Spell("Porażenie", 35, 190, "black")
thunder = Spell("Błyskawica", 45, 280, "black")
element_ball = Spell("Kula Żywiołów", 50, 340, "black")
tempest = Spell("Nawałnica Stali", 70, 500, "black")
penetration = Spell("Penetracja", 85, 650, "black")
assassination = Spell("Natychmiastowe zabójstwo", 250, 9999999999999999999999999999, "black")
shout = Spell("'Tanio skóry nie sprzedam'", 220, 0, "black")
carnage = Spell("Rzeź", 50, 250, "black")
stone_fists = Spell("Kamienne Pięści", 40, 200, "black")
cure = Spell("Uleczenie", 55, 300, "white")
heal = Spell("Uzdrowienie", 200, 9999999999999999999999999999999, "white")
block = Spell("Garda", 20, 0, "block")
HP_steal = Spell("Kradzież życia", 50, 250, "HP steal")
MP_steal = Spell("Kradzież many", 25, 50, "MP steal")
stun = Spell("Ogłuszenie", 120, 0, "stun")

# Przedmioty
health_potion = Item("Mikstura zdrowia", "potion", "Przywraca 150 HP", 150)
mana_potion = Item("Mikstura many", "potion", "Przywraca 50 MP", 50)
grenade = Item("Granat", "attack", "Zadaje 300 DMG", 300)

player_items = [{"item": health_potion, "quantity": 2},
                {"item": mana_potion, "quantity": 2},
                {"item": grenade, "quantity": 1}]

# Klasy postaci
warrior_soil = Person("Wojownik", "Ziemia", 4250, 250, 45, 45, 0, [], [power_hit, smash, block], player_items)
sorcerer_soil = Person("Mag", "Ziemia", 3150, 400, 15, 90, 0, [], [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_soil = Person("Skrytobójca", "Ziemia", 2900, 350, 50, 55, 0, [], [smite, tempest, penetration, assassination], player_items)
paladin_soil = Person("Paladyn", "Ziemia", 3450, 300, 30, 35, 0, [], [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_soil = Person("Osiłek", "Ziemia", 4650, 300, 30, 0, 0, [], [shout, cure, block], player_items)
fighter_soil = Person("Pięściarz", "Ziemia", 4000, 150, 80, 10, 0, [], [power_hit, carnage, stone_fists, block], player_items)
rogue_soil = Person("Łotrzyk", "Ziemia", 2950, 190, 40, 20, 0, [], [ignite, HP_steal, MP_steal, stun], player_items)

warrior_water = Person("Wojownik", "Woda", 3900, 350, 45, 45, 0, [], [power_hit, smash, block], player_items)
sorcerer_water = Person("Mag", "Woda", 2800, 500, 15, 90, 0, [], [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_water = Person("Skrytobójca", "Woda", 2550, 450, 50, 55, 0, [], [smite, tempest, penetration, assassination], player_items)
paladin_water = Person("Paladyn", "Woda", 3100, 400, 30, 35, 0, [], [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_water = Person("Osiłek", "Woda", 4300, 400, 30, 0, 0, [], [shout, cure, block], player_items)
fighter_water = Person("Pięściarz", "Woda", 3550, 250, 80, 10, 0, [], [power_hit, carnage, stone_fists, block], player_items)
rogue_water = Person("Łotrzyk", "Woda", 2600, 290, 40, 20, 0, [], [ignite, HP_steal, MP_steal, stun], player_items)

warrior_fire = Person("Wojownik", "Ogień", 3900, 250, 70, 50, 0, [], [power_hit, smash, block], player_items)
sorcerer_fire = Person("Mag", "Ogień", 2800, 400, 40, 99, 0, [], [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_fire = Person("Skrytobójca", "Ogień", 2550, 350, 75, 60, 0, [], [smite, tempest, penetration, assassination], player_items)
paladin_fire = Person("Paladyn", "Ogień", 3100, 300, 55, 40, 0, [], [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_fire = Person("Osiłek", "Ogień", 4300, 300, 55, 0, 0, [], [shout, cure, block], player_items)
fighter_fire = Person("Pięściarz", "Ogień", 3650, 150, 105, 11, 0, [], [power_hit, carnage, stone_fists, block], player_items)
rogue_fire = Person("Łotrzyk", "Ogień", 2600, 190, 65, 22, 0, [], [ignite, HP_steal, MP_steal, stun], player_items)

warrior_wind = Person("Wojownik", "Wiatr", 3900, 250, 45, 45, 0, [], [power_hit, smash, block], player_items)
sorcerer_wind = Person("Mag", "Wiatr", 2800, 400, 15, 90, 0, [], [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_wind = Person("Skrytobójca", "Wiatr", 2550, 350, 50, 55, 0, [], [smite, tempest, penetration, assassination], player_items)
paladin_wind = Person("Paladyn", "Wiatr", 3100, 300, 30, 35, 0, [], [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_wind = Person("Osiłek", "Wiatr", 4300, 300, 30, 0, 0, [], [shout, cure, block], player_items)
fighter_wind = Person("Pięściarz", "Wiatr", 3650, 150, 80, 10, 0, [], [power_hit, carnage, stone_fists, block], player_items)
rogue_wind = Person("Łotrzyk", "Wiatr", 2700, 190, 40, 20, 0, [], [ignite, HP_steal, MP_steal, stun], player_items)

# Przeciwnicy
goblin = Person("Goblin", [], 2100, 200, 55, 0, 0, [], [smite, power_hit], [])
straznik = Person("Strażnik", [], 2300, 100, 70, 10, 0, [], [power_hit, smash], [])
chlop = Person("Chłop", [], 2500, 100, 80, 0, 20, [], [power_hit, stun, stone_fists], [])
elf = Person("Elf", [], 3000, 60, 100, 0, 0, [], [cure, ignite], [])
gregory = Person("Gregory", [], 5000, 300, 100, 40, 0, [], [power_hit, stun, smash], [])
imp = Person("Imp", [], 2000, 100, 55, 10, 0, [], [ignite], [])
twoiia = Person("Twoiia", [], 4500, 400, 22, 80, 0, [], [ignite, smite, meteor, thunder, element_ball], [])
maci = Person("Anton Maci", [], 6000, 200, 100, 10, 0, [], [power_hit, smash], [])
moravon = Person("Moravon", [], 6000, 200, 100, 20, 0, [], [carnage], [])


enemies = [elf, goblin, chlop, straznik, imp, twoiia, gregory, maci, moravon]

# Menu
while 1:
    print("[Dowolny Przycisk] Start")
    print("[1] Klasy")
    print("[2] Żywioły")
    v = input()

    if v == '1':
        print(bcolors.BOLD + "Klasy postaci: " + bcolors.ENDC)
        print("[1] Wojownik")
        print("[2] Mag")
        print("[3] Skrytobójca")
        print("[4] Paladyn")
        print("[5] Osiłek")
        print("[6] Pięściarz")
        print("[7] Łotrzyk")
        print("[0] Powrót")
        c = input()

        if c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7':
            description(c)

        elif c == '0':
            continue

        else:
            print(bcolors.BOLD + bcolors.RED + "Nie ma takiej klasy!\n" + bcolors.ENDC)
            continue

    elif v == '2':
        description(str(8))

    else:
        break

# Inicjacja graczy
while 1:
    players_quantity = input(bcolors.BOLD + "Podaj ilość graczy(1-5): " + bcolors.ENDC)
    if players_quantity == '1' or players_quantity == '2' or players_quantity == '3' or players_quantity == '4' or players_quantity == '5':
        break

    else:
        print(bcolors.BOLD + bcolors.RED + "Nieprawidłowa liczba!\n" + bcolors.ENDC)

players = []
i = 1

while i <= int(players_quantity):
    name = input(bcolors.BOLD + "Gracz " + str(i) + ": " + bcolors.ENDC)
    print(bcolors.BOLD + "Wybierz klasę swojej postaci:" + bcolors.ENDC)
    print("[1] Wojownik")
    print("[2] Mag")
    print("[3] Skrytobójca")
    print("[4] Paladyn")
    print("[5] Osiłek")
    print("[6] Pięściarz")
    print("[7] Łotrzyk")

    while 1:
        character = input()

        if character == '1':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, warrior_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, warrior_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, warrior_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, warrior_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        elif character == '2':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, sorcerer_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, sorcerer_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, sorcerer_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, sorcerer_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        elif character == '3':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, assassin_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, assassin_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, assassin_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, assassin_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        elif character == '4':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, paladin_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, paladin_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, paladin_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, paladin_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        elif character == '5':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, tank_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, tank_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, tank_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, tank_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        elif character == '6':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, fighter_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, fighter_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, fighter_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, fighter_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        if character == '7':
            print(bcolors.BOLD + "Wybierz żywioł:" + bcolors.ENDC)
            print("[1] Ziemia")
            print("[2] Woda")
            print("[3] Ogień")
            print("[4] Wiatr")

            while 1:
                element = input()

                if element == '1':
                    player = Player(name, rogue_soil)
                    players.append(player)
                    i += 1
                    break

                elif element == '2':
                    player = Player(name, rogue_water)
                    players.append(player)
                    i += 1
                    break

                elif element == '3':
                    player = Player(name, rogue_fire)
                    players.append(player)
                    i += 1
                    break

                elif element == '4':
                    player = Player(name, rogue_wind)
                    players.append(player)
                    i += 1
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nie ma takiego żywiołu!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz żywioł ponownie!" + bcolors.ENDC)
            break

        else:
            print(bcolors.BOLD + bcolors.RED + "Nie ma takiej klasy!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz klasę ponownie!" + bcolors.ENDC)

print(bcolors.BOLD + "Gracz", "\t\t", "Klasa" + bcolors.ENDC)
fighters = []

for i in range(len(players)):
    print(players[i].nickname, "\t\t", players[i].character.cl, "-", players[i].character.buff)
    fighters.append(players[i])

print("\n")
while 1:
    print("[1] Walka")
    print("[2] Rzut Kostką")
    print("[3] Odpoczynek")
    x = input()
    if x == '1':
        print("[1] Gracz vs Gracz")
        print("[2] Gracz vs NPC")
        y = input()
        if y == '1':
            fighters1 = []
            fighters2 = []
            print(bcolors.BOLD + "Drużyna 1" + bcolors.ENDC)
            while 1:
                z = int(input(bcolors.BOLD + "Podaj ilość graczy: " + bcolors.ENDC))
                if z <= int(players_quantity) - 1 or z > 0:
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nieprawidłowa liczba!\n" + bcolors.ENDC)

            for k in range(len(players)):
                print(str(k + 1) + ". " + players[k].nickname)

            i = 1
            while i <= z:
                f = int(input("Gracz: "))
                fighters1.append(players[f - 1])
                i += 1

            print(bcolors.BOLD + "Drużyna 2" + bcolors.ENDC)
            while 1:
                q = int(input(bcolors.BOLD + "Podaj ilość graczy: " + bcolors.ENDC))
                if q <= int(players_quantity) - 1 or q > 0:
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nieprawidłowa liczba!\n" + bcolors.ENDC)

            for k in range(len(players)):
                print(str(k + 1) + ". " + players[k].nickname)

            i = 1
            while i <= q:
                f = int(input("Gracz: "))
                fighters2.append(players[f - 1])
                i += 1

            PvP(fighters2, fighters1)

        elif y == '2':
            fighters1 = []
            fighters2 = []
            while 1:
                z = int(input(bcolors.BOLD + "Podaj ilość graczy: " + bcolors.ENDC))
                if z <= int(players_quantity) or z >= int(players_quantity):
                    break

                else:
                    print(bcolors.BOLD + bcolors.RED + "Nieprawidłowa liczba!\n" + bcolors.ENDC)

            for k in range(len(players)):
                print(str(k + 1) + ". " + players[k].nickname)

            i = 1
            while i <= z:
                f = int(input("Gracz: "))
                fighters1.append(players[f - 1])
                i += 1

            z = int(input(bcolors.BOLD + "Podaj ilość przeciwników: " + bcolors.ENDC))

            for k in range(len(enemies)):
                print(str(k + 1) + ". " + enemies[k].cl)

            i = 1
            while i <= z:
                f = int(input("Przeciwnik: "))
                fighters2.append(Player([], enemies[f - 1]))
                i += 1

            battle(fighters2, fighters1)

    elif x == '2':
        print("Wybierz ilość kostek")
        print("[1] 2 kostki")
        print("[2] 3 kostki")
        print("[3] 4 kostki")
        dice = int(input())
        cube(dice)

    elif x == '3':
        for i in range(len(players)):
            players[i].heal(11111111)
            players[i].mana_restore(111111111111)