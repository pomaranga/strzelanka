jelenImg = None
dzikImg = None
zajacImg = None
celownikImg = None

class Cel:
    def __init__(self, nazwa, punkty, predkosc, sciezka_plik):
        self.nazwa = nazwa
        self.punkty = punkty
        self.predkosc = predkosc
        self.sciezka_plik = sciezka_plik

class Celownik:
    def __init__(self, sciezka_plik):
        self.sciezka_plik = sciezka_plik

Jelen = Cel("Jelen", 15, 15, "data/jelen.png")
Dzik = Cel("Dzik", 15, 10, "data/dzik.png")
Zajac = Cel("Zajac", 10, 20, "data/zajac.png")

Celownik = Celownik("data/celownik.png")

def setup():
    size(1000, 700)
    global jelenImg, dzikImg, zajacImg, celownikImg
    jelenImg = loadImage(Jelen.sciezka_plik)
    dzikImg = loadImage(Dzik.sciezka_plik)
    zajacImg = loadImage(Zajac.sciezka_plik)
    celownikImg = loadImage(Celownik.sciezka_plik)

def draw():
    background(255)
    image(jelenImg, 50, 50, 500, 600)
    image(dzikImg, 200, 100, 600, 600)
    image(zajacImg, 20, 400, 250, 250)
    image(celownikImg, mouseX-25, mouseY-25, 50, 50)
