import data
import math

def change_value(value):
    try:
        value = value.replace('sqrt', 'math.sqrt')
        value = value.replace('cos', 'math.cos')
        value = value.replace('sin', 'math.sin')
        value = value.replace('tan', 'math.tan')
        value = value.replace('pi', 'math.pi')
        return eval(value)
    except:
        return 'false'

def center(name , p1, p2, p3):
    x = (data.Arr_point[p1][0] + data.Arr_point[p2][0] + data.Arr_point[p3][0])/3
    y = (data.Arr_point[p1][1] + data.Arr_point[p2][1] + data.Arr_point[p3][1])/3
    z = (data.Arr_point[p1][2] + data.Arr_point[p2][2] + data.Arr_point[p3][2])/3
    data.Arr_point[name] = [x, y, z]

def between(name, point1, point2):
    x = (data.Arr_point[point1][0] + data.Arr_point[point2][0])/2
    y = (data.Arr_point[point1][1] + data.Arr_point[point2][1])/2
    z = (data.Arr_point[point1][2] + data.Arr_point[point2][2])/2
    data.Arr_point[name] = [x, y, z]

# hình chiếu vuông góc xuống cạnh
def mat_line(name, root, p1, p2):
    xr, yr, zr = data.Arr_point[root]
    x1, y1, z1 = data.Arr_point[p1]
    x2, y2, z2 = data.Arr_point[p2]
    a, b, c = [x2-x1, y2-y1, z2-z1]
    t = -1*((x1-xr)*a+(y1-yr)*b+(z1-zr)*c)/(a*a+b*b+c*c)
    data.Arr_point[name] = [x1+a*t, y1+b*t, z1+c*t]

# hình chiếu vuông góc xuống mặt phẳng
def mat_flat(name, root, p1, p2, p3):
    xr, yr, zr = data.Arr_point[root]
    x1, y1, z1 = data.Arr_point[p1]
    x2, y2, z2 = data.Arr_point[p2]
    x3, y3, z3 = data.Arr_point[p3]

    a1,b1,c1 = [x2-x1, y2-y1, z2-z1]
    a2,b2,c2 = [x3-x1, y3-y1, z3-z1]

    a, b, c = [b1*c2-b2*c1, a2*c1-a1*c2, a1*b2-a2*b1]
    t  = -1 * ((xr-x1)*a + (yr-y1)*b + (zr-z1)*c)/(a*a + b*b + c*c)
    data.Arr_point[name] = [xr+a*t, yr+b*t, zr+c*t]

def check_corner(name, value):
    name1 = name[1:3] + name[0]
    name2 = name[2] + name[:2]
    name1 = min(name1, name1[::-1])
    name2 = min(name2, name2[::-1])
    ar = [value]
    if name1 in data.Arr_corner:    ar.append(data.Arr_corner[name1])
    if name2 in data.Arr_corner:    ar.append(data.Arr_corner[name2])
    if len(ar)==1 and ar[0]<180:
        return True
    elif len(ar)==2 and ar[0] + ar[1] < 180:
        return True
    elif len(ar)==3 and ar[0]+ar[1]+ar[2]==180:
        return True
    return False


def get_line(name):
    point1 = name[0]
    point2 = name[1]
    ar = [data.Arr_point[point1][0]+data.Arr_point[point2][0], data.Arr_point[point1][1]+data.Arr_point[point2][1], data.Arr_point[point1][2]+data.Arr_point[point2][2]]
    return math.sqrt(ar[0]*ar[0]+ar[1]*ar[1] + ar[2]*ar[2])

# kiểm tra 2 đường thẳng có cắt nhau không
def check_2_line(name1, name2):
    cp1 = [data.Arr_point[name1[0]][0] - data.Arr_point[name1[1]][0], data.Arr_point[name1[0]][1] - data.Arr_point[name1[1]][1], data.Arr_point[name1[0]][2] - data.Arr_point[name1[1]][2]]
    cp2 = [data.Arr_point[name2[0]][0] - data.Arr_point[name2[1]][0], data.Arr_point[name2[0]][1] - data.Arr_point[name2[1]][1], data.Arr_point[name2[0]][2] - data.Arr_point[name2[1]][2]]
    p1 = data.Arr_point[name1[0]]
    p2 = data.Arr_point[name2[0]]
    vt = [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    tch = [cp1[1]*cp2[2]-cp2[1]*cp1[2], cp1[0]*cp2[2]-cp2[0]*cp1[2], cp1[0]*cp2[1]-cp2[0]*cp1[1]]
    if tch[0]*vt[0] + tch[1]*vt[1] + tch[2]*vt[2] == 0:
        return True
    else:
        return False

# tìm giao điểm của 2 đường thẳng
def intersection_2_line(name, name1, name2):
    cp1 = [data.Arr_point[name1[0]][0] - data.Arr_point[name1[1]][0], data.Arr_point[name1[0]][1] - data.Arr_point[name1[1]][1], data.Arr_point[name1[0]][2] - data.Arr_point[name1[1]][2]]
    cp2 = [data.Arr_point[name2[0]][0] - data.Arr_point[name2[1]][0], data.Arr_point[name2[0]][1] - data.Arr_point[name2[1]][1], data.Arr_point[name2[0]][2] - data.Arr_point[name2[1]][2]]
    p1 = data.Arr_point[name1[0]]
    p2 = data.Arr_point[name2[0]]
    a1, b1, c1, d1 = [ cp1[0], -cp2[0], 3, p2[0]-p1[0]+3]
    a2, b2, c2, d2 = [ cp1[1], -cp2[1], 2, p2[1]-p1[1]+2]
    a3, b3, c3, d3 = [ cp1[2], -cp2[2], 1, p2[2]-p1[2]+1]
    d = a1*b2*c3 + b1*c2*a3 + a2*b3*c1 - c1*b2*a3 - b1*a2*c3 - a1*b3*c2
    dx = d1*b2*c3 + b1*c2*d3 + d2*b3*c1 - c1*b2*d3 - b1*d2*c3 - c2*b3*d1
    t = dx/d
    data.Arr_point[name] = [ p1[0] + cp1[0]*t, p1[1] + cp1[1]*t, p1[2] + cp1[2]*t]
 
def change_line(name = '', value = 0):
    cp = [data.Arr_point[name[1]][0]-data.Arr_point[name[0]][0], data.Arr_point[name[1]][1]-data.Arr_point[name[0]][1], data.Arr_point[name[1]][2]-data.Arr_point[name[0]][2]]
    a = data.Arr_point[name[0]]
    tl = value / get_line(name)
    cp = [cp[0]*tl, cp[1]*tl, cp[2]*tl]
    data.Arr_point[name[1]] = [a[0]+cp[0], a[1]+cp[1], a[2]+cp[2]]

