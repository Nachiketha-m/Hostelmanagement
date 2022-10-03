#functions

from tkinter import *
import mysql.connector

from ast import Return
from distutils import command
from re import L
import sys
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


#receipts
#receipt1
def rc1():
    import random
    import datetime
    root = Tk()
    root.title('RECEIPT')
    l1 = Label(root, text='RECEIPT', font='Stencil').pack()
    root.geometry('450x500')
    L = [
        'IT',
        'NB',
        'NB-X',
        'MM',
        'IH',
        'G',
        ]
    block = random.choice(L)

    receiptno = random.randint(1, 1000)
    date = datetime.datetime.now()

    str = Label(root, text='******************').pack()

    Label(root, text='RECEIPT NUMBER').place(x=20, y=70)
    Label(root, text=receiptno).place(x=200, y=70)
    Label(root, text='DATE').place(x=20, y=100)
    Label(root, text=date).place(x=200, y=100)
    Label(root, text='NAME').place(x=20, y=130)
    Label(root, text='PES University').place(x=200,y=130)
    Label(root, text='ROOM TYPE').place(x=20, y=160)
    Label(root, text='Room-T').place(x=200, y=160)
    Label(root, text='Hostel Block alloted:').place(x=20, y=290)
    Label(root, text=block).place(x=200, y=290)
    Label(root, text='TOTAL', font='impact').place(x=90, y=320)
    Label(root, text='₹1,35,000', font='impact').place(x=200,y=320)
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
    cur=mydb.cursor()
    cur.execute("UPDATE `projecthostel`.`rooms` SET `Number of rooms left` = `Number of rooms left`-1 WHERE (`Fees per year` = '135000');")
    mydb.commit()
    root.mainloop()

#receipt2
def rc2():
    import random
    import datetime
    root = Tk()
    root.title('RECEIPT')
    l1 = Label(root, text='RECEIPT', font='Stencil').pack()
    root.geometry('450x500')
    L = [
        'IT',
        'NB',
        'NB-X',
        'MM',
        'IH',
        'G',
        ]
    block = random.choice(L)

    receiptno = random.randint(1, 1000)
    date = datetime.datetime.now()

    str = Label(root, text='******************').pack()

    Label(root, text='RECEIPT NUMBER').place(x=20, y=70)
    Label(root, text=receiptno).place(x=200, y=70)
    Label(root, text='DATE').place(x=20, y=100)
    Label(root, text=date).place(x=200, y=100)
    Label(root, text='NAME').place(x=20, y=130)
    Label(root, text='PES University').place(x=200,y=130)
    Label(root, text='ROOM TYPE').place(x=20, y=160)
    Label(root, text='Room-D').place(x=200, y=160)
    Label(root, text='Hostel Block alloted:').place(x=20, y=290)
    Label(root, text=block).place(x=200, y=290)
    Label(root, text='TOTAL', font='impact').place(x=90, y=320)
    Label(root, text='₹1,50,000', font='impact').place(x=200,y=320)
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
    cur=mydb.cursor()
    cur.execute("UPDATE `projecthostel`.`rooms` SET `Number of rooms left` = `Number of rooms left`-1 WHERE (`Fees per year` = '150000');")
    mydb.commit()


    root.mainloop()

#receipt3
def rc3():
    import random
    import datetime
    root = Tk()
    root.title('RECEIPT')
    l1 = Label(root, text='RECEIPT', font='Stencil').pack()
    root.geometry('450x500')
    L = [
        'IT',
        'NB',
        'NB-X',
        'MM',
        'IH',
        'G',
        ]
    block = random.choice(L)

    receiptno = random.randint(1, 1000)
    date = datetime.datetime.now()

    str = Label(root, text='******************').pack()

    Label(root, text='RECEIPT NUMBER').place(x=20, y=70)
    Label(root, text=receiptno).place(x=200, y=70)
    Label(root, text='DATE').place(x=20, y=100)
    Label(root, text=date).place(x=200, y=100)
    Label(root, text='NAME').place(x=20, y=130)
    Label(root, text='PES University').place(x=200,y=130)
    Label(root, text='ROOM TYPE').place(x=20, y=160)
    Label(root, text='Room-S').place(x=200, y=160)
    Label(root, text='Hostel Block alloted:').place(x=20, y=290)
    Label(root, text=block).place(x=200, y=290)
    Label(root, text='TOTAL', font='impact').place(x=90, y=320)
    Label(root, text='₹1,80,000', font='impact').place(x=200,y=320)
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
    cur=mydb.cursor()
    cur.execute("UPDATE `projecthostel`.`rooms` SET `Number of rooms left` = `Number of rooms left`-1 WHERE (`Fees per year` = '180000');")
    mydb.commit()

    root.mainloop()


