import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(1)
turtle.tracer(0)
turtle.ht()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
my_ball = Ball(100, 400, 5, 5, 30, "red")
your_ball = Ball(100, 400, 5, 5, 30, "blue")
number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
maximum_ball_dx = 5
minimum_ball_dx = -5
maximum_ball_dy = 5
minimum_ball_dy = -5
BALLS = []
def attributes():
		x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
		y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
		dx = random.randint(minimum_ball_dx, maximum_ball_dx)
		while dx == 0:
			dx = random.randint(minimum_ball_dx, maximum_ball_dx)
		dy = random.randint(minimum_ball_dy, maximum_ball_dy)
		while dy == 0:
			dy = random.randint(minimum_ball_dy, maximum_ball_dy)		
		r = random.randint(minimum_ball_radius, maximum_ball_radius)
		color = (random.random(), random.random(), random.random())
		return(x, y, dx, dy, r, color)

for Balls in range(number_of_balls):
	x, y, dx, dy, r, color = attributes()
	Ball_1 = Ball(x, y, dx, dy, r, color)
	BALLS.append(Ball_1)
BALLS.append(your_ball)
def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width, screen_height)
def collide(ball_a, ball_b):
		x1 = ball_a.xcor()
		x2 = ball_b.xcor()
		y1 = ball_a.ycor()
		y2 = ball_b.ycor()
		d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
		if ball_a == ball_b:
			return False
		if d <= ball_a.r + ball_b.r:
			return True
		else:
			return False
def check_all_balls_collisions():
	all_balls = []
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
		for ball_a in all_balls:
			for ball_b in all_balls:
				r1 = ball_a.r
			r2 = ball_b.r
			if collide(ball_a, ball_b):
				x, y, dx, dy, r, color = attributes()
				if r1 > r2:
					ball_a.r = ball_a.r + 1
					ball_a.shapesize(ball_a.r/10)
					ball_b.new_Ball(x, y, dx, dy, r, color)
					if my_ball == ball_b:
						running = False
					if your_ball == ball_b:
						running = False
					if your_ball == ball_a:
						your_ball.r = your_ball.r + 1
						your_ball.shapesize(your_ball.r/10)
				if r2 > r1:
					ball_b.r = ball_b.r + 1
					ball_b.shapesize(ball_b.r/10)
					ball_a.new_Ball(x, y, dx, dy, r,color)
					if my_ball == ball_a:
						running = False	 
					if your_ball == ball_a:
						running = False
					if your_ball == ball_b:
						your_ball.r = your_ball.r + 1
						your_ball.shapesize(your_ball.r/10)
def UP():
	your_ball.dy = 5
def DOWN():
	your_ball.dy = -5
def RIGHT():
	your_ball.dx = 5
def LEFT():
	your_ball.dx = -5
turtle.Screen().onkey(UP, "Up")
turtle.Screen().onkey(DOWN, "Down")
turtle.Screen().onkey(RIGHT, "Right")
turtle.Screen().onkey(LEFT, "Left")
turtle.listen()
def W():
	my_ball.dy = 5
def S():
	my_ball.dy = -5
def D():
	my_ball.dx = 5
def A():
	my_ball.dx = -5
turtle.Screen().onkey(W, "w")
turtle.Screen().onkey(S, "s")
turtle.Screen().onkey(D, "d")
turtle.Screen().onkey(A, "a")
turtle.listen()
#def movearound():
	#my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width, screen_height - turtle.getcanvas().winfo_pointery())
while running:
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	#movearound()
	move_all_balls()
	check_all_balls_collisions()
	my_ball.move(screen_width, screen_height)
	your_ball.move(screen_width, screen_height)
	turtle.Screen().update()
	time.sleep(0.05)
turtle.mainloop()