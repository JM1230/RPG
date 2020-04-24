from bcolors import bcolors

def description(c):
    while 1:
        if c == '1':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "WOJOWNIK\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "4500" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "110" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "10" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Wojownik charakteryzuje się wysoką wytrzymałością oraz wysokimi obrażeniami. Przystosowany jest do dłuższych walk.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPotężne Uderzenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   155" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)
            print(bcolors.BOLD + "\nMiazga" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '2':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "MAG\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "3000" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "20" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "150" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Niska wytrzymałość oraz bezużyteczny atak podstawowy maga są rekompensowane przez ogromne obrażenia umiejętności.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPodpalenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   110" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)
            print(bcolors.BOLD + "\nMeteor" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPorażenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   190" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  25" + bcolors.ENDC)
            print(bcolors.BOLD + "\nBłyskawica" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   300" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  35" + bcolors.ENDC)
            print(bcolors.BOLD + "\nKula Ognia" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   385" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  40" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '3':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "SKRYTOBÓJCA\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "3100" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "155" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "45" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Skrytobójca jest postacią wysokiego ryzyka. Zadaje ogromne obrażenia, ale nie jest przystosowany do długich walk.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPorażenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   190" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  25" + bcolors.ENDC)
            print(bcolors.BOLD + "\nNawałnica Stali" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   500" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  70" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPenetracja" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   650" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  80" + bcolors.ENDC)
            print(bcolors.BOLD + "\nNatychmiastowe Zabójstwo" + bcolors.ENDC)
            print("(Umiejętność ma tylko 20% szans na powodzenie oraz zużywa całą manę. W przypadku niepowodzenia, bohater traci 25% obecnego HP.)")
            print(bcolors.RED + "\tObrażenia:   MAXIMUM" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  230" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '4':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "PALADYN\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "4000" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "80" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "30" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Święty rycerz, który zadaje wysokie obrażenia za pomocą swoich umiejętności oraz z możliwością leczenia, świetnie nadaje sie do dłuższych walk.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPotężne Uderzenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   155" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPodpalenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   110" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)
            print(bcolors.BOLD + "\nMeteor" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)
            print(bcolors.BOLD + "\nBłyskawica" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   300" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  35" + bcolors.ENDC)
            print(bcolors.BOLD + "\nUleczenie" + bcolors.ENDC)
            print(bcolors.GREEN + "\tRegeneracja: 300" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  50" + bcolors.ENDC)
            print(bcolors.BOLD + "\nUzdrowienie" + bcolors.ENDC)
            print(bcolors.GREEN + "\tRegeneracja: MAXIMUM" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  200" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '5':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "OBROŃCA\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "5550" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "50" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "0" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Bardzo wysoka wytrzymałość obrońców czyni ich trudnymi do zabicia, ale sami nie zadają wysokich obrażeń.")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nOgłuszający Krzyk" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   Zależne od obecnego HP bohatera" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  0" + bcolors.ENDC)
            print(bcolors.BOLD + "\nUleczenie" + bcolors.ENDC)
            print(bcolors.GREEN + "\tRegeneracja: 500" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  50" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break

        if c == '6':
            print(bcolors.BOLD + "KLASA: " + bcolors.ENDC + "ŁOTRZYK\n")
            print(bcolors.BOLD + bcolors.GREEN + "ZDROWIE:            " + bcolors.ENDC + bcolors.GREEN + "3750" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.RED + "ATAK:               " + bcolors.ENDC + bcolors.RED + "175" + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.BLUE + "MOC UMIEJĘTNOŚCI:   " + bcolors.ENDC + bcolors.BLUE + "20" + bcolors.ENDC)
            print(bcolors.BOLD + "\n\nOPIS:" + bcolors.ENDC)
            print("Łotrzyk to postać specjalizująca się w atakach podstawowych. Jest przystosowany do dłuższych walk")
            print(bcolors.BOLD + "\n\nUMIEJĘTNOŚCI:" + bcolors.ENDC)
            print(bcolors.BOLD + "\nPotężne Uderzenie" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   155" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  20" + bcolors.ENDC)
            print(bcolors.BOLD + "\nRzeź" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   250" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  35" + bcolors.ENDC)
            print(bcolors.BOLD + "\nKamienne Pięści" + bcolors.ENDC)
            print(bcolors.RED + "\tObrażenia:   200" + bcolors.ENDC + bcolors.BLUE + "\n\tKoszt many:  30" + bcolors.ENDC)

            x = str(input(bcolors.ENDC + "\n\n\nAby powrócić, naciśnij dowolny przycisk"))
            break
