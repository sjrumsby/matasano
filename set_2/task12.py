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

data = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
key = generate_key()

a = AESCipher(key)
bs = determine_block_size(a)
print "Block size: %s" % bs
known_data = ""
char_dict = {}

for i in range(1, 176):
	short_str = "A" * (bs-i) + known_data	

	for j in range(256):
		str = short_str + known_data + chr(j)
		char_dict[str] = a.ecb_encrypt(str)

	enc = short_str + data[:i]
	msg = a.ecb_encrypt(enc)
	for k,v in char_dict.iteritems():
		if v == msg:
			known_data += k[-1]

print known_data
	
