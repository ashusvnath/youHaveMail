import os
import csv
from EmployeeData import EmployeeData

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
    		header = csv_reader.next()
    		employee_data_list = []
		for row in csv_reader:
			e = EmployeeData(header,row)
      			employee_data_list.append(e)
		input_file.close()
		return header, employee_data_list
