import direkcioni
import math
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

"""-------------------POCETAK KODA-------------------"""

kombinacije_p_f = [
           [1, [2, 3, 4]],
           [2, [3, 4, 1]],
           [3, [1, 2, 4]],
           [4, [1, 2, 3]],
]

matrica_f_p = []


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
        if f_i >5 :
            f_i = f_i - 2*math.pi
        # f VREDNOSTI U SEKUNDAMA
        f_i_sec = math.degrees(f_i)*3600

        matrica_f_p.append(f_i_sec)

    print(matrica_f_p)


    print()
    print()
print("MATRICA F ZA PRAVCE")
print(matrica_f_p)

