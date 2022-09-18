def productFib(prod):
    a = 0
    b = 1
    while a * b < prod:
        c = b
        b = a+c
        a = c
    return [a, b, a*b==prod]