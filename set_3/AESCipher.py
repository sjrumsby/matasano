import base64
from Crypto.Cipher import AES
from random import randint

class AESCipher():
    def __init__(self, key=None, bs=16, iv=None):
        self.bs = bs

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
        
    def pad_to_length(self, msg, pad_length):
        if len(msg) > pad_length:
            raise ValueError("Pad length (%s) must be greater than the message length (%s)" % (pad_length, len(msg)))
            
        missing = len(msg) - pad_length
        return msg + chr(missing)*missing

    def pkcs7pad(self, msg):
        missing = abs(len(msg) - (len(msg)/self.bs+1) * self.bs)
        return msg + (chr(missing)*missing)

    def pkcs7chk(self, msg):
        padlen = ord(msg[-1])

        if padlen == 0 or padlen > 16:
            raise ValueError("Invalid PKCS#7 padding")

        sl = len(msg)

        for x in msg[sl-padlen:]:
            if ord(x) != padlen:
                raise ValueError("Invalid PKCS#7 padding")		    

        return msg[:sl-padlen]

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
        a = AES.new(self.key, AES.MODE_CBC, self.iv)
        msg = self.pkcs7pad(msg)
        cipher_text = ""

        for i in range(0, len(msg), self.bs):
            enc = msg[i:i+self.bs]
            block = a.encrypt(enc)
            cipher_text += block
            self.iv = block

        return cipher_text

    def cbc_decrypt(self, msg):
        a = AES.new(self.key, AES.MODE_CBC, self.iv)
        plain_text = ""

        for i in range(0, len(msg), self.bs):
            enc = a.decrypt(msg[i:i+self.bs])
            plain_text += enc
            self.iv = msg[i:i+self.bs]

        return plain_text
