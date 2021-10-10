import turtle as t
import time
from  snake import Snake
import food
import scoreboard as sk


screen = t.Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snake game ")


score = sk.ScoreBoard()
my_snake = Snake()
my_snake.position()
screen.update()
food = food.Food()

screen.listen()
screen.onkey(my_snake.Up,"Up")
screen.onkey(my_snake.Down,"Down")
screen.onkey(my_snake.Left,"Left")
screen.onkey(my_snake.Right,"Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.segments[0].distance(food) < 15 :
        food.refresh()
        score.add_score()
        score.score_update()
        my_snake.extend()

    if my_snake.segments[0].xcor() > 280 or my_snake.segments[0].xcor() < -280 or my_snake.segments[0].ycor() > 280 or my_snake.segments[0].ycor() < -280:
        score.refresh()
        my_snake.reset()

    for segment in my_snake.segments[1:]:
        if my_snake.segments[0].distance(segment) < 10:
            score.refresh()
            my_snake.reset()










screen.exitonclick()
