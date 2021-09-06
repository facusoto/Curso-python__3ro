def make_repeater(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes usar cadenas"
        return string * n
    return repeater

def run():
    inv = make_repeater(5)
    print(inv("Facundo"))


if __name__ == '__main__':
    run()

