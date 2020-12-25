import turtle as p
import random
def snow(snow_count):
    p.hideturtle()
    p.speed(500)
    p.pensize(2)
    for i in range(snow_count):
        r = random.random()
        g = random.random()
        b = random.random()
        p.pencolor(r,g,b)
        p.pu()
        p.goto(random.randint(-350,350),random.randint(1,270))
        p.pd()
        dens = random.randint(8,12)
        snowsize = random.randint(10,14)
        for _ in range(dens):
            p.forward(snowsize)
            p.backward(snowsize)
            p.right(360 / dens)
def ground(ground_line_count):
    p.hideturtle()
    p.speed(500)
    for i in range(ground_line_count):
        p.pensize(random.randint(5,10))
        x=random.randint(-400,350)
        y=random.randint(-280,-1)
        r=-y/280
        g=-y/280
        b=-y/280
        p.pencolor(r,g,b)
        p.penup()
        p.goto(x,y)
        p.pendown()
        p.forward(random.randint(40,100))
def main():
    p.setup(800,600,0,0)
    #p.tracer(False)
    p.bgcolor("white")
    snow(30)
    ground(30)
    #p.tracer(True)
    p.mainloop()

main()



