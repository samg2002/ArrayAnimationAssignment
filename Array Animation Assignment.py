from tkinter import *
from random import *
from math import *

myInterface = Tk()
s = Canvas(myInterface, width=800,height=800, background="sky blue")
s.pack()


class Grass:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def display(self):
        s.create_rectangle(self.x,self.y,self.x+10,self.y+10,fill = "green")

    def update(self):
        return

class Flower:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def display(self):
        return

    def update(self):
        return

class Tree:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def display(self):
        return

    def update(self):
        return

    
plants = []
specialPlant = Grass(100, 500)

for i in range(50):
    plant = Grass(randint(50,600),randint(0,800))
    plants.append(plant)
    
while True:
    
    s.create_rectangle(0,800,800,200,fill = "#804000",outline = "")
    specialPlant.display()
    plant.display()
    
    s.update()
        
        
        








