from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 500, height = 500)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("Voice-search.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop()
