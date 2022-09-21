"""
>>> python median.py 3 7 11
7
>>> python median.py 19 85 121
85
>>> python median.py 11 15 16 22
15.5
"""
from sys import argv
numbers = sorted(list(map(float, argv[1:])))
middle = len(numbers) / 2

if len(numbers) % 2 != 0:
    print(numbers[round(middle)-1])
else:
    print((numbers[int(middle)-1]+numbers[int(middle)])/2)