from datetime import datetime

from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

# Next Friday
print(d + relativedelta(weekday=FR))

# Last Friday
print(d + relativedelta(weeks=-2, weekday=FR(-1)))
