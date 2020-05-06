from bcolors import bcolors

def description(c):
    while 1:
        if c == '1':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "WOJOWNIK\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "3900" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "45" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "45" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Wojownik charakteryzuje się wysoką wytrzymałością oraz wysokimi obrażeniami. Przystosowany jest do dłuższych walk.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPotężne Uderzenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   155" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nMiazga" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  40" + bcolors.ENDC)
            print(bcolors.BOLD + "\nGarda" + bcolors.ENDC)
            print(bcolors.YELLOW + "\tUnik:       +80" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '2':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "MAG\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "2800" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "15" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "90" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Niska wytrzymałość oraz bezużyteczny atak podstawowy maga są rekompensowane przez ogromne obrażenia umiejętności.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPodpalenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   110" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nMeteor" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  40" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPorażenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   190" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  35" + bcolors.ENDC)
            print(bcolors.BOLD + "\nBłyskawica" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   280" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  45" + bcolors.ENDC)
            print(bcolors.BOLD + "\nKula Żywiołów" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   340" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  50" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '3':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "SKRYTOBÓJCA\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "2550" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "50" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "55" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Skrytobójca jest postacią wysokiego ryzyka. Zadaje ogromne obrażenia, ale nie jest przystosowany do długich walk.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPorażenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   190" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  35" + bcolors.ENDC)
            print(bcolors.BOLD + "\nNawałnica Stali" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   500" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  70" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPenetracja" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   650" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  85" + bcolors.ENDC)
            print(bcolors.BOLD + "\nNatychmiastowe Zabójstwo" + bcolors.ENDC)
            print("(Umiejętność ma tylko 10% szans na powodzenie na każde brakujące 10% HP przeciwnika. W przypadku niepowodzenia, bohater traci 25% obecnego HP.)")
            print(bcolors.RED + "\tObrażenia:   MAXIMUM" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  250" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '4':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "PALADYN\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "3100" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "30" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "35" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Święty rycerz, który zadaje wysokie obrażenia za pomocą swoich umiejętności oraz z możliwością leczenia, świetnie nadaje sie do dłuższych walk.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPotężne Uderzenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   155" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPodpalenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   110" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nMeteor" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  40" + bcolors.ENDC)
            print(bcolors.BOLD + "\nBłyskawica" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   280" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  45" + bcolors.ENDC)
            print(bcolors.BOLD + "\nUleczenie" + bcolors.ENDC)
            print(bcolors.GREEN + "\tRegeneracja: 300" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  55" + bcolors.ENDC)
            print(bcolors.BOLD + "\nUzdrowienie" + bcolors.ENDC)
            print(bcolors.GREEN + "\tRegeneracja: MAXIMUM" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  200" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '5':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "OSIŁEK\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "4300" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "30" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "0" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Bardzo wysoka wytrzymałość osiłków czyni ich trudnymi do zabicia, ale sami nie zadają wysokich obrażeń.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\n'Tanio skóry nie sprzedam'" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   15% obecnego HP bohatera" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  220" + bcolors.ENDC)
            print(bcolors.BOLD + "\nUleczenie" + bcolors.ENDC)
            print(bcolors.GREEN + "\tRegeneracja: 300" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  55" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '6':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "PIĘŚCIARZ\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "3650" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "80" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "20" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Pięściarz to postać specjalizująca się w atakach podstawowych. Jest przystosowany do dłuższych walk")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPotężne Uderzenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   155" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nRzeź" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   250" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  50" + bcolors.ENDC)
            print(bcolors.BOLD + "\nKamienne Pięści" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  40" + bcolors.ENDC)
            print(bcolors.BOLD + "\nGarda" + bcolors.ENDC)
            print(bcolors.YELLOW + "\tUnik:       +80" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '7':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "ŁOTRZYK\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "2700" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "40" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "20" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Łotrzyk pełni rolę wspierającego drużyny. Potrafi wykradać życie i manę przeciwników oraz ogłuszać ich.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPodpalenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   110" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nKradzież zdrowia" + bcolors.ENDC)
            print(bcolors.PURPLE + "\tKradzież:    250 HP" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  50" + bcolors.ENDC)
            print(bcolors.BOLD + "\nKradzież many" + bcolors.ENDC)
            print(bcolors.PURPLE + "\tKradzież:    50 MP" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  25" + bcolors.ENDC)
            print(bcolors.BOLD + "\nOgłuszenie" + bcolors.ENDC)
            print("\tOgłusza przeciwnika na czas jednej rundy" + bcolors.BLUE + "\n\tKoszt many:  120" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '8':
            print(bcolors.BOLD + "ŻYWIŁOY:\n" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.GREEN + "ZIEMIA:" + bcolors.ENDC)
            print(bcolors.GREEN + "\tZdrowie: +350 HP" + bcolors.ENDC)
            print(bcolors.BLUE + "\tRegeneracja many: -20%" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "\nWODA:" + bcolors.ENDC)
            print(bcolors.GREEN + "\t+10% bardziej efektywne leczenie" + bcolors.ENDC)
            print(bcolors.BLUE + "\tMana: +100 MP" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "\nOGIEŃ:" + bcolors.ENDC)
            print(bcolors.RED + "\tAtak: +25 DMG" + bcolors.ENDC)
            print(bcolors.PURPLE + "\tMoc umiejętności: +10%" + bcolors.ENDC)
            print(bcolors.BOLD + "\nWIATR:" + bcolors.ENDC)
            print(bcolors.BLUE + "\tRegeneracja many: +10 MP" + bcolors.ENDC)
            print(bcolors.YELLOW + "\tSzansa na unik: +15%")

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break