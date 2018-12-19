import turtle
name = 'Tomer'
print (0 * name) #change the integer to change the number of times the variable 'name will be printed'
number1 = 4
print(number1)
number2 = number1 / 2
print(number2)
num_list = [2,4,6]
sum = 0
for num in num_list:
	print(num)
	print(2 * num)
	sum += num
print (sum)

turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.begin_fill()
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.end_fill()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.circle(25)
turtle.mainloop()