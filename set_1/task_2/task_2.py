def xor(val1, val2):
	params = {
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
	rev_params = dict((v,k) for k,v in params.iteritems())

	val1 = params[val1]
	val2 = params[val2]

	rval = ""

	for i in range(0,4):
		if val1[i] == val2[i]:
			rval += "0"
		else:
			rval += "1"
	rval = rev_params[rval.zfill(4)]
	return rval


str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"
result = ""
output = "746865206b696420646f6e277420706c6179"

for i in range(0, len(str1)):
	result += xor(str1[i], str2[i])

if output == result:
	print "Pass! : )"
else:
	print result
	print output
	print "Fail. : ("
