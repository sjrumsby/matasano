from AESCipher import AESCipher

#Turns strings into dictionaries
def parse_routine(str):
	result = {}
	for x in str.split("&"):
		parts = x.split("=")
		if len(parts) == 2:
			result[parts[0]] = parts[1]
	return result

#Turns dictionaries into strings
def parse_to_string(dct):
	return "email=" + dct['email'] + "&uid=" + dct["uid"] + "&role=" + dct['role']
	

def profile_for(email):
	rval = {}
	if "=" not in email and "&" not in email:
		rval['email'] = email
		rval['uid'] = '10'
		rval['role'] = 'user'
	return parse_to_string(rval)


email1 = 'for@bar.coadmin' + chr(11) * 11
email2 = 'foo@bar.commm'
a = AESCipher()
enc1 = a.ecb_encrypt(profile_for(email1))
enc2 = a.ecb_encrypt(profile_for(email2))
dec1 = a.ecb_decrypt(enc1)
dec2 = a.ecb_decrypt(enc2)
dec = enc2[0:32] + enc1[16:32]
ret = a.ecb_decrypt(dec)
print ret

