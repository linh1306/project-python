from importlib.metadata import entry_points
import input_data
import out
from tkinter import *


BACKGROUND_COL = '#212630'
FOREGROUND_COL = '#D9D9D9'
BUTTON_COL = '#6047DE'
BUTTON_COL_RED = '#DE2929'
TITLE_FONT = 'Poppins Black'
BODY_FONT = 'Poppins Regular'


Window = Tk()
Window.title('Block 3D')
Window.geometry('1205x500')
Window.configure(bg=BACKGROUND_COL)

# điểm
# D       B             : thêm điểm D trùng với điểm B
# A       0 0 0         : update hoặc add 1 điểm có tọa độ          .
# H       AB            : H là trung điểm của AB                    .
# G       ABC           : G là trọng tâm tam giác ABC               .
# H       S AB          : H là hình chiếu S xuống AB                .
# H       S ABC         : H là hình chiếu của S trên ABC            .
# K       AG BC         : K là giao của AG và BC                    . 
Point = Label(Window, width=10, text="Point:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=0, column=0)
name_point = StringVar(Window)
input_name_point = Entry(Window, width=20, textvariable=name_point, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=0, column=1)

Properties_point = Label(Window, width=15, text="Properties:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=0, column=2)
properties_point = StringVar(Window)
input_properties_point = Entry(Window, width=51, textvariable=properties_point, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=0, column=3, columnspan=3)

Button_point = Button(Window, text="Add point",command=lambda: input_data.input_point(name_point.get(), properties_point.get()), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL,bd=2, width=10).grid(row=0,column=6)


# thiết lập các cạnh
# AB       red          : nối 2 điểm A và B với màu đỏ              .
# AB       AC           : thay đổi điểm B cho AB = AC đơn vị      
# AB       1/2 AC       : thay đổi điểm B cho AB = AC/2 đơn vị   
# AB       blue     5   : thay đổi điểm B cho AB = 5 đơn vị    
Line = Label(Window, text="Line:", width=10, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=1, column=0)
name_line = StringVar(Window)
input_name_line = Entry(Window, width=20, textvariable=name_line, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=1, column=1)

Properties_line = Label(Window,width=15, text="Properties:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=1, column=2)
properties_line = StringVar(Window)
input_properties_line = Entry(Window,width=20, textvariable=properties_line, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=1, column=3)

Value_line = Label(Window, width=10, text="Value:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=1, column=4)
value_line = StringVar(Window)
input_value_line = Entry(Window, width=20, textvariable=value_line, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=1, column=5)

Button_line = Button(Window, text="Add line",command=lambda: input_data.input_line(name_line.get(), properties_line.get(), value_line.get()), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=1,column=6)


# thêm dữ liệu vào data
# ABC = 120             goc ABC bằng 120 độ
# AB = 12               AB dài 12 đơn vị
# ABC ASC CAB = 60      các góc lần lượt bằng 120 độ
Input = Label(Window, text="Input:", width=10, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=2, column=0)
name_input = StringVar(Window)
input_name_Input = Entry(Window, width=67, textvariable=name_input, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=2, column=1, columnspan=4)
Button_input = Button(Window, text="Add",command=lambda: input_data.in_data(name_input.get()), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=2,column=5)
Button_out = Button(Window, text="Enter",command=lambda: input_data.out_data(), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=2,column=6)
 
# xóa
# A                   : xóa điểm A và các cạnh nối với điểm A
# BC                  : xóa đường nối BC
# ABC                 : xóa góc ABC ra khỏi bộ nhớ
Subject = Label(Window, text="Delete:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=3, column=0)
name_subject = StringVar(Window)
input_name_subject = Entry(Window, width=87, textvariable=name_subject, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=3, column=1, columnspan=5)

Button_Subject = Button(Window, text="Apply",command=lambda: input_data.input_delete(name_subject.get()), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=3,column=6)

# tra cứu 
# S.ABC                   : tính thể tích hình chóp tam giác sabc           volume3(name)       // name = 'S.ABC'
# (ABC)                   : tính diện tích tam giác ABC                     area3(name)         // name = 'ABC'
# ABC                     : hàm trả về góc ABC (độ)                         get_corner(name)    // name = 'ABC'
# AB                      : hàm trả về độ dài cạnh AB                       get_line(name)      // name = 'AB'
Search = Label(Window, text="Find:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=4, column=0)
name_search = StringVar(Window)
input_name_search = Entry(Window, width=87, textvariable=name_search, font=(BODY_FONT, 15), bg=BACKGROUND_COL,fg=FOREGROUND_COL).grid(row=4, column=1, columnspan=5)

Button_search = Button(Window, text="Search",command=lambda: input_data.input_search(name_search.get()), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=4,column=6)


# xuất data
Button_output_data = Button(Window, text="Output data",command=lambda: out.output_data(), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=5,column=3)

#xuất đồ họa
Button_add = Button(Window, text="Add",command=lambda: out.output(), font=(BODY_FONT, 15),bg=BUTTON_COL, fg=FOREGROUND_COL, bd=2, width=10).grid(row=6,column=3)


Window.mainloop()
