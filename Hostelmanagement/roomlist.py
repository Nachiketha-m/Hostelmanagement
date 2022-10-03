from tkinter import *
from tkinter import messagebox

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


#buttons    
broom=Button(root,text="Room List",height=1,width=13,bg='black',fg='white',font='Bold',command=newwindow1).pack()
bmess=Button(root,text="Mess",height=1,width=13,bg='black',fg='white',font='Bold',command=newwindow2).pack()
bfee=Button(root,text="Fee payment",height=1,width=13,bg='black',fg='white',font='Bold',command=newwindow3).pack()
blogout=Button(root,text="Logout",height=1,width=13,bg='black',fg='white',font='Bold',command=logout).pack()



root.mainloop()
