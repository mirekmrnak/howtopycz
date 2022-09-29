from math import atan, pi


class Point:
    def __init__(self, x=0, y=0):        # speciální metoda (instanční) 
        self.x = x
        self.y = y

    def __add__(self, other):            # speciální metoda (instanční)
        return self.x + other.x, self.y + other.y

    def __str__(self):            # speciální metoda (instanční)
        return f'{self.x}, {self.y}'

    def distance_from_origin(self):          # metoda instance
        return(self.x**2 + self.y**2)**0.5

    def sklon(self):          # metoda instance
        try:
            sklon_par = atan(self.y / self.x)
        except ZeroDivisionError:
            sklon_par = pi/2
        return sklon_par

class Rectangle:
    def __init__(self, corner, w, h): 
        self.corner = corner
        self.width = w
        self.height = h

    def grow_rectangle(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def move_rectangle(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def find_center(self):
        p = Point() 
        p.x = self.corner.x + self.width/2.0
        p.y = self.corner.y + self.height/2.0
        return p
    
    def area(self):
        self.area_par = self.width *self.height
        return self.area_par

    def perimeter(self):
        self.perimeter_par = 2*self.width + 2*self.height
        return self.perimeter_par
    
    def flip(self): 
        self.width, self.height = self.height, self.width
    
class Punktum:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    
    def __str__(self): 
        return (f"Souřadnice bodu: x = {self.x}, y = {self.y}. __str__ was CALLED!")

    def __repr__(self): 
        return (f"Souřadnice bodu: x = {self.x}, y = {self.y}. __repr__ was CALLED!")

r = Rectangle(Point(4,10), 50,100)
print(f'Obdelník má roh v bodě {r.corner}, šířka je {r.width} a výška {r.height}. S = {r.area()}, o = {r.perimeter()}')
print('Prohoďme výšku za šířku...')
r.flip()
print(f'Obdelník má roh v bodě {r.corner}, šířka je {r.width} a výška {r.height}. S = {r.area()}, o = {r.perimeter()}')
print(r.corner.sklon())
print()
print(Punktum(5, 9))