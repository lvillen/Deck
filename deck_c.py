import deck

class Deck():
    def __init__(self, suits, numbers):
        self.suits = suits
        self.numbers = numbers
        self.deck = deck.createDeck(suits, numbers)
    
    def shuffle(self):
        deck.shuffle(self.deck)

    def givecards(self, player_num, card_num):
        players = []
        for i in range(player_num):
            players.append([])

        for card in range(card_num):
            for player in range(player_num):
                players[player].append(self.deck.pop(0))

        return players
     

'''
            podríamos hacer:
            for player in range(player_num):
                card = self.deck.pop()
                players[player].append(card)
'''


'''
How to create the deck:
    deck = []       
        for suit in suits:
            for number in numbers:
                self.deck.append(number+suit)
    self.deck = deck

Also:
        self.deck = []       
        for suit in suits:
            for number in numbers:
                self.deck.append(number+suit)


How to shuffle the deck can also be done either way:
-Importing (as it is done right now).
-Writing the code:
    def shuffle(self):
        for ix in range(len(self.desk)):
            new_position = random.randrange(len(self.desk))
            #Swapping items (cards) with empty glass technique.
            aux = list[new_position]
            list[new_position] = list[ix]
            list[ix] = aux
'''