import turtle as t 
import random
import time

t.hideturtle()
t.speed(0) 
t.tracer(0)
wn = t.Screen()
wn.setup(456, 280)

colors = ['green', 'orange', 'red', 'yellow']  # colors of shapes
x_main = -150  # left_x coordinate of the sea
y_main = -600  # bottom_y coordinate of the sea
size_main_y = 1200  # size of lines of sea
size_main_x = 300  # size of lines of sea
xs = 0 
speed_x = 3
best = 0  # initial best record (it changes after every game)
xx = 0  # initial x_location of fish
yy = -60  # initial y_location of fish
main_speed = 1  # initial speed of movements
f = main_speed  # used for current speed of moves
sizz = 10  # size of the fish

def clickk(x=0, y=50):  # when mouse clicked this function works
    startt()

def startt():  # this function is the main function of the game and everything will happen from this
    global f
    global w
    global xx
    global yy
    global now
    global per 
    global main_speed
    w = 0
    f = main_speed
    t.bgcolor('white')
    xx = 0
    yy = -60
    while True:
        while len(enemys) > 0:  # delete information of the last game
            del enemys[0]
        now = time.time()
        if now - per > .1:  # this will increase the score by 1 in every .1 second 
            w += 1
            f = main_speed + w / 100
            per = time.time()
        textt(w)
        main_shape()
        mainfish(xx, yy, sizz)
        now = time.time()
        if now - per > .1:  # this will increase the score by 1 in every .1 second
            w += 1
            f = main_speed + w / 100
            per = time.time()
        textt(w)
        for _ in range(5):
            enemys.append(shapes())  # append the shapes as class (shapes) to the list
        for _ in range(5):
            enemys.append(shapes2())  # append the shapes as class (shapes2) to the list
        e = 550 // f  # change the time of loop based on the (f)=(current speed)
        e = int(e)
        for _ in range(e):
            now = time.time()
            if now - per > .1:  # this will increase the score by 1 in every .1 second
                w += 1
                f = main_speed + w / 100
                per = time.time()
            textt(w)
            main_shape()
            now = time.time()
            mainfish(xx, yy, sizz)
            for enemy in enemys:
                enemy.move_ment()
                if (abs(enemy.y - enemy.size - yy) <= sizz or abs(enemy.y - enemy.size / 2 - yy) <= sizz) and (abs(enemy.x - xx) <= sizz or abs(enemy.x + 2 * enemy.size - xx) <= sizz or abs(enemy.x + enemy.size - xx) <= sizz):  # this will check if any shape collided with the fish 
                    time.sleep(1) 
                    ending()
            t.update()  
            t.clear()              
def ending():  # after collision with shapes this function will end the previous game and start another one
    # also it will show the (best record) and current scores of the game
    global best
    global w
    t.clear()
    t.color('white')
    t.bgcolor('black')
    t.penup()
    t.goto(-140, 80)
    t.pendown()
    t.write("Game Over", font=("Arial", 30, "normal"))
    t.penup()
    t.goto(-140, 60)
    t.pendown()
    best = max(best, w)
    t.color('yellow')
    t.write("Best: " + str(best), font=("Arial", 23, "normal"))
    t.penup()
    t.goto(150, 100)
    t.pendown()
    t.color('white')
    t.write(str(w), font=('Arial', 20, "normal"))
    t.update()
    per = time.time()
    while True:
        now = time.time()
        if now - per > 2.:
            t.bgcolor('white')
            main_shape()
            mainfish(0, -60, 10)
            w = 0
            textt(w)
            t.penup()
            t.goto(-150, 50)
            t.pendown()
            t.color(1, 1, 0)
            t.write("Click to Start", font=("Arial", 34, "normal"))
            t.mainloop()
            break

class shapes:  # used for drawing the shapes and moving them
    def __init__(self):
        global f
        self.size = 20
        self.x = random.randint(2, 8) * 40 - 200
        self.y = random.randint(0, 4) * 40 + 140
        self.color = colors[random.randint(0, len(colors) - 1)]
        self.speed = f
        self.size = random.randint(10, 19)

    def happen(self):
        t.up()
        t.setpos(self.x, self.y - self.size)
        t.down()
        t.begin_fill()
        t.setpos(self.x + 2 * self.size, self.y - self.size)
        t.setpos(self.x + 2 * self.size, self.y - self.size / 2)
        t.setpos(self.x, self.y - self.size / 2)
        t.setpos(self.x, self.y - self.size) 
        t.end_fill()

    def move_ment(self):
        self.y -= self.speed
        t.up()
        t.setpos(self.x, self.y - self.size)
        t.down()
        t.color(self.color)
        t.begin_fill()
        t.setpos(self.x + 2 * self.size, self.y - self.size)
        t.setpos(self.x + 2 * self.size, self.y - self.size / 2)
        t.setpos(self.x, self.y - self.size / 2)
        t.setpos(self.x, self.y - self.size) 
        t.end_fill()
        t.color('black')

