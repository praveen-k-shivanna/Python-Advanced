# Object-Oriented Programming (Turtle Graphics).

"""OOP has attributes(variable associated with a modelled object),
and methods(functions associated with the object),
Object is basically combining some data or variables and some functionalities.
We can have multiple Objects of the same type blueprint which is called Class"""


from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

