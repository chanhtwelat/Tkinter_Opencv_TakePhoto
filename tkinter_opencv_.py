import cv2
import numpy as np
from tkinter import *
from PIL import Image,ImageTk
import datetime

def Photolelo():
    images = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).replace(":","")+".jpg"
    images.save(time)
    #cv2.imwrite(images,/home/pi/mu_code/images)

#Set up GUI
root = Tk()
root.geometry("700x650")
root.configure(bg = "black")

#Set up Title
Label(root,text="Camera",font=("times new roman",30,"bold"),bg="black",fg="red").pack()#(fill=X,expand=True,pady=20)

#Set up Camera
f1 = LabelFrame(root,bg="red")
f1.pack()
L1 = Label(f1,bg="red")
L1.pack()

#Capture video frames
cap = cv2.VideoCapture(0)

#Set up Button for take photo
Button(root,text="Take Photo",font=("times new roman",20,"bold"),bg="black",fg="red",command=Photolelo).pack()

while True:
    frame = cap.read()[1]
    image = cv2.rotate(frame,cv2.cv2.ROTATE_180)
    img1 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    root.update()
    
    
cap.release()