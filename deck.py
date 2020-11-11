import random

def createDeck(suits, numbers):
    deck = []       
    for suit in suits:
        for number in numbers:
            deck.append(number+suit)
    return deck 

def shuffle(list):
    for ix in range(len(list)):
        new_position = random.randrange(len(list))
        #Swapping items (cards) with empty glass technique.
        aux = list[new_position]
        list[new_position] = list[ix]
        list[ix] = aux