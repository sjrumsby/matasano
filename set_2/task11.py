from AESCipher import AESCipher
from random import randint

def generate_key():
	key = ""
	for i in range(16):
		key += chr(randint(32,255))
	return key

def generate_jibber_jabber(msg):
	for i in range(randint(5,10)):
		msg = chr(randint(1,255)) + msg
	for i in range(randint(5,10)):
		msg = msg + chr(randint(5,10))
	return msg

def find_duplicate_blocks(data):
	count = 0
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			if data[i] == data[j]:
				count += 1
	return count

def encryption_oracle(enc):
	data = []
	for i in range(0, len(enc), 16):
		data.append(enc[i:i+16])

	dupe_count = find_duplicate_blocks(data)
	if dupe_count > 2:
		return 2
	elif dupe_count == 0:
		return 1
	else:
		return -1

success = 0
fail = 0
msg = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"

for i in range(200):
	enc_msg = generate_jibber_jabber(msg)
	mode = randint(1,2)
	if mode == 1:
		a = AESCipher(key=generate_key(), bs=16, iv=generate_key())
		enc = a.cbc_encrypt(enc_msg)
	elif mode == 2:
		a = AESCipher(key=generate_key(), bs=16, iv=generate_key())
		enc = a.ecb_encrypt(enc_msg)

	computed_mode = encryption_oracle(enc)

	if mode == computed_mode:
		success += 1
	else:
		fail += 1

print "Success rate: %.3f" % float(float(success)/float((success + fail)))