#contactswindow
def newwindow4():
    global mn,lmn
    r5=Toplevel()
    #r5.geometry('1000x1200')
    r5.title('CONTACTS')
    r5.configure(background='WHITE')
    mn=ImageTk.PhotoImage(Image.open('contacts.png'))
    lmn=Label(r5,image=mn).pack()

#main login image
def c6():
    global lsbr1
    global singlebr1
    global imgsbr1
    global cost1
    global recbut1
    r11=Toplevel()
    r11.geometry('1100x550')
    singlebr1=ImageTk.PhotoImage(Image.open('hostelmess2.jpg'))
    imgsbr1=Label(r11,image=singlebr1).pack()
    
def m2():
    global mess2,lm2
    m6=Toplevel()
    m6.geometry('1000x1000')
    m6.title('WEEK 1')
    m6.configure(background='')
    mess2=ImageTk.PhotoImage(Image.open('hostelmess2.JPG'))
    lm2=Label(m6,image=mess1)
def c12():
    global rlabel
    global rlabel2
    global rlabel3
    global pimg
    global imgp
    global pimg1
    global imgp1
    r10=Toplevel()
    r10.configure(background='white')
    r10.geometry('1050x750')
    r10.title('RECEIPT')

    pimg=ImageTk.PhotoImage(Image.open('paymentimg.jpeg'))
    imgp=Label(r10,image=pimg).place(x=40,y=20,width=1000,height=500)
    pimg1=ImageTk.PhotoImage(Image.open('payqr1.png'))
    imgp1=Label(r10,image=pimg1).place(x=910,y=0,width=120,height=150)
    rlabel=Label(r10,text="CONFIRMED ROOM:ROOM S",font=('stencil',40)).place(x=90,y=0)
    rlabel2=Label(r10,text="TOTAL FEES:1,80,000₹/YR",font=('stencil',40)).place(x=50,y=500)
    rlabel3=Label(r10,text="Click on the generate reciept below to recieve your confirmation token to address the WARDEN AND HIS TEAM",font='ITALIC',fg='red',bg='cyan').place(x=50,y=600)
    recbut2=Button(r10,text="CLICK IF PAYMENT DONE",font=('HELVATICA',10),fg='BLACK',command=rc3).place(x=50,y=450)

def c13():
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
    cur=mydb.cursor()
    
def c11():
    global rlabel
    global rlabel2
    global rlabel3
    global pimg
    global imgp
    global pimg1
    global imgp1
    r10=Toplevel()
    r10.configure(background='white')
    r10.geometry('1050x750')
    r10.title('RECEIPT')

    pimg=ImageTk.PhotoImage(Image.open('paymentimg.jpeg'))
    imgp=Label(r10,image=pimg).place(x=40,y=20,width=1000,height=500)
    pimg1=ImageTk.PhotoImage(Image.open('payqr1.png'))
    imgp1=Label(r10,image=pimg1).place(x=910,y=0,width=120,height=150)
    rlabel=Label(r10,text="CONFIRMED ROOM:ROOM D",font=('stencil',40)).place(x=90,y=0)
    rlabel2=Label(r10,text="TOTAL FEES:1,50,000₹/YR",font=('stencil',40)).place(x=50,y=500)
    rlabel3=Label(r10,text="Click on the generate reciept below to recieve your confirmation token to address the WARDEN AND HIS TEAM",font='ITALIC',fg='red',bg='cyan').place(x=50,y=600)
    recbut2=Button(r10,text="CLICK IF PAYMENT DONE",font=('HELVATICA',10),fg='BLACK',command=rc2).place(x=50,y=450)
