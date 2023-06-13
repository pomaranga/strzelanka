jelenImg = None
dzikImg = None
zajacImg = None

class Cel:
    def __init__(self, nazwa, punkty, predkosc):
        self.nazwa = nazwa
        self.punkty = punkty
        self.predkosc = predkosc

Jelen = Cel("Jelen", 15, 15)
Dzik = Cel("Dzik", 15, 10,)
Zajac = Cel("Zajac", 10, 20)

def setup():
    size(1000, 700)
    global jelenImg, dzikImg, zajacImg
    jelenImg = loadImage("data/jelen.png")
    dzikImg = loadImage("data/dzik.png")
    zajacImg = loadImage("data/zajac.png")
    
def draw():
    background(255)
    image(jelenImg, 50, 50, 500, 600)
    image(dzikImg, 200, 100, 600, 600)
    image(zajacImg, 20, 400, 250, 250)
