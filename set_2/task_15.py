from AESCipher import AESCipher

msg1 = "ICE ICE BABY\x04\x04\x04\x04"
msg2 = "ICE ICE BABY\x05\x05\x05\x05"
msg3 = "ICE ICE BABY\x01\x02\x03\x04"

a = AESCipher()

try:
	a.pkcs7chk(msg1)
	print "Success"
except ValueError:
	print "Fail"

try:
	a.pkcs7chk(msg2)
	print "Fail"
except ValueError:
	print "Success"

try:
	a.pkcs7chk(msg3)
	print "Fail"
except ValueError:
	print "Success"

