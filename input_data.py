import numpy as np
import matplotlib.pyplot as plt
import source_code
import out
from matplotlib.text import TextPath
from mpl_toolkits.mplot3d import Axes3D
import data

# A       0 0 0         : update hoặc add 1 điểm có tọa độ          .
# H       AB            : H là trung điểm của AB                    .
# G       ABC           : G là trọng tâm tam giác ABC               .
# H S     AB            : H là hình chiếu S xuống AB                .
# H S     ABC           : H là hình chiếu của S trên ABC            .
# K AG    BC            : K là giao của AG và BC                    
def input_point(name, properties):
    name = name.upper()
    if ' ' not in properties:
        properties = properties.upper()

    if len(name)==1:
        if ' ' in properties:
            arr = properties.split()
            arr[0] = source_code.change_value(arr[0])
            arr[1] = source_code.change_value(arr[1])
            arr[2] = source_code.change_value(arr[2])
            if 'false' not in arr:
                data.Arr_point[name] = arr
            else:
                out.data_false('không nhận diện được properties')
        elif len(properties)==2:
            if (properties[0] in data.Arr_point and properties[1] in data.Arr_point):
                source_code.between(name, properties[0],properties[1])
            else:
                out.data_false('đường thẳng không tồn tại')
        elif len(properties)==3:
            if (properties[0] in data.Arr_point) and (properties[1] in data.Arr_point) and (properties[2] in data.Arr_point):
                source_code.center(name, properties[0], properties[1], properties[2])
            else:
                out.data_false('mặt phẳng không tồn tại')
        else :
            out.data_false('bạn nhập sai thuộc tính')
    elif len(name)==3 and ' ' in name:
        root = name[2]
        name = name[0]
        if root in data.Arr_point:
            if len(properties)==2:
                if (properties[0] in data.Arr_point) and (properties[1] in data.Arr_point):
                    source_code.mat_line(name, root, properties[0], properties[1])
                else:
                    out.data_false('đường thẳng không tồn tại')
            elif len(properties)==3:
                if properties[0] in data.Arr_point and properties[1] in data.Arr_point and properties[2] in data.Arr_point:
                    source_code.mat_flat(name, root, properties[0], properties[1], properties[2])
                else:
                    out.data_false('mặt phẳng không tồn tại')
            else:
                out.data_false('bạn đã nhập sai thuộc tính')
        else:
            out.data_false(root + ' không nằm trong data')
    elif len(name)==4 and name[1] ==' ':
        line1 = name[2,4]
        line2 = properties
        name = name[0]
        check = False
        for i in (line1+line2):
            if i not in data.Arr_point:
                check = True
                break

        if check:
            out.data_false(line1 + ' hoặc ' + line2 +' không tồn tại')
        else:
            # hàm check 2 đường thẳng giao nhau                                 check_2_line(name1, name2)          name1 = 'AB' name2 = 'SC'
            # hàm tìm giao điểm của 2 đường thẳng                               intersection_2 _line(name1, name2)  -------------------------
            pass
    else:
        out.data_false('bạn đã nhập sai ' + name)

# AB       red          : nối 2 điểm A và B với màu đỏ              .
# AB       AC           : thay đổi điểm B cho AB = AC đơn vị        .
# AB       blue     5   : thay đổi điểm B cho AB = 5 đơn vị         .
def input_line(name, properties = 'red', value = ''):
    if len(name)==2:
        name = ''.join(sorted(name.upper()))
        # cho  độ dài cạnh name bằng cạnh properties
        if len(properties)==2:
            properties = properties.upper()
            if properties[0] in data.Arr_point and properties[1] in data.Arr_point:
                data.Arr_line[name] = data.Arr_line[properties]
                # hàm thay đổi tọa độ 1 điểm thỏa mãn độ dài                    
            else:
                out.data_false(properties+' không nằm trong data')
        # thay thế hoặc nối đoạn thẳng với màu sắc properties
        elif len(properties)>2 or len(properties)==0:
            if properties in data.color:
                data.Arr_color_line[name] = properties
                if value !='':
                    value = source_code.change_value(value)
                    if value != 'false':
                        data.Arr_line[name] = value
                        # hàm thay đổi tọa độ một điểm để thỏa mãn dộ dài       change_line(name, value)
                    else:
                        out.data_false('không nhận dạng được value')
            elif properties == '':
                data.Arr_color_line[name] = 'red'
            else:
                out.data_false('bạn đã nhập sai màu')
    else:
        out.data_false('bạn đã nhập sai')

# ABC              60  : thay đổi góc ABC thành 60 độ
def input_corner(name, value):
    if ' ' not in name and len(name) == 3:
        name = name.upper()
        if name[0] in data.Arr_point and name[1] in data.Arr_point and name[2] not in data.Arr_point:
            value = source_code.change_value(value)
            if value != 'false':
                if source_code.check_corner(name, value):
                    # hàm add góc vào và thay đổi tọa độ                        change_corner(name, value)      // name = 'ABC' value = 60
                    pass
            else:
                out.data_false('không nhận dạng được value')
        else:
            out.data_false(name + 'không tồn tại')
    else:
        out.data_false(name + ' không tồn tại')

def input_delete(name):
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
        name = ''.join(sorted(name.upper()))
        if name in data.Arr_color_line:
            data.Arr_color_line.pop(name)

        if name in data.Arr_line:
            data.Arr_line.pop(name)
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


def input_search(name):
    pass