# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:28:27 2024

@author: halde
"""
from tkinter import*
from tkinter import ttk
import sqlite3
class patient:
    def __init__(self):
        self.sql=sqlite3.connect("pathology.db")
        self.c=self.sql.cursor()
        
        self.root=Toplevel()
        self.root.geometry("1200x500+200+200")
        
        Label(self.root,text="Patient Name").grid(row=0,column=0,sticky=E)
        self.pname=StringVar()
        self.pname.set("Name")
        self.combo=ttk.Combobox(self.root,textvariable=self.pname,width=50)
        self.combo.grid(row=0,column=1,sticky=W,padx=10,pady=10)
        e=self.c.execute("SELECT pname from patient order by pname")
        l1=[i[0] for i in e]
        print(l1)
        self.combo.config(values=l1)
        
        
        self.btnshow=ttk.Button(self.root,text="Show details",state=DISABLED,command=self.action)
        self.btnshow.grid(row=0,column=1,sticky=W,padx=500)
        
        self.tree2=ttk.Treeview(self.root,height=6,columns=10)
        self.tree2['show']='headings'
        self.tree2['columns']=['Patient Name','Doctor','Phno','Address','Age']
        self.tree2.grid(row=1,column=0,sticky=(N,W),columnspan=3,padx=10,pady=10)
        
        for i in range(5):
            self.tree2.heading(i,text='{}'.format(self.tree2['columns'][i]))
            self.tree2.column(i,anchor=CENTER)
        
        self.scrol=ttk.Scrollbar(self.root,orient=VERTICAL,command=self.tree2.yview)
        self.tree2['yscrollcommand']=self.scrol.set
        self.scrol.grid(row=1,column=1,sticky=(N,S,W),padx=934)
        
        
        self.tree3=ttk.Treeview(self.root,height=6,columns=10)
        self.tree3['show']='headings'
        self.tree3['columns']=['Order ID','Order Date','Patient Name','Total Amt','No of Test']
        self.tree3.grid(row=2,column=0,sticky=(N,W),columnspan=3,padx=10,pady=10)
        
        for i1 in range(5):
            self.tree3.heading(i1,text='{}'.format(self.tree3['columns'][i1]))
            self.tree3.column(i1,anchor=CENTER)
        
        self.scrol1=ttk.Scrollbar(self.root,orient=VERTICAL,command=self.tree3.yview)
        self.tree3['yscrollcommand']=self.scrol1.set
        self.scrol1.grid(row=2,column=1,sticky=(N,S,W),padx=934)
        
        self.combo.bind("<<ComboboxSelected>>",lambda a:self.Comboclick("Name"))
        
        self.btndel=ttk.Button(self.root,text="Delete Patient",command=self.delete,state=DISABLED)
        self.btndel.grid(row=0,column=1,sticky=W,padx=580)
        
        
        self.root.mainloop()
        
        
    def viewRecord(self):
          self.c=self.sql.cursor()
          x=self.tree2.get_children()
          name=self.pname.get()
          for i in x:
              self.tree2.delete(i)
              
          x2=self.tree3.get_children()
          for i1 in x2:
              self.tree3.delete(i1)
      
          list=self.c.execute("SELECT * FROM patient where pname=?",(name,)).fetchall()
          list1=self.c.execute("SELECT * FROM  orderdetails  where pname=?",(name,)).fetchall()
          print(list1)
      
          for item in list:
              self.tree2.insert('',0,text=item[0],values=(item[0],item[1],item[2],item[3],item[4]))
              
          for items in list1:
              self.tree3.insert('',0,values=(items[0],items[1],items[2],items[3],items[4]))
      
          self.c.close()
        
        
    def Comboclick(self,a):
        self.btnshow.config(state=NORMAL)
        self.btndel.config(state=NORMAL)
        
        
    def action(self):
         self.viewRecord()
         
    def delete(self):
        self.c=self.sql.cursor()
        name=self.tree2.item(self.tree2.selection())['text']
        orderid=self.c.execute("SELECT OID FROM  orderdetails WHERE pname=?",(name,)).fetchone()
        print(orderid)
        print(name)
        # query1="DELETE FROM patient where pname='%s'"%name
        # query2="DELETE FROM orderdetails where pname='%s'"%name
        # query3="DELETE FROM testdetails where OID='%s'"%orderid
        # self.c.execute(query3)
        # self.c.execute(query2)
        # self.c.execute(query1)
        self.sql.commit()
        self.c.close()
        self.viewRecord()
        
        
        
        