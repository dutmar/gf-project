import turtle

wn = turtle.Screen()
wn.bgcolor("turquoise")
wn.title("Turtle")

def draw_heart(size, color):
    turtle.begin_fill()
    turtle.color(color)
    turtle.left(45)
    turtle.forward(size)
    turtle.circle(size / 2, 180)
    turtle.right(90)
    turtle.circle(size / 2, 180)
    turtle.forward(size)
    turtle.end_fill()
    turtle.left(45)
    turtle.ht()

def txt():
    turtle.up()
    turtle.setpos(0, -50)
    turtle.down()
    turtle.pensize(10)
    turtle.write("Love you Bebich", align='center', font=("Arial", 16, "normal"))
    turtle.ht()

def main():
    draw_heart(100, 'purple')
    draw_heart(80, 'pink')
    draw_heart(60, 'purple')
    draw_heart(40, 'pink')
    draw_heart(20, 'purple')
    txt()
    turtle.exitonclick()

if __name__=="__main__":
    main()
