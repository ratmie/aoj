import math
def main():
    a, b, c = (float(a) for a in input().split())
    s = a * b * math.sin(math.radians(c)) * 0.5
    l = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(c)))
    h = b * math.sin(math.radians(c))
    print(s)
    print(l)
    print(h)


main()
