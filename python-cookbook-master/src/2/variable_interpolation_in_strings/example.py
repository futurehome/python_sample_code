# example.py
#
# Examples of variable interpolation

# Class for performing safe substitutions
import sys


class safesub(dict):
    def __missing__(self, key):
        return '{%s}' % key


s1 = '{} has {} messages.'
print(s1.format('Guido', '37'))

s = '{name} has {n} messages.'
print(s.format(name='Guido', n='37'))

# (a) Simple substitution
name = 'Guido'
n = 37

print(s.format_map(vars()))

# (b) Safe substitution with missing values
del n
print(s.format_map(safesub(vars())))

# (c) Safe substitution + frame hack
n = 37


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


print(sub('Hello {name}'))
print(sub('{name} has {n} messages'))
print(sub('Your favorite color is {color}'))
