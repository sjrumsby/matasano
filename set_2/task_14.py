from base64 import b64decode
from AESCipher import AESCipher
from random import randint

def generate_key():
        key = ""
        for i in range(16):
                key += chr(randint(32,255))
        return key

def determine_block_size(aes):
	msg = "A"
	size = len(aes.ecb_encrypt(msg))
	for i in range(100):
		msg += "A"
		new_size = len(aes.ecb_encrypt(msg))

		if new_size > size:
			break
	return size

def find_duplicate_blocks(data):
        count = 0
        for i in range(len(data)):
                for j in range(i+1, len(data)):
                        if data[i] == data[j]:
				return i
        return -1

def determine_prefix_size(aes, blocksize, prefix, data):
	count = 0
	for i in range(2*blocksize, 3*blocksize):
		blocks_data = []
		msg = aes.ecb_encrypt(prefix +( "A" * i) + data)
		for j in range(0, len(msg), blocksize):
			blocks_data.append(msg[j:j+blocksize])

		ret = find_duplicate_blocks(blocks_data)
		if ret > 0:
			return blocksize*(ret - 1) + blocksize - count
		else:
			count += 1
	print "No duplicate blocks found"
	return 0

data = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

rand_count = randint(0,100)
rand_string = ""

for i in range (0,rand_count):
	rand_string += chr(randint(0,255))

print "The length of the prefix is: %s. Modulo blocksize: %s" % (rand_count, rand_count%16)
print "Data length: %s. Total length: %s" % (len(data), len(rand_string + data))

key = generate_key()

a = AESCipher(key)
bs = determine_block_size(a)
known_data = ""
char_dict = {}

prefix_size = determine_prefix_size(a, bs, rand_string, data)
print "Calculated prefix size: %s. Modulo blocksize: %s" % (prefix_size, prefix_size%bs)

for i in range(1, len(data) + 1):
	char_dict = {}
	short_str = "A" * (2*bs + (bs - prefix_size%bs) - i) + known_data

	for j in range(256):
		str = rand_string + short_str + known_data + chr(j)
		char_dict[str] = a.ecb_encrypt(str)

	enc = rand_string + short_str + data[:i]
	msg = a.ecb_encrypt(enc)
	for k,v in char_dict.iteritems():
		if v == msg:
			known_data += k[-1]

print known_data
