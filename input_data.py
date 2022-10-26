import source_code
import out
import tinhtoan
import xulydata
from mpl_toolkits.mplot3d import Axes3D
import data
import math

# A       0 0 0         : update hoặc add 1 điểm có tọa độ          .
# H       AB            : H là trung điểm của AB                    .
# G       ABC           : G là trọng tâm tam giác ABC               .
# H       S AB          : H là hình chiếu S xuống AB                .
# H       S ABC         : H là hình chiếu của S trên ABC            .
# K       AG BC         : K là giao của AG và BC                    . 
def input_point(name, properties):
    name = name.upper()
    if len(name)==1:
        arr = properties.split()
        if len(arr)==3:
            arr[0] = source_code.change_value(arr[0])
            arr[1] = source_code.change_value(arr[1])
            arr[2] = source_code.change_value(arr[2])
            if 'false' not in arr:
                data.Arr_point[name] = arr
            else: 
                out.data_false('không nhận diện được properties')
        elif len(arr)==1:
            arr = [i.upper() for i in arr]
            if arr[0] in data.Arr_point:
                data.Arr_point[name] = data.Arr_point[arr[0]]
            elif len(arr[0])==2:
                if all([i in data.Arr_point for i in''.join(arr)]):
                    source_code.between(name, arr[0][0],arr[0][1])
                else:
                    out.data_false('đường thẳng'+arr[0] + ' không tồn tại')
            elif len(arr[0])==3:
                if all([i in data.Arr_point for i in''.join(arr)]):
                    source_code.center(name, arr[0][0], arr[0][1], arr[0][2])
                else:
                    out.data_false('mặt phẳng'+arr[0]+' không tồn tại')
            else:
                out.data_false('không nhận dạng được' + arr[0])
        elif len(arr)==2:
            arr = [i.upper() for i in arr]
            if len(arr[0])==1 and arr[0] in data.Arr_point:
                if len(arr[1])==2 and all([i in data.Arr_point for i in arr[1]]):
                    source_code.mat_line(name, arr[0], arr[1][0], arr[1][1])
                elif len(arr[1])==3:
                    source_code.mat_flat(name, arr[0], arr[1][0], arr[1][1], arr[1][2])
                else:
                    out.data_false(arr[1]+'không tồn tại')
            elif len(arr[0])==2 and all([i in data.Arr_point for i in arr[0]+arr[1]]) and len(arr[1])==2:
                if source_code.check_2_line(arr[0], arr[1]):
                    source_code.intersection_2_line(name, arr[0], arr[1])
                else:
                    out.data_false('hai đường thẳng không cắt nhau')
            else:
                out.data_false('bạn nhập sai thuộc tính')
        else :
            out.data_false('bạn nhập sai thuộc tính')
    else:
        out.data_false('bạn đã nhập sai ' + name)

# AB       red          : nối 2 điểm A và B với màu đỏ              .
# AB       AC           : thay đổi điểm B cho AB = AC đơn vị      
# AB       1/2 AC       : thay đổi điểm B cho AB = AC/2 đơn vị   
# AB       blue     5   : thay đổi điểm B cho AB = 5 đơn vị         
def input_line(name = '', properties = '', value = ''):
    name = name.upper()
    if len(name)==2 and all([i in data.Arr_point for i in name]):
        arr = properties.split()
        if len(arr) == 1 or len(arr)==0:
            if len(properties)==2 and all([i in data.Arr_point for i in properties.upper()]):
                source_code.change_line(name, source_code.get_line(properties.upper()))            
            # thay thế hoặc nối đoạn thẳng với màu sắc properties
            elif len(properties)>2 or properties=='':
                if properties.lower() in data.color:
                    data.Arr_color_line[name] = properties
                elif properties == '':
                    data.Arr_color_line[name] = 'red'
                else:
                    out.data_false('bạn đã nhập sai màu')
            else:
                out.data_false('không nhận dạng được' + properties)
        elif len(arr) == 2:
            tl = source_code.change_value(arr[0])
            if tl != 'false':
                properties = arr[1].upper()
                if len(properties)==2 and all([i in data.Arr_point for i in properties.upper()]):
                    source_code.change_line(name, source_code.get_line(properties.upper()) * tl)   
                else:
                    out.data_false(properties+'không tồn tại')
            else:
                out.data_false(arr[0]+'không phải biểu thức')
        else:
            out.data_false('không nhận dạng được' + properties)        
        if value !='':
            value = source_code.change_value(value)
            if value != 'false':
                source_code.change_line(name, value)
            else:
                out.data_false('không nhận dạng được value')
        
    else:
        out.data_false('bạn đã nhập sai')

