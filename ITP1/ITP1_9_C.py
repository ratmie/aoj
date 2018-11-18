def main():
	n = int(input())
	pointTaro = 0
	pointHanako = 0
	for i in range(n):
		l = input().split()
		if l[0] > l[1]:
			pointTaro += 3
		elif l[0] == l[1]:
			pointTaro += 1
			pointHanako += 1
		else:
			pointHanako += 3
	print(pointTaro, pointHanako)

main()
