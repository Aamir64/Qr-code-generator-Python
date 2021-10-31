from tkinter import*
from tkinter import font
import qrcode
from PIL import Image,ImageTk
import resizeimage  


class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,True)
        root.resizable(True, True)

        title=Label(self.root,text="Qr Code Generator",font=("sora",40),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        
        #-----Employee default window-----
        
        #----variable----
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
    
        emp_Frame=Frame(self.root,bd=10,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=390)
        
        emp_title=Label(emp_Frame,text="Student Details",font=("sora",20),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        lbl_emp_code=Label(emp_Frame,text="Student Rollno",font=("sora",15,font.BOLD),bg='white').place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Name",font=("sora",15,font.BOLD),bg='white').place(x=20,y=100)
        lbl_department=Label(emp_Frame,text="Department",font=("sora",15,font.BOLD),bg='white').place(x=20,y=140)
        lbl_designation=Label(emp_Frame,text="Designation",font=("sora",15,font.BOLD),bg='white').place(x=20,y=180)
        
        
        txt_emp_code=Entry(emp_Frame,font=("sora",15),bg='lightyellow',textvariable=self.var_emp_code).place(x=200,y=60,width=230)
        txt_name=Entry(emp_Frame,font=("sora",15),bg='lightyellow',textvariable=self.var_name).place(x=200,y=100,width=230)
        txt_department=Entry(emp_Frame,font=("sora",15),bg='lightyellow',textvariable=self.var_department).place(x=200,y=140,width=230)
        txt_designation=Entry(emp_Frame,font=("sora",15),bg='lightyellow',textvariable=self.var_designation).place(x=200,y=180,width=230)   
        
        
        btn_generate=button = Button(emp_Frame,text='Generate Qr Image',font=('roboto',14),bg='green', command=self.generate).place(x=90,y=250,width=180,height=45)
        self.btn_clear=Button(emp_Frame,text="Clear",font=("sora",14),bg='red',fg='white',command=self.clear)
        self.btn_clear.place(x=290,y=250,width=120,height=45)
        
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("sora",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)     
        
        
        #----Qrcode image part----
        qr_Frame=Frame(self.root,bd=10,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        
        emp_title=Label(qr_Frame,text="Student Qrcode",font=("sora",20),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)  
        
        self.qr_code=Label(qr_Frame,bd=10,text='No Qr available',font=('sora',15),bg='gray')
        self.qr_code.place(x=25,y=100,width=180,height=180)   
        
        
    def clear(self):
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')  
        
    
    def generate(self):
        if self.var_name.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
            self.msg='All Entry is required'
            self.lbl_msg.config(text=self.msg,fg='red')
            
        else:
            qr_data=(f"Student ID: {self.var_emp_code.get()}\nStudent Name: {self.var_name.get()}\nDeparetment: {self.var_department.get()}\nDesignation: {self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
           
            qr_code.save("qr_images/student_"+str(self.var_emp_code.get())+'.png')
            
            #----Qr code update----
          
            self.im=ImageTk.PhotoImage("qr_images/student_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
            
            #-----updating Notification---
            self.msg='QrCode Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
            
        
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
