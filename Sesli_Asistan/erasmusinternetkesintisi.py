
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os
import time
from datetime import datetime
import webbrowser
from distutils.debug import DEBUG
import tkinter
from turtle import left
import pyautogui
import time
import random
from tkinter import *

from pygame import Color, font


def gonder():
    pass


#---------------------------------------INTERFACE-----------------------------------------
masterr=tkinter.Tk()
canvass=tkinter.Canvas(masterr,width=600,height=600)
canvass.pack()


frame_mid=tkinter.Frame(masterr,bg='dark grey')
frame_options=tkinter.Frame(masterr,bg='dark grey')
frame_options.place(relx=0.12,rely=0.1,relheight=0.10,relwidth=0.7)
frame_mid.place(relx=0.12,rely=0.23,relheight=0.6,relwidth=0.7)
Label(frame_mid,text="Start Recording",font="Arial 14 bold",bg="dark grey").pack(padx=10,pady=10,side=TOP)
Label(frame_options,text="Language :",font="Arial 12 bold",bg="dark grey").pack(padx=3,pady=5,side=LEFT)
var=IntVar()
R1=Radiobutton(frame_options,text="English",variable=var,value=1,bg='dark grey',font='Arial 12 bold')
R2=Radiobutton(frame_options,text="Spanish",variable=var,value=2,bg='dark grey',font='Arial 12 bold')
R3=Radiobutton(frame_options,text="Turkish",variable=var,value=3,bg='dark grey',font='Arial 12 bold')
R1.pack(padx=3,pady=5,side=LEFT)
R2.pack(padx=3,pady=5,side=LEFT)
R3.pack(padx=3,pady=5,side=LEFT)
gonder_butonu=Button(frame_mid,text="Start",command=gonder(),font='Arial 10 bold',height=3,width=12)
gonder_butonu.pack(padx=3,pady=15,side=TOP)
bitir_butonu=Button(frame_mid,text="Stop",command="",font="Arial 10 bold",height=3,width=12,bg="red")
bitir_butonu.pack(padx=3,pady=15,side=TOP)
masterr.mainloop()






#---------------------------------------INTERFACE-----------------------------------------


    
