from graphics import *
import time

if __name__ == "__main__":
    win = GraphWin("My window", 400, 400)
    win.setBackground("hotpink")
    my_point = Point(100,100)
    my_point.draw(win)

    my_circle= Circle(Point(50,50), 25)
    my_circle.setFill("gold")
    my_circle.setOutline("green")
    my_circle.setWidth(15)
    my_circle.draw(win)

    my_rectangle= Rectangle(Point(300,300), Point(250,250))
    my_rectangle.draw(win)

    my_message= Text(Point(100, 200), "Hello, World!")
    my_message.setSize(20)
    my_message.draw(win)

    for _ in range (20):
        time.sleep(.5)
        my_circle.move(10,0)
        my_rectangle.move(-10,0)

    win.getMouse()