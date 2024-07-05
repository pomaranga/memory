import random

def setup():
    size(1600, 800)
    global cards, rewers, krab, rozgw, ryba, meduza
    cards = make_board()
    rewers=loadShape("Memory-plansza odwrocona.svg") # wyświetla bez fal na środku
    krab=loadShape("Memory-plansza krab.svg") # wyświetla niecałego i bez gradientu
    rozgw=loadShape("Memory-plansza rozgwiazda.svg") # za dużo punktów w grafice - przepełnia pamięć
    ryba=loadShape("Memory-plansza rybka.svg") # za dużo punktów w grafice - przepełnia pamięć
    meduza=loadShape("Memory-plansza meduza.svg") # wyświetla niecałego i bez gradientu
    

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
        
    def awers(self, value):
        if self.value == 0:
            return krab
        elif self.value == 1:
            return ryba
        elif self.value == 2:
            return rozgw
        else:
            return meduza

    def show(self):
        if self.exposed or self.found_match:
            #image(Card.awers(self, self.value), self.xpos, self.ypos, self.card_width, self.card_height) # wyświetlenie grafiki karty, ArrayIndexOutOfBoundsException/TypeError przy wywołaniu oznacza za skomplikowane grafiki (gradient? sposób zapisu formatu przez konkretny program graficzny?)/nie rozpoznane jako grafika, po uproszczeniu/naprawie można odkomentować
            text(str(self.value), self.xpos, self.ypos, self.card_width, self.card_height) # numer karty w jej rogu
        else:
            fill(150)
            shape(rewers, self.xpos, self.ypos, self.card_width, self.card_height) # wyświetlenie grafiki rewersu
            text(str(self.value), self.xpos, self.ypos, self.card_width, self.card_height)#numer karty w jej rogu
def draw():
    for card in cards:
        card.show()
            
