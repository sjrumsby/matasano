f = open('dict.txt', 'r')
word_list = [x.strip() for x in f.readlines()]
f.close()

def xor(val1, val2):
        params = {
                        "0" : "0000",
                        "1" : "0001",
                        "2" : "0010",
                        "3" : "0011",
                        "4" : "0100",
                        "5" : "0101",
                        "6" : "0110",
                        "7" : "0111",
                        "8" : "1000",
                        "9" : "1001",
                        "A" : "1010",
                        "B" : "1011",
                        "C" : "1100",
                        "D" : "1101",
                        "E" : "1110",
			"F" : "1111",
                        "a" : "1010",
                        "b" : "1011",
                        "c" : "1100",
                        "d" : "1101",
                        "e" : "1110",
                        "f" : "1111",
                }
        rev_params = dict((v,k) for k,v in params.iteritems())

        val1 = params[val1]
        val2 = params[val2]

        rval = ""

        for i in range(0,4):
                if val1[i] == val2[i]:
                        rval += "0"
                else:
                        rval += "1"
        rval = rev_params[rval.zfill(4)]
        return rval

def try_char(cipher, char):
	result = ""
	words = []
	real_words = 0

	for i in range(0,len(cipher), 2):
		result += xor(cipher[i], char[0]) + xor(char[1], cipher[i+1])
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

def acheivement_unlocked(cipher, char):
	result = ""
	for i in range(0,len(cipher), 2):
		result += xor(cipher[i], char[0]) + xor(char[1], cipher[i+1])
	print cipher.encode('ascii'), result

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hex_vals = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
success = 0

for i in hex_vals:
	for j in hex_vals:
		if try_char(cipher, i+j):
			success += 1
			
if success == 1:
	print "Pass! : )"
else:
	print "Fail. : ("
