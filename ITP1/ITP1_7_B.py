def main():
	while True:
		n, x = (int(a) for a in input().split())
		answer = 0
		if n == 0 and x == 0:
			break
		for a in range(1, n + 1):
			for b in range(a + 1, n + 1):
				c = x - a - b
				if b >= c:
					break
				if  0 < c <= n and a != c and b != c:
					answer += 1
			if a >= c:
				break
		print(answer)

main()
