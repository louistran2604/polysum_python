import math

def polysum(n, s):
    """
    Calculates the sum of the area and the square of the perimeter 
    of a regular polygon.
    
    n: number of sides (integer)
    s: length of each side (float or integer)
    """
    area = (0.25*n*s**2) / (math.tan(math.pi/n))
    perimeter = n * s
    squared_perimeter = perimeter ** 2
    total = area + squared_perimeter
    return round(total, 4)

print(polysum(4, 5))