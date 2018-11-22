import math
def main():
	while True:
		n = int(input())
		if n == 0:
			break
		l = list(map(int, input().split()))
		m = sum(l)/n
		k = []
		for a in l:
			k.append((a- m)**2)
		a = math.sqrt(sum(k)/n)
		print(a)

main()
