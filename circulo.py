from figura import Figura
import flet as ft
class Circulo(Figura):
    def __init__(self):
        super().__init__()

    def calcular_area(self, radio):
        radio = float(radio)
        return 3.14*radio*radio
    
    def calcular_perimetro(self, radio):
        radio = float(radio)
        return 2*3.14*radio