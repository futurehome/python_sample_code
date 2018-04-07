# example.py
#
# Regular expression that matches multiline patterns

import re

text = '''/* this is a

              multiline comment */
'''

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text))

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text))

comment = re.compile(r'(?s)/\*(.*?)\*/')
print(comment.findall(text))
