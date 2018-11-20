def main():
	n, m = (int(a) for a in input().split())
	a = []
	b = []
	for i in range(n):
		for j in input().split():
			a.append(int(j))
	for i in range(m):
		b.append(int(input()))

	for i in range(n):
		c = 0
		for j in range(m):
			c += a[i*m + j] * b[j]
		print(c)

main()
