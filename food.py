from turtle import Turtle
import random
#class Food:
    #def __init__(self):
        #self.food_turtle=Turtle("circle")
        #self.food_turtle.color("red")
#it itself a turtle so using inheritance
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(0.9,0.9)
        self.appear()
        

    def appear(self):
        random_x=random.randint(-380,380)
        random_y=random.randint(-300,300)    
        self.goto(random_x,random_y)#same piece goto new x & y
        
        