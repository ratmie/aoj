def main():
	n = int(input())
	array = []
	string =''
	for x in input().split():
		array.append(x)
	array.reverse()
	for x  in array:
		string = string + x + ' '
	print(string[0:-1])

main()