import math

a = float(input())
b = float(input())
c = float(input())
if math.sqrt((math.pow(b, 2) - 4 * a * c) >= 0):
    x1 = (-1 * b + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    x2 = (-1 * b - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    print(x1, x2)
else:
    print('no answers')
