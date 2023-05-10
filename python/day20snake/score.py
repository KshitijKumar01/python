from turtle import Turtle

PATH = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day20snake\\data.txt"



class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open(PATH, mode='r+') as file:
            self.high_score = int(file.read())
        self.score = 0 
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.updateScore()
        self.hideturtle()

    def updateScore(self ):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))

    # def game_over(self ):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            with open(PATH, mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.updateScore()

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()
