from graphics import *
import time

win = GraphWin("game_window", 400, 400)

class Squirrel:
     def draw_right_ear(self):
        right_ear = Polygon(Point(135, 50), Point(140, 70), Point(120, 70))
        right_ear.setFill("Dark Gray")
        # right_ear.draw(win)
        return right_ear
     def draw_left_ear(self):
        left_ear = Polygon(Point(65, 50), Point(60, 70), Point(80, 70))
        left_ear.setFill("Dark Gray")
        return left_ear
     def __init__(self):
         self.right_ear= self.draw_right_ear()
         self.left_ear= self.draw_left_ear()
     def draw(self, win):
        self.left_ear.draw(win)
        self.right_ear.draw(win)
     

    

Squirrel1= Squirrel()
Squirrel1.draw(win)


         
    


#         head = Circle(Point(100,100), 50)
#         head.setFill("Burlywood")
#         return head
#         # head.draw(win)

#         tongue = Circle(Point(100,120), 5)
#         tongue.setFill("Hot Pink")
#         return tongue
#         # tongue.draw(win)

#         left_mouth = Circle(Point(110,110), 10)
#         left_mouth.setFill("Dark Gray")
#         return left_mouth
#         #left_mouth.draw(win)
#         right_mouth = Circle(Point(90,110), 10)
#         right_mouth.setFill("Dark Gray")
#         return right_mouth
#         # right_mouth.draw(win)

#         right_eye = Circle(Point(120,80),5)
#         right_eye.setFill("Black")
#         right_eye.draw(win)
#         left_eye = Circle(Point(80,80),5)
#         left_eye.setFill("Black")
#         # left_eye.draw(win) 

# Squirrel.draw_squirrel(win)

welcome = Text(Point(250, 300), "Welcome to **Game Name**! \n You are a Carleton Student in CS111!")
welcome.draw(win)

input("Choose option one through 4")
# time.sleep(3)
# welcome.undraw(win)

# explain= Text(Point(250, 300), "Your objective is to get from Davis to Dacie Moses!")
# explain.draw(win)


    



# squirrel_image = Image(Point(200,200), "squirrelppm.ppm")
# squirrel_image.draw(win)
# #win.mainloop()
win.getMouse()
