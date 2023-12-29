from tkinter import*
from tkinter import font
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class Patient_info:
    def __init__(self,master):
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("1000x500")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.pat_id = IntVar()
        self.pat_name = StringVar()
        self.pat_sex = StringVar()
        self.pat_DOB = StringVar()
        self.pat_BG = StringVar()
        self.pat_add = StringVar()
        self.pat_contact = IntVar()
        self.pat_email = StringVar()

        self.mainlbl = Label(self.frame,text='PATIENT REGISTRATION FORM',font='Helvetica 20 bold')
        self.mainlbl.grid(row=0,column=0,pady=30)

        self.Inner_frame1 = Frame(self.frame,width=500,height=250,bg='red',relief='ridge',bd=10)
        self.Inner_frame1.grid(row=1,column=0)
        self.Inner_frame2 = Frame(self.frame,width=500,height=50,bg='red',relief='ridge',bd=10)
        self.Inner_frame2.grid(row=2,column=0)

        self.lbl1 = Label(self.Inner_frame1,text='Patient ID',font='Helvetica 15 bold')
        self.lbl1.grid(row=0,column=0,pady=10,padx=10)
        self.lbl1_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_id)
        self.lbl1_entry.grid(row=0,column=1,pady=10,padx=10)
        self.lbl2 = Label(self.Inner_frame1,text='Patient name',font='Helvetica 15 bold')
        self.lbl2.grid(row=0,column=2,pady=10,padx=10)
        self.lbl2_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_name)
        self.lbl2_entry.grid(row=0,column=3,pady=10,padx=10)
        self.lbl3 = Label(self.Inner_frame1,text='Sex',font='Helvetica 15 bold')
        self.lbl3.grid(row=1,column=0,pady=10,padx=10)
        self.lbl3_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_sex)
        self.lbl3_entry.grid(row=1,column=1,pady=10,padx=10)
        self.lbl4 = Label(self.Inner_frame1,text='Date Of Birth',font='Helvetica 15 bold')
        self.lbl4.grid(row=1,column=2,pady=10,padx=10)
        self.lbl4_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_DOB)
        self.lbl4_entry.grid(row=1,column=3,pady=10,padx=10)
        self.lbl5 = Label(self.Inner_frame1,text='Blood group',font='Helvetica 15 bold')
        self.lbl5.grid(row=2,column=0,pady=10,padx=10)
        self.lbl5_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_BG)
        self.lbl5_entry.grid(row=2,column=1,pady=10,padx=10)
        self.lbl6 = Label(self.Inner_frame1,text='Address',font='Helvetica 15 bold')
        self.lbl6.grid(row=2,column=2,pady=10,padx=10)
        self.lbl6_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_add)
        self.lbl6_entry.grid(row=2,column=3,pady=10,padx=10)
        self.lbl7 = Label(self.Inner_frame1,text='Contact Number',font='Helvetica 15 bold')
        self.lbl7.grid(row=3,column=0,pady=10,padx=10)
        self.lbl7_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_contact)
        self.lbl7_entry.grid(row=3,column=1,pady=10,padx=10)
        self.lbl8 = Label(self.Inner_frame1,text='Email address',font='Helvetica 15 bold')
        self.lbl8.grid(row=3,column=2,pady=10,padx=10)
        self.lbl8_entry = Entry(self.Inner_frame1,width=25,font='Helvetica 15 bold',textvariable=self.pat_email)
        self.lbl8_entry.grid(row=3,column=3,pady=10,padx=10)

        self.but1 = Button(self.Inner_frame2,text='SUBMIT',font='Helvetica 15 bold',width=10,command=self.submit)
        self.but1.grid(row=0,column=0)
        self.but2 = Button(self.Inner_frame2,text='UPDATE',font='Helvetica 15 bold',width=10,command=self.update)
        self.but2.grid(row=0,column=1)
        self.but3 = Button(self.Inner_frame2,text='SEARCH',font='Helvetica 15 bold',width=10,command=self.search)
        self.but3.grid(row=0,column=2)
        self.but4 = Button(self.Inner_frame2,text='DELETE',font='Helvetica 15 bold',width=10,command=self.delete)
        self.but4.grid(row=0,column=3)
        self.but5 = Button(self.Inner_frame2,text='EXIT',font='Helvetica 15 bold',width=10,command=self.exit)
        self.but5.grid(row=0,column=4)

    def submit(self):
        global aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        a1 = (self.pat_id.get())
        a2 = (self.pat_name.get())
        a3 = (self.pat_sex.get())
        a4 = (self.pat_DOB.get())
        a5 = (self.pat_BG.get())
        a6 = (self.pat_add.get())
        a7 = (self.pat_contact())
        a8 = (self.pat_email())
        a = list(cursor.execute('select * from PATIENT_INFO where Patient_ID = ?',(a1,)))
        x = len(a)
        if x!=0:
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","PATIENT_ID ALREADY EXIST")
        else:
            cursor.execute('insert into PATIENT_INFO values(?,?,?,?,?,?,?,?)',(a1,a2,a3,a4,a5,a6,a7,a8))
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","DETAILS SUBMITTED INTO DATABASE")

        conn.commit()

    def update(self):
        global b1,b2,b3,b4,b5,b6,b7,b8
        cursor = conn.cursor()
        conn = sqlite3.connect("HMSDB.db")
        b1 = (self.pat_id.get())
        b2 = (self.pat_name.get())
        b3 = (self.pat_sex.get())
        b4 = (self.pat_DOB.get())
        b5 = (self.pat_BG.get())
        b6 = (self.pat_add.get())
        b7 = (self.pat_contact())
        b8 = (self.pat_email())
        a = list(cursor.execute('select * from PATIENT_INFO where Patient_ID = ?',(b1,)))
        if len(b)!=0:
            cursor.execute('update PATIENT_INFO set PATIENT_NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONTACT_NO=?,EMAIL=? where PATIENT_ID=?',(b2,b3,b4,b5,b6,b7,b8,b1))
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","DETAILS UPDATED INTO DATABASE")
            conn.commit()
        else:
            tkinter.messagebox.showinfo("HEALTHCARE DATABASE SYSTEM","PATIENT_ID DOES NOT EXIST")

    def search(self):
        self.newWindow = Toplevel(self.master)
        self.app = Search_pat(self.newWindow)

    def delete(self):
        self.newWindow = Toplevel(self.master)
        self.app = Del_pat(self.newWindow)

    def exit(self):
        self.master.destroy()


