from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("yellow")
        self.penup()
        self.goto(0,300)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}" , align="center" , font=("arial",25,"normal"))    

    def increase_score(self):
        self.score+=1
        self.clear()#to delete the previous score
        self.update_scoreboard()

    def game_over(self):
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        self.write(f"Game over \nFinal score: {self.score}", align="center", font=("arial", 25 ,"bold"))  
         
