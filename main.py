import os
import subprocess as sp
# import winshell


class FileManager:
	def find(self, address):
		find_path = os.listdir(address)
		for path in find_path:
			print(path)

	def create_file(self, address, name):
		full_address = os.path.join(address, name)
		file = open(full_address, "a")
		file.close()

	def create_dir(self, address, name):
		full_address = os.path.join(address, name)
		os.makedirs(full_address)

	def delete(self, address, name):
		full_address = os.path.join(address, name)
		os.remove(full_address)

	def restore(self, name, new_adress=None):
		# On linux
		sp.run(['mv', name, new_adress])

		# On windows
		# r = list(winshell.recycle_bin())
		# index = r.index(name)
		# winshell.undelete(r[index].orginal_filename())


a1 = FileManager()
# a1.restore('/home/username/.local/share/Trash/files/test.3.txt', '/home/username/Desktop/test.txt')
# a1.find('/home/username/Desktop/MyFiles/')
