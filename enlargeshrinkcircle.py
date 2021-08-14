from tkinter import *
class enlargeshrinkcircle:
    def __init__(self):
        self.radius=50
        window=Tk()
        window.title("Control Circle Demo")
        self.canvas=Canvas(window,bg="white",width=200,height=200)
        self.canvas.pack()
        self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")
        self.canvas.bind("<Button-1>",self.increasecircle)
        self.canvas.bind("<Button-3>",self.decreasecircle)
    def increasecircle(self,event):
        self.canvas.delete("oval")
        if self.radius<100:
            self.radius+=4
        self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")
    def decreasecircle(self,event):
        self.canvas.delete("oval")
        if self.radius>2:
            self.radius -=4
        self.canvas.create_oval(100-self.radius,100-self.radius,100+self.radius,100+self.radius,tags="oval")
enlargeshrinkcircle()
