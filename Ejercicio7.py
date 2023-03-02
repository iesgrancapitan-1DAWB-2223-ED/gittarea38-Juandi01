"""
Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos hacer las siguientes operaciones:

Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye simplificada, no se puede dividir por cero.
Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
"""

from fractions import Fraction
"Comentario"

class Fraccion:
    def __init__(self, numerador=1, denominador=1):
        self.__numerador = numerador
        self.__denominador = denominador

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def simplificar(self):
        return Fraction(self.numerador, self.denominador).limit_denominator()

    def __str__(self):
        return f"{self.simplificar().numerator}/{self.simplificar().denominator}"


f = Fraccion(125, 5)
print("La fracción simplificada es: ", str(f))

