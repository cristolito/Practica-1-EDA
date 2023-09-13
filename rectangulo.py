from figura import Figura
class Rectangulo(Figura):
    def __init__(self):
        super().__init__()

    def calcular_area(self, b, h):
        b = float(b)
        h = float(h)
        return b*h
    
    def calcular_perimetro(self, b ,h):
        b = float(b)
        h = float(h)
        return (b+h)*2