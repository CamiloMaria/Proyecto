from main import AreaCuadrado, AreaHexagono, AreaTriangulo

def TestAreaCuadrado():
    assert AreaCuadrado(2) == 4
    print("El test paso correctamente\n")

def TestAreaHexagono():
    assert AreaHexagono(2, 2) == 2
    print("El test paso correctamente\n")
    
def TestAreaTriangulo():
    assert AreaTriangulo(3, 2) == 3
    print("El test paso correctamente\n")

if __name__ == '__main__':
        TestAreaCuadrado()
        TestAreaTriangulo()
        TestAreaHexagono()
