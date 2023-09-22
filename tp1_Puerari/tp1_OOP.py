# - Realizar un programa que, a su criterio, es más adecuado para ser resuelto con programación orientada a objetos.
# - El programa debe tener al menos 3 clases.


class Persona:
    def __init__(self, nombre, edad, numero):
        self.nombre = nombre
        self.edad = edad
        self.numero = numero

    def es_mayor_de_edad(self):
        return self.edad >= 18


class Mensaje:
    def __init__(self, numero):
        self.numero = numero

    def enviar_mensaje(self):
        print(f"Se enviará un mensaje al número {self.numero} para confirmar el registro.")


class Bienvenida:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_bienvenida(self):
        print(f"Hola {self.nombre}, ¡bienvenido/a!")

persona = Persona("Juan", 19, 387485981)

if persona.es_mayor_de_edad():
    bienvenida = Bienvenida(persona.nombre)
    bienvenida.mostrar_bienvenida()

    mensaje = Mensaje(persona.numero)
    mensaje.enviar_mensaje()
else:
    print("No cumples con la condición de mayoría de edad.")




