#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter.ttk import Combobox,Treeview,Scrollbar,Style
import sqlite3
from tkinter import ttk

# In[2]:


win=Tk()
win.title('Bank Account Automation')
win.state('zoomed')
win.configure(bg='powder blue')
win.resizable(width=False,height=False)
title=Label(win,text='Bank Account Automation',font=('Arial',40,'underline','bold'),bg='powder blue')
title.pack()

def home_screen():
    frm=Frame(win)
    frm.configure(bg='green')
    frm.place(x=0,y=80,relwidth=1,relheight=.92)
    
    
    def fp():
        frm.destroy()
        forget_pass_screen()
        
    def cr_acc():
        frm.destroy()
        create_account_screen()
        
    def login():
        ac=e_acn.get()
        ps=e_password.get()
        if(len(ac)==0 or len(ps)==0):
            messagebox.showwarning('Validation','Plz fill both field')
            return
        elif(not ac.isdigit()):
            messagebox.showwarning("Validation","Acc No must be in digit")
            return
        else:
            con=sqlite3.connect(database="bank.sqlite")
            cur=con.cursor()
            cur.execute("select * from account where Account_number=? and password=?",(ac,ps))
            global row
            row=cur.fetchone()
            if(row==None):
                messagebox.showerror("Invalid","Invalid Account No/Password")
            else:
                row=list(row)
                frm.destroy()
                login_screen()
    def reset():
        e_acn.delete(0,"end")
        e_password.delete(0,"end")
        e_acn.focus()    
        
    lbl_acn=Label(frm,text='Account number :-',font=('Arial',20,'bold'),bg='green')
    lbl_acn.place(relx=.3,rely=.1)
    
    e_acn=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_acn.place(relx=.48,rely=.1)
    e_acn.focus()
    
    lbl_password=Label(frm,text='Password :-',font=('Arial',20,'bold'),bg='green')
    lbl_password.place(relx=.3,rely=.25)
    
    e_password=Entry(frm,font=('Arial',20,'bold'),bd=5,show='*')
    e_password.place(relx=.48,rely=.25) 
    
    btn_login=Button(frm,text='login',font=('Arial',18,'bold'),bd=4,command=login)
    btn_login.place(relx=.4,rely=.4)
    
    btn_reset=Button(frm,text='reset',font=('Arial',18,'bold'),bd=4,command=reset)
    btn_reset.place(relx=.47,rely=.4)
    
    btn_fg=Button(frm,text='forgot password',font=('Arial',18,'bold'),bd=4,width=16,command=fp)
    btn_fg.place(relx=.38,rely=.52)
    
    btn_new=Button(frm,text='open new account',font=('Arial',18,'bold'),bd=4,width=19,command=cr_acc)
    btn_new.place(relx=.36,rely=.63)
    

