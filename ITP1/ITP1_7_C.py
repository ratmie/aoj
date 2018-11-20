def main():
	row, column = (int(a) for a in input().split())
	sheet = []
	for i in range(row):
		c = []
		for m in input().split():
			c.append(int(m))
		sheet.insert(i, c)
	for i in range(row):
		sheet[i].append(sum(sheet[i]))
		string = map(str, sheet[i])
		printColumn(sheet[i])
	l = []
	for m in range(column + 1):
		s = 0
		for r in range(row):
			s += sheet[r][m]
		l.append(s)
	printColumn(l)

def printColumn(list):
	string = map(str, list)
	print(' '.join(string))

main()
