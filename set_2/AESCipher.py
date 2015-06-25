import base64
from Crypto.Cipher import AES
from random import randint

class AESCipher():
	def __init__(self, key=None, bs=16, iv=None):
		self.bs = 16

		if key is None:
			self.key = self.generate_key(16)
		else:
			self.key = key
		if iv is None:
			self.iv = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
		else:
			self.iv = iv

	def generate_key(self, n):
		key = ""
		for i in range(n):
			key += chr(randint(32,255))
		return key

	def pkcs7pad(self, msg):
		missing = abs(len(msg) - (len(msg)/self.bs+1) * self.bs)
		return msg + (chr(missing)*missing)

	def pkcs7chk(self, msg):
		padlen = ord(msg[-1])
		sl = len(msg)-1
		for x in msg[sl-padlen+1:]:
			if ord(x) != padlen:
				raise ValueError("Invalid PKCS#7 padding")		    

		return msg[:sl-padlen+1]

	def ecb_encrypt(self, msg):
		a = AES.new(self.key, AES.MODE_ECB)
		msg = self.pkcs7pad(msg)
		cipher_text = ""

		for i in range(0, len(msg), self.bs):
			cipher_text += a.encrypt(msg[i:i+self.bs])
		return cipher_text

	def ecb_decrypt(self, msg):
		a = AES.new(self.key, AES.MODE_ECB)
		plain_text = ""

		for i in range(0, len(msg), self.bs):
			plain_text += a.decrypt(msg[i:i+self.bs])

		return self.pkcs7chk(plain_text)

	def cbc_encrypt(self, msg):
		a = AES.new(self.key, AES.MODE_ECB)
		msg = self.pkcs7pad(msg)
		cipher_text = ""

		for i in range(0, len(msg), self.bs):
			enc = ''.join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(self.iv, msg[i:i+self.bs])])
			block = a.encrypt(enc)
			cipher_text += block
			self.iv = block

		return cipher_text
	

	def cbc_decrypt(self, msg):
		a = AES.new(self.key, AES.MODE_ECB)
		plain_text = ""

		for i in range(0, len(msg), self.bs):
			enc = a.decrypt(msg[i:i+self.bs])
			plain_text += ''.join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(self.iv, enc)])
			self.iv = msg[i:i+self.bs]

		return plain_text
