import Pila

class TestPila:
    def __init__(self):
        self.pilaNumeros = Pila.Pila()
        self.pilaCaracteres = Pila.Pila()
        self.pilaElementos = Pila.Pila()

if __name__ == "__main__":
    test = TestPila()
    test.pilaNumeros.push(1)
    test.pilaNumeros.push(2)
    test.pilaNumeros.push(3)
    print(test.pilaNumeros)
    print("Tamaño de la pila:", test.pilaNumeros.size())
    print("Elemento en la cima de la pila:", test.pilaNumeros.peek())
    print("Desapilando elemento:", test.pilaNumeros.pop())
    print(test.pilaNumeros)
    print("Tamaño de la pila:", test.pilaNumeros.size())
    print("La pila de números está vacía:", test.pilaNumeros.isEmpty())
    print("\n")
    test.pilaCaracteres.push('a')
    test.pilaCaracteres.push('b')
    test.pilaCaracteres.push('c')
    print(test.pilaCaracteres)
    print("Tamaño de la pila:", test.pilaCaracteres.size())
    print("Elemento en la cima de la pila:", test.pilaCaracteres.peek())
    print("Desapilando elemento:", test.pilaCaracteres.pop())
    print(test.pilaCaracteres)
    print("Tamaño de la pila:", test.pilaCaracteres.size())
    print("Elemento en la cima de la pila:", test.pilaCaracteres.peek())
    print("La pila de caracteres está vacía:", test.pilaCaracteres.isEmpty())
    print("\n")
    test.pilaElementos.push('a')
    test.pilaElementos.push(1)
    test.pilaElementos.push(3.14)
    test.pilaElementos.push('b')
    test.pilaElementos.push("Hola")
    test.pilaElementos.push('A')
    print(test.pilaElementos)
    print("Tamaño de la pila:", test.pilaElementos.size())
    print("Elemento en la cima de la pila:", test.pilaElementos.peek())
    print("Desapilando elemento:", test.pilaElementos.pop())
    print(test.pilaElementos)
    print("Tamaño de la pila:", test.pilaElementos.size())
    print("Elemento en la cima de la pila:", test.pilaElementos.peek())
    print("Desapilando elemento:", test.pilaElementos.pop())
    print(test.pilaElementos)
    print("Tamaño de la pila:", test.pilaElementos.size())
    print("Elemento en la cima de la pila:", test.pilaElementos.peek())
    print("La pila de elementos está vacía:", test.pilaElementos.isEmpty())
    