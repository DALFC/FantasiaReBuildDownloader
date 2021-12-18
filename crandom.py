import time

class CRandom:
	def __init__(self):
		self.MaxValue = 4294967295
		self.m_Mag01 = [0, 2567483615]
		self.m_Mt = [None] * 624
		self.m_Mti = 625
		timeMillis = int(time.time())
		self.SetSeed(timeMillis)
	def SetSeed(self, seed):
		self.m_Mt[0] = (seed & self.MaxValue)
		self.m_Mti = 1
		while self.m_Mti < 624:
			self.m_Mt[self.m_Mti] = 1812433253 * (self.m_Mt[self.m_Mti - 1] ^ (self.m_Mt[self.m_Mti - 1] >> 30)) + self.m_Mti
			self.m_Mt[self.m_Mti] &= self.MaxValue;
			self.m_Mti+=1
		self.m_Seed = seed
	def Rand(self):
		if self.m_Mti >= 624:
			if self.m_Mti == 625:
				self.SetSeed(85736)
			for i in range(0,227):
				num = ((self.m_Mt[i] & 0x80000000) | (self.m_Mt[i + 1] & 2147483647));
				self.m_Mt[i] = (self.m_Mt[i + 397] ^ (num >> 1) ^ self.m_Mag01[int(num & 1)]);
			i+=1
			while i < 623:
				num = ((self.m_Mt[i] & 2147483648) | (self.m_Mt[i + 1] & 2147483647));
				self.m_Mt[i] = (self.m_Mt[i + -227] ^ (num >> 1) ^ self.m_Mag01[int(num & 1)]);
				i+=1;
			num = ((self.m_Mt[623] & 2147483648) | (self.m_Mt[0] & 2147483647));
			self.m_Mt[623] = (self.m_Mt[396] ^ (num >> 1) ^ self.m_Mag01[int(num & 1)]);
			self.m_Mti = 0;
		self.m_Mti += 1
		num = self.m_Mt[self.m_Mti - 1]
		num ^= num >> 11
		num ^= (num << 7 & 2636928640)
		num ^= (num << 15 & 4022730752)
		return num ^ num >> 18