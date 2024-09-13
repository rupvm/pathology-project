# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:33:45 2024

@author: Anthony
"""
from PIL import ImageTk,Image
from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import font
class Admin:
    def __init__(self):
        self.sql=sqlite3.connect("pathology.db")
        self.c=self.sql.cursor()
        
        self.root=Toplevel()
        self.root.geometry("850x410+200+200")
        self.root.config(bg="#0063b2")
        self.image_tk=ImageTk.PhotoImage(file='admin1.png')
        self.label=Label(self.root,bg="#0063b2",image=self.image_tk)
        self.label.grid(row=0,column=0,padx=5)
    
        self.fr=LabelFrame(self.root,text="ADD NEW ENTRY",bg="#0063b2",fg="White")
        self.fr.grid(row=0,column=1,sticky=E,padx=8,pady=8)
    
        Label(self.fr,text="Test Name:",bg="#0063b2",fg="white",font=('Helvetica',10,font.BOLD)).grid(row=1,column=0,padx=5,sticky=W)
        self.tname=StringVar()
        testfield=Entry(self.fr,textvariable=self.tname,width=50,bg="#71bde3",fg="black")
        testfield.grid(row=1,column=1,padx=5,pady=5)
    
        Label(self.fr,text="Cost of Test:",bg="#0063b2",fg="White",font=('Helvetica',10,font.BOLD)).grid(row=2,column=0,padx=5,pady=5,sticky=W)
        self.cost=IntVar()
        self.costfield=Entry(self.fr,textvariable=self.cost,width=50,bg="#71bde3",fg="black").grid(row=2,column=1,padx=5)
    
        Label(self.fr,text="No of days to check:",bg="#0063b2",fg="white",font=('Helvetica',10,font.BOLD)).grid(row=3,column=0,padx=5,pady=5,sticky=W)
        self.nodays=IntVar()
        self.daysfield=Entry(self.fr,textvariable=self.nodays,width=50,bg="#71bde3",fg="black").grid(row=3,column=1,padx=5)
    
        btnadd=ttk.Button(self.fr,text="Add Data",command=self.add_data)
        btnadd.grid(row=5,column=5,sticky=W,padx=10,pady=10)
    
        btnshow=ttk.Button(self.root,text="Show Record",command=self.viewRecord)
        btnshow.grid(row=1,column=0,sticky=E)
    
        self.msg=Label(self.root,text='',fg="#ed3e6c",bg="#0063b2")
        self.msg.grid(row=1,column=1,sticky=(N,S))
    
        self.tree=ttk.Treeview(self.root,height=6,columns=10)
        self.tree['show']='headings'
        self.tree['columns']=['Test Name','Cost','Test Duration']
        self.tree.grid(row=2,column=0,sticky=(N,S,E,W),columnspan=2,padx=15,pady=10)
    
        for i in range(3):
            self.tree.heading(i,text='{}'.format(self.tree["columns"][i]))
            self.tree.column(i,anchor=CENTER)
    
        self.scrol=ttk.Scrollbar(self.root,orient=VERTICAL,command=self.tree.yview)
        self.tree['yscrollcommand']=self.scrol.set
        self.scrol.grid(row=2,column=2,sticky=(E,W,S,N))
        
    
        btndel=ttk.Button(self.root,text="Delete Record",command=self.delete_data) 
        btndel.grid(row=3,column=1,sticky=E,padx=10,pady=10)
    
        btnupdate=ttk.Button(self.root,text="Update Record",command=self.update)
        btnupdate.grid(row=3,column=0,sticky=W,padx=10,pady=10)
        self.create_table()
        self.root.mainloop()

    def viewRecord(self):
        self.c=self.sql.cursor()
        x=self.tree.get_children()
        for i in x:
            self.tree.delete(i)
    
        list1=self.c.execute("SELECT * FROM pathology ORDER BY COST DESC")
    
        for item in list1:
            self.tree.insert('',0,text=item[0],values=(item[0],item[1],item[2]))
    
        self.c.close()




    def create_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS pathology(tame TEXT primary key, Cost INTERGER, nodays INTEGER)")
        
    
    
    def add_data(self):
        test=self.tname.get()
        cost1=self.cost.get()
        days=self.nodays.get()
        
        if test=="":
            self.msg['text']="PILIZ INSERT THE TEST NAME"
        elif cost1==0:
            self.msg['text']="PILIZ INSERT THE COST"
        elif days==0:
            self.msg['text']="PILIZ INSERT THE DAYS"   
        else:    
            self.c=self.sql.cursor()
            self.c.execute("INSERT INTO pathology VALUES(?,?,?)",(test,cost1,days))
            self.sql.commit()
            self.c.close()
            self.tname.set("")
            self.nodays.set(0)
            self.cost.set(0)
            self.msg['text']="DATA INSERTED SUCESSFULY"
            self.viewRecord() 
            
        
    def delete_data(self):
        self.msg['text']=""
        self.c.close()
        self.c=self.sql.cursor()
        name=self.tree.item(self.tree.selection())['text']
        query="DELETE FROM pathology WHERE tame='%s'"%name
        self.c.execute(query)
        self.sql.commit()
        self.c.close()
        self.msg['text']="RECORD DELETED"
        self.viewRecord()
        
    def update(self):
        t1=Tk()
        t1.geometry("500x400+0+0")
        
        name=self.tree.item(self.tree.selection())['text']
        record=self.tree.item(self.tree.selection())['values']
        
        l1=ttk.Label(t1,text="Test Name:").grid(row=0,column=0,padx=5,pady=5,sticky=W)
        e1=Entry(t1)
        e1.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        e1.insert(0, name)
        e1.config(state=DISABLED)
        
        l2=ttk.Label(t1,text="Cost:").grid(row=1,column=0,padx=5,pady=5,sticky=W)
        e2=Entry(t1)
        e2.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        e2.insert(0,record[1])
        e2.config(state=DISABLED)
        
        l3=ttk.Label(t1,text="No of days:").grid(row=2,column=0,padx=5,pady=5,sticky=W)
        e3=Entry(t1)
        e3.grid(row=2,column=1,padx=5,sticky=W)
        e3.insert(0,record[2])
        e3.config(state=DISABLED)
        
        
        l4=ttk.Label(t1,text="New Test Name:").grid(row=0,column=2,padx=5,pady=5,sticky=W)
        v1=StringVar()
        e4=Entry(t1,textvariable=v1)
        e4.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        l5=ttk.Label(t1,text="New Cost:").grid(row=1,column=2,padx=5,pady=5,sticky=W)
        v2=IntVar()
        e5=Entry(t1,textvariable=v2)
        e5.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        l6=ttk.Label(t1,text="No of days:").grid(row=2,column=2,padx=5,pady=5,sticky=W)
        v3=IntVar()
        e6=Entry(t1,textvariable=v3)
        e6.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        
        b1=ttk.Button(t1,text="Update",command=lambda:self.update_data(e4.get(),e5.get(),e6.get(),name))
        b1.grid(row=3,column=3,padx=5,pady=5,sticky=(N,S,E,W))
        
        
    def update_data(self,v1,v2,v3,name):
        self.c.close()
        self.c=self.sql.cursor()
        a=v1
        b=v2
        c=v3
        print(a,b,c,name)
        self.c.execute("UPDATE pathology set tame=?,cost=?,nodays=? WHERE tame=?",(a,b,c,name))
        self.sql.commit()
        self.c.close()
        self.msg['text']="DATA UPDATED"
        self.viewRecord()
                
        
        

        
        
        
        

#admin(self.root1)
