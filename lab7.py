# import tkinter as tk
# from tkinter import simpledialog

#Then when ever you want to ask the user for input use this code:
# greeting = simpledialog.askstring ("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
# if greeting in ["Arrr!"]:
    # print("Go away, pirate.")
# else:
	# print("Greetings, hater of pirates!")
# import tkinter as tk
# from tkinter import simpledialog

# year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

# if year <= 1900:
    # print ("Woah, that's the past!")
# elif year > 1900 and year < 2020:
    # print ("That's totally the present!")
# else:
    # print ("Far out, that's the future!!")
# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

#class Person:
 # def __init__(self, first_name, last_name):
   # self.first = first_name
    #self.last = last_name
  #def speak(self):
  	#print("My name is " +  self.first + " " + self.last)

#me = Person("Brandon", "Walsh")
#you = Person("Ethan", "Reed")

#me.speak()
#you.speak()
#import tkinter as tk
#from tkinter import simpledialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average    Grade
# 90+        A
# 80-89    B
# 70-79    C
# 60-69    D
# 0-59    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

#exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

#exam_two = int(simpledialog.askstring("Input", "exam grade two: ", parent=tk.Tk().withdraw()))

#exam_three = int(simpledialog.askstring("Input", "exam grade three: ", parent=tk.Tk().withdraw()))

#grades = [exam_one, exam_two, exam_three]
#sum = 0
#for grade in grades:
  #sum = sum + grade

#avg = sum / len(grades)
#if avg >= 90:
    #letter_grade = "A"
#elif avg >= 80 and avg < 90:
    #letter_grade = "B"
#elif avg > 69 and avg < 80:
    #letter_grade = "C"
#elif avg <= 69 and avg >= 65:
    #letter_grade = "D"
#else:
    #letter_grade = "F"

#for grade in grades:
   # print("Exam: " + str(grade))

    #print("Average: " + str(avg))

    #print("Grade: " + letter_grade)

#if letter_grade is "F":
    #print ("Student is failing.")
#else:
    #print ("Student is passing.")
class Person():
   def __init__(self, name, favorite_food, age):
       self.name = name
       self.fav_food = favorite_food
       self.age = age


   def define_color(self, color="Red"):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16)
a.define_color("Black")
a.print_info()

b = Person("Jake", "Sushi", 15)
b.print_info()
