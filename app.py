from triangulo import Triangulo
from rectangulo import Rectangulo
from circulo import Circulo
from cuadrado import Cuadrado
import flet as ft
from flet import TextField, Column, Row, Text

def main(page):
    def btn_click_cir(e):
        page.add(Text( f"Área: {Circulo().calcular_area(radio.value)} u al cuadrado\n"
            f"Perimetro: {Circulo().calcular_perimetro(radio.value)} u(s)"
        ))
        
    def btn_click_rec(e):
        page.add(Text( f"Área: {Rectangulo().calcular_area(base.value,altura.value)} u al cuadrado\n"
            f"Perimetro: {Rectangulo().calcular_perimetro(base.value,altura.value)} u(s)"
        ))
        

    def btn_click_tri(e):
        page.add(Text( f"Área: {Triangulo().calcular_area(lado1.value,lado2.value,lado3.value)} u al cuadrado\n"
            f"Perimetro: {Triangulo().calcular_perimetro(lado1.value,lado2.value,lado3.value)} u(s)"
        ))
    
    def btn_click_cua(e):
        page.add(Text( f"Área: {Cuadrado().calcular_area(lado.value)} u al cuadrado\n"
            f"Perimetro: {Cuadrado().calcular_perimetro(lado.value)} u(s)"
        ))
        

    radio = TextField(label="Radio", width=300)
    altura = TextField(label="Altura", width=300)
    base = TextField(label="Base", width=300)
    lado1 = TextField(label="Lado 1", width=300)
    lado2 = TextField(label="Lado 2", width=300)
    lado3 = TextField(label="Lado 3", width=300)
    lado = TextField(label="Lado", width=300)
    
    circulo = Column([
        Text("Circulo"),
        radio,
        ft.ElevatedButton("Calcular", on_click=btn_click_cir)
    ], height=300)
    rectangulo = Column([
        Text("Rectangulo"),
        altura,
        base,
        ft.ElevatedButton("Calcular", on_click=btn_click_rec)
    ], height=300)
    triangulo = Column([
        Text("Triangulo"),
        lado1,
        lado2,
        lado3,
        ft.ElevatedButton("Calcular", on_click=btn_click_tri)
    ], height=300)
    cuadrado = Column([
        Text("Cuadrado"),
        lado,
        ft.ElevatedButton("Calcular", on_click=btn_click_cua)
    ], height=300)

    page.add(
        Text("Figuras"),
        Row([circulo, rectangulo, triangulo, cuadrado])
    )

ft.app(target=main)