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

#question7 
professor_dict= {}

for prof in f_reader:
    name= prof['name'].split(" ")
    f_name, l_name = name[0], name[-1]
    professor_dict[(f_name,l_name)] = [prof['degree'].upper().replace('.', ''),prof['title'], prof['email']]
pprint(professor_dict.items()[:3])

#Question 8
pprint(sorted(professor_dict.items(), key=lambda (k, v): (k[0], k[-1]))[:3])
 

