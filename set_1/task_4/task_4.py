def xor(val1, val2):
	print val1, val2, str(hex(int(val1, 16) ^ int(val2, 16)))[2:]
        return str(hex(int(val1, 16) ^ int(val2, 16)))[2:]

def try_char(cipher, char):
	result = ""
	words = []
	real_words = 0

	for x in cipher:
		result += xor(char, "0x"+x)
	try:
		result = result.decode('hex').encode('ascii')
		words = result.split(" ")

		if len(words) > 1:
			for x in words:
				if x.lower() in word_list:
					real_words += 1
		if real_words > 1:
			print char + " (" + char.decode('hex').encode('ascii')  + "): " + result
			return 1
			
	except UnicodeDecodeError:
		return 0
	#print "Trying char %s" % char.decode('hex').encode('ascii')

f = open('dict.txt', 'r')
word_list = [x.strip() for x in f.readlines()]
f.close()

f = open('strings.txt', 'r')
words = [x.strip() for x in f.readlines()]
f.close

count = 1
success = 0

for w in words:
	for i in range(0,255):
		if 
			success += 1
	count += 1

if success == 1:
	print "Pass! : )"
else:
	print "Fail. : ("

