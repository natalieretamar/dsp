# Hint:  use Google to find python function

####a) 
#date_start = '01-02-2013'  
#date_stop = '07-28-2015'   


#code to compute amount of days between two dates in string format 'mm-dd-yyyy'
import datetime
#global variables
month=''
day=0
year=0

date_start = '01-02-2013'
date_stop= '07-28-2015'

#assigns month, day & year values for date string passed to be used with datetime.date()
def convert_date(x):
    global month, day, year
    delimiter = '-'
    month=int(x.split(delimiter)[0])
    day=int(x.split(delimiter)[1])
    year=int(x.split(delimiter)[2])

#start date
convert_date(date_start)
new_start = datetime.date(year,month, day)

#stop date
convert_date(date_stop)
new_stop = datetime.date(year,month, day)

#calculating difference in days
difference = new_stop - new_start
print 'Difference in days between %s and %s is : %d' %(date_stop,date_start,difference.days)


####b)  
#date_start = '12312013'  
#date_stop = '05282015'  

#code to compute amount of days between two dates in string format 'mmddyyyy'
import datetime
#global variables
month = 0
day = 0
year = 0

date_start = '12312013'
date_stop = '05282015'

#assigns month, day & year values for date string passed to be used with datetime.date()
def convert_date(x):
    global month, day, year
    month=int(x[:2])
    day=int(x[2:4])
    year=int(x[4:])

#start date
convert_date(date_start)
new_start = datetime.date(year,month, day)

#stop date
convert_date(date_stop)
new_stop = datetime.date(year,month, day)

#calculating difference in days
difference = new_stop - new_start
print 'Difference in days between %s and %s is: %d' %(new_stop,new_start,difference.days)


####c)  
#date_start = '15-Jan-1994'  
#date_stop = '14-Jul-2015'  

#code to compute amount of days between two dates in string format 'dd-mmm-yyyy'
import datetime
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
month=''
day=0
year=0

#month dictionary
months = {'Jan': 1,'Feb': 2,'Mar': 3,'Apr': 4,'May': 5,'Jun': 6,'Jul': 7,'Aug': 8, 'Sep':9,'Oct':10,'Nov':11,'Dec':12}

#convert string month to int
def convert_month(x):
    if x in months:
        return months[x]

#convert date string to int date format: yyyy-mm-dd
def convert_date(x):
    global month, day, year
    delimiter = '-'
    day=int(x.split(delimiter)[0])
    month=convert_month(x.split(delimiter)[1])
    year=int(x.split(delimiter)[2])

#start date
convert_date(date_start)
new_start = datetime.date(year,month, day)

#stop date
convert_date(date_stop)
new_stop = datetime.date(year,month, day)

#calculating difference in days
difference= new_stop - new_start
print 'Difference in days between %s and %s is : %d' %(date_stop,date_start,difference.days)

