from math import sqrt

edge_length = int(input())

area = 2 * sqrt(3) * edge_length * edge_length

volume = (1 / 3) * sqrt(2) * edge_length * edge_length * edge_length

print(round(area, 2), round(volume, 2))
