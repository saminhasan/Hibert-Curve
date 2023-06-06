import math
from typing import Any, List

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def mult(self, r):
        self.x *= r
        self.y *= r
    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"
    

def hilbert( i : int, order : int)->List[Vector]:
        points = [
        Vector(0, 0),
        Vector(0, 1),
        Vector(1, 1),
        Vector(1, 0)
        ]

        index = i & 3
        v = points[index]

        for j in range(1, order):
            i = i >> 2
            index = i & 3
            length = pow(2, j)
            if index == 0:
                temp = v.x
                v.x = v.y
                v.y = temp
            elif index == 1:
                v.y += length
            elif index == 2:
                v.x += length
                v.y += length
            elif index == 3:
                temp = length - 1 - v.x
                v.x = length - 1 - v.y
                v.y = temp
                v.x += length
        return v

def hilbert_curve(width : int =1920, height : int =1080, order : int =2) -> List[Vector]:
        path = []
        N = 2**order
        total = N * N
        for  i in range(total): 
            path.append(hilbert(i, order))
            length = math.floor(width / N)
            path[i].mult(length)
            path[i].add(length / 2, length / 2)
        return path

    

if __name__ == '__main__':
    curve = hilbert_curve()
    [print(c) for c in curve]
