import os


class FileManager:
	def find(self, address):
		find_path = os.listdir(address)
		for path in find_path:
			print(path)

	def create_file(self, address, name):
		full_address = os.path.join(address, name)
		file = open(full_address, "a")
		file.close()

	def create_folder(self, address, name):
		full_address = os.path.join(address, name)
		os.makedirs(full_address)

	def delete(self, address, name):
		full_address = os.path.join(address, name)
		os.remove(full_address)

	def restore(self, name):
		pass

a1 = FileManager()
a1.find("/home/mohammad/Desktop/python-test/")
