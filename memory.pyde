import random

def setup():
    size(1600, 800)
    global cards
    cards = make_board()
    plansza=loadShape("Memory-plansza odwrocona.svg")
    krab=loadShape("Memory-plansza krab.svg")
    rozgw=loadShape("Memory-plansza rozgwiazda.svg")
    ryba=loadShape("Memory-plansza rybka.svg")
    meduza=loadShape("Memory-plansza meduza.svg")

def make_board():
    values = [i for i in range(4)]*2
    random.shuffle(values)
    cards = []
    card_height = height / 2
    card_width = width / 4
    for row in range(2):
        row_cards = []
        for column in range(4):
            value = values.pop()
            card = Card(value, row * card_height, column * card_width, card_height, card_width)
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

    def show(self):
        if self.exposed or self.found_match:
            image(self.obraz, self.x, self.y, self.w, self.h)
        else:
            fill(150)
            rect(self.x, self.y, self.w, self.h)
def draw():
    for card in cards:
        card.show()    
# teraz czas na funkcję draw i wyświetylenie kart wczytanych w setup'ie i stworzonych w make_board
            
