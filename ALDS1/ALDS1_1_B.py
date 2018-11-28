def main():
    x, y = (int(i) for i in input().split())
    getGreatestCommonDiviser(x,y)


def getGreatestCommonDiviser(x, y):
    c = max(x,y) % min(x,y)
    if c == 0:
        print(min(x,y))
    else:
        getGreatestCommonDiviser(min(x,y),c)

main()