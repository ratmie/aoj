def main():
	n = int(input())
	r = [int(a) for a in input().split()]
	ct = selectionSort(r, n)
	printlist(r)
	print(ct)

def selectionSort(a , n):
	cnt = 0
	for i in range(n):
		minj = i
		for j in range(i,n):
			if a[j] < a[minj]:
				minj = j
		a[i], a[minj] = a[minj], a[i]
		cnt += 1
	return cnt


def printlist(a):
	values = map(str, a)
	print(' '.join(values))

main()