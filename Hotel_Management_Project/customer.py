from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Customer_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+240+220")

        #=======variables ====
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_Father=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_IdProof=StringVar()
        self.var_address=StringVar()
        





        #=========Title================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Bahnschrift SemiBold",20,),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=58)

        #======= labelFrame =====
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Deatils",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)
        #======== labels and entrys =======
        #CustRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
       
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=22,font=("arial",12,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        #cust name
        
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)
        
        #Father name
        lblmname=Label(labelframeleft,font=("arial",12,"bold"),text="Father Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_Father,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)
        #gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
    
        #mobilenumber
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=4,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=4,column=1)
        
        #email
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=5,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=5,column=1)
                               
        
        #nationality
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=6,column=0,sticky=W)
        txtNationality=ttk.Entry(labelframeleft,textvariable=self.var_nationality,font=("arial",13,"bold"),width=29)
        txtNationality.grid(row=6,column=1)
        #idproof type 
        lblIdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=7,column=0,sticky=W)
        combo_Id=ttk.Combobox(labelframeleft,textvariable=self.var_IdProof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Id["value"]=("Adhaar Card","Driving License ","Passport")
        combo_Id.current(0)
        combo_Id.grid(row=7,column=1)

        #address
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=8,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=8,column=1)
 
        #===== btns ===
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=48)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #======== tabel frame search system==========
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIew Deatils And Seaarch System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid (row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Serach["value"]=("Mobile","Ref")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #======== Show data Table =======
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_Table=ttk.Treeview(details_table,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)  

        scroll_x.config(command=self.Cust_details_Table.xview)    
        scroll_y.config(command=self.Cust_details_Table.yview)    

        self.Cust_details_Table['columns']=("ref","name","Father","gender","mobile","email","nationality","IdProof","address")
        self.Cust_details_Table.heading("ref",text="Refer no.")   
        self.Cust_details_Table.heading("name",text="Name")
        self.Cust_details_Table.heading("Father",text="Father Name")
        self.Cust_details_Table.heading("gender",text="Gender")
        self.Cust_details_Table.heading("mobile",text="Mobile no.")
        self.Cust_details_Table.heading("email",text="Email")
        self.Cust_details_Table.heading("nationality",text="Nationality")
        self.Cust_details_Table.heading("IdProof",text="ID Proof")
        self.Cust_details_Table.heading("address",text="Address")

        self.Cust_details_Table["show"]="headings"

        self.Cust_details_Table.column("ref",width=100)
        self.Cust_details_Table.column("name",width=100)
        self.Cust_details_Table.column("Father",width=100)
        self.Cust_details_Table.column("gender",width=100)
        self.Cust_details_Table.column("mobile",width=100)
        self.Cust_details_Table.column("email",width=100)
        self.Cust_details_Table.column("nationality",width=100)
        self.Cust_details_Table.column("IdProof",width=100)
        self.Cust_details_Table.column("address",width=100)
        self.Cust_details_Table.pack(fill=BOTH,expand=1)
        self.Cust_details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_Father.get()=="":
          messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_Father.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_IdProof.get(),
                                                                                    self.var_address.get()
                                                                                    
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                    
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)  

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("",END,values=i)
            conn.commit()    
        conn.close()    

    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_details_Table.focus()
        content=self.Cust_details_Table.item(cusrsor_row)
        row=content["values"]    

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_Father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationality.set(row[6]),
        self.var_IdProof.set(row[7]),
        self.var_address.set(row[8])

    def Update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
            my_cursor=conn.cursor()
            my_cursor.execute("Update customer set name=%s,Father=%s,gender=%s,mobile=%s,email=%s,nationality=%s,IdProof=%s,address=%s where ref=%s",(
                                                                                                                
                                                                                                                self.var_cust_name.get(),
                                                                                                                self.var_Father.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_mobile.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_nationality.get(),
                                                                                                                self.var_IdProof.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_ref.get()
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been Updated successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do You Want To Delete this Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
            my_cursor=conn.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_Father.set(""),
        #self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_IdProof.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("",END,values=i)
            conn.commit()    
        conn.close()    
         











if __name__ == "__main__":
    root=Tk()
    obj=Customer_Window(root)
    root.mainloop()

