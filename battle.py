from bcolors import bcolors
import random

def battle(foe, ally):
    print(bcolors.BOLD + bcolors.RED + "\nWALKA\n" + bcolors.ENDC)
    i = 0
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
            player.choose_action()
            choice = input("\tWybierz akcje: ")
            index = int(choice) - 1

            if index == 0:
                dmg = player.generate_damage()
                enemy = player.choose_target(foe)
                foe[enemy].take_damage(dmg)
                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.RED + "Atak: " + str(dmg) + bcolors.ENDC + " DMG => " + bcolors.BOLD + foe[enemy].character.cl)

                if foe[enemy].get_hp() == 0:
                    print(foe[enemy], "został pokonany!")
                    del foe[enemy]

            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("\tWybierz umiejętność: ")) - 1

                if magic_choice == -1:
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
                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + bcolors.BLUE + " uleczył się za " + str(magic_dmg), " HP" + bcolors.ENDC)

                elif spell.type == "black":
                    enemy = player.choose_target(foe)
                    foe[enemy].take_damage(magic_dmg)
                    print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + bcolors.BLUE + spell.name + ": " + str(magic_dmg) + bcolors.ENDC + " DMG => " + bcolors.BOLD + foe[enemy].character.cl)

                    if foe[enemy].get_hp() == 0:
                        print(foe[enemy].character.cl, "został pokonany!")
                        del foe[enemy]