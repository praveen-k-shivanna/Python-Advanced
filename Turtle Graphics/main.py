import turtle as t
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchild", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3 ,25):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

