#snake class:
#methods:create snake(),move snake()
from turtle import Turtle
class Snake:#contain turtles therefore using class
    def __init__(self):
        self.turtles =[]
        self.position=[(-40,0),(-20,0),(0,0)]
        self.create_snake()
        self.head =self.turtles[-1]

    def create_snake(self):
        for i in range(len(self.position)):
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.speed(0.006)
            new_turtle.penup()
            new_turtle.goto(self.position[i])
            self.turtles.append(new_turtle)
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20) 

    def extend(self):
        new_segment =Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        #new_segment.goto(self.turtles[0].pos())
        #to add the extended part to the rest of snake 
        #not append as append will add it to the head not tail
        #new_segment.insert(0,new_segment)#no insert in turtles
        new_segment.goto(self.turtles[-1].xcor() - 20, self.turtles[-1].ycor())  # Set position relative to the tail segment
        # Add the new segment to the beginning of the turtles list
        self.turtles.insert(0, new_segment)
        


    def up (self):
        self.head.setheading(90)#setheading :for current position
    def down(self):
        self.head.setheading(270)   
    def right (self):
        self.head.setheading(0)
    def left (self):
        self.head.setheading(180)         

                

           
