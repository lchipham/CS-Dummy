#FUN WITH MATH - Chi Pham
#Due date: Mon, May 17 at 5 pm.

#A fun and easy-to-use math program with 3 sub programs
#Decription of each program is below:
#Program 1: Calculate Exponents
#Program 2: Convert a base 10 number to any other base 
#Program 3: Compute the number of ways k items can be selected from a pool of n items 

from graphics import *
from buttonClass import *

def exponent(a, n): 
    '''raises a to the int power n'''
    if n == 0:
        return 1
    else:
        factor = exponent(a,n//2)
        if n%2 == 0: #n is even
            return factor * factor
        else: #n is odd
            return factor*factor*a
        
def baseConversion(digitList, num, base):
    ''' Convert a base 10 number to any base '''
    if num < base:              #base case: if input number's value is less than base
        #print(num)
        digitList.append(num)   #append input num into list, since the result of division is 0, with the smaller num as remnant
    else:                       #recursive case
        digit = num % base      #first, division 
        num = num // base       #second, update num value 
        baseConversion(digitList,num, base) #call function again
        #print(digit)
        digitList.append(digit) #append division result into list
    return digitList

def numWays(n, k):
    ''' Calculate the number of ways to select k number from a size of n items'''
    if k == 1:              #if num items = 1 -> num of ways to select equals pool size
        ways = n
    elif n < k:             #if size of pool is smaller than num of items to be selected
        ways = 0            #then there would be no way
    else:                   #recursive case
        ways = numWays(n - 1, k - 1) + numWays(n-1, k)
    return ways

def play_program1(gwin):
  
    gwin_bg = Image(Point(200,200), "pinkbg.gif")           #background using Image object
    gwin_bg.draw(gwin)

    p2_title = Text(Point(200,110), "Exponent Calculator")  #title using Text object
    p2_title.setFace("times roman")
    p2_title.setFill(color_rgb(255,153,153))
    p2_title.setSize(32)
    p2_title.draw(gwin)

    inputNum = Entry(Point(260,170), 20)                    #ENTRY BOX for input number
    inputNum.setFill("lavender")
    inputNum.setText("26")
    inputNum.draw(gwin)

    inputPower = Entry(Point(260,200), 20)                  #ENTRY BOX for input power
    inputPower.setFill("lavender")
    inputPower.setText("9")
    inputPower.draw(gwin)

    ask_num = Text(Point(120,170), "Enter a number")        #prompt text using Text object
    ask_num.setFill("black")
    ask_num.setFace("courier")
    ask_num.setSize(14)
    ask_num.draw(gwin)

    ask_power = Text(Point(120,200), "Enter a power ")      #prompt text using Text object
    ask_power.setFill("black")
    ask_power.setFace("courier")
    ask_power.setSize(14)
    ask_power.draw(gwin)

    p1_result = Button(gwin, "RESULT", Point(200, 260), 40,70, "pink", "courier")   #get result button
    quitP1 = Button(gwin, "QUIT", Point(365, 20), 30,50, "pink", "courier")         #quit program 1 button
    pt = gwin.getMouse()
    
    while not quitP1.isClicked(pt):         #as long as quit button is not clicked
        if not p1_result.isClicked(pt):     #if user clicks outside, try again
            tryagain = Text(Point(200,380), "You didn't click any button. Try again")
            tryagain.setFace("courier")
            tryagain.setFill("black")
            tryagain.draw(gwin)
            pt = gwin.getMouse()
            tryagain.undraw()
        else:                               #if get result button is clicked, display output
            result = exponent(int(inputNum.getText()), int(inputPower.getText())) #format output to integers
            outputNum = Text(Point(200,310), result)
            outputNum.setSize(26)
            outputNum.setFill(color_rgb(255,153,153))
            outputNum.setFace("courier")
            outputNum.draw(gwin)
            pt = gwin.getMouse()
            outputNum.undraw()
        
    gwin.close()                            #quit button is clicked, program window closed

def play_program2(gwin):

    win2_bg = Image(Point(200,200), "pinkbg.gif")           #background using Image object
    win2_bg.draw(gwin)

    p2_title = Text(Point(200,110), "BASE CONVERSION")      #title using Text objetc
    p2_title.setFace("times roman")
    p2_title.setFill(color_rgb(255,153,153))
    p2_title.setSize(32)
    p2_title.draw(gwin)

    inputNum = Entry(Point(260,170), 20)                    #Entry box to enter number
    inputNum.setFill("lavender")
    inputNum.setText("46")
    inputNum.draw(gwin)

    inputBase = Entry(Point(260,200), 20)                   #Entry box to enter base
    inputBase.setFill("lavender")
    inputBase.setText("2")
    inputBase.draw(gwin)

    ask_num = Text(Point(120,170), "Enter a number")        #prompt text using Text object
    ask_num.setFill("black")
    ask_num.setFace("courier")
    ask_num.setSize(14)
    ask_num.draw(gwin)

    ask_power = Text(Point(120,200), "Enter a base ")       #prompt text using Text object
    ask_power.setFill("black")
    ask_power.setFace("courier")
    ask_power.setSize(14)
    ask_power.draw(gwin)

    p1_result = Button(gwin, "RESULT", Point(200, 260), 40,70, "pink", "courier")   #get result button
    quitP1 = Button(gwin, "QUIT", Point(365, 20), 30,50, "pink", "courier")         #quit program 2 button
    pt = gwin.getMouse()
    while not quitP1.isClicked(pt):             #as long as quit button is not clicked
        if not p1_result.isClicked(pt):         #if user clicks outside button, try again
            tryagain = Text(Point(200,380), "You didn't click any button. Try again")
            tryagain.setFace("courier")
            tryagain.setFill("black")
            tryagain.draw(gwin)
            pt = gwin.getMouse()
            tryagain.undraw()
        else:                                   #user clicked get result button, display output
            digitList = baseConversion([],int(inputNum.getText()), int(inputBase.getText())) #assign a variable to baseConversion object
            newList = []                        #empty list to store separate items (test print on line 26)
            for i in digitList:                 #for each item in original digitlist
                i = str(i)                      #format string
                newList.append(i)               #then append into newList
            converted_result = " ".join(newList)#the desired output is put together from items in newList
            outputNum = Text(Point(200,310), converted_result)
            outputNum.setSize(26)
            outputNum.setFill(color_rgb(255,153,153))
            outputNum.setFace("courier")
            outputNum.draw(gwin)
            pt = gwin.getMouse()                #another click 
            outputNum.undraw()                  #then the output from the previous try would be cleared, leaving space for ouputs of next trials
    
    gwin.close()                                #quit button is clicked, program window closed

def play_program3(gwin):
    
    win2_bg = Image(Point(200,200), "pinkbg.gif")           #background using Image object
    win2_bg.draw(gwin)

    p2_title = Text(Point(200,110), "Ways to Select")       #title using Text object
    p2_title.setFace("times roman")
    p2_title.setFill(color_rgb(255,153,153))
    p2_title.setSize(32)
    p2_title.draw(gwin)

    inputNum = Entry(Point(260,170), 20)                    #Entry box to input number of items to be selected
    inputNum.setFill("lavender")
    inputNum.setText("2")
    inputNum.draw(gwin)

    inputSize = Entry(Point(260,200), 20)                   #Entry box to input size of pool
    inputSize.setFill("lavender")
    inputSize.setText("75")
    inputSize.draw(gwin)

    ask_num = Text(Point(120,170), "num of items")          #prompt text using Text object
    ask_num.setFill("black")
    ask_num.setFace("courier")
    ask_num.setSize(14)
    ask_num.draw(gwin)

    ask_power = Text(Point(120,200), "size of pool")        #prompt text using Text object
    ask_power.setFill("black")
    ask_power.setFace("courier")
    ask_power.setSize(14)
    ask_power.draw(gwin)

    p1_result = Button(gwin, "RESULT", Point(200, 260), 40,70, "pink", "courier")   #get result button
    quitP1 = Button(gwin, "QUIT", Point(365, 20), 30,50, "pink", "courier")         #quit program 3 button
    pt = gwin.getMouse()
    while not quitP1.isClicked(pt):         #as long as quit button is not clicked
        if not p1_result.isClicked(pt):     #user clicks outside of button, try again
            tryagain = Text(Point(200,380), "You didn't click any button. Try again")
            tryagain.setFace("courier")
            tryagain.setFill("black")
            tryagain.draw(gwin)
            pt = gwin.getMouse()
            tryagain.undraw()
        else:                               #get result button is clicked, display output
            result = numWays(int(inputSize.getText()), int(inputNum.getText()))
            outputNum = Text(Point(200,310), str(result)+" ways")
            outputNum.setSize(26)
            outputNum.setFill(color_rgb(255,153,153))
            outputNum.setFace("courier")
            outputNum.draw(gwin)
            pt = gwin.getMouse()
            outputNum.undraw()
    
    gwin.close()                            #quit button is clicked, program window closed

def main():

    win = GraphWin("MATH PROGRAM", 800, 800)
    win.setBackground("white")
    
    intro = Image(Point(400,400),"mathh.gif")       #background using Image object
    intro.draw(win)
    search = Image(Point(400,350),"searchBox.gif")  #search bar using Image object
    search.draw(win)

    title = Text(Point(385,355), "Arithmetic Calculators")   #title using Text object
    title.setFace("courier")
    title.setSize(18)
    title.draw(win)

    program1 = Button(win, "PROGRAM 1", Point(200,550), 50,100, "pink", "courier")
    program2 = Button(win, "PROGRAM 2", Point(400,550), 50,100, "pink", "courier")
    program3 = Button(win, "PROGRAM 3", Point(600,550), 50,100, "pink", "courier")
    exitButton = Button(win, "EXIT", Point(730,30), 40,80, "white", "courier")

    closeWin = True                 #boolean condition set to true before while loop
    
    while closeWin:                 #as long as this condition is true
        pt = win.getMouse()         #get a mouse click
        if program1.isClicked(pt):  #user chooses program 1
            win2 = GraphWin("Exponent Caculator", 400,400) #open pop up window
            play_program1(win2)                             #execute program 1

        elif program2.isClicked(pt): #user chooses prohram 2
            win3 = GraphWin("Base Conversion", 400,400)     #open pop up window
            play_program2(win3)                             #execute program 2

        elif program3.isClicked(pt): #user chooses program 3
            win4 = GraphWin("Ways To Select", 400,400)      #open pop up window
            play_program3(win4)                             #execute program 3
    
        elif exitButton.isClicked(pt):#user exits program
            closeWin = False        #then boolean conditiion turns false -> window closed
        else:                       #user clicks outside buttons, try again
            tryagain = Text(Point(400,730), "You didn't click any button. Try again")
            tryagain.setFace("courier")
            tryagain.setFill("black")
            tryagain.draw(win)
    win.close()                     #closeWin condition turns False, window closed

main()
