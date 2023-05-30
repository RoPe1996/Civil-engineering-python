from numpy import *
import math
import direkcioni

"""
FUNKCIJA ZA KONVERZIJU U RADIJANE
"""
def radians (a, b, c):
    rez_rad = ((a+(b/60)+(c/3600))/360)*2*math.pi
    return (rez_rad)


def duzina (a, b):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    d = math.sqrt(math.pow(dy, 2) + math.pow(dx, 2) )
    return d

poc_kord = [
            [1000, 1000],
            [1000, 1187.84],
            [1073.89, 1148.9],
            [1082.58, 1075.03]
            ]


# RASPORED PRAVACA - PRVI BROJ U PRACIMA JE STAJALISTE, OSTALO SU SVE VIZURE
pravci = [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [2, 1],
            [3, 1],
            [3, 2],
            [3, 4],
            [4, 1],
            [4, 2],
            [4, 3]
         ]

# VREDNOSTI PRAVACA
pravci_vrednosti = [
    radians(0,0,0),
    radians(26,23,30),
    radians(47,44,31),
    radians(0,0,0),
    radians(26,0,16),
    radians(62,12,37),
    radians(0,0,0),
    radians(91,23,49),
    radians(326,53,57),
    radians(0,0,0),
    radians(96,3,7),
    radians(125,32,54),
]

duzine = [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [2, 1],
            [3, 1],
            [3, 2],
            [3, 4],
            [4, 1],
            [4, 2],
            [4, 3],
        ]
#VREDNOSTI DUZINA
duzine_vrednosti = [
    187.841,
    166.228,
    111.57,
    83.522,
    139.805,
    187.843,
    166.225,
    83.522,
    74.374,
    111.573,
    139.807,
    74.391
]



#BROJ REDOVA ZA PRAVCE U MATRICI "A" JE JEDNAK
redovi_A_p = int(len(pravci))

#BROJ NEPOZNATIH PARAMETARA JEDNAK JE BROJU KOLONA U MATRICI "A"
kolone_A = 3*int(len(poc_kord))
print("BROJ PRAVACA U MATRICI A = " +str(redovi_A_p)+ ", BROJ KOLONA U MATRICI A =" +str(kolone_A))

"""
#PRVO FORMIRAMO MATRICU 0 SA BROJEM REDOVA I KOLONA
matrica_A_p = [[0]*kolone_A]*redovi_A_p
for i in matrica_A_p:
    print(i)
"""


#PRAZNA MATRICA A ZA PRAVCIMA
matrica_A_p = []

#MATRICA F ZA PRAVCE
matrica_F_p = []

"""------------------------PETLJA ZA POPUNU MATRICE A PRAVACA------------------------------"""
for index, i in enumerate(pravci):

    red_nula = [0]*kolone_A
    print (red_nula)
    #red iz kod izvlaci koordinate
    #red_sa = i
    print("PRAVAC SA TACKE NA TACKU: " + str(i))
    print(pravci_vrednosti[index])

    #duzina_reda = range(len(i))
    #print("DUZINA REDA = "+str(duzina_reda))

    br_sa = int(i[0])-1
    br_na = int(i[1])-1

    print("STAJALISTE = " + str(br_sa+1) + ", PRAVAC NA = " + str(br_na+1))
    y1 = poc_kord[br_sa][0]
    x1 = poc_kord[br_sa][1]
    t1 = [poc_kord[br_sa][0], poc_kord[br_sa][1]]

    y2 = poc_kord[br_na][0]
    x2 = poc_kord[br_na][1]
    t2 = [poc_kord[br_na][0], poc_kord[br_na][1]]

    print("KOORD STAJALISTA = " + str(y1) + ", " + str(x1))
    print("KOORD VIZURE = " + str(y2) + ", " + str(x2))
    #DUZINA IZMEDJU TACAKA
    duz = duzina(t1, t2)

    #DIREKCIONI UGAO IZMEDJU TACAKA
    dir = direkcioni.dir_finkc(t1, t2)

    #KOREFICJENT RO
    ro = 206265


    koef_b1 = (ro*math.cos(dir))/(duz*1000*(-1))
    koef_a1 = (ro*math.sin(dir))/(duz*1000)

    koef_b2 = - koef_b1
    koef_a2 = - koef_a1

    #KOEFICJENTI SA STAJALISTA
    red_nula[br_sa*2] = koef_b1
    red_nula[br_sa*2+1] = koef_a1
    #KOEFICJENTI NA VIZURU
    red_nula[br_na*2] = koef_b2
    red_nula[br_na*2+1] = koef_a2

    #Z POPRAVKA
    red_nula[int(len(poc_kord))*2 + i[0]-1] = 1

    print (red_nula)

    matrica_A_p.append(red_nula)

    #RACUNANJE DELA ZA POPRAVKE F OD PRAVACA




