class PlayingCard:
    """A class to represent the available playing cards in a game of blackjack."""
    def __init__(self, rank, suit):                                    #initializes playing card with rank and suit
        self.rank = rank
        self.suit = suit
                
    def getRank(self):                                                 #returns card rank
        return self.rank
   
    def getSuit(self):                                                 #returns card suit
        return self.suit

    def getValue(self):                                                #returns value of cards
        if 10 <= self.rank <= 13:                                      #all face card values (cards 10-13) set equal to 10
            self.rank = 10
        else:                                                          #all other card values set equal to their given values
            self.rank = self.rank
        return self.rank         
        
    def __str__(self):
        rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]   #hardcodes ranks 
        suit = {"d":"Diamonds", "s": "Spades", "h":"Hearts", "c":"Clubs"}                       #hardcodes suits
        card = rank[self.rank-1] + " of " + suit[self.suit]            #formats output
        return card                                                    #returns output telling user rank and suit of entered playing card



###TEST
##def main():
##    myCard = PlayingCard(12, "c")
##    print(myCard)
##
##main()
