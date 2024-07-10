import random

menu = 0
menu_w_trakcie_gry = 1

class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = millis()
        self.time_left = duration
        self.finished = False
    
    def update(self):
        elapsed_time = (millis() - self.start_time) / 1000
        self.time_left = max(0, self.duration - elapsed_time)
        if self.time_left == 0 and not self.finished:
            self.finished = True
    
    def display(self, x, y):
        fill(0)
        textSize(32)
        textAlign(CENTER, CENTER)
        text(str(int(self.time_left)), x, y)
    
    def show_game_over(self):
        fill(255, 0, 0)
        textSize(64)
        textAlign(CENTER, CENTER)
        text("Przegrales", width / 2, height / 2)

class Card:
    def __init__(self, value, x, y, w, h):
        self.value = value
        self.xpos = x
        self.ypos = y
        self.card_width = w
        self.card_height = h
        self.exposed = False
        self.found_match = False
        
    def awers(self):
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
            shape(self.awers(), self.xpos, self.ypos, self.card_width, self.card_height)
        else:
            fill(150)
            shape(rewers, self.xpos, self.ypos, self.card_width, self.card_height)
        fill(0)
        text(str(self.value), self.xpos + 10, self.ypos + 40)  # Wyświetlanie numeru karty w jej rogu

def setup():
    size(1600, 800)
    global cards, rewers, krab, rozgw, ryba, meduza, timer, Punkty, stan_gry, najlepsze wyniki
    cards = make_board()
    rewers = loadShape("Memory-plansza odwrocona.svg")
    krab = loadShape("crab-animal-crustacean-svgrepo-com.svg")
    rozgw = loadShape("turtle-4-svgrepo-com.svg")
    ryba = loadShape("fish-svgrepo-com.svg")
    meduza = loadShape("octopus-1-svgrepo-com.svg")
    textSize(32)
    timer = CountdownTimer(30)  # Czas jaki odlicza tiemr do przegranej
    Punkty = 0
    stan_gry = menu
    najlepsze_wyniki = []
    
def initialize_game():
    global cards, timer, Punkty
    cards = make_board()
    timer = CountdownTimer(30)
    Punkty = 0

def make_board():
    values = [i for i in range(4)] * 2
    random.shuffle(values)
    cards = []
    card_width = 300 #zmienilem wielkosci bo nie bylo miejsca na timer i na punkty
    card_height = 350 #zmienilem wielkosci bo nie bylo miejsca na timer i na punkty
    for row in range(2):
        for column in range(4):
            value = values.pop()
            card = Card(value, column * card_width, row * card_height, card_width, card_height)
            cards.append(card)
    return cards

def draw():
    global stan_gry
    background(143,170,229,255)  # Czyszczenie tła przed rysowaniem, bo napisy nachodziły na siebie. TROCHE MI ZAJELO SZUKANIE KOLORU TEGO CO JEST ZA KARTAMI -_-
    
    if stan_gry == menu:
        display_menu()
    elif stan_gry == menu_w_trakcie_gry:
        timer.update()
        if timer.finished:
            global stan_gry
            stan_gry = menu
            update_high_scores()  # aktualizacja najlepszych wyników
        else:
            for card in cards:
                card.show()
            timer.display(width - 100, 50)  # Timer w górnym prawym rogu
            display_Punkty(width - 100, 100)  # Punkty pod czasem
        
def display_menu():
    fill(0)
    textSize(64)
    textAlign(CENTER, CENTER)
    text("Memory", width / 2, height / 2 - 100)
    textSize(32)
    text("Kliknij aby rozpoczac gre", width / 2, height / 2)
    text("Najlepsze wyniki: " + ', '.join(map(str, najlepsze_wyniki)), width / 2, height / 2 + 50)  # Wyświetlanie najlepszych wyników

def update_high_scores():
    global najlepsze_wyniki, Punkty
    najlepsze_wyniki.append(Punkty)  # dodanie wyniku do listy najlepszych wyników
    najlepsze_wyniki.sort(reverse=True)  # sortowanie od najwiekszego

            
def mousePressed():
    global Punkty, stan_gry, cards, timer
    if stan_gry == menu:
        stan_gry = menu_w_trakcie_gry
        cards = make_board()
        timer = CountdownTimer(30)
        Punkty = 0
    elif stan_gry == menu_w_trakcie_gry:
        for card in cards:
            if card.xpos < mouseX < card.xpos + card.card_width and card.ypos < mouseY < card.ypos + card.card_height:
                if not card.exposed and not card.found_match:
                    card.exposed = True
                    check_matches()
                    break

def check_matches():
    global cards, Punkty
    exposed_cards = [card for card in cards if card.exposed and not card.found_match]
    if len(exposed_cards) == 2:
        if exposed_cards[0].value == exposed_cards[1].value:
            for card in exposed_cards:
                card.found_match = True
            Punkty += 1  # Zwiększanie punktacji za znalezienie pary kart
        else:
            for card in exposed_cards:
                card.found_match = False
                card.exposed = False
                
def display_Punkty(x, y):
    fill(0)
    textSize(32)
    textAlign(CENTER, CENTER)
    text("Punkty: " + str(Punkty), x, y)
