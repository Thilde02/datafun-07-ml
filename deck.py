# deck.py example: A simple deck of cards program

import random

class Card:
    """Represents a single playing card"""
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Represents a deck of 52 playing cards"""
    
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop() if self.cards else None

# Testing the Deck and Card classes
if __name__ == "__main__":
    deck = Deck()
    print("Drawing a card from the deck:")
    card = deck.draw_card()
    if card:
        print(f"You drew the {card}")
    else:
        print("The deck is empty.")