class Search_pat:
    def __init__(self,master):
        global c,s_pat_id
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("1000x500")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.s_pat_id = IntVar()

        self.mainlbl = Label(self.frame,text='SEARCH WINDOW',font='Helvetica 20 bold')
        self.mainlbl.grid(row=0,column=0,pady=25)  

        self.Inner_frame = Frame(self.frame,width=800,height=400,bg='red',relief='ridge',bd=10)
        self.Inner_frame.grid(row=1,column=0)
        self.Inner_frame2 = Frame(self.frame,width=100,height=50,bg='red',relief='ridge',bd=10)
        self.Inner_frame2.grid(row=2,column=0)

        self.lbl1 = Label(self.Inner_frame,text='Enter patient ID',font='Helvetica 15 bold',bg='red')  
        self.lbl1.grid(row=0,column=0,padx=10)
        self.lbl1_entry = Entry(self.Inner_frame,width=20,font='Helvetica 15 bold',textvariable=self.s_pat_id)
        self.lbl1_entry.grid(row=0,column=1)

        self.search_but = Button(self.Inner_frame2,text='SEARCH',font='Helvetica 15 bold',width=10,command=self.search_btn)
        self.search_but.grid(row=0,column=0)
    
    def search_btn(self):
        global c,s_pat_id,t,i,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10,lbl11,lbl12,lbl13,lbl14,lbl15,lbl16,lbl17
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        c = (self.s_pat_id.get())
        a = list(cursor.execute('select * from PATIENT_INFO where PATIENT_ID = ?',(c,)))
        if (len(a)==0):
            tkinter.messagebox.showerror("HEALTHCARE MANAGEMENT SYSTEM","PATIENT INFO NOT FOUND")
        else:
            t = cursor.execute('select * from PATIENT_INFO where PATIENT_ID = ?',(c,))
            for i in t:
                self.lbl2 = Label(self.Inner_frame,text='Patient ID',font='Helvetica 15 bold')
                self.lbl2.grid(row=1,column=0)
                self.lbl3 = Label(self.Inner_frame,text=i[0],font='Helvetica 15 bold')
                self.lbl3.grid(row=1,column=1)
                self.lbl4 = Label(self.Inner_frame,text='Patient Name',font='Helvetica 15 bold')
                self.lbl4.grid(row=1,column=2)
                self.lbl5 = Label(self.Inner_frame,text=i[1],font='Helvetica 15 bold')
                self.lbl5.grid(row=1,column=3)
                self.lbl6 = Label(self.Inner_frame,text='Sex',font='Helvetica 15 bold')
                self.lbl6.grid(row=2,column=0)
                self.lbl7 = Label(self.Inner_frame,text=i[2],font='Helvetica 15 bold')
                self.lbl7.grid(row=2,column=1)
                self.lbl8 = Label(self.Inner_frame,text='Date of Birth',font='Helvetica 15 bold')
                self.lbl8.grid(row=2,column=2)
                self.lbl9 = Label(self.Inner_frame,text=i[3],font='Helvetica 15 bold')
                self.lbl9.grid(row=2,column=3)
                self.lbl10 = Label(self.Inner_frame,text='Blood Group',font='Helvetica 15 bold')
                self.lbl10.grid(row=3,column=0)
                self.lbl11 = Label(self.Inner_frame,text=i[4],font='Helvetica 15 bold')
                self.lbl11.grid(row=3,column=1)
                self.lbl12 = Label(self.Inner_frame,text='Address',font='Helvetica 15 bold')
                self.lbl12.grid(row=3,column=2)
                self.lbl13 = Label(self.Inner_frame,text=i[5],font='Helvetica 15 bold')
                self.lbl13.grid(row=3,column=3)
                self.lbl14 = Label(self.Inner_frame,text='Contact_NO',font='Helvetica 15 bold')
                self.lbl14.grid(row=4,column=0)
                self.lbl15 = Label(self.Inner_frame,text=i[6],font='Helvetica 15 bold')
                self.lbl15.grid(row=4,column=1)
                self.lbl16 = Label(self.Inner_frame,text='Email',font='Helvetica 15 bold')
                self.lbl16.grid(row=4,column=2)
                self.lbl17 = Label(self.Inner_frame,text=i[7],font='Helvetica 15 bold')
                self.lbl17.grid(row=4,column=3)
            conn.commit()

