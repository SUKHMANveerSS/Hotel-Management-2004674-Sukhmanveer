from tkinter import*
from PIL import Image,ImageTk
from customer import Customer_Window
from room import RoomBooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        img1=Image.open(r"C:\Users\DELL\Dropbox\PC\Desktop\VS CODE\Hotel_management.project\images\logo.png")
        img1=img1.resize((230,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        img2=Image.open(r"C:\Users\DELL\Dropbox\PC\Desktop\VS CODE\Hotel_management.project\images\mohammed-kabir-Mx6YtMgac8U-unsplash.jpg")
        img2=img2.resize((1310,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=140)


        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Bahnschrift SemiBold",40,),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=58)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        lbl_menu=Label(main_frame,text="MENU",font=("Bahnschrift SemiBold",20),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.customer_details,width=22,font=("Bahnschrift SemiBold",14),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=22,font=("Bahnschrift SemiBold",14),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("Bahnschrift SemiBold",14),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("Bahnschrift SemiBold",14),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        lbl_name=Label(main_frame,text="Project By-",font=("Bahnschrift SemiBold",20),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_name.place(x=0,y=300)
        lbl_name1=Label(main_frame,text="Sukhmanveer 2004674",font=("Bahnschrift SemiBold",15),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_name1.place(x=0,y=350)

        img3=Image.open(r"C:\Users\DELL\Dropbox\PC\Desktop\VS CODE\Hotel_management.project\images\wallpaperflare.com_wallpaper.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)   

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)   

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)       
        




if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

    

   