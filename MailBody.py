from types import ListType

class MailBody:
	def __init__(self, header, employee_data):
		self.header = header
		self.employee_data = employee_data if (type(employee_data) is ListType) else [employee_data]

	def html(self):
		header_row = ""
		num_data_rows = len(self.employee_data)
		value_row_text = [""]*num_data_rows
		for heading in self.header:
			header_row += self.text_with_tag(heading.strip(), "th")
			for j in range(0, num_data_rows):
				value_row_text[j] += self.text_with_tag(getattr(self.employee_data[j], heading.strip()).strip(), "td")
		table_body = self.text_with_tag(header_row, "tr")
		for value_row in value_row_text:
			table_body += self.text_with_tag(value_row, "tr")
		return self.text_with_tag(table_body, "table", "border=1")

	def text_with_tag(self, value, tag, attributes = ""):
		return "<%s %s>%s</%s>" % (tag, attributes, value, tag)
