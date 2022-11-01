import random

class Card (object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def show(self):
        print ("{} of {}".format(self.val, self.suit))
    
# card1 = Card("club", 6)
# card1.show()

class Deck():
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ["Spades", "Club", "Daimonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s,v))
                # print ("{} of {}".format(v, s))
    
    def show(self):
        for c in self.cards:
            c.show()
            
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] =  self.cards[r], self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()
    
class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        
    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

    
deck = Deck()
# deck.show()
deck.shuffle()
# deck.show()
bob = Player("bob")
bob.draw(deck)
bob.showHand()
# card = deck.draw()
# card.show()