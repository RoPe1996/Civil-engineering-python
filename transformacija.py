import numpy as np
from proracun_Qx import funkcija_Qx

print()
print("-------------------TRANSFORMACIJA-------------------")
print("IZABERITE IZ KOG DATUMA ZELITE TRANSFORMISATI")
[mat_Qx_1, vel_N_1, x_ocenjeno_1] = funkcija_Qx()
print()
print("-------------------TRANSFORMACIJA-------------------")
print("IZABERITE U KOJI DATUM ZELITE TRANSFORMISATI")
[mat_Qx_2, vel_N_2, x_ocenjeno_2] = funkcija_Qx()

x_trans = np.dot(mat_Qx_2, vel_N_1)

x_trans = np.dot(x_trans, x_ocenjeno_1)
print()
print()
print("---------TRANSFORMISANE VREDNOSTI---------")
print(x_trans)

