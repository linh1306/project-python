import  math
import data



def pt_2(a, b, c):
    if (a == 0):
        if (b == 0):    return False
        else:           return (-c / b)
    delta = b * b - 4 * a * c
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        return max(x1,x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        return x1
    return False

def to_radian(value):
    return float(value*math.pi/180)


def find_line_1_2(corner = 'ABS', line1='AB', line2='AS'):
    if corner[1] in line1 and corner[1] in line2:
        name = corner[0]+corner[2]
        value = math.sqrt(data.Arr_line[line1]**2 + data.Arr_line[line2]**2 - 2*data.Arr_line[line1]*data.Arr_line[line2]*math.cos(to_radian(data.Arr_corner[corner])))
        if name not in data.Arr_line:    data.Arr_line[name] = value
    if corner[1] in line1 or corner[1] in line2:
        n1 = ''.join(sorted(corner[0]+corner[1]))
        n2 = ''.join(sorted(corner[2]+corner[1]))
        name = n1 if n1 not in [line1,line2] else n2
        a = data.Arr_line[corner[0]+corner[2]]
        b = data.Arr_line[line1 if corner[0]+corner[2] == line2 else line2]
        g = math.cos(to_radian(data.Arr_corner[corner]))
        k = pt_2(1, -2*b*g, - a**2+b**2)
        if k != False:
            if name not in data.Arr_line:  data.Arr_line[name] = k
    data.Arr_corner.pop(corner)


def find_line_2_1(corner1 = 'ABS', corner2 = 'ASB', line = 'AB'):
    corner3 = min((corner1[1:3] + corner1[0]), (corner1[1:3] + corner1[0])[::-1])
    if corner3 == corner2:
        corner3 = min((corner1[2] + corner1[:2]), (corner1[2] + corner1[:2])[::-1])
    data.Arr_corner[corner3] = 180 - (data.Arr_corner[corner1]+data.Arr_corner[corner2])
    dic = {corner1[0]+corner1[2]:corner1, corner2[0]+corner2[2]:corner2, corner3[0]+corner3[2]:corner3}
    value = data.Arr_line[line]/math.sin(data.Arr_corner[dic.get(line)])
    dic.pop(line)
    key = list(dic.keys())
    if key[0] not in data.Arr_line:          data.Arr_line[key[0]] = value * math.sin(data.Arr_corner[dic.get(key[0])])
    if key[1] not in data.Arr_line:          data.Arr_line[key[1]] = value * math.sin(data.Arr_corner[dic.get(key[1])])
    data.Arr_corner.pop(corner1)
    data.Arr_corner.pop(corner2)
    data.Arr_corner.pop(corner3)


def find_point():
    if len(data.Arr_line) == 6:
        data.Arr_point['A'] = [0,0,0]
        data.Arr_point['B'] = [data.Arr_line['AB'],0,0]
        lab = data.Arr_line['AB']
        lbc = data.Arr_line['BC']
        lac = data.Arr_line['AC']
        las = data.Arr_line['AS']
        lbs = data.Arr_line['BS']
        lcs = data.Arr_line['CS']
        xb = lab
        x = (lbc**2 - lab**2 - lac**2)/(-2*lab)
        y = pt_2(1, 0,x**2 - lac**2)
        xc = x
        yc = y
        data.Arr_point['C'] = [x, y, 0]

        x = (lbs**2 - las**2 - xb**2)/(-2*xb)
        y = (lcs**2 - las**2 - yc**2 - xc**2 + 2*x*xc) / (-2*yc)
        z = pt_2(1, 0, x**2 + y**2 - las**2)
        data.Arr_point['S'] = [x,y,z]


def tinh_line(name = 'S.ABC'):

    siz = len(data.Arr_line)
    while True:
        while True:
            c = True
            for i in data.Arr_corner:
                s = sorted(i)
                line = [s[0]+s[1], s[0]+s[2], s[1]+s[2]]
                check = [i in data.Arr_line for i in line]
                l = [i  for i in line if i in data.Arr_line]
                if check.count(True) ==2:
                    find_line_1_2(i, l[0], l[1])
                    c=False
                    break
            if c:       break
        
        if len(data.Arr_line)<6:
            while True:
                c  =  True
                for i in data.Arr_line:
                    ap = sorted(name)
                    ap.remove('.')
                    s = sorted(i)
                    for j in s:        ap.remove(j)
                    m_p = [sorted(s+[i]) for i in ap]
                    m = [sorted(i) for i in data.Arr_corner]
                    l = [i for i in data.Arr_corner]
                    for j in m_p:
                        n = []
                        for k in range(len(m)):
                            if m[k] == j:        n.append(l[k])
                        if len(n)>1:
                            find_line_2_1(n[0], n[1], i)
                            c = False
                            break
                    if c == False:      break
                if c:   break
        if siz == len(data.Arr_line):
            break
        else:
            siz = len(data.Arr_line)
    find_point()    

        



