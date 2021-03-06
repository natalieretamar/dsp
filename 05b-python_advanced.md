## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> There are 8 different types of degrees. MD:1, MA:1, SCD:6, BSED:1, PHD:31, MPH:2, MS:2, JD:1


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> There are 3 types of positions. Assistant Professor of Biostatistics: 12, Professor of Biostatistics: 13, Associate Professor OF Biostatistics: 12. Note: 1 position was recorded as 'Assistant Professor in Biostatistics, which was recorded as 'Assistant Professor of Biostatistics'.



####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> There are 26 email addresses.


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> There are 4 types of email domains:
>> email.chop.edu:1, upenn.edu:12, cceb.med.upenn.edu:1, mail.med.upenn.edu:23

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

[('Putt',

  [['mputt@mail.med.upenn.edu', 'PHD SCD', 'Professor of Biostatistics']]),

 ('Feng',

  [['ruifeng@upenn.edu', 'PHD', 'Assistant Professor of Biostatistics']]),

 ('Bilker', [['warren@upenn.edu', 'PHD', 'Professor of Biostatistics']])]



####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

[(('Yimei', 'Li'),

  ['PHD', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']),

 (('Hongzhe', 'Li'),

  ['PHD', 'Professor of Biostatistics', 'hongzhe@upenn.edu']),

 (('Justine', 'Shults'),

  ['PHD', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'])]

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

[(('A.', 'Localio'),
  ['JD MA MPH MS PHD',
   'Associate Professor of Biostatistics',
   'rlocalio@upenn.edu']),
 (('Alisa', 'Stephens'),
  ['PHD',
   'Assistant Professor of Biostatistics',
   'alisaste@mail.med.upenn.edu']),
 (('Andrea', 'Troxel'),
  ['SCD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu'])]

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

