class Cel:
  def __init__(self, nazwa, punkty, predkosc):
    self.nazwa = nazwa
    self.punkty = punkty
    self.predkosc = predkosc
    
Jelen = Cel("Jelen", 15, 15)
Dzik = Cel("Dzik", 15, 10)
Zajac = Cel("Zajac", 10, 20)

def setup():
  size(1000,700)
