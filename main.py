import random

values = "A 2 3 4 5 6 7 8 9 T J Q K".split()
suits = "♣️ ♠️ ♥️ ♦️".split()
deck = []

for value in values:
    for suit in suits:
        deck.append(value + suit)

def shuffleDeck(deck):
    random.shuffle(deck)

def dealCard(deck):
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    board = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop(),]
    return player, dealer, board

def result(player, dealer, board):
    print("Player: ", player)
    print("Dealer: ", dealer)
    print("Board: ", board)

shuffleDeck(deck)
player, dealer, board = dealCard(deck)
result(player, dealer, board)
