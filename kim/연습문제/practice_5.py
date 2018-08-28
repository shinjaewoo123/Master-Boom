# 5.1
import zoo
print(zoo.hours())

# 5.2
import zoo as menagerie
print(menagerie.hours())

# 5.3
from zoo import hours
print(hours())

# 5.4
from zoo import hours as info
print(info())

# 5.5
plane = {'a':1, 'b':2, 'c':3}
print(plane)

# 5.6
from collections import OrderedDict
fancy = OrderedDict(plane)
print(fancy)

# 5.7
from collections import defaultdict
dict_of_lists = defaultdict(int)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])
