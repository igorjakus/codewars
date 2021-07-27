"""
You have to code a function getAllPrimeFactors wich take an integer as parameter and return an array containing its
prime decomposition by ascending factors, if a factors appears multiple time in the decomposition it should appear as
many time in the array.

exemple: getAllPrimeFactors(100) returns [2,2,5,5] in this order.

This decomposition may not be the most practical.

You should also write getUniquePrimeFactorsWithCount, a function which will return an array containing two arrays: 
one with prime numbers appearing in the decomposition and the other containing their respective power.

exemple: getUniquePrimeFactorsWithCount(100) returns [[2,5],[2,2]]

You should also write getUniquePrimeFactorsWithProducts an array containing the prime factors to their respective
powers.

exemple: getUniquePrimeFactorsWithProducts(100) returns [4,25]

Errors, if:

n is not a number
n not an integer
n is negative or 0
The three functions should respectively return [], [[],[]] and [].

Edge cases:

if n=0, the function should respectively return [], [[],[]] and [].
if n=1, the function should respectively return [1], [[1],[1]], [1].
if n=2, the function should respectively return [2], [[2],[1]], [2].
The result for n=2 is normal. The result for n=1 is arbitrary and has been chosen to return a usefull result.
The result for n=0 is also arbitrary but can not be chosen to be both usefull and intuitive. ([[0],[0]] would be meaningfull but
wont work for general use of decomposition, [[0],[1]] would work but is not intuitive.)"""


from math import sqrt
from collections import Counter


def getAllPrimeFactors(n):
    # error cases
    if not isinstance(n, int) or n <= 0:
        return []
    # edge cases
    elif n == 1:
        return [1]
    
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)

    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            n //= i
            factors.append(i)
    
    # there can be AT-MOST 1 prime factor of n greater than sqrt(n).
    # like 7 is a prime-factor for 14 which is greater than sqrt(14)
    # so we need to apply this:
    if n > 2:
        factors.append(n)
    return factors

def getUniquePrimeFactorsWithCount(n):
    counter = Counter(getAllPrimeFactors(n))
    return [list(counter.keys()), list(counter.values())]

def getUniquePrimeFactorsWithProducts(n):
    factors, count = getUniquePrimeFactorsWithCount(n)
    return [x**y for x, y in zip(factors, count)]