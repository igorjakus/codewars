"""
In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1) and fib(n + 2)? 
Use this to reason what value fib has to have for negative values.

HINT II: See https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4"""


def fib(n):
    if n == 0 or n == 1:
        return n
    if n > 1:
        v1, v2, v3 = 1, 1, 0
        for rec in bin(n)[3:]:
            calc = v2*v2
            v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
            if rec == '1':
                v1, v2, v3 = v1+v2, v1, v2
        return v2
    else:
        return -fib(-n) if n % 2 == 0 else fib(-n)