def c10():
    global rlabel
    global rlabel2
    global rlabel3
    global pimg
    global imgp
    global pimg1
    global imgp1
    r10=Toplevel()
    r10.configure(background='white')
    r10.geometry('1050x750')
    r10.title('RECEIPT')

    pimg=ImageTk.PhotoImage(Image.open('paymentimg.jpeg'))
    imgp=Label(r10,image=pimg).place(x=40,y=20,width=1000,height=500)
    pimg1=ImageTk.PhotoImage(Image.open('payqr1.png'))
    imgp1=Label(r10,image=pimg1).place(x=910,y=0,width=120,height=150)
    rlabel=Label(r10,text="CONFIRMED ROOM:ROOM T",font=('stencil',40)).place(x=90,y=0)
    rlabel2=Label(r10,text="TOTAL FEES:1,35,000₹/YR",font=('stencil',40)).place(x=50,y=500)
    rlabel3=Label(r10,text="Click on the generate reciept below to recieve your confirmation token to address the WARDEN AND HIS TEAM",font='ITALIC',fg='red',bg='cyan').place(x=50,y=600)
    recbut2=Button(r10,text="CLICK IF PAYMENT DONE",font=('HELVATICA',10),fg='BLACK',command=rc1).place(x=50,y=450)
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
    lsbr2=Label(r9,text="CHOICE:TRIPLE BED ROOM",font=('Garamond',40),fg='green',bg='white').place(x=70,y=0)
    cost2=Label(r9,text="TOTAL AMOUNT=1,50,000₹/yr",font=('Stripes caps',20),fg='red',bg='white').place(x=50,y=500)
    recbut2=Button(r9,text="MAKE PAYMENT AND GENEREATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white',command=c10).place(x=611,y=515)

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
    lsbr1=Label(r8,text="CHOICE:DUAL BED ROOM",font=('Garamond',50),fg='green',bg='white').place(x=80,y=0)
    cost1=Label(r8,text="TOTAL AMOUNT=1,50,000₹/yr",font=('Stripes caps',20),fg='red',bg='white').place(x=50,y=500)
    recbut1=Button(r8,text="MAKE PAYMENT AND GENERATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white',command=c11).place(x=611,y=515)
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
    lsbr=Label(r7,text="CHOICE:SINGLE BED ROOM",font=('Garamond',50),fg='green',bg='white').place(x=80,y=0)
    cost=Label(r7,text="TOTAL AMOUNT=1,80,000₹/yr",font=('Stripes caps',20),fg='red',bg='white').place(x=50,y=300)
    recbut=Button(r7,text="MAKE PAYMENT AND GENEREATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white',command=c12).place(x=611,y=315)


def newwindow1():
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
    cur=mydb.cursor()
    root=Tk()
    root.title("Room Allotment")
    root.geometry("700x250")
    root.configure(bg="MistyRose2")
    #type of room
    ltype=Label(root,text="TYPES OF ROOM",font="Gadugi",bg="gold",fg="black").place(x=1,y=0)
    lsing=Label(root,text="Single Person Room",font="Gadugi",bg="black",fg="white").place(x=1,y=50)
    ldual=Label(root,text="Double Person Room",font="Gadugi",bg="black",fg="white").place(x=3,y=100)
    ltri=Label(root,text="Triple Person Room",font="Gadugi",bg="black",fg="white").place(x=1,y=150)

    #room price
    lcost=Label(root,text="COST",font="Gadugi",bg="gold",fg="black").place(x=210,y=0)
    l1=Label(root,text="1,80,000",font="Gadugi",bg="white",fg="black").place(x=200,y=50)
    l2=Label(root,text="1,50,000",font="Gadugi",bg="white",fg="black").place(x=200,y=100)
    l3=Label(root,text="1,30,000",font="Gadugi",bg="white",fg="black").place(x=200,y=150)
    #single
    s=cur.execute("select `Number of rooms left` from projecthostel.rooms where `Fees per year`=180000")
    l=cur.fetchone()
    #double
    s2=cur.execute("select `Number of rooms left` from projecthostel.rooms where `Fees per year`=150000")
    l2=cur.fetchone()
    #triple
    s3=cur.execute("select `Number of rooms left` from projecthostel.rooms where `Fees per year`=135000")
    l3=cur.fetchone()
    #availability
    ll0=Label(root,text="AVAILABILITY",font="Gadugi",bg="gold",fg="black").place(x=340,y=0)
    ll1=Label(root,text=l,font="Gadugi",bg="white",fg="black").place(x=350,y=50)
    ll2=Label(root,text=l2,font="Gadugi",bg="white",fg="black").place(x=350,y=100)
    ll3=Label(root,text=l3,font="Gadugi",bg="white",fg="black").place(x=350,y=150)

    #book buttons
    but0=Label(root,text="BOOK NOW!!!",font="Gadugi",bg="gold",fg="black").place(x=540,y=0)
    but1=Button(root,text="BOOK NOW",font="Gadugi",bg="black",fg="white",height="1",width="20",command=c7).place(x=500,y=50)
    but2=Button(root,text="BOOK NOW",font="Gadugi",bg="black",fg="white",height="1",width="20",command=c8).place(x=500,y=100)
    but3=Button(root,text="BOOK NOW",font="Gadugi",bg="black",fg="white",height="1",width="20",command=c9).place(x=500,y=150)
    root.mainloop()
    
def newwindow2():
    '''root2=Toplevel()
    root=Tk()
    root2.title("MESS")'''
    
    
def newwindow3():
    global lsbr1
    global singlebr1
    global imgsbr1
    global cost1
    global recbut1
    r11=Toplevel()
    r11.geometry('710x550')
    singlebr1=ImageTk.PhotoImage(Image.open('laundryimg.jpg'))
    imgsbr1=Label(r11,image=singlebr1).pack()    
#logout notify   
def logout():
    messagebox.showinfo("","logged out")

'''from ast import Return
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
    recbut=Button(r7,text="MAKE PAYMENT AND GENEREATE RECEIPT",font=('HELVATICA',10),fg='red',bg='white').place(x=611,y=315)'''


