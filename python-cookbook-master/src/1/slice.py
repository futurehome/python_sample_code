s = 'HelloWorld'
a = slice(5,50,2)
'''
you can map a slice onto a sequence of a specific size by using its indi
ces(size) method. This returns a tuple (start, stop, step) where all values have
been suitably limited to fit within bounds (as to avoid IndexError exceptions when
indexing)
'''
t = a.indices(len(s))
'''
Generally, you can use the func(*tuple) syntax. You can even pass a part of the tuple.
This is called unpacking a tuple, and can be used for other iterables (such as lists) too.

Unpacking is used to pass a set of parameters to anywhere which require the same numbers of 
paramters.
'''
for i in range(*a.indices(len(s))):
    print(s[i])

l = [3,20,3]
lt = range(*l)