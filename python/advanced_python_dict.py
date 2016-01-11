import csv
from pprint import pprint
f_reader = csv.DictReader(open('/Users/natalieabril/ds/metis/prework/dsp/python/faculty.csv'), skipinitialspace = 'True')
faculty_dict={}

for f in f_reader:
    name = f['name'].split(' ')
    email = f['email']
    degree= (f['degree'].upper()).replace('.', '')
    title = f['title']

    if name[-1] not in faculty_dict:

        faculty_dict[name[-1]]= [[degree, title, email]]
    else:
        faculty_dict[name[-1]].append([[email, degree, title]])
   

pprint ( faculty_dict, width = 100)

