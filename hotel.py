from tkinter import*
from PIL import Image,ImageTk,ImageOps #pip install pillow
import requests
from io import BytesIO
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root): #root here is name of the window
        self.root=root  # root is assigned to self.root as this makes self.root an instance variable that can be accessed by other methods within the class.
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0") #set widthxHeight + x cordinate + y cordinate
        
         
         #============First Image===========#
         # URL of the image
        url1 = 'https://media.licdn.com/dms/image/C5612AQG9O99vMkm9bw/article-cover_image-shrink_600_2000/0/1520168310085?e=2147483647&v=beta&t=GM8Frm_5LMnypZ91Gl6ckD4HfwerifDuiIp0eU6BfXQ'  

        # Download the image
        response = requests.get(url1)
        if response.status_code == 200:
            img_data = response.content

            # Open the image with PIL
            img = Image.open(BytesIO(img_data))

            # Resize the image
            width, height = 1550, 140  # Set the desired width and height
            img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Add border
            border_width = 2
            border_color = "silver"
            img = ImageOps.expand(img, border=border_width, fill=border_color)

            # Use ImageTk to convert the PIL image to a Tkinter image
            img1 = ImageTk.PhotoImage(img)

            # Create a label to display the image
            labelImage = Label(self.root, image=img1)
            labelImage.img1 = img1  # Keep a reference to avoid garbage collection
            labelImage.place(x=0, y=0, width=width + 2 * border_width, height=height + 2 * border_width)  # Place the image

        else:
            print("Failed to retrieve image")

        #===========Logo image========#
        # URL of the logo image
        url2 = 'https://static.wikia.nocookie.net/staypedia/images/1/1c/Taj_Hotels_logo.png/revision/latest/thumbnail/width/360/height/360?cb=20200214185939'  

        # Download the image
        response = requests.get(url2)
        if response.status_code == 200:
            img_data = response.content

            # Open the image with PIL
            img = Image.open(BytesIO(img_data))

            # Resize the image
            width, height = 230, 140  # Set the desired width and height
            img = img.resize((width, height), Image.Resampling.LANCZOS)

            border_width = 2
            border_color = "silver"
            img = ImageOps.expand(img, border=border_width, fill=border_color)

            # Use ImageTk to convert the PIL image to a Tkinter image
            img2 = ImageTk.PhotoImage(img)

            # Create a label to display the image
            labelImage = Label(self.root, image=img2)
            labelImage.img2 = img2  # Keep a reference to avoid garbage collection
            labelImage.place(x=0, y=0, width=width + 2 * border_width, height=height + 2 * border_width)  # Place the image

        else:
            print("Failed to retrieve logo image")
        
        #=======Title======#
        lbl_title=Label(self.root,text="Hotel Management System",font=("times new roman",35,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=====Main frame /background=====#
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #=====Button frame=====#
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        #======Menu=====#
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=229)

        cust_btn=Button(btn_frame,text="Customer details",command=self.cust_details ,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1) #to add border to button we use pady

        room_btn=Button(btn_frame,text="Book room",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1",command=self.roombooking)
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="Available rooms",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1",command=self.details_room)
        details_btn.grid(row=2,column=0,pady=1) 

        report_btn=Button(btn_frame,text="Our other hotels",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="Log Out",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1",command=self.logout)
        logout_btn.grid(row=4,column=0,pady=1)


    #=====right side image=====#
     # URL of the right side image
        url3 = 'https://cdn.sanity.io/images/ocl5w36p/production/4ea12c45b7c1f6723c370562106d22cd308c24d4-1400x860.jpg?w=480&auto=format&dpr=2'  

        # Download the image
        response = requests.get(url3)
        if response.status_code == 200:
            img_data = response.content

            # Open the image with PIL
            img = Image.open(BytesIO(img_data))

            # Resize the image
            width, height = 1310, 595 # Set the desired width and height
            img = img.resize((width, height), Image.Resampling.LANCZOS)

            border_width = 2
            border_color = "silver"
            img = ImageOps.expand(img, border=border_width, fill=border_color)

            # Use ImageTk to convert the PIL image to a Tkinter image
            img3 = ImageTk.PhotoImage(img)

            # Create a label to display the image
            labelImage = Label(main_frame, image=img3)
            labelImage.img3 = img3  # Keep a reference to avoid garbage collection
            labelImage.place(x=225, y=0, width=width + 2 * border_width, height=height + 2 * border_width)  # Place the image

        else:
            print("Failed to retrieve logo image")

    #=====down side image 1=====#
     # URL of the down side image1
        url4 = 'https://www.india-travel.com/rajasthan/images/rambagh_b3.jpg'  

        # Download the image
        response = requests.get(url4)
        if response.status_code == 200:
            img_data = response.content

            # Open the image with PIL
            img = Image.open(BytesIO(img_data))

            # Resize the image
            width, height = 223, 210 # Set the desired width and height
            img = img.resize((width, height), Image.Resampling.LANCZOS)

            border_width = 2
            border_color = "silver"
            img = ImageOps.expand(img, border=border_width, fill=border_color)

            # Use ImageTk to convert the PIL image to a Tkinter image
            img4 = ImageTk.PhotoImage(img)

            # Create a label to display the image
            labelImage = Label(main_frame, image=img4)
            labelImage.img4 = img4  # Keep a reference to avoid garbage collection
            labelImage.place(x=0, y=225, width=width + 2 * border_width, height=height + 2 * border_width)  # Place the image

        else:
            print("Failed to retrieve logo image")
    
    #=====down side image 2=====#
     # URL of the down side image2
        url5 = 'https://i.pinimg.com/736x/d3/48/14/d348147a07fe835a45d089416acc28d0.jpg'  

        # Download the image
        response = requests.get(url5)
        if response.status_code == 200:
            img_data = response.content

            # Open the image with PIL
            img = Image.open(BytesIO(img_data))

            # Resize the image
            width, height = 223, 204 # Set the desired width and height
            img = img.resize((width, height), Image.Resampling.LANCZOS)

            border_width = 2
            border_color = "silver"
            img = ImageOps.expand(img, border=border_width, fill=border_color)

            # Use ImageTk to convert the PIL image to a Tkinter image
            img5 = ImageTk.PhotoImage(img)

            # Create a label to display the image
            labelImage = Label(main_frame, image=img5)
            labelImage.img5 = img5  # Keep a reference to avoid garbage collection
            labelImage.place(x=0, y=420, width=width + 2 * border_width, height=height + 2 * border_width)  # Place the image

        else:
            print("Failed to retrieve logo image")

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
    
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()


#call the object from main functiom
if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop() #close main loop
