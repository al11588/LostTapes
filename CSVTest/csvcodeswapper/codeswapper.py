import csv 
#reads the original CSV
with open('original.csv') as originalcsv: 
	#adds the delimeter to the file
	reader = csv.reader(originalcsv, delimiter=',')
	#opens the final CSV
	with open('final.csv', 'wb') as finalcsv: 
		writer = csv.writer(finalcsv)
		
		for row in reader:
			row[0] = row[1] #splits the rows and are organized
			writer.writerow(row)

finalcsv.close()