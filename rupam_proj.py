from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import Menu
import sqlite3
import admin
import booking_pathology
import patient
from tkinter import font


class pathology:
    def __init__(self):
        self.sql=sqlite3.connect("pathology.db")
        self.c=self.sql.cursor()
        self.root=Tk()
        self.root.geometry("1360x720+0+0")

        self.root.config(bg="white")
        
        self.mbar=Menu(self.root)
        
        self.admin=Menu(self.mbar)
        self.booking=Menu(self.mbar)
        self.patient=Menu(self.mbar)
        
        
        
        self.patient.add_cascade(label="Patient Details",command=lambda:self.method('Patient Details'))
                          
        
        self.admin.add_cascade(label="New Test",command=lambda:self.method('New Test'))
        
        self.booking.add_cascade(label="New Booking",command=lambda:self.method('New Booking'))
        
        self.mbar.add_cascade(label="Admin",menu=self.admin)
        self.mbar.add_cascade(label="Patient",menu=self.patient)
        self.mbar.add_cascade(label="Booking",menu=self.booking)
        self.root.config(menu=self.mbar)
        
        #image=Image.open('pathology.png')
        image_tk=ImageTk.PhotoImage(file='pathology.jpeg')
        l=Label(self.root,image=image_tk)
        l.image=image_tk
        l.pack()
        
        
       
        
        # self.image1=Image.open("pathology.jpeg").resize((1360,720))
        # self.image2=ImageTk.PhotoImage(self.image1)
        # self.l1=Label(root,image=self.image2).grid(row=0,column=0)
       
        self.root.mainloop()

    def method(self,caption):
        if caption=='New Test':
            admin.Admin()   
        elif caption=='New Booking':
            booking_pathology.booking()
        elif caption=='Patient Details':
            patient.patient()






pathology()
