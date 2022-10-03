from ast import Return
from distutils import command
from re import L
import sys
from tkinter import *
from PIL import ImageTk,Image
def c9():
    global lsbr2
    global singlebr2
    global imgsbr2
    global cost2
    global recbut2
    r9=Toplevel()
    r9.geometry('910x550')
    r9.title(' ROOM-T')
    r9.configure(background='cyan')
    singlebr2=ImageTk.PhotoImage(Image.open('3bedroom.jpeg'))
    imgsbr2=Label(r9,image=singlebr2).place(x=60,y=15,width=800,height=500)
    lsbr2=Label(r9,text="CHOICE:TRIPLE BED ROOM",font=('Garamond',50),fg='green',bg='white').place(x=90,y=0)
    cost2=Label(r9,text="TOTAL AMOUNT=1,50,000$/yr",font=('Stripes caps',20),fg='red',bg='white').place(x=50,y=500)
    recbut2=Button(r9,text="MAKE PAYMENT AND GENEREATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white').place(x=611,y=515)
def c8():
    global lsbr1
    global singlebr1
    global imgsbr1
    global cost1
    global recbut1
    r8=Toplevel()
    r8.geometry('910x550')
    r8.title(' ROOM-D')
    r8.configure(background='cyan')
    singlebr1=ImageTk.PhotoImage(Image.open('2bedroom.jpeg'))
    imgsbr1=Label(r8,image=singlebr1).place(x=60,y=15,width=800,height=500)
    lsbr1=Label(r8,text="CHOICE:DUAL BED ROOM",font=('Garamond',50),fg='green',bg='white').place(x=90,y=0)
    cost1=Label(r8,text="TOTAL AMOUNT=1,50,000$/yr",font=('Stripes caps',20),fg='red',bg='white').place(x=50,y=500)
    recbut1=Button(r8,text="MAKE PAYMENT AND GENEREATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white').place(x=611,y=515)
def c7():
    global lsbr
    global singlebr
    global imgsbr
    global cost
    global recbut
    r7=Toplevel()
    r7.geometry('900x350')
    r7.title(' ROOM-S')
    r7.configure(background='cyan')
    singlebr=ImageTk.PhotoImage(Image.open('singlebr.jpeg'))
    imgsbr=Label(r7,image=singlebr).place(x=60,y=15,width=800,height=300)
    lsbr=Label(r7,text="CHOICE:SINGLE BED ROOM",font=('Garamond',50),fg='green',bg='white').place(x=90,y=0)
    cost=Label(r7,text="TOTAL AMOUNT=1,80,000$/yr",font=('Stripes caps',20),fg='red',bg='white').place(x=50,y=300)
    recbut=Button(r7,text="MAKE PAYMENT AND GENEREATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white').place(x=611,y=315)
