from math import factorial


def expand(expr):
    # (-5x-3)^2 -> a=-5, x='x', b=-3, n=2
    a, x, b, n = unpack(expr)
    
    # x^0 = 1
    if n == 0:
        return '1'

    # x^1 = x
    elif n == 1:
        z = '+' if b > 0 else ''
        if a == 1:
            ax = f'{x}'
        elif a == -1:
            ax = f'-{x}'
        else:
            ax = f'{a}{x}'
        return f'{ax}{z}{b}'
    
    binomial_expansion = ''
    for k in range(0, n+1):
        newton_bionimial = newton_theorem(a, x, b, n, k)
        binomial_expansion += '' if newton_bionimial[0] == '-' else '+'
        binomial_expansion += newton_bionimial
        
    return binomial_expansion.lstrip('+')
    
def newton_theorem(a, x, y, n, k):
    if n == k:
        return f'{y**n}'
    
    xy = int(newton(n, k) * a**(n-k) * y**k)
    
    if xy == 1:
        axy = f'{x}'
    elif xy == -1:
        axy = f'-{x}'
    else:
        axy = f'{xy}{x}'
    
    r = f'^{n-k}' if n-k != 1 else ''

    return f'{axy}{r}'

def unpack(s):
    s = s.replace('(', '').replace(')', '')

    expr, n = s.split('^')
    if '+' in expr:
        ax, b = expr.split('+')
        a = ax[:-1] if len(ax) > 1 else 1
        x = ax[-1]
        
    if '-' in expr[1:]:
        ax, b = expr.rsplit('-', 1)
        a = ax[:-1] if len(ax) > 1 else 1
        x = ax[-1]
        b = -int(b)

    # exeption handling: (-x+2)^2 gives a = '-'
    if a == '-': 
        a = -1
    
    return int(a), x, int(b), int(n)

def newton(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))