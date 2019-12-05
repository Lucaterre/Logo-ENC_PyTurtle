"""
*******************************************
*******************************************
** LOGO DE L'ECOLE NATIONALE DES CHARTES **
***********************––––––––************
**********************|  O  /O |***********
2019 - TNAH *********(|    |   |)**********
**********************|   ---  |***********
***********************–––––––––***********
"""

### BIBLIOTHEQUE

import turtle

### FCT(GRAPHIQUE)


def cd_graph():
    turtle.speed(17)
    turtle.goto (0,0)
    turtle.left(90)
    turtle.forward(500)
    turtle.goto(0,0)
    turtle.right(90)
    turtle.forward(500)
    turtle.goto(0,0)
    turtle.right(90)
    turtle.forward(500)
    turtle.goto(0,0)
    turtle.right(90)
    turtle.forward(500)
    turtle.goto(0,0)
    return

### FCT(OVALE)

def draw_oval(x,y,big_radius,small_radius,tilt):
    turtle.color('white')
    turtle.up()
    turtle.width(25)
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(180+tilt)
    turtle.circle(big_radius,90)
    turtle.circle(small_radius,90)
    turtle.width(15)
    turtle.circle(big_radius,90)
    turtle.circle(small_radius,90)
    return


###APPELLE FCT(GRAPHIQUE)

#cd_graph()

###PARAMETRES GENERAUX

t = turtle.Turtle()
t.showturtle()
t.shape("turtle") #forme
t.speed(5) #vitesse
turtle.color('blue') #couleur
t.penup()

###DESSIN DES RECTANGLES

#premier rectangle
t.goto(50,50)
t.pendown()
t.color("red", "red")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.end_fill()

t.penup()

#deuxième rectangle

t.goto(0,15)
t.pendown()
t.color("red", "red")
t.begin_fill()
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.end_fill()
t.penup()

#troisieme rectangle

t.goto(105,-30)
t.pendown()
t.color("red", "red")
t.begin_fill()
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()

###DESSIN DU 'C' INTERIEUR


#premier ovale

draw_oval(-10,80,100,54,43)
t.penup()

#1er triangle dans 1er rectangle

t.goto(92,50)
t.pendown()
t.color('white','white')
t.begin_fill()
t.forward(46)
t.left(90)
t.forward(40)
t.end_fill()
t.penup()

#2e triangle dans 2eme rectangle

t.goto(0,95)
t.pendown()
t.color('white','white')
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(40)
t.end_fill()

t.penup()

#3e triangle dans 3eme rectangle

t.goto(84,-25)
t.pendown()
t.color('white','white')
t.begin_fill()
t.width(15)
t.left(90)
t.left(90)
t.left(90)
t.left(90)
t.forward(46)
t.right(90)
t.forward(40)
t.end_fill()

t.penup()

#tracer un cercle


t.goto(10,270)
t.pendown()
t.color('black')
t.width(3)
t.circle (250)

#ecrire

t.write("Ecole nationale des chartes !", True, font=("Arial", 20, "italic"))


###PARAMETRES DE FIN

t.hideturtle()

turtle.done()

###FIN
