import csv 

with open('original.csv') as originalcsv: #reads the original CSV
	reader = csv.reader(originalcsv, delimiter=',')
	with open('final.csv', 'wb') as finalcsv: #opens the final CSV
		writer = csv.writer(finalcsv)
		for row in reader:
			row[8] = " ".join(row[8].split()).strip()
			writer.writerow(row) #splits the rows and are organized


finalcsv.close()