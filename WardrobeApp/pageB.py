#Import the required library
from tkinter import *
from PIL import ImageTk, Image
import pagetwo




#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("220x500")

#Create a canvas object

win.title("Outluk")


#when clicking visit your wardrobe button redirect to next page 
def nextPage():
    win.destroy()
    import pagetwo



btn = Button( win,text='visit your wardrobe',command=nextPage)
btn.place(x=50,y=230 )


#button for adding clothes to your wardrobe 
btn2 = Button( win,text='Add to your your wardrobe')
btn2.place(x=35,y=290 )

win.mainloop()