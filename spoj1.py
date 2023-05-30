from numpy import *
import math
import direkcioni

"""
FUNKCIJA ZA KONVERZIJU U RADIJANE
"""
def radians (a, b, c):
    rez_rad = ((a+(b/60)+(c/3600))/360)*2*math.pi
    return rez_rad


def duzina (a, b):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    d = math.sqrt(math.pow(dy, 2) + math.pow(dx, 2) )
    return d





"""------------------------------POCETNE KOORDINATE I PODACI-------------------------------"""
poc_kord = [
            [1000, 1000],
            [1000, 1187.84],
            [1073.89, 1148.9],
            [1082.58, 1075.03]
            ]


# RASPORED PRAVACA - PRVI BROJ U PRACIMA JE STAJALISTE, OSTALO SU SVE VIZURE
pravci = [
            [1, 2, radians(0, 0, 0)],
            [1, 3, radians(26, 23, 30)],
            [1, 4, radians(47, 44, 31)],
            [2, 3, radians(0,0,0)],
            [2, 4, radians(26,0,16)],
            [2, 1, radians(62,12,37)],
            [3, 1, radians(0,0,0)],
            [3, 2, radians(91,23,49)],
            [3, 4, radians(326,53,57)],
            [4, 1, radians(0,0,0)],
            [4, 2, radians(96,3,7)],
            [4, 3, radians(125,32,54)]
         ]

