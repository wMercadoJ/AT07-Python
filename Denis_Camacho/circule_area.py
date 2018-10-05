import math

ratio = int(input("into the ratio"))

circle_area = lambda r: math.pi * math.pow(r, 2) if r > 10 else ""

print circle_area(ratio)
