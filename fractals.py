import turtle as t

def sierpinski():
    global tscreen
    t.Screen().bgcolor("black")
    tscreen = t.getscreen()
    t.speed(1000) 
    t.pensize(2)
    t.pencolor("white")
    t.penup()
    t.goto(-400,-400) 
    t.pendown()
    t.left(60)

    for _ in range(3):
        for _ in range(3):
            for _ in range(3):
                for _ in range(3):
                    for _ in range(3):
                        for _ in range(3):
                            for _ in range(3):
                                t.forward(12.5)
                                t.right(120)
                            t.forward(25)
                            t.right(120)
                        t.forward(50)
                        t.right(120)
                    t.forward(100)
                    t.right(120)
                t.forward(200)
                t.right(120)
            t.forward(400)
            t.right(120)
        t.forward(800)
        t.right(120)              
def hexaspiral():
    global tscreen
    t.Screen().bgcolor("black")
    tscreen = t.getscreen()
    t.speed(1000) 
    t.pensize(2)
    t.pencolor("white")
    t.penup()
    t.goto(0,0) 
    t.pendown()
    t.left(90)

    for _ in range(90):
        t.penup()
        t.forward(100)
        t.right(90)
        t.pendown()
        for _ in range(6):
            t.forward(200)
            t.right(60)
        t.penup()
        t.right(90)
        t.forward(100)
        t.right(176)
        
sierpinski()




