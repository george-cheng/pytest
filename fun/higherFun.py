def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 5, abs))
