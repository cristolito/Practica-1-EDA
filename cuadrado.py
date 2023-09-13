from figura import Figura
import flet as ft
class Cuadrado(Figura):
    def __init__(self):
        super().__init__()

    def calcular_area(self, lado):
        lado = float(lado)
        return lado*lado
    
    def calcular_perimetro(self, lado):
        lado = float(lado)
        return 4*lado