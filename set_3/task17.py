from AESCipher import AESCipher
import random

DEBUG = 0

strings = [
    "MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
    "MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
    "MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
    "MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
    "MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
    "MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
    "MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
    "MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
    "MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
    "MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93",
]

def pad_and_encrypt(a, msg):
    return a.cbc_encrypt(msg)

def decrypt_and_check_pad(a, enc):
    msg = a.cbc_decrypt(enc)
    
    try:
        a.pkcs7chk(msg)
    except ValueError:
        return False

    return msg

aes = AESCipher()
aes.key="YELLOW SUBMARINE"

msg = strings[0]
cph = aes.cbc_encrypt(msg)

def print_msg(msg):
    if DEBUG:
        print msg

def decrypt_block(a, cph, block, pos, char):
    print_msg( "%s (%s): %s" % (pos, char, repr(block)))

    if len(block) < 16:
        block.append(chr(random.randint(0,2)))
        block = decrypt_block(a, cph, block, len(block), ord(block[pos-1]))

    print_msg( "Starting iterations on character: %s. Starting at char: %s" % (pos, char))
    block_guess = block
    for c in range(char, 256):
        cph_guess = list(cph)
        print_msg( "Trying char: %s" % c)
        block_guess[pos-1] = chr(c)
        print_msg( "block_guess to xor with cipher: %s" % repr(block_guess))
        b = len(cph)/16 - 2

        print_msg( "cph_guess before block changes: %s" % repr(cph_guess[b*16:b*16+16]))
        for p in range(16):
            cph_guess[b*16+p] = chr(ord(cph[b*16+p]) ^ ord(block_guess[p]))

        print_msg( "cph_guess after xor with block: %s" % repr(cph_guess[b*16:b*16+16]))

        for p in range(pos-1,16):
            print_msg( "Padding byte: %s with value: %s" % (b*16+p+1, 17-pos))
            cph_guess[b*16+p] = chr(ord(cph_guess[b*16+p]) ^ (17 - pos))

        print_msg( "cph_guess after xor with pad byte: %s" % repr(cph_guess[b*16:b*16+16]))

        if decrypt_and_check_pad(a, "".join(cph_guess)):
            print_msg( "Valid!!!")
            return block
        else:
            print_msg( "Not valid padding")

    return block

decrypted_msg = ""
for i in range(len(cph)/16):
    block = ["\x00"]
    decrypted_block = decrypt_block(aes, cph, block, 1, 0)
    print "\nDecrypted a block!\n"
    print repr(decrypted_block)
    decrypted_msg = "".join(decrypted_block) + decrypted_msg
    cph = cph[:-16]
    
    
print aes.pkcs7chk(decrypted_msg)
