from tkinter import*
from PIL import Image,ImageTk,ImageOps
import requests
from io import BytesIO
from tkinter import ttk #for stylish entry field
import random
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime

class Roombooking:
    def __init__(self,root) :
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #=====variables======#

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        #=====TITLE=====#
        lbl_title=Label(self.root,text="Room Booking",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #=====Logo======#
        url2 = 'https://static.wikia.nocookie.net/staypedia/images/1/1c/Taj_Hotels_logo.png/revision/latest/thumbnail/width/360/height/360?cb=20200214185939'  
        response = requests.get(url2)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        width, height = 100,40 
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        border_width = 2
        border_color = "silver"
        img = ImageOps.expand(img, border=border_width, fill=border_color)
        img2 = ImageTk.PhotoImage(img)
        labelImage = Label(self.root, image=img2)
        labelImage.img2 = img2  
        labelImage.place(x=5, y=2, width=width + 2 * border_width, height=height + 2 * border_width)

        #=====Label Frame=====#
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking details",font=("times new roman",12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=50,width=425,height=490)

         #=====Labels and entries=====#
        
        #Customer contact
        lbl_cust_contact=Label(labelFrameLeft,text="Customer contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_contact) 
        entry_contact.grid(row=0,column=1,sticky=W)

        #====Fetch data button=======#
        btnFetchData=Button(labelFrameLeft,text="Fetch data",command=self.Fetch_contact,font=("arial",9,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=346,y=4)

        #Check in date
        check_in_date=Label(labelFrameLeft,text="Check-in date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_checkin) 
        txtcheck_in_date.grid(row=1,column=1)

        #Check out date
        lbl_Check_out=Label(labelFrameLeft,text="Check-out date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)

        txt_Check_out=ttk.Entry(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_checkout) 
        txt_Check_out.grid(row=2,column=1)

        #Room type
        label_Roomtype=Label(labelFrameLeft,text="Room type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_Roomtype.grid(row=3,column=0,sticky=W)
        
        #pick room types from 'detials' table and column 'RoomType'
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
        my_cusror=conn.cursor()
        my_cusror.execute("select RoomType from details") 
        rows_of_roomType=my_cusror.fetchall()

        txt_Check_out=ttk.Combobox(labelFrameLeft,width=29,font=("arial",13,"bold"),state="readonly",textvariable=self.var_roomtype) 
        # txt_Check_out["value"]=("Single","Double","Delux")
        txt_Check_out["value"]=rows_of_roomType
   

        #Room Available
        lblRoomAvailable=Label(labelFrameLeft,text="Available room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        # txtRoomAvailable=ttk.Entry(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_roomavailable) 
        # txtRoomAvailable.grid(row=4,column=1)

        # I want to pick rooms that are available from 'details' table made in mysql
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
        my_cusror=conn.cursor()
        my_cusror.execute("select RoomNo from details") 
        rows=my_cusror.fetchall()

        #Meal
        lblMeal=Label(labelFrameLeft,text="Meals:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=ttk.Combobox(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_meal)
        txtMeal["value"]=("With breakfast","Without breakfast")
        txtMeal.current(0) 
        txtMeal.grid(row=5,column=1)

        #No of days
        lblNoOfDays=Label(labelFrameLeft,text="No. of days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_noofdays) 
        txtNoOfDays.grid(row=6,column=1)
        
        #Sub total
        lblSub_total=Label(labelFrameLeft,text="Without tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSub_total.grid(row=8,column=0,sticky=W)

        txtSub_total=ttk.Entry(labelFrameLeft,width=29,font=("arial",13,"bold"),textvariable=self.var_actualtotal) 
        txtSub_total.grid(row=8,column=1)

        #Tax amount to be paid
        lblTax_paid=Label(labelFrameLeft,text="GST levied(5%):",font=("arial",12,"bold"),padx=2,pady=6)
        lblTax_paid.grid(row=7,column=0,sticky=W)

   

        #Total cost
        lblTotal_cost=Label(labelFrameLeft,text="Total cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotal_cost.grid(row=9,column=0,sticky=W)

        

         #====Button Bill======#

        btnBill=Button(labelFrameLeft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.total_days)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

         #====Btns=======#
    
        btn_frame=Frame(labelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.update)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.mDelete)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.reset)
        btnReset.grid(row=0,column=3,padx=1)

        #=====Top room image=====#

        url3 = 'https://www.holidify.com/images/cmsuploads/compressed/17072016_20221124202834.jpg'  
        response = requests.get(url3)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        width, height = 520,290
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        border_width = 2
        border_color = "silver"
        img = ImageOps.expand(img, border=border_width, fill=border_color)
        img3 = ImageTk.PhotoImage(img)
        labelImage = Label(self.root, image=img3)
        labelImage.img3 = img3  
        labelImage.place(x=760, y=55, width=width + 2 * border_width, height=height + 2 * border_width)  # Place the image

         #=======Table frame search system======#
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search system",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly",textvariable=self.search_var)
        combo_Search["value"]=("contact","roomavailable")
        combo_Search.current(0) #want 0th index element to be displayed as default
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.mob_search=StringVar()
        txtMob=ttk.Entry(Table_Frame,width=24,font=("arial",13,"bold"),textvariable=self.mob_search)
        txtMob.grid(row=0,column=2,padx=2)


        btnSearch=Button(Table_Frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10,command=self.search) #search values from mysql and show in window
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show all",font=("arial",11,"bold"),bg="black",fg="gold",width=10,command=self.fetch_data) #fetch data from mysql
        btnShowAll.grid(row=0,column=4,padx=1)


        #======Show data table=======#

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=185)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","NoOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) #just a variable to access local instances

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in date")
        self.room_table.heading("checkout",text="Check-out date")
        self.room_table.heading("roomtype",text="Room type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("NoOfdays",text="No.of days")
        
        self.room_table["show"]="headings"
        
        #to set column width of each
        self.room_table.column("contact",width=80)
        self.room_table.column("checkin",width=80)
        self.room_table.column("checkout",width=80)
        self.room_table.column("roomtype",width=80)
        self.room_table.column("roomavailable",width=80)
        self.room_table.column("meal",width=80)
        self.room_table.column("NoOfdays",width=80)
        
        #to display heading on the screen
        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error! All fields required.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
                my_cusror=conn.cursor()
                my_cusror.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(), self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get()))
                
                conn.commit()
                self.fetch_data() #n the add_data function, the fetch_data function is called after inserting a new record into the database. fetch_data function is called to retrieve the latest data from the room table.The fetch_data function fetches all records from the room table and updates the TreeView widget in your Tkinter application

                conn.close()
                messagebox.showinfo("Success","Room has been booked",parent=self.root)
             #we want message box to show in this window only,so we use parent=self.root..otherwise it will open in other window
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)    


    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Please enter contact number!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
            my_cusror=conn.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),) #',' ensures it is a tuple and self.var_contact.get() retrieves the value of self.var_contact, which is a StringVar associated with the customer's contact number
            my_cusror.execute(query,value) #The value tuple replaces the %s placeholder in the query with the actual contact number provided by the user.
            row=my_cusror.fetchone()

            conn.commit()
            conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #====Gender======#
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
                my_cusror=conn.cursor()
                query=("select gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cusror.execute(query,value)
                row=my_cusror.fetchone()

                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #====email======#
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
                my_cusror=conn.cursor()
                query=("select email from customer where mobile=%s")
    
                lblemail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #====Nationality======#
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
                my_cusror=conn.cursor()
                query=("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cusror.execute(query,value)
                row=my_cusror.fetchone()

                lblNationality=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #====Address======#
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
                my_cusror=conn.cursor()
                query=("select address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cusror.execute(query,value)
                row=my_cusror.fetchone()

                lbladdress=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl4=Label(showDataFrame,text=row[0],font=("arial",12,"bold")) #accessing only 0th element from the ruple so i used row[0]
                lbl4.place(x=90,y=120)
    
    #==fetch data from mysql to tkinter window
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
        my_cusror=conn.cursor()
        my_cusror.execute("select * from room") #display table
        rows=my_cusror.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children()) #delete exisitng data and then add new data,clear TreeView of old data
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
       
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error,mobile number not found",parent=self.root)
        else:   
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
            my_cusror=conn.cursor()
            my_cusror.execute("UPDATE room SET check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s WHERE contact=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get(),self.var_contact.get()))#columns names as in mysql table

            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Update","Room details have been updated successfully.",parent=self.root)
            conn.close()

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel management system","Do you want to delete this Room ?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@123",database="hotel_management_system")
            my_cusror=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cusror.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
            self.var_contact.set(""),
            self.var_checkin.set(""),
            self.var_checkout.set(""),
            self.var_meal.set(""),
            self.var_roomavailable.set(""),
            self.var_roomtype.set(""),
            self.var_noofdays.set(""),
            self.var_paidtax.set(""),
            self.var_actualtotal.set(""),
            self.var_total.set("")
    
    def total_days(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()

        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")

        self.var_noofdays.set(abs(outDate-inDate).days)

        rate_bf=800 #with breakfast rate
        rate_withoutbf=500 #rate without breakfast
        num_days=int(self.var_noofdays.get())#number of days
        
        if(self.var_meal.get()=="With breakfast"):
             
            room_rate=0
            if(self.var_roomtype.get()=="Delux"):
               room_rate=5000
            elif(self.var_roomtype.get()=="Single"):
                room_rate=1500
            elif(self.var_roomtype.get()=="Double"):
                room_rate=2500

            tot_room_meal=rate_bf+room_rate # cost of room and meal

            actual_total=tot_room_meal*num_days # Set the actual total cost
            paid_tax = tot_room_meal * 0.05  # Calculate at 5% tax
            
            total = paid_tax + actual_total  # Total cost including tax

        elif(self.var_meal.get()=="Without breakfast"):

            room_rate=0
            if(self.var_roomtype.get()=="Delux"):
               room_rate=5000
            elif(self.var_roomtype.get()=="Single"):
                room_rate=1500
            elif(self.var_roomtype.get()=="Double"):
                room_rate=2500

            tot_room_meal=rate_withoutbf+room_rate 

            actual_total=tot_room_meal*num_days 
            paid_tax = tot_room_meal * 0.05  
            
            total = paid_tax + actual_total  

        # Format and set the variables with "Rs."
        self.var_paidtax.set(f"Rs. {paid_tax:.2f}")
        self.var_actualtotal.set(f"Rs. {actual_total:.2f}")
        self.var_total.set(f"Rs. {total:.2f}")
    
    #search system -coded in table frame search system above ,btnSearch
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="hotel_management_system")
        my_cursor = conn.cursor()
        search_field = self.search_var.get()
        search_value = self.mob_search.get()
        query = f"SELECT * FROM room WHERE {search_field} LIKE %s"
        value = ("%" + search_value + "%",)
        # "%" + search_value + "%" surrounds search_value with % characters ,This matches any value that contains search_value anywhere in the text. Ex: If search_value is 123, %123% will match 0123456789, 123, abc123xyz, etc.

    



if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
