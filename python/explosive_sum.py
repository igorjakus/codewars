"""
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42
Explosive
exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292
See here for more examples."""


from functools import lru_cache
from performance import measure

def gpn(x):
    if x % 2 == 1:
        x = (x+1)//2 
        return x*(3*x-1)//2
    else:
        x = x//2
        return x*(3*x+1)//2


# TODO: Memoization
@lru_cache(maxsize=None)
def exp_sum(n):
    if n == 0 or n == 1:
        return 1

    sum = 0
    i = 0
    k = gpn(1)
    while n-k >= 0:
        if i % 4 in {0, 1}:
            sum += exp_sum(n-k)
        else:
            sum -= exp_sum(n-k)
        i += 1
        k = gpn(i+1)

    print(n, sum)
    return sum
