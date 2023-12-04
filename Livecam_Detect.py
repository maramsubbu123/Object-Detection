import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

unique_list = []
sent_noti = True
def start_process():
    running_state.set(value=True)
   # label2.destroy()
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

# def insert_into_text(Unique_obj):
#     global unique_list

#     if Unique_obj not in unique_list:
#         unique_list.append(Unique_obj)
#         global t_count
#         t_count+= 1
#         str_counter = f"{t_count}" + ".0"
#         text_area.insert(str_counter, Unique_obj+"\n")

def cam_open(Obj_mainwindow,label1):

    thres = 0.45  # Threshold to detect object
    nms_threshold = 0.2

    cap = cv2.VideoCapture(0)

    classNames = []
    classFile = r"C:\Users\praka\Desktop\Minor Project\labels.names"

    with open(classFile, 'rt') as f1:
        classNames = f1.read().rstrip('\n').split('\n')

    configPath = r"C:\Users\praka\Desktop\Minor Project\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    weightsPath = r"C:\Users\praka\Desktop\Minor Project\frozen_inference_graph.pb"

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    while running_state.get():
        success, img = cap.read()
        classIds, confs, bbox = net.detect(img, confThreshold=thres)
        bbox = list(bbox)
        confs = list(np.array(confs).reshape(1, -1)[0])
        confs = list(map(float, confs))

        indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

        for i in indices:
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x + w, h + y), color=(0, 255, 0), thickness=2)
#             insert_into_text(classNames[classIds[i] - 1])
            cv2.putText(img, classNames[classIds[i] - 1].upper(), (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(Image.fromarray(img))
        label1['image'] = photo
        Obj_mainwindow.update()

Obj_mainwindow = tk.Tk()
Obj_mainwindow.geometry("1336x728")
Obj_mainwindow.resizable(True,True)
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
#init_msg = tk.StringVar(value = "Camera Will Open In Here")
label1 = ttk.Label(cam_frame)
label1.pack(fill='both',expand=True)

label1_img= ImageTk.PhotoImage(file = r"C:\Users\praka\Desktop\Minor Project\gui inside3.jpg")
label1['style'] = 'CustomLabelStyle.TLabel'
style.configure('CustomLabelStyle.TLabel',image = label1_img)

#label2_img= ImageTk.PhotoImage(file = r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\text.png')
#label2 = tk.Label(cam_frame,image = label2_img,bd = 0,bg = '#fefefe',activebackground = '#fefefe')
#label2.place(x = 226,y = 230)

###################################################

b_img= ImageTk.PhotoImage(file = r"C:\Users\praka\Desktop\Minor Project\bgbg (2).png")
label = tk.Label(button_frame,image=b_img)
label.place(x=0,y=0)

name_label = tk.Label(button_frame)
name_label.grid(row=0,column=0,padx=(50,85),pady=(5,5))

# action_img= ImageTk.PhotoImage(file = r"C:\Users\kisha\Downloads\Untitled1.png")
# action_label = tk.Label(button_frame,image = action_img,bd = 0,bg = '#fefefe',foreground ='red',activebackground = '#fefefe')
# action_label.place(x = 20, y=260)

b1_img= ImageTk.PhotoImage(file = r"C:\Users\praka\Desktop\Minor Project\new start.png")
b2_img= ImageTk.PhotoImage(file = r"C:\Users\praka\Desktop\Minor Project\stop1 resised.jpg")
b3_img= ImageTk.PhotoImage(file = r"C:\Users\praka\Desktop\Minor Project\button_quit.png")

start_button = tk.Button(button_frame, image = b1_img , bd=0 , bg='#fefefe',
                        activebackground='#fefefe',
                       command = start_process)
start_button.place(x = 15, y = 99)

stop_button = tk.Button(button_frame, image = b2_img, bd=0 , bg='#fefefe',
                        activebackground='#fefefe',
                       command = stop_process)
stop_button.place(x = 20, y = 177)

#quit_button = tk.Button(button_frame, image = b3_img, bd=0 , bg='#fefefe',
#                        activebackground='#fefefe',
#                        command = quit_process,padx=10)
#quit_button.place(x = 21, y = 255)

# text_area = tk.Text(button_frame,height = 10, width = 15,font = ("Arial",9))
# text_area.place(x = 12, y = 328)
# counter = tk.IntVar(value=1)
# t_count = counter.get()

# str_counter = f"{counter.get()}" + ".0"
# text_area.insert(str_counter, "Objects Detected\n")

Obj_mainwindow.mainloop()


