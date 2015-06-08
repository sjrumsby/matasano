#XOR accepts two hex characters are performs xor on them
def bit_xor(val1, val2):
	return hex(int(val1.encode('hex'),16) ^ int(val2.encode('hex'),16))[2:].zfill(2)

def encrypt(text, cipher):
	mod = len(cipher)
	rval = ""
	count = 0
	for t in text:
		rval += str(bit_xor(t, cipher[count%mod]))
		count += 1
	return rval
		

clear_texts = 	[
		"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
		]

cipher = "ICE"

f = open('dict.txt', 'r')
words = [x.strip() for x in f.readlines()]
f.close()

#Timing to test xor function for speed. Initial results are 10.4 seconds on shitty EC2 Micro instance to encrypt all 80,000+ words in the dictionary
#for x in words:
#	encrypt(x.encode('hex'), cipher)

for c in clear_texts:
	print encrypt(c, cipher)

