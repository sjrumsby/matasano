from AESCipher import AESCipher

a = AESCipher('YELLOW SUBMARINE')

print "%s: %s" % (len(a._pad('YELLOW SUBMARINE', 20)), a._pad('YELLOW SUBMARINE', 20))

