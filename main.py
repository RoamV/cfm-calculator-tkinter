from tkinter import*

def hitung():
    Length=int(entry_length.get())
    Width=int(entry_width.get())
    Qty=int(entry_qty.get())
    
    mm=(int(Length)*int(Width))/10**6
    entry_mm.delete('0', 'end')
    entry_mm.insert(END, string=mm)
    inchy=(int(Length)+int(Width))/50
    entry_inch.delete('0', 'end')
    entry_inch.insert(END, string=inchy)
    Cfm=(int(Length)*int(Width)/10**6/0.09*600)
    entry_cfm.delete('0', 'end')
    entry_cfm.insert(END, string=Cfm)
    m3=(int(Qty)*((Length+60)*(Width+60)*60)/10**9)
    entry_m3.delete('0', 'end')
    entry_m3.insert(END, string=m3)

root= Tk()
root.minsize(width=500, height=500)
root.resizable(False,False)
root.config(bg="cadetblue")
title=Label(text="Costume Calculator",font=("Times New Roman",25,"bold"),fg="black",bg="cadet blue").place(x=130,y=30)

lbl_length=Label(text="Length",font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=0,y=100) 

entry_length=Entry(font=("times new roman",20))
entry_length.place(x=110,y=100,height=40,width=100)

lbl_width=Label(text="Width",font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=0,y=170) 
entry_width=Entry(font=("times new roman",20))
entry_width.place(x=110,y=170,height=40,width=100)

lbl_qty=Label(text="Qty",font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=0,y=240) 
entry_qty=Entry(font=("times new roman",20))
entry_qty.place(x=110,y=240,height=40,width=100)

#==============================================================================================================================#

lbl_mm=Label(text="mm",font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=220,y=100) 
entry_mm=Entry(fg="black",bg="white",font=("times new roman",20))
entry_mm.place(x=300,y=100,height=40,width=100)

lbl_cfm=Label(text="Cfm",font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=220,y=170) 
entry_cfm=Entry(fg="black",bg="white",font=("times new roman",20))
entry_cfm.place(x=300,y=170,height=40,width=100)

lbl_m3=Label(text='m3',font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=220,y=240) 
entry_m3=Entry(fg="black",bg="white",font=("times new roman",20))
entry_m3.place(x=300,y=240,height=40,width=100)

lbl_inch=Label(text='Inch',font=("Times New Roman",15,"bold"),fg="black",bg="cadet blue").place(x=220,y=300) 
entry_inch=Entry(fg="black",bg="white",font=("times new roman",20))
entry_inch.place(x=300,y=300,height=40,width=100)

hasil=Button(text="Calculate",font=("Times New Roman",15,"bold"),command=hitung,bg="white",fg="black",width=13).place(x=20,y=300)

root.mainloop()
