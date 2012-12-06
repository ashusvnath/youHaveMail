class MailBody:
	def __init__(self, header, employee_data):
		self.header = header
		self.employee_data = employee_data

	def html(self):
		header_row = ""
		value_row = ""
		for i in range(0,len(self.header)):
			header_row += self.text_with_tag(self.header[i], "th")
			value_row += self.text_with_tag(getattr(self.employee_data, self.header[i]), "td")
		header_row = self.text_with_tag(header_row, "tr")
		value_row = self.text_with_tag(value_row, "tr")
		return self.text_with_tag(header_row + value_row, "table", "border=1")

	def text_with_tag(self, value, tag, attributes = ""):
		return "<%s %s>%s</%s>" % (tag, attributes, value, tag)
