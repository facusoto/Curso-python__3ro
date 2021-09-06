def make_division_by(n):
    def number(number):
        assert type(number) == int, "Solo podes usar números enteros"
        assert n > 0, "El valor de la división debe ser mayor a cero"
        return number / n
    return number

division = make_division_by(int(input("Elegí entre cuanto dividir: ")))
print(division(int(input(f"Elegí un número para dividirlo: "))))