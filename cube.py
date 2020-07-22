import random

def cube(c):
    if c == 1:
        x = random.randrange(2, 13)
        print("Wyrzucona liczba oczek:", x)
        return x

    elif c == 2:
        x = random.randrange(3, 19)
        print("Wyrzucona liczba oczek:", x)
        return x

    elif c == 3:
        x = random.randrange(4, 25)
        print("Wyrzucona liczba oczek:", x)
        return x