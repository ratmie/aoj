while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:  
        break;
    for h in range(H):
        str = ''
        for w in range(W):
            str += '#'
        print(str)
    print()