# example.py
#
# Examples of reformatting text to different column widths

import textwrap
import os

# A long string
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print()

print(textwrap.fill(s, os.get_terminal_size().columns))
print()

print(textwrap.fill(s, 40, initial_indent='    '))
print()

print(textwrap.fill(s, 40, subsequent_indent='    '))
print()
