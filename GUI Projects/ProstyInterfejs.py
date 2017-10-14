from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets

root = Tk()

root.title("Prosty interfejs GUI")
root.geometry("225x100")
app = Frame(root)
app.grid()

bttn1 = Button(app, text = "Nic nie robie!")
bttn1.grid()


bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Ja też!")

bttn3 = Button(app)
bttn3["text"]= "Ja również!"
bttn3.grid()

root.mainloop()


