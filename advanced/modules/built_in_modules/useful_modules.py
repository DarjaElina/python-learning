from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7, 6, 6]
print(Counter(li))

sentence = "I love pythooooon!!!"
print(Counter(sentence))

dictionary = {'a': 1, 'b': 2}
# print(dictionary['c']) ❌ KeyError: 'c'

dictionary = defaultdict(lambda: 'Does not exist.', {'a': 1, 'b': 2})
print(dictionary['a']) # 1
print(dictionary['b']) # 2
print(dictionary['c']) # Does not exist.

# datetime

import datetime

print(datetime.time(5, 45, 2)) # 05:45:02

print(datetime.date.today()) # 2026-01-30

# array

# The array module provides compact arrays of basic values (like integers and floats).

# Unlike lists, arrays store elements in a typed, tightly packed representation, which uses less memory and can be faster for large numeric data.

from array import array

arr = array('i', [1, 2, 3])

print(arr[0])