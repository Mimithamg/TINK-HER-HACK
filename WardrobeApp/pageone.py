from tkinter import *
from functools import partial


#creating a function for login
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('220x500')  

#setting login as title
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x=10,y=50) 
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=65,y=50)  

validateLogin = partial(validateLogin, username, password)

#when pressing login button redirect to next page
def nextpage():
	tkWindow.destroy()
	import pageB

#login button
loginButton = Button(tkWindow, text="Login", command=nextpage).place(x=30,y=100)
tkWindow.mainloop()