import random
class Cel:
    def __init__(self, nazwa, punkty, predkosc, sciezka_plik):
        self.nazwa = nazwa
        self.punkty = punkty
        self.predkosc = predkosc
        self.sciezka_plik = sciezka_plik
        self.x = 0  
        self.y = 0 
        self.kierunek_x = random.choice([-1, 1])  
        self.kierunek_y = random.choice([-1, 1])  
        
    def zaladuj_plik(self, sciezka_plik):
        self.plik = loadImage(sciezka_plik)
        
    def poruszaj(self):
        self.x += self.kierunek_x * self.predkosc  
        self.y += self.kierunek_y * self.predkosc  
        
        if self.x < 0 or self.x > width:
            self.kierunek_x *= -1  
        if self.y < 0 or self.y > height:
            self.kierunek_y *= -1      

                      
Jelen = Cel("Jelen", 15, 15, "data/jelen.png")
Dzik = Cel("Dzik", 15, 10, "data/dzik.png")
Zajac = Cel("Zajac", 10, 20, "data/zajac.png")
Celownik = Cel("Celownik", 0, 0, "data/celownik.png")


start_game = False

def setup():
    size(1000, 700)
    Jelen.zaladuj_plik(Jelen.sciezka_plik)
    Dzik.zaladuj_plik(Dzik.sciezka_plik)
    Zajac.zaladuj_plik(Zajac.sciezka_plik)
    Celownik.zaladuj_plik(Celownik.sciezka_plik)

def draw():
    global start_game
    if not start_game:
        background(10,150,100) #zmienie na ładny obrazek jak znajdę
        fill(255)
        textSize(40)
        textAlign(CENTER, CENTER)
        text(u"Kliknij przycisk myszy, aby rozpocząć grę", width/2, height/2)
    else:
        background(255)
        Jelen.poruszaj()  
        Dzik.poruszaj()  
        Zajac.poruszaj() 
    
        image(Jelen.plik, Jelen.x, Jelen.y, 100, 100)  
        image(Dzik.plik, Dzik.x, Dzik.y, 100, 100)  
        image(Zajac.plik, Zajac.x, Zajac.y, 100, 100)
        image(Celownik.plik, mouseX-25, mouseY-25, 50, 50)  
