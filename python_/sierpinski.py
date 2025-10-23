
import turtle

def sierpinski(order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        sierpinski(order-1, size/2)
        turtle.forward(size/2)
        sierpinski(order-1, size/2)
        turtle.backward(size/2)
        turtle.left(60)
        turtle.forward(size/2)
        turtle.right(60)
        sierpinski(order-1, size/2)
        turtle.left(60)
        turtle.backward(size/2)
        turtle.right(60)

turtle.speed(100)
sierpinski(8, 2000)