def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

s = list(get_input())

d = {char:0 for char in [chr(ord('a')+i) for i in range(26)]}
for line in s:
    for x in line.lower():
        if(x in d):
            d[x] += 1

for k in d:
    print(k + " : " + str(d[k]))
