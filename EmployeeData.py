class EmployeeData:
	def __init__(self, header, data):
		for i in range(0, len(header)):
			setattr(self, header[i].strip(), data[i].strip())
