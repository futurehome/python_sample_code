class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{:%s}: {:%s}'.format(self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

# Different instances of same class can have different attributes.
# Attributes of specific instances can be added dynamically.
bart.age = 8
print(bart.age)
print(lisa.age)
