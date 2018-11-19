import math
def main():
    x1, y1, x2, y2 = (float(a) for a in input().split())
    print(math.sqrt((max(x1, x2) - min(x1,x2))**2 + ((max(y1,y2)-min(y1,y2))**2)))

main()
