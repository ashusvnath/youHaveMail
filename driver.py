from EmployeeDataReader import EmployeeDataReader
from MailBody import MailBody
from Mailer import Mailer
from Constants import Constants
if __name__ == '__main__':
	empdata_reader = EmployeeDataReader(Constants.MAPPING_FILE)
	header, employee_data_list = empdata_reader.read()
	mailer = Mailer('vishwas@thoughtworks.com')
	for employee_data in employee_data_list:
		mailer.send_mail("%s@thoughtworks.com" % employee_data.employee_id, 'Test mail', MailBody(header, employee_data).html(), Constants.MAPPING_FILE)
