a, b, c = (int(x) for x in input().split())
if a < b < c:
    answer = "Yes"
else:
    answer = "No"
print(answer)