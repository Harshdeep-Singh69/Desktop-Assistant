from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

import welcome

class audio():
    def __init__(self,master):
        self.master=master
        self.master.geometry("800x400+100+200")
        self.master.title("PLAY AUDIO")

        Label(master,text="VOICE SEARCH: THE EVOLUTION OF SPEECH RECOGNITION TECHNOLOGY",fg="green",font=('arial',10,'bold'),anchor='w').place(x=65,y=15)
       
        
        self.photo1=PhotoImage(file="voice.png")
        Label(master,image=self.photo1).place(x=150,y=150)

        self.button = Button(master, text="Select Links",width=10,height=1,bg="red",fg="white", command=self.search)
        self.button.place(x=180,y=150)

        self.l1=Label(master,font=('arial',12,'italic'),text="You are searching for : ",fg="blue",anchor='w')
        self.l1.place(x=280,y=180)
       

        self.button1 = Button(master, text="Stop Audio",width=20,height=1,bg="red",fg="white", command=self.quit)
        self.button1.place(x=280,y=150)

        self.button2 = Button(master, text="Back",width=10,height=1,bg="red",fg="white", command=self.back)
        self.button2.place(x=500,y=150)

        canvas = Canvas(master, width = 300, height = 300)  
        canvas.place(x=180,y=180)  
        self.img = ImageTk.PhotoImage(Image.open("audioplayer.jpg"))  
        canvas.create_image(20, 20, anchor=NW, image=self.img) 
      

        
        from pygame import mixer as m # Load the popular external library
        self.mm=m
        self.mm.init()
        
        
    def search(self):
        import speech_recognition as sr
        import webbrowser as wb

        r1=sr.Recognizer()
        r2=sr.Recognizer()
        r3=sr.Recognizer()
        
        with sr.Microphone() as source:
            print('Search your Query')
            self.l1.configure(fg="red")
            self.l1['text']="Search Your Query "
            
            audio=r3.listen(source)

            try:
                get=r3.recognize_google(audio)
                s="audios/"+get+".mp3"
                print(s)
                #from pygame import mixer  # Load the popular external library
                #mixer.init()
                '''canvas = Canvas(master, width = 300, height = 300)  
                canvas.place(x=180,y=180)  
                self.img = ImageTk.PhotoImage(Image.open("gify.gif"))  
                canvas.create_image(20, 20, anchor=NW, image=self.img)'''
                self.mm.music.load(s)
                self.mm.music.play()
            except sr.UnknownValueError:
                print("Error")
            except sr.RequestError as e:
                print("Failed".format(e))

        
    def back(self):
         self.master.destroy() 
         root2=Toplevel(self.master)
         MyGUI=welcome.Links(root2)


    def quit(self):
         #self.master.destroy()
         self.mm.music.stop() 
    

    def text_to_respond(self,mytext):
        from gtts import gTTS 
        import os 
  
        # Language in which you want to convert 
        language = 'en'
  
        # Passing the text and language to the engine,  
        # here we have marked slow=False. Which tells  
        # the module that the converted audio should  
        # have a high speed 
        myobj = gTTS(text=mytext, lang=language, slow=False) 
  
        #to generate random value for file name
        
        from random import randint
        
        
        # generate some integers
        value = randint(0,100)
        print(str(value)+".mp3")
        s="searches/"+str(value)+".mp3"

        # Saving the converted audio in a mp3 file named 
        # welcome
        
        myobj.save(s) 
  
        # Playing the converted file 
        
        from pygame import mixer  # Load the popular external library
        mixer.init()
        mixer.music.load(s)
        mixer.music.play()
        
        
    

#root=Tk()
#app = searcher(root)
#app.mainloop()


       
