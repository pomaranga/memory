def setup():
    size(800, 800)
    global game

def mousepressed():
    game.mouse_pressed(mouseX, mouseY)
    
class Card:
    def __init__(self, value, x, y, w, h):
        self.value = value
        self.xpos = x
        self.ypos = y
        self.card_width = w
        self.card_height = h
        self.exposed = False
        self.found = False
        self.hidden = False

    def show(self):
        if self.exposed or self.found:
            image(self.obraz, self.x, self.y, self.w, self.h)
        else:
            fill(150)
            rect(self.x, self.y, self.w, self.h)
            
