# Example of a generator with extra state that can be
# accessed.   Simply define as a class!

from collections import deque


class linehistory:
    def __init__(self, line, histlen=3):
        self.lines = line
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('python-cookbook-master/src/4/generators_with_state/somefile.txt'
          ) as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
