from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
import subprocess as sp


root=Tk()
root.geometry('800x700')
root.minsize(800,700)
root.title("Ars Shop")
root.configure(background="purple")
#root.wm_iconbitmap("icon.ico")


l1=Label(root,text="YOU ARE WELCOME",font=("Times",19,"bold"),padx=80,pady=40,bg='yellow',borderwidth=5,relief=SUNKEN)
l1.pack(side=TOP,fill=X)


f=Frame(root,bg='white',borderwidth=10,relief=FLAT)
f.pack(side=LEFT,fill='y')
l=Label(f,text="Choose your dishes: ",fg='purple',padx=10,pady=10,font="Times 20 ").pack()


l=[]

def total1():
    print("New Record")
    if pizza.get()==1:
        a=spin1.get()
        b=50*int(a)
        l.append(b)
        print("Pizza x",spin1.get(),"=",b,"Rs.")
        #print("Your total Bill: ",sum(l),"Rs.")
    if burger.get()==1:
        c=spin2.get()
        d=40*int(c)
        l.append(d)
        print("Burger x",spin2.get(),"=",d,"Rs.")
        #print("Your total Bill: ",sum(l),"Rs.")
    if maggie.get()==1:
        e=spin3.get()
        f=30*int(e)
        l.append(f)
        print("Maggie x",spin3.get(),"=",f,"Rs.")
        #print("Your total Bill: ",sum(l),"Rs.")
    if paties.get()==1:
        g=spin4.get()
        h=20*int(g)
        l.append(h)
        print("Paties x",spin4.get(),"=",h,"Rs.")
        #print("Your total Bill: ",sum(l),"Rs.")
    if softdrink.get()==1:
        i=spin5.get()
        j=30*int(i)
        l.append(j)
        print("Soft Drink x",spin5.get(),"=",j,"Rs.")
    print("Your total Bill: ",sum(l),"Rs.")
    print()
    pizza.set(0)
    burger.set(0)
    maggie.set(0)
    paties.set(0)
    softdrink.set(0)
    l.clear()
    #os.system('cls')
    #sp.call('cls',shell=True)
    
    
pizza=IntVar()
Checkbutton(f, text="Pizza",bg='white',variable=pizza,font="Times 19 ").pack(anchor='w')
spin1=Spinbox(f,from_ = 1, to = 10)
spin1.pack(padx = 5, ipadx = 2, ipady = 5)

burger=IntVar()
Checkbutton(f, text="Burger",bg='white',variable=burger,font="Times 19 ").pack(anchor='w')
spin2=Spinbox(f,from_ = 1, to = 10)
spin2.pack(padx = 5, ipadx = 2, ipady = 5)

maggie=IntVar()
Checkbutton(f, text="Maggie",bg='white',variable=maggie,font="Times 19 ").pack(anchor='w')
spin3=Spinbox(f,from_ = 1, to = 10)
spin3.pack(padx = 5, ipadx = 2, ipady = 5)

paties=IntVar()
Checkbutton(f, text="Paties",bg='white',variable=paties,font="Times 19 ").pack(anchor='w')
spin4=Spinbox(f,from_ = 1, to = 10)
spin4.pack(padx = 5, ipadx = 2, ipady = 5)

softdrink=IntVar()
Checkbutton(f, text="Soft Drink",bg='white',variable=softdrink,font="Times 19 ").pack(anchor='w')
spin5=Spinbox(f,from_ = 1, to = 10)
spin5.pack(padx = 5, ipadx = 2, ipady = 5)

nn=Label(f,text=" ",bg="white").pack()
button=Button(f, fg="red", text="Done", command=total1,padx=10,pady=10,activebackground="green",font="Times 15 ").pack()


#############################################
photos=[]
for i in range(0,3):
    image=Image.open(f"{i+1}.jpg")
    image=image.resize((250,175),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))


Label(root,image=photos[0]).pack(anchor="se",padx=10,pady=10)
Label(root,image=photos[1]).pack(anchor="se",padx=10)
Label(root,image=photos[2]).pack(anchor="se",padx=10,pady=10)


'''
f2=Frame(root,bg='white',borderwidth=0,relief=SUNKEN)
f2.pack(side=LEFT,fill='y',expand=True)

photos1=[]
for i in range(3,7):
    image=Image.open(f"{i+1}.jpg")
    image=image.resize((250,175),Image.ANTIALIAS)
    photos1.append(ImageTk.PhotoImage(image))


Label(f,image=photos1[0]).pack(anchor="sw",padx=10,pady=10)
Label(f,image=photos1[1]).pack(anchor="sw",padx=10)
Label(f,image=photos1[2]).pack(anchor="sw",padx=10,pady=10)

'''

'''scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=root.yview)
root.config(yscrollcommand=scroll.set)
'''


root.mainloop()
