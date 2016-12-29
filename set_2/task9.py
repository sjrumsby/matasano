from AESCipher import AESCipher

a = AESCipher('YELLOW SUBMARINE', 20)

print "%s: %s" % (len(a.pkcs7pad('YELLOW SUBMARINE')), a.pkcs7pad('YELLOW SUBMARINE'))

