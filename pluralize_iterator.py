#import fibonacci2
#
#for n in fibonacci2.Fib(1000):
#    print(n, end=' ')

import plural6

rule = plural6.LazyRules()

def plural(noun):
    for matches_rule, apply_rule in rule:
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

print(plural('vacancy'))