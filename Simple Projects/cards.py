class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = " "
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "<pusta>"
            return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

def add(hand,card):
    hand.cards.append(card)


card_1 = Card("A", "c")
card_2 = Card("A", "d")

hand_1 = Hand()
hand_2 = Hand()

hand_1.add(card_1)
hand_2.add(card_2)

add(hand_1, card_1)

Card.RANKS