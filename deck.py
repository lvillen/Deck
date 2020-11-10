suits = ['o', 'c', 'e', 'b']
numbers = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

def createDeck():
    deck = []       
    for suit in suits:
        for number in numbers:
            deck.append(number+suit)
    return deck 