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
            player.dodge_chance()
            player.temp_dodge = False

        print("\n")

        for enemy in foe:
            print(bcolors.BOLD + enemy.character.cl + ":" + bcolors.ENDC)
            enemy.get_enemy_stats()
            enemy.dodge_chance()

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
                    if foe[enemy].get_dodge_chance() >= 0 and foe[enemy].get_dodge_chance() < 13:
                        dmg = 0
                        dodge_string = "(Unik)"

                    else:
                        dodge_string = ""

                    foe[enemy].take_damage(dmg)
                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC, str(dodge_string))

                    if foe[enemy].get_hp() == 0:
                        print(bcolors.GREEN + foe[enemy].character.cl, "został pokonany!" + bcolors.ENDC)
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
                        friend = player.choose_ally(ally)
                        ally[friend].heal(magic_dmg)

                        if magic_dmg > player.maxhp:
                            magic_dmg = int(player.maxhp - magic_dmg)

                        print(bcolors.BOLD + player.nickname + ": " + ally[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)
                        break

                    elif spell.type == "black":
                        enemy = player.choose_target(foe)

                        if spell.name == "Natychmiastowe zabójstwo":
                            chance = random.randrange(0, 10)
                            if foe[enemy].get_hp() == foe[enemy].get_max_hp():
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                dmg = int(player.get_hp() / 4)
                                player.take_damage(dmg)

                            elif foe[enemy].get_hp() <= int(0.9 * foe[enemy].get_max_hp()):
                                if foe[enemy].get_hp() <= int(0.8 * foe[enemy].get_max_hp()):
                                    if foe[enemy].get_hp() <= int(0.7 * foe[enemy].get_max_hp()):
                                        if foe[enemy].get_hp() <= int(0.6 * foe[enemy].get_max_hp()):
                                            if foe[enemy].get_hp() <= int(0.5 * foe[enemy].get_max_hp()):
                                                if foe[enemy].get_hp() <= int(0.4 * foe[enemy].get_max_hp()):
                                                    if foe[enemy].get_hp() <= int(0.3 * foe[enemy].get_max_hp()):
                                                        if foe[enemy].get_hp() <= int(0.2 * foe[enemy].get_max_hp()):
                                                            if foe[enemy].get_hp() <= int(0.1 * foe[enemy].get_max_hp()):
                                                                if chance >= 0 and chance < 9:
                                                                    foe[enemy].take_damage(magic_dmg)
                                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                                else:
                                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                    dmg = int(player.get_hp() / 4)
                                                                    player.take_damage(dmg)
                                                        else:
                                                            if chance >= 0 and chance < 8:
                                                                foe[enemy].take_damage(magic_dmg)
                                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                            else:
                                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                dmg = int(player.get_hp() / 4)
                                                                player.take_damage(dmg)
                                                    else:
                                                        if chance >= 0 and chance < 7:
                                                            foe[enemy].take_damage(magic_dmg)
                                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                        else:
                                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                            dmg = int(player.get_hp() / 4)
                                                            player.take_damage(dmg)
                                                else:
                                                    if chance >= 0 and chance < 6:
                                                        foe[enemy].take_damage(magic_dmg)
                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                    else:
                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                        dmg = int(player.get_hp() / 4)
                                                        player.take_damage(dmg)
                                            else:
                                                if chance >= 0 and chance < 5:
                                                    foe[enemy].take_damage(magic_dmg)
                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                else:
                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                    dmg = int(player.get_hp() / 4)
                                                    player.take_damage(dmg)
                                        else:
                                            if chance >= 0 and chance < 4:
                                                foe[enemy].take_damage(magic_dmg)
                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                            else:
                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                dmg = int(player.get_hp() / 4)
                                                player.take_damage(dmg)
                                    else:
                                        if chance >= 0 and chance < 3:
                                            foe[enemy].take_damage(magic_dmg)
                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                        else:
                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                            dmg = int(player.get_hp() / 4)
                                            player.take_damage(dmg)
                                else:
                                    if chance == 0 or chance == 1:
                                        foe[enemy].take_damage(magic_dmg)
                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                    else:
                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                        dmg = int(player.get_hp() / 4)
                                        player.take_damage(dmg)
                            else:
                                if chance == 0:
                                    foe[enemy].take_damage(magic_dmg)
                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                else:
                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                    dmg = int(player.get_hp() / 4)
                                    player.take_damage(dmg)

                        elif spell.name == "'Tanio skóry nie sprzedam'":
                            if foe[enemy].get_dodge_chance() >= 0 and foe[enemy].get_dodge_chance() < 13:
                                dmg = 0
                                dodge_string = "(Unik)"

                            else:
                                dmg = int(0.15 * player.get_hp())
                                dodge_string = ""

                            foe[enemy].take_damage(dmg)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC, str(dodge_string))

                        else:
                            if foe[enemy].get_dodge_chance() >= 0 and foe[enemy].get_dodge_chance() < 13:
                                magic_dmg = 0
                                dodge_string = "(Unik)"

                            else:
                                dodge_string = ""

                            foe[enemy].take_damage(magic_dmg)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC, str(dodge_string))

                        if foe[enemy].get_hp() == 0:
                            print(bcolors.GREEN + foe[enemy].character.cl, "został pokonany!" + bcolors.ENDC)
                            del foe[enemy]
                            defeated_enemies += 1

                            if defeated_enemies == int(len(foe)) + 1:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                running = False
                        break

                    elif spell.type == "block":
                        player.temp_dodge = True
                        break

                    elif spell.type == "HP steal":
                        enemy = player.choose_target(foe)
                        friend = player.choose_ally(ally)
                        magic_dmg = 250
                        foe[enemy].take_damage(magic_dmg)
                        heal = int(magic_dmg/1.5)
                        ally[friend].heal(heal)

                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)
                        print(bcolors.BOLD + player.nickname + ": " + ally[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(heal) + " HP" + bcolors.ENDC)

                        if foe[enemy].get_hp() == 0:
                            print(bcolors.GREEN + foe[enemy].character.cl, "został pokonany!" + bcolors.ENDC)
                            del foe[enemy]
                            defeated_enemies += 1

                        if defeated_enemies == int(len(foe)) + 1:
                            print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                            running = False
                        break

                    elif spell.type == "MP steal":
                        enemy = player.choose_target(foe)
                        friend = player.choose_ally(ally)
                        magic_dmg = 50

                        if enemy.get_mp() < magic_dmg:
                            magic_dmg = enemy.get_mp()

                        foe[enemy].reduce_mp(magic_dmg)
                        mana = int(magic_dmg/1.75)
                        ally[friend].mana_restore(mana)

                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " MP <= " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)
                        print(bcolors.BOLD + player.nickname + ": " + ally[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uzyskał " + str(mana) + " MP" + bcolors.ENDC)
                        break

                    elif spell.type == "stun":
                        enemy = player.choose_target(foe)
                        if foe[enemy].get_dodge_chance() >= 0 and foe[enemy].get_dodge_chance() < 13:
                            dodge_string = "(Unik)"

                        else:
                            dodge_string = ""
                            foe[enemy].stunned = True

                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + bcolors.ENDC + " => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC, str(dodge_string))
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
                            if player.character.buff == "Woda":
                                regeneration = int((item.prop / 10) + item.prop)
                                player.heal(regeneration)
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.GREEN + "\n" + item.name + " przywraca", str(regeneration), "HP" + bcolors.ENDC)
                                break

                            else:
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
                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.YELLOW + item.name + ": " + bcolors.ENDC + str(item.prop) + " DMG => " + bcolors.BOLD + bcolors.RED + foe[enemy].character.cl + bcolors.ENDC)

                        if foe[enemy].get_hp() == 0:
                            print(bcolors.GREEN + foe[enemy].character.cl, "został pokonany!" + bcolors.ENDC)
                            del foe[enemy]
                            defeated_enemies += 1

                            if defeated_enemies == int(len(foe)) + 1:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                running = False
                        break

        for enemy in foe:
            if enemy.stunned == True:
                enemy.stunned = False
                print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC, "- brak akcji")

            else:
                while 1:
                    enemy_choice = random.randrange(0, 2)
                    if enemy_choice == 0:
                        target = random.randrange(0, alive)
                        enemy_dmg = enemy.generate_damage()
                        dodge_endline = 13
                        if ally[target].temp_dodge == True:
                            ally[target].dodge_chance()
                            dodge_endline += 67

                        if ally[target].buff == "Wiatr":
                            dodge_endline += 15

                        if ally[target].get_dodge_chance() >= 0 and ally[target].get_dodge_chance() < dodge_endline:
                            enemy_dmg = 0
                            dodge_string = "(Unik)"

                        else:
                            dodge_string = ""

                        ally[target].take_damage(enemy_dmg)
                        print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + bcolors.ENDC + str(enemy_dmg) + " DMG => " + bcolors.BOLD + ally[target].nickname + bcolors.ENDC, str(dodge_string))

                        if ally[target].get_hp() == 0:
                            print(bcolors.RED + ally[target].nickname, "został pokonany!" + bcolors.ENDC)
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

                            if enemy.get_hp() == enemy.get_max_hp():
                                continue

                            enemy.heal(magic_dmg)
                            print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)
                            break

                        elif spell.type == "black":
                            target = random.randrange(0, alive)
                            dodge_endline = 13
                            if ally[target].temp_dodge == True:
                                ally[target].dodge_chance()
                                dodge_endline += 67

                            if ally[target].buff == "Wiatr":
                                dodge_endline += 15

                            if ally[target].get_dodge_chance() >= 0 and ally[target].get_dodge_chance() < dodge_endline:
                                magic_dmg = 0
                                dodge_string = "(Unik)"

                            else:
                                dodge_string = ""

                            ally[target].take_damage(magic_dmg)
                            print(bcolors.BOLD + bcolors.RED + enemy.character.cl + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + ally[target].nickname + bcolors.ENDC, str(dodge_string))

                            if ally[target].get_hp() == 0:
                                print(bcolors.RED + ally[target].nickname, "został pokonany!" + bcolors.ENDC)
                                del ally[target]
                                alive -= 1
                                defeated_players += 1

                                if defeated_players == int(len(ally)) + 1:
                                    print(bcolors.RED + "Przeciwnicy zwyciężają!" + bcolors.ENDC)
                                    running = False
                            break

        for player in ally:
                if player.character.buff == "Ziemia":
                    player.heal(20)
                    player.mana_restore(20)

                elif player.character.buff == "Woda":
                    player.heal(22)
                    player.mana_restore(35)

                elif player.character.buff == "Ogień":
                    player.heal(20)
                    player.mana_restore(17)

                elif player.character.buff == "Wiatr":
                    player.heal(20)
                    player.mana_restore(40)

        for enemy in foe:
            enemy.heal(25)
            enemy.mana_restore(20)