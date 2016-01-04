#Advanced Python
import csv
import string
f_dict = csv.DictReader(open('/Users/natalieabril/ds/metis/prework/dsp/python/faculty.csv'), skipinitialspace = 'True')

degrees={}
titles={}
email=[]

for row in f_dict:
#TITLE CODE
    #search for title data
    title = (row['title'].upper())
    if title not in titles:
        titles[title] = 1
    #else add one to existing value
    else:
        titles[title] += 1

#DEGREE CODE
    deg= (row['degree'].upper()).replace('.', '')
    #if index has only one item that does not equal zero
    if len(deg)<4 and deg != '0':
        #if item not in dictionary, assign it a value in dictionary
        if deg not in degrees:
            degrees[deg] = 1
        #else add one to existing value
        else:
            degrees[deg] += 1
    #if index has more than 3 chars (the max abbreviation for degree)
    #make it a nested list by splitting string
    if len(deg)>3:
        #split string by empty space
        deg =deg.split()
        #assign length of index, which in this case counts number of elements in nested list
        j = len(deg)
        #traverse through nested list and update dictionary
        for k in range(0, j):
            if deg[k] not in degrees:
                degrees[deg[k]] = 1
            else:
                degrees[deg[k]] += 1
#EMAIL CODE
    emails = row['email']
    if emails not in email:
        email.append(emails)

#EMAIL DOMAIN CODE
domains = {}
for e in email:
    d = e.split('@')
    if d[1] not in domains:
        domains[d[1]] = 1
    else:
        domains[d[1]] += 1


print 'There are %d types of degrees.' %(len(degrees))
print degrees
print
print 'There are %d types of titles.' %(len(titles))
print titles
print
print 'There are %d emails.' %(len(emails))
print email
print
print 'There are %d types of email domains.'%(len(domains))
print domains

