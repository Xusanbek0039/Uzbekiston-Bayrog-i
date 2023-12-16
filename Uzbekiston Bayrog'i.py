import turtle as flag

uzb = flag.Skreen()
uzb.setup(1000,600)
uzb.bgcolor('white')


text =flag.Turtle()
text.speed()
text.hideturtle()


def write(message,pas,color,font_size):
    x,y =pas
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style = ('Courier',font_size,'bold')
    text.write(message,font=style)



flag.speed(4)
flag.color('white')
flag.genup()
flag.setposition(-500,300)
flag.pendown()

hight_main = 195
width_main = 1000

def main(color):
    flag.color(color)
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(width_main)
    flag.right(90)
    flag.forward(hight_main)
    flag.right(180)
    flag.end_fill()


hight_mid = 10 
width_mid = 1000


def middle(color):
    flag.color(color)
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(width_mid)
    flag.right(90)
    flag.forward(width_mid)
    flag.right(180)
    flag.end_fill()


main("#4169E1")
middle("#CF0921")
main("#FFFFFF")
middle("#CF0921")
main("#188637")




def moon(size):
    flag.color('white')
    flag.right(90)
    flag.genup()
    flag.goto(-435,202.5)
    flag.pendown()
    flag.fillcolor('white') 
    flag.begin_fill()
    flag.circle(size)
    flag.end_fill()

    flag