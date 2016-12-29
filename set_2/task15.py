from AESCipher import AESCipher

msg1 = "ICE ICE BABY\x04\x04\x04\x04"
msg2 = "ICE ICE BABY\x05\x05\x05\x05"
msg3 = "ICE ICE BABY\x01\x02\x03\x04"

a = AESCipher()

try:
	a.pkcs7chk(msg1)
	print "Success: No error was thrown"
except ValueError:
	print "Fail: An error was thrown"

try:
	a.pkcs7chk(msg2)
	print "Fail: No error was thrown"
except ValueError:
	print "Success: An error was thrown"

try:
	a.pkcs7chk(msg3)
	print "Fail: No error was thrown"
except ValueError:
	print "Success: An error was thrown"

