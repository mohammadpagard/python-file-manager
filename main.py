import os


class FileManager:
	def find(self, name, address):
		pass

	def create_file(self, name, address):
		pass

	def create_folder(self, address, name):
		full_address = os.path.join(address, name)
		os.makedirs(full_address)

	def delete(self, name, address):
		pass

	def restore(self, name):
		pass

a1 = FileManager()
