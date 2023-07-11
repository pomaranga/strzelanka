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

class Boss(Cel):
    def ruch(self):
        self.kierunek_x = random.choice([-1, 1])  
        self.kierunek_y = random.choice([-1, 1])
        self.x += self.kierunek_x * self.predkosc 
        self.y += self.kierunek_y * self.predkosc
        
        if self.x < 0 or self.x > width-self.rozmiar:
            self.kierunek_x *= -1  
        if self.y < 0 or self.y > height-self.rozmiar:
            self.kierunek_y *= -1
    def walcz(self):
        self.x = 200
        self.y = 300
                      
Jelen = Cel("Jelen", 15, 7, "data/jelen.png", 100)
Dzik = Cel("Dzik", 15, 5, "data/dzik.png", 100)
Zajac = Cel("Zajac", 10, 10, "data/zajac.png", 100)
Kotek = Cel("Kotek", -10, 8, "data/kotek.png", 100)
Bazant = Cel("Bazant", 15,5, "data/bazant.png", 100)
Sarna = Cel("Sarna", 15, 10, "data/sarna.png", 100)
Lis = Cel("Lis", 150, 20, "data/lis.png", 100)
Zyrafa = Cel("Zyrafa", 5, 10, "data/zyrafa.png", 100)
Zaba = Cel("Zaba", 15, 5, "data/zaba.png", 100)
Szop = Cel("Szop", 10, 5, "data/szop.png", 100)
BossFaza1 = Boss("BossFaza1", 100, 2, "data/boss.png", 200)
BossFaza2 = Boss("BossFaza2", 150, 15, "data/bossfaza2.png", 350)
BossFaza3 = Boss("BossFaza3", 200, 20, "data/bossfaza3.png", 400)

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

Zaba.x = 200
Zaba.y = 150

Szop.x = 150
Szop.y = 200

BossFaza1.x = -200 #chowa bossa poza ekranem na początku gry
BossFaza1.y = -200

BossFaza2.x = -200
BossFaza2.y = -200

BossFaza3.x = -200
BossFaza3.y = -200

