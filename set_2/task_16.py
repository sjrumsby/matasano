from AESCipher import AESCipher

def f1(s, aes):
	return a.cbc_encrypt("comment1=cooking%20MCs;userdata=" + s + ";comment2=%20like%20a%20pound%20of%20bacon")

a = AESCipher()
prefix_size = 32
block_size = 16

flp1 = "IAAAAAIAAAAAAAAA"		#This is our goal first 16 blocks
str1 = "AAAAAAAAAAAAAAAA3admin5true"	#This is what we'll pass as the userdata to f1
enc1 = f1(str1, a)

#This string has 2 bits flipped in the specfic positions required to turn the 3 into ; and 5 into =

xor  = "\x00" * 32 + "\x08\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00" + "\x00" * (len(enc1) - 48)

#xor them together
enc2 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(enc1, xor))

#Great success!
print a.cbc_decrypt(enc2)
