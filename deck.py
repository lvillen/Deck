import random

suits = ['o', 'c', 'e', 'b']
numbers = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

def createDeck():
    deck = []       
    for suit in suits:
        for number in numbers:
            deck.append(number+suit)
    return deck 

def swap(value1, value2):
    aux = value1
    value1 = value2
    value2 = aux
    return value1, value2

def shuffleDeck(list):
    for ix in range(len(list)):
        new_position = random.randrange(len(list))
        #Swapping items (cards) with empty glass technique.
        aux = list[new_position]
        list[new_position] = list[ix]
        list[ix] = aux


'''
def shuffleDeck(deck):
    deck = []
    random.randint(1, 40)
        
deck = createDeck()
shuffleDeck()

print(deck)

print("Your card is {}.".format(random.choice(deck)))
'''