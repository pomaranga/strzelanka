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
Bazant = Cel("Bazant", 15,5, "data/bazant.png", 100)
Sarna = Cel("Sarna", 15, 10, "data/sarna.png", 100)
Lis = Cel("Lis", 150, 20, "data/lis.png", 100)
Zyrafa = Cel("Zyrafa", 5, 10, "data/zyrafa.png", 100)
Boss = Cel("Boss", 100, 5, "data/boss.png", 200)

# Dodanie koordynatów celów 
Jelen.x = 100
Jelen.y = 50

Dzik.x = 200
Dzik.y = 150

Zajac.x = 300
Zajac.y = 100

Kotek.x = 400
Kotek.y = 200

Bazant.x = 500
Bazant.y = 300

Sarna.x = 100
Sarna.y = 50

Lis.x = 150
Lis.y = 100

Zyrafa.x = 250
Zyrafa.y = 400

Boss.x = 100
Boss.y = 300

start_game = False
score = 0
pauza = False
def setup():
    size(1000, 700)
    global celownikImg, pauzaImg, startImg, tloImg, restartImg, tlostartImg, wyjscieImg, trafieniabossa
    Jelen.zaladuj_plik(Jelen.sciezka_plik)
    Dzik.zaladuj_plik(Dzik.sciezka_plik)
    Zajac.zaladuj_plik(Zajac.sciezka_plik)
    Lis.zaladuj_plik(Lis.sciezka_plik)
    Zyrafa.zaladuj_plik(Zyrafa.sciezka_plik)
    celownikImg = loadImage("data/celownik.png")
    Kotek.zaladuj_plik(Kotek.sciezka_plik)
    pauzaImg = loadImage("data/pauza.png")
    startImg = loadImage("data/start.png")
    restartImg = loadImage("data/restart.png")
    tloImg = loadImage("data/tlo.jpg")
    Bazant.zaladuj_plik(Bazant.sciezka_plik)
    Sarna.zaladuj_plik(Sarna.sciezka_plik)
    Boss.zaladuj_plik(Boss.sciezka_plik)
    tlostartImg = loadImage("data/tstart.png")
    wyjscieImg = loadImage("data/exit.png")
    trafieniabossa = 0

def draw():
    global start_game, tlostartImg
    if not start_game:
        background(tlostartImg)
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
            Bazant.poruszaj()
            Sarna.poruszaj()
            Boss.poruszaj()
            Lis.poruszaj()
            Zyrafa.poruszaj()
        elif pauza:
            image(startImg, 450, 300, 100, 100)
    
        image(Jelen.plik, Jelen.x, Jelen.y, Jelen.rozmiar, Jelen.rozmiar)  
        image(Dzik.plik, Dzik.x, Dzik.y, Dzik.rozmiar, Dzik.rozmiar)  
        image(Zajac.plik, Zajac.x, Zajac.y, Zajac.rozmiar, Zajac.rozmiar)
        image(Kotek.plik, Kotek.x, Kotek.y, Kotek.rozmiar, Kotek.rozmiar)
        image(Bazant.plik, Bazant.x, Bazant.y, Bazant.rozmiar, Bazant.rozmiar)
        image(Sarna.plik, Sarna.x, Sarna.y, Sarna.rozmiar, Sarna.rozmiar)
        image(Lis.plik, Lis.x, Lis.y, Lis.rozmiar, Lis.rozmiar)
        image(Zyrafa.plik, Zyrafa.x, Zyrafa.y, Zyrafa.rozmiar, Zyrafa.rozmiar)
        image(Boss.plik, Boss.x, Boss.y, Boss.rozmiar, Boss.rozmiar)
        image(restartImg, 10, 70, 50, 50)
        image(celownikImg, mouseX-25, mouseY-25, 50, 50) 
        image(wyjscieImg, 930, 630, 50, 50)
        
        fill(255)
        textSize(23)
        textAlign(RIGHT, TOP)
        text("Score: " + str(score), width - 20, 20)
        
def mousePressed():
    global start_game
    if not start_game:
        start_game = True

def mouseClicked():
    global pauza, score, trafieniabossa
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
    if mouseX > Bazant.x and mouseX < Bazant.x + Bazant.rozmiar and mouseY > Bazant.y and mouseY < Bazant.y + Bazant.rozmiar and pauza == False:
        Bazant.x = -200
        Bazant.y = -200
        score += 15
    if mouseX > Kotek.x and mouseX < Kotek.x + Kotek.rozmiar and mouseY > Kotek.y and mouseY < Kotek.y + Kotek.rozmiar and pauza == False:
        Kotek.x = -200
        Kotek.y = -200
        score -= 10 #tu było 0, a wyżej jest, że powinno odejmować 10 punktów, więc zmieniłam
    if mouseX > Sarna.x and mouseY < Sarna.y + Sarna.rozmiar and mouseY > Sarna.y and mouseY < Sarna.y + Sarna.rozmiar and pauza == False:
        Sarna.x = -200
        Sarna.y = -200
        score += 20
    if mouseX > Boss.x and mouseX < Boss.x + Boss.rozmiar and mouseY > Boss.y and mouseY < Boss.y + Boss.rozmiar and pauza == False:
        score += 100
        trafieniabossa += 1
        if trafieniabossa == 3:
            Boss.x = -200
            Boss.y = -200
    if mouseX > 10 and mouseX < 60 and mouseY > 70 and mouseY < 120:
        reset()
    if mouseX > Lis.x and mouseX < Lis.x + Lis.rozmiar and mouseY > Lis.y and mouseY < Lis.y + Lis.rozmiar and pauza == False:
        Lis.x = -200
        Lis.y = -200
        score += 150
    if mouseX > Zyrafa.x and mouseX < Zyrafa.x + Zyrafa.rozmiar and mouseY > Zyrafa.y and mouseY < Zyrafa.y + Zyrafa.rozmiar and pauza == False:
        Zyrafa.x = -200
        Zyrafa.y = -200
        score += 50
    if mouseX > 930 and mouseX < 1000 and mouseY > 630 and mouseY < 700:
        exit()

def reset():
    global score, trafieniabossa
    score = 0
    trafieniabossa = 0
    Jelen.x = 100
    Jelen.y = 50
    
    Dzik.x = 200
    Dzik.y = 150
    
    Zajac.x = 300
    Zajac.y = 100
  
    Kotek.x = 400
    Kotek.y = 200

    Bazant.x = 500
    Bazant.y = 300

    Sarna.x = 100
    Sarna.y = 50

    Lis.x = 150
    Lis.y = 100

    Zyrafa.x = 250
    Zyrafa.y = 400

    Boss.x = 100
    Boss.y = 300
    
def keyPressed():
    if "L" or "l":
        exit()
