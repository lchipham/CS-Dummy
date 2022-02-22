#WORD JUMBLE (GUI INTERFACE) - Chi Pham
#Due date:  Mon, May 17 at 5 pm.

#A program that solves word jumble problems.
#The user types in a scrambled word, program generates all anagrams of the word
#and then checks which (if any) are in the dictionary.
#The anagrams ap­pearing in the dictionary are printed as solutions to the puzzle.

from graphics import *
from buttonClass import *
from wordJumble import *

def setUp(win, gwin):

    background2 = Image(Point(250,250), "sky.gif")  #background using Image object
    background2.draw(gwin)

    promptText = Text(Point(250,180), "Enter any scrambled \nword of your choice:") #prompt text using Text object
    promptText.setFace("courier")
    promptText.setFill("white")
    promptText.setStyle("bold")
    promptText.setSize(20)
    promptText.draw(gwin)

    userInput = Entry(Point(250,250),20)    #input word entry box
    userInput.setFill("white")
    userInput.setText("syk")
    userInput.draw(gwin)

    resultButton = Button(gwin, "GET RESULT", Point(180,340), 40,90, "pink", "courier")
    exitButton = Button(gwin, "EXIT", Point(320,340), 40,90, "pink", "courier")

    closewin = True                         #boolean condition set to True before while loop
    outputWord = Text(Point(250,400), "")   #output word temporarily set as empty string before input
                                            #so that for each input, the output would be displayed then cleared before a new trial
    outputWord.setSize(32)
    outputWord.setFill("white")
    outputWord.setFace("courier")
    outputWord.draw(gwin)
    while closewin:                         #while boolean condition stays True
        pt = gwin.getMouse()    
        if resultButton.isClicked(pt):      #if user clicks result button
            outputWord.setText("")          #output word set to empty string
            word_to_check = userInput.getText() #word to be checked is auto text in user Entry box
            newWord = WordJumble('2of12.txt', word_to_check) #word jumble object assigned w/ a variable
            result = newWord.check_anagrams()   #check anagrams of input word
            outputWord.setText(result)          #output is now set to the checked and rerranged anagram        
        elif exitButton.isClicked(pt):      #user clicks exit button
            closewin = False                #boolean condition turns False, window closed

        else:                               #user clicks outside button, try again
            cautionText = Text(Point(250,480), "You didn't click any button. Please try again.")  
            cautionText.setFill("white")
            cautionText.draw(gwin)         
    gwin.close()                            #boolean condition now turns False

    return False                            #so that both word jumble & main windows are closed
    win.close()

def main():
    win = GraphWin("word jumble", 500,500)
    
    introBG = Image(Point(250,250), "star.gif")     #background using Image object
    introBG.draw(win)

    introTitle = Image(Point(250,140), "cool.gif")  #title using Image object
    introTitle.draw(win)

    intro = Text(Point(250,260), "Our word jumble solver\nis a fast dictionary search:\nsimply enter a scrambled\nword, we will check and\nprint out an anagram of it.")
    intro.setFill("white")                          #intro using Text object
    intro.setFace("courier")
    intro.setSize(22)
    intro.draw(win)

    startButton = Button(win, "START", Point(200,380), 35,80, "pink", "courier")

    quitButton = Button(win, "QUIT", Point(300,380), 35,80, "pink", "courier")

    closeWin = True                         #boolean condition set to True before while loop
    while closeWin:                         #as long as boolean condition stays True
        pt = win.getMouse()
        if startButton.isClicked(pt):       #user clicks start button
            win2 = GraphWin("main program", 500,500) #pop up window created and opens
            boolean = setUp(win, win2)              #execute main setUp program

            if boolean == False:            #if this program isn't True
                closeWin = False            #window closed
        elif quitButton.isClicked(pt):      #user clicks quit button
            closeWin = False                #window closed
        else:                               #user clicks outside buttons, try again
            cautionText1 = Text(Point(250,480), "You didn't click any button. Please try again.")  
            cautionText1.setFill("white")
            cautionText1.draw(win)
    win.close()                             #boolean condition turns False, close window

main()
