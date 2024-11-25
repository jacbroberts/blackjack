import random

class Card:
    def __init__(self,suit,rank, hidden):
        self.suits = ["C","D","H","S"]
        self.ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.suit = suit
        self.rank = rank #1-A, 2-2, ..., 10-10, J-11, Q-12, K-13
        self.hidden = hidden
        if self.rank < 11:
            self.value = self.rank
        else:
            self.value = 10
        if self.rank == 1:
            self.value = 11

    def setValue(self,value):
        #for setting A to 11 rather than 1
        self.value = value

    def hideCard(self,hidden):
        self.hidden = hidden

    def print_card(self):
        if self.rank == 1:
            r = "A"
        elif self.rank == 11:
            r = "J"
        elif self.rank == 12:
            r = "Q"
        elif self.rank == 13:
            r = "K"
        else:
            r = self.rank

        if self.suit == 1:
            s = "♣"
        elif self.suit == 2:
            s = "♦"
        elif self.suit == 3:
            s = "♥"
        else:
            s = "♠"

        if self.hidden == False:
            print(f"{r}{s}",end='')
        else:
            print("xx", end='')

class Deck:
    def __init__(self,decks):
        
        self.deck = []
        for i in range(1,5):
            for j in range(1,14):
                self.deck.append(Card(i,j,True))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        card = self.deck.pop()
        return card


    def show_deck(self):
        #shows cards from end of array to beginning but does not draw them
        for card in self.deck:
            card.print_card()

class Hand:
    def __init__(self):
        self.value = 0
        self.hand = []
    
    def draw_card(self, deck):
        new_card = deck.draw_card()
        new_card.hideCard(False)
        self.hand.append(new_card)
        self.value += new_card.value
        if self.value > 21:
            ace = self.has_ace()
            if ace != None:
                
                ace.setValue(1)
        self.value = 0
        for i in self.hand:
            self.value += i.value

    def get_shown_value(self):
        value = 0
        for card in self.hand:
            if card.hidden == False:
                value += card.value
        return value

    def print_hand(self):
        for card in self.hand:            
            card.print_card()
            print(" ",end='')
        print(f" value: {self.get_shown_value()}")

    def has_ace(self):
        ace = None
        for card in self.hand:
            if card.rank == 1:
                ace = card
        return ace

def dealer(deck, hand):
    value = hand.value
    while value < 17:
        hand.draw_card(deck)
        value = hand.value
        if value > 21:
            ace = hand.has_ace()
            if ace != None:
                ace.setValue(1)
        if value == 21:
            break
