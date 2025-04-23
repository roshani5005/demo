
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        
        
         # self.root.resizable(0,0)
        #====== title==========
        title=Label(self.root,text="Inventory Management system",font=("goudy old style",40,"bold"),bg='#0f4d7d',fg="white").place(x=0,y=0,relwidth=1,height=70)
       
        #==============image================
        #self.phone_image=PhotoImage("file=image/phone.png")
        #self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=10,y=100)
        
        #===Login Frame===========
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="#ECECEC")#"#767171"
        login_Frame.place(x=650,y=100,width=355,height=450)#bg="#ECECEC"
      
        #self.login_image=PhotoImage("image/login.png")
        #self.lbl_login_image=Label(login_Frame,image=self.login_image,bd=0).place(x=640,y=100)
     
      #  logoImage=PhotoImage(file="image\man.png")
       # logoLable=Label(self.root,image=logoImage)
       # logoLable.place(x=400,y=100)
        
        #login_image=PhotoImage(file="image\window.png")
        #lbl_login_image=Label(login_Frame,image=self.lbl_login_image,bd=0).place(x=640,y=100)
        
        #title=Label(login_Frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        
        lbl_user=Label(login_Frame,text="Employee Id",font=("Arial Rounded MT Bold",15),fg="#767171").place(x=50,y=110)
        self.employee_id=StringVar()#Andalus
        #self.password=StringVar()
        txt_username=Entry(login_Frame,textvariable=self.employee_id,show="*",font=("times new roman",15)).place(x=50,y=145,width=250)
        
        lbl_pass=Label(login_Frame,text="Password",font=("Arial Rounded MT Bold",15),fg="#767171").place(x=50,y=190)#,bg="#ECECEC"
        txt_pass=Entry(login_Frame,textvariable=self.password,font=("goudy old style",15),bg="white").place(x=50,y=230,width=250)
        
        btn_login=Button(login_Frame,command=self.login,text="Login",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",bd=2,activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
      #  hr=Label(login_Frame,bg="Lightgray").place(x=50,y=370,width=250,height=2)   
        
       # or_=Label(login_Frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        btn_forget=Button(login_Frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=50,y=270)
        
        
        #==========Frame2===========
       # register_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        #register_Frame.place(x=650,y=540,width=355,height=75)           #x=650,y=570,width=350,height=60
        
       # lbl_reg=Label(register_Frame,text="SUBCRIBE | LIKE | SHERE ",font=("times new roman",13),bg="white").place(x=0,y=20,relwidth=1)
       # btn_signup=Button(register_Frame,text="Sign Up",command=self.forget_window,font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=210,y=17)
        
        
        
        #=====Animation Images=====
      #  self.im1=ImageTk.PhotoImage(file="image/im1.png")
      #  self.im2=ImageTk.PhotoImage(file="image/im2.png")
      #  self.im3=ImageTk.PhotoImage(file="image/im3.png")
        
      #  self.lbl_change_image=Label(self.root,bg="white")
      #  self.lbl_change_image.place(x=367,y=153,width=240,height=300)   #(x=367,y=153,width=240,height=400)
        
      #  self.animate()
#=============================All function================================

   # def animate(self):
    #    self.im=self.im1
     #   self.im1=self.im2
       # self.im2=self.im3
      #  self.im3=self.im
       # self.lbl_change_image.config(image=self.im)
       # self.lbl_change_image.after(2000,self.animate)     
        
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are rquired",parent=self.root)
            else:    
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get(),))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invaild USERNAME/PASSWORD",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destory()
                        os.system("python dashboard.py")
                    else:
                        self.root.destory()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)      
             
    
    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
               messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=? ",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invaild EmployeebID,try again",parent=self.root)
                else:
                    #====forget Window========
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_conf_pass=StringVar()
                    
                    #call send_email_function()
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    
                    title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg='lightyellow').place(x=20,y=100,width=250,height=30)
                    self.btn_reset=Button(self.forget_win,text="SUBMIT",font=("times new roman",15),bg='lightblue')
                    self.btn_reset.place(x=280,y=100,width=100,height=30)
                     
                    lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_password,font=("times new roman",15),bg='lightyellow').place(x=20,y=190,width=250,height=30)
            
                   
                    txt_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=255,width=250,height=30)
                     
                    self.btn_update=Button(self.forget_win,text="Update",state=DISABLED,font=("times new roman",15),bg='lightblue')
                    self.btn_update.place(x=150,y=300,width=100,height=30)
                   
                    
                 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)      
              
    

root=Tk()
obj=Login_System(root)
root.mainloop()        
        
        
        
        
        
        
        