class shapes2:  # used for drawing the shapes and moving them
    def __init__(self):
        global f
        self.size = 20
        self.x = random.randint(2, 8) * 40 - 200
        self.y = random.randint(5, 8) * 40 + 140
        self.color = colors[random.randint(0, len(colors) - 1)]
        self.speed = f
        self.size = random.randint(10, 19)

    def happen(self):
        t.up()
        t.setpos(self.x, self.y - self.size)
        t.down()
        t.begin_fill()
        t.circle(self.size)
        t.end_fill()

    def move_ment(self):
        self.y -= self.speed
        t.up()
        t.setpos(self.x, self.y - self.size)
        t.down()
        t.color(self.color)
        t.begin_fill()
        t.setpos(self.x + 2 * self.size, self.y - self.size)
        t.setpos(self.x + 2 * self.size, self.y - self.size / 2)
        t.setpos(self.x, self.y - self.size / 2)
        t.setpos(self.x, self.y - self.size) 
        t.end_fill()
        t.color('black')

def main_shape():  # drawing the sea 
    t.up()
    t.goto(x_main, y_main)
    t.down()
    t.color('black', (0, 0, .5))
    t.begin_fill()
    t.goto(x_main + size_main_x, y_main)
    t.goto(x_main + size_main_x, y_main + size_main_y)
    t.goto(x_main, y_main + size_main_y)
    t.goto(x_main, y_main)
    t.end_fill()

def mainfish(mcarx, mcary, sizz):  # drawing the fish
    global xs
    global speed_x
    if xs >= 15 or xs <= -15:
        speed_x = -speed_x
    xs += speed_x
    t.up()
    t.goto(mcarx, mcary - sizz)
    t.down()
    t.color(1, 0, 1)
    t.begin_fill()
    t.circle(sizz)
    t.end_fill()
    t.up()
    t.goto(mcarx, mcary - sizz)
    t.down()
    t.begin_fill()
    t.goto(mcarx - xs, mcary - sizz - 15)
    t.goto(mcarx + xs, mcary - sizz - 15)
    t.goto(mcarx, mcary - sizz)
    t.end_fill()
    t.up()
    t.goto(mcarx, mcary + 1)
    t.color('black')
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def textt(w):  # showing the current score and best record every moment at the top of the page
    t.color('black')
    t.penup()
    t.goto(150, 100)
    t.pendown()
    t.write(str(w), font=('Arial', 20, "normal"))
    t.penup()
    t.goto(-214, 100)
    t.pendown()
    t.color('gray')
    t.write("BEST: ", font=('Arial', 20, "normal"))
    t.penup()
    t.goto(-210, 70)
    t.pendown()
    t.write(str(best), font=('Arial', 20, "normal"))

enemys = []  # list to use for appending and moving several class instances 

def leftt():  # move main fish to the left 
    global xx
    global yy
    if xx - 30 >= -150:
        xx -= 15
    mainfish(xx, yy, sizz)

def rightt():  # move main fish to the right
    global xx
    global yy
    if xx + 30 <= 150:
        xx += 15
    mainfish(xx, yy, sizz)

def upp():  # move main fish up
    global xx
    global yy
    yy += 12
    mainfish(xx, yy, sizz)

def downn():  # move main fish down
    global xx
    global yy
    yy -= 12
    mainfish(xx, yy, sizz)

now = time.time()
per = time.time()
# (now) and (per) are for using to calculate score and delay between games 
now = per + 1.
re = 2
w = 0
t.listen()
t.onkeypress(leftt, "Left")
t.onkeypress(rightt, "Right")
t.onkeypress(upp, "Up")
t.onkeypress(downn, "Down")
# use keyboard to move fish anywhere
t.onscreenclick(clickk)
# use mouse to start the game initially and after every game over
t.bgcolor('white')
main_shape()
mainfish(0, -60, 10)
w = 0
textt(w)
t.penup()
t.goto(-150, 50)
t.pendown()
t.color(1, 1, 0)
t.write("Click to Start", font=("Arial", 34, "normal"))
t.mainloop()
