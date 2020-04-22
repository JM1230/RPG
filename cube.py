import random

def cube(c):
    if c == 1:
        x = random.randrange(2, 13)
        print("Wyrzucona liczba oczek:", x)
        return x

    elif c == 2:
        x = random.randrange(2, 21)
        print("Wyrzucona liczba oczek:", x)
        return x

    elif c == 3:
        x = random.randrange(2, 26)
        print("Wyrzucona liczba oczek:", x)
        return x
