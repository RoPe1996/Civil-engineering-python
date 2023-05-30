import math

def dir_finkc_rad_deg (dy, dx):



    if dy > 0 :
        if dx > 0:
            dir_ugao = math.atan(dy/dx)
            #print(dir_ugao)
            #return dir_ugao
        elif dx == 0:
            dir_ugao = math.pi/2
            #print(dir_ugao)
            #return dir_ugao
        else:
            dir_ugao_1 = math.atan(dy / dx)
            #print(dir_ugao_1)
            #OVO JE DEO OD +- 180
            if dir_ugao_1 > math.pi:
                dir_ugao = dir_ugao_1 - math.pi
                #return dir_ugao
            else:
                dir_ugao = dir_ugao_1 + math.pi
                #return dir_ugao


    elif dy == 0:
        if dx > 0:
            dir_ugao = 0
            #print(dir_ugao)
            #return dir_ugao
        else:
            dir_ugao = math.pi
            #print(dir_ugao)
            #return dir_ugao
    #AKO JE dy < 0
    else:
        if dx > 0:
            dir_ugao_1 = math.atan(dy / dx)
            #print(dir_ugao_1)
            # OVO JE DEO OD +- 180
            if dir_ugao_1 > math.pi*2:
                dir_ugao = dir_ugao_1 - math.pi*2
                #return dir_ugao
            else:
                dir_ugao = dir_ugao_1 + math.pi * 2
                #return dir_ugao
        elif dx == 0:
            dir_ugao = math.pi*(3/2)
            #print(dir_ugao)
            #return dir_ugao
        else:
            dir_ugao_1 = math.atan(dy / dx)
            #print(dir_ugao_1)
            #OVO JE DEO OD +- 180
            if dir_ugao_1 > math.pi:
                dir_ugao = dir_ugao_1 - math.pi
                #return dir_ugao
            else:
                dir_ugao = dir_ugao_1 + math.pi
                #return dir_ugao


    sekundi_ukupno = round((dir_ugao / (2 * math.pi)) * 360 * 60 * 60)
    #print(str(sekundi_ukupno))
    sekundi = sekundi_ukupno % 60
    minuta = round((sekundi_ukupno / 60) % 60)
    stepeni = math.trunc(((sekundi_ukupno) / (60 * 60)))
    #print(str(stepeni) + " " + str(minuta) + " " + str(sekundi))
    return [dir_ugao, [stepeni, minuta, sekundi]]



#ugao = dir_finkc_rad_deg(2, 2)
#print (str(ugao))
