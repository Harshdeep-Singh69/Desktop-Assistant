from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


import welcome

class about():
    def __init__(self,master):
        self.master=master
        self.master.geometry("800x400+100+200")
        self.master.title("WELCOME")

        Label(master,text="VOICE SEARCH: THE EVOLUTION OF SPEECH RECOGNITION TECHNOLOGY",fg="green",font=('arial',10,'bold'),anchor='w').place(x=165,y=15)
        
       
        explanation = """ **************

        To run this Application
        
        1. Install Python 3+ or 3.6

        2. Install some libraries:
        pip install PyAudio
        pip install Speech_recognition
        pip install pygame
        pip install gtts

        3. Run welcome.py file, click Start Button.

        4. Then it will show Button for

         Google Search, Youtube Videos, To play Audios

        ********************"""

        Label(master,padx = 10, text=explanation).pack(side="left")


        
        self.button1 = Button(master, text="Quit",width=10,height=1,bg="red",fg="white", command=self.quit)
        self.button1.place(x=380,y=50)

        self.button2 = Button(master, text="Back",width=10,height=1,bg="red",fg="white", command=self.back)
        self.button2.place(x=380,y=150)
        canvas = Canvas(master, width = 300, height = 300)  
        canvas.place(x=500,y=60)  
        self.img = ImageTk.PhotoImage(Image.open("images-2.png"))  
        canvas.create_image(20, 20, anchor=NW, image=self.img)
        
        
    
        
    def back(self):
         self.master.destroy()
         root2=Toplevel(self.master)
         MyGUI=welcome.Links(root2)


    def quit(self):
         self.master.destroy()

#root=Tk()
#app = searcher(root)
#app.mainloop()


       
