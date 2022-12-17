#Import the required library
from tkinter import *
from PIL import ImageTk, Image



#Create an instance of tkinter frame
win= Tk()

#Set the geometry
win.geometry("220x500")


#Create a canvas object

win.title("Outluk")
img = ImageTk.PhotoImage(Image.open("logoo.png"))

#Add a text in Canvas
canvas= Canvas(win, width=220 , height= 500, bg="white")
canvas.create_text(110, 250, text="Outluk", fill="black", font=('Helvetica 15 bold'))
canvas.pack()
canvas.create_image(90,180,anchor=NW,image=img)
btn = Button( text='>', width=1,height=1, bd='10')
btn.place(x=180, y=450)

win.mainloop()