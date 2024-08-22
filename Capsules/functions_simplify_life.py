## 1. pprint
import pprint
import json

with open("load.json", "r") as f:
    data = json.load(f)

print(data)
pprint.pprint(data)


## 2. default dict
from collections import defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
words_count = defaultdict(int)

for word in words:
    words_count[word] += 1

print(dict(words_count))


## 3. any
numbers = [0, 1, 2, 3]
print(any(numbers))  # => True

numbers2 = [-1, -2, 0, -4]
print(any(num > 0 for num in numbers2))  # => False

strings = ["apple", "", "banana"]
print(any(s == "" for s in strings))  # => True


## 4. all
numbers = [1, 2, 3, 4]
print(all(num > 0 for num in numbers))  # => True

strings = ["apple", "banana", "cherry"]
print(all(len(s) > 3 for s in strings))  # => True


## 5. Counter (frequency dictionary)
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(counter(words))


## 6. timeit
import timeit

#   Implementation 1: List comprehension
code1 = """
a = [1, 2, 3, 4, 5]
b = [x*2 for x in a]
"""


#   Implementation 2: Map function
def code2():
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x: x * 2, a))


def code3():
    a = [1, 2, 3, 4, 5]
    b = []
    for i in a:
        b.append(i)


#   Time both implementations
time1 = timeit.timeit(code1, number=10_000_000)
time2 = timeit.timeit(code2, number=10_000_000)
time3 = timeit.timeit(code3, number=10_000_000)

print(f"Time1: {time1}")
print(f"Time2: {time2}")
print(f"Time2: {time3}")


## 7. chain
from itertools import chain
import timeit

#   List addition
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined_add = list1 + list2  # Immediate and memory-intensive

# itertools.chain
combined_chain = list(chain(list1, list2))  # Lazy and efficient

print(combined_add)
print(combined_chain)
