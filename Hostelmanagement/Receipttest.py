
'''import random
import datetime
from tkinter import *
from tkinter import messagebox
import mysql.connector
import Username_password as up


def rc():
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
        cur=mydb.cursor()
	root=Tk()
	root.title("RECEIPT")
	l1=Label(root,text="RECEIPT",font="Stencil").pack()
	root.geometry("450x500")
	L=["IT","NB","NB-X","MM","IH","G"]
	block=random.choice(L)
	n=cur.execute("SELECT `username` from userpwd Where password=%s",(up.e2.get()))
        namedis=cur.fetchone()



	receiptno=random.randint(1,1000)
	date=datetime.datetime.now()

	str=Label(root,text="******************").pack()

	Label(root,text="RECEIPT NUMBER").place(x=20,y=70)
	Label(root,text=receiptno).place(x=200,y=70)
	Label(root,text="DATE").place(x=20,y=100)
	Label(root,text=date).place(x=200,y=100)
	Label(root,text="NAME").place(x=20,y=130)
	Label(root,text="ROOM TYPE").place(x=20,y=160)
	Label(root,text="Room-T").place(x=200,y=160)
	Label(root,text="Hostel Block alloted:").place(x=20,y=290)
	Label(root,text=block).place(x=200,y=290)
	Label(root,text="TOTAL",font="impact").place(x=90,y=320)


	root.mainloop()

rc()'''

from tkinter import*
from PIL import ImageTk,Image

root=Tk()
root.title('bg image')
root.geometry("800x500")
bg = PhotoImage(file = "pesimg.png")
labepic = Label(root, image = bg)
labepic.place(x = 0,y = 0)
root.mainloop()












