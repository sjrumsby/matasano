def try_char(cipher, char):
        letter_freqs = {
                        "a" : 8.167,
                        "b" : 1.492,
                        "c" : 2.782,
                        "d" : 4.253,
                        "e" : 12.702,
                        "f" : 2.228,
                        "g" : 2.015,
                        "h" : 6.094,
                        "i" : 6.966,
                        "j" : 0.153,
                        "k" : 0.772,
                        "l" : 4.025,
                        "m" : 2.406,
                        "n" : 6.749,
                        "o" : 7.507,
                        "p" : 1.929,
                        "q" : 0.095,
                        "r" : 5.987,
                        "s" : 6.327,
                        "t" : 9.056,
                        "u" : 2.758,
                        "v" : 0.978,
                        "v" : 0.978,
                        "w" : 2.361,
                        "x" : 0.150,
                        "y" : 1.974,
                        "z" : 0.074,
                        " " : 15
                        }
	score = 0

	for c in [cipher[i:i+2] for i in range(0, len(cipher), 2)]:
		result = int(hex(int(c,16) ^ int(bin(char),2))[2:].zfill(2), 16)
		if result > 32 and result < 128:
			try: 
				score += letter_freqs[chr(result).lower()]
			except:
				score -= 2
		else:
			score -= 2
	return score

def singleByteXOrDecrypt(cipher, enc):
        result = ""
        split_bits = [cipher[x:x+2] for x in range(0, len(cipher), 2)]
        for j in split_bits:
                result += chr(int(j,16) ^ int(bin(ord(str(enc)))[2:].zfill(8),2))
        return result

f = open('task4_strings.txt', 'r')
words = [x.strip() for x in f.readlines()]
f.close()
results = []

highest_score = 0
likeliest_string = ''
likeliest_letter = ''

for w in words:
	word_dict = {}
	for i in range(32,128):
		score = try_char(w,i)
		if score > highest_score:
			highest_score = score
			likeliest_string = w
			likeliest_letter = chr(i)

print "String: %s\nLetter: %s\nDecrypted: %s" % (likeliest_string, likeliest_letter, singleByteXOrDecrypt(likeliest_string, likeliest_letter).strip())
