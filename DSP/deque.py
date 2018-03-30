#from collections import deque
#
#
#def search(lines, pattern, history=5):
#    previous_lines = deque(maxlen=history)
#    for line in lines:
#        if pattern in line:
#            yield line, previous_lines
#        previous_lines.append(line)
#
#
## Example use on a file
#if __name__ == '__main__':
#    with open('DSP/somefile.txt') as f:
#        for line, prevlines in search(f, 'python', 5):
#            for pline in prevlines:
#                print(pline, end='')
#            print(line, end='')
#            print('-' * 20)
    
import heapq
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
for s in portfolio:
    t = s['price']

