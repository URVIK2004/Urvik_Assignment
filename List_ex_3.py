# wrong
from tkinter import *

w=Tk()

w.geometry("500x500")
w.configure("lightgreen") # To change the Background of window

favList=["Cricket","Volleyball","Football"]
AllList=["Netflix","Instagram","Twitter"]

l1 = Label(w,text="Favourite List:",font=("Satisfy",20),fg="white",justify=CENTER,background="lightgreen")
l1.grid(row=0,column=0)

l2 = Label(w,text="All List:",font=("Satisfy",20),fg="white",justify=CENTER,background="lightgreen")
l2.grid(row=0,column=0)

lb1 = Listbox(w,width=1,height=8,fg="maroon",font=("Times new roman",16),background="silver",
selectmode="multiple",selectbackground="lightgrey",selectforeground="black",justify=CENTER)
lb1.grid(row=1,column=3,padx=4,pady=55,rowspan=4)

lb2 = Listbox(w,width=1,height=8,fg="maroon",font=("Times new roman",16),background="silver",
selectmode="multiple",selectbackground="lightgrey",selectforeground="black",justify=CENTER)
lb2.grid(row=1,column=3,padx=4,pady=55,rowspan=4)

Ltor_addAll=Button(Text=">>",width=10,height=5,justify=CENTER,font=("Satisfy",9))
Ltor_addAll.grid(row=1,column=1,padx=15,pady=2,ipadx=2)

w.mainloop()