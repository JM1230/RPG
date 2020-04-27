from person import Person
from magic import Spell
from inventory import Item
from player import Player
from description import description
from battle import battle
from cube import cube
from bcolors import bcolors
import random

# Umiejętności
power_hit = Spell("Potężne Uderzenie", 20, 155, "black")
smash = Spell("Miazga", 30, 200, "black")
ignite = Spell("Podpalenie", 20, 110, "black")
meteor = Spell("Meteor", 30, 200, "black")
smite = Spell("Porażenie", 25, 190, "black")
thunder = Spell("Błyskawica", 35, 300, "black")
element_ball = Spell("Kula Żywiołów", 40, 385, "black")
tempest = Spell("Nawałnica Stali", 70, 500, "black")
penetration = Spell("Penetracja", 80, 650, "black")
assassination = Spell("Natychmiastowe zabójstwo", 150, 9999999999999999999999999999, "black")  # 20% szans na powodzenie
shout = Spell("'Tanio skóry nie sprzedam'", 200, 0, "black")                                            # Obrażenia umiejętności są zależne od obecnego HP bohatera
carnage = Spell("Rzeź", 35, 250, "black")
stone_fists = Spell("Kamienne Pięści", 30, 200, "black")
cure = Spell("Uleczenie", 50, 300, "white")
heal = Spell("Uzdrowienie", 200, 9999999999999999999999999999999, "white")
block = Spell("Garda", 10, 0, "block")

# Przedmioty
health_potion = Item("Mikstura zdrowia", "potion", "Przywraca 150 HP", 150)
mana_potion = Item("Mikstura many", "potion", "Przywraca 50 MP", 50)
grenade = Item("Granat", "attack", "Zadaje 300 DMG", 300)

player_items = [{"item": health_potion, "quantity": 2},
                {"item": mana_potion, "quantity": 2},
                {"item": grenade, "quantity": 1}]

# Klasy postaci
warrior_soil = Person("Wojownik", "Ziemia", 4350, 300, 35, 45, 0, [power_hit, smash, block], player_items)
sorcerer_soil = Person("Mag", "Ziemia", 3150, 600, 15, 110, 0, [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_soil = Person("Skrytobójca", "Ziemia", 3000, 350, 50, 55, 0, [smite, tempest, penetration, assassination], player_items)
paladin_soil = Person("Paladyn", "Ziemia", 3450, 400, 25, 45, 0, [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_soil = Person("Osiłek", "Ziemia", 4950, 300, 30, 0, 0, [shout, cure], player_items)
fighter_soil = Person("Pięściarz", "Ziemia", 4100, 150, 60, 10, 0, [power_hit, carnage, stone_fists], player_items)

warrior_water = Person("Wojownik", "Woda", 4000, 400, 35, 45, 0, [power_hit, smash, block], player_items)
sorcerer_water = Person("Mag", "Woda", 2800, 700, 15, 110, 0, [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_water = Person("Skrytobójca", "Woda", 2650, 450, 50, 55, 0, [smite, tempest, penetration, assassination], player_items)
paladin_water = Person("Paladyn", "Woda", 3100, 500, 25, 45, 0, [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_water = Person("Osiłek", "Woda", 4600, 400, 30, 0, 0, [shout, cure], player_items)
fighter_water = Person("Pięściarz", "Woda", 3750, 250, 60, 10, 0, [power_hit, carnage, stone_fists], player_items)

warrior_fire = Person("Wojownik", "Ogień", 4000, 300, 55, 45, 0, [power_hit, smash, block], player_items)
sorcerer_fire = Person("Mag", "Ogień", 2800, 600, 35, 110, 0, [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_fire = Person("Skrytobójca", "Ogień", 2650, 350, 70, 55, 0, [smite, tempest, penetration, assassination], player_items)
paladin_fire = Person("Paladyn", "Ogień", 3100, 400, 45, 45, 0, [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_fire = Person("Osiłek", "Ogień", 4600, 300, 50, 0, 0, [shout, cure], player_items)
fighter_fire = Person("Pięściarz", "Ogień", 3750, 150, 80, 10, [], [power_hit, carnage, stone_fists], player_items)

warrior_wind = Person("Wojownik", "Wiatr", 4000, 300, 35, 45, 0, [power_hit, smash, block], player_items)
sorcerer_wind = Person("Mag", "Wiatr", 2800, 600, 15, 110, 0, [ignite, meteor, smite, thunder, element_ball], player_items)
assassin_wind = Person("Skrytobójca", "Wiatr", 2650, 350, 50, 55, 0, [smite, tempest, penetration, assassination], player_items)
paladin_wind = Person("Paladyn", "Wiatr", 3100, 400, 25, 45, 0, [power_hit, ignite, meteor, thunder, heal, cure], player_items)
tank_wind = Person("Osiłek", "Wiatr", 4600, 300, 30, 0, 0, [shout, cure], player_items)
fighter_wind = Person("Pięściarz", "Wiatr", 3750, 150, 60, 10, 0, [power_hit, carnage, stone_fists], player_items)

# Przeciwnicy (tymczasowo)
imp = Person("Imp", [], 2000, 100, 55, 0, 0, [smite], [])
demon = Person("Demon", [], 8000, 300, 50, 0, 0, [ignite, meteor, cure], [])
orc = Person("Ork", [], 7000, 150, 100, 0, 0, [power_hit], [])

enemies = [imp, demon, orc]

# Menu
while 1:
    print(bcolors.BOLD + "Klasy postaci: " + bcolors.ENDC)
    print("[1] Wojownik")
    print("[2] Mag")
    print("[3] Skrytobójca")
    print("[4] Paladyn")
    print("[5] Osiłek")
    print("[6] Pięściarz")
    print("\n[Dowolny Przycisk] Start")

    c = input()

    if c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6':
        description(c)

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

        else:
            print(bcolors.BOLD + bcolors.RED + "Nie ma takiej klasy!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz klasę ponownie!" + bcolors.ENDC)

print(bcolors.BOLD + "Gracz", "\t\t", "Klasa" + bcolors.ENDC)

for i in range(len(players)):
    print(players[i].nickname, "\t\t", players[i].character.cl, "-", players[i].character.buff)

# HISTORIA (tymczasowo brak, ale w tym miejscu musi zostać pierwszy raz wywołana)

# Walka (tymczasowo - Walczyć będą ci gracze, którzy aktualnie znajdują się na polu, na którym wystąpiło zdarzenie walki[albo wszyscy, albo tylko jeden, później sie zdecyduje])
q1 = random.randrange(0, 3)
i = 0
foe = []
foe_list = [{}, {}, {}]

while i <= q1:
    enemy = random.choice(enemies)
    foe_list[i] = Player([], enemy)
    foe.append(foe_list[i])
    i += 1

q2 = random.randrange(0, int(players_quantity))      # tymczasowo do testów - gracze nie będą losowani
i = 0
ally = []

while i <= q2:
    player = random.choice(players)
    ally.append(player)

    if i != 0:
        if ally[i] == ally[i - 1]:
            del ally[i]
        else:
            i += 1
    else:
        i += 1

battle(foe, ally)