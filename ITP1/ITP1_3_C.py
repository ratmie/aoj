while True:
	a, b = (int(x) for x in input().split())
	if a == 0 and b ==0:
		break
	else:
		if a > b:
			a, b = b, a
	print(a, b)
