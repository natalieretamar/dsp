# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are similar because they are both sequences of values however the values in tuples can not be changed unlike lists. Tuple elements are immutable. In addition, lists use square brackets and tuples use parentheses to enclose its elelements. Tuples will work as keys in dictionaries because they are made up of key-value pairs.  

---

###Q2. Lists &amp; Sets

>>How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>Python lists and sets are both collections of values. They can have any number of values and may be of different types but sets are an ordered collection of items and each item must be unique. There can not be any duplicates whereas in a list, duplicates can exist. Sets are also immutable and they require items to be hashable. Lists can be modified and their items are not required to be hashable. Even though the items in sets are immutable, the set itself is mutable, just like lists. items can be removed or added. Unlike lists, sets can be used to perform mathematical set operations like union, intersection, etc. List and set syntax is different. For example, to create a list square brackets are used. To assign a set, curly braces are used. 

Examples:
a_set= {1,2,3} #creating a set
a_list= [1,2,2,3]#creating a list, duplicates are allowed

To declare an empty set, the set() function must be used because empty curly braces will create a dictionary. 

Example:
empty_set = {}#creates a dictionary
empty_set = set() #creates a SET

>>Sets are faster with finding membership. Since the items are hashable, a set can locate if an item exists in a given set much quicker then a list because it does not have to iterate through each item in a list. the speed for finding an element in a set regardless of size is O(1) vs. the speed of finding an element in a list which is O(n).

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

The Lambda function is a way to create one line, small functions without a name. They are just needed where they have been created. Unlike regular functions, they use an abbreviated syntax and the return keyword is implied not assigned. The function is nameless and can be called by the variable it was assigned to, if one was assigned since variable assignment is not optional. It takes any number of arguments and returns the value of a single expression. 

Example of a lambda multiplication function:
a= lambda: 5*9*6

Lambda is often used in the sorted() function because it can be specifically directly inline in the function. If we wanted to sort a tuple by the second value in each tuple, we could use a lambda function in the sorted() function to sort by the value we need thus eliminating a need to write a separate function for specifying a key. 

Example:
sorted(tuple_name, key=lambda tuple_name: tuple_name[1]

That one line of code would return a tuple list sorted by its second value. 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

 Map, filter and list comprehension each provide a function to each iterable element in a list but list comprehension is easier to use for simpler functions because a separate function does not have to be created. List comprehensions collect the result of applying an expression to a sequence and returns them in a new list. The effect is similar to a for loop and the map call but list comprehensions are more convenient and concise because they use less code and are easier to read.
The syntax for list comprehension is based on set notation:
syntax: [ output_value for element in list ]

Example:

The following function builds a list that multiplies each item by 2 using map () function:
my_list= [2,3,4]
>>def multiply_by_two(x): 
>>return x*2

new_list=map(multiply*2, my_list)

Same result can be used with list comprehension:
my_list= [2, 3,4,]
new_list = [ x* 2 for x in my_list] #list comprehension

Filter function allows you to create a new list from an old list based on conditions. 
Example:
my_list=[2,3,4,5,6,7]
def even_num(x):
>>if x % 2 ==0
>>return x

new_list= filter(even_num, my_list)
>>(2,4,6)

Same result could be had using list comprehension:
my_list= [2,3,4,5,6,7]
new_list= x for x in my_list if x%2==0

Set comprehension is similar to list comprehension but returns a set, not a list. The notation is similar to the traditional mathematical notation for expressing sets in terms of other sets.
Example:
old_set= {2,5,8}
new_set= {2*x for x in old_set}

Dictionary comprehension is used to create a new dictionary from an iterable item.
Example:
my_list= [1,2,3]
new_dict = {x:x**2 for x in my_list}
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> Difference is: 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> Difference is: 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> Difference is: 7,850 days.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





