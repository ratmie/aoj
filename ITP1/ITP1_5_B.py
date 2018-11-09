while True:
	H, W = map(int, input().split())
	if H == 0 and W == 0:  
		break
	for h in range(H):
		str = ''
		for w in range(W):
			if h != 0 and h != (H - 1) and w != 0 and w != (W - 1):
				str += '.'
			else:
				str += '#'
		print(str)
	print()