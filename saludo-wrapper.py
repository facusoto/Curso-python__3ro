def decorador(func):
    def wrapper():
        print("Esto se añade a mi función original")
        func()
    return wrapper

@decorador
def saludo():
    print("¡Hola!")

saludo()

#

def mayusculas(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))

#

def decorador_str(func):
    def wrapper():
        print("Hay algo que tenía que decir")
        func()
    return wrapper

@decorador_str
def mensaje():
    print('Hola')

mensaje()