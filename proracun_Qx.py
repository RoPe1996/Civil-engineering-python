import math
import numpy as np
from spoj1 import matrice_paket_2
from spoj1 import matrice_paket_1
from direkcioni_rad_deg import dir_finkc_rad_deg




"""---------------FUNKCIJE-------------"""
def radians (a, b, c):
    rez_rad = ((a+(b/60)+(c/3600))/360)*2*math.pi
    return (rez_rad)

def deg_min_sec (dir_ugao):
    sekundi_ukupno = round((dir_ugao / (2 * math.pi)) * 360 * 60 * 60)
    # print(str(sekundi_ukupno))
    sekundi = sekundi_ukupno % 60
    minuta = round((sekundi_ukupno / 60) % 60)
    stepeni = math.trunc(((sekundi_ukupno) / (60 * 60)))
    # print(str(stepeni) + " " + str(minuta) + " " + str(sekundi))
    return [stepeni, minuta, sekundi]

"""------------FUNKCIJA ZA RACUNANJE Qx---------------"""

def funkcija_Qx ():



    """---MATRICA N---"""

    [matrica_A, matrica_P, matrica_f, pravci_0, duzine_vrednosti_0] = matrice_paket_2()
    mat_A = np.array(matrica_A)
    mat_P = np.array(matrica_P)
    mat_f = np.array(matrica_f)

    vel_N = np.dot(mat_A.transpose(), mat_P)

    vel_N = np.dot(vel_N, mat_A)



    print()
    print("MATRICA N")
    print()
    print(vel_N)



    """---MATRICA n---"""

    malo_n = np.dot(np.transpose(mat_A), mat_P)
    malo_n = np.dot(malo_n, mat_f)

    print()
    print("MATRICA n")
    print()
    print(malo_n)

    """---MATRICA Qx---"""

    print()
    print("NACIN DEFINISANJA DATUMA")
    print("AKO JE KLASICAN UNESI BROJ 1")
    print("AKO JE MINIMALNI TRAG NA SVE TACKE UNESI 2")
    print("AKO JE PARCIJALNI MINIMALNI TRAG UNESI 3")
    izbor_datuma = int(input())
    print(izbor_datuma)



    if izbor_datuma == 1:
        from matrica_R_klas import paket_R_T_klas
        [mat_R_T, br_zxz, koef_d] = paket_R_T_klas()


    elif izbor_datuma == 2:
        from matrica_R_min_1 import paket_R_T_min1
        [mat_R_T, br_zxz, koef_d] = paket_R_T_min1()

    elif izbor_datuma == 3:
        from matrica_R_min_2 import paket_R_T_min2
        [mat_R_T, br_zxz, koef_d] = paket_R_T_min2()
    else:
        print("NESTO STE KRIVO UNELI")


    #DODAVANJE R MATRICE SASTRANE
    mat_R_T = np.array(mat_R_T)
    mat_R = np.transpose(mat_R_T)


    #DODAVANEJ mat_R SASTRANE MATRICE N
    vel_N = np.concatenate((vel_N, mat_R), axis=1)
    #vel_N = np.append(vel_N, mat_R, 1)

    #print(vel_N)

    #SAD TREBA DODATI NA R_T JOS REDOVE NULA KOLIKO IMA ZxZ VELICINA

    mat_ZxZ = np.array([[0 for i in range(koef_d)] for j in range(koef_d)])

    #print(mat_ZxZ)
    #DODAVANJE NULA SASTRANE ORIGINALNE R_T MATRICE ZATO JE AXIS=1, DOBIJEMO PROSIRENU R_T MATRICU
    mat_R_T = np.concatenate((mat_R_T, mat_ZxZ), axis=1)
    print(mat_R_T)

    #SPAJANJE PROSIRENE N MATRICE SA PROSIRENOM R_T MATRICEOM
    #print(vel_N)
    #print(mat_R_T)
    mat_Qx = np.concatenate((vel_N, mat_R_T), axis=0)

    print()
    print("PRIPREMA ZA INVERZIJU MATRICE Qx")
    print(mat_Qx)
    print()

    mat_Qx = np.linalg.inv(mat_Qx)

    print()
    print("MATRICA Qx")
    print(mat_Qx)
    print()


    """---VREDNOSTI DEFEKTA d, NEPOZNATIH PARAMETARA u I MERENIH VELICINA n ---"""

    print()

    koef_n = len(mat_A)
    print("BROJ MERENIH VELICINA = " + str(koef_n))
    koef_u = len(mat_A[0])
    print("BROJ NEPOZNATIH PARAMETARA = " + str(koef_u))
    koef_d = koef_d
    print("DEFEKT MREZE JE = " + str(koef_d))
    print()

    """---PRVO TREBA IZDVOJITI KORISTAN DEO MATRICE Qx---"""

    mat_Qx_korist = []

    #for i in


    for i in range(koef_u):
        red_qx = []
        for j in range(koef_u):
            red_qx.append(mat_Qx[i][j])
        mat_Qx_korist.append(red_qx)


    print()
    print("------------KORISAN DEO MATRICE Qx--------------")
    for i in mat_Qx_korist:
        print(i)

    #---OBLIK MATRICE---
    #print(np.shape(mat_Qx_korist))
    #print(np.shape(malo_n))



    """"---MATRICA MALO x - OCENE (POPRAVKE) KOORDINATA---"""
    print()
    print("---MATRICA MALO x - OCENE (POPRAVKE) KOORDINATA [mm]---")
    x_ocenjeno = np.dot(mat_Qx_korist, malo_n)
    for i, vred in enumerate(x_ocenjeno):

        x_ocenjeno[i] = vred*(-1)

        print("ELEMENT MATRICE x OCENJENO  "+str(x_ocenjeno[i]))


    """---MATRICA v POPRAVAKA MERENIH VELICINA---"""

    mat_v_ocenjeno = np.dot(mat_A, x_ocenjeno)
    #print()
    #print(mat_v_ocenjeno)
    print()
    print("--------------VREDNOSTI MATRICE v POPRAVAKA MERENIH VELICINA----------------------")
    for i, vred in enumerate(mat_v_ocenjeno):
        mat_v_ocenjeno[i] = mat_v_ocenjeno[i] + mat_f[i]

    print()
    print(mat_v_ocenjeno)

    print()
    print("--------------POPRAVLJENE VREDNOSTI MERENIH VELICINA----------------------")
    print("----------------------------PRAVCI----------------------------------------")
    oc_mer_vel = []
    for i, vred in enumerate (pravci_0):
        prav_ocenjen_rad = pravci_0[i][2] + radians(0, 0, mat_v_ocenjeno[i])
        prav_ocenjen_deg = deg_min_sec(prav_ocenjen_rad)
        print("OCENJENI PRAVCI U RAD = " + str(prav_ocenjen_rad) + " U DEG = " + str(prav_ocenjen_deg))
        oc_mer_vel.append([prav_ocenjen_rad, prav_ocenjen_deg])

    print("----------------------------DUZINE----------------------------------------")
    #mat_Qx_korist [2 * len(poc_kord):]
    for i, vred in enumerate (duzine_vrednosti_0):
        duz_ocenjena = duzine_vrednosti_0[i] + mat_v_ocenjeno[len(pravci_0) + i]/1000
        print("OCENENJA DUZINA U m = "+str(duz_ocenjena))
        oc_mer_vel.append(duz_ocenjena)







    """---PROVERA MATRICA (fT*P*f +nT*x)- vT*P*v = 0 ---"""

    vT_P = np.dot(np.transpose(mat_v_ocenjeno), mat_P)
    vT_P_v = np.dot(vT_P, (mat_v_ocenjeno))

    fT_P = np.dot(np.transpose(mat_f), mat_P)
    ft_P_f = np.dot(fT_P, mat_f)

    nT_x = np.dot(np.transpose(malo_n), x_ocenjeno)

    razlika = vT_P_v - (ft_P_f + nT_x)
    print()
    print("--------------ISPRAVNOST IZRAVNANJA----------------------")
    print("PROVERA AKO JE JEDNAKA 0 ONDA JE U REDU =" + str(razlika))

    """---OCENA DISPERZIVNOG KOEFICJENTA m_2_o (matematicko ocekivanje)---"""

    #NULTA HIPOTEZA
    print()
    print("--------------PROVERA GRUBIH GRESAKA----------------------")
    koef_f = koef_n - koef_u + koef_d

    m_o_2 = ((vT_P_v / koef_f))

    #print()
    #print("APASTERIORI DISPERZIVNI KOEFICJENT m_o = " + str(m_o))

    #ALTERNATIVNA HIPOTEZA
    import scipy.stats

    m_a = scipy.stats.f.isf(0.05, koef_f, 10000)

    #print("APASTERIORI DISPERZIVNI KOEFICJENT m_2_o = " + str(m_2_o))
    #print(m_a)

    if m_o_2 < m_a:
        print("NEMA GRUBIH GRESAKA")
        print("m_o = " +str(m_o_2) + "m_a = " + str(m_a))
        print()
    else:
        print("IMA GRUBIH GRESAKA")
        print("m_o = " + str(m_o_2) + "m_a = " + str(m_a))
        print()


    """"---POPRAVLJENE KOORDINATE---"""
    print()
    print("--------------POPRAVLJENE KOORDINATE [m]--------------")
    print()
    [poc_kord, br_zxz] = matrice_paket_1()
    ocenjene_koordinate = []
    for i in range(len(poc_kord)):
        red = [0, 0]
        red[0] = poc_kord[i][0] + (x_ocenjeno[i*2] / 1000)
        red[1] = poc_kord[i][1] + (x_ocenjeno[i*2 + 1] / 1000)

        ocenjene_koordinate.append(red)

    for i in ocenjene_koordinate:
        print(i)

    """---DIJAGONALNI ELEMENTI MATRICE Qx---"""

    print()
    print("-------DIJAGONALNI ELEMENTI MATRICE Qx I OCENA TACNOSTI NEPOZNATIH PARAMETARA---------")
    print()
    for i in range(2 * len(poc_kord)) :

        print("DIJAGONALNI ELEMENT Qx = " + str(math.sqrt(mat_Qx_korist[i][i])))
        print()
    #MATRICA ELIPSI I TETA UGLOVA [lambda i, lambda 2, teta]
    mat_elipse_teta = []
    for i in range(len(poc_kord)):

        qyy = mat_Qx_korist[i*2][i*2]
        qxx = mat_Qx_korist[i*2+1][i*2+1]
        qxy =mat_Qx_korist[i*2+1][i*2]

        lambda1 = abs((qxx + qyy + math.sqrt(math.pow((qxx - qyy), 2) + 4 * math.pow(qxy, 2))) / 2)
        lambda2 = abs((qxx + qyy - math.sqrt(math.pow((qxx - qyy), 2) + 4 * math.pow(qxy, 2))) / 2)
        #5.99 JE VREDNOST ZA CHIINV(alfa, f) alfa = 0.05, f = 2 (DVODIMENZIONA MREZA)
        poluosa_A = math.sqrt(lambda1 * 5.99)
        poluosa_B = math.sqrt(lambda2 * 5.99)
        #TETA U RADIJANIMA
        [teta_radx2, teta_degx2] = dir_finkc_rad_deg(2*qxy, (qxx-qyy))
        teta_rad = teta_radx2 / 2
        teta_deg = [ teta_degx2[0] / 2, teta_degx2[1] / 2, teta_degx2[2] / 2]
        tacka = [poluosa_A, poluosa_B, teta_rad , teta_deg]
        mat_elipse_teta.append(tacka)
        print()
        print("MATRICA ELEMENATA poluose A i B, teta u RADIJANIMA I S/MIN/SEC " + str(tacka))





    print("-----------------PROBA OCENJENO Z----------------")
    for i, vred in enumerate(mat_Qx_korist [2 * len(poc_kord):]):
        print("DIJAGONALNI ELEMENT ZA Zi OCENENJENO = " + str(vred[2 * len(poc_kord)+i]))
        print()


    """----------------------ANALIZA TACNOSTI GEODETSKIH MREZA--------------------------"""
    print("-----------------ANALIZA TACNOSTI GEODETSKIH MREZA ----------------")
    print("-------------Ql KOFAKTORSKA MATRICA IZRAVNATIH MERENIH VELICINA --------------")
    mat_Ql = np.dot( np.dot(mat_A, mat_Qx_korist), np.transpose(mat_A) )
    print(mat_Ql)


    print()
    print("-------------Qv KOFAKTORSKA MATRICA POPRAVAKA MERENIH VELICINA --------------")
    mat_Qv = []
    p_minus_1 = np.linalg.inv(mat_P)

    for i, vred in enumerate(p_minus_1):
        red=[]
        for j, celija in enumerate(vred):
            red.append(p_minus_1[i][j] - mat_Ql[i][j])

        print(red[i])
        mat_Qv.append(red)

    print()
    print("-------------------UNUTRASNJA POUZDANOST-------------------")
    print("----------------------------rii----------------------------")
    mat_rii = np.dot(mat_Qv, mat_P)

    for i in mat_rii:
        print(mat_rii[i][i])

    """
    mat_rii = []
    #UTICAJ GRUBE GRESKE I-TOG OPAZANJA NA I-TU POPRAVKU
    for i, vred in enumerate(mat_Qv):
        ri = mat_Qv[i][i] * mat_P[i][i]
        print(ri)
        mat_rii.append(ri)
    """
    print()
    print("----------------------------Gii----------------------------")
    mat_Gii = []

    for i, vred in enumerate(mat_Qv):
        gi = 2.802 / (mat_P[i][i]*math.sqrt(mat_Qv[i][i]))
        print(gi)
        mat_Gii.append(gi)

    vel_N_parc = []
    for i, vred in enumerate(vel_N):
        red = []
        for j, vred in enumerate(mat_Qx_korist):
            red.append(vel_N[i][j])
        vel_N_parc.append(red)

    return [mat_Qx_korist ,vel_N_parc, x_ocenjeno]

funkcija_Qx()










