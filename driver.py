from EmployeeDataReader import EmployeeDataReader
from MailBody import MailBody
from Mailer import Mailer
from Constants import Constants
import sys

import os
if __name__ == '__main__':
	empdata_reader = EmployeeDataReader(Constants.MAPPING_FILE)
	header, employee_data_list = empdata_reader.read()
	sender = raw_input("Enter mail_id of sender(Eg: <asdf>@thoughtworks.com) : ")
	mailer = Mailer(sender)
	e = None
	try:
		employees_without_bill_file = []
		for employee_data in employee_data_list:
			if os.path.exists("%s.pdf" % employee_data.mobile_number):
				mailer.send_mail(('%s@thoughtworks.com' % employee_data.employee_id), 'Your bill for the month between %s and %s' % (employee_data.start_date, employee_data.end_date), MailBody(header, employee_data).html(), Constants.MAPPING_FILE)
			else:
				employees_without_bill_file.append(employee_data)
		new_header = ["employee_id", "name", "mobile_number"]
		if len(employees_without_bill_file) > 0:
			mailer.send_mail(sender, 'Employees who did not get their bill', MailBody(new_header, employees_without_bill_file).html())
	except Exception as exception:
		e = exception
	finally:
		mailer.close()
	if e != None:
		raise e
