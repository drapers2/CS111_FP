from graphics import *

win = GraphWin("game_window", 400, 400)

class Squirrel:

    right_ear = Polygon(Point(135, 50), Point(140, 70), Point(120, 70))
    right_ear.setFill("Dark Gray")
    right_ear.draw(win)
    left_ear = Polygon(Point(65, 50), Point(60, 70), Point(80, 70))
    left_ear.setFill("Dark Gray")
    left_ear.draw(win)


    head = Circle(Point(100,100), 50)
    head.setFill("Burlywood")
    head.draw(win)

    tongue = Circle(Point(100,120), 5)
    tongue.setFill("Hot Pink")
    tongue.draw(win)

    left_mouth = Circle(Point(110,110), 10)
    left_mouth.setFill("Dark Gray")
    left_mouth.draw(win)
    right_mouth = Circle(Point(90,110), 10)
    right_mouth.setFill("Dark Gray")
    right_mouth.draw(win)

    right_eye = Circle(Point(120,80),5)
    right_eye.setFill("Black")
    right_eye.draw(win)
    left_eye = Circle(Point(80,80),5)
    left_eye.setFill("Black")
    left_eye.draw(win) 


    



# squirrel_image = Image(Point(200,200), "squirrelppm.ppm")
# squirrel_image.draw(win)
# #win.mainloop()
win.getMouse()
