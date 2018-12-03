class Player:
    '''
    This class represents a Player object.

    Attributes:
        hand (Card array): The cards a person is currently holding.
        value (int): The value of the cards in a persons hand.
        name (str): The name of the player which can be passed in as a param.
    '''
    num = 0

    def __init__(self, card, name=None):
        self.hand = []
        self.value = 0
        Player.num += 1
        self.name = name if name else f'Player {Player.num}' # Default name
        self.dealCard(card) # Player must be initialized with a card

    def __str__(self):
        return self.name

    __repr__ = __str__

    def dealCard(self, card):
        '''
        Adds a Card to a players hand and appends it's value.
        If the value is over 21, the player loses.

        Params:
            card (Card): The card object that the player is dealt

        Returns:
            Boolean: True if the player has lost else False
        '''
        print(f'{self} was dealt a {card}.')
        self.hand.append(card)
        self.value += card.toValue()
        print(f'Your value is now {self.value}.\n')
        if self.value > 21:
            print(f"Sorry, {self} you lost.")
            return True

        return False
