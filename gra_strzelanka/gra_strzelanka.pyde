import random
celownikImg = None

class Cel:
    def __init__(self, nazwa, punkty, predkosc, sciezka_plik, rozmiar):
        self.nazwa = nazwa
        self.punkty = punkty
        self.predkosc = predkosc
        self.sciezka_plik = sciezka_plik
        self.x = 0  
        self.y = 0 
        self.kierunek_x = random.choice([-1, 1])  
        self.kierunek_y = random.choice([-1, 1])
        self.rozmiar = rozmiar 
        
    def zaladuj_plik(self, sciezka_plik):
        self.plik = loadImage(sciezka_plik)
        
    def poruszaj(self):
        self.x += self.kierunek_x * self.predkosc 
        self.y += self.kierunek_y * self.predkosc
        
        if self.x < 0 or self.x > width-self.rozmiar:
            self.kierunek_x *= -1  
        if self.y < 0 or self.y > height-self.rozmiar:
            self.kierunek_y *= -1      

                      
Jelen = Cel("Jelen", 15, 7, "data/jelen.png", 100)
Dzik = Cel("Dzik", 15, 5, "data/dzik.png", 100)
Zajac = Cel("Zajac", 10, 10, "data/zajac.png", 100)
Kotek = Cel("Kotek", -10, 8, "data/kotek.png", 100) 

start_game = False
score = 0
pauza = False
def setup():
    size(1000, 700)
    global celownikImg, pauzaImg, startImg
    Jelen.zaladuj_plik(Jelen.sciezka_plik)
    Dzik.zaladuj_plik(Dzik.sciezka_plik)
    Zajac.zaladuj_plik(Zajac.sciezka_plik)
    celownikImg = loadImage("data/celownik.png")
    Kotek.zaladuj_plik(Kotek.sciezka_plik)
    pauzaImg = loadImage("data/pauza.png")
    startImg = loadImage("data/start.png")

def draw():
    global start_game
    if not start_game:
        background(10,150,100) #zmienie na ładny obrazek jak znajdę
        fill(255)
        textSize(40)
        textAlign(CENTER, CENTER)
        text(u"Kliknij przycisk myszy, aby rozpocząć grę", width/2, height/2)
    else:
        noCursor()
        background(250)
        global pauza
        if not pauza:
            image(pauzaImg, 10, 10, 50, 50)
            Jelen.poruszaj()  
            Dzik.poruszaj()  
            Zajac.poruszaj()
            Kotek.poruszaj()
        elif pauza:
            image(startImg, 450, 300, 100, 100)
    
        image(Jelen.plik, Jelen.x, Jelen.y, Jelen.rozmiar, Jelen.rozmiar)  
        image(Dzik.plik, Dzik.x, Dzik.y, Dzik.rozmiar, Dzik.rozmiar)  
        image(Zajac.plik, Zajac.x, Zajac.y, Zajac.rozmiar, Zajac.rozmiar)
        image(celownikImg, mouseX-25, mouseY-25, 50, 50) 
        image(Kotek.plik, Kotek.x, Kotek.y, Kotek.rozmiar, Kotek.rozmiar)
        
        fill(0)
        textSize(23)
        textAlign(RIGHT, TOP)
        text("Score: " + str(score), width - 20, 20)
        
def mousePressed():
    global start_game
    if not start_game:
        start_game = True

def mouseClicked():
    global pauza, start_game
    if mouseX > 10 and mouseX < 60 and mouseY > 10 and mouseY < 60:
        pauza = True
    if mouseX > 300 and mouseX < 600 and mouseY > 150 and mouseY < 450 and pauza == True:
        pauza = False
