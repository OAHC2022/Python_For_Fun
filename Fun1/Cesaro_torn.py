import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
alex.hideturtle()
def draw(t,order,size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [85,-170,85,0]:
            draw(t,order-1,size/2)
            t.right(angle)

def draw_squre(t,order,size):
    for i in range(4):
        draw(t,order,size)
        t.right(90)


draw_squre(alex,3,300)

wn.mainloop()