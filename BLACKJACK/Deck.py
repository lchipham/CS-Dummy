from PlayingCard import*
from random import*

class Deck:
    """A class to represent a deck of cards"""
    def __init__(self):                          #initializes deck class
        suit = ["c", "d", "h", "s"]              #creates list of potential suits
        self.deck = []                           #creates empty list to store card values ---> suits and ranks
        for suits in suit:                       #loops through suits
            for ranks in range(1,14):            #loops through ranks
                card = PlayingCard(ranks, suits) #generates cards with each possible suit and rank using PlayingCard class
                self.deck.append(card)           #appends created card to self.deck (4 suits * 13 ranks = 52 total cards) to create deck


    def shuffle(self):                         #method to shuffle cards
        shuffledCards = []                     #list to store shuffled cards
        for oldCard in range(len(self.deck)):  #loops through/shuffles each of the 52 cards in "old" positions of list self.deck
            newCard = randrange(0,52)          #generates a random rank number value to replace "old" card value with a "new" card value in list self.deck 
            self.deck[oldCard], self.deck[newCard] = self.deck[newCard], self.deck[oldCard] #shuffles cards; takes card in position "oldCard" of cardList                                                                                           
        return self.deck                         #returns shuffled deck of cards                                    #and replaces it with randomly generated "newCard" 52x  

    def dealCard(self):                          #method to deal first card from the top of the deck and remove it from deck
        return self.deck.pop(0)                  #pops off first item in deck and returns value of card
        

    def cardsLeft(self):                         #method to return the number of cards left in deck
        return len(self.deck)                    #returns the length of current deck when called


###TEST
##def main():
##    n = int(input("How many cards would you like to deal out? "))
##    myDeck = Deck()
##    myDeck.shuffle()
##    for i in range(n):
##        print(myDeck.dealCard())
##main()                
            
            
            
            
            
                
                
