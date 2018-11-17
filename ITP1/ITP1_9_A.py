def main():
	wordCount = {}
	W = input()
	while True:
		line = input()
		if line == 'END_OF_TEXT':
			break
		line = line.lower()
		for word in line.split():
			if word in wordCount:
				wordCount[word] += 1
			else:
				wordCount[word] = 1
	print(wordCount[W])
	
main()
