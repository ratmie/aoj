while True:
    sumOfDigit = 0
    x = int(input())
    if x == 0:
        break
    while x != 0:
        sumOfDigit += x % 10
        x = x // 10
    print(sumOfDigit)
    