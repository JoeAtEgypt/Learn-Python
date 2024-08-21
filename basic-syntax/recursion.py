# When you call a function in Python, the interpreter creates a new local namespace so that names defined
# within that function don’t collide with identical names defined elsewhere.

"""
When function() executes the first time, Python creates a namespace and assigns x the value 10 in that namespace.
Then function() calls itself recursively. The second time function() runs, the interpreter creates a second namespace,
 and assigns 10 to x there as well.
These two instances of the name x are distinct from each another and can coexist without clashing
because they are in separate namespaces.
"""


def function():
    x = 10
    function()


function()  # => RecursionError: maximum recursion depth exceeded


from sys import getrecursionlimit

getrecursionlimit()  # => 1000

from sys import setrecursionlimit

setrecursionlimit(2000)
getrecursionlimit()  # => 2000


recursive_setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""
iterative_setup_string = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
"""
module_setup_string = "from math import factorial"

from timeit import timeit

print(timeit("factorial(4)", setup=recursive_setup_string, number=10_000_000))
print(timeit("factorial(4)", setup=iterative_setup_string, number=10_000_000))
print(timeit("factorial(4)", setup=module_setup_string, number=10_000_000))
