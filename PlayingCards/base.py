
class Card:
    def __init__(self, value, suit, colour="red"):
        self.suit = suit
        self.value = value
        self.colour = colour
        self.suit_color = "red" if suit in ("h", "d") else "black"

    def __str__(self):
        return f"{self.value}{self.suit}"

    def __repr__(self):
        return str(self)


class Joker(Card):
    pass


class Hand:
    def __init__(self, *cards, player="unknown"):
        self.cards = cards
        self.player = player

    def __str__(self):
        return f"Hand[{', '.join([str(card) for card in self.cards])}]"

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Deck{" + f"{len(self.cards)}" + "}"

    def __repr__(self):
        return str(self)
