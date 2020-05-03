from bcolors import bcolors
import random

def PvP(team2, team1):
    print(bcolors.BOLD + bcolors.RED + "\nWALKA\n" + bcolors.ENDC)
    enemies1 = int(len(team1))
    enemies2 = int(len(team2))
    running = True

    while running:
        print("===============================\n\n")
        print("           HP                                         MP")

        for player in team1:
            print(bcolors.BOLD + player.nickname + ":" + bcolors.ENDC)
            player.get_stats()
            player.dodge_chance()
            player.temp_dodge = False

        print("\n")

        for player in team2:
            print(bcolors.BOLD + player.nickname + ":" + bcolors.ENDC)
            player.get_stats()
            player.dodge_chance()
            player.temp_dodge = False

        print("\n")

        for player in team1:
            if player.stunned == True:
                player.stunned = False
                print("\n", bcolors.BOLD + player.nickname + " - " + bcolors.PURPLE + " Ogłuszony" + bcolors.ENDC)

            else:
                while 1:
                    print("\n", bcolors.BOLD + player.nickname + ": " + bcolors.ENDC)
                    player.choose_action()
                    choice = input("\tWybierz akcje: ")
                    index = int(choice) - 1

                    if index == 0:
                        dmg = player.generate_damage()
                        enemy = player.choose_target(team2)
                        if team2[enemy].get_dodge_chance() >= 0 and team2[enemy].get_dodge_chance() < 13:
                            dmg = 0
                            dodge_string = "(Unik)"
                            team2[enemy].dodge_chance()

                        else:
                            dodge_string = ""

                        team2[enemy].take_damage(dmg)
                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC, str(dodge_string))

                        if team2[enemy].get_hp() == 0:
                            print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                            del team2[enemy]
                            enemies2 -= 1

                            if enemies2 == 0:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                return True
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
                            print(bcolors.RED + "\nZa mało MP!\n" + bcolors.ENDC)
                            continue

                        player.reduce_mp(spell.cost)

                        if spell.type == "white":
                            friend = player.choose_ally(team1)
                            team1[friend].heal(magic_dmg)

                            if magic_dmg > player.maxhp:
                                magic_dmg = int(player.maxhp - magic_dmg)

                            print(bcolors.BOLD + player.nickname + ": " + team1[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)
                            break

                        elif spell.type == "black":
                            enemy = player.choose_target(team2)

                            if spell.name == "Natychmiastowe zabójstwo":
                                chance = random.randrange(0, 10)
                                if team2[enemy].get_hp() == team2[enemy].get_max_hp():
                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                    dmg = int(player.get_hp() / 4)
                                    player.take_damage(dmg)

                                elif team2[enemy].get_hp() <= int(0.9 * team2[enemy].get_max_hp()):
                                    if team2[enemy].get_hp() <= int(0.8 * team2[enemy].get_max_hp()):
                                        if team2[enemy].get_hp() <= int(0.7 * team2[enemy].get_max_hp()):
                                            if team2[enemy].get_hp() <= int(0.6 * team2[enemy].get_max_hp()):
                                                if team2[enemy].get_hp() <= int(0.5 * team2[enemy].get_max_hp()):
                                                    if team2[enemy].get_hp() <= int(0.4 * team2[enemy].get_max_hp()):
                                                        if team2[enemy].get_hp() <= int(0.3 * team2[enemy].get_max_hp()):
                                                            if team2[enemy].get_hp() <= int(0.2 * team2[enemy].get_max_hp()):
                                                                if team2[enemy].get_hp() <= int(0.1 * team2[enemy].get_max_hp()):
                                                                    if chance >= 0 and chance < 9:
                                                                        team2[enemy].take_damage(magic_dmg)
                                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                                    else:
                                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                        dmg = int(player.get_hp() / 4)
                                                                        player.take_damage(dmg)
                                                            else:
                                                                if chance >= 0 and chance < 8:
                                                                    team2[enemy].take_damage(magic_dmg)
                                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                                else:
                                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                    dmg = int(player.get_hp() / 4)
                                                                    player.take_damage(dmg)
                                                        else:
                                                            if chance >= 0 and chance < 7:
                                                                team2[enemy].take_damage(magic_dmg)
                                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                            else:
                                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                dmg = int(player.get_hp() / 4)
                                                                player.take_damage(dmg)
                                                    else:
                                                        if chance >= 0 and chance < 6:
                                                            team2[enemy].take_damage(magic_dmg)
                                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                        else:
                                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                            dmg = int(player.get_hp() / 4)
                                                            player.take_damage(dmg)
                                                else:
                                                    if chance >= 0 and chance < 5:
                                                        team2[enemy].take_damage(magic_dmg)
                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                    else:
                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                        dmg = int(player.get_hp() / 4)
                                                        player.take_damage(dmg)
                                            else:
                                                if chance >= 0 and chance < 4:
                                                    team2[enemy].take_damage(magic_dmg)
                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                else:
                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                    dmg = int(player.get_hp() / 4)
                                                    player.take_damage(dmg)
                                        else:
                                            if chance >= 0 and chance < 3:
                                                team2[enemy].take_damage(magic_dmg)
                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                            else:
                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                dmg = int(player.get_hp() / 4)
                                                player.take_damage(dmg)
                                    else:
                                        if chance == 0 or chance == 1:
                                            team2[enemy].take_damage(magic_dmg)
                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                        else:
                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                            dmg = int(player.get_hp() / 4)
                                            player.take_damage(dmg)
                                else:
                                    if chance == 0:
                                        team2[enemy].take_damage(magic_dmg)
                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                    else:
                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                        dmg = int(player.get_hp() / 4)
                                        player.take_damage(dmg)

                            elif spell.name == "'Tanio skóry nie sprzedam'":
                                if team2[enemy].get_dodge_chance() >= 0 and team2[enemy].get_dodge_chance() < 13:
                                    dmg = 0
                                    dodge_string = "(Unik)"
                                    team2[enemy].dodge_chance()

                                else:
                                    dmg = int(0.15 * player.get_hp())
                                    dodge_string = ""

                                team2[enemy].take_damage(dmg)
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC, str(dodge_string))

                            else:
                                if team2[enemy].get_dodge_chance() >= 0 and team2[enemy].get_dodge_chance() < 13:
                                    magic_dmg = 0
                                    dodge_string = "(Unik)"
                                    team2[enemy].dodge_chance()

                                else:
                                    dodge_string = ""

                                team2[enemy].take_damage(magic_dmg)
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC, str(dodge_string))

                            if team2[enemy].get_hp() == 0:
                                print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                                del team2[enemy]
                                enemies2 -= 1

                                if enemies2 == 0:
                                    print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                    return True
                            break

                        elif spell.type == "block":
                            player.temp_dodge = True
                            break

                        elif spell.type == "HP steal":
                            enemy = player.choose_target(team2)
                            friend = player.choose_ally(team1)
                            magic_dmg = 250
                            team2[enemy].take_damage(magic_dmg)
                            heal = int(magic_dmg/1.5)
                            team1[friend].heal(heal)

                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC)
                            print(bcolors.BOLD + player.nickname + ": " + team1[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(heal) + " HP" + bcolors.ENDC)

                            if team2[enemy].get_hp() == 0:
                                print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                                del team2[enemy]
                                enemies2 -= 1

                            if enemies2 == 0:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                return True
                            break

                        elif spell.type == "MP steal":
                            enemy = player.choose_target(team2)
                            friend = player.choose_ally(team1)
                            magic_dmg = 50

                            if team2[enemy].get_mp() < magic_dmg:
                                magic_dmg = team2[enemy].get_mp()

                            team2[enemy].reduce_mp(magic_dmg)
                            mana = int(magic_dmg/1.75)
                            team1[friend].mana_restore(mana)

                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + " <= " + str(magic_dmg) + " MP <= " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC)
                            print(bcolors.BOLD + player.nickname + ": " + team1[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uzyskał " + str(mana) + " MP" + bcolors.ENDC)
                            break

                        elif spell.type == "stun":
                            enemy = player.choose_target(team2)
                            if team2[enemy].get_dodge_chance() >= 0 and team2[enemy].get_dodge_chance() < 13:
                                dodge_string = "(Unik)"
                                team2[enemy].dodge_chance()

                            else:
                                dodge_string = ""
                                team2[enemy].stunned = True

                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + bcolors.ENDC + " => " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC, str(dodge_string))
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
                            enemy = player.choose_target(team2)
                            team2[enemy].take_damage(item.prop)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.YELLOW + item.name + ": " + bcolors.ENDC + str(item.prop) + " DMG => " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC)

                            if team2[enemy].get_hp() == 0:
                                print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                                del team2[enemy]
                                enemies2 -= 1

                                if enemies2 == 0:
                                    print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                    return True
                            break

        for player in team2:
            if player.stunned == True:
                player.stunned = False
                print("\n", bcolors.BOLD + player.nickname + " - " + bcolors.PURPLE + " Ogłuszony" + bcolors.ENDC)

            else:
                while 1:
                    print("\n", bcolors.BOLD + player.nickname + ": " + bcolors.ENDC)
                    player.choose_action()
                    choice = input("\tWybierz akcje: ")
                    index = int(choice) - 1

                    if index == 0:
                        dmg = player.generate_damage()
                        enemy = player.choose_target(team1)
                        if team1[enemy].get_dodge_chance() >= 0 and team1[enemy].get_dodge_chance() < 13:
                            dmg = 0
                            dodge_string = "(Unik)"
                            team1[enemy].dodge_chance()

                        else:
                            dodge_string = ""

                        team1[enemy].take_damage(dmg)
                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team1[enemy].nickname + bcolors.ENDC, str(dodge_string))

                        if team1[enemy].get_hp() == 0:
                            print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                            del team1[enemy]
                            enemies1 -= 1

                            if enemies1 == 0:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                return True
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
                            print(bcolors.RED + "\nZa mało MP!\n" + bcolors.ENDC)
                            continue

                        player.reduce_mp(spell.cost)

                        if spell.type == "white":
                            friend = player.choose_ally(team2)
                            team1[friend].heal(magic_dmg)

                            if magic_dmg > player.maxhp:
                                magic_dmg = int(player.maxhp - magic_dmg)

                            print(bcolors.BOLD + player.nickname + ": " + team1[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)
                            break

                        elif spell.type == "black":
                            enemy = player.choose_target(team1)

                            if spell.name == "Natychmiastowe zabójstwo":
                                chance = random.randrange(0, 10)
                                if team2[enemy].get_hp() == team2[enemy].get_max_hp():
                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                    dmg = int(player.get_hp() / 4)
                                    player.take_damage(dmg)

                                elif team2[enemy].get_hp() <= int(0.9 * team2[enemy].get_max_hp()):
                                    if team2[enemy].get_hp() <= int(0.8 * team2[enemy].get_max_hp()):
                                        if team2[enemy].get_hp() <= int(0.7 * team2[enemy].get_max_hp()):
                                            if team2[enemy].get_hp() <= int(0.6 * team2[enemy].get_max_hp()):
                                                if team2[enemy].get_hp() <= int(0.5 * team2[enemy].get_max_hp()):
                                                    if team2[enemy].get_hp() <= int(0.4 * team2[enemy].get_max_hp()):
                                                        if team2[enemy].get_hp() <= int(0.3 * team2[enemy].get_max_hp()):
                                                            if team2[enemy].get_hp() <= int(0.2 * team2[enemy].get_max_hp()):
                                                                if team2[enemy].get_hp() <= int(0.1 * team2[enemy].get_max_hp()):
                                                                    if chance >= 0 and chance < 9:
                                                                        team2[enemy].take_damage(magic_dmg)
                                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                                    else:
                                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                        dmg = int(player.get_hp() / 4)
                                                                        player.take_damage(dmg)
                                                            else:
                                                                if chance >= 0 and chance < 8:
                                                                    team2[enemy].take_damage(magic_dmg)
                                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                                else:
                                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                    dmg = int(player.get_hp() / 4)
                                                                    player.take_damage(dmg)
                                                        else:
                                                            if chance >= 0 and chance < 7:
                                                                team2[enemy].take_damage(magic_dmg)
                                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                            else:
                                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                                dmg = int(player.get_hp() / 4)
                                                                player.take_damage(dmg)
                                                    else:
                                                        if chance >= 0 and chance < 6:
                                                            team2[enemy].take_damage(magic_dmg)
                                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                        else:
                                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                            dmg = int(player.get_hp() / 4)
                                                            player.take_damage(dmg)
                                                else:
                                                    if chance >= 0 and chance < 5:
                                                        team2[enemy].take_damage(magic_dmg)
                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                    else:
                                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                        dmg = int(player.get_hp() / 4)
                                                        player.take_damage(dmg)
                                            else:
                                                if chance >= 0 and chance < 4:
                                                    team2[enemy].take_damage(magic_dmg)
                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                                else:
                                                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                    dmg = int(player.get_hp() / 4)
                                                    player.take_damage(dmg)
                                        else:
                                            if chance >= 0 and chance < 3:
                                                team1[enemy].take_damage(magic_dmg)
                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                            else:
                                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                                dmg = int(player.get_hp() / 4)
                                                player.take_damage(dmg)
                                    else:
                                        if chance == 0 or chance == 1:
                                            team1[enemy].take_damage(magic_dmg)
                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                        else:
                                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                            dmg = int(player.get_hp() / 4)
                                            player.take_damage(dmg)
                                else:
                                    if chance == 0:
                                        team1[enemy].take_damage(magic_dmg)
                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona powodzeniem!" + bcolors.ENDC)

                                    else:
                                        print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Próba zabójstwa zakończona niepowodzeniem!" + bcolors.ENDC)
                                        dmg = int(player.get_hp() / 4)
                                        player.take_damage(dmg)

                            elif spell.name == "'Tanio skóry nie sprzedam'":
                                if team1[enemy].get_dodge_chance() >= 0 and team1[enemy].get_dodge_chance() < 13:
                                    dmg = 0
                                    dodge_string = "(Unik)"
                                    team1[enemy].dodge_chance()

                                else:
                                    dmg = int(0.15 * player.get_hp())
                                    dodge_string = ""

                                team1[enemy].take_damage(dmg)
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team1[enemy].nickname + bcolors.ENDC, str(dodge_string))

                            else:
                                if team1[enemy].get_dodge_chance() >= 0 and team1[enemy].get_dodge_chance() < 13:
                                    magic_dmg = 0
                                    dodge_string = "(Unik)"
                                    team1[enemy].dodge_chance()

                                else:
                                    dodge_string = ""

                                team1[enemy].take_damage(magic_dmg)
                                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team1[enemy].nickname + bcolors.ENDC, str(dodge_string))

                            if team1[enemy].get_hp() == 0:
                                print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                                del team1[enemy]
                                enemies1 -= 1

                                if enemies1 == 0:
                                    print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                    return True
                            break

                        elif spell.type == "block":
                            player.temp_dodge = True
                            break

                        elif spell.type == "HP steal":
                            enemy = player.choose_target(team1)
                            friend = player.choose_ally(team2)
                            magic_dmg = 250
                            team1[enemy].take_damage(magic_dmg)
                            heal = int(magic_dmg/1.5)
                            team2[friend].heal(heal)

                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + str(magic_dmg) + " DMG => " + bcolors.BOLD + bcolors.RED + team1[enemy].nickname + bcolors.ENDC)
                            print(bcolors.BOLD + player.nickname + ": " + team2[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(heal) + " HP" + bcolors.ENDC)

                            if team1[enemy].get_hp() == 0:
                                print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                                del team2[enemy]
                                enemies1 -= 1

                            if enemies1 == 0:
                                print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                return True
                            break

                        elif spell.type == "MP steal":
                            enemy = player.choose_target(team1)
                            friend = player.choose_ally(team2)
                            magic_dmg = 50

                            if team1[enemy].get_mp() < magic_dmg:
                                magic_dmg = team1[enemy].get_mp()

                            team1[enemy].reduce_mp(magic_dmg)
                            mana = int(magic_dmg/1.75)
                            team2[friend].mana_restore(mana)

                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + bcolors.ENDC + " <= " + str(magic_dmg) + " MP <= " + bcolors.BOLD + bcolors.RED + team2[enemy].nickname + bcolors.ENDC)
                            print(bcolors.BOLD + player.nickname + ": " + team1[friend].nickname + bcolors.ENDC + bcolors.BLUE + " uzyskał " + str(mana) + " MP" + bcolors.ENDC)
                            break

                        elif spell.type == "stun":
                            enemy = player.choose_target(team1)
                            if team1[enemy].get_dodge_chance() >= 0 and team1[enemy].get_dodge_chance() < 13:
                                dodge_string = "(Unik)"
                                team1[enemy].dodge_chance()

                            else:
                                dodge_string = ""
                                team1[enemy].stunned = True

                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + bcolors.ENDC + " => " + bcolors.BOLD + bcolors.RED + team1[enemy].nickname + bcolors.ENDC, str(dodge_string))
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
                            enemy = player.choose_target(team1)
                            team1[enemy].take_damage(item.prop)
                            print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.YELLOW + item.name + ": " + bcolors.ENDC + str(item.prop) + " DMG => " + bcolors.BOLD + bcolors.RED + team1[enemy].nickname + bcolors.ENDC)

                            if team1[enemy].get_hp() == 0:
                                print(bcolors.GREEN + team2[enemy].nickname, "został pokonany!" + bcolors.ENDC)
                                del team2[enemy]
                                enemies1 -= 1

                                if enemies1 == 0:
                                    print(bcolors.GREEN + "Sukces!" + bcolors.ENDC)
                                    return True
                            break
                            
        for player in team1:
            if player.character.buff == "Ziemia":
                player.heal(12)
                player.mana_restore(20)

            elif player.character.buff == "Woda":
                player.heal(22)
                player.mana_restore(25)

            elif player.character.buff == "Ogień":
                player.heal(20)
                player.mana_restore(15)

            elif player.character.buff == "Wiatr":
                player.heal(20)
                player.mana_restore(25)

        for enemy in team2:
            enemy.heal(25)
            enemy.mana_restore(20)