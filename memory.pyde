import random

def setup():
    size(1600, 800)
    global cards, rewers, krab, rozgw, ryba, meduza
    cards = make_board()
    rewers=loadShape("Memory-plansza odwrocona.svg")
    krab=loadShape("Memory-plansza krab.svg")
    rozgw=loadShape("Memory-plansza rozgwiazda.svg")
    ryba=loadShape("Memory-plansza rybka.svg")
    meduza=loadShape("Memory-plansza meduza.svg")

def make_board():
    values = [i for i in range(4)]*2
    random.shuffle(values)
    print(values)
    cards = []
    card_height = height / 2
    card_width = width / 4
    for row in range(2):
        row_cards = []
        for column in range(4):
            value = values.pop()
            card = Card(value, column * card_height, row * card_width, card_height, card_width)
            cards.append(card)
    return cards
    
class Card:
    def __init__(self, value, x, y, w, h):
        self.value = value
        self.xpos = x
        self.ypos = y
        self.card_width = w
        self.card_height = h
        self.exposed = False
        self.found_match = False
        self.obraz = karta()
    def karta():
        if value=0:
            return krab
        elif value=1:
            return ryba
        elif value=2:
            return rozgw
        else:
            return meduza
        

    def show(self):
        if self.exposed or self.found_match:
            image(self.obraz, self.x, self.y, self.w, self.h) # wyświetlenie grafiki karty
        else:
            fill(150)
            shape(rewers, self.xpos, self.ypos, self.card_width, self.card_height) # wyświetlenie grafiki rewersu
def draw():
    for card in cards:
        card.show()
            
