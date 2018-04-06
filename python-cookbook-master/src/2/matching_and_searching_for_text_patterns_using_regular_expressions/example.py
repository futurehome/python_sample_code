# example.py
#
# Examples of simple regular expression matching

import re

# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/13.'

# (a) Find all matching dates
datepat = re.compile(r'\d{1,2}/\d{1,2}/(?:\d{4}|\d{2})')
print(datepat.findall(text))

# (b) Find all matching dates with capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# (c) Iterative search
for m in datepat.finditer(text):
    print(m.groups())
