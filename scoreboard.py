from turtle import Turtle
alignment = 'center'
font = ('Quicksand', 8, 'bold' )

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('../../../OneDrive/Desktop/data.txt','r') as current_highscore:
            self.highscore = int(current_highscore.read())
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f'Current Score: {self.score} High Score: {self.highscore}',align= alignment, font= font)

    def increasescore(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        with open('../../OneDrive/Desktop/data.txt','w') as current_highscore:
            current_highscore.write(f'{self.highscore}')

