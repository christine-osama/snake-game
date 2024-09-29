#Game window  #Loop
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
window = Screen()
window.setup(width=800, height=800)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)#no drawing will be displayed until call the update() func.

snake=Snake() #self=snake(object)then create_snake
food=Food()
score=Scoreboard()
game_on=True
while game_on:
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.up,"Up")#control through keyboard
    window.onkey(snake.down,"Down")
    window.onkey(snake.right,"Right")
    window.onkey(snake.left,"Left")
    if snake.head.distance(food) < 15:
        food.appear()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() >370 or  snake.head.xcor() <-370 or snake.head.ycor() >300 or snake.head.ycor() <-300  :
        game_on =False
        score.game_over()

    for segment in snake.turtles[0:-1]:
        if snake.head.distance(segment)<10:
            game_on=False
            score.game_over()    
        
window.exitonclick()