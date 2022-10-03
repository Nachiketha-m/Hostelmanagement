from tkinter import *
import mysql.connector
import functions as f


window=Tk()
window.title("HOSTEL LOGIN")
window.geometry("300x250")



def login():
    def login_database():
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
        cur=mydb.cursor()
        cur.execute("SELECT * from userpwd Where username=%s and password=%s",(e1.get(),e2.get()))
        l=cur.fetchall()
        mydb.close()
        print(l)
        if l!=[]:
            username=l[0][1]
            l3.config(text="User name found")
            root=Tk()
            root.title("STUDENT MAIN PAGE")
            l1=Label(root,text="STUDENT MAIN PAGE",font="Stencil").pack()
            root.geometry("350x200")
            broom=Button(root,text="Room List",height=1,width=13,bg='black',fg='white',font='Bold',command=f.newwindow1).pack()
            bmess=Button(root,text="Mess",height=1,width=13,bg='black',fg='white',font='Bold',command=f.c6).pack()
            bfee=Button(root,text="Laundry",height=1,width=13,bg='black',fg='white',font='Bold',command=f.newwindow3).pack()
            blogout=Button(root,text="Logout",height=1,width=13,bg='black',fg='white',font='Bold',command=f.logout).pack()
            

        else:
            l3.config(text="User not found")

    window.destroy()
    login_window=Tk()
    login_window.geometry("400x250")
    l1=Label(login_window,text="Username",font="times 20")
    l1.grid(row=1,column=1)
    l2=Label(login_window,text="Password",font="times 20")
    l2.grid(row=2,column=1)
    l3=Label(login_window,font="times 20")
    l3.grid(row=5,column=2)
    email_text=StringVar()

    e1=Entry(login_window,textvariable=email_text)
    e1.grid(row=1,column=2)
    password_text=StringVar()
    e2=Entry(login_window,textvariable=password_text)
    e2.grid(row=2,column=2)
    e2.config(show="*")
    b1=Button(login_window,text="LOGIN",width=20,command=login_database)
    b1.grid(row=4,column=2)
    login_window.mainloop()
    window.destroy()

def signup():
    def signup_database():
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Amadpsnacha@123", database = "projecthostel")
        cur = mydb.cursor()
        cur.execute("""INSERT INTO userpwd (`username`, `password`) VALUES (%s,%s)""", (e1.get(), e2.get()))
        l4 = Label(signup_window, text = "Account Created", font = "times 15")
        l4.grid(row = 6, column = 2)
        mydb.commit()
        mydb.close()


    window.destroy()
    signup_window = Tk()
    signup_window.geometry("400x250")
    l1 = Label(signup_window, text = "User Name", font = "times 20")
    l1.grid(row = 1, column = 1)
    l2 = Label(signup_window, text = "Password", font = "times 20")
    l2.grid(row = 3, column = 1)

    name_text = StringVar()
    e1 = Entry(signup_window, textvariable = name_text)
    e1.grid(row = 1, column = 2)
    email_text = StringVar()
    password_text = StringVar()
    e2 = Entry(signup_window, textvariable = password_text)
    #e2.config("*")
    e2.grid(row = 3, column = 2)

    b1 = Button(signup_window, text = "Signup", width = 20, command = signup_database)
    b1.grid(row = 4, column = 2)



		
c=Canvas(window,bg="gray16",height=200,width=200)


l1=Label(window,text="HOSTEL",font="times 20")
l1.place(x=100,y=10)

b1=Button(window,text="LOGIN",width=20,command=login)
b1.place(x=80,y=70)
b2=Button(window,text="SIGNUP",width=20,command=signup)
b2.place(x=80,y=120)
'''

# Importing module
import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
cur=mydb.cursor()
username=input("Enter user: ")
password=input("Enter pwd: ")
statement = f"SELECT username from userpwd WHERE username='{username}' AND password = '{password}';"
cur.execute(statement)
if not cur.fetchone():
    print("Login failed")
else:
    print("Welcome")
root=Tk()
root.title("STUDENT MAIN PAGE")
l1=Label(root,text="STUDENT MAIN PAGE",font="Stencil").pack()
root.geometry("350x200")


#new window
def newwindow1():
    root1=Toplevel()
    root1.title("ROOM LIST")
    
def newwindow2():
    root2=Toplevel()
    root2.title("MESS")
    
def newwindow3():
    root3=Toplevel()
    root3.title("FEE PAYMENT")
    
#logout notify   
def logout():
        messagebox.showinfo("","logged out")
broom=Button(root,text="Room List",height=1,width=13,bg='black',fg='white',font='Bold',command=newwindow1).pack()
bmess=Button(root,text="Mess",height=1,width=13,bg='black',fg='white',font='Bold',command=newwindow2).pack()
bfee=Button(root,text="Fee payment",height=1,width=13,bg='black',fg='white',font='Bold',command=newwindow3).pack()
blogout=Button(root,text="Logout",height=1,width=13,bg='black',fg='white',font='Bold',command=logout).pack()
from tkinter import *
from tkinter import messagebox'''

'''
root=Tk()
root.title("Room Allotment")
root.geometry("700x250")

#type of room
ltype=Label(root,text="TYPES OF ROOM",font="Gadugi",bg="gold",fg="black").place(x=1,y=0)
lsing=Label(root,text="Single Bed Room",font="Gadugi",bg="black",fg="white").place(x=1,y=50)
ldual=Label(root,text="Dual Bed Room",font="Gadugi",bg="black",fg="white").place(x=3,y=100)
ltri=Label(root,text="Triple Bed Room",font="Gadugi",bg="black",fg="white").place(x=1,y=150)

#room price
lcost=Label(root,text="COST",font="Gadugi",bg="gold",fg="black").place(x=210,y=0)
l1=Label(root,text="1,30,000",font="Gadugi",bg="white",fg="black").place(x=200,y=50)
l2=Label(root,text="1,56,000",font="Gadugi",bg="white",fg="black").place(x=200,y=100)
l3=Label(root,text="1,83,000",font="Gadugi",bg="white",fg="black").place(x=200,y=150)

#availability
ll0=Label(root,text="AVAILABILITY",font="Gadugi",bg="gold",fg="black").place(x=340,y=0)
ll1=Label(root,text="available",font="Gadugi",bg="white",fg="black").place(x=350,y=50)
ll2=Label(root,text="available",font="Gadugi",bg="white",fg="black").place(x=350,y=100)
ll3=Label(root,text="available",font="Gadugi",bg="white",fg="black").place(x=350,y=150)

#book buttons
but0=Label(root,text="BOOK NOW!!!",font="Gadugi",bg="gold",fg="black").place(x=540,y=0)
but1=Button(root,text="BOOK NOW",font="Gadugi",bg="black",fg="white",height="1",width="20").place(x=500,y=50)
but2=Button(root,text="BOOK NOW",font="Gadugi",bg="black",fg="white",height="1",width="20").place(x=500,y=100)
but3=Button(root,text="BOOK NOW",font="Gadugi",bg="black",fg="white",height="1",width="20").place(x=500,y=150)



root.mainloop()'''


