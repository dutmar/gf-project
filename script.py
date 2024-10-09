import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()

def curve():
    for i in range(200):  
        skk.right(1) 
        skk.forward(1) 

def draw():
    skk.left(120)
    skk.forward(120)

    curve()

    skk.left(120)

    curve()

    skk.forward(120)

def main():
    draw()
    skk.hideturtle

if __name__=="__main__":
    main()