print("MATRICA A_PRAVACA: ")
for i in matrica_A_p:
    print(i)



print()
print()
print("          MATRICA A DUZINA           ")

matrica_A_d = []
"""------------------------PETLJA ZA POPUNU MATRICE A DUZINA------------------------------"""

for index, vrednost in enumerate(duzine):

    #U OVAJ RED UBACUJEMO IZRACUNATE KOEFICJENTE PA GA ONDA CELOG DODAMO U MATRICU "matrica_A_d"
    red_nula = [0] * kolone_A
    print(red_nula)

    br_sa = int(vrednost[0])-1
    br_na = int(vrednost[1])-1
    print("STAJALISTE = " + str(br_sa+1) + ", PRAVAC NA = " + str(br_na+1))
    y1 = poc_kord[br_sa][0]
    x1 = poc_kord[br_sa][1]
    t1 = [poc_kord[br_sa][0], poc_kord[br_sa][1]]

    y2 = poc_kord[br_na][0]
    x2 = poc_kord[br_na][1]
    t2 = [poc_kord[br_na][0], poc_kord[br_na][1]]

    print("KOORD STAJALISTA = " + str(y1) + ", " + str(x1))
    print("KOORD VIZURE = " + str(y2) + ", " + str(x2))

    # DIREKCIONI UGAO IZMEDJU TACAKA
    dir = direkcioni.dir_finkc(t1, t2)

    koef_B1 = (math.sin(dir)*(-1))
    koef_A1 = (math.cos(dir)*(-1))

    koef_B2 = - koef_B1
    koef_A2 = - koef_A1

    # KOEFICJENTI SA STAJALISTA
    red_nula[br_sa * 2] = koef_B1
    red_nula[br_sa * 2 + 1] = koef_A1
    # KOEFICJENTI NA VIZURU
    red_nula[br_na * 2] = koef_B2
    red_nula[br_na * 2 + 1] = koef_A2

    print(red_nula)

    matrica_A_d.append(red_nula)

print()
print("MATRICA A_DUZINA: ")
for i in matrica_A_d:
    print(i)


"""------------------------KOMPLETNA MATRICA A------------------------------"""

matrica_A = []
for i in matrica_A_p:
    matrica_A.append(i)
for i in matrica_A_d:
    matrica_A.append(i)
print()
print("    KOMPLETNA MATRICA A     ")
for i in matrica_A:
    print(i)


"""--------------------NEPOTREBNO ALI IMA ISPIS PODATAKA OD DRUGOG DO POSLEDNJEG------------------------------

    # j je indeks od drugog mesta u listi do poslednjeg
    for j in duzina_reda[1:len(i)]:
        # broj tacaka na stajalistu
        br_sa = int(i[0])
        br_na = int(i[1])
        print("STAJALISTE = " +str(br_sa)+ ", PRAVAC NA = " +str(br_na))
        y1 = poc_kord[br_sa-1][0]
        x1 = poc_kord[br_na-1][1]
        stajaliste = [y1, x1]
        print ("KOORD STAJALISTA = " +str(y1)+ ", "+str(x1))
        y2 = poc_kord[j-1][0]
        x2 = poc_kord[j-1][0]
        vizura = [y2, x2]
        print("KOORD VIZURE = " + str(y2) + ", " + str(x2))
        #TRENUTANA DUZINA IZMEDJU POJEDINACNIH TACAKA
        duz = duzina(stajaliste, vizura)

        #DODAVANJE IZRACUNATE DUZINE U REDU
        red_duzine.append(duz)

    #PRIKAZIVANJE REDA SA DUZINAMA
    print("DUZINE U REDU "+str(i) + str(red_duzine))

    duzine.append(red_duzine)
    """

#for i in duzine:
    #print("MATRICA DUZINA = " +str(i))

"""------------------------MATRICA f RAZLIKA----------------------------"""

kombinacije_p_f = [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 1, 2, 4],
            [4, 1, 2, 3],
]


