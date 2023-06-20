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

# Dodanie koordynatów celów 
Jelen.x = 100
Jelen.y = 50

Dzik.x = 200
Dzik.y = 150

Zajac.x = 300
Zajac.y = 100

Kotek.x = 400
Kotek.y = 200

start_game = False
score = 0
pauza = False
def setup():
    size(1000, 700)
    global celownikImg, pauzaImg, startImg, tloImg, restartImg
    Jelen.zaladuj_plik(Jelen.sciezka_plik)
    Dzik.zaladuj_plik(Dzik.sciezka_plik)
    Zajac.zaladuj_plik(Zajac.sciezka_plik)
    celownikImg = loadImage("data/celownik.png")
    Kotek.zaladuj_plik(Kotek.sciezka_plik)
    pauzaImg = loadImage("data/pauza.png")
    startImg = loadImage("data/start.png")
    restartImg = loadImage("data/restart.png")
    tloImg = loadImage("data/tlo.jpg")

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
        image(tloImg, 0, 0, width, height)
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
        image(Kotek.plik, Kotek.x, Kotek.y, Kotek.rozmiar, Kotek.rozmiar)
        image(restartImg, 10, 70, 50, 50)
        image(celownikImg, mouseX-25, mouseY-25, 50, 50) 
        
        fill(0)
        textSize(23)
        textAlign(RIGHT, TOP)
        text("Score: " + str(score), width - 20, 20)
        
def mousePressed():
    global start_game
    if not start_game:
        start_game = True

def mouseClicked():
    global pauza, score
    if mouseX > 10 and mouseX < 60 and mouseY > 10 and mouseY < 60:
        pauza = True
    if mouseX > 300 and mouseX < 600 and mouseY > 150 and mouseY < 450 and pauza == True:
        pauza = False
    # sprawdzenie czy celownik najeżdża na cel i usunięcie go po trafieniu
    if mouseX > Jelen.x and mouseX < Jelen.x + Jelen.rozmiar and mouseY > Jelen.y and mouseY < Jelen.y + Jelen.rozmiar and pauza == False:
        Jelen.x = -200  # Przesuwa cel za ekran
        Jelen.y = -200
        score += 20
    if mouseX > Dzik.x and mouseX < Dzik.x + Dzik.rozmiar and mouseY > Dzik.y and mouseY < Dzik.y + Dzik.rozmiar and pauza == False:
        Dzik.x = -200
        Dzik.y = -200
        score += 10
    if mouseX > Zajac.x and mouseX < Zajac.x + Zajac.rozmiar and mouseY > Zajac.y and mouseY < Zajac.y + Zajac.rozmiar and pauza == False:
        Zajac.x = -200
        Zajac.y = -200
        score += 30
    if mouseX > Kotek.x and mouseX < Kotek.x + Kotek.rozmiar and mouseY > Kotek.y and mouseY < Kotek.y + Kotek.rozmiar and pauza == False:
        Kotek.x = -200
        Kotek.y = -200
        score = 0
    if mouseX > 10 and mouseX < 60 and mouseY > 70 and mouseY < 120:
        reset()

def reset():
    global score
    score = 0
    Jelen.x = 100
    Jelen.y = 50
    
    Dzik.x = 200
    Dzik.y = 150
    
    Zajac.x = 300
    Zajac.y = 100
  
    Kotek.x = 400
    Kotek.y = 200
