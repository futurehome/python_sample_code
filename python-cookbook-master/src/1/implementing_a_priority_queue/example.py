# example.py
#
# Example of a priority queue

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# Example use
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        '''The conversion field causes a type coercion before formatting. 
        Normally, the job of formatting a value is done by the __format__() 
        method of the value itself. However, in some cases it is desirable 
        to force a type to be formatted as a string, overriding its own 
        definition of formatting. By converting the value to a string before 
        calling __format__(), the normal formatting logic is bypassed.

        Three conversion flags are currently supported: 
        '!s' which calls str() on the value, 
        '!r' which calls repr() and 
        '!a' which calls ascii()
        '''
        #def __str__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.push(Item('sad'), 2)
q.push(Item('glue'), 6)

print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())
