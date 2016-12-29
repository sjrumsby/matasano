import binascii

def pretty(d, indent=0):
   for key, value in d.iteritems():
      print '\t' * indent + str(key)
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print '\t' * (indent+1) + str(value)

def hamming_distance(bits1, bits2):
	distance = 0
	if len(bits1) == len(bits2):
		for i in range(0,len(bits1)):
			if bits1[i] != bits2[i]:
				distance += 1
		return distance
	else:
		print len(bits1)
		print len(bits2)
		return 1

def bit_iterator(bits):
	hamdist = 0
	for i in range(0, len(bits)):
		for j in range(i+1, len(bits)):
			hamdist += hamming_distance(bits[i], bits[j])
	return hamdist

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
		for j in range(0,len(bits)):
			result = int(bits[j].zfill(8),2) ^ int(bin(i).zfill(8)[2:].zfill(8),2)
			if result > 0 and result < 256:
				letter = chr(result).lower()
				try:
					score += letter_freqs[letter]
				except:
					pass
			else:
				score -= 20
		if score > highest_score:
			highest_score = score
			likely_letter = chr(i)
		#print "Testing char: %s. Score: %s" % (chr(i), score)
	return likely_letter

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

test_string1 = ''.join(format(ord(x), '08b') for x in "this is a test")
test_string2 = ''.join(format(ord(x), '08b') for x in "wokka wokka!!!")

if hamming_distance(test_string1, test_string2) == 37:
	print "Correct hamming distance function"
else:
	exit()

f = open('task6_file.txt', 'r')
enc_data = ''.join( x for x in [x.strip() for x in f.readlines()])
f.close()

bin_enc_data = ''.join(hex_to_bin[x] for x in binascii.a2b_base64(enc_data).encode('hex'))
bin_data_len = len(bin_enc_data)

distances = {}

for k in range(2,50):
	count = 0
	strings = []
	while count < 5:
		strings.append(bin_enc_data[count*k*8:(count+1)*k*8])
		count += 1

	total_distance = bit_iterator(strings)
	distances[k] = {'key' : k, 't_dist' : total_distance, 'norm_dist' : float(total_distance)/k}

print "Computing keysizes..."
print "\nKeysizes: %s\n\n" % distances

lowest_norm_distance = float("inf")
lowest_keysize = 1

for k in range(2,50):
	if distances[k]['norm_dist'] < lowest_norm_distance:
		lowest_norm_distance  = distances[k]['norm_dist']
		lowest_keysize = k

print "The lowest keysize is: %s\n" % lowest_keysize

blocks = []

for i in range(0,29):
	blocks.append(bin_enc_data[i*lowest_keysize*8:(i+1)*lowest_keysize*8])

transposed_blocks = []

for i in range(0,29):
	bit_block = []
	for j in range(0,29):
		bit_block.append(blocks[j][i*8:(i+1)*8])
	transposed_blocks.append(bit_block)

cipher = ""

for k in range(0,29):
	letter = histogram_analysis(transposed_blocks[k])
	print "Performing histogram analysis on bit %s. Likely bit: %s" % (k, letter)
	cipher += letter

print "\nMost likely cipher:\n"
print cipher

hex_cipher = ''.join([str(bin(ord(x)))[2:].zfill(8) for x in cipher])

i = 0
result = []
clear_text = ""

for b in blocks:
	result.append( bin(int(b,2) ^ int(hex_cipher,2))[2:].zfill(len(hex_cipher)) )

for r in result:
	char_bits = [r[i:i+8] for i in range(0,len(r),8)]
	for c in char_bits:
		clear_text += chr(int(c,2))

print "\n === CLEAR TEXT ===\n\n" + clear_text
