class Cel:
    def __init__(self, nazwa, punkty, predkosc, sciezka_plik):
        self.nazwa = nazwa
        self.punkty = punkty
        self.predkosc = predkosc
        self.sciezka_plik = sciezka_plik
        
    def zaladuj_plik(self, sciezka_plik):
        self.plik = loadImage(sciezka_plik)
                      
Jelen = Cel("Jelen", 15, 15, "data/jelen.png")
Dzik = Cel("Dzik", 15, 10, "data/dzik.png")
Zajac = Cel("Zajac", 10, 20, "data/zajac.png")
Celownik = Cel("Celownik", 0, 0, "data/celownik.png")

def setup():
    size(1000, 700)
    Jelen.zaladuj_plik(Jelen.sciezka_plik)
    Dzik.zaladuj_plik(Dzik.sciezka_plik)
    Zajac.zaladuj_plik(Zajac.sciezka_plik)
    Celownik.zaladuj_plik(Celownik.sciezka_plik)

def draw():
    background(255)
    image(Jelen.plik, 50, 50, 500, 600)
    image(Dzik.plik, 200, 100, 600, 600)
    image(Zajac.plik, 20, 400, 250, 250)
    image(Celownik.plik, mouseX-25, mouseY-25, 50, 50)
