from turtle import Screen, Turtle
import turtle

turtle.clear()
turtle.home()
#turtle.bgcolor("gray")


CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

#create stack
class create():
    def draw_onclick_stack(self):
        import turtle
        turtle.clear()
        turtle.home()
        a=input("\n**** CREATE STACK ****")
        n=int(input("Enter the number of nodes to be drawn: "))
        loadwindow=turtle.screensize()
        turtle.ht()
        turtle.penup()
        turtle.goto(0,-250)
        turtle.st()
        turtle.pendown()
        turtle.speed(10)
        for i in range(0,n):
            b=int(input("enter elements to the node:"))
            print(i)
            turtle.ht()
            turtle.lt(90)
            turtle.fd(70)
            turtle.rt(90)
            turtle.fd(70)
            turtle.rt(90)
            turtle.fd(70)
            turtle.rt(90)
            turtle.fd(70)
            turtle.rt(90)
            #turtle.fd(70)
            #turtle.stamp()
            turtle.write(b,font="Arial",align='left')
            turtle.fd(i+70)
            turtle.rt(90)

            


#insert node
class insert(create):
    def add(self):
        c=input("\n**** PUSH OPRATION ****")
        d=int(input("Insert elements to the node:"))
        turtle.color("red")
        turtle.write(d,font="Arial",align='left')
        turtle.lt(90)
        turtle.fd(70)
        turtle.rt(90)
        turtle.fd(70)
        turtle.rt(90)
        turtle.fd(70)
        turtle.rt(90)
        turtle.fd(70)
        turtle.rt(90)

class delete(insert):
    def remove(self):
        e=input("\n**** POP OPRATION ****")
        turtle.speed(10)
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        turtle.undo()
        f=input("\n' Stack uses LIFO method,It will remove last element from stack")

              

a1 = insert()
a1.draw_onclick_stack()
a1.add()


b1 = delete()
b1.remove()

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
screen.mainloop()
