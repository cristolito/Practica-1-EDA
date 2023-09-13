from figura import Figura
import math
class Triangulo(Figura):
    def __init__(self):
        super().__init__()

    def calcular_area(self, lado1, lado2, lado3):
        lado1 = float(lado1)
        lado2 = float(lado2)
        lado3 = float(lado3)
        s = self.calcular_perimetro(lado1, lado2, lado3)/2
        return math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    
    def calcular_perimetro(self, lado1, lado2, lado3):
        lado1 = float(lado1)
        lado2 = float(lado2)
        lado3 = float(lado3)
        return lado1+lado2+lado3