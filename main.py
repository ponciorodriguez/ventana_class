from tkinter import *
 
class FrameMan(Tk):
  """ Gestion de Frames. """
  def __init__(self):
    """ Initialize the frame. """
    Tk.__init__(self)
    self.grid()
 
    self.title("Simple Calculator.")
    self.resizable(width = 0, height = 0)
    self.geometry("750x750")
 
    self.result = 0
    self.createWidgets()
 
  def createWidgets(self):
    """ Creamos el Frame y demas controles hijos. """
    self.myFrame1 = Frame(self)
    self.myFrame2 = Frame(self)
    self.myFrame1.place(x = 100, y = 100)
    self.myFrame2.place(x = 200, y = 100)
 
    self.Label1 = Label(self.myFrame1, text = "Este es el Frame 1")
    self.Label2 = Label(self.myFrame2, text = "Este es el Frame 2")
    self.Label1.place(x = 100, y = 0)
    self.Label2.place(x = 100, y = 0)
 
    self.Button1 = Button(self, text = "Dest 1", command = exit)
    self.Button2 = Button(self, text = "Dest 2", command = exit)
    self.Button1.place(x = 200, y = 200)
    self.Button2.place(x = 300, y = 200)
 
  def runApp(self):
    """ Ejecutamos la aplicacion. """
    self.mainloop()
 
  # def destF1(self):
  #   self.myFrame1.destroy()
 
  # def destF2(self):
  #   self.myFrame2.destroy()
 
root = FrameMan().runApp()
