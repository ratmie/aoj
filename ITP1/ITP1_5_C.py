while True:
	H, W = map(int, input().split())
	if H == 0 and W == 0:  
		break
	for h in range(H):
		str = ''
		for w in range(W):
			if (h % 2) == 0:
				if (w % 2) == 0:
					str += '#'
				else:
					str += '.'
			else:
				if (w % 2) == 0:
					str += '.'
				else:
					str += '#'				
		print(str)
	print()