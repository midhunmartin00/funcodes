import turtle
import time
def draw_square():
    window=turtle.Screen()
    window.bgcolor("#aaff34")
    me=turtle.Turtle()
    me.speed(1)
    me.shape("classic")
    me.forward(100)
    me.right(90)
    time.sleep(0.5)
    me.forward(100)
    me.right(90)
    time.sleep(0.5)
    me.forward(100)
    me.right(90)
    time.sleep(0.5)
    me.forward(100)
    me.right(90)
    window.exitonclick()

draw_square()

     