# thiết lập thêm dữ liệu vào data
# ABC = 120             goc ABC bằng 120 độ
# AB = 12               AB dài 12 đơn vị
# ABC ASC CAB = 60      các góc lần lượt bằng 120 độ
def in_data(properties = ''):
    k = properties.upper()
    if k[0] == 'S' and k[1]=='.':
        st = properties.split()
        st[0] = st[0].upper()
        name = st[0]
        st.remove(name)
        vl = [source_code.change_value(i) for i in st]
        if all([i!='false' for i in vl]) and len(vl)>0:
            if sorted(name) == sorted('S.ABC') and len(vl)==1:
                v = vl[0]
                data.Arr_line = {'AB':v, 'BC':v, 'AS':v, 'AC':v, 'BS':v, 'CS':v}
                xulydata.tinh_line('S.ABC')
            elif sorted(name) == sorted('S.ABC') and len(vl)==2:
                v1 = vl[0]
                v2 = vl[1]
                data.Arr_line = {'AB':v2, 'BC':v2, 'AC':v2, 'AS':v1, 'BS':v1, 'CS':v1}
                xulydata.tinh_line('S.ABC')
            else:
                out.data_false('chương trình chỉ hỗ trợ vẽ nhanh tứ diện đều S.ABC')
        else:
            out.data_false('không nhận diện được giá trị')
    elif properties.upper() == 'RESET':
        data.Arr_point = {'S':[1,math.sqrt(3)/3,math.sqrt(3)], 'A':[0,0,0], 'B':[2,0,0], 'C':[1,math.sqrt(3),0]}
        data.Arr_line = {'AB':2, 'BC':2, 'AS':2, 'AC':2, 'BS':2, 'CS':2}
        data.Arr_color_line = {'AB':'red', 'AC':'red', 'AS':'red', 'BC':'red', 'BS':'red', 'CS':'red'}
    else:
        for i in properties.split('||'):
            if ' = ' not in properties:
                continue
            properties = i
            arr = properties.split()
            value = source_code.change_value(arr[-1])
            if value != 'false':
                arr.pop()
                if arr[-1] == '=':  arr.pop()
                arr = [i.upper() for i in arr]
                st = 'SABC'
                if 'D' in data.Arr_point: st = 'SABCD'
                if all([len(i)==2 for i in arr]):
                    if all([i in st for i in ''.join(arr)]):
                        arr = [''.join(sorted(i)) for i in arr]
                        for i in arr:
                            data.Arr_line[i] = value
                    else:
                        out.data_false('chương trình chỉ hỗ trợ cho S.ABC và S.ABCD')
                elif all([len(i)==3 for i in arr]):
                    if all([i in st for i in ''.join(arr)]):
                        if all([len(set(i))==3 for i in arr]):
                            arr = [min(i, i[::-1]) for i in arr]
                            for i in arr:
                                data.Arr_corner[i] = value
                        else:
                            out.data_false('góc không tồn tại')
                    else:
                        out.data_false('chương trình chỉ hỗ trợ cho S.ABC và S.ABCD')
                else:
                    out.data_false(*arr + 'không cùng thuộc tính')
            else:
                out.data_false('không nhận dạng được giá trị của' + arr[-1])

def out_data():
    try:
        xulydata.tinh_line('ABC')
    except:
        out.data_false('dữ liệu không đúng')

def input_delete(name = ''):
    if name.upper() == 'ALL':
        data.Arr_line.clear()
        data.Arr_corner.clear()
    else:
        # xóa điểm
        if len(name)==1:
            name = name.upper()
            if name in data.Arr_point:
                data.Arr_point.pop(name)
                arr = []
                for i in data.Arr_color_line:
                    if name in i:
                        arr.append(i)
                for i in arr:
                    data.Arr_color_line.pop(i)
                arr = []
                for i in data.Arr_line:
                    if name in i:
                        arr.append(i)
                for i in arr:
                    data.Arr_line.pop(i)
            else:
                out.data_false('điểm không tồn tại trong data')
        # xóa cạnh
        elif len(name)==2:
            name = ''.join(name.upper())
            if name in data.Arr_line:
                data.Arr_line.pop(name)
            elif name in data.Arr_color_line:
                data.Arr_color_line.pop(name)
            else:
                out.data_false('cạnh không tồn tại trong data')
        # xóa góc
        elif len(name)==3:
            name = name.upper()
            check = True
            name =  min(name, name[::-1])
            for i in sorted(name):
                if i not in data.Arr_point:
                    out.data_false('góc không tồn tại')
                    check = False
                    break
            if check:
                if name in data.Arr_corner:
                    data.Arr_corner.pop(name)
                else:
                    out.data_false('góc không nằm trong data')
        else:
            out.data_false('dữ liệu nhập vào bị sai')


# thiết lập tra cứu 
# S.ABC                   : tính thể tích hình chóp tam giác sabc           volume3(name)       // name = 'S.ABC'
# (ABC)                   : tính diện tích tam giác ABC                     area3(name)         // name = 'ABC'
# ABC                     : hàm trả về góc ABC (độ)                         get_corner(name)    // name = 'ABC'
# AB                      : hàm trả về độ dài cạnh AB                       get_line(name)      // name = 'AB'
def input_search(name):
    name = name.upper()
    if name[1] == '.':
        st = sorted(name)
        st.remove('.')
        if all([i in data.Arr_point for i in st]):
            mess = tinhtoan.thetichtudien(''.join(st))
            out.sdata('thể tích của tứ giác ' + name +' = ' + str(mess))
        else:
            out.data_false('tứ giác ' + name + ' không tồn tại')
    elif name[0] == '(' and name[4] ==')':
        name = sorted(name)
        name.remove('(')
        name.remove(')')
        name = ''.join(name)
        if all([i in data.Arr_point for i in name]):
            mess = tinhtoan.dientichtamgiac(name)
            out.sdata('diện tích tam giác ' +  name +' = ' + str(mess))
        else:
            out.data_false('tam giác '+name+' không tồn tại')
    elif len(name) == 3 and all([i in data.Arr_point for i in name]):
        mess = tinhtoan.goc(name)
        out.sdata(name +' = ' + str(mess))
    elif len(name) == 2 and all([i in data.Arr_point for i in name]):
        mess = tinhtoan.tinhcanh(name)
        out.sdata(name +' = ' + str(mess))
    else:
        out.data_false('bạn đã nhập sai')





