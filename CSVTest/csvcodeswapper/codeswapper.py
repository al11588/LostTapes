import csv 

with open('original.csv') as originalcsv: #reads the original CSV
	reader = csv.reader(originalcsv, delimiter=',')
	with open('final.csv', 'wb') as finalcsv: #opens the final CSV
		writer = csv.writer(finalcsv)
		counter = 0
		for row in reader:
			row[0] = row[1] #splits the rows and are organized
			writer.writerow(row)

finalcsv.close()