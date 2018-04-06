import re

text = 'UPPER PYTHON, lower python, Mixed Python'


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

datapattern = re.compile(r'(?i)python')
print(datapattern.sub(matchcase('snake'), text))
