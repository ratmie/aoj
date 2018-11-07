n = int(input())
a = input().split()
ammount = 0
mini = int(a[0])
maxi = int(a[0])
for i in range(n):
	ammount += int(a[i])
	if mini > int(a[i]):
		mini = int(a[i])
	if maxi < int(a[i]):
		maxi = int(a[i])
print(mini, maxi, ammount)
