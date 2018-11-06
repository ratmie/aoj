a, b, c = (int(x) for x in input().split())
ct = 0
for x in range(a, b + 1):
	if (c % x) == 0:
		ct = ct + 1
print(ct)
