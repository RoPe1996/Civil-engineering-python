import math

def dir_finkc (a, b):
    y1 = a[0]
    x1 = a[1]
    y2 = b[0]
    x2 = b[1]

    dy = y2-y1
    dx = x2-x1



    if dy > 0 :
        if dx > 0:
            dir_ugao = math.atan(dy/dx)
            #print(dir_ugao)
            return dir_ugao
        elif dx == 0:
            dir_ugao = math.pi/2
            #print(dir_ugao)
            return dir_ugao
        else:
            dir_ugao_1 = math.atan(dy / dx)
            #print(dir_ugao_1)
            #OVO JE DEO OD +- 180
            if dir_ugao_1 > math.pi:
                dir_ugao = dir_ugao_1 - math.pi
                return dir_ugao
            else:
                dir_ugao = dir_ugao_1 + math.pi
                return dir_ugao


    elif dy == 0:
        if dx > 0:
            dir_ugao = 0
            #print(dir_ugao)
            return dir_ugao
        else:
            dir_ugao = math.pi
            #print(dir_ugao)
            return dir_ugao
    #AKO JE dy < 0
    else:
        if dx > 0:
            dir_ugao_1 = math.atan(dy / dx)
            #print(dir_ugao_1)
            # OVO JE DEO OD +- 180
            if dir_ugao_1 > math.pi*2:
                dir_ugao = dir_ugao_1 - math.pi*2
                return dir_ugao
            else:
                dir_ugao = dir_ugao_1 + math.pi * 2
                return dir_ugao
        elif dx == 0:
            dir_ugao = math.pi*(3/2)
            #print(dir_ugao)
            return dir_ugao
        else:
            dir_ugao_1 = math.atan(dy / dx)
            #print(dir_ugao_1)
            #OVO JE DEO OD +- 180
            if dir_ugao_1 > math.pi:
                dir_ugao = dir_ugao_1 - math.pi
                return dir_ugao
            else:
                dir_ugao = dir_ugao_1 + math.pi
                return dir_ugao



#ugao = dir_finkc([1,1], [1,2])
#print (str(ugao))
