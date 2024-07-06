from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageOps
import requests
from io import BytesIO
from tkinter import ttk #for stylish entry field
import random
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import mysql.connector

from hotel import HotelManagementSystem
from register import Register 

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

       # =====Background======#
        url1 = 'https://media.architecturaldigest.com/photos/55e79526302ba71f3017f9ec/1:1/w_424,h_424,c_limit/dam-images-homes-2008-09-taj-hosl01_taj.jpg'
        response = requests.get(url1)
        img_data = response.content
        self.img = Image.open(BytesIO(img_data))
        # Resize image to fit the initial window size
        img_resized = self.img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img_resized)  # Store it as an instance variable
        self.lbl_bg = tk.Label(self.root, image=self.img_tk)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        # Update image size dynamically to fit the window
        self.root.bind("<Configure>", self.resize_image)


        frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        #=====Login logo======#
        url2 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBNYHBfUfHrvvxot_Hzofa5UQ-90k3nKxtkQ&usqp=CAU'  
        response = requests.get(url2)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        width, height = 100,100
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        border_width = 2
        border_color = "silver"
        img = ImageOps.expand(img, border=border_width, fill=border_color)
        img2 = ImageTk.PhotoImage(img)
        labelImage = Label(self.root, image=img2)
        labelImage.img2 = img2  
        labelImage.place(x=730, y=175)
        
        #Get strarted heading
        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=90,y=110)
        #Email/Username
        get_username=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        get_username.place(x=20,y=155)

        self.entry_username=ttk.Entry(frame,font=("arial",15,"bold")) 
        self.entry_username.place(x=140,y=155,width=150)

        #password
        get_password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        get_password.place(x=20,y=200)

        self.entry_password=ttk.Entry(frame,font=("arial",15,"bold"),show="*") 
        self.entry_password.place(x=140,y=200,width=150)

        btnLogin=Button(frame,text="Login",font=("times new roman",12,"bold"),bg="red",fg="white",width=9,bd=3,activeforeground="white",activebackground="red",command=self.login)
        btnLogin.place(x=120,y=250)

        btnRegister=Button(frame,text="Sign Up",command=self.register_window,font=("times new roman",12,"bold"),bg="black",fg="white",width=9,borderwidth=0,activeforeground="white",activebackground="red")
        btnRegister.place(x=65,y=300)
        #to change colour when hover on button
        btnRegister.bind("<Enter>", lambda e: self.on_enter(e, btnRegister))
        btnRegister.bind("<Leave>", lambda e: self.on_leave(e, btnRegister))

        btnForgotPass=Button(frame,text="Forgot password",command=self.forgot_password_window,font=("times new roman",12,"bold"),bg="black",fg="white",width=14,borderwidth=0,activeforeground="white",activebackground="red")
        btnForgotPass.place(x=155,y=300)
        btnForgotPass.bind("<Enter>", lambda e: self.on_enter(e, btnForgotPass))
        btnForgotPass.bind("<Leave>", lambda e: self.on_leave(e, btnForgotPass))

    def login(self):
        if(self.entry_username.get()=="" or self.entry_password.get()==""):
            messagebox.showerror("Error!","All fields required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
            my_cusror=conn.cursor()
            my_cusror.execute("select * from register where email=%s and password=%s",(self.entry_username.get(),self.entry_password.get()))
            row=my_cusror.fetchone()

            if row is None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("Yes or No","Welcome")
                if open_main:
                    self.new_window=Toplevel(self.root)#Passing self.root as an argument to Toplevel ensures that the new window is a child window of the main application window.
                    self.app=HotelManagementSystem(self.new_window) #the new instance of HotelManagementSystem will use self.new_window as its root window.
                else:
                    return
            conn.commit()
            conn.close()
    def reset_pass(self):
        if self.entry_username.get()=="":
            messagebox.showerror("Error","Plese fill the username",parent=self.root2)
        elif(self.entry_password.get()==""):
            messagebox.showerror("Error","Plese fill the password",parent=self.root2)
        elif(self.securityAns_entry.get()==""):
            messagebox.showerror("Error","Plese fill the security answer",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
            my_cusror=conn.cursor()
            query=("select * from register email=%s and securityQ=%s and securityA=%s")
            value=(self.entry_username.get(),self.combo_SecurityQ.get(),self.securityAns_entry.get(),)
            my_cusror.execute(query,value)
            row=my_cusror.fetchone()

            if row==None:
                messagebox.showerror("Error","Plese enter correct info.",parent=self.root2)
            else:
                query1=("UPDATE register SET password=%s where email=%s")
                value=(self.newPass_entry.get(),self.entry_username.get())
                my_cusror.execute(query1,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your credentials have been changed",parent=self.root2)
                self.root2.destroy()


    def forgot_password_window(self):
        if self.entry_username.get()=="":
            messagebox.showerror("Error","Enter email address")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
            my_cusror=conn.cursor()
            query=("SELECT * from register WHERE email=%s")
            value=(self.entry_username.get(),)
            my_cusror.execute(query,value)
            row=my_cusror.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid details")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)


                securityQ_lbl=Label(self.root2,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg='black')
                securityQ_lbl.place(x=50,y=80)
            
                self.combo_SecurityQ=ttk.Combobox(self.root2,font=("arial",15,"bold"),state="readonly")
                self.combo_SecurityQ["value"]=("Select","Your birth place","your nickname")
                self.combo_SecurityQ.current(0) 
                self.combo_SecurityQ.place(x=50,y=110,width=250)

                securityAns_lbl=Label(self.root2,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                securityAns_lbl.place(x=50,y=150)

                self.securityAns_entry=ttk.Entry(self.root2,font=("arial",15,"bold")) 
                self.securityAns_entry.place(x=50,y=180,width=250)

                newpassword_Lbl=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                newpassword_Lbl.place(x=50,y=220)

                self.newPass_entry=ttk.Entry(self.root2,font=("arial",15,"bold")) 
                self.newPass_entry.place(x=50,y=250,width=250)

                btnResetPass=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="darkgreen")
                btnResetPass.place(x=100,y=290)
    


    def register_window(self):
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)
        
    def on_enter(self, event, widget):
        widget['bg'] = 'red'

    def on_leave(self, event, widget):
        widget['bg'] = 'black'

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        img_resized = self.img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img_resized)  # Update instance variable
        self.lbl_bg.config(image=self.img_tk)
        self.lbl_bg.image = self.img_tk  # Keep a reference to avoid garbage collection



class Register:
        def __init__(self,root):
            self.root=root #name of window
            self.root.title("Register")
            self.root.geometry("1600x900+0+0")
            
            #==========variables==========#
            self.var_fname=StringVar()
            self.var_lname=StringVar()
            self.var_contact=StringVar()
            self.var_email=StringVar()
            self.var_securityQ=StringVar()
            self.var_securityA=StringVar()
            self.var_pass=StringVar()
            self.var_confpass=StringVar()

            #===background image======#
            url='https://images.rawpixel.com/image_social_landscape/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3Y5MDYtZ2liLTAwMjMuanBn.jpg'
            response = requests.get(url)
            img_data = response.content
            self.img = Image.open(BytesIO(img_data))
            # Resize image to fit the initial window size
            img_resized = self.img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(img_resized)  # Store it as an instance variable
            self.lbl_bg = tk.Label(self.root, image=self.img_tk)
            self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
            # Update image size dynamically to fit the window
            self.root.bind("<Configure>", self.resize_image) 


            #=====Left image======#
            url2 = 'https://i.pinimg.com/originals/e2/51/59/e25159f54c8d8c761ef20d57ef9bf93f.png'  
            response = requests.get(url2)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            width, height = 470,550
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            border_width = 1
            border_color = "white"
            img = ImageOps.expand(img, border=border_width, fill=border_color)
            img2 = ImageTk.PhotoImage(img)
            labelImage = Label(self.root, image=img2)
            labelImage.img2 = img2  
            labelImage.place(x=50, y=100)

            #===main fram====#
            frame=Frame(self.root,bg="white")
            frame.place(x=520,y=100,width=800,height=552)

            register_lbl=Label(frame,text="SIGN UP",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
            register_lbl.place(x=20,y=20)

            #===Label and entries====#

            #Row 1
            fname_lbl=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="white")
            fname_lbl.place(x=50,y=100)
        
            self.fname_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_fname) 
            self.fname_entry.place(x=50,y=130,width=250)

            lname_lbl=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white")
            lname_lbl.place(x=370,y=100)

            self.lname_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_lname) 
            self.lname_entry.place(x=370,y=130,width=250)

            #Row 2
            contact_lbl=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg='black')
            contact_lbl.place(x=50,y=170)
        
            self.contact_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_contact) 
            self.contact_entry.place(x=50,y=200,width=250)

            email_lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
            email_lbl.place(x=370,y=170)

            self.email_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_email) 
            self.email_entry.place(x=370,y=200,width=250)

            #Row 3
            securityQ_lbl=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg='black')
            securityQ_lbl.place(x=50,y=170)
        
            self.combo_SecurityQ=ttk.Combobox(frame,text="Security Question",font=("arial",15,"bold"),state="readonly",textvariable=self.var_securityQ)
            self.combo_SecurityQ["value"]=("Select","Your birth place","your nickname")
            self.combo_SecurityQ.current(0) 
            self.combo_SecurityQ.place(x=50,y=270,width=250)

            securityAns_lbl=Label(frame,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
            securityAns_lbl.place(x=370,y=240)

            self.securityAns_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_securityA) 
            self.securityAns_entry.place(x=370,y=270,width=250)

            #Row 4
            pswd_lbl=Label(frame,text="Enter new password",font=("times new roman",15,"bold"),bg="white",fg='black')
            pswd_lbl.place(x=50,y=310)
        
            self.pswd_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_pass) 
            self.pswd_entry.place(x=50,y=340,width=250)

            confirmPswd_lbl=Label(frame,text="Confirm password",font=("times new roman",15,"bold"),bg="white",fg="black")
            confirmPswd_lbl.place(x=370,y=310)

            self.confirmPswd_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_confpass) 
            self.confirmPswd_entry.place(x=370,y=340,width=250)

            #===Check Btn====#
            self.var_check=IntVar() #as its value is either 0 or 1
            checkBtn=Checkbutton(frame,variable=self.var_check,text="I agree to terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
            checkBtn.place(x=50,y=380)

            #===Button image sign up======#
            
            url3 = 'https://freepngimg.com/convert-png/24743-sign-up-button-transparent'
            response = requests.get(url3)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            width, height = 120, 50
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            border_width = 1
            border_color = "white"
            img = ImageOps.expand(img, border=border_width, fill=border_color)
            self.img_button = ImageTk.PhotoImage(img)

            b1 = Button(frame, image=self.img_button, borderwidth=0, cursor="hand2",command=self.register_data)
            b1.place(x=50, y=440)

            #===Button image login in======#
            
            url4 = 'https://strathostess.co.za/wp-content/uploads/2016/11/login-button-blue-i8.jpg'
            response = requests.get(url4)
            img_data = response.content
            img1 = Image.open(BytesIO(img_data))
            width, height = 150, 50
            img1 = img1.resize((width, height), Image.Resampling.LANCZOS)
            border_width = 1
            border_color = "white"
            img1 = ImageOps.expand(img1, border=border_width, fill=border_color)
            self.img_button1 = ImageTk.PhotoImage(img1)

            b2 = Button(frame, image=self.img_button1, borderwidth=0, cursor="hand2",command=self.return_login)
            b2.place(x=200, y=440)

        def return_login(self):
           self.root.destroy()

        def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error!","All fields are required.")
            elif(self.var_pass.get()!=self.var_confpass.get()):
                messagebox.showerror("Error","Confirm password must be same as password.")
            elif(self.var_check.get()==0):
                messagebox.showerror("Invalid","Please agree to terms and conditions.")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
                my_cusror=conn.cursor()
                query=("SELECT * from register where email=%s")
                value=(self.var_email.get(),)
                my_cusror.execute(query,value)
                row=my_cusror.fetchone()

                if(row!=None):
                    messagebox.showerror("Invalid","User already exists,try different email")
                else:
                    my_cusror.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Registered successfully")

        def resize_image(self, event):
            new_width = event.width
            new_height = event.height
            img_resized = self.img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(img_resized)  # Update instance variable
            self.lbl_bg.config(image=self.img_tk)
            self.lbl_bg.image = self.img_tk  # Keep a reference to avoid garbage collection


if __name__=="__main__":
    main()






