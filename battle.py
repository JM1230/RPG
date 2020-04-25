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
                print(bcolors.BOLD + player.nickname + bcolors.ENDC + ": " + str(dmg) + " DMG => " + bcolors.BOLD + foe[enemy].character.cl)