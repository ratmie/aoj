def main():
	n = int(input())
	for i in range(n):
		x = i + 1
		multipleOf3(i, x)
	print('')

def multipleOf3(i, n):
	if(n % 3) == 0:
		print(' %d' % (i + 1), end='')
	else:
		firstDigitis3(i, n)

def firstDigitis3(i, n):
	if(n % 10) == 3:
		print(' %d' % (i + 1), end='')
	else:
		n = n // 10
		if n > 0:
			firstDigitis3(i, n)

main()