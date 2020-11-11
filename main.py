import deck

suits = ['o', 'c', 'e', 'b']
numbers = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

ordered_deck = deck.createDeck(suits, numbers)
print("This is your first deck: {}".format(ordered_deck))

shuffled_deck = deck.createDeck(suits, numbers)
print("This is your second deck: {}".format(shuffled_deck))
deck.shuffleDeck(shuffled_deck)
print("This is your second deck, now shuffled and ready: {}".format(shuffled_deck))