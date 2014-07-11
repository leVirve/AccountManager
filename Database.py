import sqlite3
import os
from Crypto.Hash import SHA512

class Database():

	def __init__(self, name):
		self.name = name

		if os.path.exists('config'):
			with open('config', 'r') as tmp:
				HASHED_DB_KEY = tmp.read()[:-1]
				self.key  = input('Password >> ')
				h = SHA512.new(data = self.key.encode('utf8')).hexdigest()
				if not (h == HASHED_DB_KEY):
					raise DB_KEY_ERROR
		else:
			TEMP_DB_KEY = input('Set Database Password >>> ')
			self.key = TEMP_DB_KEY
			h = SHA512.new(data = TEMP_DB_KEY.encode('utf8'))

			config = open('config', 'w')
			print(h.hexdigest(), file = config)

	def connect(self):
		create = not os.path.exists(self.name)
		conn = sqlite3.connect(self.name)    

		if create:
			cursor = conn.cursor()
			cursor.execute("CREATE TABLE account ("
				"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
				"domain TEXT NOT NULL,"
				"name TEXT NOT NULL,"
				"passw TEXT NOT NULL,"
				"comment TEXT)")
			conn.commit()

		self.conn = conn

	def add(self, entry):
		entry = entry.split('\t')
		entry.append('')
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO account "
			"(domain, name, passw, comment) "
			"VALUES (?, ?, ?, ?)",
			(entry[0], entry[1], entry[2], entry[3]))
		self.conn.commit()

	# required when effitiency needed
	def addEntries(self):
		pass

	def query(self, string):
		cursor = self.conn.cursor()
		cursor.execute("SELECT domain, name, passw, comment FROM account WHERE domain=?",
			(string,))
		fields = cursor.fetchall()
		return fields if fields is not None else None

	def delete(self, query):
		cursor = self.conn.cursor()
		cursor.execute("DELETE FROM account WHERE id=?",
			(query,))
		self.conn.commit()

	def all(self):
		cursor = self.conn.cursor()
		cursor.execute("SELECT id, domain, name, comment FROM account")

		fields = cursor.fetchall()
		return fields if fields is not None else None