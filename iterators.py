import time

# Clase creadora
class FiboIter():
    # Ahora si utilizo el iniciador, el argumento es el maximo número
    def __init__(self, max_number=int):
        self.max_number = max_number

    # No hace falta __init__ por no necesitar argumentos
    def __iter__(self):
        # Primer numerador === 0
        self.n1 = 0
        # Segundo numerador === 1
        self.n2 = 1
        # Contador === 0
        self.counter = 0
        return self

    def __next__(self):
        # Si contador es 0 lo aumenta y devuelve n1
        if self.counter == 0:
            self.counter += 1
            return self.n1
        # Si contador es 1 lo aumenta y devuelve n2
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            # Si eso no sucede genera un [aux = n1 + n2]
            self.aux = self.n1 + self.n2
            # Luego n1 se vuelve n2 y n2 se vuelve aux
            # Por ende se mueve todo una línea (Todo comentado para cambiar a swap)
            """
            self.n1 = self.n2
            self.n2 = self.aux
            """
            # Con un swap cambiamos los valores de forma resumida
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            # Llama el argumento de init y lo compara al aux, si es >= sube la excepcion StopIteration
            if self.aux >= self.max_number:
                raise StopIteration
            return self.aux


if __name__ == '__main__':
    fibonacci = FiboIter(999)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)