from person import Person
from magic import Spell
from inventory import Item
from player import Player
from cube import cube
from bcolors import bcolors

# Umiejętności
power_hit = Spell("Potężne Uderzenie", 20, 155, "black")
smash = Spell("Miazga", 30, 200, "black")
ignite = Spell("Podpalenie", 20, 110, "black")
meteor = Spell("Meteor", 30, 200, "black")
smite = Spell("Porażenie", 25, 190, "black")
thunder = Spell("Błyskawica", 35, 300, "black")
fireball = Spell("Kula Ognia", 40, 385, "black")
tempest = Spell("Nawałnica Stali", 70, 500, "black")
penetration = Spell("Penetracja", 80, 650, "black")
assassination = Spell("Natychmiastowe zabójstwo", 230, 9999999999999999999999999999, "black")  # 20% szans na powodzenie
shout = Spell("Ogłuszający Krzyk", 0, 100, "black")                                            # Obrażenia umiejętności są zależne od obecnego HP bohatera
carnage = Spell("Rzeź", 30, 245, "black")
stone_fists = Spell("Kamienne Pięści", 25, 200, "black")
cure = Spell("Uleczenie", 50, 500, "white")
heal = Spell("Uzdrowienie", 150, 9999999999999999999999999999999, "white")

# Przedmioty
health_potion = Item("Mikstura zdrowia", "potion", "Przywraca 150 HP", 150)
mana_potion = Item("Mikstura many", "potion", "Przywraca 50 MP", 50)
grenade = Item("Granat", "attack", "Zadaje 400 DMG", 400)

player_items = [{"item": health_potion, "quantity": 2},
                {"item": mana_potion, "quantity": 2},
                {"item": grenade, "quantity": 1}]

# Klasy postaci
warrior = Person("Wojownik", 4500, 70, 110, 10, {power_hit, smash}, player_items)
sorcerer = Person("Mag", 3000, 350, 20, 150, {ignite, meteor, smite, thunder, fireball}, player_items)
assassin = Person("Skrytobójca", 3100, 230, 155, 45, {smite, tempest, penetration, assassination}, player_items)
paladin = Person("Paladyn", 4000, 250, 80, 30, {power_hit, ignite, meteor, thunder, heal, cure}, player_items)
tank = Person("Obrońca", 5550, 50, 50, 0, {shout, cure}, player_items)
rogue = Person("Łotrzyk", 3500, 150, 175, 20, {power_hit, carnage, stone_fists}, player_items)

# Inicjacja graczy
players_quantity = int(input(bcolors.BOLD + "Podaj ilość graczy(1-5): " + bcolors.ENDC))

while players_quantity < 1 or players_quantity > 5:
    players_quantity = int(input(bcolors.BOLD + bcolors.RED + "Nieprawidłowa liczba!\n" + bcolors.ENDC + bcolors.BOLD + "Podaj ilość graczy ponownie(1-5): " + bcolors.ENDC))

players = []
i = 1

while i <= players_quantity:
    name = str(input(bcolors.BOLD + "Gracz " + str(i) + ": " + bcolors.ENDC))
    print(bcolors.BOLD + "Wybierz klasę swojej postaci:" + bcolors.ENDC)
    print("[1]Wojownik")
    print("[2]Mag")
    print("[3]Skrytobójca")
    print("[4]Paladyn")
    print("[5]Obrońca")
    print("[6]Łotrzyk")

    while 1:
        character = int(input())

        if character == 1:
            player = Player(name, warrior)
            players.append(player)
            i += 1
            break

        elif character == 2:
            player = Player(name, sorcerer)
            players.append(player)
            i += 1
            break

        elif character == 3:
            player = Player(name, assassin)
            players.append(player)
            i += 1
            break

        elif character == 4:
            player = Player(name, paladin)
            players.append(player)
            i += 1
            break

        elif character == 5:
            player = Player(name, tank)
            players.append(player)
            i += 1
            break

        elif character == 6:
            player = Player(name, rogue)
            players.append(player)
            i += 1
            break

        else:
            print(bcolors.BOLD + bcolors.RED + "Nie ma takiej klasy!\n" + bcolors.ENDC + bcolors.BOLD + "Wybierz klasę ponownie!" + bcolors.ENDC)

print(bcolors.BOLD + "Gracz", "\t\t", "Klasa" + bcolors.ENDC)

for i in range(len(players)):
    print(players[i].nickname, "\t\t", players[i].character.cl)