# VREDNOSTI PRAVACA
pravci_vrednosti = [
    [radians(0,0,0),
    radians(26,23,30),
    radians(47,44,31)],

    [radians(0,0,0),
    radians(26,0,16),
    radians(62,12,37)],

    [radians(0,0,0),
    radians(91,23,49),
    radians(326,53,57)],

    [radians(0,0,0),
    radians(96,3,7),
    radians(125,32,54)]
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

"""!!!!!!!!!!!!!!! OVDE NAMESTITI MATRICU KOMBINACIJA PRAVACA ZA PRORACUN f  344 RED !!!!!!!!!!!!!!!!!!!!"""

kombinacije_p_f = [
           [1, [2, 3, 4]],
           [2, [3, 4, 1]],
           [3, [1, 2, 4]],
           [4, [1, 2, 3]],
]

"""------------------------------STANDARDI PRAVACA--------------------------------"""

tezine_oblik_p = int(input('AKO JE STANDARD PRAVCA APSOLUTAN UPISI 1, A AKO JE ZAVISAN 2'))


#def provera_unosa_tezine_pravaca(a):
if tezine_oblik_p == 1:
    apsolutni_standard_pravaca = float(input('UNESI APSOLUTNI STANDARD PRAVACA :'))

elif tezine_oblik_p == 2:
    relativni_standard_pravca = float(input('UNESI RELATIVNI STANDARD PRAVCA : '))
    broj_girusa = int(input('UNESI BROJ GIRUSA : '))


    # TREBALO BI DA POSTOJI PROVERA I AKO SE UNESE NESTO DRUGO OSIM 1 I 2 ALI ZA SAD OVAKO
    # else:
    # tezine_oblik = input('UNESI OBLIK TEZINA PRAVACA 1 ILI 2 : ')
    # return standard_p

    """------------------------------STANDARDI DUZINA--------------------------------"""

tezine_oblik_d = int(input('AKO JE STANDARD DUZINE APSOLUTAN UPISI 1, A AKO JE ZAVISAN 2'))


if tezine_oblik_d == 1:
    apsolutni_standard_duzina = float(input('UNESI APSOLUTNI STANDARD DUZINA :'))

elif tezine_oblik_d == 2:
    stalni_deo = float(input('CEO DEO STANDARDA U mm : '))
    promenjivi_deo = float(input('PROMENJIVI DEO STANDARDA PO KM DUZINE : '))
    broj_ponavljanja = int(input('UNESI BROJ PONAVLJANJA : '))



"""-----------------------------------------POCETAK KODA--------------------------------------------"""

#BROJ REDOVA ZA PRAVCE U MATRICI "A" JE JEDNAK
redovi_A_p = int(len(pravci))

#BROJ NEPOZNATIH PARAMETARA JEDNAK JE BROJU KOLONA U MATRICI "A"
kolone_A = 2*int(len(poc_kord)) + int(len(kombinacije_p_f))
print("BROJ PRAVACA U MATRICI A = " +str(redovi_A_p)+ ", BROJ KOLONA U MATRICI A =" +str(kolone_A))

"""
#PRVO FORMIRAMO MATRICU 0 SA BROJEM REDOVA I KOLONA
matrica_A_p = [[0]*kolone_A]*redovi_A_p
for i in matrica_A_p:
    print(i)
"""


#PRAZNA MATRICA A ZA PRAVCIMA
matrica_A_p = []

#MATRICA P
kolone_P = int(len(pravci)) + int(len(duzine))
matrica_P_p = []


"""------------------------PETLJA ZA POPUNU MATRICE A PRAVACA------------------------------"""
for index, i in enumerate(pravci):

    red_nula = [0]*kolone_A
    print (red_nula)
    #red iz kod izvlaci koordinate
    #red_sa = i
    print("PRAVAC SA TACKE NA TACKU: " + str(i))
    #print(pravci_vrednosti[index])

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

    for j, red in enumerate(kombinacije_p_f):
        if red[0] == i[0]:
            red_nula[2 * int(len(poc_kord)) + j] = 1

    print (red_nula)

    matrica_A_p.append(red_nula)

    """------------------------------STANDARDI PRAVACA I DUZINA--------------------------------"""



    if tezine_oblik_p == 1:
        standard_p = 1 / math.pow(apsolutni_standard_pravaca, 2)
    elif tezine_oblik_p == 2:
        standard_p = broj_girusa/math.pow(relativni_standard_pravca, 2)


    # ------------DEO ZA TEZINE P--------------

    red_nula_P_p = [0]*kolone_P

    red_nula_P_p[index] = standard_p

    matrica_P_p.append(red_nula_P_p)




#RACUNANJE DELA ZA POPRAVKE F OD PRAVACA




print("MATRICA A_PRAVACA: ")
for i in matrica_A_p:
    print(i)



print()
print()
print("          MATRICA A DUZINA           ")

matrica_A_d = []
matrica_f_d = []
matrica_P_d = []
"""------------------------PETLJA ZA POPUNU MATRICE A DUZINA I MATRICA F DUZINA I MATTRICU P DUZINA------------------------------"""

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

    #------------DEO ZA POPRAVKE F OD DUZINA-------------

    duz = duzina(t1, t2)

    merena_duz = duzine_vrednosti[index]
        #PREBACIVANJE U MILIMETRE!!!!!
    f_i_d = (duz - merena_duz)*1000

    matrica_f_d.append(f_i_d)

    """------------------------------STANDARDI  DUZINA--------------------------------"""

    if tezine_oblik_d == 1:
        standard_d = 1 / math.pow(apsolutni_standard_duzina, 2)
    elif tezine_oblik_d == 2:
        relativni_standard_duzina = stalni_deo + (promenjivi_deo*(duz))/1000
        standard_d = broj_ponavljanja / math.pow(relativni_standard_duzina, 2)
    # ------------DEO ZA TEZINE D--------------

    red_nula_P_d = [0] * kolone_P

    red_nula_P_d[index+len(pravci)] = standard_d

    matrica_P_d.append(red_nula_P_d)




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



"""------------------------MATRICA f RAZLIKU PRAVACA----------------------------"""

print("!!!!!!!!!!!!!!! OVDE NAMESTITI MATRICU KOMBINACIJA PRAVACA ZA PRORACUN f  344 RED !!!!!!!!!!!!!!!!!!!!")
kombinacije_p_f = [
           [1, [2, 3, 4]],
           [2, [3, 4, 1]],
           [3, [1, 2, 4]],
           [4, [1, 2, 3]],
]
matrica_f_p = []
#MATRICA ZA SVE SREDNJE Z_0
br_zxz = len(kombinacije_p_f)
mat_z_0 = []


for i, vred_reda in enumerate(kombinacije_p_f):
    print(i, vred_reda)
    #print(vred_reda[0])
    br_sta = vred_reda[0]
    #print("STAJALISTE = "+str(br_sta))
    vizure = vred_reda[1]
    #Z ZA JEDNO STAJALISTE
    z_i = []

    #PRVO RADIMO IZLISTAVANJE DA BI NAPRAVILI MATRICU Z_0_i
    for j, br_viz in enumerate(vizure):

        y1 = poc_kord[br_sta-1][0]
        x1 = poc_kord[br_sta-1][1]
        t1 = [y1, x1]

        y2 = poc_kord[br_viz-1][0]
        x2 = poc_kord[br_viz-1][1]
        t2 = [y2, x2]
        #print("KOORD STAJALISTA = " + str(y1) + ", " + str(x1))
        #print("KOORD VIZURE = " + str(y2) + ", " + str(x2))

        dir_ugao = direkcioni.dir_finkc(t1, t2)
        #print("DIREKCIONI UGAO JE " + str(dir_ugao))
        #print(j, br_viz)
        ugao = pravci_vrednosti[i][j]
        #print("ODMERENI PRAVAC JE "+str(ugao))
        if ugao-dir_ugao <= 0:
            z_i_i = ugao + 2*math.pi - dir_ugao
        else:
            z_i_i = ugao - dir_ugao
        z_i.append(z_i_i)

    print(z_i)
    z_i_0 = sum(z_i)/len(z_i)
    print("SREDNJA VREDNOST Z = "+str(z_i_0))

    mat_z_0.append(z_i_0)



    #MATRICA POPRAVAKA PRAVACA


    #RACUNANJE POJEDINACNIH POPRAVAKA ZA SVE PRAVCE
    for j, br_viz in enumerate(vizure):

        y1 = poc_kord[br_sta-1][0]
        x1 = poc_kord[br_sta-1][1]
        t1 = [y1, x1]

        y2 = poc_kord[br_viz-1][0]
        x2 = poc_kord[br_viz-1][1]
        t2 = [y2, x2]
        print("KOORD STAJALISTA = " + str(y1) + ", " + str(x1))
        print("KOORD VIZURE = " + str(y2) + ", " + str(x2))

        dir_ugao = direkcioni.dir_finkc(t1, t2)
        print("DIREKCIONI UGAO JE " + str(dir_ugao))
        #print(j, br_viz)
        ugao = pravci_vrednosti[i][j]
        print("ODMERENI PRAVAC JE "+str(ugao))
        print()

        f_i = dir_ugao + z_i_0 - ugao
        #OVO JE DA BI SE RESILI VREDNOSTI BLIZU 360 NPR 359 59 30
        if f_i > 6.27:
            f_i = f_i - 2 * math.pi
        # f VREDNOSTI U SEKUNDAMA
        f_i_sec = math.degrees(f_i)*3600

        matrica_f_p.append(f_i_sec)

    #print(matrica_f_p)


    print()
    print()
print("MATRICA F ZA PRAVCE")
for i in matrica_f_p:
    print(i)
print()
print()
print("MATRICA F ZA DUZINE")
for i in matrica_f_d:
    print(i)
print()
print()

matrica_f = []

print("--------------MATRICA F KOMPLETNA----------------")
for i in matrica_f_p:
    matrica_f.append(i)
for i in matrica_f_d:
    matrica_f.append(i)
for i in matrica_f:
    print(i)
print()
print()

"""------------------------KOMPLETNA MATRICA TEZINA P ----------------------------"""
matrica_P = []
for i in matrica_P_p:
    matrica_P.append(i)
for i in matrica_P_d:
    matrica_P.append(i)

#PRIKAZ P MATRICE
print("MATRICA P KOMPLETNA")
for i in matrica_P:
    print(i)

"""---PAKET MATRICA ZA OBRACUN R_T MATRICE---"""
def matrice_paket_1 ():
    return [poc_kord, br_zxz]

"""---PAKET MATRICA ZA PRORACUN QX MATRICE---"""
def matrice_paket_2 ():
    return [matrica_A, matrica_P, matrica_f, pravci, duzine_vrednosti]

#print("NACIN DEFINISANJA DATUMA")
#print("AKO JE KLASICAN UNESI BROJ 1")
#print("AKO JE MINIMALNI TRAG NA SVE TACKE UNESI 2")
#print("AKO JE PARCIJALNI MINIMALNI TRAG UNESI 3")
#izbor_datuma = int(input())
#print(izbor_datuma)






