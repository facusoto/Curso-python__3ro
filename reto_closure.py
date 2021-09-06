def make_division_by(n):
    def number(number):
        assert type(number) == int, "Solo podes usar números enteros"
        return number / n
    return number

division = make_division_by(2)
print(division(20))