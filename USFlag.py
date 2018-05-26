#  File: USFlag.py
#  Description: Use turtle graphics to draw the US flag
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 9/14/16
#  Date Last Modified:9/16/16

def drawWhiteStar(ttl,radius,startx,starty):
    ttl.setheading(0)
    ttl.fillcolor("white")
    ttl.penup()
    ttl.goto(startx,starty)
    angle = 144
    ttl.pendown()
    ttl.begin_fill()
    for i in range(5):
        ttl.right(angle)
        ttl.forward(radius)
        ttl.left(72-angle)
        ttl.forward(radius)
    ttl.end_fill()    

def main():

    import turtle

    hoist = input("Enter the height of the hoist in pixels: ")
    hoist = float(hoist)
    width = 1.9 * hoist
    

    ttl = turtle.Turtle() 

    ttl.speed(0)
    screen = turtle.Screen()
    screen.setup(width + 200,hoist + 200,0,0)
    screen.title ("'Murica")
    screen.bgcolor ("white")

    ttl.fillcolor("blue")
    ttl.penup()
    ttl.goto(-width/2,hoist/2)
    ttl.pendown()

    canton_height = hoist * (7/13)
    canton_width = width * 0.4
    ttl.begin_fill()
    ttl.forward(canton_width)
    ttl.right(90)
    ttl.forward(canton_height)
    ttl.right(90)
    ttl.forward(canton_width)
    ttl.right(90)
    ttl.forward(canton_height)
    ttl.right(90)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(canton_width)

    stripeLen = width - canton_width
    stripeWid = hoist / 13
    
    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(2 * stripeWid)
    ttl.left(90)

    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(2 * stripeWid)
    ttl.left(90)

    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(2 * stripeWid)
    ttl.left(90)

    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(stripeLen)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()    

    
    ttl.penup()
    ttl.forward(2 * stripeWid)
    ttl.right(90)
    ttl.forward(canton_width)
    ttl.left(180)

    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(2 * stripeWid)
    ttl.left(90)

    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(2 * stripeWid)
    ttl.left(90)

    ttl.fillcolor("red")
    ttl.pendown()
    ttl.begin_fill()
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(90)
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(stripeWid)
    ttl.right(180)
    ttl.end_fill()

    ttl.penup()
    ttl.forward(stripeWid)
    ttl.left(90)

    ttl.pendown()
    ttl.forward(width)
    ttl.left(90)
    ttl.forward(hoist)
    ttl.left(90)
    ttl.forward(width)
    ttl.left(90)
    ttl.forward(hoist)
    ttl.left(90)


    radius = (0.8 * stripeWid) / 2
    E = canton_height / 10
    G = canton_width / 12
    
    ttl.penup()
    ttl.goto(-width/2,hoist/2)

    startx = -width/2 + G
    starty = hoist/2 - E

    for i in range(6):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G
    
    ttl.penup()
    startx = -width/2 + 2*G
    starty = hoist/2 - 2*E

    for i in range(5):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    ttl.penup()
    startx = -width/2 + G
    starty = hoist/2 - 3*E

    for i in range(6):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    ttl.penup()
    startx = -width/2 + 2*G
    starty = hoist/2 - 4*E

    for i in range(5):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    ttl.penup()
    startx = -width/2 + G
    starty = hoist/2 - 5*E
    
    for i in range(6):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    ttl.penup()
    startx = -width/2 + 2*G
    starty = hoist/2 - 6*E

    for i in range(5):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    
    ttl.penup()
    startx = -width/2 + G
    starty = hoist/2 - 7*E

    for i in range(6):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    ttl.penup()
    startx = -width/2 + 2*G
    starty = hoist/2 - 8*E

    for i in range(5):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    ttl.penup()
    startx = -width/2 + G
    starty = hoist/2 - 9*E

    for i in range(6):
        drawWhiteStar(ttl,radius,startx,starty)
        startx += 2*G

    turtle.done() 

main() 
