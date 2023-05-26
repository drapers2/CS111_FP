from graphics import *
import time
import button

win = GraphWin("game_window", 400, 400)

class Squirrel:
      def __init__(self, color ):
         self.color= color
         self.right_ear= self.draw_right_ear()
         self.left_ear= self.draw_left_ear()
         self.head= self.draw_head(self.color)
         self.tongue= self.draw_tongue()
         self.left_mouth= self.draw_left_mouth()
         self.right_mouth= self.draw_right_mouth()
         self.right_eye= self.draw_right_eye()
         self.left_eye= self.draw_left_eye()
      def draw_right_ear(self):
        right_ear = Polygon(Point(135, 50), Point(140, 70), Point(120, 70))
        right_ear.setFill("Dark Gray")
        return right_ear
      def draw_left_ear(self):
        left_ear = Polygon(Point(65, 50), Point(60, 70), Point(80, 70))
        left_ear.setFill("Dark Gray")
        return left_ear
      def draw_head(self, color):
          head = Circle(Point(100,100), 50)
          head.setFill(self.color)
          return head
      def draw_tongue(self):
         tongue = Circle(Point(100,120), 5)
         tongue.setFill("Hot Pink")
         return tongue
      def draw_left_mouth(self):
         left_mouth = Circle(Point(110,110), 10)
         left_mouth.setFill("Dark Gray")
         return left_mouth
      def draw_right_mouth(self):
         right_mouth = Circle(Point(90,110), 10)
         right_mouth.setFill("Dark Gray")
         return right_mouth
      def draw_right_eye(self):
         right_eye = Circle(Point(120,80),5)
         right_eye.setFill("Black")
         return right_eye
      def draw_left_eye(self):
         left_eye = Circle(Point(80,80),5)
         left_eye.setFill("Black")
         return left_eye
      def draw(self, win):
        self.left_ear.draw(win)
        self.right_ear.draw(win)
        self.head.draw(win)
        self.tongue.draw(win)
        self.right_eye.draw(win)
        self.left_eye.draw(win)
        self.left_mouth.draw(win)
        self.right_mouth.draw(win)

def draw_wait(variable):
   variable.draw(win)
   time.sleep(3)
   variable.undraw()
# Squirrel1= Squirrel("green")
# Squirrel1.draw(win)


welcome = Text(Point(250, 300), "Welcome to **Game Name**! \n You are a Carleton Student in CS111!")
draw_wait(welcome)




explain= Text(Point(250, 300), "Your objective is to get from Davis to Dacie Moses \n to bake cookies for your CS111 professor!")
draw_wait(explain)
explain= Text(Point(250, 300), "If you don't bring him cookies, you'll fail your project!")
draw_wait(explain)
explain= Text(Point(250, 300), "But 4 squirrel guards are intent on stopping you!\n What time of day will you venture?")
draw_wait(explain)

morning= button.Button(Point(50, 150), "Morning")
morning.draw(win)
afternoon= button.Button(Point(50, 200), "Afternoon")
afternoon.draw(win)
evening= button.Button(Point(50, 250), "Evening")
evening.draw(win)
night= button.Button(Point(50, 300), "Night")
night.draw(win)









    

win.getMouse()
