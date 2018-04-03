from decimal import localcontext
from decimal import Decimal

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

'''
Python’s with statement provides a very convenient way of 
dealing with the situation where you have to do a setup and 
teardown to make something happen. A very good example for 
this is the situation where you want to gain a handler to a 
file, read data from the file and the close the file handler.
'''
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

print(a / b)
