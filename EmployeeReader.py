import csv

class MappingFileNotFound(Exception):
	def __init__(self, message = "Employee data file does not exist"):
		self.message = message
	
	def __repr__(self):
		return repr(self.message) 

class EmployeeDataReader():
	def __init__(self, filename):
		self.filename = filename
		if not os.path.exists(filename):
			raise MappingFileNotFound()			
	
	def read(self):
		input_file  = open(self.filename, "rb")
		csv_reader = csv.reader(input_file)
		rownum = 0
		for row in csv_reader:
			if rownum == 0:
				header = row
			else:
				colnum = 0
				for col in row:
					print '%-8s: %s' % (header[colnum], col)
					colnum += 1
			rownum += 1
		input_file.close()
