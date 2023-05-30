import math
from spoj1 import matrice_paket_1




"""------------------------------POCETNE KOORDINATE I PODACI-------------------------------"""


[poc_kord, br_zxz] = matrice_paket_1()
"""
poc_kord = [
            [1934.594, 1820.979],
            [2050.591, 1810.192],
            [2104.296, 1734.664],
            [2087.261, 1647.372],
            [1980.073, 1602.704],
            [1893.92, 1649.316],
            [1867.332, 1739.565],
            ]
"""


#DUZINA JEDNOG REDA MATRICE R_T
r = len(poc_kord)*2
#r = len(poc_kord)*len(poc_kord[0])

print ("DUZINA JEDNOG REDA MATRICE R_T = " +str(r))

print()
print("UNESI DEFEKT MREZE")
koef_d = int(input())
def_mreze = range(koef_d)


"RACUNANJE KLASNICNOG NACINA"

matrica_R = []
matrica_R_T = []

for i in def_mreze:
    # ZA PRVI RED MATRICE

    if i == 0:

        print("KOJOM TACKOM JE DEFINISANA TRANSLACIJA (ty) PO Y ")

        ty = int(input())
        red_nula = [0] * r
        pozicija = (ty - 1) * 2
        red_nula[pozicija] = 1
        red_nula.extend([0] * br_zxz)
        print("PRVI RED MATRICE R")
        print(red_nula)
        matrica_R_T.append(red_nula)

    elif i == 1:

        print("KOJOM TACKOM JE DEFINISANA TRANSLACIJA (tx) PO X ")

        tx = int(input())
        red_nula = [0] * r
        pozicija = ((tx - 1) * 2) + 1
        red_nula[pozicija] = 1
        print("DRUGI RED matrica_R_T")
        red_nula.extend([0] * br_zxz)
        print(red_nula)
        matrica_R_T.append(red_nula)


    elif i == 2:
        print("KOJOM TACKOM JE DEFINISANA ROTACIJA (rZ)")

        rZ = int(input())
        red_nula = [0] * r
        pozicija = ((rZ - 1) * 2)
        red_nula[pozicija] = 1
        print("TRECI RED matrica_R_T")
        red_nula.extend([0] * br_zxz)
        print(red_nula)
        matrica_R_T.append(red_nula)



    elif i == 3:
        print("KOJOM Y TACKOM JE DEFINISANO SKALIRANJE (S)")

        s = int(input())
        red_nula = [0] * r
        pozicija = ((s - 1) * 2) + 1
        red_nula[pozicija] = 1
        print("CETVRTI RED matrica_R_T")
        red_nula.extend([0] * br_zxz)
        print(red_nula)
        matrica_R_T.append(red_nula)
    else:
        print("UNESLI STE NESTO KRIVO")

print()
print("KOMPLETNA MATRICA R_T")
for i in matrica_R_T:
    print(i)

def paket_R_T_klas():

    return [matrica_R_T, br_zxz, koef_d]