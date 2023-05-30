#import direkcioni
#from spoj1 import matice_paket_1
import numpy as np
import math
#FUNKCIJA ZA KONVERZIJU U RADIJANE

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
            [1082.58, 1075.03],
            [1000, 1000],
            [1000, 1187.84],
            [1073.89, 1148.9],
            [1082.58, 1075.03]
            ]

pravci = [
            [1, 2, radians(0, 0, 0)],
            [1, 3, radians(26, 23, 30)],
            [1, 4, radians(47, 44, 31)],
            [2, 3, radians(0,0,0)],
            [2, 4, radians(26,0,16)],
            [2, 1, radians(62,12,37)],
            [4, 1, radians(0,0,0)],
            [4, 2, radians(96,3,7)],
            [4, 3, radians(125,32,54)]
         ]

kombinacije_p_f = [
           [1, [2, 3, 4]],
           [2, [3, 4, 1]],
           [4, [1, 2, 3]],
]

mat_A= []

redovi_A_p = int(len(pravci))

#BROJ NEPOZNATIH PARAMETARA JEDNAK JE BROJU KOLONA U MATRICI "A"
kolone_A = 2*int(len(poc_kord)) + int(len(kombinacije_p_f))

for i, vred in enumerate(pravci):
    red_nula = [0]*kolone_A
    for j, red in enumerate(kombinacije_p_f):
        if red[0] == vred[0]:
            red_nula[2*int(len(poc_kord)) + j] = 1
    mat_A.append(red_nula)

for i in mat_A:
    print(i)

"""



a = np.array([[0, 1, 3], [5, 7, 9]])
b = np.array([[0, 2, 4], [6, 8, 10]])
c = np.concatenate((a, b), axis=1)
print(c)

"""

"""
# input two matrices of size n x m
matrix1 = [[1, 1, 1],
           [2, 2, 2],
           ]
matrix2 = [[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]]

res = [[0 for x in range(len(matrix2))] for y in range(len(matrix1))]
print(res)
# explicit for loops
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix1[0])):
            # resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]

print(res)

res_2 = np.dot(matrix1, matrix2)
print(res_2)
"""

"""----------------------FUNKCIJA KOJA RADI UNOS TACAKA DOK MI TO NE PREKINEMO----------------------------"""
"""
print("UNSI BROJ TACKE KOJI DEFINISE TRAG")
print("AKO UNESES 0, ZNACI DA JE UNOS TACAKA GOTOV")


#def unos_t
#unos = int(input())
unesene_tacke = []

def min_tacke ():
    unos = int(input())
    print(unos)
    if unos != 0:
        unesene_tacke.append(unos)
        min_tacke()
    elif unos == 0:
        print("KRAJ UNOSA")
    else:
        print("NESTO STE KRIVO UNELI")

min_tacke()

unesene_tacke.extend([0]*len(poc_kord))
print(unesene_tacke)

for i in range(5):
    print(i)



for i, val in enumerate(poc_kord):
    if (i) % 2 == 0:
        print("NEPAR "+str(poc_kord[i]))
        print(i)
        rez = (i)%2
        print(rez)
        print()
    else:
        print("PAR "+str(poc_kord[i]))
        print(i)
        rez = (i) % 2
        print(rez)
        print()



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

zeros = [[0]*5]*5

lista_1 = [1, 2, 3, 3, 5]
lista = [10, 20, 30, 40, 50]

for idx, val in enumerate(lista_1):
    br_reda = idx
    vrednost = val
    #zeros[br_reda][br_reda] = 1
    print(br_reda, vrednost)
    print(lista[idx])

for i in lista_1:
    #br_reda = idx
    #vrednost = val
    #zeros[br_reda][br_reda] = 1
    print(i)

kombinacije_p_f = [
           [1, 2, 3, 4],
           [2, 3, 4, 1],
           [3, 1, 2, 4],
           [4, 1, 2, 3],
]

matrica_f_p = []
for i, vred_reda in enumerate(kombinacije_p_f):
    print(i, vred_reda)
    print(vred_reda[0])
    br_sta = vred_reda[0]
    for in_viz in range(1, len(vred_reda)):
        br_viz = vred_reda[in_viz]
        print(br_viz)

#print(matrica_f_p)

[matrice_a, matrica_p, matrica_f] = matice_paket_1()

print("MATRICA A :")
for i in matrice_a:
    print(i)

print("MATRICA P :")
for i in matrica_p:
    print(i)

print("MATRICA F :")
for i in matrica_f:
    print(i)
"""









