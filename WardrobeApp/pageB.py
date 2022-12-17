#Import the required library
from tkinter import *
from PIL import ImageTk, Image




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
    from pagetwo import WardrobeApp

img = ImageTk.PhotoImage(Image.open("logoo.png"))
canvas= Canvas(win, width=220 , height= 500, bg='#E3C396')
canvas.pack()
canvas.create_image(80,150,anchor=NW,image=img)


img = ImageTk.PhotoImage(Image.open("closet1.png"))
canvas.create_image(0,0,anchor=NW,image=img)


btn = Button( win,text='visit your wardrobe',command=nextPage,border=2)
btn.place(x=50,y=230 )


#button for adding clothes to your wardrobe 
btn2 = Button( win,text='Add to your your wardrobe')
btn2.place(x=35,y=290 )

win.mainloop()