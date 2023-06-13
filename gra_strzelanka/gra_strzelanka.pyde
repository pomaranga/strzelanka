jelenImg = None
dzikImg = None
zajacImg = None

class Cel:
    def __init__(self, nazwa, punkty, predkosc, sciezka_plik):
        self.nazwa = nazwa
        self.punkty = punkty
        self.predkosc = predkosc
        self.sciezka_plik = sciezka_plik

Jelen = Cel("Jelen", 15, 15, "data/jelen.png")
Dzik = Cel("Dzik", 15, 10, "data/dzik.png")
Zajac = Cel("Zajac", 10, 20, "data/zajac.png")

def setup():
    size(1000, 700)
    global jelenImg, dzikImg, zajacImg
    jelenImg = loadImage(Jelen.sciezka_plik)
    dzikImg = loadImage(Dzik.sciezka_plik)
    zajacImg = loadImage(Zajac.sciezka_plik)
    
def draw():
    background(255)
    image(jelenImg, 50, 50, 500, 600)
    image(dzikImg, 200, 100, 600, 600)
    image(zajacImg, 20, 400, 250, 250)
