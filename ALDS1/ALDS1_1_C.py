import math

def main():
	n = int(input())
	cnt = 0
	for _ in range(n):
		a = int(input())
		if isPrime(a):
			cnt += 1
	print(cnt)


def isPrime(x):
	if x == 2:
		return True

	if x < 2 or (x%2) == 0:
		return False

	i = 3
	while i <= math.sqrt(x):
		if (x%i) == 0:
			return False
		i  += 2
	
	return True

main()