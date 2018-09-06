# 10.1
from datetime import date
now = date.today()
now_str = now.isoformat()

with open('today', 'wt') as fout:
	fout.write(now_str)
	
# 10.2
with open('today', 'rt') as fin:
	today_string = fin.read()
	print(today_string)
	
# 10.3
import time
fmt = '%Y-%m-%d'
time.strptime(today_string, fmt)
print(today_string)

# 10.4
import os
print(os.listdir('.'))

# 10.5
print(os.listdir('..'))

# 10.7
birthday = date(1991, 3, 2)
print(birthday)

# 10.8
print(birthday.isoweekday())

# 10.9
from datetime import timedelta
party_day = birthday + timedelta(days=10000)
print(party_day)
