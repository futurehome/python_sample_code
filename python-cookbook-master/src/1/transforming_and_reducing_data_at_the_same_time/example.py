# example.py
#
# Some examples of using generators in arguments

'''
The generator solution transforms the data iteratively and is 
therefore much more memory-efficient.
'''
import os
files = os.listdir(os.path.expanduser('~'))
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_shares = min(portfolio, key=lambda x:x['shares'])
print(min_shares)
