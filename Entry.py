from Cipher import AESCipher

class Entry():

	def __init__(self, key, data, inputType = 'list'):
		if inputType == 'manual':
			self.fields = data.split()
			self.fields[3] = ' '.join(self.fields[3:])

		elif inputType == 'query':
			self.fields = list(data)

		else:
			self.fields = data[:-1].split('\t')
	
		self.cipher = AESCipher(key)

	def __str__(self):

		return '\t'.join(self.fields) + '\n'

	def encode(self):
		print('Account {0} {1} 處理中...'.format(self.fields[0], self.fields[1]))
		self.fields[2] = self.cipher.encrypt(self.fields[2]).decode('utf8')

		return self.__str__()

	def decode(self):
		self.fields[2] = self.cipher.decrypt(self.fields[2]).decode('utf8')

		return self.__str__().strip()
