#BUTTON CLASS 
from graphics import *
class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate() and deactivate() methods.
    The isClicked() method returns True if and only if the button is activated and
    pt is inside its boundaries."""

    def __init__(self,win,label,centerPt,height,width,color,font):
        """Create a rectangular button in a graphical window with the words label
        in it located at Point centerPt and with height being how tall the button
        and width being how wide the button is, e.g
        myButton = Button(myWin, "Quit", Point(300,300), 50,100)"""
        x = centerPt.getX()
        y = centerPt.getY()
        self.xmin = x - width/2
        self.xmax = x + width/2
        self.ymin = y - height/2
        self.ymax = y + height/2
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(pt1,pt2)
        self.rect = Rectangle(pt1,pt2)
        self.rect.draw(win)
        self.rect.setFill(color)
        #Text in Button
        self.words = Text(centerPt, label)
        self.words.setFace(font)
        self.words.draw(win)
        self.activate()

    def activate(self):
        """Set this button to be enabled/active"""
        self.words.setFill("black")
        self.rect.setWidth(2)
        self.active = True
    def deactivate(self):
        ##color the text dark grey
        self.words.setFill("light gray")
        ##set poutline of button to be thinner
        self.rect.setWidth(1)
        ##set the boolean active flag t be false
        self.active = False
        
    def isClicked(self,point):
        """Returns True if button active and Point is inside, else returns False"""
        if self.xmin <= point.getX() <= self.xmax \
            and self.ymin <= point.getY() <= self.ymax:
                return True
        else:
            return False
def main():
    #creates a new Graphwin object
    myWin = GraphWin("test",600,600)
    #create a new Button object
    #ie. instantiate the Button class to test it out
    myButton = Button(myWin, "Quit", Point(300,300),50,100)
    myButton.deactivate()
    pt = myWin.getMouse()
    #yButton.deactivate()
    while not myButton.isClicked(pt):
        #if the window is clicked, then activate button
        if not myButton.isClicked(pt):
            myButton.activate()
        pt = myWin.getMouse()
    myWin.close()
if __name__ == '__main__':
    main()
