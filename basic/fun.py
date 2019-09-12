def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


b = fact(600)
print(b)
