import deck_c

suits = ['o', 'c', 'e', 'b']
numbers = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

deck1 = deck_c.Deck(suits, numbers)
print("This is your ordered deck: {}.".format(deck1.deck))
deck1.shuffle()
print("Now, for something completely different: {}".format(deck1.deck))