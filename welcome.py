from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image  

import searcher
import videos
import abouts
import audios


class Welcome():
    def __init__(self,master):
        self.master=master
        self.master.geometry("800x700+50+50")
        self.master.title("WELCOME")

        
        Label(master,text="VOICE SEARCH: THE EVOLUTION OF SPEECH RECOGNITION TECHNOLOGY",fg="green",font=('arial',10,'bold'),anchor='w').place(x=165,y=15)
       
        
        Button(master, text="START",bg="red",fg="white", command=self.gotolinks).place(x=185,y=90)
        
        Button(master, text="QUIT",bg="red",fg="white", command=self.finish).place(x=285,y=90)

        Button(master, text="QUIT",bg="red",fg="white", command=self.finish).place(x=85,y=150)
        canvas = Canvas(master, width = 500, height = 500)  
        canvas.place(x=85,y=150)  
        self.img = ImageTk.PhotoImage(Image.open("Voice-search.jpg"))  
        canvas.create_image(20, 20, anchor=NW, image=self.img)
      
        
    def finish(self):
         self.master.destroy()
         
    def gotolinks(self):
         root2=Toplevel(self.master)
         MyGUI=Links(root2)



class Links():
    def __init__(self,master):
        self.master=master
        self.master.geometry("800x400+100+200")
        self.master.title("SEARCH OPTIONS")

        Label(master,text="VOICE SEARCH: THE EVOLUTION OF SPEECH RECOGNITION TECHNOLOGY",fg="green",font=('arial',10,'bold'),anchor='w').place(x=165,y=15)
        
       


        Button(master, text="REQUIREMENTS",width=18,bg="red",fg="white", command=self.gotologin).place(x=95,y=70)
        
        Button(master, text="YOUTUBE VIDEOS",width=18,bg="red",fg="white", command=self.video).place(x=95,y=170)

        Button(master, text="GOOGLE SEARCH", width=18,bg="red",fg="white", command=self.search).place(x=95,y=270)

        Button(master, text="PLAY AUDIO", width=18,bg="red",fg="white", command=self.audio).place(x=95,y=350)
        canvas = Canvas(master, width = 500, height = 500)  
        canvas.place(x=300,y=70)  
        self.img = ImageTk.PhotoImage(Image.open("images-1.jpg"))  
        canvas.create_image(20, 20, anchor=NW, image=self.img) 
      
        
    def finish(self):
         self.master.destroy()
         
    def gotologin(self):
         root2=Toplevel(self.master)
         MyGUI=abouts.about(root2)

    def audio(self):
         root2=Toplevel(self.master)
         MyGUI=audios.audio(root2)
         
    def video(self):
         root2=Toplevel(self.master)
         MyGUI=videos.video(root2)

    def search(self):
         root2=Toplevel(self.master)
         MyGUI=searcher.search(root2)





def main():
    root=Tk()
    myGUIWelcome=Welcome(root)
    root.mainloop()

    
if __name__=='__main__':
    main()
