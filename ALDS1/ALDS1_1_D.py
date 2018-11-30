def main():
	n = int(input())
	r = [int(input()) for _ in range(n)]
	rmax = r[1] - r[0]
	rmin = r[0]
	for i in range(1, n):
		rmax = max(rmax, r[i] - rmin)
		rmin = min(r[i], rmin)
	print(rmax)

main()