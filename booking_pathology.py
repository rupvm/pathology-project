
from tkinter import*
from tkinter import ttk
from tkinter import font
from datetime import date
from PIL import ImageTk,Image
import datetime
import itertools
import sqlite3
class booking:
    def __init__(self):
        self.cur=sqlite3.connect("pathology.db")
        self.c=self.cur.cursor()
        
        self.t2=Toplevel()
        self.t2.geometry("1600x720+200+200")
        self.t2.config(bg="#ebcad2")
      
        self.image_tk=ImageTk.PhotoImage(file='booking1.png')
        self.l=Label(self.t2,bg="#ebcad2",image=self.image_tk)
        self.l.grid(row=0,column=0,padx=5)
    
        self.fr=LabelFrame(self.t2,text="ADD NEW ORDER",bg="#ebcad2",fg="#0067C6")
        self.fr.grid(row=0,column=1,sticky=(N,E),padx=8,pady=8)
    
        l1=Label(self.fr,text="Order id:",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=0,column=0,padx=5,pady=10,sticky=W)
        self.orderid=StringVar()
        query1=self.c.execute("SELECT max(OID) from orderdetails").fetchone()
        print(query1)
        e=[i for i in query1]
        newId="00"+str(int(e[0])+1)
        print(newId)
        self.e1=ttk.Entry(self.fr,textvariable=self.orderid)
        self.e1.insert(0,newId)
        self.e1.grid(row=0,column=1,sticky=W,padx=5)
        self.e1.config(state=DISABLED)
    
        l2=Label(self.fr,text="Order Date",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=0,column=2,padx=5,sticky=W,pady=10)
        self.e2=ttk.Entry(self.fr)
        self.e2.grid(row=0,column=3,sticky=W,pady=5,padx=5)
        self.e2.insert(0,date.today())
        print(type(date.today()))
        self.e2.config(state=DISABLED)
    
        l3=Label(self.fr,text="Test Date:",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=0,column=4,padx=5,sticky=W,pady=10)
        self.testdate=StringVar()
        self.e3=ttk.Entry(self.fr,textvariable=self.testdate)
        self.e3.grid(row=0,column=5,sticky=W,padx=5,pady=5)
    
        l4=Label(self.fr,text="Doctor's Name:",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=0,column=6,padx=5,sticky=W,pady=10)
        self.docname=StringVar()
        self.e4=ttk.Entry(self.fr,textvariable=self.docname,width=30)
        self.e4.grid(row=0,column=7,sticky=W,padx=5,pady=5)
    
        l5=Label(self.fr,text="Patient Name",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=1,column=0,padx=5,pady=5,sticky=W)
        self.pname=StringVar()
        self.e5=ttk.Entry(self.fr,textvariable=self.pname,width=30)
        self.e5.grid(row=1,column=1,sticky=W,padx=5,pady=10)
    
        l6=Label(self.fr,text="Contact No",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=1,column=2,padx=5,pady=5,sticky=W)
        self.contact=IntVar()
        self.e6=ttk.Entry(self.fr,textvariable=self.contact,width=30)
        self.e6.grid(row=1,column=3,sticky=W,padx=5,pady=10)
    
        l7=Label(self.fr,text="Address:",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=1,column=4,padx=5,sticky=W,pady=10)
        self.address=StringVar()
        self.e7=Text(self.fr,width=25,height=3)
        self.e7.grid(row=1,column=5,sticky=W,padx=5,pady=10)
    
        l8=Label(self.fr,text="Age:",bg="#ebcad2",fg="#0067C6",font=("Helvetica",11,font.BOLD)).grid(row=2,column=0,padx=5,sticky=E,pady=10)
        self.age=StringVar()
        self.e8=Entry(self.fr,width=30,textvariable=self.age,fg="black",font=("Helvetica",11,font.BOLD))
        self.e8.grid(row=2,column=1,sticky=W,padx=5,pady=10)
        
        v=IntVar()
        v.set(0)
                
        
        ttk.Radiobutton(self.fr,text="Male",variable=v,value=1).grid(row=2,column=2,sticky=(E,W))
        ttk.Radiobutton(self.fr,text="Female",variable=v,value=2).grid(row=2,column=3,sticky=W)
           
            
    
        l9=Label(self.t2,text="Test Name",font=("Helvetica",12,font.ITALIC),bg="#ebcad2").grid(row=2,column=0,sticky=E)
        
        self.com=StringVar()
        self.com.set("Test")
        self.combo=ttk.Combobox(self.t2,textvariable=self.com,width=50)
        self.combo.grid(row=2,column=1,sticky=W,padx=10,pady=10)
        
        
        #self.com.trace(self,'w',self.Comboclick)
        
        e=self.c.execute('select tame from pathology order by tame')
        L1=[i[0] for i in e]
        print(L1)
        self.combo.config(values=L1)
        

        
        
    
        self.l10=Label(self.t2,text="Charge",bg="#ebcad2",font=("Helvetica",12,font.ITALIC)).place(x=600,y=200)
        self.rate=StringVar()
        self.e9=ttk.Entry(self.t2,textvariable=self.rate)
        self.e9.place(x=670,y=200)
    
        self.btninsert=ttk.Button(self.t2,text="INSERT",command=self.action,state=DISABLED)
        self.btninsert.place(x=900,y=200)
        
        
        self.fr1=LabelFrame(self.t2,text="Amount Details",bg="#0067C6",fg="#ebcad2",font=("Helvetica",11,font.BOLD))
        #self.fr1.grid(row=3,column=0,padx=900,pady=250)
        self.fr1.place(x=900,y=250)
        
        l11=Label(self.fr1,text="No. of Test",bg="#0067C6",fg="#ebcad2",font=("Helvetica",11,font.BOLD)).grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.v1=IntVar()
        self.e11=Entry(self.fr1,textvariable=self.v1)
        self.e11.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        l12=Label(self.fr1,text="ToTal Cost",bg="#0067C6",fg="#ebcad2",font=("Helvetica",11,font.BOLD)).grid(row=1,column=0,padx=5,pady=5,sticky=W)
        self.v2=IntVar()
        self.e12=Entry(self.fr1,textvariable=self.v2)
        self.e12.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        l13=Label(self.fr1,text="CGST(6.5%)",bg="#0067C6",fg="#ebcad2",font=("Helvetica",11,font.BOLD)).grid(row=2,column=0,padx=5,pady=5,sticky=W)
        self.v3=IntVar()
        self.e13=Entry(self.fr1,textvariable=self.v3)
        self.e13.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        
        l14=Label(self.fr1,text="SGST(6.5%)",bg="#0067C6",fg="#ebcad2",font=("Helvetica",11,font.BOLD)).grid(row=3,column=0,padx=5,pady=5,sticky=W)
        self.v4=IntVar()
        self.e14=Entry(self.fr1,textvariable=self.v4)
        self.e14.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        l15=Label(self.fr1,text="Payable Amount",bg="#0067C6",fg="#ebcad2",font=("Helvetica",11,font.BOLD)).grid(row=4,column=0,padx=5,pady=5,sticky=W)
        self.v5=IntVar()
        self.e15=Entry(self.fr1,textvariable=self.v5)
        self.e15.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
    
        self.tree1=ttk.Treeview(self.t2,height=15,columns=10)
        self.tree1['show']='headings'
        self.tree1['columns']=['Test Name','Rate','NO.of days','Delivery Date']
        self.tree1.grid(row=3,column=0,sticky=(N,S,W),padx=5,columnspan=5)   
    
        for i in range(4):
            self.tree1.heading(i,text='{}'.format(self.tree1['columns'][i]))
            self.tree1.column(i,anchor=CENTER)
    
        self.scrol1=ttk.Scrollbar(self.t2,orient=VERTICAL,command=self.tree1.yview)
        self.tree1['yscrollcommand']=self.scrol1.set
        self.scrol1.grid(row=3,column=1,sticky=(N,S,W),padx=597)
        
        
        
        btnconfirm=ttk.Button(self.t2,text="Confirm",command=self.confirm).place(x=900,y=500)
        
        btncancel=ttk.Button(self.t2,text="Cancel",command=self.cancel).place(x=1060,y=500)
        
        self.btnexit=ttk.Button(self.t2,text="Exit",command=self.exittt).place(x=980,y=550)
    
        self.combo.bind("<<ComboboxSelected>>",lambda a:self.Comboclick("Test"))
        self.c.close()
        self.createtable()

        self.t2.mainloop() 
        
        
        
    def createtable(self):
        self.c.close()
        self.c=self.cur.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS patient(pname TEXT primary key,doctor TEXT, phno INTEGER, address TEXT,age INTEGER)")
        self.c.execute("CREATE TABLE IF NOT EXISTS orderdetails(OID TEXT primary key, orderdate DATE, pname TEXT, total_amount INTEGER, nooftest INTEGER, FOREIGN KEY(pname) REFERENCES patient)")
        self.c.execute("CREATE TABLE IF NOT EXISTS testdetails(OID TEXT,testdate DATE, testname TEXT , cost INTEGER, FOREIGN KEY(OID) REFERENCES orderdetails)")
        
        
        
    def Comboclick(self,a):
        name=self.com.get()
        #print(name)
        self.c.close()
        self.c=self.cur.cursor()
        self.rate.set("")
        #query="select cost from pathology where tame='%s'"%name
        val1=self.c.execute("select cost from pathology where tame='%s'"%name)
        val1=self.c.fetchone()
        self.e9.insert(0,val1)
        self.btninsert.config(state=NORMAL)
        
        
        
        
    def action(self):
        self.c=self.cur.cursor()
        name=self.com.get()
        charge=self.e9.get()
        query=self.c.execute("select nodays from pathology where tame='%s'"%name).fetchone()
        
        now=date.today()
        days1=[i for i in query]
        print(days1)
        print(now)
        time=now+datetime.timedelta(days=days1[0])
        print(time)
        
        
        self.tree1.insert('',0,values=(name,charge,query,time))
        self.com.set("Test")
        self.rate.set("")
        self.c.close()
        val=self.v1.get()
        val+=1
        self.v1.set(val)
        self.e11.config(state=DISABLED)
        
        val2=self.v2.get()
        val2+=int(charge)
        print(val2)
        self.v2.set(val2)
        
        val3=self.v3.get()
        val3=val2
        val3=(val3*0.065)
        print(val3)
        self.v3.set(val3)
        self.v4.set(val3)
        

        total=self.v5.get()
        total=val3+val3+val2
        self.v5.set(total)
        
        
        
    def confirm(self):
        patient=self.e5.get()
        phno=self.e6.get()
        add=self.e7.get(1.0,END)
        doc=self.e4.get()
        Age=self.e8.get()
        
        
        total=self.v5.get()
        Testno=self.v1.get()
        
        orderid=self.e1.get()
        date=self.e2.get()
        
        self.c.close()
        self.c=self.cur.cursor()
        Testname=[]
        cost=[]
        x=self.tree1.get_children()
        print(x)
        for i in x:
            record=self.tree1.item(i)['values']
            Testname.append(record[0])
            cost.append(record[1])
            
        print(Testname,cost)
            
       
        
        self.c.execute("INSERT INTO patient VALUES(?,?,?,?,?)",(patient,doc,phno,add,Age))
        self.c.execute("INSERT INTO orderdetails VALUES(?,?,?,?,?)",(orderid,date,patient,total,Testno))
        for i in range(len(Testname)):
              self.c.execute("INSERT INTO testdetails VALUES(?,?,?,?)",(orderid,date,Testname[i],cost[i]))
        self.cur.commit()
        self.c.close()
        
        
    def cancel(self):
        self.orderid.set(0)
        self.testdate.set("")
        self.pname.set("")
        self.docname.set("")
        self.address.set("")
        self.contact.set(0)
        self.age.set("")
        self.com.set("Test")
        self.rate.set("")
        self.v1.set(0)
        self.v2.set(0)
        self.v3.set(0)
        self.v4.set(0)
        self.v5.set(0)
        self.e7.delete(1.0,END)
        
        x=self.tree1.get_children()
        for i in x:
            self.tree1.delete(i)
            
            
    def exittt(self):
        self.t2.destroy()
        
        
       
        
        
    
        
        
        
        
        
        

    

#booking()

        
