import os


class FileManager:
	def find(self, address, name):
		pass

	def create_file(self, address, name):
		full_address = os.path.join(address, name)
		file = open(full_address, "a")
		file.close()

	def create_folder(self, address, name):
		full_address = os.path.join(address, name)
		os.makedirs(full_address)

	def delete(self, address, name):
		pass

	def restore(self, name):
		pass

a1 = FileManager()