"""Deck of cards
This program contains a list of cards, knows how to shuffle them
and allows the user to retrieve a card from the deck by its number.
"""
import random
from itertools import product


class Card:
    """Create attributes of class"""
    number_list = ([2, 3, 4, 5, 6, 7, 8, 9, 10] +
                   ['jack', 'queen', 'king', 'ace'])
    suit_list = ['hearts', 'diamonds', 'crosses', 'spades']

    def __init__(self, number_list: list, mast_list: list):
        """Initialize class object attributes,
        the card has 2 attributes: value and suit"""
        self.number_list = number_list
        self.suit_list = mast_list

    def __str__(self):
        """Converts the output to a string"""
        return f'{self.number_list} {self.suit_list}'


class CardsDeck:
    """This class contains three methods: create a deck of cards,
    shuffle the cards, and return a card"""
    def __init__(self):
        """This method create cards with 2 attributes: number and suit
        and packs it into a list"""
        self.cards = []

        for number, suit in product(Card.number_list, Card.suit_list):
            self.cards.append(Card(number, suit))

        self.cards.append('Joker Black')
        self.cards.append('Joker Red')

    def shuffle(self):
        """This method shuffles the cards"""
        random.shuffle(self.cards)

    def get(self, card_number: int) -> str | None:
        """This method checks range amount cards and return a card"""
        try:
            if 0 <= card_number < len(self.cards):
                return self.cards[card_number]
        except TypeError as e:
            print(e)
        return None


deck = CardsDeck()
deck.shuffle()

print(deck.get(0))
print(deck.get(27))
print(deck.get(53))

try:
    if deck:
        pass
    else:
        print('Invalid card number. '
              'Please choose a number card between 0 and 53')
except ValueError:
    print("Error! You need enter an integer")
