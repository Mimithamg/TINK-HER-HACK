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
def prevPage():
   win.destroy()
   import pageB
   #from pagetwo import WardrobeApp



#Add a text in Canvas
canvas= Canvas(win, width=220 , height= 500, bg='#E3C396')
canvas.create_text(110,30, text="your selected pair", fill="black", font=('Helvetica 15 bold'))
canvas.pack()
canvas.create_image(80,430,anchor=NW,image=img)
btn = Button( win,text='move it to washbox')
btn.place(x=50, y=400)

btn2 = Button( win,text='<', width=1,height=1,command=prevPage)
btn2.place(x=30, y=450)

win.mainloop()