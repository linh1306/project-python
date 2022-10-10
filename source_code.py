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
