from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("red")
        self.write(f"Puan Durumu  :{self.score}",align='center',font=FONT)

    def increase_score(self):
        self.score+=1
        self.write(f"Puan Durumu  :{self.score}",align='center',font=FONT)

class Over(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

    def game_over(self):
        self.write("Sorry, You lost! ",align="center",font=("Courier", 24, "normal") )