class Del_pat:
    def __init__(self,master):
        global d
        self.master = master
        self.master.title("Healthcare Management System")
        self.master.geometry("800x400")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.d_pat_id = IntVar()

        self.mainlbl = Label(self.frame,text='DELETE WINDOW',font='Helvetica 20 bold')
        self.mainlbl.grid(row=0,column=0,pady=25)

        self.Inner_frame1 = Frame(self.frame,width=400,height=200,bg='red',relief='ridge',bd=10)
        self.Inner_frame1.grid(row=1,column=0)
        self.Inner_frame2 = Frame(self.frame,width=100,height=50,bg='red',relief='ridge',bd=10)
        self.Inner_frame2.grid(row=2,column=0)

        self.lbl = Label(self.Inner_frame1,text='Enter Patient ID',font='Helvetica 15 bold',bg='red')
        self.lbl.grid(row=0,column=0,padx=10)
        self.lbl_entry = Entry(self.Inner_frame1,width=20,font='Helvetica 15 bold',textvariable=self.d_pat_id)
        self.lbl_entry.grid(row=0,column=1)

        self.del_but = Button(self.Inner_frame2,text='DELETE',width=10,font='Helvetica 15 bold',command=self.del_btn)
        self.del_but.grid(row=0,column=0)

    def del_btn(self):
        global d,d_pat_id
        conn = sqlite3.connect("HMSDB.db")
        cursor = conn.cursor()
        d = (self.d_pat_id.get())
        a = list(cursor.execute('select * from PATIENT_INFO where PATIENT_ID = ?',(d,)))
        if (len(a)==0):
            tkinter.messagebox.showerror("HEALTHCARE MANAGEMENT SYSTEM","PATIENT INFO NOT FOUND")
        else:
            cursor.execute('Delete from PATIENT_INFO where PATIENT_ID = ?',(d))
            tkinter.messagebox.showinfo("HEALTHCARE MANAGEMENT SYSTEM","DETAILS DELETED FROM DATABASE")
            conn.commit()









        















