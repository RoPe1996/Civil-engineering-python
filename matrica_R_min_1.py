import math
from spoj1 import matrice_paket_1
"""------------------------------MINIMALNI TRAG NA SVE TACKE-------------------------------"""

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

print ("DUZINA JEDNOG REDA MATRICE R_T = " +str(r))

print()
print("UNESI DEFEKT MREZE")
koef_d = int(input())
def_mreze = range(koef_d)


"RACUNANJE KLASNICNOG NACINA"

matrica_R = []
matrica_R_T = []

# BROJ TACAKA KOJE DEFINISU DATUM
m = int(len(poc_kord))
print("UKUPAN BROJ TACAKA KOJE DEFINISU DATUM " + str(m))
mi = math.sqrt(m)
# RACUNANANJE Y I X SREDNJE
y_suma = 0
x_suma = 0

for i in poc_kord:
    y_suma = y_suma + i[0]
    x_suma = x_suma + i[1]


y_srednje = y_suma / m
x_srednje = x_suma / m
suma_dy_2 = 0
suma_dx_2 = 0

for i in poc_kord:
    # TEKUCE dy
    dy = i[0] - y_srednje
    suma_dy_2 = suma_dy_2 + math.pow(dy, 2)

    dx = i[1] - x_srednje
    suma_dx_2 = suma_dx_2 + math.pow(dx, 2)
g = math.sqrt(suma_dy_2 + suma_dx_2)

# UREDJENI PAR KSI I ETA ZA SVAKU TACKU
matrica_ksi_eta = []
for i in poc_kord:
    ksi = (i[1] - x_srednje) / g
    eta = (i[0] - y_srednje) / g
    matrica_ksi_eta.append([ksi, eta])

# print()
# print("MATRICA KSI I ETA")
# print(matrica_ksi_eta)
# ZA OSTATAK SA DELJENJEM %


for i in def_mreze:

    if i == 0:
        print("PRVI RED")
        red_nula = [0] * r
        # PROVERA PARAN NEPARAN BROJ
        for i, val in enumerate(red_nula):
            if i % 2 == 0:
                red_nula[i] = 1 / mi
                # NEPARAN
        red_nula.extend([0] * br_zxz)
        matrica_R_T.append(red_nula)

    elif i == 1:
        print("DRUGI RED")
        red_nula = [0] * r
        for i, val in enumerate(red_nula):
            if i % 2 != 0:
                red_nula[i] = 1 / mi
                # PARAN
        red_nula.extend([0] * br_zxz)
        matrica_R_T.append(red_nula)

    elif i == 2:
        print("TRECI RED")
        cista_matrica = []
        red_nula = []
        for i, vred in enumerate(matrica_ksi_eta):
            ksii = vred[0] * (-1)
            etaa = vred[1]
            cista_matrica.append(ksii)
            cista_matrica.append(etaa)
        red_nula.extend([0] * br_zxz)
        cista_matrica.extend(red_nula)
        matrica_R_T.append(cista_matrica)

    elif i == 3:
        print("CETVRTI RED")
        red_nula = []
        cista_matrica = []
        for i, vred in enumerate(matrica_ksi_eta):
            ksii = vred[0]
            etaa = vred[1]
            cista_matrica.append(etaa)
            cista_matrica.append(ksii)
        red_nula.extend([0] * br_zxz)
        cista_matrica.extend(red_nula)
        matrica_R_T.append(cista_matrica)

    else:
        print("NESTO JE KRIVO UNETO")


print()
print("KOMPLETNA MATRICA R_T")
for i in matrica_R_T:
    print(i)

def paket_R_T_min1():

    return [matrica_R_T, br_zxz,  koef_d]

