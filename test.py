from unittest import TestCase, main, mock
from card import Card
from player import Player

class TestClass(TestCase):
    '''
    This class tests core functionality of Card and Player classes
    '''

    def testCardValues(self):
        print("Testing toValue() function in Card class")
        SUIT = "Spades"
        self.assertEqual(Card("1", SUIT).toValue(), 1)
        self.assertEqual(Card("2", SUIT).toValue(), 2)
        self.assertEqual(Card("3", SUIT).toValue(), 3)
        self.assertEqual(Card("4", SUIT).toValue(), 4)
        self.assertEqual(Card("5", SUIT).toValue(), 5)
        self.assertEqual(Card("6", SUIT).toValue(), 6)
        self.assertEqual(Card("7", SUIT).toValue(), 7)
        self.assertEqual(Card("8", SUIT).toValue(), 8)
        self.assertEqual(Card("9", SUIT).toValue(), 9)
        self.assertEqual(Card("10", SUIT).toValue(), 10)
        self.assertEqual(Card("Jack", SUIT).toValue(), 10)
        self.assertEqual(Card("Queen", SUIT).toValue(), 10)
        self.assertEqual(Card("King", SUIT).toValue(), 10)

    @mock.patch('card.input', create=True)
    def testAceValueInput(self, mocked_input):
        print("Testing that toValue() for Ace correctly reads and validates user input")
        SUIT = "Spades"
        mocked_input.side_effect = ['str', 'not valid', '42', '11.00', '1', '111', 'hello', '1.0', '1yes11', '11']
        ace = Card("Ace", SUIT)
        self.assertEqual(ace.toValue(), 1)

        newAce = Card("Ace", SUIT)
        self.assertEqual(newAce.toValue(), 11)

    def testPopulateDeck(self):
        print("Testing that populateDeck() function produces a valid 52 card deck")
        deck = Card.populateDeck()
        self.assertEqual(len(deck), 52)

        suitCount = {}
        rankCount = {}
        for card in deck:
            suitCount[card.suit] = suitCount.get(card.suit, 0) + 1
            rankCount[card.rank] = rankCount.get(card.rank, 0) + 1

        for key in suitCount:
            self.assertEqual(suitCount[key], 13)

        for key in rankCount:
            self.assertEqual(rankCount[key], 4)

    def testDealingCards(self):
        print("Testing that dealCard() function correctly increases value and terminates")
        SUIT = "Diamonds"

        player = Player(Card("9", SUIT))
        self.assertEqual(player.value, 9)

        done = player.dealCard(Card("3", SUIT))
        self.assertEqual(player.value, 12)
        self.assertFalse(done)

        done = player.dealCard(Card("5", SUIT))
        self.assertEqual(player.value, 17)
        self.assertFalse(done)

        done = player.dealCard(Card("Jack", SUIT))
        self.assertEqual(player.value, 27)
        self.assertTrue(done)

if __name__ == '__main__':
    main()