def forget_pass_screen():
    frm=Frame(win)
    frm.configure(bg='green')
    frm.place(x=0,y=80,relwidth=1,relheight=.92)
    
    def back():
        frm.destroy()
        home_screen()
        
    def get():
        acn=e_acn.get()
        mob=e_phone.get()
        email=e_email.get()
    
        con=sqlite3.connect(database="bank.sqlite")
        cur=con.cursor()
        cur.execute("select password from account where Account_number=? and email=? and mob=?",(acn,email,mob))
        pwd=cur.fetchone()
        if(pwd==None):
            messagebox.showerror("invalid","Invalid details")
        else:
            messagebox.showinfo("Password",f"Your Password :-{pwd[0]}")
        e_acn.delete(0,"end")
        e_phone.delete(0,"end")
        e_email.delete(0,"end")
        e_acn.focus()
    
    btn_back=Button(frm,text='back',font=('Arial',16,'bold'),bd=4,command=back)
    btn_back.place(relx=0,rely=0)
    
    lbl_acn=Label(frm,text='Account number :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_acn.place(relx=.25,rely=.15)
    
    e_acn=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_acn.place(relx=.45,rely=.15)
    e_acn.focus()
    
    lbl_phone=Label(frm,text='Phone number :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_phone.place(relx=.25,rely=.3)
    
    e_phone=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_phone.place(relx=.45,rely=.3)
    
    lbl_email=Label(frm,text='Email :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_email.place(relx=.25,rely=.45)
    
    e_email=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_email.place(relx=.45,rely=.45)
    
    btn_genpass=Button(frm,text='Get password',font=('Arial',18,'bold'),bd=4,width=19,command=get)
    btn_genpass.place(relx=.37,rely=.59)

def create_account_screen():
    frm=Frame(win)
    frm.configure(bg='green')
    frm.place(x=0,y=80,relwidth=1,relheight=.92)
    
    def backcr():
        frm.destroy()
        home_screen()
        
    def create():
        name=e_name.get()
        mob=e_phone.get()
        email=e_email.get()
        pwd=e_password.get()
        bal=e_bal.get()
        if(len(name)==0 or len(mob)==0 or len(email)==0 or len(pwd)==0 or len(bal)==0):
            messagebox.showwarning('Validation','Plz fill the required fields')
            return
        elif(not mob.isdigit()):
            messagebox.showwarning("Validation","Phone No must be in digit")
            return
        else:
            con=sqlite3.connect(database="bank.sqlite")
            cur=con.cursor()
            cur.execute("insert into account(Name,Mob,Email,password,balance) values(?,?,?,?,?)",(name,mob,email,pwd,bal))
            con.commit()
            con.close()
        
            con=sqlite3.connect(database="bank.sqlite")
            cur=con.cursor()
            cur.execute("select max(Account_number)from account")
            tup=cur.fetchone()
            con.close()
            messagebox.showinfo("Success",f"Your Account opend with Account No :-{tup[0]}")
            e_name.delete(0,"end")
            e_email.delete(0,"end")
            e_phone.delete(0,"end")
            e_password.delete(0,"end")
            e_bal.delete(0,"end")
            home_screen()
            return
    
    btn_backcr=Button(frm,text='back',font=('Arial',16,'bold'),bd=4,command=backcr)
    btn_backcr.place(relx=0,rely=0)
    
    lbl_name=Label(frm,text='Name :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_name.place(relx=.25,rely=.15)
    
    e_name=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_name.place(relx=.45,rely=.15)
    e_name.focus()
    
    lbl_phone=Label(frm,text='Phone number :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_phone.place(relx=.25,rely=.25)
    
    e_phone=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_phone.place(relx=.45,rely=.25)
    
    lbl_email=Label(frm,text='Email :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_email.place(relx=.25,rely=.35)
    
    e_email=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_email.place(relx=.45,rely=.35)
    
    lbl_password=Label(frm,text='Password :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_password.place(relx=.25,rely=.45)
    
    e_password=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_password.place(relx=.45,rely=.45)
    
    lbl_bal=Label(frm,text='Balance :-',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_bal.place(relx=.25,rely=.55)
    
    e_bal=Entry(frm,font=('Arial',20,'bold'),bd=4)
    e_bal.place(relx=.45,rely=.55)
    
    btn_open_acc=Button(frm,text='Open Account',font=('Arial',18,'bold'),bd=4,width=19,command=create)
    btn_open_acc.place(relx=.37,rely=.67)
    
def login_screen():
    frm=Frame(win)
    frm.configure(bg='green')
    frm.place(x=0,y=80,relwidth=1,relheight=.92)
    
    def logout():
        frm.destroy()
        home_screen()
        
    def profile():
        ifrm=Frame(frm)
        ifrm.configure(bg="Silver")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        con=sqlite3.connect(database="bank.sqlite")
        cur=con.cursor()
        cur.execute("select * from account where Account_number=?",(row[0],))
        ckbl=cur.fetchone()
        ckblacc=ckbl[0]
        lbl_ckbl=Label(ifrm,text=f'Acc No :-',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.15,rely=.15)
        lbl_ckbl=Label(ifrm,text=f'{ckblacc}',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.43,rely=.15)
        
        ckblname=ckbl[1]
        
        lbl_ckbl=Label(ifrm,text=f'Name :-',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.15,rely=.25)
        lbl_ckbl=Label(ifrm,text=f'{ckblname}',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.43,rely=.25)
        
        ckblmob=ckbl[2]
        
        lbl_ckbl=Label(ifrm,text=f'Phone No :-',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.15,rely=.35)
        lbl_ckbl=Label(ifrm,text=f'{ckblmob}',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.43,rely=.35)
        
        ckblemail=ckbl[3]
        
        lbl_ckbl=Label(ifrm,text=f'Email :-',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.15,rely=.45)
        lbl_ckbl=Label(ifrm,text=f'{ckblemail}',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.43,rely=.45)
        
        ckblpass=ckbl[4]
        
        lbl_ckbl=Label(ifrm,text=f'password :-',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.15,rely=.55)
        lbl_ckbl=Label(ifrm,text=f'{ckblpass}',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.43,rely=.55)
        
        ckblbal=ckbl[5]
        
        lbl_ckbl=Label(ifrm,text=f'Balance :-',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.15,rely=.65)
        lbl_ckbl=Label(ifrm,text=f'{ckblbal}',font=('Arial',17,'bold'),bd=7,bg='Silver')
        lbl_ckbl.place(relx=.43,rely=.65)
        
    def check():
        ifrm=Frame(frm)
        ifrm.configure(bg="#7FB3D5")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        con=sqlite3.connect(database="bank.sqlite")
        cur=con.cursor()
        cur.execute("select * from account where Account_number=?",(row[0],))
        ckbl=cur.fetchone()
        ckblball=ckbl[5]
        lbl_ckbl=Label(ifrm,text=f'Rs. {ckblball}',font=('Arial',35,'bold'),bd=7,fg='blue',bg='#7FB3D5')
        lbl_ckbl.place(relx=.35,rely=.25)
        lbl_ckbl=Label(ifrm,text=' Is your Current Balance.',font=('Arial',20,'bold'),bd=7,bg='#7FB3D5')
        lbl_ckbl.place(relx=.27,rely=.45)
        
    def deposit():
        ifrm=Frame(frm)
        ifrm.configure(bg="red")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        def amtd():
                dp=e_deposit.get()
                amt=float(e_deposit.get())
                dt=datetime.now()
                if(len(dp)==0):
                    messagebox.showwarning('Validation','Plz fill the given field')
                    return
                elif(not dp.isdigit()):
                    messagebox.showwarning("Validation","Amount must be in digit")
                    return
                else:
                    con=sqlite3.connect(database="bank.sqlite")
                    cur=con.cursor()
                    cur.execute("insert into txn values(?,?,?,?)",(row[0],amt,"Cr.",dt))
                    cur.execute("update account set balance=balance+? where Account_Number=?",(amt,row[0]))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success",f"{amt} Amount deposited")
                    e_deposit.delete(0,"end")
                    return
                
        lbl_deposit=Label(ifrm,text='Enter the Amount :-',font=('Arial',17,'bold'),bd=4,bg='red')
        lbl_deposit.place(relx=.15,rely=.33)
        
        e_deposit=Entry(ifrm,font=('Arial',20,'bold'),bd=4)
        e_deposit.place(relx=.48,rely=.33)
        e_deposit.focus()
        
        btn_dp=Button(frm,text='Deposit',font=('Arial',17,'bold'),width=10,bd=4,command=amtd)
        btn_dp.place(relx=.76,rely=.465)
        
    def withdraw():
        ifrm=Frame(frm)
        ifrm.configure(bg="yellow")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        def amtw():
                wt=e_withdraw.get()
                amt=float(e_withdraw.get())
                dt=datetime.now()
                if(len(wt)==0):
                    messagebox.showwarning('Validation','Plz fill the given field')
                    return
                elif(not wt.isdigit()):
                    messagebox.showwarning("Validation","Amount must be in digit")
                    return
                else:
                    con=sqlite3.connect(database="bank.sqlite")
                    cur=con.cursor()
                    cur.execute("select balance from account where Account_Number=?",(row[0],))
                    bal=cur.fetchone()
                    con.close()
                    if(bal[0]>amt):
                        con=sqlite3.connect(database="bank.sqlite")
                        cur=con.cursor()
                        cur.execute("insert into txn values(?,?,?,?)",(row[0],amt,"Cr.",dt))
                        cur.execute("update account set balance=balance-? where Account_Number=?",(amt,row[0]))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success",f"{amt} Amount Withdrawn")
                        e_withdraw.delete(0,"end")
                        return
                    else:
                        messagebox.showerror("Error","Insufficient Bal")
                        return
        
        lbl_withdraw=Label(ifrm,text='Enter the Amount :-',font=('Arial',17,'bold'),bd=4,bg='yellow')
        lbl_withdraw.place(relx=.15,rely=.33)
        
        e_withdraw=Entry(ifrm,font=('Arial',20,'bold'),bd=4)
        e_withdraw.place(relx=.48,rely=.33)
        e_withdraw.focus()
        
        btn_wd=Button(frm,text='Withdraw',font=('Arial',17,'bold'),width=10,bd=4,command=amtw)
        btn_wd.place(relx=.76,rely=.465)
        
    def transfer():
        ifrm=Frame(frm)
        ifrm.configure(bg="grey")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        def trns():
            trns_to=e_transfer_acc.get()
            trns_amt=e_transfer_amt.get()
            if(len(trns_to)==0 or len(trns_amt)==0):
                messagebox.showwarning('Validation','Plz fill the Both fields')
                return
            elif(not trns_to.isdigit() or not trns_amt.isdigit()):
                messagebox.showwarning("Validation","Amount must be in digit")
                return
            else:
                amt=float(e_transfer_amt.get())
                to=int(e_transfer_acc.get())
                dt=datetime.now()
                con=sqlite3.connect(database="bank.sqlite")
                cur=con.cursor()
                cur.execute("select * from account where Account_Number=?",(to,))
                tup=cur.fetchone()
                con.close()
                if(tup==None):
                    messagebox.showerror("Invalid","To account does not exist")
                    return
                else:
                    con=sqlite3.connect(database="bank.sqlite")
                    cur=con.cursor()
                    cur.execute("select balance from account where Account_Number=?",(row[0],))
                    bal=cur.fetchone()
                    con.close()
                    if(bal[0]>amt):
                        con=sqlite3.connect(database="bank.sqlite")
                        cur=con.cursor()
                        cur.execute("insert into txn values(?,?,?,?)",(row[0],amt,'Db.',dt))
                        cur.execute("insert into txn values(?,?,?,?)",(to,amt,'Cr.',dt))
                        cur.execute("update account set balance=balance-? where Account_Number=?",(amt,row[0]))
                        cur.execute("update account set balance=balance+? where Account_Number=?",(amt,to))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success",f"{amt} transfered successfully")
                        e_transfer_acc.delete(0,"end")
                        e_transfer_amt.delete(0,"end")
                        e_transfer_acc.focus()
                        return
                    else:
                        messagebox.showerror("Error","Insufficient Bal")
                        return
        
        lbl_acc=Label(ifrm,text='Enter Account No :-',font=('Arial',17,'bold'),bd=4,bg='grey')
        lbl_acc.place(relx=.12,rely=.25)
        
        e_transfer_acc=Entry(ifrm,font=('Arial',20,'bold'),bd=4)
        e_transfer_acc.place(relx=.48,rely=.25)
        e_transfer_acc.focus()
        
        lbl_amt=Label(ifrm,text='Enter the Amount :-',font=('Arial',17,'bold'),bd=4,bg='grey')
        lbl_amt.place(relx=.12,rely=.40)
        
        e_transfer_amt=Entry(ifrm,font=('Arial',20,'bold'),bd=4)
        e_transfer_amt.place(relx=.48,rely=.40)
        
        btn_wd=Button(frm,text='Transfer',font=('Arial',17,'bold'),width=10,bd=4,command=trns)
        btn_wd.place(relx=.758,rely=.535)

    def statement():
        ifrm=Frame(frm)
        ifrm.configure(bg="orange")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        tv=Treeview(ifrm)
        tv.place(relx=.13,rely=.2,relwidth=.75,height=200)
    
        st=Style()
        st.configure("Treeview.Heading",font=('Arial',16,'bold'),foreground='brown')
    
        sb=Scrollbar(frm,orient="vertical",command=tv.yview)
        sb.place(relx=.858,rely=.2565,height=200)
        tv.configure(yscrollcommand=sb.set)
    
        tv['columns']=['1','2','3']
        tv['show']='headings'
  
        tv.column('1',anchor='c',width=250)
        tv.column('2',anchor='w',width=150)
        tv.column('3',anchor='w',width=150)
    
    
        tv.heading('1',text="Date/Time")
        tv.heading('2',text="Amount")
        tv.heading('3',text="Type (Db./Cr.)")
        
        con=sqlite3.connect(database='bank.sqlite')
        cur=con.cursor()
        cur.execute("select * from account where Account_number=?",(row[0],))
        fet=cur.fetchone()
        cur.execute("select * from txn where Account_number=?",(fet[0],))
        ucount=0
        for fet in cur:
            ucount+=1
            tv.insert("","end",values=(fet[3],fet[1],fet[2]))     
        stat_lbl=Label(frm,text=f"Total statement:{ucount}",font=('Arial',30,'bold'),fg='blue',bg='orange')
        stat_lbl.place(relx=.55,rely=.18)
        con.close()
        
    def update():
        ifrm=Frame(frm)
        ifrm.configure(bg="purple")
        ifrm.place(relx=.42,rely=.10,relwidth=.5,relheight=.79)
        
        def upd():
            name=e_name.get()
            mob=e_mob.get()
            email=e_email.get()
            pwd=e_pass.get()
            
            con=sqlite3.connect(database="bank.sqlite")
            cur=con.cursor()
            cur.execute("update account set Name=?,Mob=?,Email=?,password=? where Account_number=?",(name,mob,email,pwd,row[0]))
            con.commit()
            con.close()
            messagebox.showinfo("Update","Profile Updated")
            row[1]=name
            row[2]=mob
            row[3]=email
            row[4]=pwd
            
            frm.destroy()
            login_screen()
                    
        lbl_name=Label(frm,text="Name :-",font=('Arial',20,'bold'),bg='purple')
        lbl_name.place(relx=.47,rely=.2)

        e_name=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_name.place(relx=.65,rely=.2)
        e_name.focus()
        e_name.insert(0,row[1])

        lbl_mob=Label(frm,text="Phone number :-",font=('Arial',20,'bold'),bg='purple')
        lbl_mob.place(relx=.47,rely=.3)

        e_mob=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_mob.place(relx=.65,rely=.3)
        e_mob.insert(0,row[2])
        
        lbl_email=Label(frm,text="Email :-",font=('Arial',20,'bold'),bg='purple')
        lbl_email.place(relx=.47,rely=.4)

        e_email=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_email.place(relx=.65,rely=.4)
        e_email.insert(0,row[3])
        
        lbl_pass=Label(frm,text="Password :-",font=('Arial',20,'bold'),bg='purple')
        lbl_pass.place(relx=.47,rely=.5)

        e_pass=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_pass.place(relx=.65,rely=.5)
        e_pass.insert(0,row[4])

        btn_get=Button(frm,text="Update",font=('Arial',18,'bold'),bd=4,width=13,command=upd)
        btn_get.place(relx=.71,rely=.615)
        
    
    btn_log=Button(frm,text='Logout',font=('Arial',16,'bold'),bd=4,command=logout)
    btn_log.place(relx=.94,rely=0)
    
    nn=row[1]
    
    lbl_wlc=Label(frm,text=f'Welcome,   {nn}',font=('Arial',20,'bold'),bd=4,bg='green')
    lbl_wlc.place(relx=.001,rely=0)
    
    btn_prof=Button(frm,text='Profile',font=('Arial',18,'bold'),bd=4,width=18,command=profile)
    btn_prof.place(relx=.13,rely=.10)
    
    btn_ckbal=Button(frm,text='Check balance',font=('Arial',18,'bold'),bd=4,width=18,command=check)
    btn_ckbal.place(relx=.13,rely=.22)
    
    btn_deposit=Button(frm,text='Deposit',font=('Arial',18,'bold'),bd=4,width=18,command=deposit)
    btn_deposit.place(relx=.13,rely=.34)
    
    btn_withdraw=Button(frm,text='Withdraw',font=('Arial',18,'bold'),bd=4,width=18,command=withdraw)
    btn_withdraw.place(relx=.13,rely=.46)
    
    btn_transfer=Button(frm,text='Transfer',font=('Arial',18,'bold'),bd=4,width=18,command=transfer)
    btn_transfer.place(relx=.13,rely=.58)

    btn_statement=Button(frm,text='Mini Statement',font=('Arial',18,'bold'),bd=4,width=18,command=statement)
    btn_statement.place(relx=.13,rely=.70)
    
    btn_update=Button(frm,text='Update',font=('Arial',18,'bold'),bd=4,width=18,command=update)
    btn_update.place(relx=.13,rely=.82)
    
home_screen()  
win.mainloop()


# In[ ]:


#con=sqlite3.connect(database="bank.sqlite")
#cur=con.cursor()
#cur.execute("create table account(Account_number integer primary key autoincrement,Name text,Mob text,Email text,password text,balance float)")
#con.commit()
#con.close()


# In[ ]:


#con=sqlite3.connect(database="bank.sqlite")
#cur=con.cursor()
#cur.execute("create table txn(Account_number integer,Amount float,txn_type text,txn_datetime datetime)")
#con.commit()
#con.close()

