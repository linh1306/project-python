import math
import data


def tinhcanh(name):#ab
    point1=name[0]
    point2=name[1]
    ar=[data.Arr_point[point1][0]-data.Arr_point[point2][0],data.Arr_point[point1][1]-data.Arr_point[point2][1],data.Arr_point[point1][2]-data.Arr_point[point2][2]]
    return math.sqrt(ar[0]**2+ar[1]**2+ar[2]**2)

def goc(name):# abc
    n1 = min(name[0]+name[2], name[2]+name[0])
    n2 = min(name[2]+name[1], name[1]+name[2])
    n3 = min(name[0]+name[1], name[1]+name[0])
    if n1  not in data.Arr_line:       a=tinhcanh(n1)
    else:                                           a=data.Arr_line[n1]
    if n2  not in data.Arr_line:       b=tinhcanh(n2)
    else:                                           b=data.Arr_line[n2]
    if n3  not in data.Arr_line:       c=tinhcanh(n3)
    else:                                           c=data.Arr_line[n3]
    tu=b*b+c*c-a*a
    mau=2*b*c
    return math.acos(tu/mau)*180/math.pi

def dientichtamgiac(name):#abc
    n1 = min(name[0]+name[2], name[2]+name[0])
    n2 = min(name[2]+name[1], name[1]+name[2])
    n3 = min(name[0]+name[1], name[1]+name[0])
    if n1  not in data.Arr_line:       a=tinhcanh(n1)
    else:                                           a=data.Arr_line[n1]
    if n2  not in data.Arr_line:       b=tinhcanh(n2)
    else:                                           b=data.Arr_line[n2]
    if n3  not in data.Arr_line:       c=tinhcanh(n3)
    else:                                           c=data.Arr_line[n3]
    cv=a+b+c
    p=cv/2
    tmp=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return tmp


def thetichtudien(name): #abcd
    if name[1]+name[2]  not in data.Arr_line:       a=tinhcanh(name[1]+name[2])
    else:                                           a=data.Arr_line[name[1]+name[2]]
    if name[0]+name[2]  not in data.Arr_line:       b=tinhcanh(name[0]+name[2])
    else:                                           b=data.Arr_line[name[0]+name[2]]
    if name[0]+name[1]  not in data.Arr_line:       c=tinhcanh(name[0]+name[1])
    else:                                           c=data.Arr_line[name[0]+name[1]]
    if name[0]+name[3]  not in data.Arr_line:       d=tinhcanh(name[0]+name[3])
    else:                                           d=data.Arr_line[name[0]+name[3]]
    if name[1]+name[3]  not in data.Arr_line:       e=tinhcanh(name[1]+name[3])
    else:                                           e=data.Arr_line[name[1]+name[3]]
    if name[2]+name[3]  not in data.Arr_line:       f=tinhcanh(name[2]+name[3])
    else:                                           f=data.Arr_line[name[2]+name[3]]
    M=a*a*d*d*(b*b+e*e+c*c+f*f-a*a-d*d)
    N=b*b*e*e*(a*a+d*d+c*c+f*f-b*b-e*e)
    P=c*c*f*f*(a*a+d*d+b*b+e*e-c*c-f*f)
    Q=(a*b*c)**2+(a*e*f)**2+(b*d*f)**2+(c*d*e)**2
    return 1/12*math.sqrt(M+N+P-Q)