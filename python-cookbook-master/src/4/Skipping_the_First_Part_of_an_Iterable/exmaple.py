from itertools import dropwhile, islice

with open(
        'python-cookbook-master/src/4/Skipping_the_First_Part_of_an_Iterable \
        /sample.txt'
) as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
print(end='\n')
