#Import the required library
from tkinter import *
from PIL import ImageTk, Image




#Create an instance of tkinter frame
win= Tk()

#Set the geometry
win.geometry("220x500")


#Create a canvas object
#create a title 
win.title("Outluk")

#adding an image
img = ImageTk.PhotoImage(Image.open("logoo.png"))


#when clicking the button redirect to next page and exiting from running page 
def nextpage():
    win.destroy()
    import pageone

#Add a text in Canvas
canvas= Canvas(win, width=220 , height= 500, bg='#E3C396')
canvas.create_text(110, 250, text="Outluk", fill="black", font=('Helvetica 15 bold'))
canvas.pack()
canvas.create_image(80,180,anchor=NW,image=img)
btn = Button( win,text='>', width=1,height=1,command=nextpage)
btn.place(x=180, y=450)

win.mainloop()