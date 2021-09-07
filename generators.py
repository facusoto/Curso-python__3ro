def my_gen():
    print("Hello, 1")
    n = 0
    yield n

    print("Hello, 2")
    n = 1
    yield n

    print("Hello, 3")
    n = 2
    yield n

a = my_gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a))