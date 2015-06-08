f = open('8.txt')
strings = [x.strip() for x in f.readlines()]
f.close()

def find_dups(blocks):
	for i in range(0, len(blocks)):
		for j in range(i+1, len(blocks)):
			if blocks[i] == blocks[j]:
				return 1
	return 0

for s in strings:
	blocks = [s[i:i+32] for i in range(0,len(s),32)]

	if find_dups(blocks):
		print s
