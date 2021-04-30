from math import radians
from math import tan

degrees = int(input())

radians = radians(degrees)

cotangent = 1 / tan(radians)

print('%.10f' % cotangent)
