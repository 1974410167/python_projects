import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        super(Application, self).__init__(master)
        self.pack()
        self.create_widgets()



c