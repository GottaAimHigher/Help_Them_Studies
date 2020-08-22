# coding=utf-8

"""@Author: Navil, Hossain"""

import random
import sys

Kemi_Amnen1 = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S ","Cl","Ar","K ","Ca","Mn","Fe","Cu","Zn","Br","Ag","Sn","I","Ba","Au","Hg","Pb","U"]
Kemi_Amnen2 = ["Väte","Helium","Litium","Beryllium","Bor","Kol","Kväve","Syre","Fluor","Neon","Natrium","Magnesium","Aluminium","Kisel","Fosfor","Svavel","Klor","Argon","Kalium","Kalcium","Mangan","Järn","Koppar","Zink","Brom","Silver","Tenn","Jod","Barium","Guld","Kvicksilver","Bly","Uran"]

Slumpmassig = "ja"
kemisk_tecken_eller_amne = "kemisk tecken"

if Slumpmassig == "ja":
    Rand = random.randint(1, len(Kemi_Amnen1))

    for i in range(len(Kemi_Amnen1)):
        if Kemi_Amnen1[Rand] == "BYTT!":
            Rand = random.randint(1, len(Kemi_Amnen1))

        else:

            if kemisk_tecken_eller_amne == "kemisk tecken":
                svar = input("Vad står " + Kemi_Amnen1[Rand] + " för?\n")

                if svar == Kemi_Amnen2[Rand]:
                    print("Rätt!")

                else:
                    print("Fel!\nSvaret är: " + Kemi_Amnen2[Rand])

            elif kemisk_tecken_eller_amne == "amne":
                svar = input("Vad är " + Kemi_Amnen2[Rand] + "s kemiska beteckning?\n")

                if svar == Kemi_Amnen1[Rand]:
                    print("Rätt!")

                else:
                    print("Fel!\nSvaret är: " + Kemi_Amnen1[Rand])

        Kemi_Amnen1[Rand] = "BYTT!"
        Rand = random.randint(1, len(Kemi_Amnen1))

if kemisk_tecken_eller_amne == "kemisk tecken":
    for i in range(len(Kemi_Amnen1)):
        svar = input("Vad står " + Kemi_Amnen1[i] + " för?\n")

        if svar == Kemi_Amnen2[i]:
            print("Rätt!")

        else:
            print("Fel!\nSvaret är: " + Kemi_Amnen2[i])



elif kemisk_tecken_eller_amne == "amne":
    for i in range(len(Kemi_Amnen2)):
        svar = input("Vad är " + Kemi_Amnen2[i] + "s kemiska beteckning?\n")

        if svar == Kemi_Amnen1[i]:
            print("Rätt!")

        else:
            print("Fel!\nSvaret är: " + Kemi_Amnen1[i])

