import csv

input_file  = open('mapping.csv', "rb")
csv_reader = csv.reader(ifile)

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
