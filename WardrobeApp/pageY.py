from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os
import credentials as cr

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("220x500")
        self.window.config(bg = "white")

        


        frame = Frame(self.window, bg="white")
        frame.place(x=0,y=0,width=220,height=500)

        title1 = Label(frame, text="Sign Up", font=("times new roman",10,"bold"),bg="white").place(x=80, y=10)
        title2 = Label(frame, text="Join with us", font=("times new roman",8),bg="white", fg="gray").place(x=77, y=25)

        f_name = Label(frame, text="Name", font=("helvetica",8,"bold"),bg="white").place(x=8, y=80)
        

        self.fname_txt = Entry(frame,font=("helvetica"))
        self.fname_txt.place(x=100, y=80, width=100,height=20)

        

        email = Label(frame, text="Email", font=("helvetica",8,"bold"),bg="white").place(x=8, y=120)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=100, y=120, width=100,height=20)

        

        password =  Label(frame, text="New password", font=("helvetica",8,"bold"),bg="white").place(x=5, y=160)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=100, y=160, width=100,height=20)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",7)).place(x=5,y=200)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",8, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=38,y=300,width=150)

    def signup_func(self):
        if self.fname_txt.get()==""  or self.email_txt.get()==""  or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s",self.email_txt.get())
                row=cur.fetchone()

                # Check if th entered email id is already exists or not.
                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                else:
                    cur.execute("insert into student_register (f_name,email,password) values(%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        #self.lname_txt.get(),
                                        self.email_txt.get(),
                                        #self.questions.get(),
                                        #self.answer_txt.get(),
                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        #self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        #self.questions.current(0)
        #self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
