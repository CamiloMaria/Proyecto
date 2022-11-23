from math import sqrt

def Welcome():
        print("Bienvenido al programa de calculo de areas.")

def AreaCuadrado(a):
        print("El area de Cuadrado = " + pow(a,2))
        return pow(a, 2)
        
def AreaRectangulo(a, b):
        print("El area de rectangulo = " + a*b)
        return a*b

def AreaTriangulo(a, b):
        print("El area de triangulo = " + (a*b)/2)
        return (a*b)/2

def AreaCirculo(a):
        print("El area de circulo = " + 3.1416 * pow(a, 2))
        return 3.1416 * pow(a, 2)

def AreaCono(a, b):
        print("El area de cono = " + (a * b) * 3.1416)
        return (a * b) * 3.1416

def AreaHipotenusa(a, b):
        print("El area de hipotenusa = " + (sqrt(pow(a, 2) + pow(b, 2))))
        return (sqrt(pow(a, 2) + pow(b, 2)))

def AreaTrapecio(a, b, c):
        print("El area de trapecio = " + (a + b) * c / 2)
        return (a + b) * c / 2

def AreaHexagono(a, b):
        print("El area de hexagono = " + (a*b)/2)
        return (a*b)/2

def AreaElipse(a, b):
        print("El area de elipse = " + (a * b) * 3.1416)
        return (a * b) * 3.1416

if __name__ == '__main__':
        Welcome()