# example.py
'''
One possible use of a is as a replacement for a dictionary, which requires
namedtuple more space to store. Thus, if you are building large data structures 
involving dictionaries, use of a will be more efficient. However, be aware that 
unlike a dictionary, namedtuple a is immutable.
'''

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# Some Data
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),
    ('IBM', 50, 91.15)
]

print(compute_cost(records))

