from math import sqrt

points = [
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
]

def brute_force(points):
    min_val = 9999
    min_points = (), ()
    for i, point in enumerate(points[:-1]):
        dist = distance(point, points[i+1])
        if dist < min_val:
            min_val = dist
            min_points = point, points[i+1]

    return min_points



def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def sort_by_x(points):
    return sorted(points, key=lambda x: x[0])

def divide_two_halves(arr):
    half = len(arr)//2
    return arr[:half], arr[half:]

def recursive_smallest_distance(points):
    if len(points) <= 3:
        return brute_force(points)

"""
Following is a recap of the algorithm discussed in the previous post.

1) We sort all points according to x coordinates.

2) Divide all points in two halves.

3) Recursively find the smallest distances in both subarrays.



4) Take the minimum of two smallest distances. Let the minimum be d.

5) Create an array strip[] that stores all points which are at most d distance away from the middle line dividing the two sets.

6) Find the smallest distance in strip[].

7) Return the minimum of d and the smallest distance calculated in above step 6.
"""
from performance import measure
from math import hypot, sqrt

def one(a, b):
    return hypot(a, b)

def two(a, b):
    return sqrt(a**2 + b**2)

@measure
def test1():
    for i in range(1000):
        one(i, i+1)

@measure
def test2():
    for i in range(1000):
        two(i, i+1)
        
test1()
test2()