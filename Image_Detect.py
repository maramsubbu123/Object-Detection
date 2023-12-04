import cv2
import matplotlib.pyplot as plt



import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

unique_list = []
sent_noti = True
def start_process():
    running_state.set(value=True)
    label2.destroy()
    cam_open(Obj_mainwindow, label1)

def stop_process():
    running_state.set(False)
    global unique_list
    unique_list = []
    text_area.delete("1.0","end")
    str_counter = f"{counter.get()}" + ".0"
    text_area.insert(str_counter, "Objects Detected\n")

def quit_process():
    if running_state.get():
        stop_process()
    Obj_mainwindow.destroy()

def insert_into_text(Unique_obj):
    global unique_list

    if Unique_obj not in unique_list:
        unique_list.append(Unique_obj)
        global t_count
        t_count+= 1
        str_counter = f"{t_count}" + ".0"
        text_area.insert(str_counter, Unique_obj+"\n")

def cam_open(Obj_mainwindow,label1):
    config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    frozen_model = 'frozen_inference_graph.pb'
    model = cv2.dnn_DetectionModel(frozen_model,config_file)
    classlabels = []
    file_name = 'labels.names'
    with open(file_name,'rt') as fpt:
        classlabels = fpt.read().rstrip('\n').split('\n')
        model.setInputSize(320, 320)
        model.setInputScale(1.0 / 127.5)  # 1/(255/2)
        model.setInputMean((127.5, 127.5, 127.5))  # RGB
        model.setInputSwapRB(True)
        img = cv2.imread('2.jpg')
        plt.imshow(img)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
        print(ClassIndex)
        font_scale = 6
        font = cv2.FONT_HERSHEY_PLAIN
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            cv2.rectangle(img, boxes, (0,255,0), 3)
            cv2.putText(img, classlabels[ClassInd-1], (boxes[0]+10,boxes[1]+40), font, fontScale=font_scale, color=(0,0,255), thickness=3)
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


    
Obj_mainwindow = tk.Tk()
Obj_mainwindow.geometry("1366x768")
Obj_mainwindow.resizable(False,False)
Obj_mainwindow.title("OBJECT DETECTOR")

style = ttk.Style(Obj_mainwindow)

cam_frame = tk.Frame(Obj_mainwindow)
cam_frame.pack(side = 'left',fill = 'both',expand=True)
cam_frame['borderwidth'] = 1
cam_frame['relief'] = 'solid'

ttk.Separator(Obj_mainwindow,orient='vertical').pack(side = 'left' , fill='y',padx =(0,5))

button_frame = ttk.Frame(Obj_mainwindow)
button_frame.pack(side = 'left',fill = 'both')
button_frame['borderwidth'] = 1
button_frame['relief'] = 'solid'
button_frame.grid_columnconfigure(0,weight=1)
button_frame.grid_rowconfigure(0,weight=1)

running_state = tk.BooleanVar()
init_msg = tk.StringVar(value = "Camera Will Open In Here")
#label1 = ttk.Label(cam_frame)
#label1.pack(fill='both',expand=True)

#label1_img= ImageTk.PhotoImage(file = r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\1.jpg')
#label1['style'] = 'CustomLabelStyle.TLabel'
#style.configure('CustomLabelStyle.TLabel',image = label1_img)

#label2_img= ImageTk.PhotoImage(file = r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\text.png')
#label2 = tk.Label(cam_frame,image = label2_img,bd = 0,bg = '#fefefe',activebackground = '#fefefe')
#label2.place(x = 226,y = 230)

###################################################

b_img= ImageTk.PhotoImage(file = r"C:\Users\kisha\OneDrive\Desktop\MinorProject\background.jpg")
label = tk.Label(button_frame,image=b_img)
label.place(x=0,y=0)

name_label = tk.Label(button_frame)
name_label.grid(row=0,column=0,padx=(50,85),pady=(5,5))

action_img= ImageTk.PhotoImage(file = r"C:\Users\kisha\OneDrive\Desktop\MinorProject\actions.png")
action_label = tk.Label(button_frame,image = action_img,bd = 0,bg = '#fefefe',activebackground = '#fefefe')
action_label.place(x = 34, y= 50)

b1_img= ImageTk.PhotoImage(file = r"C:\Users\kisha\OneDrive\Desktop\MinorProject\button_detect.ico")
b2_img= ImageTk.PhotoImage(file = r"C:\Users\kisha\OneDrive\Desktop\MinorProject\button_stop.ico")
b3_img= ImageTk.PhotoImage(file = r"C:\Users\kisha\OneDrive\Desktop\MinorProject\button_quit.png")

start_button = tk.Button(button_frame, image = b1_img , bd=0 , bg='#fefefe',
                         activebackground='#fefefe',
                         command = start_process)
start_button.place(x = 21, y = 98)

stop_button = tk.Button(button_frame, image = b2_img, bd=0 , bg='#fefefe',
                        activebackground='#fefefe',
                        command = stop_process)
stop_button.place(x = 21, y = 177)

quit_button = tk.Button(button_frame, image = b3_img, bd=0 , bg='#fefefe',
                        activebackground='#fefefe',
                        command = quit_process,padx=10)
quit_button.place(x = 21, y = 255)

text_area = tk.Text(button_frame,height = 10, width = 15,font = ("Arial",9))
text_area.place(x = 12, y = 328)
counter = tk.IntVar(value=1)
t_count = counter.get()

str_counter = f"{counter.get()}" + ".0"
text_area.insert(str_counter, "Objects Detected\n")

Obj_mainwindow.mainloop()


