import time

lst = []

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    limit = max

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if aux >= limit:
                break
            yield aux

if __name__ == '__main__':
    fibonacci = fibo_gen(999)
    for element in fibonacci:
        print(element)
        lst.append(element)
        time.sleep(.05)
    print(lst)