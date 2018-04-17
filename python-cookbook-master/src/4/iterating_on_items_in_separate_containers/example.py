# Example of iterating over two sequences as one

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
'''
chain() performs no such operation, so it’s far
more efficient with memory if the input sequences are large
and it can be easily applied when the iterables in question
are of different types.
'''
c = [1, 2, 3, 4]
d = ('x', 'y', 'z')

for x in chain(d, c):
    print(x)
