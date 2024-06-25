from tkinter import *

root=Tk()
root.geometry("1000x550")
root.title("Bill Management System")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_idli.delete(0,END)
    entry_vada.delete(0,END)
    entry_chai.delete(0,END)
    entry_coffee.delete(0,END)
    entry_rasam.delete(0,END)
    entry_tot.delete(0,END)

def totl():
    try: a1=int(dosa.get())
    except: a1=0

    try: a2=int(idli.get())
    except: a2=0

    try: a3=int(vada.get())
    except: a3=0

    try: a4=int(chai.get())
    except: a4=0

    try: a5=int(coffee.get())
    except: a5=0

    try: a6=int(rasam.get())
    except: a6=0

    #cost per item
    c1=a1*70
    c2=a2*60
    c3=a3*50
    c4=a4*10
    c5=a5*10
    c6=a6*30

    lbl_tot=Label(f2,font=("arial",20,"bold"),text="Total",width=16,fg="blue")
    lbl_tot.place(x=0,y=50)


    total_cost=c1+c2+c3+c4+c5+c6
    str_bill="Rs.",str('%.2f' %total_cost)
    tot.set(str_bill)




Label(text="Bill Management System",bg="black",fg="white",font=("Gabriola",30),width="300",height="2").pack()

#Menu
f=Frame(root,bg="blue",highlightbackground="white",highlightthickness=1,width=300,height=290)
f.place(x=10,y=167)

Label(f,text="Menu",font=("Gabriola",35,"bold"),fg="black",bg="blue").place(x=80,y=0)
Label(f,font=("Gabriola",15,"bold"),text="Dosa ....... 70 Rs/plate",fg="white",bg="blue").place(x=50,y=70)
Label(f,font=("Gabriola",15,"bold"),text="Idli ....... 60 Rs/plate",fg="white",bg="blue").place(x=50,y=105)
Label(f,font=("Gabriola",15,"bold"),text="Medu Vada ....... 50 Rs/plate",fg="white",bg="blue").place(x=50,y=135)
Label(f,font=("Gabriola",15,"bold"),text="Chai ....... 10 Rs/plate",fg="white",bg="blue").place(x=50,y=165)
Label(f,font=("Gabriola",15,"bold"),text="Coffee ....... 10 Rs/plate",fg="white",bg="blue").place(x=50,y=195)
Label(f,font=("Gabriola",15,"bold"),text="Rasam ....... 30 Rs/plate",fg="white",bg="blue").place(x=50,y=225)

#Entry Variables
f1=Frame(root,bd=7,height=410,width=300,relief=RAISED)
f1.place(x=320,y=167)

dosa=StringVar()
idli=StringVar()
chai=StringVar()
vada=StringVar()
coffee=StringVar()
rasam=StringVar()
tot=StringVar()

#Label
lbl_dosa=Label(f1,font=("arial",17,"bold"),text="Dosa",width=12,fg="red")
lbl_dosa.grid(row=1,column=0)

lbl_idli=Label(f1,font=("arial",17,"bold"),text="Idli",width=12,fg="red")
lbl_idli.grid(row=2,column=0)

lbl_vada=Label(f1,font=("arial",17,"bold"),text="Vada",width=12,fg="red")
lbl_vada.grid(row=3,column=0)

lbl_chai=Label(f1,font=("arial",17,"bold"),text="Chai",width=12,fg="red")
lbl_chai.grid(row=4,column=0)

lbl_coffee=Label(f1,font=("arial",17,"bold"),text="Coffee",width=12,fg="red")
lbl_coffee.grid(row=5,column=0)

lbl_rasam=Label(f1,font=("arial",17,"bold"),text="Rasam",width=12,fg="red")
lbl_rasam.grid(row=6,column=0)


#Bill
f2=Frame(root,highlightbackground="blue",highlightthickness=3,bd=7,height=370,width=300,relief=RAISED)
f2.place(x=670,y=167)

Bill=Label(f2,text="Bill",font=("calibri",20,"bold"))
Bill.place(x=120,y=10)





#Entry Work
entry_dosa=Entry(f1,font=("arial",20,"bold"),textvariable=dosa,bd=6,width=8,bg="red",fg="white")
entry_dosa.grid(row=1,column=1)

entry_idli=Entry(f1,font=("arial",20,"bold"),textvariable=idli,bd=6,width=8,bg="red",fg="white")
entry_idli.grid(row=2,column=1)

entry_vada=Entry(f1,font=("arial",20,"bold"),textvariable=vada,bd=6,width=8,bg="red",fg="white")
entry_vada.grid(row=3,column=1)

entry_chai=Entry(f1,font=("arial",20,"bold"),textvariable=chai,bd=6,width=8,bg="red",fg="white")
entry_chai.grid(row=4,column=1)

entry_coffee=Entry(f1,font=("arial",20,"bold"),textvariable=coffee,bd=6,width=8,bg="red",fg="white")
entry_coffee.grid(row=5,column=1)

entry_rasam=Entry(f1,font=("arial",20,"bold"),textvariable=rasam,bd=6,width=8,bg="red",fg="white")
entry_rasam.grid(row=6,column=1)

entry_tot=Entry(f2,font=("arial",20,"bold"),textvariable=tot,bd=6,width=15,)
entry_tot.place(x=20,y=100)

#Buttons
rst=Button(f1,bd=5,fg="white",bg="blue",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
rst.grid(row=8,column=0)
btn_tot=Button(f1,bd=5,fg="white",bg="blue",font=("arial",16,"bold"),width=10,text="Total",command=totl)
btn_tot.grid(row=8,column=1)



root.mainloop()