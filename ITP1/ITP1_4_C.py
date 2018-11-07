while True:
	a, op, b = (x for x in input().split())
	a, b = int(a), int(b)
	if op == '+':
		print(a + b)
	elif op == '-':
		print(a - b)
	elif op == '*':
		print(a * b)
	elif op == '/':
		print(a // b)
	elif op == '?':
		break