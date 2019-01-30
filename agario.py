import turtle
import time
import random
import math
from ball import Ball
turtle.register_shape("pic.gif")
turtle.bgpic("pic.gif") #making a background
turtle.colormode(1)
turtle.tracer(0)
turtle.ht()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
my_ball = Ball(100, 100, 5, 5, 30, "red") #creating the balls that the players will use
your_ball = Ball(100, 100, 5, 5, 30, "blue")
number_of_balls = 5 #making sure that there will always be a certain number that will move automatically
minimum_ball_radius = 10 #giving a range of values to the radiuses of the random help
maximum_ball_radius = 100 
maximum_ball_dx = 5 #giving a range of values to the speed of the random balls
minimum_ball_dx = -5
maximum_ball_dy = 5
minimum_ball_dy = -5
BALLS = []
def attributes():
		x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius) #making a function that will generate random attributes for the balls
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

for Balls in range(number_of_balls): #giving the random balls attributes by using the "attributes" function
	x, y, dx, dy, r, color = attributes()
	Ball_1 = Ball(x, y, dx, dy, r, color)
	BALLS.append(Ball_1)
def move_all_balls(): #making a function that will move all balls inside the screen
	for ball in BALLS:
		ball.move(screen_width, screen_height)
def collide(ball_a, ball_b): #making a function that will check for collisions
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
def check_all_balls_collisions(): #making a function that uses the function "collide" to check for collisions,
	all_balls = []				  #and if a colision happens, it will make the bigger ball even bigger and the
	all_balls.append(my_ball)	  #smaller ball become a new, random ball
	all_balls.append(your_ball)
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
def UP(): #defining the keys that will be used to move the blue ball (your_ball)
	your_ball.dy = 5
	if your_ball.ycor() + your_ball.r > screen_height:
		your_ball.dy = -your_ball.dy
def DOWN():
	your_ball.dy = -5
	if your_ball.ycor() - your_ball.r < -screen_height:
		your_ball.dy = -your_ball.dy
def RIGHT():
	your_ball.dx = 5
	if your_ball.xcor() + your_ball.r > screen_width:
		your_ball.dx = -your_ball.dx
def LEFT():
	your_ball.dx = -5
	if your_ball.xcor() - your_ball.r < -screen_width:
		your_ball.dx = -your_ball.dx
turtle.Screen().onkey(UP, "Up")
turtle.Screen().onkey(DOWN, "Down")
turtle.Screen().onkey(RIGHT, "Right")
turtle.Screen().onkey(LEFT, "Left")
turtle.listen()
def W(): #defining the keys that will be used to move the red ball (my_ball)
	my_ball.dy = 5
	if my_ball.ycor() + my_ball.r > screen_height:
		my_ball.dy = -my_ball.dy
def S():
	my_ball.dy = -5
	if my_ball.ycor() - my_ball.r < -screen_height:
		my_ball.dy = -my_ball.dy
def D():
	my_ball.dx = 5
	if my_ball.xcor() + my_ball.r > screen_width:
		my_ball.dx = -my_ball.dx
def A():
	my_ball.dx = -5
	if my_ball.xcor() - my_ball.r < -screen_width:
		my_ball.dx = -my_ball.dx
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
	#print(your_ball.dx,your_ball.dy,my_ball.dx,my_ball.dy)
	turtle.Screen().update()
	time.sleep(0.05)
turtle.mainloop()