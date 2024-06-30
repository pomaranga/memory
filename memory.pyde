def setup():
    size(1600, 800)
    plansza=loadShape("Memory-plansza odwrocona.svg")
    krab=loadShape("Memory-plansza krab.svg")
    rozgw=loadShape("Memory-plansza rozgwiazda.svg")
    ryba=loadShape("Memory-plansza rybka.svg")
    meduza=loadShape("Memory-plansza meduza.svg")
    
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
        if self.exposed or self.found:
            image(self.obraz, self.x, self.y, self.w, self.h)
        else:
            fill(150)
            rect(self.x, self.y, self.w, self.h)
            
