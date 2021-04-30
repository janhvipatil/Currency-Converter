from math import exp

num = int(input())

print(round(exp(num) / (1 + exp(num)), 2))
