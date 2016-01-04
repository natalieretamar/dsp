#emails.csv
import csv
faculty_file = csv.DictReader(open('/Users/natalieabril/ds/metis/prework/dsp/python/faculty.csv'), skipinitialspace = 'True')

outfile = open('emails.csv', 'wb')
writer = csv.writer(outfile, delimiter = '\n')

emails=[]

for row in faculty_file:
    emails.append(row['email'])

writer.writerow(emails)
