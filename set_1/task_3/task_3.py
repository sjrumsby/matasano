import binascii

def histogram_analysis(bits):
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

        highest_score = 0
        likely_letter = ''
        for i in range(32,128):
                score = 0
		split_bits = [bits[x:x+8] for x in range(0, len(bits), 8)]
                for j in split_bits:
                        result = int(j,2) ^ int(bin(i)[2:].zfill(8),2)
                        if result > 0 and result < 256:
                                letter = chr(result).lower()
                                try:
                                        score += letter_freqs[letter]
                                except:
					score -= 2
                        else:
                                score -= 2
                if score > highest_score:
                        highest_score = score
                        likely_letter = chr(i)
        return likely_letter

def singleByteXOrDecrypt(cipher, enc):
	result = ""
	split_bits = [cipher[x:x+8] for x in range(0, len(cipher), 8)]
	for j in split_bits:
		result += chr(int(j,2) ^ int(bin(ord('X'))[2:].zfill(8),2))
	return result

hex_to_bin = {
                "0" : "0000",
                "1" : "0001",
                "2" : "0010",
                "3" : "0011",
                "4" : "0100",
                "5" : "0101",
                "6" : "0110",
                "7" : "0111",
                "8" : "1000",
                "9" : "1001",
                "A" : "1010",
                "B" : "1011",
                "C" : "1100",
                "D" : "1101",
                "E" : "1110",
                "a" : "1010",
                "b" : "1011",
                "c" : "1100",
                "d" : "1101",
                "e" : "1110",
                "f" : "1111",
             }

cipher_bits = ''.join([hex_to_bin[x] for x in "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"])
success = 0

letter = histogram_analysis(cipher_bits)
plain_text = singleByteXOrDecrypt(cipher_bits, letter)

print '(%s) %s' % (letter, plain_text)

