import turtle as t



class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.point = 0
        with open("data.txt",mode="r") as file:

            self.high_point = int(file.read())
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.score_update()

    def add_score(self):
        self.point += 1

    def score_update(self):
        self.clear()
        self.write(f"Score = {self.point}  High score {self.high_point}",align = "center",font=("Arial", 14, "normal"))

    def refresh(self):
        if self.point > self.high_point:
            self.high_point = self.point
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_point))
        self.point = 0
        self.score_update()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=("Arial", 14, "normal"))




