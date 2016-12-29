from base64 import b64decode
from binascii import hexlify
from AESCipher import AESCipher

a = AESCipher("YELLOW SUBMARINE", 16, "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
f = open('task10_data.txt', 'rb')
cipher_text = b64decode(f.read())
f.close()

print a.cbc_decrypt(cipher_text)

