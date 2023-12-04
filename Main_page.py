import tkinter as tk 
from PIL import Image,ImageTk
import subprocess

def Live():
    subprocess.call(['python', r'Livecam_Detect.py'])

def Video():
    subprocess.call(['python', r'Video_Detect.py'])
def Image():
    subprocess.call(['python',r'Image_Detect.py'])

Main_frame = tk.Tk()
Main_frame.geometry("800x585")
Main_frame.resizable(False,False)
Main_frame.title("OBJECT DETECTION")
Main_frame.configure(background = 'black') 

Main_frame.grid_rowconfigure(0, weight = 1) 
Main_frame.grid_columnconfigure(0, weight = 1) 

Bg_image = Image.open(r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\bg1.png')
Bg_image_p = ImageTk.PhotoImage(Bg_image)
Bg_label = tk.Label(Main_frame,image = Bg_image_p) 
Bg_label.place(x=0,y=0)


sub1img = Image.open(r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\icon1.jfif')
sub1img_p = ImageTk.PhotoImage(sub1img)

sub1button = tk.Button(Main_frame,command = Live,image = sub1img_p , bd=0 , bg='white',
                                                                     activebackground='white')
sub1button.place(x = 568, y = 210)
sub1button_label = tk.Label(Main_frame,text = "Live Cam",fg="white",bg="#5B49CF",font=('Ar cena', 9))
sub1button_label.place(x=598, y=364)


sub2img = Image.open(r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\icon2.jfif')
sub2img_p = ImageTk.PhotoImage(sub2img)

sub2button = tk.Button(Main_frame,command = Video, image = sub2img_p , bd=0 , bg='white',
                                                                     activebackground='white')
sub2button.place(x = 568, y = 406)
sub2button_label = tk.Label(Main_frame,text = "Video",fg="white",bg="#4F22B3",font=('Ar cena', 9))
sub2button_label.place(x=593, y=559)

sub3img = Image.open(r'C:\Users\kisha\OneDrive\Desktop\MLA PROJECT\icon3.jfif')
sub3img_p = ImageTk.PhotoImage(sub3img)

sub3button = tk.Button(Main_frame,command = Image, image = sub2img_p , bd=0 , bg='white',
                                                                     activebackground='white')
sub3button.place(x = 568, y = 615)
sub3button_label = tk.Label(Main_frame,text = "Image",fg="white",bg="#4F22B3",font=('Ar cena', 9))
sub3button_label.place(x=593, y=730)

Main_frame.mainloop()