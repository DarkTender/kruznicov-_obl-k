from math import sin, cos, tan
import os
import math
import numpy as np
os.system("clear")
polomer = input("Zadajte polomer(r): ")

dlzka = input("Zadajte dĺžku(s): ")

alfa_otazka = input("Zadajte alfu(α): ")

alfa = int(alfa_otazka) * 0.015707933

roo_klas = input("Zadajte Ró(ρ): ")

alfa_vyp = 200 - int(alfa_otazka) # Výpočet Tau zo vzorcom 200-alfa = ?g
print("\nTau(τ) sa rovná:  " + str(alfa_vyp) + "g")

oprava_fiii = float(dlzka) / int(polomer) * float(roo_klas)
oprava_fi = oprava_fiii * 0.0157079633
print("Výpočet Fí(ϕ): ", round(oprava_fiii, 4), "g" )

#print("T=r*tg*alfa/2 = ")
vyp_T = float(polomer) * math.tan(alfa/2)
print("Výpočet T: ",round(vyp_T, 2), "m")

lava_0 = math.cos(alfa/2)
print(str("Výpočet l="), round(int(polomer) /lava_0, 2),"m") #l = r/ cos*alfa/2
lava_1 = int(polomer) /lava_0

oprava_roo = float(roo_klas) * 0.0157079633
vyp_0 = int(polomer) * float(alfa)
vyp_1 = float(vyp_0) / oprava_roo
print("Výpočet dĺžky oblúka(o) = ", round(float(vyp_1),2), "m")

print("Výpočet Z =",round(float(lava_1) - int(polomer),2), "m") # KK

bodov = float(vyp_1) / float(dlzka)
print("Výpočet bodov je: ", round(float(bodov), 1), "!!!! Zaokrúhľujeme dole ↓↓")

konec_bodov = int(input("\nNa koľko bodov zaokrúhlim?: ")) + 1

while True:
    metoda = input("""
1.Ortogonálna metóda
2.Polárna metóda

Vybrať sa dá len jedna možnosť: """)
#Ortogonálna metóda
    if metoda == "1":
        for y in range(1,konec_bodov):
            Yn_1 = math.cos(y * oprava_fi)
            Yn_0 = int(polomer) * float(1 - float(Yn_1))
            print("Výpočet Yn je:", round(float(Yn_0),2), "m")
        print("\n")

        for x in range(1,konec_bodov):
            Xn_2 = math.sin(x * oprava_fi)
            Xn_1 = int(polomer) * float(Xn_2)
            print("Výpočet Xn je: ", round(float(Xn_1),2),"m")

    elif metoda == "2":
            delta_d = int(polomer) * 2
            delta_t = float(dlzka) / delta_d * float(roo_klas)
            for delta_r in range(1,konec_bodov):
                print("Výpočet δ(n): ", round(delta_r * delta_t, 4), "g")
            print("")
            delta_d = int(polomer) * 2
            delta_t = float(dlzka) / delta_d * float(roo_klas)
            for dn_0 in range(1,konec_bodov):
                dn_2 = 2 * float(polomer)
                dn_1 = dn_2 * math.sin(dn_0*delta_t*0.0157079633) 
                print("Výpočet dn: ", round(dn_1, 2) , "m")

            print("\nVýpočet KK: ", round(float(alfa_otazka) / 4, 4), "g")
    else:
        exit()