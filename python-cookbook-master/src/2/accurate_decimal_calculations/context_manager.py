from contextlib import contextmanager

'''
One nice shortcut to creating a context manager from a class 
is to use the @contextmanager decorator. To use it, decorate 
a generator function that calls yield exactly once. Everything 
before the call to yield is considered the code for __enter__(). 
Everything after is the code for __exit__(). 
'''
@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(10):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
    print(f)