"""
>>> python mean.py 3 4
3.5
>>> python mean.py 3 4 5
4.0
>>> python mean.py 11 15 94.5 22
35.625
"""
from statistics import mean
from sys import argv
numbers = list(map(float, argv[1:]))
print(sum(numbers)/len(numbers))
print(mean(numbers))