start_game = False
score = 0
pauza = False
def setup():
    size(1000, 700)
    global celownikImg, pauzaImg, startImg, tloImg, restartImg, tlostartImg, wyjscieImg
    Jelen.zaladuj_plik(Jelen.sciezka_plik)
    Zaba.zaladuj_plik(Zaba.sciezka_plik)
    Dzik.zaladuj_plik(Dzik.sciezka_plik)
    Szop.zaladuj_plik(Szop.sciezka_plik)
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
    tlostartImg = loadImage("data/tstart.png")
    wyjscieImg = loadImage("data/exit.png")
    BossFaza1.zaladuj_plik(BossFaza1.sciezka_plik)
    BossFaza2.zaladuj_plik(BossFaza2.sciezka_plik)
    BossFaza3.zaladuj_plik(BossFaza3.sciezka_plik)

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
            Lis.poruszaj()
            Zyrafa.poruszaj()
            Zaba.poruszaj()
            Szop.poruszaj()
            BossFaza1.ruch()
            BossFaza2.ruch()
            BossFaza3.ruch()
            
        elif pauza:
            image(startImg, 450, 300, 100, 100)
    
        image(Jelen.plik, Jelen.x, Jelen.y, Jelen.rozmiar, Jelen.rozmiar)  
        image(Dzik.plik, Dzik.x, Dzik.y, Dzik.rozmiar, Dzik.rozmiar)
        image(Zaba.plik, Zaba.x, Zaba.y, Zaba.rozmiar, Zaba.rozmiar)  
        image(Zajac.plik, Zajac.x, Zajac.y, Zajac.rozmiar, Zajac.rozmiar)
        image(Kotek.plik, Kotek.x, Kotek.y, Kotek.rozmiar, Kotek.rozmiar)
        image(Bazant.plik, Bazant.x, Bazant.y, Bazant.rozmiar, Bazant.rozmiar)
        image(Sarna.plik, Sarna.x, Sarna.y, Sarna.rozmiar, Sarna.rozmiar)
        image(Lis.plik, Lis.x, Lis.y, Lis.rozmiar, Lis.rozmiar)
        image(Zyrafa.plik, Zyrafa.x, Zyrafa.y, Zyrafa.rozmiar, Zyrafa.rozmiar)
        image(Szop.plik, Szop.x, Szop.y, Szop.rozmiar, Szop.rozmiar)
        image(restartImg, 10, 70, 50, 50)
        image(celownikImg, mouseX-25, mouseY-25, 50, 50) 
        image(wyjscieImg, 930, 630, 50, 50)
        
        fill(255)
        textSize(23)
        textAlign(RIGHT, TOP)
        text("Score: " + str(score), width - 20, 20)
        
        if score >= 150:
            Jelen.x = -200
            Jelen.y = -200
            Dzik.x = -200
            Dzik.y = -200
            Zajac.x = -200
            Zajac.y = -200
            Bazant.x = -200
            Bazant.y = -200
            Sarna.x = -200
            Sarna.y = -200
            Lis.x = -200
            Lis.y = -200
            Zyrafa.x = -200
            Zyrafa.y = -200
            Zaba.x = -200
            Zaba.y = -200
            Szop.x = -200
            Szop.y = -200
            Kotek.x = -200
            Kotek.y = -200 #chowa wszystkie cele poza ekranem, jeśli nie zostały zestrzelone
            image(BossFaza1.plik, BossFaza1.x, BossFaza1.y, BossFaza1.rozmiar, BossFaza1.rozmiar)
            image(celownikImg, mouseX-25, mouseY-25, 50, 50)
            BossFaza1.walcz()
            
        if score > 300:
            BossFaza1.x = -200
            BossFaza1.y = -200
            image(BossFaza2.plik, BossFaza2.x, BossFaza2.y, BossFaza2.rozmiar, BossFaza2.rozmiar)
            image(celownikImg, mouseX-25, mouseY-25, 50, 50)
            BossFaza2.walcz()
            
        if score > 750:
            BossFaza2.rozmiar = 50
            BossFaza2.x = -200
            BossFaza2.y = -200
            image(BossFaza3.plik, BossFaza3.x, BossFaza3.y, BossFaza3.rozmiar, BossFaza3.rozmiar)
            image(celownikImg, mouseX-25, mouseY-25, 50, 50)
            BossFaza3.walcz()
            
        if score > 1350:
            BossFaza3.rozmiar = 50
            BossFaza3.x = -200
            BossFaza3.y = -200
            background(10, 150, 100)
            fill(255)
            textSize(40)
            textAlign(CENTER, CENTER)
            text("YOU WON", width/2, height/2 - 50)
            text("Score: " + str(score), width/2, height/2)
            textSize(20)
            text("Press ESC to exit", width/2, height/2 + 50)  
        
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
    if mouseX > Zaba.x and mouseX < Zaba.x + Zaba.rozmiar and mouseY > Zaba.y and mouseY < Zaba.y + Zaba.rozmiar and pauza == False:
        Zaba.x = -200
        Zaba.y = -200
        score += 25
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
    if mouseX > Szop.x and mouseX < Szop.x + Szop.rozmiar and mouseY > Szop.y and mouseY < Szop.y + Szop.rozmiar and pauza == False:
        Szop.x = -200
        Szop.y = -200
        score += 35
    if mouseX > BossFaza1.x and mouseX < BossFaza1.x + BossFaza1.rozmiar and mouseY > BossFaza1.y and mouseY < BossFaza1.y + BossFaza1.rozmiar and pauza == False:
        score += BossFaza1.punkty
    if mouseX > BossFaza2.x and mouseX < BossFaza2.x + BossFaza2.rozmiar and mouseY > BossFaza2.y and mouseY < BossFaza2.y + BossFaza2.rozmiar and pauza == False:
        score += BossFaza2.punkty
    if mouseX > BossFaza3.x and mouseX < BossFaza3.x + BossFaza3.rozmiar and mouseY > BossFaza3.y and mouseY < BossFaza3.y + BossFaza3.rozmiar and pauza == False:
        score += BossFaza3.punkty
    if mouseX > 930 and mouseX < 1000 and mouseY > 630 and mouseY < 700:
        exit()

def reset():
    global score, trafieniabossa, gameOver
    score = 0
    gameOver = False
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
    
    Zaba.x = 50
    Zaba.y = 250

    Szop.x = 150
    Szop.y = 200

    Boss.x = 100
    Boss.y = 300

def keyPressed():
        if keyCode == ESC:
            exit()
