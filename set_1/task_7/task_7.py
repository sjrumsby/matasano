import base64
from Crypto.Cipher import AES

key = 'YELLOW SUBMARINE'

f = open('7.txt')
cipher_text = base64.b64decode(f.read()) 
f.close()

cipher = AES.new(key, AES.MODE_ECB)
plain_text = cipher.decrypt(cipher_text)

print plain_text
