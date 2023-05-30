import math
#from spoj1 import matice_paket_1

"""------------------------------POCETNE KOORDINATE I PODACI-------------------------------"""
poc_kord = [
            [1934.594, 1820.979],
            [2050.591, 1810.192],
            [2104.296, 1734.664],
            [2087.261, 1647.372],
            [1980.073, 1602.704],
            [1893.92, 1649.316],
            [1867.332, 1739.565],
            ]

#[poc_kord] = matice_paket_1()



#DUZINA JEDNOG REDA MATRICE R_T
r = len(poc_kord)*2

print ("DUZINA JEDNOG REDA MATRICE R_T = " +str(r))

print()
print("UNESI DEFEKT MREZE")
def_mreze = range(int(input()))
print("NACIN DEFINISANJA DATUMA")
print("AKO JE KLASICAN UNESI BROJ 1")
print("AKO JE MINIMALNI TRAG NA SVE TACKE UNESI 2")
print("AKO JE PARCIJALNI MINIMALNI TRAG UNESI 3")
izbor_datuma = int(input())
print(izbor_datuma)

"RACUNANJE KLASNICNOG NACINA"

matrica_R = []
matrica_R_T = []

if izbor_datuma == 1:

    for i in def_mreze:
        # ZA PRVI RED MATRICE

        if i == 0:

            print("KOJOM TACKOM JE DEFINISANA TRANSLACIJA (ty) PO Y ")

            ty = int(input())
            red_nula = [0] * r
            pozicija = (ty-1)*2
            red_nula[pozicija] = 1
            red_nula.extend([0]*len(poc_kord))
            print("PRVI RED MATRICE R")
            print(red_nula)
            matrica_R_T.append(red_nula)

        elif i == 1:

            print("KOJOM TACKOM JE DEFINISANA TRANSLACIJA (tx) PO X ")

            tx = int(input())
            red_nula = [0] * r
            pozicija = ((tx - 1) * 2) +1
            red_nula[pozicija] = 1
            print("DRUGI RED matrica_R_T")
            red_nula.extend([0] * len(poc_kord))
            print(red_nula)
            matrica_R_T.append(red_nula)


        elif i == 2:
            print("KOJOM TACKOM JE DEFINISANA ROTACIJA (rZ)")

            rZ = int(input())
            red_nula = [0] * r
            pozicija = ((rZ - 1) * 2)
            red_nula[pozicija] = 1
            print("TRECI RED matrica_R_T")
            red_nula.extend([0] * len(poc_kord))
            print(red_nula)
            matrica_R_T.append(red_nula)



        elif i == 3:
            print("KOJOM Y TACKOM JE DEFINISANO SKALIRANJE (S)")

            s = int(input())
            red_nula = [0] * r
            pozicija = ((s - 1) * 2) + 1
            red_nula[pozicija] = 1
            print("CETVRTI RED matrica_R_T")
            red_nula.extend([0] * len(poc_kord))
            print(red_nula)
            matrica_R_T.append(red_nula)
        else:
            print("UNESLI STE NESTO KRIVO")

#AKO JE IZBOR DATUMA MINIMALNI TRAG NA SVE TACKE

elif izbor_datuma == 2:
    #BROJ TACAKA KOJE DEFINISU DATUM
    m = int(len(poc_kord))
    print("UKUPAN BROJ TACAKA KOJE DEFINISU DATUM " + str(m))
    mi = math.sqrt(m)
    #RACUNANANJE Y I X SREDNJE
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
        #TEKUCE dy
        dy = i[0] - y_srednje
        suma_dy_2 = suma_dy_2 + math.pow(dy, 2)
        dx = i[0] - x_srednje
        suma_dx_2 = suma_dx_2 + math.pow(dx, 2)
    g = math.sqrt(suma_dy_2 + suma_dx_2)

    #UREDJENI PAR KSI I ETA ZA SVAKU TACKU
    matrica_ksi_eta = []
    for i in poc_kord:
        ksi = (i[1] - x_srednje)/g
        eta = (i[0] - y_srednje)/g
        matrica_ksi_eta.append([ksi, eta])

    #print()
    #print("MATRICA KSI I ETA")
    #print(matrica_ksi_eta)
# ZA OSTATAK SA DELJENJEM %


    for i in def_mreze:
        
        # PRVI RED MATRICE R_T
        if i == 0:
            red_nula = [0] * r
            #PROVERA PARAN NEPARAN BROJ
            for i, val in enumerate(red_nula):
                if i % 2 == 0:
                    red_nula[i] = 1/mi
                    #NEPARAN
            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(red_nula)


                    
        # DRUGI RED MATRICE R_T
        elif i == 1:
            red_nula = [0] * r
            for i, val in enumerate(red_nula):
                if i % 2 != 0:
                    red_nula[i] = 1 / mi
                    # PARAN
            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(red_nula)

        # TRECI RED MATRICE R_T
        elif i == 2:
            cista_matrica = []
            for i, vred in enumerate(matrica_ksi_eta) :
                ksii = vred[0]*(-1)
                etaa = vred[1]
                cista_matrica.append(ksii)
                cista_matrica.append(etaa)
            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(cista_matrica)
            matrica_R_T.append(red_nula)

        # CETVRTI RED MATRICE R_T
        elif i == 3:
            cista_matrica = []
            for i, vred in enumerate(matrica_ksi_eta):
                ksii = vred[0]
                etaa = vred[1]
                cista_matrica.append(etaa)
                cista_matrica.append(ksii)
            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(cista_matrica)
            matrica_R_T.append(red_nula)
        else:
            print("UNESLI STE NESTO KRIVO")



