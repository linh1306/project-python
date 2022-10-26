import numpy as np
import matplotlib.pyplot as plt
import data
from tkinter import *
from matplotlib.text import TextPath
from mpl_toolkits.mplot3d import Axes3D

BACKGROUND_COL = '#212630'
FOREGROUND_COL = '#D9D9D9'
BUTTON_COL = '#6047DE'
BUTTON_COL_RED = '#DE2929'
TITLE_FONT = 'Poppins Black'
BODY_FONT = 'Poppins Regular'

def output_data():
    op_data = Tk()
    op_data.title('Data')
    op_data.geometry('350x500')
    op_data.configure(bg=BACKGROUND_COL)


    textLabel = Label(op_data, text='Point', bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=0)
    textLabel = Label(op_data, text='       ', bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=1)
    textLabel = Label(op_data, text='Line', bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=2)
    textLabel = Label(op_data, text='       ', bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=3)
    textLabel = Label(op_data, text='Corner', bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=4)
    k = 1
    for i in data.Arr_point:
        textLabel = Label(op_data, text=i, bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=k,column=0)
        k+=1

    k = 1
    for i in data.Arr_line:
        textLabel = Label(op_data, text=i +' = '+ str(data.Arr_line[i]), bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=k,column=2)
        k+=1

    k = 1
    for i in data.Arr_corner:
        textLabel = Label(op_data, text=i +' = '+ str(data.Arr_corner[i]), bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=k,column=4)
        k+=1
    op_data.mainloop()

def output():
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    for i in data.Arr_point:
        ax.scatter(data.Arr_point[i][0], data.Arr_point[i][1], data.Arr_point[i][2])
        ax.text(data.Arr_point[i][0], data.Arr_point[i][1], data.Arr_point[i][2], i, color='black')

    def line(P1, P2, color):
        x = np.array([P1[0],P2[0]])
        y = np.array([P1[1],P2[1]])
        z = np.array([P1[2],P2[2]])
        ax.plot(x, y, z, c=color)

    for i in data.Arr_color_line:
        line(data.Arr_point[i[0]],data.Arr_point[i[1]], data.Arr_color_line[i])

    ax.set_aspect('equal')
    plt.show()
 
def data_false(message):
    dt_false = Tk()
    dt_false.title('Error!')
    dt_false.geometry('600x160')
    dt_false.configure(bg=BACKGROUND_COL)

    dt_false.grid_columnconfigure(0, weight=1)
    dt_false.grid_rowconfigure(0, weight=1)
    dt_false.grid_rowconfigure(1, weight=1)

    textLabel = Label(dt_false, text=message, bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=0)
    okButton = Button(dt_false, text="OK", command=dt_false.destroy, bg=BUTTON_COL, fg=FOREGROUND_COL,font=(BODY_FONT, 15)).grid(row=1, column=0)

    dt_false.mainloop()

def sdata(message):
    dt_false = Tk()
    dt_false.title('Output')
    dt_false.geometry('600x160')
    dt_false.configure(bg=BACKGROUND_COL)

    dt_false.grid_columnconfigure(0, weight=1)
    dt_false.grid_rowconfigure(0, weight=1)
    dt_false.grid_rowconfigure(1, weight=1)

    textLabel = Label(dt_false, text=message, bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 15)).grid(row=0,column=0)
    okButton = Button(dt_false, text="OK", command=dt_false.destroy, bg=BUTTON_COL, fg=FOREGROUND_COL,font=(BODY_FONT, 15)).grid(row=1, column=0)

    dt_false.mainloop()