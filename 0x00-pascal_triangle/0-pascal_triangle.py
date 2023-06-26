#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            num = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(num)
        row.append(1)
        triangle.append(row)

    return triangle

