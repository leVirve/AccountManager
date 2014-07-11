from Entry import Entry
from Database import Database

db_name = 'dataset'

class Manager():

	def __init__(self, data = 'data.in'):
		self.db = Database(db_name)
		self.key = self.db.key
		self.input  = data
		print('datadata')
		self.db.connect()

	def add(self):
		line = input('New entry >> ')
		e = Entry(self.key, line, 'manual')
		self.db.add(e.encode())

	def addList(self):
		with open(self.input, 'r') as file:
			for line in file.readlines():
				e = Entry(self.key, line, 'list')
				self.db.add(e.encode())

	def query(self):
		word = input('Query >> ')
		result = self.db.query(word)
		for row in result:
			print(Entry(self.key, row, 'query').decode())

	def delete(self):
		word = input('Delete >> ')
		result = self.db.delete(int(word))

	def all(self):
		result = self.db.all()
		for row in result:
			print(row)


	def help(self):
		text = '==== Account Manager ====\n'\
		 '0 : add accounts list in file named "data.in"\n'\
		 '1 : add account manually\n'\
		 '2 : search account info in database\n'\
		 '3 : delete account in database by ID\n'\
		 'q : exit\n'
		print(text)

if __name__ == '__main__':
	
	manager = Manager()

	instructions = {
		-1: manager.all,
		0: manager.addList,
		1: manager.add,
		2: manager.query,
		3: manager.delete
	}

	manager.help()

	while True:
		inst = input('> ')
		if(inst == 'q'):
			break
		instructions[int(inst)]()
