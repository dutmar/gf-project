import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.speed('fastest')

def curve():
    for i in range(200):  
        skk.right(1) 
        skk.forward(1) 

def draw():
    skk.fillcolor('purple')
    skk.begin_fill()

    skk.left(140)
    skk.forward(113)

    curve()

    skk.left(120)

    curve()

    skk.forward(112)

    skk.end_fill()

def txt():
    skk.up()
    skk.setpos(-50, -50)
    skk.down()
    skk.pensize(10)
    skk.write("Love you Bebich", font=("Arial", 16, "normal"))
    skk.ht()

def main():
    draw()
    txt()
    turtle.exitonclick()

if __name__=="__main__":
    main()