#AKO JE IZBOR DATUMA MINIMALNI TRAG NA ODREDJENE TACKE
elif izbor_datuma == 3:

    unesene_tacke = []

    def min_tacke():
        print("UNESI TACKE KOJE KONFIGURISU MATRICU R_T ")
        print("UNESI BROJ 0 AKO SU TO SVE TACKE KOJE KONFIGURISU ")
        unos = int(input())
        print(unos)
        if unos != 0:
            unesene_tacke.append(unos)
            min_tacke()
        elif unos == 0:
            print("KRAJ UNOSA")
            pass
        else:
            print("NESTO STE KRIVO UNELI POKUSAJ PONOVO")
            min_tacke()
    #POZIV FUNKCIJE
    min_tacke()
    print("TACKE PARCIJALNOG MIN TRAGA")
    print(unesene_tacke)

    #KORDINATE TRAGA
    kord_traga = []

    for i, vred in enumerate(unesene_tacke):
        kord_traga.append(poc_kord[vred-1])

    for i in kord_traga:
        print()
        print("KOORDINATE PARCIJALNOG TRAGA")
        print(i)




    m = int(len(kord_traga))
    print("UKUPAN BROJ TACAKA KOJE DEFINISU DATUM " + str(m))
    mi = math.sqrt(m)
    # RACUNANANJE Y I X SREDNJE
    y_suma = 0
    x_suma = 0
    for i in kord_traga:
        y_suma = y_suma + i[0]
        x_suma = x_suma + i[1]

    y_srednje = y_suma / m
    x_srednje = x_suma / m
    suma_dy_2 = 0
    suma_dx_2 = 0
    for i in kord_traga:
        # TEKUCE dy
        dy = i[0] - y_srednje
        suma_dy_2 = suma_dy_2 + math.pow(dy, 2)
        dx = i[1] - x_srednje
        suma_dx_2 = suma_dx_2 + math.pow(dx, 2)
    g = math.sqrt(suma_dy_2 + suma_dx_2)

    # UREDJENI PAR KSI I ETA ZA SVAKU TACKU
    matrica_ksi_eta = []
    #OVDE KORISTIMO SVE TACKE DA BI MOGLI POVUCI KSI I ETA SAMO ZA ONE KOJE SE UNESU
    #JER MOZE BITI DA SE UNESU TACKE NEPRAVILNIM REDOSLEDOM
    #PA CE KSI I ETA PAROVA BITI KOLIKO I UKUPNO KOORDINATA A MI CEMO IZVLACITI SAMO ONE KOJI NAM TREBAJU
    for i in poc_kord:

        ksi = (i[1] - x_srednje) / g
        eta = (i[0] - y_srednje) / g
        matrica_ksi_eta.append([ksi, eta])

    print("MATRICA KSI I ETA")
    print(matrica_ksi_eta)


    for i in def_mreze:
        print("RED U MATRICI R_T " + str(i+1))

    # PRVI RED MATRICE R_T
        if i == 0:
            print()
            print("PRVI RED MATRICE R_T")

            red_nula = [0] * r

            for i, vred in enumerate(unesene_tacke):
                print()
                print(vred)
                print(((vred-1)*2))
                red_nula[((vred-1)*2)] = 1/mi
                

            #OSTATAK NULA ZA Z DEO MATRICE
            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(red_nula)
            print(matrica_R_T)
            print()


        # DRUGI RED MATRICE R_T
        elif i == 1:
            red_nula = [0] * r

            print("DRUGI RED MATRICE R_T")
            print()


            for i, vred in enumerate(unesene_tacke):
                print()
                print(vred)
                print(((vred - 1) * 2 + 1))
                red_nula[((vred - 1) * 2 + 1)] = 1 / mi
                


            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(red_nula)
            print(matrica_R_T)
            print()


    # TRECI RED MATRICE R_T
        elif i == 2:
            red_nula = [0] * r
            print()
            print("TRECI RED MATRICE R_T")

            for i, vred in enumerate(unesene_tacke):
                print("BROJ TACKE ZA KSI I ETA")
                print(vred)
                #PAR OD KSI I ETA
                print("KSI ZA UNESENU TACKU")
                ksii = matrica_ksi_eta[vred-1][0]
                print("ETA ZA UNESENU TACKU")
                etaa = matrica_ksi_eta[vred-1][1]

                red_nula[((vred - 1) * 2)] = (-1) * ksii
                red_nula[((vred - 1) * 2 + 1)] = etaa
                


            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(red_nula)
            print(matrica_R_T)
            print()


    # CETVRTI RED MATRICE R_T
        elif i == 3:
            red_nula = [0] * r
            print()
            print("CETVRTI RED MATRICE R_T")

            for i, vred in enumerate(unesene_tacke):
                # PAR OD KSI I ETA
                ksii = matrica_ksi_eta[vred - 1][0]
                etaa = matrica_ksi_eta[vred - 1][1]

                red_nula[((vred - 1) * 2)] = etaa
                red_nula[((vred - 1) * 2 + 1)] = ksii
                
                print(matrica_R_T)

            red_nula.extend([0] * len(poc_kord))
            matrica_R_T.append(red_nula)

        else:
            print("UNESLI STE NESTO KRIVO")


print()
print("KOMPLETNA MATRICA R_T")
for i in matrica_R_T:
    print(i)