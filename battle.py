from bcolors import bcolors
import random

def battle(foe, ally):
    print(bcolors.BOLD + bcolors.RED + "\nWALKA\n" + bcolors.ENDC)
    alive = int(len(ally))
    defeated_enemies = 0
    defeated_players = 0
    running = True

    while running:
        print("===============================\n\n")
        print("           HP                                         MP")

        for player in ally:
            print(bcolors.BOLD + player.nickname + ":" + bcolors.ENDC)
            player.get_stats()

        print("\n")

        for enemy in foe:
            print(bcolors.BOLD + enemy.character.cl + ":" + bcolors.ENDC)
            enemy.get_enemy_stats()

        print("\n")

        for player in ally:
            while 1:
                print("\n", bcolors.BOLD + player.nickname + ": " + bcolors.ENDC)
                player.choose_action()
                choice = input("\tWybierz akcje: ")
                index = int(choice) - 1

                if index == 0:
                    dmg = player.generate_damage()
                    enemy = player.choose_target(foe)
                    foe[enemy].take_damage(dmg)
                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)

                    if foe[enemy].get_hp() == 0:
                        print(foe[enemy].character.cl, "został pokonany!")
                        del foe[enemy]
                        defeated_enemies += 1

                        if defeated_enemies == int(len(foe)) + 1:
                            print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                            running = False
                    break

                elif index == 1:
                    player.choose_magic()
                    print("        0: Powrót")
                    magic_choice = int(input("\tWybierz umiejętność: ")) - 1

                    if magic_choice == -1:
                        continue

                    if magic_choice < -1 or magic_choice >= int(len(player.magic)):
                        print(bcolors.RED + "Nie ma takiej umiejętności!" + bcolors.ENDC)
                        continue

                    spell = player.magic[magic_choice]
                    magic_dmg = spell.generate_damage() + player.power
                    current_mp = player.get_mp()

                    if spell.cost > current_mp:
                        print(bcolors.RED + "\nZa mało MP\n" + bcolors.ENDC)
                        continue

                    player.reduce_mp(spell.cost)

                    if spell.type == "white":
                        player.heal(magic_dmg)

                        if magic_dmg > player.maxhp:
                            magic_dmg = int(player.maxhp - magic_dmg)

                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)
                        break

                    elif spell.type == "black":
                        enemy = player.choose_target(foe)

                        if spell.name == "Natychmiastowe zabójstwo":
                            chance = random.randrange(0, 5)

                            if chance == 0:
                                foe[enemy].take_damage(magic_dmg)
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                            else:
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                dmg = int(player.get_hp() / 4)
                                player.take_damage(dmg)

                        elif spell.name == "Ogłuszający Krzyk":
                            if player.get_hp() == player.maxhp:
                                dmg = 180

                            else:
                                dmg = int(0.03 * player.get_hp())

                            foe[enemy].take_damage(dmg)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)

                        else:
                            foe[enemy].take_damage(magic_dmg)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)

                        if foe[enemy].get_hp() == 0:
                            print(foe[enemy].character.cl, "został pokonany!")
                            del foe[enemy]
                            defeated_enemies += 1

                            if defeated_enemies == int(len(foe)) + 1:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                running = False
                        break

                elif index == 2:
                    player.choose_item()
                    print("        0: Powrót")
                    item_choice = int(input("\tWybierz przedmiot: ")) - 1

                    if item_choice == -1:
                        continue

                    if item_choice < -1 or item_choice >= int(len(player.items)):
                        print(bcolors.RED + "Nie ma takiego przedmiotu!" + bcolors.ENDC)
                        continue

                    item = player.items[item_choice]["item"]

                    if player.items[item_choice]["quantity"] == 0:
                        print(bcolors.RED + "\n" + "Brak..." + bcolors.ENDC)
                        continue

                    player.items[item_choice]["quantity"] -= 1

                    if item.type == "potion":
                        if item.name == "Mikstura zdrowia":
                            player.heal(item.prop)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.GREEN + "\n" + item.name + " przywraca", str(item.prop), "HP" + bcolors.ENDC)
                            break

                        elif item.name == "Mikstura many":
                            player.mana_restore(item.prop)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + "\n" + item.name + " przywraca", str(item.prop), "MP" + bcolors.ENDC)
                            break

                    elif item.type == "attack":
                        enemy = player.choose_target(foe)
                        foe[enemy].take_damage(item.prop)
                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + item.name + ": " + bcolors.ENDC + str(item.prop) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)

                        if foe[enemy].get_hp() == 0:
                            print(foe[enemy].character.cl, "został pokonany!")
                            del foe[enemy]
                            defeated_enemies += 1

                            if defeated_enemies == int(len(foe)) + 1:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                running = False
                        break

        for enemy in foe:
            while 1:
                enemy_choice = random.randrange(0, 2)

                if enemy_choice == 0:
                    target = random.randrange(0, alive)
                    enemy_dmg = enemy.generate_damage()
                    ally[target].take_damage(enemy_dmg)
                    print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + bcolors.ENDC + str(enemy_dmg) + " DMG => " + bcolors.BOLD + ally[target].nickname + bcolors.ENDC)

                    if ally[target].get_hp() == 0:
                        print(ally[target].nickname, "został pokonany!")
                        del ally[target]
                        alive -= 1
                        defeated_players += 1

                        if defeated_players == int(len(ally)) + 1:
                            print(bcolors.RED + "Przeciwnicy zwyciężają!" + bcolors.ENDC)
                            running = False
                    break

                elif enemy_choice == 1:
                    spell, magic_dmg = enemy.choose_enemy_spell()
                    enemy.reduce_mp(spell.cost)
                    current_mp = enemy.get_mp()

                    if spell.cost > current_mp:
                        continue

                    if spell.type == "white":
                        enemy.heal(magic_dmg)
                        print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)
                        break

                    elif spell.type == "black":
                        target = random.randrange(0, alive)
                        ally[target].take_damage(magic_dmg)
                        print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + ally[target].nickname + bcolors.ENDC)

                        if ally[target].get_hp() == 0:
                            print(ally[target].nickname, "został pokonany!")
                            del ally[target]
                            alive -= 1
                            defeated_players += 1

                            if defeated_players == int(len(ally)) + 1:
                                print(bcolors.RED + "Przeciwnicy zwyciężają!" + bcolors.ENDC)
                                running = False
                        break