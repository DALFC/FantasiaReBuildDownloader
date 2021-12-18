import codecs, base64, zlib, json, lzma
from crandom import CRandom

def DecryptJSONString(string):
	if len(string) < 3:
		return None
	s = string[0:3]
	num = 0
	try:
		num = int(s)
	except:
		print("Failed to convert string to int")
		return None
	text = string[3:]
	if num == 1:
		# No sample to test
		ar = base64.b64decode(text)
		array = bytearray(ar)
		crandom = CRandom()
		length = len(array)
		seed = length + (length & 9139450)
		crandom.SetSeed(seed)
		for i in range(0,length):
			b = (crandom.Rand() & 255)
			array[j] = (~(array[j] ^ b)) & 255
		return None #zlib.decompress(array).decode("utf-8")
	elif num == 2:
		ar = base64.b64decode(text)
		array = bytearray(ar)
		crandom2 = CRandom()
		length = len(array)
		seed = length + (length & 9139450)
		crandom2.SetSeed(seed)
		for j in range(0,length):
			b2 = (crandom2.Rand() & 255)
			b3 = (crandom2.Rand() & 255)
			array[j] = ((array[j] - b3) ^ b2) & 255
		return zlib.decompress(array).decode("utf-8")
	elif num == 3:
		text_rot13 = codecs.encode(text[::-1], 'rot_13')
		result = base64.b64decode(text_rot13)
		return zlib.decompress(result).decode("utf-8")
	else:
		return None

def DecompressLZMA(filename):
	with lzma.open(filename) as f:
		return f.read()