from random import shuffle

class Card:
    '''
    This class represents a Card object and contains meta information about standard playing cards.

    Attributes:
        rank (str): The rank of the Card
        suit (str): The suit of the Card
    '''
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    FACE_CARDS = set(["Jack", "Queen", "King"])

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    __repr__ = __str__

    def toValue(self):
        '''
        This function returns the int value of a card depending on it's rank.
        Face cards have a value of 10, Ace can be 1 or 11, and the rest are their face value.

        returns:
            Int value of the card
        '''
        if self.rank in Card.FACE_CARDS:
            return 10
        elif self.rank is "Ace": # Can be either 1 or 11
            return Card.getAceValue()
        else: # Numerical Value
            return int(self.rank)

    @staticmethod
    def getAceValue():
        '''
        Prompt the user for input when they draw an Ace.
        Checks for valid input until user enters either '1' or '11'

        returns:
            Int value of an Ace after valid user input
        '''
        aceVals = set(["1", "11"])
        print("You drew an Ace. Would you like it to be worth 1 or 11 points?")
        val = None
        while not val:
            val = input()
            if val in aceVals:
                return int(val)
            else:
                print("Invalid Value. Please enter a 1 or 11.")
                val = None

    @staticmethod
    def populateDeck():
        '''
        Populates and shuffles a standard 52 Card Deck

        returns:
            A randomized array of unique Cards representing every suit and rank
        '''
        deck = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                deck.append(Card(rank, suit))

        shuffle(deck)
        return deck
