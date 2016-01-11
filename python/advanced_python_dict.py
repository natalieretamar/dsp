import csv
from pprint import pprint
from collections import defaultdict

f_reader = csv.DictReader(open('/Users/natalieabril/ds/metis/prework/dsp/python/faculty.csv'), skipinitialspace = 'True')

#Question 6

faculty_dict=defaultdict(list)

for f in f_reader:
    name = f['name'].split(' ')
    faculty_dict[name[-1]].append([ f['email'],f['degree'].upper().replace('.', ''),f['title']])

pprint ( faculty_dict, width = 100)

