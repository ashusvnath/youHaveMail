class MailBody:
	def __init__(self, header, csvrow):
		self.header = header
		self.csvrow = csvrow

	def txt(self):
		header_row = ""
		value_row = ""
		for i in range(0,len(self.header)):
			header_row += self.text_with_tag(self.header[i], "th")
			value_row += self.text_with_tag(self.csvrow[i], "td")
		header_row = self.text_with_tag(header_row, "tr")
		value_row = self.text_with_tag(value_row, "tr")
		return self.text_with_tag(header_row + value_row, "table")

  def textWithTag(self, value, tag):
		return "<%s>%s</%s>" % (tag, value, tag)
