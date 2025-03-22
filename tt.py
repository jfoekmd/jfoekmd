import random as r
import turtle as t

def apple_move():
    apple.ht()
    apple.setx(r.randint(-200,200))
    apple.sety(r.randint(-200,200))
    apple.st()

obstacles=[]
def createobstacle():
    obstacles=t.Turtle()
    obstacles.shape('triangle')
    obstacles.color('purple')
    obstacles.penup()
    obstacles.setx(r.randint(-t.window_width//2,t.window_width//2))
    obstacles.sety(r.randint(-t.window_height//2,t.window_height//2))



score=0
def outside_window():
    (x,y)=me.pos()
    outside=x<-t.window_width()/2 or \
    x>t.window_width()/2 or \
    y<-t.window_height()/2 or \
    y>t.window_height()/2 
    return outside
def gameover():
    score_turtle.clear()
    score_turtle.write('GAME OVER',align='right',font=('Arial',30,'normal'))

def display_score():
    score_turtle.clear()
    score_turtle.write(score,font=('Arial,30,bold'))
def move_up():
    me.setheading(90)
def move_down():
    me.setheading(270)
def move_left():
    me.setheading(180)
def move_right():
    me.setheading(0)
def start():
    global score
    apple_move()
    display_score()
    while True:
        me.forward(score/10+20)
        if me.distance(apple)<20:
            score+=10
            apple_move()
            display_score()
            createobstacle()
        if outside_window():
            gameover()
            break
      

score_turtle=t.Turtle()
score_turtle.ht()
score_turtle.penup()
x=t.window_width()/3
y=t.window_height()/3
score_turtle.setpos(x,y)







t.onkey(start,'space')
t.onkey(move_up,'w')
t.onkey(move_right,'d')
t.onkey(move_down,'s')
t.onkey(move_left,'a')
t.listen()









me=t.Turtle()
me.shape('square')
me.color('blue')
me.penup()


apple=t.Turtle()
apple.shape('circle')
apple.color('red')
apple.penup()











t.mainloop()