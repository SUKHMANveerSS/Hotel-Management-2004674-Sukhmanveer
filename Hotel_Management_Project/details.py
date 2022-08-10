from tkinter import*
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+240+220")

        #=========Title================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Bahnschrift SemiBold",20,),bg="black",fg="tan",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=58)

        #======= labelFrame =====
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=500,height=350)

        #Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",12,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)

        #Room no.
        lbl_RoomNo=Label(labelframeleft,text="Room No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        self.var_RoomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("arial",12,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        
        self.var_RoomType=StringVar()
        enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",12,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)

        #===== btns =====
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #======== tabel frame search system==========
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)  

        scroll_x.config(command=self.room_table.xview)    
        scroll_y.config(command=self.room_table.yview) 

        self.room_table['columns']=("floor","roomNo","roomtype")
        self.room_table.heading("floor",text="Floor")   
        self.room_table.heading("roomNo",text="Room no")
        self.room_table.heading("roomtype",text="Room Type")
        
       
        

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomNo",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
          messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",( 
                                                                                    self.var_floor.get(),
                                                                                    self.var_RoomNo.get(),
                                                                                    self.var_RoomType.get(),
                                                                                    

                                                                                       ))
                                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()                                                                    
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)   

    #====Fetch data====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()    
        conn.close() 

    #getcursor
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]    

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

    #==Update Function========
    def Update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Floor No.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
            my_cursor=conn.cursor()
            my_cursor.execute("Update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                
                                                                                                                
                                                                                                          self.var_floor.get(),
                                                                                                          self.var_RoomType.get(),
                                                                                                          self.var_RoomNo.get()
                                                                                                                
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room Details has been Updated successfully",parent=self.root)
    
    #===Delete Function=======
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do You Want To Delete this Room Details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  

    #====Reset Function=====
    def reset(self):  
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")          
                             



        




if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()        