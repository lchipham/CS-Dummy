from graphics import*
from buttonClass import*
from PlayingCard import*
from Deck import*
from random import*

class BlackJack:
    '''A class to generate cards and dealer plays to play a game of Blackjack'''
    
    def __init__(self, dealerHand = [], playerHand = []):    #constructor to initialize instance variables
        '''_init__(self, dHand=[], pHand=[])
        constructor that initializes instance variables, it also gives the playingDeck an initial shuffle
        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with'''
        self.dHand = dealerHand
        self.pHand = playerHand                              #instance variables
        self.playingDeck = Deck()
        self.playingDeck.shuffle()                           #constructor to shuffle cards

    def initDeal(self, gwin, xposD1, xposD2, yposD1, yposD2, xposP1, xposP2, yposP1, yposP2): #corresponding values for positions: 20,40,45,45,20,40,65,65
        '''initDeal(self,gwin,xposD,yposD,xposP,yposP):
        deals out initial cards, 2 per player and displays dealer and player hands on
        graphical win xposD and yposD give initial position for dealer cards, xposP and yposP are analogous'''
        facedown_dCardVal = self.playingDeck.dealCard()
        self.dHand.append(facedown_dCardVal)
        facedown_dCardImage = Image(Point(xposD1,yposD1), "playingcards/b1fv.gif")  
        facedown_dCardImage.draw(gwin)                  #generates first facedown dealer card with a value that gets appended to dealer hand
    
        init_pCard = self.playingDeck.dealCard()   #generates first player card and appends it to player hand
        self.pHand.append(init_pCard)
        image_pCard = Image(Point(xposP1,yposP1), "playingcards/" + init_pCard.getSuit() + str(init_pCard.getRank()) + ".gif")
        image_pCard.draw(gwin)

        init_dCard = self.playingDeck.dealCard()   #generates second dealer card and appends it to dealer hand
        self.dHand.append(init_dCard)
        image_dCard = Image(Point(xposD2,yposD2), "playingcards/" + init_dCard.getSuit() + str(init_dCard.getRank()) + ".gif")
        image_dCard.draw(gwin)
    
        init_pCard = self.playingDeck.dealCard()    #generates second player card and appends it to player hand
        self.pHand.append(init_pCard)
        image_pCard = Image(Point(xposP2,yposP2), "playingcards/" + init_pCard.getSuit() + str(init_pCard.getRank()) + ".gif")
        image_pCard.draw(gwin)

        return facedown_dCardVal                    #returns facedown_dCardVal so it can be used during dealer card reveal

    def hit(self, gwin, xPos, yPos):                #adds a new card to the player's hand if they hit
        '''hit(self, gwin, xPos, yPos) adds a new card to the player's hand and places it at xPos, yPos'''
        addedCards = self.playingDeck.dealCard()    #new player card dealt
        image_addedCards = Image(Point(xPos, yPos), "playingcards/" + addedCards.suit + str(addedCards.rank) + ".gif") 
        image_addedCards.draw(gwin)                 #card's value is retrieved and card is drawn from playingcard folder
        self.pHand.append(addedCards)

    def evaluateHand(self, hand):                   #evaluates hands by implementing BlackJack rules for card vals
        '''evaluateHand(self, hand)totals the cards in the hand that is passed in and returns total
           (ace counts as 11 if doing so allows total to stay under 21)'''
        tot = 0                                    
        hasAce = False                              #Boolean condition set before loop
        for card in hand:
            cardVal = card.getValue()
            if card.getValue() == 1:                #creates condition if Ace takes 1 as its value
                hasAce = True
            tot = tot + cardVal
        if hasAce and tot + 10 <= 21:               #creates condition if Ace takes 11 as its value and the total card value doesn't go above 21
            tot = tot + 10
        return tot


    def dealerPlays(self, gwin, xPos, yPos):
        ''' dealearPlays(self, gwin, xPos, yPos) dealer deals cards to herself, stopping when hitting "soft 17"'''
        dTot = self.evaluateHand(self.dHand)        #variabel to store dealer total; set originally to the value of 2 auto-generated dealer cards 
        while dTot < 17:                            
            dCard = self.playingDeck.dealCard()     #new dealer card dealt
            image_dCard = Image(Point(xPos,yPos), "playingcards/" + dCard.getSuit() + str(dCard.getRank()) + ".gif") #deals if player tot is <= 17, dealer plays
            image_dCard.draw(gwin)
            self.dHand.append(dCard)                #new dealer card appended into existing list of dealer cards
            dTot = self.evaluateHand(self.dHand)
            xPos = xPos + 20                        #incrementing position dealer cards are drawn in 
            
        return dTot
 
