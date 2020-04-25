from person import Person
from player import Player
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
            player.character.get_stats()

        print("\n")

        for enemy in foe:
            print(bcolors.BOLD + enemy.cl + ":" + bcolors.ENDC)
            enemy.get_enemy_stats()

        running = False