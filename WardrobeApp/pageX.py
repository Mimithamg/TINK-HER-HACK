from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
from pageY import SignUp
import credentials as cr

#login page connected with database 
class login_page:
    def __init__(self, root):
        self.window = root
        #setting windows dimensions
        self.window.geometry("220x500")
        self.window.config(bg ='#E3C396')

        #============================================================================
        #==============================DESIGN PART===================================
        #============================================================================

        
        #=============Entry Field & Buttons============

        
        self.window.title("Outluk")
        self.frame3 = Frame(self.window, bg='#E3C396')
        self.frame3.place(x=0,y=0,width=220,height=500)

        self.email_label = Label(self.frame3,text="Email Address", font=("helvetica",10,"bold"),bg="white", fg="gray").place(x=5,y=20)
        self.email_entry = Entry(self.frame3,font=("times new roman",10,"bold"),bg="white",fg="gray")
        self.email_entry.place(x=115, y=20, width=100,height=20)

        self.password_label = Label(self.frame3,text="Password", font=("helvetica",10,"bold"),bg="white", fg="gray").place(x=5,y=50)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray",show="*")
        self.password_entry.place(x=115, y=50, width=100,height=20)

        #================Buttons===================
        self.login_button = Button(self.frame3,text="Log In",command=self.login_func,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=80,y=100,width=60)
  
        self.forgotten_pass = Button(self.frame3,text="Forgotten password?",command=self.forgot_func,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="white",fg="blue").place(x=40,y=150,width=150)

        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=40,y=200,width=150)
        

    def login_func(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from login_details where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=self.window)
                else:
                    
                    self.window.destroy()
                    import pageZ
                    # Clear all the entries
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def forgot_func(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error!", "Please enter your Email Id",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.email_entry.get())
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists")
                else:
                    connection.close()
                    
                    #=========================SECOND WINDOW===============================
                    #------------Toplevel:create a window top of another window-----------
                    #------------focus_force:Helps to to focus on the current window------
                    #-----Grab:Helps to grab the current window until user ungrab it------

                    self.root=Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("220x500")
                    self.root.config(bg='#E3C396')
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root,text="Change your password",font=("times new roman",9,"bold"),bg="white").place(x=10,y=10)

                    title4 = Label(self.root,text="It's quick and easy",font=("times new roman",8),bg="white").place(x=10,y=30)

                    

                    title7 = Label(self.root, text="New Password", font=("times new roman", 8, "bold"), bg="white").place(x=5,y=100)

                    self.new_pass = Entry(self.root,font=("arial"))
                    self.new_pass.place(x=85,y=100,width=130,height=20)

                    self.create_button = Button(self.root,text="Submit",command=self.change_pass,font=("times new roman",9, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=80,y=180,width=80)
                    #=========================================================================

            except Exception as e:
                messagebox.showerror("Error", f"{e}")
                
      
    def change_pass(self):
        if self.email_entry.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and question=%s and answer=%s", (self.email_entry.get(),self.sec_ques.get(),self.ans.get()))
                row=cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update student_register set password=%s where email=%s", (self.new_pass.get(),self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
                        
            except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
            

    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)
# The main function
#if __name__ == "__main__":
root = Tk()
obj = login_page(root)
root.mainloop()
